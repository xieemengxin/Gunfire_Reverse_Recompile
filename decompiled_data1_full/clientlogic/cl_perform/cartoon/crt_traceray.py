# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_traceray.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_traceray.pyc
# Source Generated with Decompyle++
# File: crt_traceray.pyc (Python 3.6)

from cl_only import Second2Frame, PY_FLAG_DEAD, GAME_FRAME_SECOND, GAME_FRAME
from cl_commondefines import OBJ_ALL, SIDE_TYPE_HERO, MONSTER_PART_UNTAGGED, VICTIM_STATE_BLOCK, VICTIM_STATE_VALID, VICTIM_STATE_HIT, VICTIM_STATE_NOEXIST
from cl_pxlayer import PXMASK_SKILLBLK, PXMASK_LIVEOBJ, PXMASK_SIDEBLK
import cllib.lib_cartoon as cartooncheck
import cl_math
import cl_gamedebug as debug
from .crt_raycast import RayCastCartoon

class TraceCartoon(RayCastCartoon):
    m_BaseTraceTimes = 1
    
    def InitTraceClient(cls, oSkill, dCartoon, iPierce, fDistance, fSpeed, targettype = OBJ_ALL, effect = 0, iIgnoreMonsterID = 0, traceTimes = 1, canLockMoreTimes = 0, *args, **kwargs):
        dCartoon['Pierce'] = iPierce
        dCartoon['Distance'] = fDistance
        dCartoon['SpeedPerFrame'] = fSpeed * GAME_FRAME_SECOND
        dCartoon['TargetType'] = targettype
        dCartoon['Radius'] = 0
        iNodeID = dCartoon['ID']
        dClient = oSkill.m_NetReceive[iNodeID]
        dCartoon['End'] = dClient['End']
        dCartoon['Start'] = dClient['Start']
        dCartoon['CurPos'] = dCartoon['Start']
        dCartoon['FilterDie'] = kwargs['FilterDie'] if 'FilterDie' in kwargs else True
        dCartoon['AllVLST'] = []
        dNet = {
            'End': dCartoon['End'] }
        if 'MuzzlePos' not in dCartoon or dCartoon['MuzzlePos'] != dCartoon['Start']:
            dNet['Start'] = dCartoon['Start']
        if 'LockTarget' in dClient:
            dNet['LockTarget'] = list(dClient['LockTarget'])
        if 'IgnoreStatic' in dClient:
            dNet['IgnoreStatic'] = dClient['IgnoreStatic']
        if 'Angle' in dClient:
            dNet['Angle'] = dClient['Angle']
        if 'Offset' in dClient:
            dNet['Offset'] = dClient['Offset']
        oSkill.Send(dCartoon['ID'], dNet)
        iFlyFrame = Second2Frame(fDistance / fSpeed)
        dCartoon['WaitNet'] = oSkill.GetWaitNetFrame(iFlyFrame)
        dCartoon['PierceStatic'] = True
        dCartoon['AllHitInfo'] = []
        dCartoon['IgnoremonsterID'] = iIgnoreMonsterID
        dCartoon['ArriveDoTrigger'] = kwargs['arriveDoTrigger'] if 'arriveDoTrigger' in kwargs else False
        dCartoon['CanLockMoreTimes'] = 0
        if traceTimes > cls.m_BaseTraceTimes:
            dCartoon['CheckTraceTimes'] = True
            dCartoon['TraceTimes'] = traceTimes
            dCartoon['CurTraceTimes'] = 0
            if canLockMoreTimes:
                dCartoon['CanLockMoreTimes'] = 1
            else:
                dCartoon['CheckTraceTimes'] = False

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return -1
        cartooncheck.CheckDataRayCast(oSkill, dCartoon)
        dClient = oSkill.m_NetReceive[iNodeID]
        dNet = { }
        if 'LockTarget' in dClient:
            dNet['LockTarget'] = list(dClient['LockTarget'])
        iHit = 0
        if 'Ray' in dClient and dCartoon['Pierce'] > 0:
            iHit = 1
            iNoCostPierce = 0
            oAttack = oSkill.GetAttack()
            iWeapon = oSkill.m_Base['Weapon']
            if iWeapon:
                oWeapon = oAttack.m_WieldCon.GetItemByID(iWeapon)
                iNoCostPierce = oWeapon.Query('NoCostPierce', 0) if oWeapon else 0
            bCostPierce = True
            if iNoCostPierce or 'Trigger' in dClient:
                bCostPierce = False
            lstRay = dClient['Ray']
            lstVLST = []
            lstSend = []
            lstHitInfo = []
            bFilterDie = dCartoon['FilterDie']
            for vHitPos, vNormal, iVictim, iHitPart in lstRay:
                if dCartoon['IgnoremonsterID'] and iVictim == dCartoon['IgnoremonsterID']:
                    continue
                iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
                if not cls.CheckValidDamage(dCartoon, iVictim, iHitPart):
                    pass
                bCheckHit = not bCostPierce
                if iVictimState == VICTIM_STATE_HIT:
                    if bCheckHit or dCartoon['CanLockMoreTimes']:
                        iVictimState = VICTIM_STATE_VALID
                if iVictimState == VICTIM_STATE_BLOCK:
                    lstSend.append((vHitPos, vNormal, 0, iHitPart))
                    oSkill.m_Update['HitStatic'] = 1
                    dNet['HitStatic'] = 1
                    dCartoon['Pierce'] = 0
                elif iVictimState == VICTIM_STATE_VALID:
                    if bCostPierce:
                        dCartoon['Pierce'] -= cls.GetVictimPierceCost(oSkill, iVictim)
                    dHitInfo = {
                        'Victim': iVictim,
                        'HitPos': vHitPos,
                        'HitArea': iHitPart }
                    dCartoon['AllVLST'].append(iVictim)
                    lstVLST.append(iVictim)
                    lstHitInfo.append(dHitInfo)
                    dCartoon['AllHitInfo'].append(dHitInfo)
                    lstSend.append((vHitPos, vNormal, iVictim, iHitPart))
                    if dCartoon['CheckTraceTimes']:
                        dCartoon['CurTraceTimes'] += 1
                        if dCartoon['CurTraceTimes'] == dCartoon['TraceTimes']:
                            dCartoon['Pierce'] = 0
                        elif not bFilterDie and iVictimState == VICTIM_STATE_NOEXIST:
                            dHitInfo = {
                                'Victim': iVictim,
                                'HitPos': vHitPos,
                                'HitArea': iHitPart }
                            dCartoon['AllVLST'].append(iVictim)
                            lstVLST.append(iVictim)
                            lstHitInfo.append(dHitInfo)
                            dCartoon['AllHitInfo'].append(dHitInfo)
                        
                dCartoon['CurPos'] = vHitPos
                if dCartoon['Pierce'] <= 0:
                    dCartoon['Final'] = vHitPos
                    break
            
            oSkill.m_Update['LastVLST'] = lstVLST
            oSkill.m_Update['HitInfo'] = lstHitInfo
            dNet['Ray'] = lstSend
            oSkill.Send(dCartoon['ID'], dNet)
        elif 'Trigger' in dClient and dCartoon['ArriveDoTrigger']:
            cls.Trigger(oSkill)
            dNet['Trigger'] = dClient['Trigger']
        oSkill.Send(dCartoon['ID'], dNet)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, StartPos, EndPos, iPierce, fDistance, fSpeed, targettype = OBJ_ALL, angle = 0, iIgnoreMonsterID = 0, *args, **kwargs):
        dCartoon['Start'] = StartPos
        dCartoon['End'] = EndPos
        dCartoon['Pierce'] = iPierce
        dCartoon['Distance'] = fDistance
        dCartoon['SpeedPerFrame'] = fSpeed * GAME_FRAME_SECOND
        dCartoon['AnglePerFrame'] = angle
        dCartoon['HeightRatio'] = 0.85
        dCartoon['TargetType'] = targettype
        dCartoon['CurPos'] = StartPos
        dCartoon['PierceBlock'] = False
        dCartoon['LockTarget'] = oSkill.m_Base['VID']
        dCartoon['IgnoreTarget'] = iIgnoreMonsterID if iIgnoreMonsterID else oSkill.m_Base['AID']
        dCartoon['Dir'] = cl_math.Vec3Normalize(cl_math.Vec3Minus(dCartoon['End'], dCartoon['Start']))
        dNet = {
            'Start': dCartoon['Start'],
            'End': dCartoon['End'],
            'LockTarget': [
                oSkill.m_Base['VID']] }
        oSkill.Send(dCartoon['ID'], dNet)
        debug.ClearDebugLine(oSkill.m_Game, debug.LINE_TILE)

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
        else:
            vTarget = None
        if vTarget:
            vDir = cl_math.Vec3Minus(vTarget, vCur)
            tAxis = cl_math.Vec3Normalize(cl_math.VectorCross3D(vPreDir, vDir))
            iAngle = cl_math.CalAngle3D(vPreDir, vDir)
            if iAngle:
                iAngle = min(dCartoon['AnglePerFrame'], iAngle)
                vNewDir = cl_math.Vec3Normalize(cl_math.RotateAroundVector(vPreDir, tAxis, iAngle))
                dCartoon['Dir'] = vNewDir
        vTar = cl_math.Vec3Mad(vCur, vNewDir, dCartoon['SpeedPerFrame'])
        iMask = PXMASK_LIVEOBJ if dCartoon['PierceBlock'] else PXMASK_SKILLBLK | PXMASK_LIVEOBJ
        if oSkill.m_Cache['Side'] != SIDE_TYPE_HERO:
            iBlockMask = PXMASK_SIDEBLK
        else:
            iBlockMask = PXMASK_SKILLBLK
        lstVictim = oGame.Scene_RaycastMultiple(oSkill.m_Base['Scene'], vCur, vTar, iMask, {
            'PassID': dCartoon['IgnoreTarget'],
            'BlockMask': iBlockMask,
            'ExcludeFlag': PY_FLAG_DEAD,
            'Normal': 1 })
        if oGame.m_WarMgr.Query('DebugRay'):
            (ox, oy, oz) = vCur
            (tx, ty, tz) = vTar
            debug.DebugLine(oGame, ox, oy, oz, tx, ty, tz, 65280, debug.LINE_TILE)
        if not lstVictim:
            dCartoon['CurPos'] = vTar
            return 0
        lstVLST = []
        lstSend = []
        for iVictim, dHit in lstVictim:
            dCartoon['CurPos'] = dHit['Pos']
            iVitcimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
            if iVitcimState == VICTIM_STATE_BLOCK:
                oSkill.m_Update['HitStatic'] = 1
                dCartoon['Pierce'] = 0
                lstSend.append((dHit['Pos'], dHit['Normal'], iVictim, MONSTER_PART_UNTAGGED))
            elif iVitcimState == VICTIM_STATE_VALID:
                dCartoon['Pierce'] -= cls.GetVictimPierceCost(oSkill, iVictim)
                lstVLST.append(iVictim)
                lstSend.append((dHit['Pos'], dHit['Normal'], iVictim, MONSTER_PART_UNTAGGED))
            
            if dCartoon['Pierce'] <= 0:
                dCartoon['Final'] = dHit['Pos']
                break
        
        oSkill.m_Update['LastVLST'] = lstVLST
        dNet = {
            'Ray': lstSend,
            'HitStatic': oSkill.m_Update['HitStatic'] if 'HitStatic' in oSkill.m_Update else 0 }
        oSkill.Send(dCartoon['ID'], dNet)
        cls.CollectSkillInfo(oSkill, dCartoon)
        return 1

    HitTargetServer = classmethod(HitTargetServer)
    
    def IsOverServer(cls, oSkill, dCartoon):
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

    IsOverServer = classmethod(IsOverServer)
    
    def CollectSkillInfo(cls, oSkill, dCartoon):
        lstCartoonPos = oSkill.m_Collect['CartoonPos'] if 'CartoonPos' in oSkill.m_Collect else []
        vStart = dCartoon['Start']
        vEnd = dCartoon['Final'] if 'Final' in dCartoon else dCartoon['CurPos']
        lstCartoonPos.append((vStart, vEnd))
        oSkill.m_Collect['CartoonPos'] = lstCartoonPos

    CollectSkillInfo = classmethod(CollectSkillInfo)

