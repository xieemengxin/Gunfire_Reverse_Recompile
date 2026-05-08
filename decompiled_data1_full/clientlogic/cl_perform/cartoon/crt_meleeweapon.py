# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_meleeweapon.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_meleeweapon.pyc
# Source Generated with Decompyle++
# File: crt_meleeweapon.pyc (Python 3.6)

from cl_commondefines import OBJ_ALL, ATT_SHAPE_SECTOR, HITPART_DIRECTPOS, VICTIM_STATE_VALID, VICTIM_STATE_BLOCK, MONSTER_PART_BARRIAR, MONSTER_PART_WEAKNESS
from cl_pxlayer import PXMASK_STATIC
from cl_object.logging import SkillLog
import cl_math
import cl_gamedebug as debug
import cllib.lib_cartoon as cartooncheck
from .mobject import CBaseCartoon

class MeleeWeaponCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        cls.Update(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def GetPushStart(cls, oSkill, dCartoon):
        vStart = dCartoon['Start']
        fGroundDis = oSkill.m_Game.Scene_GroundDistance(oSkill.m_Base['Scene'], vStart, 3, PXMASK_STATIC, oSkill.m_Base['AID'])
        vStart = (vStart[0], vStart[1] - fGroundDis, vStart[2])
        return vStart

    GetPushStart = classmethod(GetPushStart)
    
    def InitTraceClient(cls, oSkill, dCartoon, lstArgs, meshCount, totalTime, attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ALL, pierceStatic = False, left2right = True, *args, **kwargs):
        dCartoon['AttShape'] = attshape
        dCartoon['MeshCount'] = meshCount
        dCartoon['TotalTime'] = totalTime
        dCartoon['TargetType'] = targettype
        dCartoon['PierceStatic'] = pierceStatic
        dCartoon['Left2Right'] = left2right
        dCartoon['EffArgs'] = lstArgs
        dCartoon['AllVLST'] = []
        iNodeID = dCartoon['ID']
        dClient = oSkill.m_NetReceive[iNodeID]
        dCartoon['End'] = dClient['End']
        dCartoon['Start'] = dClient['Start']
        dCartoon['CurPos'] = dClient['Start']
        dCartoon['Final'] = dClient['End']
        dCartoon['CanCritical'] = kwargs['canCritical'] if 'canCritical' in kwargs else False
        dNet = {
            'Start': dClient['Start'],
            'End': dClient['End'] }
        oSkill.Send(dCartoon['ID'], dNet)
        if oSkill.m_Game.m_WarMgr.Query('DebugRay'):
            debug.ClearDebugLine(oSkill.m_Game, debug.LINE_TILE)

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return -1
        dClient = oSkill.m_NetReceive[iNodeID]
        if 'Start' not in dClient or 'End' not in dClient:
            oAttack = oSkill.GetAttack()
            SkillLog.Error('%s %s melee no start' % (oAttack.m_PlayerID, oSkill.m_Base['pfid']))
            return 0
        oGame = oSkill.m_Game
        vStart = dClient['Start']
        vEnd = dClient['End']
        dCartoon['Start'] = vStart
        dCartoon['End'] = vEnd
        dCartoon['CurPos'] = vStart
        dCartoon['Final'] = vStart
        cartooncheck.CheckDataRayCast(oSkill, dCartoon)
        if dCartoon['AttShape'] == ATT_SHAPE_SECTOR and oGame.m_WarMgr.Query('DebugRay'):
            lstEffArgs = dCartoon['EffArgs'][:2]
            lstEffArgs.append(dCartoon['EffArgs'][2] // dCartoon['MeshCount'])
            vDir = cl_math.Vec3Minus(vEnd, vStart)
            vDir = cl_math.RotateAroundVector(vDir, (0, -1, 0), lstEffArgs[2] // 2)
            debug.DebugSector(oGame, vStart, lstEffArgs[0], vDir, lstEffArgs[2], debug.LINE_TILE)
            debug.DebugSector(oGame, (vStart[0], vStart[1] + lstEffArgs[1], vStart[2]), lstEffArgs[0], vDir, lstEffArgs[2], debug.LINE_TILE)
        iHit = 0
        if 'Ray' in dClient:
            iHitFrame = dClient['Frame']
            oAttack = oSkill.GetAttack()
            vAttack = oGame.GetLastPos(oSkill.m_Base['AID'], iHitFrame)
            if abs(vAttack[1] - vStart[1]) > 1.5 * oAttack.m_ModelHeight or not cl_math.CheckDistance(vAttack, vStart, 3 * oAttack.m_ModelRadius):
                sInfo = '%s %s melee start invalid %s %s %s %s %s %s' % (oAttack.m_PlayerID, oSkill.m_Base['pfid'], oGame.GetFrameNum(), iHitFrame, vAttack, vStart, oAttack.m_ModelHeight, oAttack.m_ModelRadius)
                SkillLog.Debug(sInfo)
            iHit = 1
            dNet = { }
            lstVLST = []
            lstHitInfo = []
            lstSend = []
            lstRay = dClient['Ray']
            for vHitPos, vNormal, iVictim, iHitPart in lstRay:
                iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
                if iVictimState == VICTIM_STATE_VALID:
                    lstSend.append((vHitPos, vNormal, iVictim, iHitPart))
                    dCartoon['AllVLST'].append(iVictim)
                    lstVLST.append(iVictim)
                    if iHitPart == MONSTER_PART_BARRIAR:
                        iHitArea = MONSTER_PART_BARRIAR
                    elif dCartoon['CanCritical'] and iHitPart == MONSTER_PART_WEAKNESS:
                        iHitArea = MONSTER_PART_WEAKNESS
                    else:
                        iHitArea = HITPART_DIRECTPOS
                    dHitInfo = {
                        'Victim': iVictim,
                        'HitPos': vHitPos,
                        'HitArea': iHitArea }
                    lstHitInfo.append(dHitInfo)
                elif iVictimState == VICTIM_STATE_BLOCK:
                    lstSend.append((vHitPos, vNormal, 0, iHitPart))
                    oSkill.m_Update['HitStatic'] = 1
                    dNet['HitStatic'] = 1
            
            oSkill.m_Update['LastVLST'] = lstVLST
            oSkill.m_Update['HitInfo'] = lstHitInfo
            oSkill.m_Update['CurPos'] = dCartoon['CurPos']
            dNet['Ray'] = lstSend
            oSkill.Send(dCartoon['ID'], dNet)
            cls.CollectSkillInfo(oSkill, dCartoon)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, StartPos, EndPos, lstArgs, meshCount, totalTime, attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ALL, pierceStatic = False, explosion = False):
        pass

    InitTraceServer = classmethod(InitTraceServer)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        return 0

    HitTargetServer = classmethod(HitTargetServer)
    
    def IsOver(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return -1
        dClient = oSkill.m_NetReceive[iNodeID]
        if 'Over' in dClient and dClient['Over'] == 1:
            oSkill.Send(iNodeID, {
                'Over': 1 })
            return 1
        return 0

    IsOver = classmethod(IsOver)
    
    def CollectSkillInfo(cls, oSkill, dCartoon):
        lstCartoonPos = oSkill.m_Collect['CartoonPos'] if 'CartoonPos' in oSkill.m_Collect else []
        vStart = dCartoon['Start']
        vEnd = dCartoon['End']
        lstCartoonPos.append((vStart, vEnd))
        oSkill.m_Collect['CartoonPos'] = lstCartoonPos

    CollectSkillInfo = classmethod(CollectSkillInfo)

