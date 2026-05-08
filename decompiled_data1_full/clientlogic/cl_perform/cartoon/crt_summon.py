# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_summon.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_summon.pyc
# Source Generated with Decompyle++
# File: crt_summon.pyc (Python 3.6)

from cl_only import Second2Frame, Time2Frame, GAME_FRAME, GAME_FRAME_SECOND, Functor
from cl_commondefines import CRT_CHECK_CLIENT, MODEL_TYPE_CTRLAGENT, VICTIM_STATE_BLOCK, VICTIM_STATE_VALID
from cl_pxlayer import PXMASK_STATIC
import cl_math
import cl_summon.performsummon
from .mobject import CBaseCartoon

class SummonCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        if oSkill.m_CheckType & CRT_CHECK_CLIENT:
            oGame = oSkill.m_Game
            oAttack = oSkill.GetAttack()
            dAddInfo = {
                'Owner': oSkill.m_Base['AID'],
                'Shape': MODEL_TYPE_CTRLAGENT,
                'ObjShape': dCartoon['SummonShape'],
                'ClientOwner': oAttack.m_ID,
                'BuffData': dCartoon['BuffData'],
                'NeglectAttack': True,
                'SrcPerform': oSkill.m_Base['pfid'] }
            clsSummonData = cl_summon.performsummon.CPerformSummonData
            oSummon = clsSummonData.Create(oGame, dAddInfo)
            if not oSummon:
                oSkill.Halt('nosummon')
                return None
            oSummon.Goto(oSkill.m_Base['Scene'], dCartoon['Start'], dCartoon['Dir'])
            if dCartoon['ClientSummonId']:
                oAttack.SetClientSummon(dCartoon['ClientSummonId'], oSummon.m_ID)
            else:
                oAttack.CreateClientSummon(oSummon.m_ID)
            dCartoon['SummonID'] = oSummon.m_ID
            dCartoon['Radius'] = oSummon.m_ModelData.GetModelRadius()
            oSkill.Call_Out(1, dCartoon['ID'])
            iTimeoutFrame = dCartoon['MoveFrame'] + dCartoon['DurationFrame'] + GAME_FRAME * 5
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
            iSummonID = dCartoon['SummonID']
            oSummon = oSkill.m_Game.GetObject(iSummonID)
            if not oSummon:
                cls.Disable(oSkill, dCartoon)
                return 0
            oSummon.Remove('Hit')
            dCartoon['Final'] = dCartoon['CurPos']
            oSkill.Send(iNodeID, {
                'Over': 1 })
            return 1
        return 0

    IsOver = classmethod(IsOver)
    
    def Restart(cls, oSkill, dCartoon):
        if 'Stopped' in dCartoon or 'TimerUpdate' not in dCartoon:
            return None
        dCartoon.pop('TimerUpdate')
        if oSkill.m_CheckType & CRT_CHECK_CLIENT:
            vCur = dCartoon['CurPos']
            vDir = dCartoon['Dir']
            vTar = cl_math.Vec3Mad(vCur, vDir, dCartoon['SpeedPerFrame'])
            if cl_math.CheckDistance3D(dCartoon['Start'], vTar, dCartoon['Distance']):
                oGame = oSkill.m_Game
                vTar2 = cl_math.Vec3DisplaceDir(vTar, dCartoon['Dir'], dCartoon['Radius'])
                bAnyHit = oGame.Scene_RaycastAnyHit(oSkill.m_Base['Scene'], vCur, vTar2, PXMASK_STATIC)
                if not bAnyHit:
                    oSummon = oGame.GetObject(dCartoon['SummonID'])
                    if not oSummon:
                        cls.Disable(oSkill, dCartoon)
                        return None
                    oSummon.WalkTo(vTar)
                    dCartoon['CurPos'] = vTar
                else:
                    dCartoon['Stopped'] = 1
                    return None
                oSkill.Call_Out(1, dCartoon['ID'])

    Restart = classmethod(Restart)
    
    def InitTraceClient(cls, oSkill, dCartoon, iSummonShape, fRadius, fDistance, fSpeed, iDurationTime, dBuff, effect = 0):
        dCartoon['SummonShape'] = iSummonShape
        dCartoon['Distance'] = fDistance
        dCartoon['SpeedPerFrame'] = fSpeed * GAME_FRAME_SECOND
        dCartoon['MoveFrame'] = Second2Frame(fDistance / fSpeed)
        dCartoon['DurationFrame'] = Time2Frame(iDurationTime)
        dCartoon['BuffData'] = dBuff
        iNodeID = dCartoon['ID']
        dClient = oSkill.m_NetReceive[iNodeID]
        dCartoon['End'] = dClient['End']
        dCartoon['Start'] = dClient['Start']
        dCartoon['Dir'] = cl_math.Vec3Normalize(cl_math.Vec3Minus(dCartoon['End'], dCartoon['Start']))
        dCartoon['CurPos'] = dCartoon['Start']
        dCartoon['ClientSummonId'] = dClient.get('ClientSummonId', 0)
        dNet = {
            'End': dCartoon['End'] }
        if 'MuzzlePos' not in dCartoon or dCartoon['MuzzlePos'] != dCartoon['Start']:
            dNet['Start'] = dCartoon['Start']
        oSkill.Send(dCartoon['ID'], dNet)

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            if dCartoon['OverFrame'] < oSkill.m_Game.GetFrameNum():
                dCartoon['Over'] = 1
            else:
                dCartoon['TimerUpdate'] = 1
            return 0
        iHit = 0
        dClient = oSkill.m_NetReceive[iNodeID]
        if 'LastVLST' in dClient:
            lstVLST = []
            for iTarget in dClient['LastVLST']:
                iVictimState = cls.CheckVictimState(oSkill, dCartoon, iTarget)
                if iVictimState == VICTIM_STATE_BLOCK:
                    oSkill.m_Update['HitStatic'] = 1
                    dCartoon['Over'] = 1
                    continue
                if iVictimState == VICTIM_STATE_VALID:
                    lstVLST.append(iTarget)
                    dCartoon['Over'] = 1
            
            oSkill.m_Update['LastVLST'] = lstVLST
            iHit = 1
        oSkill.Send(dCartoon['ID'], dClient)
        if 'Trigger' in dClient:
            cls.Trigger(oSkill)
            dCartoon['Over'] = 1
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


def ClearCartoon(dCartoon, oSkill):
    if 'SummonID' in dCartoon:
        iSummonID = dCartoon.pop('SummonID')
        oSummon = oSkill.m_Game.GetObject(iSummonID)
        if oSummon:
            oSummon.ScenesRemoveDelay('CartoonOver')

