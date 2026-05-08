# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_directpos.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_directpos.pyc
# Source Generated with Decompyle++
# File: crt_directpos.pyc (Python 3.6)

from cl_only import GAME_FRAME_TIME, SendAlert
from cl_commondefines import OBJ_ALL, ATT_SHAPE_SECTOR, ATT_SHAPE_SPHERE, ATT_SHAPE_SPHERICALSHELL, ATT_SHAPE_RECTANGLE, CRT_CHECK_CLIENT, CRT_TYPE_DIRECTPOS, HITPART_DIRECTPOS, MONSTER_PART_BARRIAR, CRT_CHECK_SERVER, VICTIM_STATE_VALID, VICTIM_STATE_HIT, SIDE_TYPE_HERO, ATT_SHAPE_CYLINDER, CRT_EXTCHECK_NONE, CRT_EXTCHECK_SEEDPLANT
from cl_pxlayer import PXMASK_LIVEOBJ, PXMASK_STATIC, PXMASK_SKILLBLK, PXMASK_SIDEBLK, PXMASK_TRANSPARENT, g_PxLayerMap
from cl_object.logging import SkillLog
from C_frgame import CheckDistance3D
import cl_math
import cl_gamedebug as debug
import cllib.lib_cartoon as cartooncheck
import cllib.lib_flag as lib_flag
import cl_msgcenter
import cl_engobjconf
from .mobject import CBaseCartoon
DAMAGE_MERGETIMES = 3

class DirectPosCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        if 'Over' in dCartoon:
            cls.Disable(oSkill, dCartoon)
            return None
        cls.Update(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def HitTarget(cls, oSkill, dCartoon):
        cls.CollectSkillInfo(oSkill, dCartoon)
        return super().HitTarget(oSkill, dCartoon)

    HitTarget = classmethod(HitTarget)
    
    def GetPushStart(cls, oSkill, dCartoon):
        vStart = dCartoon['Start']
        fGroundDis = oSkill.m_Game.Scene_GroundDistance(oSkill.m_Base['Scene'], vStart, 3, PXMASK_STATIC, oSkill.m_Base['AID'])
        vStart = (vStart[0], vStart[1] - fGroundDis, vStart[2])
        return vStart

    GetPushStart = classmethod(GetPushStart)
    
    def InitTraceClient(cls, oSkill, dCartoon, lstArgs, attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ALL, pierceStatic = False, explosion = False, multipleExplode = True, **kwargs):
        dCartoon['AttShape'] = attshape
        dCartoon['TargetType'] = targettype
        dCartoon['PierceStatic'] = pierceStatic
        dCartoon['EffArgs'] = lstArgs
        dCartoon['AllVLST'] = []
        iNodeID = dCartoon['ID']
        dClient = oSkill.m_NetReceive[iNodeID]
        dCartoon['End'] = dClient['End'] if attshape != ATT_SHAPE_SPHERE else dClient['Start']
        dCartoon['Start'] = dClient['Start']
        dCartoon['CurPos'] = dClient['Start'] if attshape == ATT_SHAPE_SECTOR else dClient['End']
        if explosion:
            SendExplosionMsg(oSkill, dCartoon)
        if multipleExplode and 'MultipleExplodeCnt' in oSkill.m_Cache and oSkill.m_Cache['MultipleExplodeCnt']:
            dCartoon['MultipleExplodeCnt'] = oSkill.m_Cache['MultipleExplodeCnt']
            GetTrueMultiExplodeCnt(oSkill, dCartoon)
        if dCartoon['Start'] != dCartoon['End']:
            dCartoon['Dir'] = cl_math.Vec3Normalize(cl_math.Vec3Minus(dCartoon['End'], dCartoon['Start']))
        else:
            dCartoon['Dir'] = (0, 0, 0)
        dCartoon['Final'] = dClient['End']
        dNet = {
            'Start': dClient['Start'],
            'End': dClient['End'] }
        oSkill.Send(dCartoon['ID'], dNet)

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return -1
        cartooncheck.CheckDataRayCast(oSkill, dCartoon)
        dClient = oSkill.m_NetReceive[iNodeID]
        iHit = 0
        oSkill.m_Update['End'] = dCartoon['End']
        oGame = oSkill.m_Game
        if dCartoon['AttShape'] in (ATT_SHAPE_SPHERE, ATT_SHAPE_SPHERICALSHELL) and oGame.m_WarMgr.Query('DebugRay'):
            debug.ClearDebugLine(oGame, debug.LINE_TILE)
            for iArgs in dCartoon['EffArgs']:
                debug.DebugSphere(oGame, dCartoon['Start'], iArgs, debug.LINE_TILE)
                debug.DebugCircle(oGame, dCartoon['Start'], iArgs, debug.LINE_TILE)
            
        if 'Ray' in dClient:
            iHit = 1
            lstVLST = []
            lstHitInfo = []
            if 'MultipleExplodeCnt' in dCartoon:
                if 'CurTimes' not in dCartoon:
                    dCartoon['CurTimes'] = 0
                else:
                    dCartoon['CurTimes'] += 1
                    if dCartoon['CurTimes'] == dCartoon['TrueMultiExplodeCnt'] and dCartoon['MultipleExplodeCnt'] % DAMAGE_MERGETIMES:
                        dCartoon['CopyTimes'] = dCartoon['MultipleExplodeCnt'] % DAMAGE_MERGETIMES - 1
                    elif dCartoon['CurTimes'] == 1:
                        dCartoon['CopyTimes'] = DAMAGE_MERGETIMES - 1
            lstRay = dClient['Ray']
            for vHitPos, _, iVictim, iHitPart in lstRay:
                iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
                if not iVictimState == VICTIM_STATE_VALID:
                    if iVictimState == VICTIM_STATE_HIT and 'TrueMultiExplodeCnt' in dCartoon:
                        lstVLST.append(iVictim)
                dHitInfo = {
                    'Victim': iVictim,
                    'HitPos': vHitPos,
                    'HitArea': HITPART_DIRECTPOS if iHitPart != MONSTER_PART_BARRIAR else iHitPart }
                lstHitInfo.append(dHitInfo)
                if iVictimState == VICTIM_STATE_HIT and iVictim in dCartoon['AllVLST']:
                    continue
                dCartoon['AllVLST'].append(iVictim)
            
            oSkill.m_Update['LastVLST'] = lstVLST
            oSkill.m_Update['HitInfo'] = lstHitInfo
            dNet = {
                'LastVLST': lstVLST }
            oSkill.Send(dCartoon['ID'], dNet)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, StartPos, EndPos, lstArgs, attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ALL, pierceStatic = False, explosion = False, multipleExplode = True, explosionDelay = 10, extCheck = CRT_EXTCHECK_NONE, **kwargs):
        dCartoon['Start'] = StartPos
        dCartoon['End'] = EndPos if attshape != ATT_SHAPE_SPHERE else StartPos
        dCartoon['AttShape'] = attshape
        dCartoon['TargetType'] = targettype
        dCartoon['PierceStatic'] = pierceStatic
        dCartoon['EffArgs'] = lstArgs
        dCartoon['AllVLST'] = []
        dCartoon['CrtType'] = CRT_TYPE_DIRECTPOS
        dCartoon['Mask'] = PXMASK_LIVEOBJ
        if extCheck == CRT_EXTCHECK_SEEDPLANT:
            dCartoon['Mask'] = dCartoon['Mask'] | PXMASK_TRANSPARENT
        dCartoon['CurPos'] = StartPos if attshape == ATT_SHAPE_SECTOR else dCartoon['End']
        if dCartoon['Start'] != dCartoon['End']:
            dCartoon['Dir'] = cl_math.Vec3Normalize(cl_math.Vec3Minus(dCartoon['End'], dCartoon['Start']))
        elif attshape in (ATT_SHAPE_SECTOR, ATT_SHAPE_RECTANGLE):
            oSkill.Send(dCartoon['ID'], {
                'Over': 1 })
            dCartoon['Over'] = 1
            return None
        dCartoon['Dir'] = (0, 0, 0)
        dCartoon['Final'] = dCartoon['End']
        dNet = {
            'Start': dCartoon['Start'],
            'End': dCartoon['End'] }
        if multipleExplode and 'MultipleExplodeCnt' in oSkill.m_Cache and oSkill.m_Cache['MultipleExplodeCnt']:
            dCartoon['MultipleExplodeCnt'] = oSkill.m_Cache['MultipleExplodeCnt']
            GetTrueMultiExplodeCnt(oSkill, dCartoon)
            iExplosionDelay = explosionDelay // GAME_FRAME_TIME
            if iExplosionDelay < 1:
                SendAlert('err', '技能%d DirectPosCartoon配置的explosionDelay为%d百分秒，小于1帧(4百分秒)，请检查' % (oSkill.m_Base['pfid'], explosionDelay))
                iExplosionDelay = 1
            dCartoon['ExplosionDelay'] = iExplosionDelay
            dNet['Count'] = dCartoon['MultipleExplodeCnt']
        if explosion:
            SendExplosionMsg(oSkill, dCartoon)
        if 'LockTarget' in oSkill.m_Custom:
            dNet['LockTarget'] = oSkill.m_Custom['LockTarget']
        oSkill.Send(dCartoon['ID'], dNet)

    InitTraceServer = classmethod(InitTraceServer)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        oSkill.m_Update['End'] = dCartoon['End']
        if 'MultipleExplodeCnt' in dCartoon:
            if 'CurTimes' not in dCartoon:
                dCartoon['CurTimes'] = 0
                dCartoon['lstVictim'] = cls.GetAllTarget(oSkill, dCartoon)
            else:
                dCartoon['CurTimes'] += 1
                if dCartoon['CurTimes'] == dCartoon['TrueMultiExplodeCnt'] and dCartoon['MultipleExplodeCnt'] % DAMAGE_MERGETIMES:
                    dCartoon['CopyTimes'] = dCartoon['MultipleExplodeCnt'] % DAMAGE_MERGETIMES - 1
                elif dCartoon['CurTimes'] == 1:
                    dCartoon['CopyTimes'] = DAMAGE_MERGETIMES - 1
            lstVictim = dCartoon['lstVictim']
        else:
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
        lstEffArgs = dCartoon['EffArgs']
        vStart = dCartoon['Start']
        if dCartoon['AttShape'] in (ATT_SHAPE_SPHERE, ATT_SHAPE_SPHERICALSHELL):
            if oGame.m_WarMgr.Query('DebugRay'):
                debug.ClearDebugLine(oGame, debug.LINE_TILE)
                for iArgs in lstEffArgs:
                    debug.DebugSphere(oGame, vStart, iArgs, debug.LINE_TILE)
                    debug.DebugCircle(oGame, vStart, iArgs, debug.LINE_TILE)
                
            lstArgs = [
                vStart]
            lstArgs.extend(lstEffArgs)
        elif dCartoon['AttShape'] == ATT_SHAPE_SECTOR:
            iAngle = lstEffArgs[-1]
            if iAngle > 180 and oSkill.m_Base['pfid'] == 1304:
                dCartoon['AttShape'] = ATT_SHAPE_SPHERE
                lstArgs = [
                    vStart,
                    lstEffArgs[0]]
            elif oGame.m_WarMgr.Query('DebugRay'):
                debug.ClearDebugLine(oGame, debug.LINE_TILE)
                vDir = cl_math.RotateAroundVector(dCartoon['Dir'], (0, -1, 0), lstEffArgs[2] // 2)
                vDir = cl_math.Vec3MulV(vDir, (1, 0, 1))
                debug.DebugSector(oGame, vStart, lstEffArgs[0], vDir, lstEffArgs[2], debug.LINE_TILE)
                debug.DebugSector(oGame, (vStart[0], vStart[1] + lstEffArgs[1], vStart[2]), lstEffArgs[0], vDir, lstEffArgs[2], debug.LINE_TILE)
            lstArgs = [
                vStart,
                dCartoon['Dir']]
            lstArgs.extend(lstEffArgs)
        elif dCartoon['AttShape'] == ATT_SHAPE_RECTANGLE:
            if oGame.m_WarMgr.Query('DebugRay'):
                (fLength, fWidth, fHeight) = lstEffArgs
                debug.ClearDebugLine(oGame, debug.LINE_BOX)
                debug.DebugBox(oGame, vStart, dCartoon['Dir'], fLength, fWidth, fHeight)
            lstArgs = [
                vStart,
                dCartoon['Dir']]
            lstArgs.extend(lstEffArgs)
        elif dCartoon['AttShape'] == ATT_SHAPE_CYLINDER:
            if oGame.m_WarMgr.Query('DebugRay'):
                debug.ClearDebugLine(oGame, debug.LINE_TILE)
                debug.DebugCylinder(oGame, vStart, lstEffArgs[0], lstEffArgs[1], debug.LINE_TILE)
            lstArgs = [
                vStart]
            lstArgs.extend(lstEffArgs)
        else:
            return []
        iMask = dCartoon['Mask']
        if 'IgnoreLayer' in oSkill.m_Custom:
            lstIgnoreLayer = oSkill.m_Custom['IgnoreLayer']
            for iIgnoreLayer in lstIgnoreLayer:
                if iMask & iIgnoreLayer:
                    iMask -= iIgnoreLayer
            
        dQArgs = {
            'Mask': iMask }
        if oSkill.m_Cache['Side'] != SIDE_TYPE_HERO:
            dQArgs['BlockMask'] = PXMASK_SIDEBLK
        else:
            dQArgs['BlockMask'] = PXMASK_SKILLBLK
        if dCartoon['PierceStatic']:
            dQArgs['BlockMask'] = 0
        iScene = oSkill.m_Base['Scene']
        lstHit = cl_math.GetAttackTargetList(oGame, iScene, dCartoon['AttShape'], lstArgs, dQArgs)
        oScene = oGame.m_SceneMgr.GetScene(iScene)
        if oScene and 'SpecalSphericalTarget' in oScene.m_CustomData:
            setSpecialTarget = oScene.m_CustomData['SpecalSphericalTarget']
            for iTarget in setSpecialTarget:
                if iTarget in lstHit:
                    continue
                oTarget = oGame.GetObject(iTarget)
                if not oTarget:
                    continue
                (_, _, iLayer) = cl_engobjconf.GetEngineObjConf(oTarget.m_FightType)
                if iLayer not in g_PxLayerMap:
                    continue
                iTargetMark = g_PxLayerMap[iLayer][2]
                if not iTargetMark & iMask:
                    continue
                iRadius = oTarget.m_ModelData.GetModelRadius()
                if CheckDistance3D(oTarget.GetPos(), vStart, iRadius):
                    lstHit.add(iTarget)
            
        if not lib_flag.g_UseNewRectangle:
            bIsOffSet = True if not dQArgs['BlockMask'] else False
            if dCartoon['AttShape'] == ATT_SHAPE_RECTANGLE and not bIsOffSet:
                lstHit2 = cl_math.GetAttackTargetList(oGame, oSkill.m_Base['Scene'], dCartoon['AttShape'], lstArgs, dQArgs, bIsOffSet)
                lstNewHit = []
                for iVictim in lstHit:
                    if iVictim not in lstHit2:
                        continue
                    lstNewHit.append(iVictim)
                
                lstHit = lstNewHit
        lstTarget = []
        for iVictim in lstHit:
            iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
            if not iVictimState == VICTIM_STATE_VALID:
                if iVictimState == VICTIM_STATE_HIT and 'TrueMultiExplodeCnt' in dCartoon:
                    lstTarget.append(iVictim)
                    if iVictimState == VICTIM_STATE_HIT and iVictim in dCartoon['AllVLST']:
                        continue
                    dCartoon['AllVLST'].append(iVictim)
                    continue
        
        return lstTarget

    GetAllTarget = classmethod(GetAllTarget)
    
    def Restart(cls, oSkill, dCartoon):
        if oSkill.m_CheckType & CRT_CHECK_SERVER:
            oSkill.Call_Out(dCartoon['ExplosionDelay'], dCartoon['ID'])

    Restart = classmethod(Restart)
    
    def IsOver(cls, oSkill, dCartoon):
        if 'TrueMultiExplodeCnt' in dCartoon:
            iOver = 0
            iNodeID = dCartoon['ID']
            if (iNodeID in oSkill.m_NetReceive or 'Over' in oSkill.m_NetReceive[iNodeID] or 'CurTimes' in dCartoon) and dCartoon['CurTimes'] >= dCartoon['TrueMultiExplodeCnt']:
                iOver = 1
            if iOver:
                oSkill.Send(dCartoon['ID'], {
                    'Over': 1 })
            return iOver
        return 1

    IsOver = classmethod(IsOver)
    
    def CollectSkillInfo(cls, oSkill, dCartoon):
        lstCartoonPos = oSkill.m_Collect['CartoonPos'] if 'CartoonPos' in oSkill.m_Collect else []
        vStart = dCartoon['Start']
        vEnd = dCartoon['End']
        lstCartoonPos.append((vStart, vEnd))
        oSkill.m_Collect['CartoonPos'] = lstCartoonPos

    CollectSkillInfo = classmethod(CollectSkillInfo)


def GetTrueMultiExplodeCnt(oSkill, dCartoon):
    dCartoon['TrueMultiExplodeCnt'] = dCartoon['MultipleExplodeCnt'] // DAMAGE_MERGETIMES
    if dCartoon['MultipleExplodeCnt'] % DAMAGE_MERGETIMES:
        dCartoon['TrueMultiExplodeCnt'] += 1


def SendExplosionMsg(oSkill, dCartoon):
    radius = 0
    if oSkill.m_CheckType & CRT_CHECK_CLIENT:
        radius = oSkill.m_Cache['Radius']
    elif dCartoon['AttShape'] == ATT_SHAPE_SPHERE:
        lstEffArgs = dCartoon['EffArgs']
        radius = lstEffArgs[0]
    else:
        SkillLog.Alert('目前非球形爆炸，还不支持发送【造成爆炸】消息，请联系程序确认。')
        return None
    dData = {
        'Skill': oSkill,
        'Start': dCartoon['Start'],
        'End': dCartoon['End'],
        'Radius': radius }
    if radius <= 0:
        SkillLog.Alert('%d radius is %s' % (oSkill.m_Base['pfid'], radius))
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_EXPLOSION, oSkill.m_Game.GetObject(oSkill.m_Base['AID']), dData)

