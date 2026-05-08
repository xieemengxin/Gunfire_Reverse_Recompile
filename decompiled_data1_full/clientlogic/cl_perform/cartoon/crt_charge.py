# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_charge.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_charge.pyc
# Source Generated with Decompyle++
# File: crt_charge.pyc (Python 3.6)

from cl_only import Time2Frame, Functor
from cl_commondefines import PF_TYPE_CHARGE, DEBUG_STATUS_NOCOSTBULLET, CRT_CHECK_SERVER, CHARGECARTOON_SUBMSG_START, CHARGECARTOON_SUBMSG_END, CHARGECARTOON_SUBMSG_EXCESSIVESTART
from .mobject import CBaseCartoon
import cl_msgcenter

class ChargeCartoon(CBaseCartoon):
    m_NeedCtrlNet = 0
    
    def Disable(cls, oSkill, dCartoon):
        super().Disable(oSkill, dCartoon)
        dCartoon['Disable'] = 1
        oAttack = oSkill.GetAttack()
        if oAttack:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CHARGECARTOON_TRIGGER, oAttack, {
                'Skill': oSkill,
                'Cartoon': dCartoon }, iSub = CHARGECARTOON_SUBMSG_END)

    Disable = classmethod(Disable)
    
    def IsOver(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        iOver = 0
        if 'Over' in dCartoon:
            iOver = 1
        if iOver:
            oSkill.Send(iNodeID, {
                'Over': 1 })
            return 1
        return 0

    IsOver = classmethod(IsOver)
    
    def OnArrive(cls, oSkill, dCartoon):
        oAttack = oSkill.GetAttack()
        pfobj = oAttack.GetPerform(oSkill.m_Base['pfid'], oSkill.m_Base['Weapon'])
        if not pfobj:
            oSkill.Halt('charge nopf')
            return None
        if pfobj.m_PFType == PF_TYPE_CHARGE:
            if dCartoon['PerBulletCost']:
                iPreBulletCostNum = dCartoon['ChargeLevel'] * dCartoon['PerBulletCost']
                oSkill.m_Collect['BaseBullet'] = iPreBulletCostNum
                if dCartoon['AllowMaxChargeLowAmmo']:
                    pfobj = oAttack.GetPerform(oSkill.m_Base['pfid'], oSkill.m_Base['Weapon'])
                    if pfobj:
                        oWeapon = pfobj.GetMyItem()
                        oBulletCom = oWeapon.GetComponent('Bullet')
                        iBullet = oBulletCom.Bullet()
                        if not iBullet <= 0 or oAttack.Query('CanNoBulletUse', 0):
                            oSkill.Halt('skill cost bullet err %d' % iBullet)
                            return None
                    elif iBullet < iPreBulletCostNum:
                        oSkill.m_Collect['BaseBullet'] = iBullet
                    else:
                        oSkill.m_Collect['BaseBullet'] = pfobj.m_CurBulletUse
            oSkill.m_Collect['ChargeLevel'] = None['ChargeLevel']
            pfobj.TrueUsePerform(oAttack, oSkill)
            if oAttack.Query('DebugStatus', 0) & DEBUG_STATUS_NOCOSTBULLET != DEBUG_STATUS_NOCOSTBULLET:
                pfobj.CostBullet(oAttack, oSkill)
            pfobj.WeaponFire(oAttack, oSkill)
        if dCartoon['ChargeLevel'] > 0:
            cls.Trigger(oSkill)

    OnArrive = classmethod(OnArrive)
    
    def InitTraceClient(cls, oSkill, dCartoon, iIntervalTime, iMaxChargeLevel, iPerBulletCost, iAutoEnd, iAdvanceEnd, halfEnd = False, allowMaxChargeLowAmmo = False, **kwargs):
        dCartoon['IntervalFrame'] = Time2Frame(int(iIntervalTime))
        dCartoon['MaxChargeLevel'] = iMaxChargeLevel
        dCartoon['PerBulletCost'] = iPerBulletCost
        dCartoon['AutoEnd'] = iAutoEnd
        dCartoon['AdvanceEnd'] = iAdvanceEnd
        dCartoon['HalfEnd'] = halfEnd
        dCartoon['AllowMaxChargeLowAmmo'] = allowMaxChargeLowAmmo
        iMaxFrame = dCartoon['IntervalFrame'] * iMaxChargeLevel
        dCartoon['MaxFrame'] = iMaxFrame
        if iAutoEnd:
            dCartoon['WaitNet'] = oSkill.GetWaitNetFrame(iMaxFrame)

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return -1
        dClient = oSkill.m_NetReceive[iNodeID]
        iMaxChargeLevel = GetMaxChargeLevel(oSkill, dCartoon)
        iChargeLevel = min(dClient['Count'], iMaxChargeLevel) if 'Count' in dClient else 0
        if 'Trigger' in dClient:
            TrySendExcessiveStart(oSkill, dCartoon)
            dCartoon['ExcessiveStartFrame'] = dClient['Frame'] if 'Frame' in dClient else 0
            oSkill.Send(dCartoon['ID'], dClient)
        if 'Over' in dClient:
            dCartoon['ExcessiveOverFrame'] = dClient['Frame'] if 'Frame' in dClient else 0
            if dCartoon['HalfEnd'] and not dCartoon['AdvanceEnd'] and iChargeLevel < iMaxChargeLevel:
                oSkill.Halt('chargelevel err %d %d' % (iChargeLevel, iMaxChargeLevel))
                return -1
            dCartoon['Over'] = 1
            if 'Time' in dClient:
                dCartoon['Time'] = dClient['Time']
            dCartoon['ChargeLevel'] = iChargeLevel
            oSkill.Send(dCartoon['ID'], dClient)
            return 1
        return 0

    HitTargetClient = classmethod(HitTargetClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, iIntervalTime, iMaxChargeLevel, iPerBulletCost, iAutoEnd, iAdvanceEnd, **kwargs):
        dCartoon['IntervalFrame'] = Time2Frame(int(iIntervalTime))
        dCartoon['MaxChargeLevel'] = iMaxChargeLevel
        dCartoon['ChargeLevel'] = iMaxChargeLevel
        dCartoon['PerBulletCost'] = iPerBulletCost
        dCartoon['AutoEnd'] = True
        dCartoon['WaitFrame'] = dCartoon['IntervalFrame'] * iMaxChargeLevel

    InitTraceServer = classmethod(InitTraceServer)
    
    def Trace(cls, oSkill, dCartoon):
        oAttack = oSkill.GetAttack()
        if oAttack:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CHARGECARTOON_TRIGGER, oAttack, {
                'Skill': oSkill,
                'Cartoon': dCartoon }, iSub = CHARGECARTOON_SUBMSG_START)
            oSkill.AddEndFunc(Functor(ClearCartoon, dCartoon))
        if oSkill.m_CheckType & CRT_CHECK_SERVER:
            oSkill.Call_Out(dCartoon['WaitFrame'], dCartoon['ID'], dCartoon['Casting'])

    Trace = classmethod(Trace)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        if dCartoon['StartFrame'] + dCartoon['WaitFrame'] <= oSkill.m_Game.GetFrameNum():
            dCartoon['Over'] = 1
            oSkill.Send(dCartoon['ID'], {
                'Count': dCartoon['ChargeLevel'] })
            return 1
        return 0

    HitTargetServer = classmethod(HitTargetServer)


def GetMaxChargeLevel(oSkill, dCartoon):
    if oSkill.m_Base['PFType'] == PF_TYPE_CHARGE and dCartoon['PerBulletCost']:
        oAttack = oSkill.GetAttack()
        pfobj = oAttack.GetPerform(oSkill.m_Base['pfid'], oSkill.m_Base['Weapon'])
        if pfobj:
            oWeapon = pfobj.GetMyItem()
            oBulletCom = oWeapon.GetComponent('Bullet')
            iBullet = oBulletCom.Bullet()
            if iBullet <= 0 and oWeapon.QueryTmp('InfiniteFire', 0):
                return dCartoon['MaxChargeLevel']
            if not dCartoon['AllowMaxChargeLowAmmo']:
                return min(iBullet // dCartoon['PerBulletCost'], dCartoon['MaxChargeLevel'])
    return dCartoon['MaxChargeLevel']


def TrySendExcessiveStart(oSkill, dCartoon):
    oAttack = oSkill.GetAttack()
    if oAttack:
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CHARGECARTOON_TRIGGER, oAttack, {
            'Skill': oSkill,
            'Cartoon': dCartoon }, iSub = CHARGECARTOON_SUBMSG_EXCESSIVESTART)


def ClearCartoon(dCartoon, oSkill):
    if 'Disable' in dCartoon:
        return None
    oAttack = oSkill.GetAttack()
    if oAttack:
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CHARGECARTOON_TRIGGER, oAttack, {
            'Skill': oSkill,
            'Cartoon': dCartoon }, iSub = CHARGECARTOON_SUBMSG_END)

