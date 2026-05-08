# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_wallsummon.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_wallsummon.pyc
# Source Generated with Decompyle++
# File: crt_wallsummon.pyc (Python 3.6)

from cl_only import Time2Frame, GAME_FRAME, GAME_FRAME_SECOND, Functor
from cl_commondefines import MODEL_TYPE_BOX, VICTIM_STATE_VALID, HITPART_DIRECTPOS, ATT_SHAPE_RECTANGLE, CRT_CHECK_CLIENT, CRT_CHECK_SERVER
from cl_pxlayer import PXMASK_LIVEOBJ, PXMASK_SKILLBLK, PXMASK_GROUNDBLK
import cl_math
import cl_modeldefine
import cl_gamedebug as debug
from .mobject import CBaseCartoon

class WallSummonCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        if 'Over' in dCartoon:
            return None
        oGame = oSkill.m_Game
        vPos = dCartoon['Start']
        oAttack = oSkill.GetAttack()
        iSrcPerform = oSkill.m_Base['pfid']
        clsSummonData = oGame.m_ResMgr.m_WarData.GetSummonData(dCartoon['SummonSID'])
        iShape = clsSummonData.m_Shape
        vBox = cl_modeldefine.GetModelDefine(iShape, 'Box')
        tEuler = cl_math.Dir2Radians(dCartoon['Dir'])
        vAngle = cl_math.Radians2Angle(tEuler)
        dAddInfo = {
            'Owner': oSkill.m_Base['AID'],
            'Shape': MODEL_TYPE_BOX,
            'ObjShape': iShape,
            'ClientOwner': oAttack.m_ID if oSkill.m_CheckType & CRT_CHECK_CLIENT else 0,
            'Angle': vAngle,
            'Origin': vPos,
            'NeglectAttack': False,
            'SrcPerform': iSrcPerform,
            'Center': (0, vBox[1] * 0.5, 0) if vBox else (0, 0, 0),
            'Scale': dCartoon['Scale'],
            'Size': vBox if vBox else (1, 1, 1),
            'Side': oSkill.m_Cache['Side'] }
        oSummon = clsSummonData.Create(oGame, dAddInfo)
        if oSummon:
            if 'ClientSummonId' in dCartoon:
                oSummon.m_ClientSummonID = dCartoon['ClientSummonId']
                oAttack.SetClientSummon(dCartoon['ClientSummonId'], oSummon.m_ID)
            oSummon.Goto(oSkill.m_Base['Scene'], dCartoon['Start'], dCartoon['Dir'])
            dCartoon['SummonID'] = oSummon.m_ID
            dCartoon['Radius'] = oSummon.m_ModelData.GetModelRadius()
        oSkill.Call_Out(1, dCartoon['ID'])
        iTimeoutFrame = dCartoon['LiveFrame'] + GAME_FRAME * 5
        dCartoon['OverFrame'] = dCartoon['StartFrame'] + iTimeoutFrame
        oSkill.AddEndFunc(Functor(ClearCartoon, dCartoon))
        oSkill.Call_Out(iTimeoutFrame, dCartoon['ID'])
        cls.Update(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def IsOver(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        iOver = 0
        if 'Over' in dCartoon:
            iOver = 1
        if iOver:
            if 'SummonID' in dCartoon:
                oSummon = oSkill.m_Game.GetObject(dCartoon['SummonID'])
                if oSummon:
                    oSummon.Remove('Over')
            dCartoon['Final'] = dCartoon['CurPos']
            oSkill.Send(iNodeID, {
                'Over': 1 })
            return 1
        return 0

    IsOver = classmethod(IsOver)
    
    def Restart(cls, oSkill, dCartoon):
        if 'TimerUpdate' not in dCartoon:
            return None
        dCartoon.pop('TimerUpdate')
        vCur = dCartoon['CurPos']
        vDir = dCartoon['Dir']
        vTar = cl_math.Vec3Mad(vCur, vDir, dCartoon['SpeedPerFrame'])
        if cl_math.CheckDistance3D(dCartoon['Start'], vTar, dCartoon['Distance']):
            oGame = oSkill.m_Game
            if 'SummonID' in dCartoon:
                oSummon = oGame.GetObject(dCartoon['SummonID'])
                if not oSummon:
                    cls.Disable(oSkill, dCartoon)
                    return None
                oSummon.WalkTo(vTar)
            dCartoon['CurPos'] = vTar
            oSkill.Call_Out(1, dCartoon['ID'])
        elif oSkill.m_CheckType & CRT_CHECK_SERVER:
            cls.Disable(oSkill, dCartoon)

    Restart = classmethod(Restart)
    
    def InitTraceClient(cls, oSkill, dCartoon, vScale, iPierce, iSummon, fDistance, fSpeed, iLivetime, **kwargs):
        dCartoon['Scale'] = vScale
        dCartoon['SummonSID'] = iSummon
        dCartoon['Pierce'] = iPierce
        dCartoon['Distance'] = fDistance
        dCartoon['SpeedPerFrame'] = fSpeed * GAME_FRAME_SECOND
        dCartoon['LiveFrame'] = Time2Frame(iLivetime)
        dCartoon['TargetType'] = kwargs['targettype']
        iNodeID = dCartoon['ID']
        dClient = oSkill.m_NetReceive[iNodeID]
        dCartoon['End'] = dClient['End']
        dCartoon['Start'] = dClient['Start']
        dCartoon['Dir'] = cl_math.Vec3Normalize(cl_math.Vec3Minus(dCartoon['End'], dCartoon['Start']))
        dCartoon['LowestPoint'] = dClient['CheckStart']
        dCartoon['HighestPoint'] = dClient['Offset']
        oSkill.m_Collect['HighestPoint'] = dCartoon['HighestPoint']
        dCartoon['CurPos'] = dCartoon['Start']
        dCartoon['AllVLST'] = []
        dCartoon['AllHitInfo'] = []
        dCartoon['ClientSummonId'] = dClient['ClientSummonId']
        dNet = {
            'End': dCartoon['End'] }
        if 'MuzzlePos' not in dCartoon or dCartoon['MuzzlePos'] != dCartoon['Start']:
            dNet['Start'] = dCartoon['Start']
        if 'Over' in dClient:
            dCartoon['Over'] = 1
            dNet['Over'] = 1
        oSkill.Send(dCartoon['ID'], dNet)

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            if dCartoon['LiveFrame'] > 0 and dCartoon['OverFrame'] < oSkill.m_Game.GetFrameNum():
                dCartoon['Over'] = 1
            else:
                dCartoon['TimerUpdate'] = 1
            return 0
        iHit = 0
        dClient = oSkill.m_NetReceive[iNodeID]
        if 'Ray' in dClient and dCartoon['Pierce'] > 0:
            dNet = { }
            iHit = 1
            lstVLST = []
            lstSend = []
            lstHitInfo = []
            for vHitPos, vNormal, iVictim, iHitPart in dClient['Ray']:
                iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
                if iVictimState == VICTIM_STATE_VALID:
                    dCartoon['Pierce'] -= cls.GetVictimPierceCost(oSkill, iVictim)
                    dCartoon['AllVLST'].append(iVictim)
                    lstVLST.append(iVictim)
                    dHitInfo = {
                        'Victim': iVictim,
                        'HitPos': vHitPos,
                        'HitArea': iHitPart }
                    lstHitInfo.append(dHitInfo)
                    dCartoon['AllHitInfo'].append(dHitInfo)
                    lstSend.append((vHitPos, vNormal, iVictim, iHitPart))
                
                if dCartoon['Pierce'] <= 0:
                    break
            
            oSkill.m_Update['HitInfo'] = lstHitInfo
            oSkill.m_Update['LastVLST'] = lstVLST
            dNet['Ray'] = lstSend
            oSkill.Send(dCartoon['ID'], dNet)
        cls.CollectSkillInfo(oSkill, dCartoon)
        if 'Trigger' in dClient:
            cls.Trigger(oSkill)
        if 'Over' in dClient:
            dCartoon['Over'] = 1
        return iHit

    HitTargetClient = classmethod(HitTargetClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, vStart, vShowStart, vEnd, vScale, iPierce, iSummon, fDistance, fSpeed, iLivetime, **kwargs):
        dCartoon['End'] = vEnd
        dCartoon['Start'] = vStart
        dCartoon['Dir'] = cl_math.Vec3Normalize(cl_math.Vec3Minus(dCartoon['End'], dCartoon['Start']))
        dCartoon['Scale'] = vScale
        dCartoon['SummonSID'] = iSummon
        dCartoon['Pierce'] = iPierce
        dCartoon['Distance'] = fDistance
        dCartoon['SpeedPerFrame'] = fSpeed * GAME_FRAME_SECOND
        dCartoon['LiveFrame'] = Time2Frame(iLivetime)
        dCartoon['TargetType'] = kwargs['targettype']
        oGame = oSkill.m_Game
        iScene = oSkill.m_Base['Scene']
        vCheckStart = (vStart[0], vStart[1] + vScale[1] * 0.5, vStart[2])
        vCheckEnd = (vEnd[0], vEnd[1] + vScale[1] * 0.5, vEnd[2])
        fGroundDis = oGame.Scene_GroundDistance(iScene, vCheckStart, 15, PXMASK_GROUNDBLK)
        vLowestPoint = (vCheckStart[0], vCheckStart[1] + 0.2 - fGroundDis, vCheckStart[2])
        vRet = oGame.Scene_RaycastSingle(iScene, vCheckStart, vCheckEnd, PXMASK_SKILLBLK)
        if vRet[0] != -1:
            vHighestPoint = vRet[1]
        else:
            vHighestPoint = cl_math.Vec3DisplaceDir(vCheckStart, dCartoon['Dir'], fDistance)
        dCartoon['LowestPoint'] = vLowestPoint
        dCartoon['HighestPoint'] = vHighestPoint
        oSkill.m_Collect['HighestPoint'] = dCartoon['HighestPoint']
        dCartoon['CurPos'] = dCartoon['Start']
        dCartoon['AllVLST'] = []
        dCartoon['AllHitInfo'] = []
        dNet = {
            'End': dCartoon['End'] }
        if 'MuzzlePos' not in dCartoon or dCartoon['MuzzlePos'] != dCartoon['Start']:
            dNet['Start'] = dCartoon['Start']
        oSkill.Send(dCartoon['ID'], dNet)

    InitTraceServer = classmethod(InitTraceServer)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        if dCartoon['LiveFrame'] > 0 and dCartoon['OverFrame'] < oSkill.m_Game.GetFrameNum():
            dCartoon['Over'] = 1
            return 0
        dCartoon['TimerUpdate'] = 1
        lstVictim = cls.GetAllTarget(oSkill, dCartoon)
        if not lstVictim:
            return 0
        lstHitInfo = []
        for iVictim in lstVictim:
            dHitInfo = {
                'Victim': iVictim,
                'HitArea': HITPART_DIRECTPOS }
            lstHitInfo.append(dHitInfo)
        
        oSkill.m_Update['LastVLST'] = lstVictim
        oSkill.m_Update['HitInfo'] = lstHitInfo
        cls.CollectSkillInfo(oSkill, dCartoon)
        dNet = {
            'LastVLST': lstVictim }
        oSkill.Send(dCartoon['ID'], dNet)
        return 1

    HitTargetServer = classmethod(HitTargetServer)
    
    def GetAllTarget(cls, oSkill, dCartoon):
        oGame = oSkill.m_Game
        lstTarget = []
        if 'SummonID' in dCartoon:
            oSummon = oGame.GetObject(dCartoon['SummonID'])
            vSummon = oSummon.GetPos()
            vDir = dCartoon['Dir']
            (fLength, fWidth, fHeight) = dCartoon['Scale']
            vPos = cl_math.Vec3DisplacePos(vSummon, (0, 1, 0), fHeight * 0.5)
            if oGame.m_WarMgr.Query('DebugRay'):
                debug.ClearDebugLine(oGame, debug.LINE_BOX)
                debug.DebugBox(oGame, vPos, vDir, fLength, fWidth, fHeight)
            lstArgs = [
                vPos,
                vDir,
                fLength,
                fWidth,
                fHeight]
            lstHit = cl_math.GetAttackTargetList(oGame, oSkill.m_Base['Scene'], ATT_SHAPE_RECTANGLE, lstArgs, {
                'Mask': PXMASK_LIVEOBJ,
                'BlockMask': 0 })
            for iVictim in lstHit:
                iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
                if iVictimState == VICTIM_STATE_VALID:
                    dCartoon['AllVLST'].append(iVictim)
                    lstTarget.append(iVictim)
            
        return lstTarget

    GetAllTarget = classmethod(GetAllTarget)
    
    def CollectSkillInfo(cls, oSkill, dCartoon):
        lstCartoonPos = oSkill.m_Collect['CartoonPos'] if 'CartoonPos' in oSkill.m_Collect else []
        vStart = dCartoon['Start']
        if 'Final' in dCartoon:
            vEnd = dCartoon['Final']
        elif 'Radius' in dCartoon:
            pass
        
        fRadius = 0
        vEnd = dCartoon['CurPos'] if fRadius == 0 else cl_math.Vec3Mad(dCartoon['CurPos'], dCartoon['Dir'], fRadius)
        lstCartoonPos.append((vStart, vEnd))
        oSkill.m_Collect['CartoonPos'] = lstCartoonPos
        oSkill.m_Collect['lstVLST'] = dCartoon['AllVLST']

    CollectSkillInfo = classmethod(CollectSkillInfo)


def ClearCartoon(dCartoon, oSkill):
    if 'SummonID' in dCartoon:
        iSummonID = dCartoon.pop('SummonID')
        oSummon = oSkill.m_Game.GetObject(iSummonID)
        if oSummon:
            oSummon.ScenesRemoveDelay('CartoonOver')

