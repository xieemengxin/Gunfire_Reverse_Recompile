# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_switchweapon.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_switchweapon.pyc
# Source Generated with Decompyle++
# File: crt_switchweapon.pyc (Python 3.6)

from cl_only import Time2Frame
from cl_item.defines import EMPTY_HAND_UNWIELDTIME
from .mobject import CBaseCartoon

class SwitchWeaponCartoon(CBaseCartoon):
    
    def InitTraceClient(cls, oSkill, dCartoon):
        dReceive = oSkill.m_NetReceive[dCartoon['ID']]
        iWeaponChange = dReceive['WeaponChange']
        dCartoon['MainPos'] = iWeaponChange & 15
        dCartoon['DeputyPos'] = iWeaponChange >> 4 & 15
        dCartoon['WeaponChange'] = dReceive['WeaponChange']
        dNet = {
            'WeaponChange': dReceive['WeaponChange'] }
        oSkill.Send(dCartoon['ID'], dNet)

    InitTraceClient = classmethod(InitTraceClient)
    
    def InitTraceServer(cls, oSkill, dCartoon):
        iNewPos = oSkill.m_Custom['SwitchPos']
        dCartoon['MainNewPos'] = iNewPos
        dCartoon['WeaponChange'] = iNewPos

    InitTraceServer = classmethod(InitTraceServer)
    
    def Trace(cls, oSkill, dCartoon):
        oAttack = oSkill.GetAttack()
        if not oAttack:
            oSkill.Halt()
            return None
        iSwitchPos = dCartoon['WeaponChange']
        if not oAttack.ValidSwitchWeapon(iSwitchPos):
            oSkill.Halt()
            return None
        iMainPos = dCartoon['MainPos']
        oWieldCon = oAttack.m_WieldCon
        oMainWeapon = oWieldCon.GetCurWeapon()
        oNewWeapon = oWieldCon.GetItemByPos(iMainPos)
        iUnHoldTime = oMainWeapon.QueryAttr('UnwieldTime') if oMainWeapon else EMPTY_HAND_UNWIELDTIME
        iHoldTime = oNewWeapon.QueryAttr('WieldTime')
        iHoldFrame = Time2Frame(iHoldTime)
        iUnHoldFrame = Time2Frame(iUnHoldTime)
        dCartoon['AllSwitch'] = (iHoldFrame, iUnHoldFrame)
        dCartoon['UnHold'] = 1
        oSkill.Call_Out(iUnHoldFrame, dCartoon['ID'])

    Trace = classmethod(Trace)
    
    def HitTarget(cls, oSkill, dCartoon):
        iNow = oSkill.m_Game.GetFrameNum()
        (iHoldFrame, iUnHoldFrame) = dCartoon['AllSwitch']
        if 'UnHold' in dCartoon and iNow >= iUnHoldFrame + dCartoon['StartFrame']:
            oAttack = oSkill.GetAttack()
            iSwitchPos = dCartoon['WeaponChange']
            if not oAttack or not oAttack.ValidSwitchWeapon(iSwitchPos):
                dCartoon['Over'] = 1
                return 1
            dCartoon.pop('UnHold')
            oAttack.SwitchWeapon(iSwitchPos)
            cls.Trigger(oSkill)
            oSkill.Call_Out(iHoldFrame, dCartoon['ID'])
        elif iNow >= iHoldFrame + iUnHoldFrame + dCartoon['StartFrame']:
            dCartoon['Over'] = 1
            return 1
        return 0

    HitTarget = classmethod(HitTarget)
    
    def IsOver(cls, oSkill, dCartoon):
        if 'Over' in dCartoon:
            dNet = {
                'Over': 1 }
            oSkill.Send(dCartoon['ID'], dNet)
            return 1
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return 0
        dClient = oSkill.m_NetReceive[iNodeID]
        if CheckSwitchWeaponOver(oSkill, dCartoon, dClient):
            return 1
        return 0

    IsOver = classmethod(IsOver)


def CheckSwitchWeaponOver(oSkill, dCartoon, dClient):
    if 'Over' not in dClient or dClient['Over'] != 1:
        return 0
    iFrame = dClient['Frame']
    (iHoldFrame, iUnHoldFrame) = dCartoon['AllSwitch']
    if iFrame < iUnHoldFrame + dCartoon['StartFrame'] or iFrame > iHoldFrame + iUnHoldFrame + dCartoon['StartFrame'] + 2:
        oSkill.LogCheckErr('client over err %s' % iFrame)
        return 0
    return 1

