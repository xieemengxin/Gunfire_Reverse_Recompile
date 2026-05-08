# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_choosemonster.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_choosemonster.pyc
# Source Generated with Decompyle++
# File: crt_choosemonster.pyc (Python 3.6)

from cl_commondefines import ATT_SHAPE_SECTOR, ATT_SHAPE_SPHERE, ATT_SHAPE_RECTANGLE, HITPART_DIRECTPOS, WARRIOR_MONSTER, VICTIM_STATE_VALID, CHOOSE_NEAREST, CHOOSE_RANDOM
from cl_pxlayer import PXMASK_LIVEOBJ
import cl_math
import cllib.lib_cartoon as cartooncheck
from .mobject import CBaseCartoon

class ChooseMonsterCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        cls.Update(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def HitTarget(cls, oSkill, dCartoon):
        cls.CollectSkillInfo(oSkill, dCartoon)
        return super().HitTarget(oSkill, dCartoon)

    HitTarget = classmethod(HitTarget)
    
    def InitTraceClient(cls, oSkill, dCartoon, lstArgs, attshape = ATT_SHAPE_SECTOR, pierceStatic = False, chooseSelfIfNoTargetInRange = False, iVictim = 0):
        dCartoon['AttShape'] = attshape
        dCartoon['PierceStatic'] = pierceStatic
        dCartoon['ChooseSelf'] = chooseSelfIfNoTargetInRange
        dCartoon['EffArgs'] = lstArgs
        dCartoon['victim'] = iVictim
        dCartoon['AllVLST'] = []
        iNodeID = dCartoon['ID']
        dClient = oSkill.m_NetReceive[iNodeID]
        dCartoon['End'] = dClient['End'] if attshape != ATT_SHAPE_SPHERE else dClient['Start']
        dCartoon['Start'] = dClient['Start']
        dCartoon['CurPos'] = dClient['Start'] if attshape == ATT_SHAPE_SECTOR else dClient['End']
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
        if 'Ray' in dClient:
            iHit = 1
            lstVLST = []
            lstHitInfo = []
            lstRay = dClient['Ray']
            for vHitPos, _, iVictim, _ in lstRay:
                iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
                if iVictimState == VICTIM_STATE_VALID:
                    dCartoon['AllVLST'].append(iVictim)
                    lstVLST.append(iVictim)
                    dHitInfo = {
                        'Victim': iVictim,
                        'HitPos': vHitPos,
                        'HitArea': HITPART_DIRECTPOS }
                    lstHitInfo.append(dHitInfo)
            
            oSkill.m_Update['LastVLST'] = lstVLST
            oSkill.m_Update['HitInfo'] = lstHitInfo
            dNet = {
                'LastVLST': lstVLST }
            oSkill.Send(dCartoon['ID'], dNet)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, StartPos, EndPos, lstArgs, attshape = ATT_SHAPE_SECTOR, pierceStatic = False, ChooseType = CHOOSE_RANDOM, chooseSelfIfNoTargetInRange = False, iVictim = 0):
        dCartoon['Start'] = StartPos
        dCartoon['End'] = EndPos if attshape != ATT_SHAPE_SPHERE else StartPos
        dCartoon['AttShape'] = attshape
        dCartoon['PierceStatic'] = pierceStatic
        dCartoon['ChooseSelf'] = chooseSelfIfNoTargetInRange
        dCartoon['EffArgs'] = lstArgs
        dCartoon['ChooseType'] = ChooseType
        dCartoon['victim'] = iVictim
        dCartoon['CurPos'] = StartPos if attshape == ATT_SHAPE_SECTOR else dCartoon['End']
        if dCartoon['Start'] != dCartoon['End']:
            dCartoon['Dir'] = cl_math.Vec3Normalize(cl_math.Vec3Minus(dCartoon['End'], dCartoon['Start']))
        elif attshape in (ATT_SHAPE_SECTOR, ATT_SHAPE_RECTANGLE):
            oSkill.Send(dCartoon['ID'], {
                'Over': 1 })
            cls.Disable(oSkill, dCartoon)
            return None
        dCartoon['Dir'] = (0, 0, 0)
        dCartoon['Final'] = dCartoon['End']
        dNet = {
            'Start': dCartoon['Start'],
            'End': dCartoon['End'] }
        oSkill.Send(dCartoon['ID'], dNet)

    InitTraceServer = classmethod(InitTraceServer)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        oSkill.m_Update['End'] = dCartoon['End']
        iVictim = cls.ChooseTarget(oSkill, dCartoon)
        dNet = { }
        if iVictim:
            lstVLST = [
                iVictim]
            lstSend = [
                iVictim]
            dHitInfo = {
                'Victim': iVictim,
                'HitArea': HITPART_DIRECTPOS }
            oSkill.m_Update['LastVLST'] = lstVLST
            oSkill.m_Update['HitInfo'] = [
                dHitInfo]
            dNet['LastVLST'] = lstSend
        else:
            dNet['Trigger'] = 1
        oSkill.Send(dCartoon['ID'], dNet)
        if not iVictim:
            cls.Trigger(oSkill)
            return 0
        return 1

    HitTargetServer = classmethod(HitTargetServer)
    
    def ChooseTarget(cls, oSkill, dCartoon):
        lstEffArgs = dCartoon['EffArgs']
        iTrigger = oSkill.m_Custom.get('LockTrigger', 0)
        oGame = oSkill.m_Game
        oTrigger = oGame.GetObject(iTrigger)
        if oTrigger:
            vAttack = oTrigger.GetPos()
            iScene = oTrigger.m_Scene
        else:
            iTrigger = dCartoon['victim']
            vAttack = dCartoon['Start']
            if not iTrigger or not vAttack:
                return 0
            iScene = oSkill.m_Base['Scene']
        if dCartoon['AttShape'] == ATT_SHAPE_SPHERE:
            lstArgs = [
                dCartoon['Start'],
                lstEffArgs[0]]
        elif dCartoon['AttShape'] == ATT_SHAPE_SECTOR:
            lstArgs = [
                dCartoon['Start'],
                dCartoon['Dir']]
            for iArgs in lstEffArgs:
                lstArgs.append(iArgs)
            
        elif dCartoon['AttShape'] == ATT_SHAPE_RECTANGLE:
            lstArgs = [
                dCartoon['Start'],
                dCartoon['Dir']]
            for iArgs in lstEffArgs:
                lstArgs.append(iArgs)
            
        else:
            return 0
        dQArgs = {
            'Mask': PXMASK_LIVEOBJ }
        if dCartoon['PierceStatic']:
            dQArgs['BlockMask'] = 0
        lstHit = cl_math.GetAttackTargetList(oGame, iScene, dCartoon['AttShape'], lstArgs, dQArgs)
        lstTarget = []
        for iVictim in lstHit:
            if iVictim == iTrigger:
                continue
            iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
            if iVictimState == VICTIM_STATE_VALID:
                oVictim = oGame.GetObject(iVictim)
                if not oVictim:
                    continue
                if not oVictim.m_FightType & WARRIOR_MONSTER == WARRIOR_MONSTER:
                    continue
                vVictim = oVictim.GetPos()
                iDis = cl_math.CalDistance3D(vAttack, vVictim)
                lstTarget.append((iDis, iVictim))
        
        if lstTarget:
            if dCartoon['ChooseType'] == CHOOSE_NEAREST:
                lstTarget.sort()
                iTarget = lstTarget[0][1]
                oSkill.m_Base['VID'] = iTarget
                return iTarget
            if dCartoon['ChooseType'] == CHOOSE_RANDOM:
                idx = oGame.Random(len(lstTarget))
                iTarget = lstTarget[idx][1]
                oSkill.m_Base['VID'] = iTarget
                return iTarget
        iState = cls.CheckVictimState(oSkill, dCartoon, iTrigger)
        if dCartoon['ChooseSelf'] and iState == VICTIM_STATE_VALID:
            oSkill.m_Custom['ChooseSelf'] = iTrigger
            oSkill.m_Base['VID'] = iTrigger
            return iTrigger
        return 0

    ChooseTarget = classmethod(ChooseTarget)
    
    def IsOver(cls, oSkill, dCartoon):
        return 1

    IsOver = classmethod(IsOver)
    
    def CollectSkillInfo(cls, oSkill, dCartoon):
        lstCartoonPos = oSkill.m_Collect['CartoonPos'] if 'CartoonPos' in oSkill.m_Collect else []
        vStart = dCartoon['Start']
        vEnd = dCartoon['End']
        lstCartoonPos.append((vStart, vEnd))
        oSkill.m_Collect['CartoonPos'] = lstCartoonPos

    CollectSkillInfo = classmethod(CollectSkillInfo)

