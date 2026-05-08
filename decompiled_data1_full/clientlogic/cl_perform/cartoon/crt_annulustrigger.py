# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_annulustrigger.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_annulustrigger.pyc
# Source Generated with Decompyle++
# File: crt_annulustrigger.pyc (Python 3.6)

from cl_only import Time2Frame
from cl_commondefines import VICTIM_STATE_VALID, OBJ_ENEMY
import cllib.lib_cartoon as cartooncheck
from .mobject import CBaseCartoon
from . import ContinuousCostBullet

class AnnulusTriggerCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        if 'Over' in dCartoon:
            return None
        cls.Update(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def InitTraceClient(cls, oSkill, dCartoon, iAttIntervalTime, iLeaveAnnulusTime):
        iNodeID = dCartoon['ID']
        dCartoon['TargetType'] = OBJ_ENEMY
        dCartoon['AttIntervalFrame'] = Time2Frame(iAttIntervalTime)
        dCartoon['LastHitFrameInfo'] = { }
        dClient = oSkill.m_NetReceive[iNodeID]
        dCartoon['StartFrame'] = dClient['Frame']
        dCartoon['CurAnnulusRadius'] = dClient['Distance']
        dCartoon['LeaveAnnulusFrame'] = Time2Frame(iLeaveAnnulusTime)
        dCartoon['InvalidHitFrame'] = 0

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        dNet = { }
        iHit = 0
        iNodeID = dCartoon['ID']
        dClient = oSkill.m_NetReceive[iNodeID]
        oSkill.m_Collect['AnnulusTriggerFisrtHit'] = []
        oSkill.m_Collect['AnnulusTriggerFisrtHitHight'] = []
        if 'Count' in dClient:
            for _ in range(dClient['Count']):
                ContinuousCostBullet(oSkill, iNodeID)
            
        if 'Ray' in dClient and 'Frame' in dClient:
            iHit = 1
            iFrame = dClient['Frame']
            lstRay = dClient['Ray']
            lstVLST = []
            lstHitInfo = []
            lstSend = []
            oWeapon = GetSkillWeapon(oSkill)
            iLockCartoon = oWeapon.Query('lockCartoon', -1)
            oAttack = oSkill.GetAttack()
            pfobj = oAttack.GetPerform(oSkill.m_Base['pfid'], oSkill.m_Base['Weapon'])
            for vHitPos, vNormal, iVictim, iHitPart in lstRay:
                iIsSaveLastFrame = 1
                iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
                if iVictimState == VICTIM_STATE_VALID or iVictim in lstVLST:
                    continue
                if iLockCartoon != -1:
                    oSkill.m_Collect['AnnulusTriggerFisrtHitHight'].append(iVictim)
                    pfobj.WeaponFire(oAttack, oSkill)
                    dCartoon['LastHitFrameInfo'] = { }
                    iIsSaveLastFrame = 0
                elif iVictim not in dCartoon['LastHitFrameInfo'] or iFrame - dCartoon['LastHitFrameInfo'][iVictim] > dCartoon['LeaveAnnulusFrame']:
                    oSkill.m_Collect['AnnulusTriggerFisrtHit'].append(iVictim)
                    dCartoon['InvalidHitFrame'] = iFrame + (iFrame - dCartoon['StartFrame']) % dCartoon['AttIntervalFrame']
                    pfobj.WeaponFire(oAttack, oSkill)
                elif (iFrame - dCartoon['StartFrame']) % dCartoon['AttIntervalFrame'] >= 2:
                    iLastHitFrame = dCartoon['LastHitFrameInfo'][iVictim] if iVictim in dCartoon['LastHitFrameInfo'] else 0
                    oSkill.LogCheckErr('annulusattintervalcheckfail %s %s %s %s' % (iFrame, dCartoon['StartFrame'], dCartoon['AttIntervalFrame'], iLastHitFrame))
                    continue
                if dCartoon['InvalidHitFrame'] and iFrame == dCartoon['InvalidHitFrame']:
                    oSkill.LogCheckErr('annulusinvalidhitframecheckfail %s %s %s %s' % (iFrame, dCartoon['StartFrame'], dCartoon['AttIntervalFrame'], dCartoon['InvalidHitFrame']))
                    continue
                lstVLST.append(iVictim)
                dHitInfo = {
                    'Victim': iVictim,
                    'HitPos': vHitPos,
                    'HitArea': iHitPart }
                lstHitInfo.append(dHitInfo)
                lstSend.append((vHitPos, vNormal, iVictim, iHitPart))
                if iIsSaveLastFrame:
                    dCartoon['LastHitFrameInfo'][iVictim] = iFrame
            
            iAttack = oSkill.m_Base['AID']
            oAttack = oSkill.m_Game.GetObject(iAttack)
            vPos = oAttack.GetLastPos(iFrame)
            vPos = (vPos[0], vPos[1] + 1, vPos[2])
            dCartoon['CurPos'] = vPos
            oSkill.m_Update['LastVLST'] = lstVLST
            oSkill.m_Update['HitInfo'] = lstHitInfo
            dNet['Ray'] = lstSend
        oSkill.Send(dCartoon['ID'], dNet)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)
    
    def IsOver(cls, oSkill, dCartoon):
        iOver = 0
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return iOver
        dClient = oSkill.m_NetReceive[iNodeID]
        if 'Over' in dClient:
            iOver = 1
        if iOver:
            oSkill.Send(iNodeID, {
                'Over': 1 })
        return iOver

    IsOver = classmethod(IsOver)


def GetSkillWeapon(oSkill):
    iWeapon = oSkill.m_Base['Weapon']
    iAttack = oSkill.m_Base['AID']
    oAttack = oSkill.m_Game.GetObject(iAttack)
    oWeapon = oAttack.m_WieldCon.GetItemByID(iWeapon)
    return oWeapon

