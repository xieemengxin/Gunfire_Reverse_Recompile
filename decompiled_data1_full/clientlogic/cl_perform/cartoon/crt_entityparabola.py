# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_entityparabola.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_entityparabola.pyc
# Source Generated with Decompyle++
# File: crt_entityparabola.pyc (Python 3.6)

from cl_only import Time2Frame
from cl_commondefines import CRT_CHECK_CLIENT, CRT_CHECK_SERVER, OBJ_ENEMY, WARRIOR_HERO, WARRIOR_MONSTER, VICTIM_STATE_BLOCK, VICTIM_STATE_VALID, MODEL_TYPE_SPHERE
from cl_pxlayer import PXLAYER_RBULLET, PXLAYER_RBULLET_NOMONS, PXLAYER_RBULLET_OUTER, PXLAYER_RBULLET_OUTER_NOMONS, PXLAYER_RBULLET_INNER
import cl_scene
import cl_math
import cl_engphyobj
from .mobject import CBaseCartoon

class EntityParabolaCartoon(CBaseCartoon):
    
    def IsOver(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if oSkill.m_CheckType & CRT_CHECK_SERVER:
            iOver = cls.IsOverServer(oSkill, dCartoon)
        else:
            iOver = cls.IsOverClient(oSkill, dCartoon)
        if iOver:
            oSkill.Send(iNodeID, {
                'Over': 1 })
        return iOver

    IsOver = classmethod(IsOver)
    
    def Trace(cls, oSkill, dCartoon):
        if oSkill.m_CheckType & CRT_CHECK_CLIENT:
            return None
        oGame = oSkill.m_Game
        fRadius = dCartoon['Radius']
        if dCartoon['InitSummon'] == -1:
            oSummon = None
        elif dCartoon['InitSummon'] == 0:
            vPos = dCartoon['Start']
            iScene = oSkill.m_Base['Scene']
            dAddInfo = {
                'Owner': oSkill.m_Base['AID'],
                'Shape': MODEL_TYPE_SPHERE,
                'Angle': (0, 0, 0),
                'Center': (0, 0, 0),
                'Scale': (dCartoon['Scale'], dCartoon['Scale'], dCartoon['Scale']),
                'Size': (fRadius, fRadius, fRadius),
                'Side': oSkill.m_Cache['Side'],
                'Origin': vPos,
                'SrcPerform': oSkill.m_Base['pfid'] }
            oSummon = oGame.m_ResMgr.CreateSummon(iScene, dCartoon['SummonSID'], dAddInfo)
            if oSummon:
                iSummon = oSummon.m_ID
            else:
                iSummon = 0
            dCartoon['SummonID'] = iSummon
        else:
            oSummon = oGame.GetObject(dCartoon['SummonID'])
        if not oSummon:
            dCartoon['Over'] = 1
        else:
            tSkillCheckArgs = (oSummon.SkillCheckArgs[0] * dCartoon['Scale'], oSummon.SkillCheckArgs[1] * dCartoon['Scale'])
            oSummon.SetSkillCheckArgs(tSkillCheckArgs[0], tSkillCheckArgs[1])
            dBulletParam = {
                'TraceIdx': oSkill.m_Base['PFKey'],
                'Speed': dCartoon['SpeedVector'],
                'AccSpeed': dCartoon['Accelerate'],
                'PassID': oSkill.m_Base['AID'] }
            iInnerRadius = dCartoon['InnerRadius']
            if iInnerRadius > 0:
                iOuterLayer = PXLAYER_RBULLET_OUTER_NOMONS if dCartoon['IgnoreMonster'] else PXLAYER_RBULLET_OUTER
                oBullet = cl_engphyobj.CreateDoubleAttachBullet(oGame, oSummon, dBulletParam, PXLAYER_RBULLET_INNER, {
                    'Shape': MODEL_TYPE_SPHERE,
                    'Radius': iInnerRadius }, iOuterLayer, {
                    'Shape': MODEL_TYPE_SPHERE,
                    'Radius': fRadius * dCartoon['Scale'] })
            elif dCartoon['IgnoreMonster']:
                pass
            
            iLayer = PXLAYER_RBULLET
            oBullet = cl_engphyobj.CreateAttachBullet(oGame, oSummon, dBulletParam, iLayer, {
                'Shape': MODEL_TYPE_SPHERE,
                'Radius': fRadius * dCartoon['Scale'] })
            oGame.m_SkillMgr.RegisterBullet(oBullet, oSkill.m_Base['AID'], oSkill.m_Base['ActNum'], dCartoon['ID'])
            dCartoon['BulletKey'] = oBullet.Key()
        cls.Update(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def Restart(cls, oSkill, dCartoon):
        if oSkill.m_CheckType & CRT_CHECK_SERVER:
            oSkill.Call_Out(1, dCartoon['ID'])

    Restart = classmethod(Restart)
    
    def CollectSkillInfo(cls, oSkill, dCartoon):
        lstCartoonPos = oSkill.m_Collect['CartoonPos'] if 'CartoonPos' in oSkill.m_Collect else []
        vStart = dCartoon['Start']
        vEnd = dCartoon['Final'] if 'Final' in dCartoon else dCartoon['CurPos']
        lstCartoonPos.append((vStart, vEnd))
        oSkill.m_Collect['CartoonPos'] = lstCartoonPos

    CollectSkillInfo = classmethod(CollectSkillInfo)
    
    def ClearCartoonBullet(cls, oSkill, dCartoon):
        if not dCartoon['InitSummon'] and 'SummonID' in dCartoon:
            iSummonID = dCartoon.pop('SummonID')
            oSummon = oSkill.m_Game.GetObject(iSummonID)
            if oSummon:
                oSummon.ScenesRemoveDelay('CartoonOver')
        super().ClearCartoonBullet(oSkill, dCartoon)

    ClearCartoonBullet = classmethod(ClearCartoonBullet)
    
    def IsOverClient(cls, oSkill, dCartoon):
        return True

    IsOverClient = classmethod(IsOverClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, vStart, vDir, fSpeed, fRadius, vAccelerate, tBounciness, tHitUnitBounciness, iTriggerDelay, iHitOver, iHitStaticOver, iPierce, bIgnoreMonster, iSummonID, iSummonSID, targetType = OBJ_ENEMY, maxDistance = 0, hitHeroOver = False, forceSpeed = False, innerRadius = 0, scale = 1, hitmonsterover = False, *arg, **kwargs):
        if 'SpeedVector' not in dCartoon:
            vDir = cl_math.Vec3Normalize(vDir)
            dCartoon['Dir'] = vDir
            dCartoon['SpeedVector'] = cl_math.Vec3MulF(vDir, fSpeed)
        else:
            dCartoon['Dir'] = cl_math.Vec3Normalize(dCartoon['SpeedVector'])
        dCartoon['Accelerate'] = vAccelerate
        dCartoon['Bounciness'] = tBounciness
        dCartoon['HitUnitBounciness'] = tHitUnitBounciness if tHitUnitBounciness[0] != 0 or tHitUnitBounciness[1] != 0 else None
        dCartoon['ForceSpeed'] = forceSpeed
        dCartoon['HitOver'] = iHitOver
        dCartoon['HitStaticOver'] = iHitStaticOver
        dCartoon['HitHeroOver'] = hitHeroOver
        dCartoon['IgnoreMonster'] = bIgnoreMonster
        dCartoon['HitMonsterOver'] = hitmonsterover
        dCartoon['Pierce'] = iPierce
        dCartoon['TargetType'] = targetType
        if iSummonID:
            oSummon = oSkill.m_Game.GetObject(iSummonID)
            if not oSummon:
                dCartoon['Over'] = 1
                dCartoon['SummonID'] = 0
                dCartoon['Start'] = (0, 0, 0)
                dCartoon['Radius'] = 0
                dCartoon['InitSummon'] = -1
            else:
                dCartoon['InitSummon'] = iSummonID
                dCartoon['SummonID'] = iSummonID
                dCartoon['SummonSID'] = oSummon.m_SID
                dCartoon['Radius'] = fRadius if fRadius > 0 else oSummon.m_ModelRadius
                dCartoon['Start'] = oSummon.GetPos()
        else:
            dCartoon['InitSummon'] = 0
            dCartoon['Start'] = vStart
            dCartoon['SummonSID'] = iSummonSID
            dCartoon['Radius'] = fRadius
            dCartoon['SummonID'] = 0
        dCartoon['InnerRadius'] = innerRadius
        dCartoon['CurPos'] = dCartoon['Start']
        dCartoon['WaitFrame'] = Time2Frame(iTriggerDelay)
        dCartoon['AllVLST'] = []
        dCartoon['Distance'] = maxDistance
        dCartoon['Scale'] = scale
        dNet = {
            'Start': dCartoon['Start'],
            'Time': iTriggerDelay }
        oSkill.Send(dCartoon['ID'], dNet)

    InitTraceServer = classmethod(InitTraceServer)
    
    def IsOverServer(cls, oSkill, dCartoon):
        oSkill.m_Update['EPFPos'] = dCartoon['Final'] if 'Final' in dCartoon else dCartoon['CurPos']
        iNodeID = dCartoon['ID']
        iOver = 0
        if 'Over' in dCartoon:
            iOver = 1
        elif not oSkill.m_Game.GetObject(dCartoon['SummonID']):
            iOver = 1
        elif dCartoon['Distance'] > 0 and not cl_math.CheckDistance3D(dCartoon['Start'], dCartoon['CurPos'], dCartoon['Distance'] - dCartoon['Radius']):
            iOver = 1
        if iOver:
            cls.ClearCartoonBullet(oSkill, dCartoon)
            oSkill.Send(iNodeID, {
                'Over': 1 })
            return 1
        return 0

    IsOverServer = classmethod(IsOverServer)
    
    def AddHitTarget(cls, oSkill, dCartoon, iTarget, dHit):
        if 'Over' in dCartoon:
            return None
        dHit['Victim'] = iTarget
        dCartoon['BulletHit'] = dHit

    AddHitTarget = classmethod(AddHitTarget)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        oGame = oSkill.m_Game
        iSummonID = dCartoon['SummonID']
        if iSummonID:
            oSummon = oGame.GetObject(iSummonID)
            if oSummon:
                oSummon.RefreshPos()
                cl_scene.GS2CMapGoto(oSummon, oSummon.GetPos())
        if 'Over' in dCartoon:
            return 0
        dNet = { }
        oBullet = oGame.m_SkillMgr.GetBullet(dCartoon['BulletKey'])
        iHit = 0
        if 'BulletHit' in dCartoon:
            iHit = 1
            dHit = dCartoon['BulletHit']
            dCartoon.pop('BulletHit')
            iTarget = dHit['Victim']
            iVictimState = cls.CheckVictimState(oSkill, dCartoon, iTarget)
            if iVictimState == VICTIM_STATE_BLOCK:
                oSkill.m_Update['HitStatic'] = 1
                iTarget = 0
                if dCartoon['HitStaticOver']:
                    dCartoon['Over'] = 1
                elif iVictimState == VICTIM_STATE_VALID:
                    if dCartoon['HitOver']:
                        dCartoon['Over'] = 1
                    else:
                        oVictim = oGame.GetObject(iTarget)
                        if oVictim:
                            if dCartoon['HitHeroOver'] and oVictim.m_FightType & WARRIOR_HERO:
                                dCartoon['Over'] = 1
                            elif dCartoon['HitMonsterOver'] and oVictim.m_FightType & WARRIOR_MONSTER:
                                dCartoon['Over'] = 1
                    lstVLST = oSkill.m_Update['LastVLST'] if 'LastVLST' in oSkill.m_Update else []
                    lstVLST.append(iTarget)
                    dCartoon['AllVLST'].append(iTarget)
                    oSkill.m_Update['LastVLST'] = lstVLST
            if not None['ForceSpeed']:
                sBouncinessKey = 'Bounciness'
                if iTarget and dCartoon['HitUnitBounciness']:
                    oVictim = oGame.GetObject(iTarget)
                    if oVictim:
                        if oVictim.m_FightType & WARRIOR_HERO or oVictim.m_FightType & WARRIOR_MONSTER:
                            sBouncinessKey = 'HitUnitBounciness'
                (fBouncinessH, fBouncinessV) = dCartoon[sBouncinessKey]
                vSpeedX = fBouncinessH * dHit['speed'][0]
                vSpeedY = fBouncinessV * dHit['speed'][1]
                vSpeedZ = fBouncinessH * dHit['speed'][2]
                vSpeedVector = (vSpeedX, vSpeedY, vSpeedZ)
                oBullet.SetBulletSpeed(vSpeedVector)
                dCartoon['SpeedVector'] = vSpeedVector
                dNet['SpeedVector'] = dCartoon['SpeedVector']
            dNet['Ray'] = [
                (dHit['hitpos'], dHit['normal'], iTarget, 0)]
        if oBullet:
            dCartoon['CurPos'] = oBullet.GetBulletPosition()
            dCartoon['Final'] = dCartoon['CurPos']
            if dCartoon['ForceSpeed']:
                oBullet.SetBulletSpeed(dCartoon['SpeedVector'])
            else:
                dCartoon['Over'] = 1
        if None['StartFrame'] + dCartoon['WaitFrame'] <= oSkill.m_Game.GetFrameNum():
            cls.Trigger(oSkill)
            dCartoon['Over'] = 1
            dNet['Trigger'] = 1
        dNet['Start'] = dCartoon['Final']
        oSkill.Send(dCartoon['ID'], dNet)
        return iHit

    HitTargetServer = classmethod(HitTargetServer)

