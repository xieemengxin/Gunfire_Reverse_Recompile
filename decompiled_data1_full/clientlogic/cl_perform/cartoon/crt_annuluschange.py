# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_annuluschange.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_annuluschange.pyc
# Source Generated with Decompyle++
# File: crt_annuluschange.pyc (Python 3.6)

from cl_only import GAME_FRAME, GAME_FRAME_TIME
from .mobject import CBaseCartoon

class AnnulusChangeCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        if 'Over' in dCartoon:
            return None
        cls.Update(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def Restart(cls, oSkill, dCartoon):
        oSkill.Call_Out(1, dCartoon['ID'])

    Restart = classmethod(Restart)
    
    def InitTraceClient(cls, oSkill, dCartoon, fAnnulusMaxRadius, fAnnulusMinRadius, fMaxSpeed, fMinSpeed, fSlope, iIsKeepChange, iTime = 0):
        iNodeID = dCartoon['ID']
        dClient = oSkill.m_NetReceive[iNodeID]
        dCartoon['AnnulusMaxRadius'] = fAnnulusMaxRadius
        dCartoon['AnnulusMinRadius'] = fAnnulusMinRadius
        dCartoon['MaxSpeed'] = fMaxSpeed
        dCartoon['Slope'] = fSlope
        dCartoon['MinSpeed'] = fMinSpeed
        dCartoon['CurAnnulusRadius'] = dClient['Distance']
        dCartoon['IsKeepChange'] = iIsKeepChange
        dCartoon['ChangeTime'] = iTime
        oWeapon = GetSkillWeapon(oSkill)
        if not oWeapon:
            return None
        if not iIsKeepChange:
            oWeapon.Set('lockCartoon', iNodeID)
        dNet = {
            'Frame': dClient['Frame'] }
        oSkill.Send(dCartoon['ID'], dNet)

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        if dCartoon['IsKeepChange'] and dCartoon['CurAnnulusRadius'] >= dCartoon['AnnulusMaxRadius']:
            return False
        if not dCartoon['IsKeepChange'] and dCartoon['CurAnnulusRadius'] <= dCartoon['AnnulusMinRadius']:
            return False
        oWeapon = GetSkillWeapon(oSkill)
        if not oWeapon:
            return False
        iLockCartoon = oWeapon.Query('lockCartoon', -1)
        if iLockCartoon != dCartoon['ID'] and iLockCartoon != -1:
            return False
        if dCartoon['ChangeTime']:
            fCurAnnulusRadius = oWeapon.Query('CurAnnulusRadius', dCartoon['CurAnnulusRadius'])
            iChangeFrame = dCartoon['ChangeTime'] / GAME_FRAME_TIME
            if 'TimeSpeed' not in dCartoon:
                dCartoon['TimeSpeed'] = (dCartoon['AnnulusMinRadius'] - fCurAnnulusRadius) / iChangeFrame
            dCartoon['CurAnnulusRadius'] += dCartoon['TimeSpeed']
        elif dCartoon['Slope'] <= 0:
            iStartSpeed = dCartoon['MaxSpeed']
        else:
            iStartSpeed = dCartoon['MinSpeed']
        dCartoon['CurSpeed'] = dCartoon['Slope'] * dCartoon['CurAnnulusRadius'] + iStartSpeed
        if dCartoon['CurSpeed'] > dCartoon['MaxSpeed']:
            dCartoon['CurSpeed'] = dCartoon['MaxSpeed']
        if dCartoon['CurSpeed'] < dCartoon['MinSpeed']:
            dCartoon['CurSpeed'] = dCartoon['MinSpeed']
        dCartoon['CurAnnulusRadius'] += dCartoon['CurSpeed'] / GAME_FRAME
        if dCartoon['CurAnnulusRadius'] > dCartoon['AnnulusMaxRadius']:
            dCartoon['CurAnnulusRadius'] = dCartoon['AnnulusMaxRadius']
        elif dCartoon['CurAnnulusRadius'] < dCartoon['AnnulusMinRadius']:
            dCartoon['CurAnnulusRadius'] = dCartoon['AnnulusMinRadius']
        oWeapon.Set('CurAnnulusRadius', dCartoon['CurAnnulusRadius'])
        return True

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
            if not dCartoon['IsKeepChange']:
                oWeapon = GetSkillWeapon(oSkill)
                if oWeapon:
                    oWeapon.Set('lockCartoon', -1)
        return iOver

    IsOver = classmethod(IsOver)


def GetSkillWeapon(oSkill):
    iWeapon = oSkill.m_Base['Weapon']
    iAttack = oSkill.m_Base['AID']
    oAttack = oSkill.m_Game.GetObject(iAttack)
    oWeapon = oAttack.m_WieldCon.GetItemByID(iWeapon)
    return oWeapon

