# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_entitycurve.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_entitycurve.pyc
# Source Generated with Decompyle++
# File: crt_entitycurve.pyc (Python 3.6)

from cl_only import GAME_FRAME_SECOND, GAME_FRAME, Functor, PY_FLAG_DEAD, GAME_GRAVITY
from cl_commondefines import CRT_CHECK_SERVER, MODEL_TYPE_SPHERE, OBJ_ALL, VICTIM_STATE_BLOCK, VICTIM_STATE_VALID
from cl_pxlayer import PXLAYER_RBULLET
import cl_math
import cl_scene
import cl_engphyobj
import cl_gamedebug as debug
from .mobject import CBaseCartoon

class EntityCurveCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        if oSkill.m_CheckType & CRT_CHECK_SERVER:
            oGame = oSkill.m_Game
            vPos = dCartoon['Start']
            fRadius = dCartoon['Radius']
            if 'SummonID' not in dCartoon:
                dAddInfo = {
                    'Owner': oSkill.m_Base['AID'],
                    'Shape': MODEL_TYPE_SPHERE,
                    'Angle': (0, 0, 0),
                    'Center': vPos,
                    'Scale': (1, 1, 1),
                    'Size': (fRadius, fRadius, fRadius),
                    'Side': oSkill.m_Cache['Side'],
                    'Origin': vPos }
                iScene = oSkill.m_Base['Scene']
                if dCartoon['SummonSID']:
                    oSummon = oGame.m_ResMgr.CreateSummon(iScene, dCartoon['SummonSID'], dAddInfo)
                    if oSummon:
                        iSummon = oSummon.m_ID
                    else:
                        iSummon = 0
                        dCartoon['Over'] = 1
                else:
                    oSummon = None
                    iSummon = 0
                oGame = oSkill.m_Game
                dCartoon['SummonID'] = iSummon
            else:
                oSummon = oGame.GetObject(dCartoon['SummonID'])
            if oSummon:
                oSummon.Set('CartoonUse', 1)
                oBullet = cl_engphyobj.CreateAttachBullet(oGame, oSummon, {
                    'TraceIdx': oSkill.m_Base['PFKey'],
                    'PassID': oSkill.m_Base['AID'] }, PXLAYER_RBULLET, {
                    'Shape': MODEL_TYPE_SPHERE,
                    'Radius': fRadius })
                oBullet.SetBulletSpeed((0, 0, 0))
                oBullet.SetBulletAccSpeed((0, -GAME_GRAVITY, 0))
                oGame.m_SkillMgr.RegisterBullet(oBullet, oSkill.m_Base['AID'], oSkill.m_Base['ActNum'], dCartoon['ID'])
                dCartoon['BulletKey'] = oBullet.Key()
                oSkill.AddEndFunc(Functor(ClearCartoon, dCartoon))
            cls.Update(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def Restart(cls, oSkill, dCartoon):
        if oSkill.m_CheckType & CRT_CHECK_SERVER:
            oGame = oSkill.m_Game
            iSummonID = dCartoon['SummonID']
            if iSummonID:
                oSummon = oGame.GetObject(iSummonID)
                oSummon.RefreshPos()
                cl_scene.GS2CMapGoto(oSummon, oSummon.GetPos())
            oBullet = oGame.m_SkillMgr.GetBullet(dCartoon['BulletKey'])
            vCur = oBullet.GetBulletPosition()
            if oGame.m_WarMgr.Query('DebugRay'):
                (ox, oy, oz) = dCartoon['CurPos']
                (tx, ty, tz) = vCur
                debug.DebugLine(oSkill.m_Game, ox, oy, oz, tx, ty, tz, 65280, debug.LINE_TILE)
            dCartoon['CurPos'] = vCur
            dCartoon['Final'] = vCur
            vPreDir = dCartoon['Dir']
            vNewDir = vPreDir
            oLockTarget = oGame.GetObject(dCartoon['LockTarget'], dCartoon['PyFlag'])
            if oLockTarget:
                (x, y, z) = oLockTarget.GetPos()
                vTarget = (x, y + oLockTarget.m_ModelHeight * dCartoon['HeightRatio'], z)
                vDir = cl_math.Vec3Minus(vTarget, vCur)
                tAxis = cl_math.Vec3Normalize(cl_math.VectorCross3D(vPreDir, vDir))
                iAngle = cl_math.CalAngle3D(vPreDir, vDir)
                if iAngle:
                    iAngle = min(dCartoon['AnglePerFrame'], iAngle)
                    vNewDir = cl_math.Vec3Normalize(cl_math.RotateAroundVector(vPreDir, tAxis, iAngle))
                    dCartoon['Dir'] = vNewDir
            vSpeed = cl_math.Vec3MulF(vNewDir, dCartoon['Speed'])
            oBullet.SetBulletSpeed(vSpeed)
            oSkill.Call_Out_NoSuspend(1, dCartoon['ID'])

    Restart = classmethod(Restart)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        return 0

    HitTargetClient = classmethod(HitTargetClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, StartPos, EndPos, Radius, iSummon, fDistance, fSpeed, iAnglePerSecond, fHeightRatio, targettype = OBJ_ALL, summonID = 0, forceDel = False, iPyFlag = PY_FLAG_DEAD, **kwargs):
        dCartoon['End'] = EndPos
        dCartoon['Distance'] = fDistance
        dCartoon['Speed'] = fSpeed
        dCartoon['AnglePerFrame'] = iAnglePerSecond // GAME_FRAME
        dCartoon['HeightRatio'] = fHeightRatio
        dCartoon['TargetType'] = targettype
        dCartoon['CurPos'] = StartPos
        dCartoon['Start'] = StartPos
        dCartoon['SummonSID'] = iSummon
        dCartoon['Radius'] = Radius
        dCartoon['InitSummon'] = 0
        dCartoon['ForceDel'] = forceDel
        dCartoon['PyFlag'] = iPyFlag
        if summonID:
            oSummon = oSkill.m_Game.GetObject(summonID)
            if not oSummon:
                dCartoon['Over'] = 1
                dCartoon['SummonID'] = 0
            else:
                dCartoon['Start'] = oSummon.GetPos()
                dCartoon['SummonSID'] = oSummon.m_SID
                dCartoon['Radius'] = oSummon.m_ModelRadius
                dCartoon['SummonID'] = summonID
                dCartoon['InitSummon'] = summonID
        dCartoon['Dir'] = cl_math.Vec3Normalize(cl_math.Vec3Minus(dCartoon['End'], dCartoon['Start']))
        dCartoon['LockTarget'] = oSkill.m_Base['VID']
        dNet = {
            'Start': dCartoon['Start'],
            'End': dCartoon['End'],
            'LockTarget': [
                dCartoon['LockTarget']] }
        oSkill.Send(dCartoon['ID'], dNet)

    InitTraceServer = classmethod(InitTraceServer)
    
    def AddHitTarget(cls, oSkill, dCartoon, iTarget, dHit):
        if 'Over' in dCartoon:
            return None
        dHit['Victim'] = iTarget
        dCartoon['BulletHit'] = dHit

    AddHitTarget = classmethod(AddHitTarget)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        dNet = { }
        iHit = 0
        if 'BulletHit' in dCartoon:
            iHit = 1
            dHit = dCartoon['BulletHit']
            dCartoon.pop('BulletHit')
            iTarget = dHit['Victim']
            iVictimState = cls.CheckVictimState(oSkill, dCartoon, iTarget)
            bValidHit = True
            if iVictimState == VICTIM_STATE_BLOCK:
                iTarget = 0
                oSkill.m_Update['HitStatic'] = 1
            elif iVictimState == VICTIM_STATE_VALID:
                lstVLST = oSkill.m_Update['LastVLST'] if 'LastVLST' in oSkill.m_Update else []
                lstVLST.append(iTarget)
                oSkill.m_Update['LastVLST'] = lstVLST
            else:
                bValidHit = False
            if bValidHit:
                dNet['Ray'] = [
                    (dHit['hitpos'], dHit['normal'], iTarget, 0)]
                dCartoon['Over'] = 1
        dNet['End'] = dCartoon['CurPos']
        oSkill.Send(dCartoon['ID'], dNet)
        return iHit

    HitTargetServer = classmethod(HitTargetServer)
    
    def IsOver(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        dNet = { }
        iOver = 0
        if 'Over' in dCartoon:
            iOver = 1
        oGame = oSkill.m_Game
        if (oGame.GetFrameNum() - dCartoon['StartFrame']) * dCartoon['Speed'] * GAME_FRAME_SECOND > dCartoon['Distance']:
            cls.Trigger(oSkill)
            dNet['Trigger'] = 1
            iOver = 1
        if 'SummonID' in dCartoon and dCartoon['SummonID'] and not oGame.GetObject(dCartoon['SummonID']):
            iOver = 1
        if iOver:
            dCartoon['Final'] = dCartoon['CurPos']
            cls.CollectSkillInfo(oSkill, dCartoon)
            ClearCartoon(dCartoon, oSkill)
            dNet['Over'] = 1
            oSkill.Send(iNodeID, dNet)
            return 1
        return 0

    IsOver = classmethod(IsOver)
    
    def CollectSkillInfo(cls, oSkill, dCartoon):
        lstCartoonPos = oSkill.m_Collect['CartoonPos'] if 'CartoonPos' in oSkill.m_Collect else []
        vStart = dCartoon['Start']
        vEnd = dCartoon['Final'] if 'Final' in dCartoon else dCartoon['CurPos']
        lstCartoonPos.append((vStart, vEnd))
        oSkill.m_Collect['CartoonPos'] = lstCartoonPos

    CollectSkillInfo = classmethod(CollectSkillInfo)


def ClearCartoon(dCartoon, oSkill):
    dCartoon['cls'].ClearCartoonBullet(oSkill, dCartoon)
    if dCartoon['InitSummon'] and not dCartoon['ForceDel']:
        return None
    if 'SummonID' in dCartoon:
        iSummonID = dCartoon.pop('SummonID')
        oSummon = oSkill.m_Game.GetObject(iSummonID)
        if oSummon:
            oSummon.ScenesRemoveDelay('CartoonOver')

