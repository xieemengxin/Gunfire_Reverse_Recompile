# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_castingpos.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_castingpos.pyc
# Source Generated with Decompyle++
# File: crt_castingpos.pyc (Python 3.6)

from cl_only import Time2Frame, PY_FLAG_DEAD
from cl_commondefines import OBJ_ALL, ATT_SHAPE_SECTOR, ATT_SHAPE_SPHERE, ATT_SHAPE_RECTANGLE, ATT_SHAPE_CYLINDER
from cl_commondefines import HITPART_DIRECTPOS, CRT_CHECK_SERVER, WARRIOR_BUILD
from cl_commondefines import VICTIM_STATE_VALID
from cl_commondefines import SIDE_TYPE_HERO
from cl_pxlayer import PXMASK_LIVEOBJ, PXMASK_SKILLBLK, PXMASK_SIDEBLK
from cl_object.logging import SkillLog
import cl_math
import cl_gamedebug as debug
from .mobject import CBaseCartoon

class CastingPosCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        cls.Update(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def Restart(cls, oSkill, dCartoon):
        if oSkill.m_CheckType & CRT_CHECK_SERVER:
            oSkill.Call_Out(dCartoon['IntervalFrame'], dCartoon['ID'], dCartoon['Casting'])

    Restart = classmethod(Restart)
    
    def IsOver(cls, oSkill, dCartoon):
        iOver = 0
        iFrame = dCartoon['ChangeSpeedFrame'] if 'ChangeSpeedFrame' in dCartoon else dCartoon['StartFrame']
        if iFrame + dCartoon['WaitFrame'] <= oSkill.m_Game.GetFrameNum():
            iOver = 1
        if dCartoon['AttackDieBreak']:
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
    
    def InitTraceServer(cls, oSkill, dCartoon, StartPos, OffsetPos, iIntervalTime, iTotalTime, lstArgs, attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ALL, AttackDieBreak = False, *args, **kwargs):
        dCartoon['Start'] = StartPos
        dCartoon['Offset'] = OffsetPos
        dCartoon['IntervalFrame'] = Time2Frame(iIntervalTime)
        dCartoon['WaitFrame'] = (Time2Frame(iTotalTime) // dCartoon['IntervalFrame']) * dCartoon['IntervalFrame']
        dCartoon['AttShape'] = attshape
        dCartoon['TargetType'] = targettype
        dCartoon['EffArgs'] = lstArgs
        dCartoon['AttackDieBreak'] = AttackDieBreak
        dNet = {
            'Start': StartPos,
            'Offset': OffsetPos,
            'Time': iTotalTime }
        oSkill.Send(dCartoon['ID'], dNet)

    InitTraceServer = classmethod(InitTraceServer)
    
    def HitTargetServer(cls, oSkill, dCartoon):
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
        dNet = {
            'LastVLST': lstVictim }
        oSkill.Send(dCartoon['ID'], dNet)
        return 1

    HitTargetServer = classmethod(HitTargetServer)
    
    def GetAllTarget(cls, oSkill, dCartoon):
        oGame = oSkill.m_Game
        iAttack = oSkill.m_Base['AID']
        oAttack = oGame.GetObject(iAttack)
        if not oAttack:
            return []
        vStart = dCartoon['Start']
        if cl_math.IsZero(vStart):
            vStart = oAttack.GetPos()
        vOffset = dCartoon['Offset']
        lstEffArgs = dCartoon['EffArgs']
        if 'Side' in oSkill.m_Cache and oSkill.m_Cache['Side'] != SIDE_TYPE_HERO:
            iBlockMask = PXMASK_SIDEBLK
        else:
            iBlockMask = PXMASK_SKILLBLK
        if oAttack.m_FightType & WARRIOR_BUILD == WARRIOR_BUILD and dCartoon['AttShape'] == ATT_SHAPE_RECTANGLE:
            vEuler = oAttack.GetEuler()
            if not cl_math.IsZero(vOffset):
                vAngle = cl_math.Radians2Angle(vEuler)
                vOffset = cl_math.RotateByEuler(vOffset, vAngle)
                vStart = cl_math.Vec3Add(vStart, vOffset)
            dCartoon['CurPos'] = vStart
            lstArgs = [
                vStart,
                vEuler]
            lstArgs.extend(lstEffArgs)
            lstHit = cl_math.GetAttackTargetList(oGame, oAttack.m_Scene, dCartoon['AttShape'], lstArgs, {
                'Mask': PXMASK_LIVEOBJ,
                'UseEuler': 1,
                'BlockMask': iBlockMask })
        else:
            vDir = oAttack.GetFacing()
            if cl_math.IsZero(vDir):
                oFaceVictim = oGame.GetObject(oAttack.m_FaceCtrl.m_FaceVictim)
                oVictim = oGame.GetObject(oSkill.m_Base['VID'])
                vFaceVictimPos = (0, 0, 0)
                vVictimPos = (0, 0, 0)
                if oFaceVictim:
                    vFaceVictimPos = oFaceVictim.GetPos()
                if oVictim:
                    vVictimPos = oVictim.GetPos()
                SkillLog.Alert('%s %s attack face is zero, facevid:%s vid:%s facestatus:%s attackpos:%s facevictimpos:%s victimpos:%s' % (oAttack.m_ID, oSkill.m_Base['PFKey'], oAttack.m_FaceCtrl.m_FaceVictim, oSkill.m_Base['VID'], oAttack.m_FaceCtrl.m_CurStatus, oAttack.GetPos(), vFaceVictimPos, vVictimPos))
                return []
            if not cl_math.IsZero(vOffset):
                iAngle = cl_math.CalRotate2D(vDir)
                vOffset = cl_math.RotateByEuler(vOffset, (0, iAngle, 0))
                vStart = cl_math.Vec3Add(vStart, vOffset)
            dCartoon['CurPos'] = vStart
            if dCartoon['AttShape'] == ATT_SHAPE_SPHERE:
                lstArgs = [
                    vStart,
                    lstEffArgs[0]]
            elif dCartoon['AttShape'] == ATT_SHAPE_CYLINDER:
                lstArgs = [
                    vStart,
                    lstEffArgs[0],
                    lstEffArgs[1]]
            elif dCartoon['AttShape'] in (ATT_SHAPE_SECTOR, ATT_SHAPE_RECTANGLE):
                if oGame.m_WarMgr.Query('DebugRay'):
                    if dCartoon['AttShape'] == ATT_SHAPE_RECTANGLE:
                        debug.ClearDebugLine(oGame, debug.LINE_BOX)
                        (fLength, fWidth, fHeight) = lstEffArgs
                        debug.DebugBox(oGame, dCartoon['CurPos'], vDir, fLength, fWidth, fHeight)
                    else:
                        debug.ClearDebugLine(oGame, debug.LINE_TILE)
                        vDir = cl_math.RotateAroundVector(vDir, (0, -1, 0), lstEffArgs[2] / 2)
                        debug.DebugSector(oGame, dCartoon['CurPos'], lstEffArgs[0], vDir, lstEffArgs[2], debug.LINE_TILE)
                        debug.DebugSector(oGame, (dCartoon['CurPos'][0], dCartoon['CurPos'][1] + lstEffArgs[1], dCartoon['CurPos'][2]), lstEffArgs[0], vDir, lstEffArgs[2], debug.LINE_TILE)
                lstArgs = [
                    vStart,
                    vDir]
                lstArgs.extend(lstEffArgs)
            else:
                return []
            lstHit = cl_math.GetAttackTargetList(oGame, oAttack.m_Scene, dCartoon['AttShape'], lstArgs, {
                'Mask': PXMASK_LIVEOBJ,
                'BlockMask': iBlockMask })
        lstTarget = []
        for iVictim in lstHit:
            iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
            if iVictimState == VICTIM_STATE_VALID:
                lstTarget.append(iVictim)
        
        return lstTarget

    GetAllTarget = classmethod(GetAllTarget)
    
    def OnChangeSpeed(cls, oSkill, dCartoon):
        iAttack = oSkill.m_Base['AID']
        oAttack = oSkill.m_Game.GetObject(iAttack)
        if not oAttack:
            return None
        iNowFrame = oSkill.m_Game.GetFrameNum()
        iFrame = dCartoon['ChangeSpeedFrame'] if 'ChangeSpeedFrame' in dCartoon else dCartoon['StartFrame']
        iRemainFrame = iFrame + dCartoon['WaitFrame'] - iNowFrame
        if iRemainFrame <= 0:
            return None
        dCartoon['WaitFrame'] = oAttack.GetChangeSpeedDelayFrame(iRemainFrame)
        dCartoon['ChangeSpeedFrame'] = iNowFrame

    OnChangeSpeed = classmethod(OnChangeSpeed)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        return 0

    HitTargetClient = classmethod(HitTargetClient)

