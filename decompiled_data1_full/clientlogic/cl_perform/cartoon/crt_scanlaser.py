# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_scanlaser.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_scanlaser.pyc
# Source Generated with Decompyle++
# File: crt_scanlaser.pyc (Python 3.6)

from cl_only import Time2Frame, PY_FLAG_DEAD
from cl_commondefines import VICTIM_STATE_VALID, VICTIM_STATE_HIT, VICTIM_STATE_BLOCK, OBJ_ALL
from cl_commondefines import CRT_CHECK_SERVER
from cl_pxlayer import PXMASK_LIVEOBJ, PXMASK_SKILLBLK, PXMASK_SIDEBLK
from cl_commondefines import SIDE_TYPE_HERO, MONSTER_PART_UNTAGGED
import cl_math
import cl_gamedebug as debug
from .mobject import CBaseCartoon

class ScanLaserCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        cls.Update(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def Restart(cls, oSkill, dCartoon):
        if oSkill.m_CheckType & CRT_CHECK_SERVER:
            oSkill.Call_Out(dCartoon['IntervalFrame'], dCartoon['ID'], dCartoon['Casting'])

    Restart = classmethod(Restart)
    
    def IsOver(cls, oSkill, dCartoon):
        iOver = 0
        iFrame = dCartoon['StartFrame']
        if iFrame + dCartoon['WaitFrame'] <= oSkill.m_Game.GetFrameNum():
            iOver = 1
        oGame = oSkill.m_Game
        iAttack = oSkill.m_Base['AID']
        oAttack = oGame.GetObject(iAttack, PY_FLAG_DEAD)
        if not oAttack:
            iOver = 1
        if iOver:
            oSkill.Send(dCartoon['ID'], {
                'Over': 1 })
            return 1
        return 0

    IsOver = classmethod(IsOver)
    
    def InitTraceServer(cls, oSkill, dCartoon, vStart, fMaxDis, fRadius, iAngle, iTime, iInterval, iTargetType = OBJ_ALL, **kwargs):
        if not vStart or cl_math.IsZero(vStart):
            dCartoon['Start'] = oSkill.m_Base['vStart']
        else:
            dCartoon['Start'] = vStart
        iTarget = oSkill.m_Base['VID']
        oGame = oSkill.m_Game
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if oTarget:
            vDir = cl_math.Vec3Minus(oTarget.GetCenter(), vStart)
            vDir = cl_math.Vec3NormalizeByPython(vDir)
        else:
            oAttack = oSkill.GetAttack()
            vDir = oAttack.GetFacing()
        iWaitFrame = Time2Frame(iTime)
        iIntervalFrame = Time2Frame(iInterval)
        dCartoon['Distance'] = fMaxDis
        dCartoon['Radius'] = fRadius
        dCartoon['Angle'] = iAngle
        dCartoon['AngleInc'] = -iAngle * 2 / iWaitFrame / iIntervalFrame
        dCartoon['WaitFrame'] = iWaitFrame
        dCartoon['IntervalFrame'] = iIntervalFrame
        dCartoon['TargetType'] = iTargetType
        dCartoon['Direction'] = vDir
        dNet = {
            'Start': vStart,
            'Direction': vDir }
        oSkill.Send(dCartoon['ID'], dNet)

    InitTraceServer = classmethod(InitTraceServer)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        vStart = dCartoon['Start']
        fDis = dCartoon['Distance']
        fRadius = dCartoon['Radius']
        oGame = oSkill.m_Game
        iAngle = dCartoon['Angle']
        dCartoon['Angle'] = iAngle + dCartoon['AngleInc']
        vDir = cl_math.RotateAroundVector(dCartoon['Direction'], (0, 1, 0), int(iAngle))
        vTar = cl_math.Vec3Mad(vStart, vDir, fDis)
        dCartoon['CurPos'] = vTar
        iPassID = oSkill.m_Base['AID']
        iMask = PXMASK_SKILLBLK | PXMASK_LIVEOBJ
        if oSkill.m_Cache['Side'] != SIDE_TYPE_HERO:
            iBlockMask = PXMASK_SIDEBLK
        else:
            iBlockMask = PXMASK_SKILLBLK
        if fRadius == 0:
            lstVictim = oGame.Scene_RaycastMultiple(oSkill.m_Base['Scene'], vStart, vTar, iMask, {
                'PassID': iPassID,
                'BlockMask': iBlockMask,
                'ExcludeFlag': PY_FLAG_DEAD,
                'Normal': 1 })
        else:
            lstVictim = oGame.Scene_SweepMultiple(oSkill.m_Base['Scene'], vStart, fRadius, vDir, fDis, iMask, {
                'PassID': iPassID,
                'BlockMask': iBlockMask,
                'ExcludeFlag': PY_FLAG_DEAD,
                'Normal': 1,
                'Distance': 1 })
        if oGame.m_WarMgr.Query('DebugRay'):
            (ox, oy, oz) = vStart
            (tx, ty, tz) = vTar
            debug.DebugLine(oGame, ox, oy, oz, tx, ty, tz, 65280, debug.LINE_TILE)
        if not lstVictim:
            return 0
        lstVLST = []
        lstSend = []
        for iVictim, dHit in lstVictim:
            iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
            if iVictimState == VICTIM_STATE_BLOCK:
                oSkill.m_Update['HitStatic'] = 1
                dCartoon['Pierce'] = 0
                lstSend.append((dHit['Pos'], dHit['Normal'], 0, MONSTER_PART_UNTAGGED))
                break
            if not iVictimState == VICTIM_STATE_VALID:
                pass
            fDistance = dHit['Distance'] if iVictimState == VICTIM_STATE_HIT or 'Distance' in dHit else 1
            if not fDistance:
                dHit['Pos'] = cl_math.Vec3Mad(vStart, vDir, fDis * 0.5)
            lstVLST.append(iVictim)
            lstSend.append((dHit['Pos'], vDir, iVictim, MONSTER_PART_UNTAGGED))
            dCartoon['AllVLST'] = lstVLST
        
        oSkill.m_Update['LastVLST'] = lstVLST
        oSkill.m_Update['CurPos'] = dCartoon['CurPos']
        dNet = {
            'Ray': lstSend,
            'HitStatic': oSkill.m_Update['HitStatic'] if 'HitStatic' in oSkill.m_Update else 0 }
        oSkill.Send(dCartoon['ID'], dNet)
        return 1

    HitTargetServer = classmethod(HitTargetServer)

