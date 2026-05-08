# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_subduction.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_subduction.pyc
# Source Generated with Decompyle++
# File: crt_subduction.pyc (Python 3.6)

from cl_only import Functor, SendAlert
from cl_commondefines import VICTIM_STATE_VALID, VICTIM_STATE_BLOCK, MODEL_TYPE_SPHERE
from cl_pxlayer import PXLAYER_RBULLET, PXMASK_MOVEBLK
import cl_engphyobj
from .mobject import CBaseCartoon

class SubductionCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        lstEndPos = dCartoon['LstEnd']
        lstSpeed = dCartoon['LstSpeed']
        if not lstEndPos or len(lstEndPos) != len(lstSpeed):
            SendAlert('err', '%s PF%s 终点数量不匹配' % (oSkill.m_Game.m_ID, oSkill.m_Base['pfid']))
            return None
        oAttack = oSkill.GetAttack()
        oGame = oSkill.m_Game
        if not oAttack:
            cls.Disable(oSkill, dCartoon)
            return None
        dCartoon['PosIndex'] = 0
        if not StartAirMove(oAttack, oSkill, dCartoon):
            return None
        oBullet = cl_engphyobj.CreateTraceBullet(oGame, oAttack, {
            'TraceIdx': oSkill.m_Base['PFKey'] + str(cls.m_SID),
            'PassID': oAttack.m_ID }, PXLAYER_RBULLET, {
            'Shape': MODEL_TYPE_SPHERE,
            'Radius': oAttack.m_ModelRadius,
            'Center': (0, oAttack.m_ModelHeight / 2, 0) })
        oGame.m_SkillMgr.RegisterBullet(oBullet, oSkill.m_Base['AID'], oSkill.m_Base['ActNum'], dCartoon['ID'])
        dCartoon['BulletKey'] = oBullet.Key()
        oSkill.AddEndFunc(Functor(ClearCartoon, dCartoon))

    Trace = classmethod(Trace)
    
    def InitTraceServer(cls, oSkill, dCartoon, StartPos, lstEndPos, lstSpeed):
        dCartoon['LstSpeed'] = lstSpeed
        dCartoon['Start'] = StartPos
        dCartoon['LstEnd'] = lstEndPos
        dCartoon['CurPos'] = StartPos
        dNet = {
            'Start': StartPos }
        oSkill.Send(dCartoon['ID'], dNet)

    InitTraceServer = classmethod(InitTraceServer)
    
    def AddHitTarget(cls, oSkill, dCartoon, iTarget, dHit):
        if 'SubductionEnd' in dCartoon:
            return None
        lstHit = dCartoon.get('TargetList', [])
        if iTarget not in lstHit:
            lstHit.append(iTarget)
        dCartoon['TargetList'] = lstHit
        if iTarget == 0:
            cls.SubductionEnd(oSkill, dCartoon)

    AddHitTarget = classmethod(AddHitTarget)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        oAttack = oSkill.GetAttack()
        lstVictim = []
        lstHit = dCartoon.get('TargetList', [])
        dCartoon['TargetList'] = []
        if not lstHit:
            return 0
        for iVictim in lstHit:
            iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
            if iVictimState == VICTIM_STATE_BLOCK:
                oSkill.m_Update['HitStatic'] = 1
                continue
            if iVictimState == VICTIM_STATE_VALID and iVictim not in lstVictim:
                lstVictim.append(iVictim)
        
        oSkill.m_Update['LastVLST'] = lstVictim
        dCartoon['CurPos'] = oAttack.GetPos()
        dNet = {
            'LastVLST': lstVictim,
            'HitStatic': oSkill.m_Update['HitStatic'] if 'HitStatic' in oSkill.m_Update else 0 }
        oSkill.Send(dCartoon['ID'], dNet)
        return 1

    HitTargetServer = classmethod(HitTargetServer)
    
    def SubductionEnd(cls, oSkill, dCartoon):
        oAttack = oSkill.GetAttack()
        if not oAttack:
            return None
        if dCartoon['PosIndex'] + 1 < len(dCartoon['LstEnd']):
            dCartoon['PosIndex'] += 1
            StartAirMove(oAttack, oSkill, dCartoon)
            return None
        if 'SubductionEnd' not in dCartoon:
            dCartoon['SubductionEnd'] = 1
            oAttack.m_MoveCtrl.Stop(oAttack)

    SubductionEnd = classmethod(SubductionEnd)
    
    def IsOver(cls, oSkill, dCartoon):
        iOver = 0
        if 'SubductionEnd' in dCartoon:
            iOver = 1
        if iOver:
            oAttack = oSkill.GetAttack()
            dCartoon['Final'] = oAttack.GetPos()
            iNodeID = dCartoon['ID']
            oSkill.Send(iNodeID, {
                'Over': 1 })
            return 1
        return 0

    IsOver = classmethod(IsOver)


def SubductionAttackEnd(iActNum, iCartoon, oAttack, tEnd, iFail):
    oGame = oAttack.m_Game
    oSkill = oGame.m_SkillMgr.GetSkill(oAttack.m_ID, iActNum)
    if not oSkill or iCartoon not in oSkill.m_Cartoon:
        return None
    dCartoon = oSkill.m_Cartoon[iCartoon]
    if 'SubductionEnd' not in dCartoon:
        clsCartoon = dCartoon['cls']
        clsCartoon.SubductionEnd(oSkill, dCartoon)
        oSkill.Update([
            dCartoon['ID']])


def ClearCartoon(dCartoon, oSkill):
    clsCartoon = dCartoon['cls']
    clsCartoon.SubductionEnd(oSkill, dCartoon)
    clsCartoon.ClearCartoonBullet(oSkill, dCartoon)


def StartAirMove(oAttack, oSkill, dCartoon):
    vAttackPos = oAttack.GetPos()
    vPos = dCartoon['LstEnd'][dCartoon['PosIndex']]
    dCartoon['Start'] = vAttackPos
    dCartoon['End'] = vPos
    fGroundDis = oSkill.m_Game.Scene_GroundDistance(oAttack.m_Scene, (vPos[0], vPos[1] + 1, vPos[2]), 5, PXMASK_MOVEBLK, oAttack.m_ID)
    vPos = (vPos[0], (vPos[1] - fGroundDis) + 1, vPos[2])
    cbfunc = Functor(SubductionAttackEnd, oSkill.m_Base['ActNum'], dCartoon['ID'])
    vSpeed = dCartoon['LstSpeed'][dCartoon['PosIndex']]
    iRet = oAttack.m_MoveCtrl.AirMove(oAttack, vPos, vSpeed, False, cbfunc)
    if not iRet:
        oSkill.Halt('subductionmovefail')
    return iRet

