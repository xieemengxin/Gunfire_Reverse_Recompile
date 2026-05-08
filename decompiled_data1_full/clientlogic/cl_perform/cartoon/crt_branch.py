# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_branch.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_branch.pyc
# Source Generated with Decompyle++
# File: crt_branch.pyc (Python 3.6)

from cl_commondefines import VICTIM_STATE_VALID, OBJ_ENEMY, MONSTER_PART_UNTAGGED, CRT_CHECK_SERVER, ATT_SHAPE_RECTANGLE, ATT_SHAPE_SPHERE
from cl_pxlayer import PXMASK_MONSTER, PXMASK_SKILLBLK
from cl_only import Second2Frame
from .mobject import CBaseCartoon
import cllib.lib_cartoon as cartooncheck
import cl_math

class BranchCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        if 'Over' in dCartoon:
            return None
        cls.Update(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def InitTraceClient(cls, oSkill, dCartoon, vStart, vEnd, attshape, shapeargs, iTargetNums, *args, **kwargs):
        dCartoon['TargetType'] = OBJ_ENEMY
        dCartoon['Start'] = vStart
        dCartoon['End'] = vEnd
        dCartoon['TargetNums'] = iTargetNums
        dCartoon['AttShape'] = attshape
        dCartoon['EffArgs'] = shapeargs
        dCartoon['CurPos'] = dCartoon['Start']
        dCartoon['PierceStatic'] = True

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return -1
        dClient = oSkill.m_NetReceive[iNodeID]
        cartooncheck.CheckDataRayCast(oSkill, dCartoon)
        dNet = { }
        iHit = 0
        if 'Ray' in dClient:
            iHit = 1
            lstVLST = []
            lstSend = []
            lstHitInfo = []
            lstRay = dClient['Ray']
            iSumTimes = dCartoon['TargetNums']
            for vHitPos, vNormal, iVictim, iHitPart in lstRay:
                dCartoon['CurPos'] = vHitPos
                iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
                if iVictimState == VICTIM_STATE_VALID:
                    dCartoon['TargetNums'] -= 1
                    lstVLST.append(iVictim)
                    dHitInfo = {
                        'Victim': iVictim,
                        'HitPos': vHitPos,
                        'HitArea': MONSTER_PART_UNTAGGED }
                    lstHitInfo.append(dHitInfo)
                    lstSend.append((vHitPos, vNormal, iVictim, iHitPart))
                    dCartoon['Final'] = vHitPos
                if dCartoon['TargetNums'] <= 0:
                    break
            
            oSkill.m_Collect['RemainTimes'] = dCartoon['TargetNums']
            oSkill.m_Collect['HitTimes'] = iSumTimes - dCartoon['TargetNums']
            oSkill.m_Update['LastVLST'] = lstVLST
            oSkill.m_Update['HitInfo'] = lstHitInfo
            dNet['Ray'] = lstSend
        if 'Trigger' in dClient:
            lstAllTarget = []
            if 'LockTarget' in dClient:
                for iVictim in dClient['LockTarget']:
                    iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
                    if iVictimState == VICTIM_STATE_VALID:
                        lstAllTarget.append(iVictim)
                
                dNet['LockTarget'] = lstAllTarget
            dCartoon['AllTarget'] = lstAllTarget
            dNet['Trigger'] = 1
            cls.Trigger(oSkill)
        oSkill.Send(iNodeID, dNet)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)
    
    def Restart(cls, oSkill, dCartoon):
        if oSkill.m_CheckType & CRT_CHECK_SERVER:
            oSkill.Call_Out(dCartoon['IntervalFrame'], dCartoon['ID'])

    Restart = classmethod(Restart)
    
    def InitTraceServer(cls, oSkill, dCartoon, vStart, vEnd, attshape, shapeargs, iPierce, fDelayTime, *args, **kwargs):
        dCartoon['TargetType'] = OBJ_ENEMY
        dCartoon['Start'] = vStart
        oMainHit = oSkill.m_Game.GetObject(oSkill.m_Base['VID'])
        if oMainHit and oMainHit.GetPos() == vEnd:
            vEnd = oMainHit.GetCenter()
        dCartoon['End'] = vEnd
        dCartoon['Dir'] = cl_math.Vec3Normalize(cl_math.Vec3Minus(dCartoon['End'], dCartoon['Start']))
        dCartoon['InitPierce'] = iPierce
        dCartoon['Pierce'] = iPierce
        dCartoon['AttShape'] = attshape
        dCartoon['EffArgs'] = shapeargs
        dCartoon['CurPos'] = dCartoon['Start']
        dCartoon['PierceStatic'] = True
        dCartoon['IntervalFrame'] = Second2Frame(fDelayTime)

    InitTraceServer = classmethod(InitTraceServer)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        if 'AllHitInfo' not in dCartoon:
            iHit = 0
            cls.OnRetard(oSkill, dCartoon)
        else:
            iHit = cls.OnTrueHit(oSkill, dCartoon)
        return iHit

    HitTargetServer = classmethod(HitTargetServer)
    
    def OnRetard(cls, oSkill, dCartoon):
        iScene = oSkill.m_Base['Scene']
        vStart = dCartoon['Start']
        (iMainHit, vMainHitPos, vMainHitNormal) = oSkill.m_Game.Scene_RaycastSingle(iScene, vStart, dCartoon['End'], PXMASK_MONSTER, {
            'Normal': 1,
            'BlockMask': PXMASK_SKILLBLK })
        (fLength, fWidth, fHeight) = dCartoon['EffArgs']
        lstRectangleHit = cl_math.GetAttackTargetList(oSkill.m_Game, iScene, ATT_SHAPE_RECTANGLE, [
            vStart,
            dCartoon['Dir'],
            fLength,
            fWidth,
            fHeight], {
            'Mask': PXMASK_MONSTER,
            'PassID': iMainHit,
            'BlockMask': PXMASK_SKILLBLK })
        iPierce = dCartoon['Pierce']
        if iMainHit <= 0:
            for iRectangleHit in lstRectangleHit:
                oRectangleHit = oSkill.m_Game.GetObject(iRectangleHit)
                if not oRectangleHit:
                    continue
                iMainHit = iRectangleHit
                vMainHitPos = oRectangleHit.GetCenter()
                vMinusPos = cl_math.Vec3Minus(vStart, vMainHitPos)
                vMainHitNormal = cl_math.Vec3Normalize(vMinusPos)
            else:
                dCartoon['Pierce'] = 0
                return None
            lstRectangleHit.remove(iMainHit)
        lstSphereHit = cl_math.GetAttackTargetList(oSkill.m_Game, iScene, ATT_SHAPE_SPHERE, [
            vMainHitPos,
            4], {
            'Mask': PXMASK_MONSTER,
            'PassID': iMainHit,
            'BlockMask': PXMASK_SKILLBLK })
        setMinorHit = set(lstRectangleHit).union(set(lstSphereHit))
        dAllHit = {
            iMainHit: [
                vMainHitPos,
                vMainHitNormal,
                0] }
        dNet = { }
        for iMinorHit in setMinorHit:
            iVictimState = cls.CheckVictimState(oSkill, dCartoon, iMinorHit)
            if iVictimState != VICTIM_STATE_VALID:
                continue
            oMinorHit = oSkill.m_Game.GetObject(iMinorHit)
            vMinorHitPos = oMinorHit.GetCenter()
            vMinusPos = cl_math.Vec3Minus(vStart, vMinorHitPos)
            vMinoHitNormal = cl_math.Vec3Normalize(vMinusPos)
            iDis = cl_math.CalDistance3D(vStart, vMinorHitPos)
            dAllHit[iMinorHit] = [
                vMinorHitPos,
                vMinoHitNormal,
                iDis]
        
        if len(dAllHit) > iPierce:
            lstAllHit = sorted(dAllHit.items(), key = (lambda x: x[1][2]))
            dAllHit = dict(lstAllHit[:iPierce])
        lstAllTarget = list(dAllHit.keys())
        dNet['LockTarget'] = lstAllTarget
        dCartoon['AllTarget'] = lstAllTarget
        dCartoon['AllHitInfo'] = dAllHit
        dNet['Trigger'] = 1
        cls.Trigger(oSkill)
        oSkill.Send(dCartoon['ID'], dNet)

    OnRetard = classmethod(OnRetard)
    
    def OnTrueHit(cls, oSkill, dCartoon):
        dAllHitInfo = dCartoon['AllHitInfo']
        lstVLST = []
        lstSend = []
        lstHitInfo = []
        dNet = { }
        iHitPart = MONSTER_PART_UNTAGGED
        dCartoon['Pierce'] = 0
        for iVictim, (vHitPos, vNormal, _) in dAllHitInfo.items():
            dCartoon['CurPos'] = vHitPos
            iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
            if iVictimState != VICTIM_STATE_VALID:
                continue
            lstVLST.append(iVictim)
            dHitInfo = {
                'Victim': iVictim,
                'HitPos': vHitPos,
                'HitArea': MONSTER_PART_UNTAGGED }
            lstHitInfo.append(dHitInfo)
            lstSend.append((vHitPos, vNormal, iVictim, iHitPart))
            dCartoon['Final'] = vHitPos
        
        oSkill.m_Collect['RemainTimes'] = dCartoon['InitPierce']
        oSkill.m_Collect['HitTimes'] = len(lstSend)
        oSkill.m_Update['LastVLST'] = lstVLST
        oSkill.m_Update['HitInfo'] = lstHitInfo
        dNet['Ray'] = lstSend
        oSkill.Send(dCartoon['ID'], dNet)
        if lstSend:
            return 1
        return 0

    OnTrueHit = classmethod(OnTrueHit)
    
    def IsOver(cls, oSkill, dCartoon):
        iOver = 0
        iNodeID = dCartoon['ID']
        if oSkill.m_CheckType & CRT_CHECK_SERVER or dCartoon['Pierce'] <= 0:
            iOver = 1
        else:
            dClient = oSkill.m_NetReceive[iNodeID]
            if 'Over' in dClient and dClient['Over'] == 1:
                iOver = 1
        if iOver:
            oSkill.Send(iNodeID, {
                'Over': 1 })
            return 1
        return 0

    IsOver = classmethod(IsOver)

