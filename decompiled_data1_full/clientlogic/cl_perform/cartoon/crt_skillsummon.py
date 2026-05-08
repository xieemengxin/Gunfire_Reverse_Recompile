# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_skillsummon.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_skillsummon.pyc
# Source Generated with Decompyle++
# File: crt_skillsummon.pyc (Python 3.6)

from cl_only import Second2Frame, Time2Frame, GAME_FRAME, GAME_FRAME_SECOND, Functor, SendAlert
from cl_commondefines import CRT_CHECK_CLIENT, VICTIM_STATE_BLOCK, MODEL_TYPE_CTRLAGENT, VICTIM_STATE_VALID, VICTIM_STATE_HIT
import cl_math
import cllib.lib_cartoon as cartooncheck
from .mobject import CBaseCartoon

class SkillSummonCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        if oSkill.m_CheckType & CRT_CHECK_CLIENT:
            oGame = oSkill.m_Game
            vPos = dCartoon['Start']
            oAttack = oSkill.GetAttack()
            iSrcWeapon = oSkill.m_Base['Weapon']
            clsSummonData = oGame.m_ResMgr.m_WarData.GetSummonData(dCartoon['SummonSID'])
            dAddInfo = {
                'Owner': oSkill.m_Base['AID'],
                'Shape': MODEL_TYPE_CTRLAGENT,
                'ObjShape': dCartoon['SummonShape'] if dCartoon['SummonShape'] else clsSummonData.m_Shape,
                'ClientOwner': oAttack.m_ID,
                'BuffData': { },
                'Angle': (0, 0, 0),
                'Origin': vPos,
                'NeglectAttack': False,
                'Weapon': iSrcWeapon }
            oSummon = clsSummonData.Create(oGame, dAddInfo)
            if oSummon:
                oSummon.m_ClientSummonID = dCartoon['ClientSummonId']
                oAttack.SetClientSummon(dCartoon['ClientSummonId'], oSummon.m_ID)
                oSummon.Goto(oSkill.m_Base['Scene'], dCartoon['Start'], dCartoon['Dir'])
                dCartoon['SummonID'] = oSummon.m_ID
                dCartoon['Radius'] = oSummon.m_ModelData.GetModelRadius()
            oSkill.Call_Out(1, dCartoon['ID'])
            iTimeoutFrame = dCartoon['LiveFrame'] + GAME_FRAME * 5
            dCartoon['OverFrame'] = dCartoon['StartFrame'] + iTimeoutFrame
            oSkill.AddEndFunc(Functor(ClearCartoon, dCartoon))
            oSkill.Call_Out(iTimeoutFrame, dCartoon['ID'])

    Trace = classmethod(Trace)
    
    def IsOver(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        iOver = 0
        if 'Over' in dCartoon:
            iOver = 1
        if iOver:
            oSummon = oSkill.m_Game.GetObject(dCartoon['SummonID'])
            if oSummon:
                oSummon.Remove('Over')
            dCartoon['Final'] = dCartoon['CurPos']
            oSkill.Send(iNodeID, {
                'Over': 1 })
            return 1
        return 0

    IsOver = classmethod(IsOver)
    
    def InitTraceClient(cls, oSkill, dCartoon, iPierce, iSummonShape, iSummon, fRadius, fDistance, fSpeed, iLivetime, **kwargs):
        dCartoon['SummonSID'] = iSummon
        dCartoon['SummonShape'] = iSummonShape
        dCartoon['Pierce'] = iPierce
        dCartoon['Distance'] = fDistance
        dCartoon['SpeedPerFrame'] = fSpeed * GAME_FRAME_SECOND
        dCartoon['MoveFrame'] = Second2Frame(fDistance / fSpeed)
        dCartoon['LiveFrame'] = Time2Frame(iLivetime)
        iHitInterval = kwargs['hitInterval'] if 'hitInterval' in kwargs else 0
        dCartoon['HitInterval'] = iHitInterval
        dCartoon['HitIntervalFrame'] = Time2Frame(iHitInterval)
        dCartoon['TargetType'] = kwargs['targettype']
        if dCartoon['HitInterval'] > 0 and dCartoon['HitIntervalFrame'] == 0:
            SendAlert('err', '技能%d SkillSummonCartoon配置的HitInterval %d 过小' % (oSkill.m_Base['pfid'], dCartoon['HitInterval']))
        iNodeID = dCartoon['ID']
        dClient = oSkill.m_NetReceive[iNodeID]
        dCartoon['End'] = dClient['End']
        dCartoon['Start'] = dClient['Start']
        dCartoon['Dir'] = cl_math.Vec3Normalize(cl_math.Vec3Minus(dCartoon['End'], dCartoon['Start']))
        dCartoon['CurPos'] = dCartoon['Start']
        dCartoon['AllVLST'] = []
        dCartoon['AllHitInfo'] = []
        dCartoon['ClientSummonId'] = dClient['ClientSummonId']
        dNet = {
            'End': dCartoon['End'] }
        if 'MuzzlePos' not in dCartoon or dCartoon['MuzzlePos'] != dCartoon['Start']:
            dNet['Start'] = dCartoon['Start']
        if 'Over' in dClient:
            dCartoon['Over'] = 1
            dNet['Over'] = 1
        oSkill.Send(dCartoon['ID'], dNet)

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            if dCartoon['LiveFrame'] > 0 and dCartoon['OverFrame'] < oSkill.m_Game.GetFrameNum():
                dCartoon['Over'] = 1
            return 0
        iHit = 0
        dClient = oSkill.m_NetReceive[iNodeID]
        iSummonID = dCartoon['SummonID']
        oSummon = oSkill.m_Game.GetObject(iSummonID)
        if not oSummon:
            dCartoon['Over'] = 1
        elif 'Start' in dClient:
            oSummon.WalkTo(dClient['Start'])
        dNet = { }
        if 'Trigger' in dClient:
            dCartoon['AllVLST'] = []
            dCartoon['AllHitInfo'] = []
            oSkill.m_Update['Trigger'] = 1
        if 'Touch' in dClient and dCartoon['Pierce'] > 0:
            iHit = 1
            lstVLST = []
            lstSend = []
            lstHitInfo = []
            dTouch = { }
            iHitFrame = dClient['Frame']
            for vHitPos, vNormal, iVictim, iHitPart, iTouch in dClient['Touch']:
                iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
                if not CheckHitInterval(oSkill, dCartoon, iVictim, iHitFrame, dCartoon['HitIntervalFrame'], iTouch):
                    pass
                bCheckHit = cls.CheckValidDamage(dCartoon, iVictim, iHitPart)
                if iVictimState == VICTIM_STATE_HIT and bCheckHit:
                    iVictimState = VICTIM_STATE_VALID
                if iVictimState == VICTIM_STATE_BLOCK:
                    lstSend.append((vHitPos, vNormal, 0, iHitPart, iTouch))
                    oSkill.m_Update['HitStatic'] = 1
                    dNet['HitStatic'] = 1
                    dCartoon['Pierce'] = 0
                    dCartoon['CurPos'] = vHitPos
                elif iVictimState == VICTIM_STATE_VALID or iTouch:
                    dTouch[iVictim] = 1
                    dCartoon['Pierce'] -= cls.GetVictimPierceCost(oSkill, iVictim)
                dCartoon['AllVLST'].append(iVictim)
                lstVLST.append(iVictim)
                dHitInfo = {
                    'Victim': iVictim,
                    'HitPos': vHitPos,
                    'HitArea': iHitPart,
                    'HitFrame': iHitFrame }
                lstHitInfo.append(dHitInfo)
                dCartoon['AllHitInfo'].append(dHitInfo)
                lstSend.append((vHitPos, vNormal, iVictim, iHitPart, iTouch))
                dCartoon['CurPos'] = vHitPos
                dCartoon['Final'] = vHitPos
                if dCartoon['Pierce'] <= 0:
                    break
            
            oSkill.m_Update['LastVLST'] = lstVLST
            oSkill.m_Update['HitInfo'] = lstHitInfo
            oSkill.m_Update['Touch'] = dTouch
            dNet['Touch'] = lstSend
            oSkill.Send(dCartoon['ID'], dNet)
        if 'End' in dClient:
            dCartoon['Final'] = dClient['End']
        cls.CollectSkillInfo(oSkill, dCartoon)
        if 'Trigger' in dClient:
            cls.Trigger(oSkill)
        if 'Over' in dClient:
            dCartoon['Over'] = 1
        return iHit

    HitTargetClient = classmethod(HitTargetClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, iSummon, fRadius, fDistance, fSpeed, iDurationTime, effect = 0):
        pass

    InitTraceServer = classmethod(InitTraceServer)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        return 0

    HitTargetServer = classmethod(HitTargetServer)
    
    def CollectSkillInfo(cls, oSkill, dCartoon):
        lstCartoonPos = oSkill.m_Collect['CartoonPos'] if 'CartoonPos' in oSkill.m_Collect else []
        vStart = dCartoon['Start']
        if 'Final' in dCartoon:
            vEnd = dCartoon['Final']
        else:
            fRadius = dCartoon['Radius']
            vEnd = dCartoon['CurPos'] if fRadius == 0 else cl_math.Vec3Mad(dCartoon['CurPos'], dCartoon['Dir'], fRadius)
        lstCartoonPos.append((vStart, vEnd))
        oSkill.m_Collect['CartoonPos'] = lstCartoonPos

    CollectSkillInfo = classmethod(CollectSkillInfo)


def ClearCartoon(dCartoon, oSkill):
    if 'SummonID' in dCartoon:
        iSummonID = dCartoon.pop('SummonID')
        oSummon = oSkill.m_Game.GetObject(iSummonID)
        if oSummon:
            oSummon.ScenesRemoveDelay('CartoonOver')


def CheckHitInterval(oSkill, dCartoon, iVictim, iHitFrame, iHitIntervalFrame, iTouch):
    if iTouch:
        return True
    if iHitIntervalFrame == 0:
        return False
    if 'AllHitInfo' not in dCartoon:
        return False
    for dHitInfo in dCartoon['AllHitInfo']:
        if dHitInfo['Victim'] != iVictim:
            continue
        if iHitFrame < dHitInfo['HitFrame'] + iHitIntervalFrame:
            return False
    
    return True

