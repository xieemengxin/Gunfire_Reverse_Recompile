# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_delegatecollidedtrigger.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_delegatecollidedtrigger.pyc
# Source Generated with Decompyle++
# File: crt_delegatecollidedtrigger.pyc (Python 3.6)

from cl_only import GAME_FRAME, Time2Frame
from cl_commondefines import OBJ_ALL, ATT_SHAPE_SECTOR, PUSH_TYPE_NORMAL_MOVE, PUSH_TYPE_FOLLOW_ATTACKER, PUSH_TYPE_MOVE_STAND, PUSH_TYPE_FOLLOW_SERVANT, HITPART_DIRECTPOS, MONSTER_PART_BARRIAR, VICTIM_STATE_VALID
from cl_only import Functor
import cllib.lib_cartoon as cartooncheck
import cl_summon.barriersummon
import cl_msgcenter
import cl_math
from .mobject import CBaseCartoon

class DelegateCollidedTriggerCartoon(CBaseCartoon):
    m_WorldLineOutFrame = 2 * GAME_FRAME
    
    def HitTarget(cls, oSkill, dCartoon):
        return cls.HitTargetClient(oSkill, dCartoon)

    HitTarget = classmethod(HitTarget)
    
    def InitTraceServer(cls, oSkill, dCartoon, StartPos, EndPos, speed, triggerTimes, totalTime, innerRadius, lstArgs, attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ALL, pushtype = PUSH_TYPE_NORMAL_MOVE, standtime = 0, summonsid = 0, *args, **kwargs):
        dCartoon['Start'] = StartPos
        dCartoon['End'] = EndPos
        dCartoon['CurPos'] = StartPos
        dCartoon['Speed'] = speed
        dCartoon['TriggerTimes'] = max(triggerTimes, 1)
        dCartoon['AttShape'] = attshape
        dCartoon['TargetType'] = targettype
        dCartoon['EffArgs'] = lstArgs
        dCartoon['PushType'] = pushtype
        iWaitFrame = Time2Frame(totalTime)
        dCartoon['WaitFrame'] = iWaitFrame
        dCartoon['InnerRadius'] = innerRadius
        iStandFrame = Time2Frame(standtime)
        dCartoon['StandFrame'] = iStandFrame
        dCartoon['SummonSID'] = summonsid
        oAttack = oSkill.GetAttack()
        dCartoon['ClientSource'] = oAttack.m_Owner if oAttack.m_Owner else oAttack.m_ID
        oSkill.Send(dCartoon['ID'], { })
        iTotalFrame = iWaitFrame + iStandFrame + 2
        dCartoon['DealFrame'] = oSkill.m_Game.GetFrameNum() + iTotalFrame
        oSkill.Call_Out(iTotalFrame, dCartoon['ID'], dCartoon['Casting'])

    InitTraceServer = classmethod(InitTraceServer)
    
    def Trace(cls, oSkill, dCartoon):
        iPushType = dCartoon['PushType']
        if iPushType == PUSH_TYPE_MOVE_STAND:
            oAttack = oSkill.GetAttack()
            oGame = oSkill.m_Game
            clsSummonData = oGame.m_WarData.GetSummonData(dCartoon['SummonSID'])
            dAddInfo = {
                'Owner': oSkill.m_Base['AID'],
                'ObjShape': clsSummonData.m_Shape,
                'SrcPerform': oSkill.m_Base['pfid'],
                'Side': oSkill.m_Cache['Side'],
                'SendMsgTarget': oAttack.m_Owner if oAttack else 0 }
            oSummon = clsSummonData.Create(oSkill.m_Game, dAddInfo)
            if not oSummon:
                oSkill.Halt('Summon')
                return None
            oSummon.SetOwner(oAttack)
            vEuler = cl_math.Dir2Radians(oAttack.GetFacing())
            oSummon.Goto(oSkill.m_Base['Scene'], oAttack.GetPos(), tEuler = vEuler)
            dCartoon['SummonID'] = oSummon.m_ID
            dCartoon['FollowID'] = oSummon.m_ID
            oSkill.AddEndFunc(Functor(ClearCartoon, dCartoon))
            dNet = {
                'EntityID': oSummon.m_ID }
            oSkill.Send(dCartoon['ID'], dNet)
        elif iPushType == PUSH_TYPE_FOLLOW_SERVANT:
            oAttack = oSkill.GetAttack()
            oOwner = oAttack.GetOwner()
            if not oOwner or not (oOwner.m_Servant):
                oSkill.Halt('Servant')
                return None
            oServant = oSkill.m_Game.GetObject(oOwner.m_Servant)
            dCartoon['FollowID'] = oServant.m_ID
            dNet = {
                'EntityID': oServant.m_ID }
            oSkill.Send(dCartoon['ID'], dNet)

    Trace = classmethod(Trace)
    
    def IsOver(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        iOver = 0
        if 'Over' in dCartoon:
            iOver = 1
        elif oSkill.m_Game.GetFrameNum() >= dCartoon['DealFrame']:
            iOver = 1
        if iOver:
            ClearCartoon(dCartoon, oSkill)
            oSkill.Send(iNodeID, {
                'Over': 1 })
            return 1
        return 0

    IsOver = classmethod(IsOver)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return 0
        dClient = oSkill.m_NetReceive[iNodeID]
        if dClient['Source'] != dCartoon['ClientSource']:
            return 0
        iHit = 0
        iPushType = dCartoon['PushType']
        dNet = { }
        if 'Ray' in dClient:
            iHit = 1
            lstVLST = []
            lstHitInfo = []
            lstSend = []
            oAttack = oSkill.GetAttack()
            if iPushType == PUSH_TYPE_NORMAL_MOVE:
                cartooncheck.CheckDataRayCast(oSkill, dCartoon)
                dCartoon['CurPos'] = dClient['End']
            else:
                cartooncheck.CheckPosAround(oSkill, dCartoon)
                if iPushType == PUSH_TYPE_FOLLOW_ATTACKER:
                    dCartoon['CurPos'] = oAttack.GetPos()
            oOwner = oAttack.GetOwner()
            for vHitPos, vNormal, iVictim, iHitPart in dClient['Ray']:
                iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
                if iVictimState == VICTIM_STATE_VALID:
                    lstVLST.append(iVictim)
                dHitInfo = {
                    'Victim': iVictim,
                    'HitPos': vHitPos,
                    'HitArea': HITPART_DIRECTPOS if iHitPart != MONSTER_PART_BARRIAR else iHitPart }
                lstHitInfo.append(dHitInfo)
                lstSend.append((vHitPos, vNormal, iVictim, iHitPart))
                if oOwner:
                    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_BARRIER_COLLIDED, oOwner, {
                        'AID': oAttack.m_Owner,
                        'VID': iVictim,
                        'dArgs': { } })
            
            oSkill.m_Update['LastVLST'] = lstVLST
            oSkill.m_Update['HitInfo'] = lstHitInfo
            dNet['Ray'] = lstSend
            oSkill.Send(dCartoon['ID'], dNet)
        if iPushType == PUSH_TYPE_MOVE_STAND and 'Offset' in dClient:
            vPos = dClient['Offset']
            oGame = oSkill.m_Game
            oSummon = oGame.GetObject(dCartoon['SummonID'])
            if oSummon:
                oSummon.m_Game.Scene_Walk(oSummon.m_ID, vPos)
            if 'FlyOverDis' in dClient:
                if 'HitStatic' in dClient:
                    dNet['HitStatic'] = dClient['HitStatic']
                    if oSummon:
                        tEuler = oSummon.GetEuler()
                        oSummon.SetEuler((0, tEuler[1], 0))
                dNet['FlyOverDis'] = dClient['FlyOverDis']
                dNet['End'] = dClient['End']
                iStandFrame = dCartoon['StandFrame'] + 2
                dCartoon['DealFrame'] = oSkill.m_Game.GetFrameNum() + iStandFrame
                oSkill.Call_Out(iStandFrame, dCartoon['ID'], dCartoon['Casting'])
        if 'Over' in dClient:
            dCartoon['Over'] = 1
        if dNet:
            oSkill.Send(dCartoon['ID'], dNet)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)


def ClearCartoon(dCartoon, oSkill):
    if 'SummonID' in dCartoon:
        iSummonID = dCartoon.pop('SummonID')
        oSummon = oSkill.m_Game.GetObject(iSummonID)
        if oSummon:
            oSummon.ScenesRemoveDelay('CartoonOver')

