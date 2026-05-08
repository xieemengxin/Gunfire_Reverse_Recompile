# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_throwbypower.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_throwbypower.pyc
# Source Generated with Decompyle++
# File: crt_throwbypower.pyc (Python 3.6)

from cl_only import Time2Frame, Functor, GAME_FRAME
from cl_commondefines import WARRIOR_STONEPILLAR, WARRIOR_MONSTER, WARRIOR_HERO, MONSTER_PART_UNTAGGED, VICTIM_STATE_VALID, VICTIM_STATE_BLOCK, VICTIM_STATE_HIT, OBJ_ENEMY, CRT_CHECK_SERVER, MODEL_TYPE_SPHERE, CRT_CHECK_CLIENT, HIT_OVER_NORMAL, HIT_OVER_GROUND
from cl_pxlayer import PXLAYER_RBULLET, PXLAYER_RBULLET_NOMONS, PXLAYER_RBULLET_OUTER, PXLAYER_RBULLET_OUTER_NOMONS, PXLAYER_RBULLET_INNER, PXMASK_SKILLBLK
from cl_object.logging import SkillLog
import cl_math
import cl_engphyobj
import cl_gamedebug as debug
from .mobject import CBaseCartoon

class ThrowByPowerCartoon(CBaseCartoon):
    m_CutClient = 2
    
    def Trace(cls, oSkill, dCartoon):
        if 'Over' in dCartoon:
            return None
        if oSkill.m_CheckType & CRT_CHECK_CLIENT:
            return None
        oGame = oSkill.m_Game
        iInnerRadius = dCartoon['InnerRadius']
        dBulletParam = {
            'Speed': dCartoon['SpeedVector'],
            'AccSpeed': dCartoon['Accelerate'],
            'PassID': oSkill.m_Base['AID'] }
        iPierce = dCartoon['Pierce']
        if iPierce:
            if iInnerRadius > 0:
                iOuterLayer = PXLAYER_RBULLET_OUTER_NOMONS if dCartoon['IgnoreMonster'] else PXLAYER_RBULLET_OUTER
                oBullet = cl_engphyobj.CreateDoubleRigidBullet(oGame, dBulletParam, PXLAYER_RBULLET_INNER, {
                    'Shape': MODEL_TYPE_SPHERE,
                    'Radius': iInnerRadius,
                    'IsTrigger': 0,
                    'EnableSimulation': 1 }, iOuterLayer, {
                    'Shape': MODEL_TYPE_SPHERE,
                    'Radius': dCartoon['Radius'],
                    'IsTrigger': 1,
                    'EnableSimulation': 0 })
            elif dCartoon['IgnoreMonster']:
                pass
            
            iLayer = PXLAYER_RBULLET
            dShape = {
                'Shape': MODEL_TYPE_SPHERE,
                'Radius': dCartoon['Radius'] }
            if dCartoon['TriggerBullet']:
                dShape['IsTrigger'] = 1
                dShape['EnableSimulation'] = 0
            oBullet = cl_engphyobj.CreateRigidBullet(oGame, dBulletParam, iLayer, dShape)
        elif iInnerRadius > 0:
            iOuterLayer = PXLAYER_RBULLET_OUTER_NOMONS if dCartoon['IgnoreMonster'] else PXLAYER_RBULLET_OUTER
            oBullet = cl_engphyobj.CreateDoubleRigidBullet(oGame, dBulletParam, PXLAYER_RBULLET_INNER, {
                'Shape': MODEL_TYPE_SPHERE,
                'Radius': iInnerRadius }, iOuterLayer, {
                'Shape': MODEL_TYPE_SPHERE,
                'Radius': dCartoon['Radius'] })
        elif dCartoon['IgnoreMonster']:
            pass
        
        iLayer = PXLAYER_RBULLET
        dShape = {
            'Shape': MODEL_TYPE_SPHERE,
            'Radius': dCartoon['Radius'] }
        if dCartoon['TriggerBullet']:
            dShape['IsTrigger'] = 1
            dShape['EnableSimulation'] = 0
        oBullet = cl_engphyobj.CreateRigidBullet(oGame, dBulletParam, iLayer, dShape)
        oBullet.Goto(oSkill.m_Base['Scene'], dCartoon['Start'], tEuler = (0, 0, 0))
        oBullet.SetBulletSpeed(dCartoon['SpeedVector'])
        oBullet.SetBulletAccSpeed(dCartoon['Accelerate'])
        oGame.m_SkillMgr.RegisterBullet(oBullet, oSkill.m_Base['AID'], oSkill.m_Base['ActNum'], dCartoon['ID'])
        dCartoon['BulletKey'] = oBullet.Key()
        oSkill.AddEndFunc(Functor(ClearCartoon, dCartoon))
        oSkill.Call_Out(1, dCartoon['ID'])

    Trace = classmethod(Trace)
    
    def IsOver(cls, oSkill, dCartoon):
        oSkill.m_Update['EPFPos'] = dCartoon['Final'] if 'Final' in dCartoon else dCartoon['CurPos']
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
    
    def InitTraceClient(cls, oSkill, dCartoon, fRadius, vAccelerate, tbounciness, iTriggerDelay, iHitOver, iHitStaticOver, *arg, innerRadius = OBJ_ENEMY, pierce = (0, 0), ignoreMonster = False, hitUnitBounciness = 0, targettype = 0, **kwargs):
        dCartoon['Accelerate'] = vAccelerate
        iNodeID = dCartoon['ID']
        dClient = oSkill.m_NetReceive[iNodeID]
        dCartoon['Final'] = dClient['Start']
        dCartoon['Start'] = dClient['Start']
        dCartoon['CurPos'] = dCartoon['Start']
        dCartoon['SpeedVector'] = dClient['SpeedVector']
        dCartoon['WaitFrame'] = Time2Frame(dClient['Time']) if 'Time' in dClient else 0
        dCartoon['HitOver'] = iHitOver
        dCartoon['HitStaticOver'] = iHitStaticOver
        dCartoon['Pierce'] = pierce
        dCartoon['TargetType'] = targettype
        dCartoon['IgnoreMonster'] = ignoreMonster
        dCartoon['AllVLST'] = []
        dCartoon['AllHitInfo'] = []
        dNet = dClient.copy()
        if 'MuzzlePos' in dCartoon and dCartoon['MuzzlePos'] == dCartoon['Start']:
            dNet.pop('Start')
        oSkill.Send(dCartoon['ID'], dNet)

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return -1
        iHit = 0
        dClient = oSkill.m_NetReceive[iNodeID]
        dNet = { }
        if 'Start' in dClient:
            dCartoon['WaitNet'] = oSkill.GetWaitNetFrame()
            dCartoon['CurPos'] = dClient['Start']
            dCartoon['Final'] = dClient['Start']
            if 'SpeedVector' in dClient:
                dCartoon['SpeedVector'] = dClient['SpeedVector']
            dNet['Start'] = dClient['Start']
        if 'Ray' in dClient:
            iHit = 1
            lstVLST = []
            lstHitInfo = []
            for _vHitPos, _vNormal, iTarget, iHitPart in dClient['Ray']:
                iVictimState = cls.CheckVictimState(oSkill, dCartoon, iTarget)
                if iVictimState == VICTIM_STATE_BLOCK:
                    oSkill.m_Update['HitStatic'] = 1
                    dCartoon['AllVLST'] = []
                    dCartoon['AllHitInfo'] = []
                    if dCartoon['HitStaticOver']:
                        dCartoon['Pierce'] = 0
                        dCartoon['Over'] = 1
                        break
            
            if 'HitPos' not in dCartoon:
                dCartoon['HitPos'] = []
                dCartoon['HitTimes'] = 0
            dCartoon['HitPos'].append(dCartoon['CurPos'])
            dCartoon['HitTimes'] += 1
            oSkill.m_Update['LastVLST'] = lstVLST
            oSkill.m_Update['HitInfo'] = lstHitInfo
            dNet['Ray'] = dClient['Ray']
            cls.CollectSkillInfo(oSkill, dCartoon)
        if 'Trigger' in dClient:
            dNet['Trigger'] = dClient['Trigger']
        if 'Over' in dClient:
            dCartoon['Over'] = 1
            dNet['Over'] = 1
        oSkill.Send(dCartoon['ID'], dNet)
        if 'Trigger' in dClient:
            cls.Trigger(oSkill)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, StartPos, vDir, fSpeed, fRadius, vAccelerate, tBounciness, iTriggerDelay, iHitOver, iHitStaticOver, *arg, innerRadius = 0, pierce = HIT_OVER_NORMAL, ignoreMonster = OBJ_ENEMY, hitUnitBounciness = (0, 0), targettype = False, hitovertype = 0, iTriggerBullet = 0, **kwargs):
        dCartoon['Start'] = StartPos
        dCartoon['CurPos'] = dCartoon['Start']
        if 'SpeedVector' not in dCartoon:
            vDir = cl_math.Vec3Normalize(vDir)
            dCartoon['SpeedVector'] = cl_math.Vec3MulF(vDir, fSpeed)
        dCartoon['Accelerate'] = vAccelerate
        dCartoon['Bounciness'] = tBounciness
        dCartoon['HitUnitBounciness'] = hitUnitBounciness if hitUnitBounciness[0] or hitUnitBounciness[1] else None
        dCartoon['Radius'] = fRadius
        dCartoon['InnerRadius'] = innerRadius
        dNet = {
            'Start': dCartoon['Start'],
            'SpeedVector': dCartoon['SpeedVector'],
            'Time': iTriggerDelay }
        dCartoon['WaitFrame'] = Time2Frame(iTriggerDelay)
        dCartoon['HitOver'] = iHitOver
        dCartoon['HitStaticOver'] = iHitStaticOver
        dCartoon['Pierce'] = pierce
        dCartoon['TargetType'] = targettype
        dCartoon['IgnoreMonster'] = ignoreMonster
        dCartoon['TriggerBullet'] = iTriggerBullet
        dCartoon['AllVLST'] = []
        dCartoon['Hitovertype'] = hitovertype
        oAttack = oSkill.GetAttack()
        if not oAttack:
            dCartoon['Over'] = 1
            oSkill.Send(dCartoon['ID'], {
                'Over': 1 })
            cls.Disable(oSkill, dCartoon)
            SkillLog.Debug(f'''{oSkill.m_Base['pfid']} throwcrt not attack {oSkill.m_Base['AID']}''')
            return None
        vAttack = oAttack.GetPos()
        if vAttack != StartPos:
            vCheckStart = (vAttack[0], StartPos[1], vAttack[2])
            r = oSkill.m_Game.Scene_RaycastSingle(oSkill.m_Base['Scene'], vCheckStart, StartPos, PXMASK_SKILLBLK, {
                'Normal': 1,
                'PassID': oAttack.m_ID })
            if r[0] != -1:
                vHitPos = r[1]
                dCartoon['Final'] = vHitPos
                dNet['Ray'] = [
                    (vHitPos, r[2], 0, MONSTER_PART_UNTAGGED)]
                cls.HitStatic(oSkill)
                if dCartoon['HitStaticOver']:
                    dCartoon['Over'] = 1
                    dNet['Over'] = 1
                    cls.Disable(oSkill, dCartoon)
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
        iCurFrame = oGame.GetFrameNum()
        iOverTime = 0
        if 'BulletHit' in dCartoon:
            iHit = 1
            dHit = dCartoon['BulletHit']
            iTarget = dHit['Victim']
            iVictimState = cls.CheckVictimState(oSkill, dCartoon, iTarget)
            if iVictimState == VICTIM_STATE_BLOCK:
                oSkill.m_Update['HitStatic'] = 1
                iTarget = 0
                if dCartoon['HitStaticOver']:
                    dCartoon['Over'] = 1
                elif 'normal' in dHit and dHit['normal'][1] <= -0.7:
                    if dCartoon['Hitovertype'] == HIT_OVER_GROUND:
                        iOverTime = 1
                    if 'TriggerStartFrame' not in dCartoon:
                        dCartoon['TriggerStartFrame'] = iCurFrame
                    elif iVictimState == VICTIM_STATE_VALID:
                        if dCartoon['HitOver']:
                            dCartoon['Pierce'] -= cls.GetVictimPierceCost(oSkill, iTarget)
                            if dCartoon['Pierce'] <= 0:
                                dCartoon['Over'] = 1
                        lstVLST = oSkill.m_Update['LastVLST'] if 'LastVLST' in oSkill.m_Update else []
                        lstVLST.append(iTarget)
                        dCartoon['AllVLST'].append(iTarget)
                        oSkill.m_Update['LastVLST'] = lstVLST
            sBouncinessKey = None
            if iTarget and dCartoon['HitUnitBounciness']:
                oVictim = oGame.GetObject(iTarget)
                if oVictim:
                    if oVictim.m_FightType & WARRIOR_HERO == WARRIOR_HERO or oVictim.m_FightType & WARRIOR_MONSTER == WARRIOR_MONSTER:
                        sBouncinessKey = 'HitUnitBounciness'
            (fBouncinessH, fBouncinessV) = dCartoon[sBouncinessKey]
            vSpeedX = fBouncinessH * dHit['speed'][0]
            vSpeedY = fBouncinessV * dHit['speed'][1]
            vSpeedZ = fBouncinessH * dHit['speed'][2]
            vSpeedVector = (vSpeedX, vSpeedY, vSpeedZ)
            oBullet.SetBulletSpeed(vSpeedVector)
            dCartoon.pop('BulletHit')
            dCartoon['SpeedVector'] = vSpeedVector
            dNet['SpeedVector'] = dCartoon['SpeedVector']
            if 'hitpos' in dHit and 'normal' in dHit:
                dNet['Ray'] = [
                    (dHit['hitpos'], dHit['normal'], iTarget, 0)]
            else:
                dNet['Ray'] = [
                    ((0, 0, 0), (0, 0, 0), iTarget, 0)]
        dCartoon['CurPos'] = oBullet.GetBulletPosition()
        dCartoon['Final'] = dCartoon['CurPos']
        if 'DebugRay' in oGame.m_WarMgr.m_Data:
            debug.DebugSphere(oGame, dCartoon['CurPos'], dCartoon['Radius'], debug.LINE_TILE, 65280)
        if 'TriggerStartFrame' in dCartoon or dCartoon['TriggerStartFrame'] + dCartoon['WaitFrame'] <= iCurFrame:
            iOverTime = 1
        elif dCartoon['StartFrame'] + GAME_FRAME * 15 <= iCurFrame:
            iOverTime = 1
        if iOverTime:
            cls.Trigger(oSkill)
            dCartoon['Over'] = 1
            dNet['Trigger'] = 1
        dNet['Start'] = dCartoon['Final']
        oSkill.Send(dCartoon['ID'], dNet)
        return iHit

    HitTargetServer = classmethod(HitTargetServer)
    
    def CollectSkillInfo(cls, oSkill, dCartoon):
        lstCartoonPos = oSkill.m_Collect['CartoonPos'] if 'CartoonPos' in oSkill.m_Collect else []
        vStart = dCartoon['Start']
        vEnd = dCartoon['CurPos']
        lstCartoonPos.append((vStart, vEnd))
        oSkill.m_Collect['CartoonPos'] = lstCartoonPos

    CollectSkillInfo = classmethod(CollectSkillInfo)
    
    def GetVictimPierceCost(cls, oSkill, iVictim):
        iCost = CBaseCartoon.GetVictimPierceCost(oSkill, iVictim)
        if iCost and oSkill.m_CheckType & CRT_CHECK_SERVER:
            oVictim = oSkill.m_Game.GetObject(iVictim)
            if oVictim and oVictim.m_FightType == WARRIOR_STONEPILLAR:
                iCost = 0
        return iCost

    GetVictimPierceCost = classmethod(GetVictimPierceCost)


def ClearCartoon(dCartoon, oSkill):
    dCartoon['cls'].ClearCartoonBullet(oSkill, dCartoon)

