# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_specifyspeedbullet.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_specifyspeedbullet.pyc
# Source Generated with Decompyle++
# File: crt_specifyspeedbullet.pyc (Python 3.6)

from cl_only import Time2Frame, Functor
from cl_commondefines import CRT_CHECK_CLIENT, CRT_CHECK_SERVER, OBJ_ENEMY, MODEL_TYPE_SPHERE, VICTIM_STATE_BLOCK, VICTIM_STATE_VALID
from cl_pxlayer import PXLAYER_RBULLET
import cl_engphyobj
from .mobject import CBaseCartoon

class SpecifySpeedBulletCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        if oSkill.m_CheckType & CRT_CHECK_CLIENT:
            return None
        oGame = oSkill.m_Game
        dBulletParam = {
            'Speed': dCartoon['SpeedVector'],
            'AccSpeed': (0, 18, 0),
            'PassID': oSkill.m_Base['AID'] }
        oBullet = cl_engphyobj.CreateRigidBullet(oGame, dBulletParam, PXLAYER_RBULLET, {
            'Shape': MODEL_TYPE_SPHERE,
            'Radius': dCartoon['Radius'] })
        oBullet.Goto(oSkill.m_Base['Scene'], dCartoon['Start'], tEuler = (0, 0, 0))
        oBullet.SetBulletSpeed(dCartoon['SpeedVector'])
        oBullet.SetBulletAccSpeed((0, 18, 0))
        oGame.m_SkillMgr.RegisterBullet(oBullet, oSkill.m_Base['AID'], oSkill.m_Base['ActNum'], dCartoon['ID'])
        dCartoon['BulletKey'] = oBullet.Key()
        oSkill.AddEndFunc(Functor(ClearCartoon, dCartoon))
        oSkill.Call_Out(1, dCartoon['ID'])

    Trace = classmethod(Trace)
    
    def IsOver(cls, oSkill, dCartoon):
        oSkill.m_Update['EPFPos'] = dCartoon['Final']
        iNodeID = dCartoon['ID']
        iOver = 0
        if 'Over' in dCartoon:
            iOver = 1
        if iOver:
            ClearCartoon(dCartoon, oSkill)
            oSkill.Send(iNodeID, {
                'Over': 1 })
            return 1
        return 0

    IsOver = classmethod(IsOver)
    
    def Restart(cls, oSkill, dCartoon):
        if oSkill.m_CheckType & CRT_CHECK_SERVER:
            oSkill.Call_Out(1, dCartoon['ID'])

    Restart = classmethod(Restart)
    
    def InitTraceClient(cls, oSkill, dCartoon, fRadius, iTriggerDelay, iHitOver, iHitStaticOver, *arg, targettype = OBJ_ENEMY, **kwargs):
        iNodeID = dCartoon['ID']
        dClient = oSkill.m_NetReceive[iNodeID]
        dCartoon['Final'] = dClient['Start']
        dCartoon['Start'] = dClient['Start']
        dCartoon['SpeedVector'] = dClient['SpeedVector']
        dCartoon['WaitFrame'] = Time2Frame(dClient['Time'])
        dCartoon['HitOver'] = iHitOver
        dCartoon['HitStaticOver'] = iHitStaticOver
        dCartoon['AllVLST'] = []
        dCartoon['CurPos'] = dClient['Start']
        oSkill.Send(dCartoon['ID'], dClient)

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        return 0

    HitTargetClient = classmethod(HitTargetClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, StartPos, vSpeed, fRadius, iTriggerDelay, iHitOver, iHitStaticOver, *arg, targettype = OBJ_ENEMY, **kwargs):
        dCartoon['Start'] = StartPos
        dCartoon['Final'] = dCartoon['Start']
        dCartoon['SpeedVector'] = vSpeed
        dCartoon['Radius'] = fRadius
        dNet = {
            'Start': dCartoon['Start'],
            'SpeedVector': dCartoon['SpeedVector'],
            'Time': iTriggerDelay }
        dCartoon['WaitFrame'] = Time2Frame(iTriggerDelay)
        dCartoon['HitOver'] = iHitOver
        dCartoon['HitStaticOver'] = iHitStaticOver
        dCartoon['TargetType'] = targettype
        dCartoon['AllVLST'] = []
        dCartoon['CurPos'] = StartPos
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
        oGame = oSkill.m_Game
        oBullet = oGame.m_SkillMgr.GetBullet(dCartoon['BulletKey'])
        iHit = 0
        if 'BulletHit' in dCartoon:
            iHit = 1
            dHit = dCartoon['BulletHit']
            iTarget = dHit['Victim']
            iVictimState = cls.CheckVictimState(oSkill, dCartoon, iTarget)
            if iVictimState == VICTIM_STATE_BLOCK:
                if dCartoon['HitStaticOver']:
                    dCartoon['Over'] = 1
                iTarget = 0
                oSkill.m_Update['HitStatic'] = 1
                dCartoon['CurPos'] = dHit['hitpos']
            elif iVictimState == VICTIM_STATE_VALID:
                if dCartoon['HitOver']:
                    dCartoon['Over'] = 1
                lstVLST = oSkill.m_Update['LastVLST'] if 'LastVLST' in oSkill.m_Update else []
                lstVLST.append(iTarget)
                dCartoon['AllVLST'].append(iTarget)
                oSkill.m_Update['LastVLST'] = lstVLST
                dCartoon['CurPos'] = dHit['hitpos']
            vSpeedVector = dCartoon['SpeedVector']
            oBullet.SetBulletSpeed(vSpeedVector)
            dNet['Ray'] = [
                (dHit['hitpos'], dHit['normal'], iTarget, 0)]
        if dCartoon['StartFrame'] + dCartoon['WaitFrame'] <= oSkill.m_Game.GetFrameNum():
            cls.Trigger(oSkill)
            dCartoon['Over'] = 1
            dNet['Trigger'] = 1
        dCartoon['Final'] = oBullet.GetBulletPosition()
        dNet['End'] = dCartoon['Final']
        oSkill.Send(dCartoon['ID'], dNet)
        return iHit

    HitTargetServer = classmethod(HitTargetServer)
    
    def CollectSkillInfo(cls, oSkill, dCartoon):
        lstCartoonPos = oSkill.m_Collect['CartoonPos'] if 'CartoonPos' in oSkill.m_Collect else []
        vStart = dCartoon['Start']
        vEnd = dCartoon['Final']
        lstCartoonPos.append((vStart, vEnd))
        oSkill.m_Collect['CartoonPos'] = lstCartoonPos

    CollectSkillInfo = classmethod(CollectSkillInfo)


def ClearCartoon(dCartoon, oSkill):
    dCartoon['cls'].ClearCartoonBullet(oSkill, dCartoon)

