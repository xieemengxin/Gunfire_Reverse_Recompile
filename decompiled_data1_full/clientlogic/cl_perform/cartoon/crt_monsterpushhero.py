# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_monsterpushhero.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_monsterpushhero.pyc
# Source Generated with Decompyle++
# File: crt_monsterpushhero.pyc (Python 3.6)

from cl_only import GAME_FRAME, Functor
from cl_commondefines import CRT_CHECK_SERVER, MODEL_TYPE_BOX, WARRIOR_HERO, OBJ_ALL, VICTIM_STATE_VALID
from cl_pxlayer import PXLAYER_EBULLET
from cl_object.logging import SkillLog
import cl_math
import cl_engphyobj
from .mobject import CBaseCartoon

class MonsterPushHeroCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        if not oSkill.m_CheckType & CRT_CHECK_SERVER:
            return None
        oGame = oSkill.m_Game
        iVictim = dCartoon['LockTarget']
        oVictim = oGame.GetObject(iVictim)
        if not oVictim or oVictim.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
            dCartoon['Over'] = 1
            cls.Update(oSkill, dCartoon)
            return None
        fSpeed = dCartoon['Speed']
        fDistance = dCartoon['Distance']
        if fSpeed <= 0 or fDistance <= 0:
            dCartoon['Over'] = 1
            cls.Update(oSkill, dCartoon)
            return None
        vDir = dCartoon['Dir']
        cbfunc = Functor(PushMoveEnd, oSkill.m_Base['AID'], oSkill.m_Base['ActNum'], dCartoon['ID'])
        fTimeOutSecond = fDistance / fSpeed
        fDownSpeed = 0
        fGravaty = 9.8
        iRet = oVictim.m_MoveCtrl.PushMove(oVictim, vDir, fSpeed, fTimeOutSecond, fDownSpeed, fGravaty, cbfunc)
        if not iRet:
            oSkill.Halt('pushfail')
            return None
        fExtentZ = fSpeed / GAME_FRAME
        oBullet = cl_engphyobj.CreateTraceBullet(oGame, oVictim, {
            'TraceIdx': oSkill.m_Base['PFKey'],
            'LocalPos': (0, 0, fExtentZ),
            'PassID': oVictim.m_ID,
            'LockDirection': vDir }, PXLAYER_EBULLET, {
            'Shape': MODEL_TYPE_BOX,
            'HalfExt': (oVictim.m_ModelRadius, oVictim.m_ModelHeight, fExtentZ) })
        oGame.m_SkillMgr.RegisterBullet(oBullet, oSkill.m_Base['AID'], oSkill.m_Base['ActNum'], dCartoon['ID'])
        dCartoon['BulletKey'] = oBullet.Key()
        oSkill.AddEndFunc(Functor(ClearCartoon, dCartoon))
        iAttachSummon = dCartoon['AttachSummon']
        if iAttachSummon:
            oAttachSummon = oGame.GetObject(iAttachSummon)
            if oAttachSummon:
                vOffset = cl_math.Vec3Minus(oAttachSummon.GetPos(), oVictim.GetPos())
                dCartoon['SummonOffset'] = vOffset
        dCartoon['CurPos'] = oVictim.GetPos()
        dCartoon['Start'] = dCartoon['CurPos']
        dCartoon['Final'] = dCartoon['CurPos']
        cls.Update(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def Restart(cls, oSkill, dCartoon):
        if not oSkill.m_CheckType & CRT_CHECK_SERVER:
            return None
        oSkill.Call_Out(1, dCartoon['ID'])

    Restart = classmethod(Restart)
    
    def InitTraceServer(cls, oSkill, dCartoon, fSpeed, vDir, fMaxDistance, attachSummon = 0, targettype = OBJ_ALL, lockTarget = 0, **kwargs):
        dCartoon['LockTarget'] = 0
        if lockTarget:
            dCartoon['LockTarget'] = lockTarget
        elif 'CurVID' in oSkill.m_Update:
            dCartoon['LockTarget'] = oSkill.m_Update['CurVID']
        dCartoon['Dir'] = vDir
        dCartoon['Speed'] = fSpeed
        dCartoon['Distance'] = fMaxDistance
        dCartoon['AttachSummon'] = attachSummon
        dCartoon['LimitDistance2D'] = True

    InitTraceServer = classmethod(InitTraceServer)
    
    def IsOver(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if 'Over' in dCartoon:
            iVictim = dCartoon['LockTarget']
            oGame = oSkill.m_Game
            oVictim = oGame.GetObject(iVictim)
            if oVictim:
                dCartoon['Final'] = oVictim.GetPos()
            elif 'CurPos' in dCartoon:
                dCartoon['Final'] = dCartoon['CurPos']
            else:
                dCartoon['Final'] = (0, 0, 0)
            dNet = {
                'Over': 1,
                'End': dCartoon['Final'] }
            oSkill.Send(iNodeID, dNet)
            cls.ClearCartoonBullet(oSkill, dCartoon)
            return 1
        return 0

    IsOver = classmethod(IsOver)
    
    def AddHitTarget(cls, oSkill, dCartoon, iTarget, dHit):
        lstHit = dCartoon['TargetList'] if 'TargetList' in dCartoon else []
        if iTarget not in lstHit:
            lstHit.append(iTarget)
        dCartoon['TargetList'] = lstHit
        cls.Update(oSkill, dCartoon)

    AddHitTarget = classmethod(AddHitTarget)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        if 'Over' in dCartoon:
            return 0
        iVictim = dCartoon['LockTarget']
        oGame = oSkill.m_Game
        oVictim = oGame.GetObject(iVictim)
        if not oVictim:
            dCartoon['Over'] = 1
            return 0
        vNowPos = oVictim.GetPos()
        if dCartoon['LimitDistance2D'] and not cl_math.CheckDistance(vNowPos, dCartoon['Start'], dCartoon['Distance']):
            dCartoon['Over'] = 1
            oVictim.Stop()
            return 0
        if dCartoon['AttachSummon']:
            oAttachSummon = oGame.GetObject(dCartoon['AttachSummon'])
            vSummonOffet = dCartoon['SummonOffset'] if 'SummonOffset' in dCartoon else None
            if oAttachSummon and vSummonOffet:
                vSummonPos = cl_math.Vec3Add(vNowPos, vSummonOffet)
                oAttachSummon.WalkTo(vSummonPos)
        lstHit = dCartoon['TargetList'] if 'TargetList' in dCartoon else []
        dCartoon['TargetList'] = []
        if not lstHit:
            return 0
        lstVLST = []
        for iTarget in lstHit:
            iTargetState = cls.CheckVictimState(oSkill, dCartoon, iTarget)
            if iTargetState == VICTIM_STATE_VALID and iTarget not in lstVLST:
                lstVLST.append(iTarget)
        
        if not lstVLST:
            return 0
        dCartoon['CurPos'] = oVictim.GetPos()
        dCartoon['Final'] = dCartoon['CurPos']
        oSkill.m_Update['LastVLST'] = lstVLST
        dNet = {
            'LastVLST': lstVLST }
        oSkill.Send(dCartoon['ID'], dNet)
        return 1

    HitTargetServer = classmethod(HitTargetServer)


def PushMoveEnd(iAttack, iActNum, iCartoon, oOwner, iFlag):
    if not oOwner:
        return None
    oGame = oOwner.m_Game
    oSkill = oGame.m_SkillMgr.GetSkill(iAttack, iActNum)
    if not oSkill or iCartoon not in oSkill.m_Cartoon:
        return None
    dCartoon = oSkill.m_Cartoon[iCartoon]
    if 'Over' in dCartoon:
        return None
    dCartoon['Over'] = 1
    dCartoon['cls'].Update(oSkill, dCartoon)


def ClearCartoon(dCartoon, oSkill):
    dCartoon['cls'].ClearCartoonBullet(oSkill, dCartoon)

