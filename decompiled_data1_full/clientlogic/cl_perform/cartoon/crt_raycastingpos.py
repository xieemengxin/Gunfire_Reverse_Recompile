# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_raycastingpos.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_raycastingpos.pyc
# Source Generated with Decompyle++
# File: crt_raycastingpos.pyc (Python 3.6)

from cl_only import GAME_FRAME_SECOND
from cl_commondefines import CRT_CHECK_SERVER, VICTIM_STATE_VALID, VICTIM_STATE_BLOCK, HITPART_DIRECTPOS, OBJ_ALL, ATT_SHAPE_RECTANGLE, MONSTER_PART_BARRIAR
from cl_pxlayer import PXMASK_SKILLBLK, PXMASK_LIVEOBJ
from cl_object.logging import SkillLog
import cllib.lib_cartoon as cartooncheck
import cl_math
from .mobject import CBaseCartoon

class RayCastingPosCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        if 'Over' in dCartoon:
            return None
        cls.Update(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def Restart(cls, oSkill, dCartoon):
        if oSkill.m_CheckType & CRT_CHECK_SERVER:
            fDisPerFrame = dCartoon['SpeedPerFrame']
            vCur = cl_math.Vec3Mad(dCartoon['CurPos'], dCartoon['Dir'], fDisPerFrame)
            dCartoon['CurPos'] = vCur
            oSkill.Call_Out(1, dCartoon['ID'])

    Restart = classmethod(Restart)
    
    def IsOver(cls, oSkill, dCartoon):
        if oSkill.m_CheckType & CRT_CHECK_SERVER:
            iOver = cls.IsOverServer(oSkill, dCartoon)
        else:
            iOver = cls.IsOverClient(oSkill, dCartoon)
        if iOver:
            oSkill.Send(dCartoon['ID'], {
                'Over': 1 })
        return iOver

    IsOver = classmethod(IsOver)
    
    def InitTraceClient(cls, oSkill, dCartoon, iPierce, fDistance, fSpeed, fInnerRadius, *args, attshape = OBJ_ALL, targettype = ATT_SHAPE_RECTANGLE, **kwargs):
        dCartoon['Pierce'] = iPierce
        dCartoon['Distance'] = fDistance
        dCartoon['SpeedPerFrame'] = fSpeed * GAME_FRAME_SECOND
        dCartoon['TargetType'] = targettype
        dCartoon['Radius'] = fInnerRadius
        iNodeID = dCartoon['ID']
        dClient = oSkill.m_NetReceive[iNodeID]
        dCartoon['End'] = dClient['End']
        dCartoon['Start'] = dClient['Start']
        dCartoon['CurPos'] = dCartoon['Start']
        dCartoon['PierceStatic'] = True
        dNet = {
            'End': dCartoon['End'],
            'Start': dCartoon['Start'] }
        oSkill.Send(dCartoon['ID'], dNet)
        dCartoon['AllVLST'] = []
        dCartoon['AllHitInfo'] = []

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return -1
        dClient = oSkill.m_NetReceive[iNodeID]
        dNet = { }
        iHit = 0
        cartooncheck.CheckDataRayCast(oSkill, dCartoon)
        if 'Ray' in dClient and dCartoon['Pierce'] > 0:
            iHit = 1
            lstVLST = []
            lstSend = []
            lstHitInfo = []
            for vHitPos, vNormal, iVictim, iHitPart in dClient['Ray']:
                iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
                if iVictimState == VICTIM_STATE_BLOCK:
                    lstSend.append((vHitPos, vNormal, 0, iHitPart))
                    oSkill.m_Update['HitStatic'] = 1
                    dNet['HitStatic'] = 1
                    dCartoon['Pierce'] = 0
                    dCartoon['CurPos'] = vHitPos
                elif iVictimState == VICTIM_STATE_VALID:
                    dCartoon['AllVLST'].append(iVictim)
                    lstVLST.append(iVictim)
                dHitInfo = {
                    'Victim': iVictim,
                    'HitPos': vHitPos,
                    'HitArea': HITPART_DIRECTPOS if iHitPart != MONSTER_PART_BARRIAR else iHitPart }
                lstHitInfo.append(dHitInfo)
                dCartoon['AllHitInfo'].append(dHitInfo)
                lstSend.append((vHitPos, vNormal, iVictim, iHitPart))
                dCartoon['CurPos'] = vHitPos
                if dCartoon['Pierce'] <= 0:
                    break
            
            oSkill.m_Update['LastVLST'] = lstVLST
            oSkill.m_Update['HitInfo'] = lstHitInfo
            oSkill.m_Update['CurPos'] = dCartoon['CurPos']
            dNet['Ray'] = lstSend
            oSkill.Send(dCartoon['ID'], dNet)
            cls.CollectSkillInfo(oSkill, dCartoon)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)
    
    def CollectSkillInfo(cls, oSkill, dCartoon):
        lstCartoonPos = oSkill.m_Collect['CartoonPos'] if 'CartoonPos' in oSkill.m_Collect else []
        vStart = dCartoon['Start']
        vEnd = dCartoon['CurPos']
        dCartoon['Final'] = vEnd
        lstCartoonPos.append((vStart, vEnd))
        oSkill.m_Collect['CartoonPos'] = lstCartoonPos

    CollectSkillInfo = classmethod(CollectSkillInfo)
    
    def IsOverClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return 0
        dClient = oSkill.m_NetReceive[iNodeID]
        if 'Over' in dClient and dClient['Over'] == 1:
            return 1
        return 0

    IsOverClient = classmethod(IsOverClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, vStartPos, vEndPos, iPierce, fDistance, fSpeed, fInnerRadius, lstShapeArgs, attshape = ATT_SHAPE_RECTANGLE, targettype = OBJ_ALL, **kwargs):
        dCartoon['Start'] = vStartPos
        dCartoon['End'] = vEndPos
        dCartoon['Pierce'] = iPierce
        dCartoon['Distance'] = fDistance
        dCartoon['SpeedPerFrame'] = fSpeed * GAME_FRAME_SECOND
        dCartoon['TargetType'] = targettype
        dCartoon['InnerRadius'] = fInnerRadius
        dCartoon['ShapeArgs'] = lstShapeArgs
        dCartoon['AttShape'] = attshape
        dCartoon['CurPos'] = vStartPos
        dCartoon['Dir'] = cl_math.Vec3Normalize(cl_math.Vec3Minus(dCartoon['End'], dCartoon['Start']))
        dCartoon['AllVLST'] = []
        dCartoon['AllHitInfo'] = []
        dNet = {
            'End': dCartoon['End'],
            'Start': dCartoon['Start'] }
        oSkill.Send(dCartoon['ID'], dNet)

    InitTraceServer = classmethod(InitTraceServer)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        oGame = oSkill.m_Game
        vStart = dCartoon['Start']
        vDir = dCartoon['Dir']
        vCur = dCartoon['CurPos']
        fInnerRadius = dCartoon['InnerRadius']
        iAttShape = dCartoon['AttShape']
        iScene = oSkill.m_Base['Scene']
        oAttack = oSkill.GetAttack()
        oSkill.m_Update['CurPos'] = dCartoon['CurPos']
        iHit = 0
        dNet = { }
        lstSend = []
        lstArgs = []
        if dCartoon['AttShape'] == ATT_SHAPE_RECTANGLE:
            lstArgs = [
                vCur,
                vDir]
            lstArgs.extend(dCartoon['ShapeArgs'])
        else:
            SkillLog.Alert('暂未支持%d类型检测，请联系程序添加！' % dCartoon['AttShape'])
        lstVictim = []
        if lstArgs:
            lstVictim = cl_math.GetAttackTargetList(oGame, iScene, iAttShape, lstArgs, {
                'Mask': PXMASK_LIVEOBJ })
        if lstVictim:
            lstSend = []
            lstVLST = []
            lstHitInfo = []
            for iVictim in lstVictim:
                iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
                if iVictimState == VICTIM_STATE_VALID:
                    iHit = 1
                    oTarget = oGame.GetObject(iVictim)
                    dCartoon['AllVLST'].append(iVictim)
                    lstVLST.append(iVictim)
                    vPos = oTarget.GetPos()
                    vHitPos = (vPos[0], vPos[1] + oTarget.m_ModelHeight / 2, vPos[2])
                    lstSend.append((vHitPos, (0, 0, 0), iVictim, HITPART_DIRECTPOS))
                    dHitInfo = {
                        'Victim': iVictim,
                        'HitPos': vHitPos,
                        'HitArea': HITPART_DIRECTPOS }
                    lstHitInfo.append(dHitInfo)
                    dCartoon['AllHitInfo'].append(dHitInfo)
            
            oSkill.m_Update['LastVLST'] = lstVLST
            oSkill.m_Update['HitInfo'] = lstHitInfo
        iHitStatic = 0
        if fInnerRadius == 0:
            tRet = oGame.Scene_RaycastSingle(iScene, vStart, vCur, PXMASK_SKILLBLK, {
                'Normal': 1,
                'PassID': oAttack.m_ID })
            if tRet[0] != -1:
                iHitStatic = 1
                vHitPos = tRet[1]
                vNormal = tRet[2]
                lstSend.append((vHitPos, vNormal, 0, 0))
        else:
            lstHitInfo = oGame.Scene_SweepMultiple(iScene, vStart, fInnerRadius, vDir, cl_math.CalDistance3D(vStart, vCur), PXMASK_SKILLBLK, {
                'Normal': 1,
                'PassID': oAttack.m_ID })
            if lstHitInfo:
                iHitStatic = 1
                for iVictim, dInfo in lstHitInfo:
                    lstSend.append((dInfo['Pos'], dInfo['Normal'], iVictim, 0))
                
        if iHitStatic:
            iHit = 1
            dCartoon['Pierce'] = 0
            oSkill.m_Update['HitStatic'] = 1
            dNet['HitStatic'] = 1
        if iHit:
            dNet['Ray'] = lstSend
            oSkill.Send(dCartoon['ID'], dNet)
            cls.CollectSkillInfo(oSkill, dCartoon)
        return iHit

    HitTargetServer = classmethod(HitTargetServer)
    
    def IsOverServer(cls, oSkill, dCartoon):
        iOver = 0
        if dCartoon['Pierce'] <= 0:
            iOver = 1
        elif not cl_math.CheckDistance3D(dCartoon['Start'], dCartoon['CurPos'], dCartoon['Distance']):
            iOver = 1
        return iOver

    IsOverServer = classmethod(IsOverServer)

