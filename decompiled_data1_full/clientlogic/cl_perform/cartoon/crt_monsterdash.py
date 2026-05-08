# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_monsterdash.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_monsterdash.pyc
# Source Generated with Decompyle++
# File: crt_monsterdash.pyc (Python 3.6)

from cl_only import Second2Frame, GAME_FRAME, Functor, Time2Frame
from cl_commondefines import WARRIOR_HERO, MODEL_TYPE_BOX, PATHMODE_POWERPUSH, VICTIM_STATE_VALID, VICTIM_STATE_BLOCK, OBJ_ALL
from cl_pxlayer import PXLAYER_EBULLET_STATIC
import cl_math
import cl_engphyobj
import cl_gamedebug as debug
from .mobject import CBaseCartoon

class MonsterDashCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        if 'Over' in dCartoon:
            return None
        oAttack = oSkill.GetAttack()
        fTimeOutSecond = dCartoon['TotalSecond'] if 'TotalSecond' in dCartoon else 0
        if not oAttack or not fTimeOutSecond:
            cls.Disable(oSkill, dCartoon)
            return None
        fSlideSecond = dCartoon['SlideSecond']
        tDir = dCartoon['Dir']
        fSpeed = dCartoon['Speed']
        if fSpeed < 1e-06:
            oSkill.Halt('dashspeediszero')
            return None
        cbfunc = Functor(DashMoveEnd, oSkill.m_Base['ActNum'], dCartoon['ID'])
        iRet = oAttack.m_MoveCtrl.DashMove(oAttack, tDir, fSpeed, fTimeOutSecond, cbfunc, fSlideSecond)
        if not iRet:
            oSkill.Halt('dashfail')
            return None
        if dCartoon['PushOff']:
            oAttack.m_MoveCtrl.SetPathMode('PushOff', PATHMODE_POWERPUSH)
        if dCartoon['HeroBreak'] or dCartoon['StaticBreak'] or dCartoon['Collision']:
            oGame = oSkill.m_Game
            if dCartoon['CheckDis']:
                fExtentZ = dCartoon['CheckDis']
            else:
                fExtentZ = fSpeed / GAME_FRAME
            fBulletHeightScale = dCartoon['BulletHeightScale'] if 'BulletHeightScale' in dCartoon else 1
            fBulletRadiusScale = dCartoon['BulletRadiusScale'] if 'BulletRadiusScale' in dCartoon else 1
            fHaltExtX = (oAttack.m_ModelRadius / 2) * fBulletRadiusScale
            fHaltExtY = (oAttack.m_ModelHeight / 2) * fBulletHeightScale
            oBullet = cl_engphyobj.CreateTraceBullet(oGame, oAttack, {
                'TraceIdx': oSkill.m_Base['PFKey'],
                'LocalPos': (0, dCartoon['OffSetY'], fExtentZ),
                'PassID': oAttack.m_ID,
                'LockDirection': tDir }, PXLAYER_EBULLET_STATIC, {
                'Shape': MODEL_TYPE_BOX,
                'HalfExt': (fHaltExtX, fHaltExtY, fExtentZ) })
            oGame.m_SkillMgr.RegisterBullet(oBullet, oSkill.m_Base['AID'], oSkill.m_Base['ActNum'], dCartoon['ID'])
            dCartoon['BulletKey'] = oBullet.Key()
            oSkill.AddEndFunc(Functor(ClearCartoon, dCartoon))
            if oGame.m_WarMgr.Query('DebugRay'):
                fLength = fExtentZ * 2
                fWidth = oAttack.m_ModelRadius
                fHeight = oAttack.m_ModelHeight
                debug.ClearDebugLine(oGame, debug.LINE_BOX)
                debug.DebugBox(oGame, cl_math.Vec3Add(oAttack.GetPos(), (0, dCartoon['OffSetY'], fExtentZ)), tDir, fLength, fWidth, fHeight)
        if dCartoon['TotalSecond'] and dCartoon['WaitOverTime']:
            cls.WaitOverTime(oSkill, dCartoon)
        if dCartoon['CheckFrame']:
            oSkill.Call_Out(dCartoon['CheckFrame'], dCartoon['ID'])

    Trace = classmethod(Trace)
    
    def InitTraceServer(cls, oSkill, dCartoon, EndPos, TotalTime, SlideTime, fSpeed, Pushoff, Herobreak = True, bWaitOverTime = False, checkDis = 0, start = None, offSetY = 0, staticbreak = False, CheckTime = 0, StopDis = 0, CheckHalt = False, targettype = OBJ_ALL, Collision = False, BulletHeightScale = 1, BulletRadiusScale = 1):
        if not start or cl_math.IsZero(start):
            dCartoon['Start'] = oSkill.m_Base['vStart']
        else:
            dCartoon['Start'] = start
        dCartoon['End'] = EndPos
        if dCartoon['End'] == dCartoon['Start']:
            dCartoon['Over'] = 1
            oSkill.Send(dCartoon['ID'], {
                'Over': 1 })
            cls.Disable(oSkill, dCartoon)
        if TotalTime < 0.0001 and fSpeed < 1e-06:
            oSkill.Send(dCartoon['ID'], {
                'Over': 1 })
            cls.Disable(oSkill, dCartoon)
            return None
        if fSpeed < 1e-06:
            fDis = cl_math.CalDistance3D(dCartoon['Start'], dCartoon['End'])
            fSpeed = fDis * 100 / TotalTime
            if fSpeed < 1e-06:
                oSkill.Send(dCartoon['ID'], {
                    'Over': 1 })
                cls.Disable(oSkill, dCartoon)
        if TotalTime < 0.0001:
            fDis = cl_math.CalDistance3D(dCartoon['Start'], dCartoon['End'])
            TotalTime = fDis * 100 / fSpeed
            if TotalTime < 0.0001:
                oSkill.Send(dCartoon['ID'], {
                    'Over': 1 })
                cls.Disable(oSkill, dCartoon)
        dCartoon['TotalSecond'] = TotalTime * 0.01
        dCartoon['SlideSecond'] = SlideTime * 0.01
        iAttack = oSkill.m_Base['AID']
        oAttack = oSkill.m_Game.GetObject(iAttack)
        if cl_math.IsZero(EndPos):
            dCartoon['Dir'] = cl_math.Vec3Normalize(oAttack.GetFacing())
        else:
            dCartoon['Dir'] = cl_math.Vec3Normalize(cl_math.Vec3Minus(dCartoon['End'], dCartoon['Start']))
        dCartoon['Speed'] = fSpeed
        dCartoon['PushOff'] = Pushoff
        dCartoon['HeroBreak'] = Herobreak
        dCartoon['StaticBreak'] = staticbreak
        dCartoon['WaitOverTime'] = bWaitOverTime
        dCartoon['CheckDis'] = checkDis
        dCartoon['OffSetY'] = offSetY
        dCartoon['LastDashPos'] = oAttack.GetPos()
        dCartoon['StopDis'] = StopDis
        dCartoon['CheckFrame'] = Time2Frame(CheckTime)
        dCartoon['CheckHalt'] = CheckHalt
        dCartoon['TargetType'] = targettype
        dCartoon['Collision'] = Collision
        dCartoon['BulletHeightScale'] = BulletHeightScale if BulletHeightScale > 0 else 1
        dCartoon['BulletRadiusScale'] = BulletRadiusScale if BulletRadiusScale > 0 else 1

    InitTraceServer = classmethod(InitTraceServer)
    
    def AddHitTarget(cls, oSkill, dCartoon, iTarget, dHit):
        if 'WinkEnd' in dCartoon:
            return None
        dHit['Victim'] = iTarget
        dCartoon['BulletHit'] = dHit

    AddHitTarget = classmethod(AddHitTarget)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        lstVictim = []
        iHit = 0
        if 'BulletHit' in dCartoon:
            iHit = 1
            dHit = dCartoon['BulletHit']
            dCartoon.pop('BulletHit')
            iVictim = dHit['Victim']
            iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
            if iVictimState == VICTIM_STATE_BLOCK:
                oSkill.m_Update['HitStatic'] = 1
                if dCartoon['StaticBreak']:
                    cls.WinkMoveEnd(oSkill, dCartoon)
                    iAttack = oSkill.m_Base['AID']
                    oAttack = oSkill.m_Game.GetObject(iAttack)
                    oAttack.m_MoveCtrl.Stop(oAttack)
                elif iVictimState == VICTIM_STATE_VALID:
                    lstVictim = [
                        iVictim]
                    oGame = oSkill.m_Game
                    oWarrior = oGame.GetObject(iVictim)
                    if oWarrior and oWarrior.m_FightType == WARRIOR_HERO and dCartoon['HeroBreak']:
                        cls.WinkMoveEnd(oSkill, dCartoon)
                        iAttack = oSkill.m_Base['AID']
                        oAttack = oSkill.m_Game.GetObject(iAttack)
                        oAttack.m_MoveCtrl.Stop(oAttack)
        if None:
            oSkill.m_Update['LastVLST'] = lstVictim
            dNet = {
                'LastVLST': lstVictim,
                'HitStatic': oSkill.m_Update['HitStatic'] if 'HitStatic' in oSkill.m_Update else 0 }
            oSkill.Send(dCartoon['ID'], dNet)
        return iHit

    HitTargetServer = classmethod(HitTargetServer)
    
    def IsOver(cls, oSkill, dCartoon):
        iOver = 0
        if dCartoon['CheckFrame']:
            tLastPos = dCartoon['LastDashPos']
            iAttack = oSkill.m_Base['AID']
            oAttack = oSkill.m_Game.GetObject(iAttack)
            tPos = oAttack.GetPos()
            dCartoon['LastDashPos'] = tPos
            if cl_math.CheckDistance3D(tLastPos, tPos, dCartoon['StopDis']):
                cls.WinkMoveEnd(oSkill, dCartoon)
                oAttack.m_MoveCtrl.Stop(oAttack)
                if dCartoon['CheckHalt']:
                    oSkill.Halt('CheckHalt')
                    return 1
        if 'WinkEnd' in dCartoon:
            if 'EndFrame' not in dCartoon or dCartoon['EndFrame'] <= oSkill.m_Game.GetFrameNum():
                iOver = 1
        if iOver:
            iNodeID = dCartoon['ID']
            oSkill.Send(iNodeID, {
                'Over': 1 })
            cls.ClearCartoonBullet(oSkill, dCartoon)
            return 1
        return 0

    IsOver = classmethod(IsOver)
    
    def WaitOverTime(cls, oSkill, dCartoon):
        iWaitFrame = Second2Frame(dCartoon['TotalSecond']) + 1
        dCartoon['EndFrame'] = dCartoon['StartFrame'] + iWaitFrame
        oSkill.Call_Out(iWaitFrame, dCartoon['ID'])

    WaitOverTime = classmethod(WaitOverTime)
    
    def WinkMoveEnd(cls, oSkill, dCartoon):
        if 'WinkEnd' not in dCartoon:
            dCartoon['WinkEnd'] = 1
            iAttack = oSkill.m_Base['AID']
            oAttack = oSkill.m_Game.GetObject(iAttack)
            oAttack.m_MoveCtrl.ClearPathMode('PushOff')
            oAttack.m_MoveCtrl.m_WinkMoveCB = None

    WinkMoveEnd = classmethod(WinkMoveEnd)
    
    def Restart(cls, oSkill, dCartoon):
        if dCartoon['CheckFrame']:
            oSkill.Call_Out(dCartoon['CheckFrame'], dCartoon['ID'])

    Restart = classmethod(Restart)


def DashMoveEnd(iActNum, iCartoon, oAttack, iFlag):
    if not oAttack:
        return None
    oGame = oAttack.m_Game
    oSkill = oGame.m_SkillMgr.GetSkill(oAttack.m_ID, iActNum)
    if not oSkill or iCartoon not in oSkill.m_Cartoon:
        return None
    dCartoon = oSkill.m_Cartoon[iCartoon]
    if 'WinkEnd' not in dCartoon:
        clsCartoon = dCartoon['cls']
        clsCartoon.WinkMoveEnd(oSkill, dCartoon)
        if not (oSkill.m_HaltRS) and not oAttack.IsDead():
            oSkill.Update([
                dCartoon['ID']])


def ClearCartoon(dCartoon, oSkill):
    dCartoon['cls'].ClearCartoonBullet(oSkill, dCartoon)

