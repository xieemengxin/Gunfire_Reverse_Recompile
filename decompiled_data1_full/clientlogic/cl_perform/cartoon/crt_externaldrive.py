# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_externaldrive.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_externaldrive.pyc
# Source Generated with Decompyle++
# File: crt_externaldrive.pyc (Python 3.6)

from cl_only import GAME_FRAME, Functor
from cl_msgcenter.defines import MSG_WAR_TRIGGER_EXTERNALDRIVE
import cl_msgcenter
from .mobject import CBaseCartoon

class ExternalDriveCartoon(CBaseCartoon):
    m_NeedCtrlNet = 0
    
    def Trace(cls, oSkill, dCartoon):
        if 'Over' in dCartoon:
            cls.Disable(oSkill, dCartoon)
            return None
        oSkill.Call_Out(GAME_FRAME * dCartoon['ClearTime'], dCartoon['ID'])

    Trace = classmethod(Trace)
    
    def InitTraceClient(cls, oSkill, dCartoon, iCurHitID, iCurHitArea, iClearTime, *args, **kwargs):
        if not iCurHitID:
            dCartoon['Over'] = 1
            oSkill.Send(dCartoon['ID'], {
                'Over': 1 })
            lstLastVLST = oSkill.m_Update['LastVLST'] if 'LastVLST' in oSkill.m_Update else []
            iCurVID = oSkill.m_Update['CurVID'] if 'CurVID' in oSkill.m_Update else 0
            oSkill.LogCheckErr('drive %s %s' % (lstLastVLST, iCurVID))
            return None
        oGame = oSkill.m_Game
        dCartoon['CurHitID'] = iCurHitID
        dCartoon['CurHitArea'] = iCurHitArea
        oVictim = oGame.GetObject(iCurHitID)
        dCartoon['Start'] = oVictim.GetPos()
        dCartoon['ClearTime'] = iClearTime
        dCartoon['CurPos'] = oVictim.GetPos()
        cls.CollectSkillInfo(oSkill, dCartoon)

    InitTraceClient = classmethod(InitTraceClient)
    
    def IsOver(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if 'Over' in dCartoon:
            dNet = {
                'Over': 1 }
            oSkill.Send(iNodeID, dNet)
            return 1
        return 0

    IsOver = classmethod(IsOver)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        if dCartoon['StartFrame'] + GAME_FRAME * dCartoon['ClearTime'] <= oSkill.m_Game.GetFrameNum():
            dCartoon['Over'] = 1
            return 0
        if 'Victim' not in dCartoon:
            dCartoon['Over'] = 1
            return 0
        oVictim = oSkill.m_Game.GetObject(dCartoon['Victim'])
        if not oVictim:
            dCartoon['Over'] = 1
            return 0
        lstVLST = [
            dCartoon['Victim']]
        dHitInfo = {
            'Victim': dCartoon['Victim'],
            'HitPos': oVictim.GetPos(),
            'HitArea': dCartoon['CurHitArea'] }
        oSkill.m_Update['HitInfo'] = [
            dHitInfo]
        oSkill.m_Update['LastVLST'] = lstVLST
        dCartoon['CurPos'] = oVictim.GetPos()
        dCartoon['Final'] = oVictim.GetPos()
        dCartoon['Over'] = 1
        return 1

    HitTargetClient = classmethod(HitTargetClient)
    
    def AddHitTarget(cls, oSkill, dCartoon, iTarget, dHit):
        if 'Over' in dCartoon:
            return None
        dCartoon['Victim'] = iTarget

    AddHitTarget = classmethod(AddHitTarget)
    
    def CollectSkillInfo(cls, oSkill, dCartoon):
        dHitInfo = oSkill.m_Collect['HitTimesInfo'] if 'HitTimesInfo' in oSkill.m_Collect else { }
        iCurHitID = dCartoon['CurHitID']
        if iCurHitID in dHitInfo:
            dHitInfo[iCurHitID] += 1
        else:
            dHitInfo[iCurHitID] = 1
        oSkill.m_Collect['HitTimesInfo'] = dHitInfo

    CollectSkillInfo = classmethod(CollectSkillInfo)
    
    def InitTraceServer(cls, oSkill, dCartoon, iCurHitID, iCurHitArea, iClearTime, *args, **kwargs):
        dCartoon['ClearTime'] = iClearTime
        oSkill.Send(dCartoon['ID'], { })
        oAttack = oSkill.GetAttack()
        iSkill = oSkill.m_Base['ActNum']
        iCartoonID = dCartoon['ID']
        sKey = oSkill.m_Base['PFKey']
        cl_msgcenter.AddFunction(oAttack, MSG_WAR_TRIGGER_EXTERNALDRIVE, Functor(TriggerExternalCB, iSkill, iCartoonID, sKey), sKey)

    InitTraceServer = classmethod(InitTraceServer)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        if dCartoon['StartFrame'] + GAME_FRAME * dCartoon['ClearTime'] <= oSkill.m_Game.GetFrameNum():
            dCartoon['Over'] = 1
            oAttack = oSkill.GetAttack()
            cl_msgcenter.DoneEvent(oAttack, MSG_WAR_TRIGGER_EXTERNALDRIVE, oSkill.m_Base['PFKey'])
            return 0
        cls.Trigger(oSkill)
        dCartoon['Over'] = 1
        dNet = {
            'Trigger': 1 }
        oSkill.Send(dCartoon['ID'], dNet)
        return 1

    HitTargetServer = classmethod(HitTargetServer)


def TriggerExternalCB(iSkill, iCartoonID, sKey, oAttack, dInfo):
    cl_msgcenter.DoneEvent(oAttack, MSG_WAR_TRIGGER_EXTERNALDRIVE, sKey)
    iVictim = dInfo['iVictim']
    oGame = oAttack.m_Game
    oVictim = oGame.GetObject(iVictim)
    oSkill = oGame.m_SkillMgr.GetSkill(oAttack.m_ID, iSkill)
    if not oSkill:
        return None
    if oVictim:
        vPos = oVictim.GetPos()
        vPos = (vPos[0], vPos[1] + oVictim.m_ModelHeight * 0.5, vPos[2])
    else:
        vPos = (0, 0, 0)
    oSkill.m_VarCache['HitPos'] = vPos
    oSkill.Call_Out(1, iCartoonID)

