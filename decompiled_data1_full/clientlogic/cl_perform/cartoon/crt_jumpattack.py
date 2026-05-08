# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_jumpattack.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_jumpattack.pyc
# Source Generated with Decompyle++
# File: crt_jumpattack.pyc (Python 3.6)

from cl_commondefines import CRT_CHECK_CLIENT, CRT_CHECK_SERVER, VICTIM_STATE_VALID, MODEL_TYPE_BOX
from cl_only import Functor, GAME_FRAME
from cl_pxlayer import PXLAYER_EBULLET
import cl_engphyobj
import cllib.lib_cartoon as cartooncheck
from .crt_winkpos import ExitDashCheck
from .mobject import CBaseCartoon

class JumpAttackCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        if 'Over' in dCartoon:
            return None
        if oSkill.m_CheckType & CRT_CHECK_CLIENT:
            return None
        oGame = oSkill.m_Game
        oAttack = oSkill.GetAttack()
        tDir = dCartoon['Dir']
        fTimeOutSecond = dCartoon['TotalSecond']
        fSpeed = dCartoon['Speed']
        cbfunc = Functor(MoveEnd, oSkill.m_Base['ActNum'], dCartoon['ID'])
        iRet = oAttack.m_MoveCtrl.DashMove(oAttack, tDir, fSpeed, fTimeOutSecond, cbfunc)
        if not iRet:
            oSkill.Halt('dashfail')
            return None
        fExtentZ = fSpeed / GAME_FRAME + 0.8
        oBullet = cl_engphyobj.CreateTraceBullet(oGame, oAttack, {
            'TraceIdx': oSkill.m_Base['PFKey'],
            'LocalPos': (0, 0, fExtentZ),
            'PassID': oAttack.m_ID,
            'LockDirection': tDir }, PXLAYER_EBULLET, {
            'Shape': MODEL_TYPE_BOX,
            'HalfExt': (oAttack.m_ModelRadius, oAttack.m_ModelHeight, fExtentZ) })
        oGame.m_SkillMgr.RegisterBullet(oBullet, oSkill.m_Base['AID'], oSkill.m_Base['ActNum'], dCartoon['ID'])
        dCartoon['BulletKey'] = oBullet.Key()
        oSkill.AddEndFunc(Functor(ClearCartoon, dCartoon))

    Trace = classmethod(Trace)
    
    def IsOver(cls, oSkill, dCartoon):
        if 'Over' in dCartoon:
            dNet = {
                'Trigger': 1,
                'Over': 1 }
            if oSkill.m_CheckType & CRT_CHECK_SERVER:
                dNet['Trigger'] = 1
                cls.Trigger(oSkill)
            oSkill.Send(dCartoon['ID'], dNet)
            return 1
        return 0

    IsOver = classmethod(IsOver)
    
    def InitTraceClient(cls, oSkill, dCartoon, fAccelerateTime, fDecelerateTime, fTotalTime, fMinTime, fMaxSpeed, fFinalSpeed, *args, **kwargs):
        iNodeID = dCartoon['ID']
        dClient = oSkill.m_NetReceive[iNodeID]
        dCartoon['Dir'] = dClient['Direction']
        dCartoon['TotalSecond'] = fTotalTime * 0.01
        dCartoon['Speed'] = fMaxSpeed
        dCartoon['CurPos'] = oSkill.m_Base['vStart']
        dCartoon['Start'] = oSkill.m_Base['vStart']
        dNet = {
            'Direction': dCartoon['Dir'] }
        oSkill.Send(dCartoon['ID'], dNet)
        if 'Ray' in dClient or 'Over' in dClient:
            cls.Update(oSkill, dCartoon)
        else:
            oAttack = oSkill.GetAttack()
            dCtrlCheck = {
                'ActNum': oSkill.m_Base['ActNum'],
                'CartoonID': dCartoon['ID'],
                'ExitCB': ExitDashCheck,
                'Second': dCartoon['TotalSecond'],
                'Speed': fMaxSpeed,
                'UpSpeed': fFinalSpeed }
            oAttack.m_MoveCtrl.AddDashCtrlCheck(oAttack, dCtrlCheck)

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        iHit = 0
        if iNodeID not in oSkill.m_NetReceive:
            return iHit
        dClient = oSkill.m_NetReceive[iNodeID]
        dNet = { }
        cartooncheck.CheckDataWinkPos(oSkill, dCartoon)
        lstRay = dClient['Ray'] if 'Ray' in dClient else []
        if lstRay:
            iHit = 1
            lstVLST = []
            lstSend = []
            for vHitPos, vNormal, iVictim, iHitPart in lstRay:
                iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
                dCartoon['Final'] = vHitPos
                if iVictimState == VICTIM_STATE_VALID and iVictim not in lstVLST:
                    lstVLST.append(iVictim)
                    lstSend.append((vHitPos, vNormal, iVictim, iHitPart))
            
            oSkill.m_Update['LastVLST'] = lstVLST
            dNet['Ray'] = dClient['Ray']
        if 'End' in dClient:
            dNet['End'] = dClient['End']
            dCartoon['Final'] = dClient['End']
        if 'Over' in dClient or lstRay:
            dCartoon['Over'] = 1
            dNet['Over'] = 1
        if 'Trigger' in dClient:
            dNet['Trigger'] = 1
            cls.Trigger(oSkill)
        oSkill.Send(dCartoon['ID'], dNet)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, vDir, fAccelerateTime, fDecelerateTime, fTotalTime, fMinTime, fMaxSpeed, fFinalSpeed, *args, **kwargs):
        dCartoon['Dir'] = vDir
        dCartoon['TotalSecond'] = fTotalTime * 0.01
        dCartoon['Speed'] = fMaxSpeed
        dCartoon['CurPos'] = oSkill.m_Base['vStart']
        dCartoon['Start'] = oSkill.m_Base['vStart']
        dNet = {
            'Direction': dCartoon['Dir'] }
        oSkill.Send(dCartoon['ID'], dNet)

    InitTraceServer = classmethod(InitTraceServer)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        return 0

    HitTargetServer = classmethod(HitTargetServer)
    
    def AddHitTarget(cls, oSkill, dCartoon, iTarget, dHit):
        if 'Over' in dCartoon:
            return None
        lstHit = dCartoon.get('TargetList', [])
        if iTarget not in lstHit:
            lstHit.append(iTarget)
        dCartoon['TargetList'] = lstHit
        cls.WinkMoveEnd(oSkill, dCartoon)

    AddHitTarget = classmethod(AddHitTarget)
    
    def WinkMoveEnd(cls, oSkill, dCartoon):
        if 'Over' not in dCartoon:
            dCartoon['Over'] = 1
            iAttack = oSkill.m_Base['AID']
            oAttack = oSkill.m_Game.GetObject(iAttack)
            oAttack.m_MoveCtrl.m_WinkMoveCB = None
            oAttack.m_MoveCtrl.Stop(oAttack)

    WinkMoveEnd = classmethod(WinkMoveEnd)


def MoveEnd(iActNum, iCartoon, oAttack, iFlag):
    if not oAttack:
        return None
    oGame = oAttack.m_Game
    oSkill = oGame.m_SkillMgr.GetSkill(oAttack.m_ID, iActNum)
    if not oSkill or iCartoon not in oSkill.m_Cartoon:
        return None
    dCartoon = oSkill.m_Cartoon[iCartoon]
    if 'Over' not in dCartoon:
        dCartoon['Over'] = 1
        oSkill.Update([
            dCartoon['ID']])


def ClearCartoon(dCartoon, oSkill):
    dCartoon['cls'].ClearCartoonBullet(oSkill, dCartoon)

