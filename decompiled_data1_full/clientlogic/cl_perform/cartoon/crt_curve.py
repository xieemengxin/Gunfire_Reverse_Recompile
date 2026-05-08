# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_curve.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_curve.pyc
# Source Generated with Decompyle++
# File: crt_curve.pyc (Python 3.6)

from cl_only import PY_FLAG_DEAD, GAME_FRAME_SECOND, GAME_FRAME
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ALL, MONSTER_PART_UNTAGGED, VICTIM_STATE_BLOCK, VICTIM_STATE_VALID, SIDE_TYPE_HERO, WARRIOR_BUILD, OBSTACLE_CURVEIGNORE
from cl_pxlayer import PXMASK_SKILLBLK, PXMASK_LIVEOBJ, PXMASK_SIDEBLK, PXMASK_BOX
import cl_math
import cl_gamedebug as debug
from .mobject import CBaseCartoon

class CurveCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        cls.Update(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def Restart(cls, oSkill, dCartoon):
        if oSkill.m_CheckType & CRT_CHECK_SERVER:
            oSkill.Call_Out(1, dCartoon['ID'])

    Restart = classmethod(Restart)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        return 0

    HitTargetClient = classmethod(HitTargetClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, StartPos, EndPos, iPierce, fDistance, fSpeed, iAnglePerSecond, fHeightRatio, targettype = OBJ_ALL, pierceblock = False, effect = 0, hittarger = False, iVictim = 0, lockPos = (0, 0, 0), bLockDeadPos = False, *args, **kwargs):
        dCartoon['Start'] = StartPos
        dCartoon['End'] = EndPos
        dCartoon['Pierce'] = iPierce
        dCartoon['Distance'] = fDistance
        dCartoon['SpeedPerFrame'] = fSpeed * GAME_FRAME_SECOND
        dCartoon['AnglePerFrame'] = iAnglePerSecond // GAME_FRAME
        dCartoon['HeightRatio'] = fHeightRatio
        dCartoon['TargetType'] = targettype
        dCartoon['CurPos'] = StartPos
        dCartoon['PierceBlock'] = pierceblock
        dCartoon['HitTarget'] = hittarger
        dCartoon['Victim'] = iVictim
        dCartoon['LockTarget'] = oSkill.m_Base['VID']
        dCartoon['Dir'] = cl_math.Vec3Normalize(cl_math.Vec3Minus(dCartoon['End'], dCartoon['Start']))
        dCartoon['LockPos'] = lockPos
        dCartoon['LockDeadPos'] = bLockDeadPos
        dCartoon['LockDir'] = 0
        dNet = {
            'Start': dCartoon['Start'],
            'End': dCartoon['End'],
            'SpeedVector': dCartoon['Dir'],
            'LockTarget': [
                oSkill.m_Base['VID']] }
        oSkill.Send(dCartoon['ID'], dNet)

    InitTraceServer = classmethod(InitTraceServer)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        oGame = oSkill.m_Game
        vCur = dCartoon['CurPos']
        vPreDir = dCartoon['Dir']
        vNewDir = vPreDir
        oLockTarget = oGame.GetObject(dCartoon['LockTarget'], PY_FLAG_DEAD)
        if oLockTarget:
            (x, y, z) = oLockTarget.GetPos()
            vTarget = (x, y + oLockTarget.m_ModelHeight * dCartoon['HeightRatio'], z)
        elif not cl_math.IsZero(dCartoon['LockPos']):
            vTarget = dCartoon['LockPos']
            if dCartoon['LockDeadPos'] and not dCartoon['LockDir']:
                dCartoon['LockDir'] = 1
                dCartoon['Dir'] = cl_math.Vec3Normalize(cl_math.Vec3Minus(vTarget, vCur))
            else:
                vTarget = None
        if None and not dCartoon['LockDir']:
            vDir = cl_math.Vec3Minus(vTarget, vCur)
            tAxis = cl_math.Vec3Normalize(cl_math.VectorCross3D(vPreDir, vDir))
            iAngle = cl_math.CalAngle3D(vPreDir, vDir)
            if iAngle:
                iAngle = min(dCartoon['AnglePerFrame'], iAngle)
                vNewDir = cl_math.Vec3Normalize(cl_math.RotateAroundVector(vPreDir, tAxis, iAngle))
                dCartoon['Dir'] = vNewDir
        vTar = cl_math.Vec3Mad(vCur, vNewDir, dCartoon['SpeedPerFrame'])
        iAttack = oSkill.m_Base['AID']
        if oSkill.m_Cache['Side'] != SIDE_TYPE_HERO:
            iBlockMask = PXMASK_SIDEBLK
        else:
            iBlockMask = PXMASK_SKILLBLK
        iPierceBlock = dCartoon['PierceBlock']
        if iPierceBlock:
            iMask = PXMASK_LIVEOBJ
            iBlockMask |= PXMASK_BOX
        else:
            iMask = PXMASK_SKILLBLK | PXMASK_LIVEOBJ
        lstVictim = oGame.Scene_RaycastMultiple(oSkill.m_Base['Scene'], vCur, vTar, iMask, {
            'PassID': iAttack,
            'BlockMask': iBlockMask,
            'ExcludeFlag': PY_FLAG_DEAD })
        if oGame.m_WarMgr.Query('DebugRay'):
            (ox, oy, oz) = vCur
            (tx, ty, tz) = vTar
            debug.DebugLine(oGame, ox, oy, oz, tx, ty, tz, 65280, debug.LINE_TILE)
        if not lstVictim and dCartoon['LockDir'] and vTarget and cl_math.CalDistance(vCur, vTarget) <= dCartoon['SpeedPerFrame']:
            lstVictim = [
                (0, {
                    'Pos': vTarget })]
        lstNewVictim = []
        iTrigger = oSkill.m_Custom['LockTrigger'] if 'LockTrigger' in oSkill.m_Custom else dCartoon['Victim']
        iChooseSelf = 0
        if 'ChooseSelf' in oSkill.m_Custom:
            iChooseSelf = oSkill.m_Custom['ChooseSelf']
        for iVictim, dHit in lstVictim:
            if iPierceBlock:
                oVictim = oGame.GetObject(iVictim, PY_FLAG_DEAD)
                if oVictim and oVictim.m_FightType & WARRIOR_BUILD and OBSTACLE_CURVEIGNORE in oVictim.m_ClassifyList:
                    continue
                continue
            if iTrigger and iTrigger == iVictim and not iChooseSelf:
                continue
            if dCartoon['HitTarget'] and oLockTarget and oLockTarget.m_ID != iVictim:
                continue
            lstNewVictim.append((iVictim, dHit))
        
        if oSkill.m_Base['pid']:
            lstNewVictim = cls.PreProcessVictimList(oSkill, dCartoon, lstNewVictim)
        if not lstNewVictim:
            dCartoon['CurPos'] = vTar
            return 0
        lstVLST = []
        lstSend = []
        for iVictim, dHit in lstNewVictim:
            iVitcimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
            if iVitcimState == VICTIM_STATE_BLOCK:
                dCartoon['CurPos'] = dHit['Pos']
                oSkill.m_Update['HitStatic'] = 1
                dCartoon['Pierce'] = 0
                lstSend.append((dHit['Pos'], (0, 0, 0), iVictim, MONSTER_PART_UNTAGGED))
            elif iVitcimState == VICTIM_STATE_VALID:
                dCartoon['CurPos'] = dHit['Pos']
                dCartoon['Pierce'] -= cls.GetVictimPierceCost(oSkill, iVictim)
                lstVLST.append(iVictim)
                lstSend.append((dHit['Pos'], (0, 0, 0), iVictim, MONSTER_PART_UNTAGGED))
            
            if dCartoon['Pierce'] <= 0:
                dCartoon['Final'] = dHit['Pos']
                break
        
        if not lstVLST:
            dCartoon['CurPos'] = vTar
            return 0
        oSkill.m_Update['LastVLST'] = lstVLST
        dNet = {
            'Ray': lstSend,
            'HitStatic': oSkill.m_Update['HitStatic'] if 'HitStatic' in oSkill.m_Update else 0 }
        oSkill.Send(dCartoon['ID'], dNet)
        cls.CollectSkillInfo(oSkill, dCartoon)
        return 1

    HitTargetServer = classmethod(HitTargetServer)
    
    def IsOver(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        iOver = 0
        if dCartoon['Pierce'] <= 0:
            iOver = 1
        elif (oSkill.m_Game.GetFrameNum() - dCartoon['StartFrame']) * dCartoon['SpeedPerFrame'] > dCartoon['Distance']:
            iOver = 1
            dCartoon['Final'] = dCartoon['CurPos']
            cls.CollectSkillInfo(oSkill, dCartoon)
        if iOver:
            vEnd = dCartoon['Final'] if 'Final' in dCartoon else dCartoon['CurPos']
            oSkill.Send(iNodeID, {
                'Over': 1,
                'End': vEnd })
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

