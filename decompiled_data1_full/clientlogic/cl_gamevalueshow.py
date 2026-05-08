# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_gamevalueshow.pyc
# RelativePath: clientlogic/cl_gamevalueshow.pyc
# Source Generated with Decompyle++
# File: cl_gamevalueshow.pyc (Python 3.6)

from cl_commondefines import PF_TYPE_CAREERPF, PF_TYPE_THROW, ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAKNESS, DATAUI_TYPE_WEAPON, PF_TYPE_ATTACK
from cl_only import Functor, SendAlert, Frame2Time
import cl_msgcenter
import cl_snetwar
import cl_formula
import cl_perform
import cl_state
DAMTYPE_WEAPON = 1
DAMTYPE_PERFORM = 2
DAMTYPE_OTHER = 3

class CShowDamageValue:
    
    def __init__(self, oGame):
        self.m_Game = oGame
        self.m_Flag = 'HeroDamageShow'
        self.m_Cache = { }
        self.m_ShowArgs = {
            'Interval': { },
            'Num': { } }

    
    def OpenShow(self, oHero, iFrame, iCacheNum):
        cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_DEALTOTALDAM, self.OnDealTotalDam, self.m_Flag, -1, 0)
        cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, self.OnRemovePlayer, self.m_Flag, -1, 0)
        self.m_ShowArgs['Interval'][oHero.m_PlayerID] = iFrame
        self.m_ShowArgs['Num'][oHero.m_PlayerID] = iCacheNum
        self.m_Cache[oHero.m_PlayerID] = []

    
    def CloseShow(self, oHero):
        cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_DEALTOTALDAM, self.m_Flag)
        cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, self.m_Flag)
        self.m_ShowArgs['Interval'].pop(oHero.m_PlayerID, 0)
        self.m_ShowArgs['Num'].pop(oHero.m_PlayerID, 0)
        oHero.Remove_Call_Out('IntervalShowDam')

    
    def OnRemovePlayer(self, oHero, dInfo):
        self.CloseShow(oHero)

    
    def OnDealTotalDam(self, oHero, dInfo):
        if 'Skill' not in dInfo:
            return None
        oSkill = dInfo['Skill']
        iWeapon = oSkill.m_Base['Weapon']
        if oSkill.m_Base['PFType'] in (PF_TYPE_CAREERPF, PF_TYPE_THROW):
            oPerform = oHero.GetPerform(oSkill.m_Base['pfid'])
            if not oPerform:
                oServant = self.m_Game.GetObject(dInfo['OriginAID']) if 'OriginAID' in dInfo else None
                if oServant:
                    oPerform = oServant.GetPerform(oSkill.m_Base['pfid'])
            if oPerform:
                iDamType = DAMTYPE_PERFORM
                if not oPerform.GetAttr('Att'):
                    if 'Att' not in oSkill.m_Cache:
                        SendAlert('err', 'perform %d not att' % oPerform.m_SID)
                        return None
                    iBaseAtt = oSkill.m_Cache['Att']
                else:
                    iBaseAtt = oPerform.CalAttr('Att')
                (iAttackFactorAdd, iAttackFactorMul, iVictimFactorAdd, iVictimFactorMul, iSkillFactorAdd, iSkillFactorMul, _) = self.GetDamFactor(dInfo)
                iPlayer = oHero.m_PlayerID
                iInterval = self.m_ShowArgs['Interval'][iPlayer]
                if not self.m_Cache[iPlayer]:
                    oHero.Call_Out(Functor(self.SendCacheInfo, iPlayer), iInterval, 'IntervalShowDam')
                self.m_Cache[iPlayer].append([
                    iDamType,
                    iBaseAtt,
                    iAttackFactorAdd,
                    iAttackFactorMul,
                    iVictimFactorAdd,
                    iVictimFactorMul,
                    iSkillFactorAdd,
                    iSkillFactorMul])
        elif iWeapon:
            oWeapon = oHero.m_WieldCon.GetItemByID(iWeapon)
            if oWeapon:
                iDamType = DAMTYPE_WEAPON
                (iAttackFactorAdd, iAttackFactorMul, iVictimFactorAdd, iVictimFactorMul, iSkillFactorAdd, iSkillFactorMul, iLuckyHit) = self.GetDamFactor(dInfo)
                iBaseAtt = oWeapon.QueryAttr('Att')
                oCrazyEffAttr = oWeapon.GetItemAttr('CrazyEff')
                if oCrazyEffAttr.m_Type == 'Base':
                    iBaseCrazy = oCrazyEffAttr.GetBaseAttr()
                    iExtraCrazy = oCrazyEffAttr.m_AddPositive + oCrazyEffAttr.m_AddNegative
                elif oCrazyEffAttr.m_Type == 'Link':
                    iBaseCrazy = oCrazyEffAttr.GetValueNotRefresh(oWeapon)
                    iExtraCrazy = 0
                else:
                    return None
                iPlayer = oHero.m_PlayerID
                iInterval = self.m_ShowArgs['Interval'][iPlayer]
                if not self.m_Cache[iPlayer]:
                    oHero.Call_Out(Functor(self.SendCacheInfo, iPlayer), iInterval, 'IntervalShowDam')
                iChargeLevel = oSkill.m_Collect['ChargeLevel'] if 'ChargeLevel' in oSkill.m_Collect else 0
                self.m_Cache[iPlayer].append([
                    iDamType,
                    iBaseAtt,
                    iAttackFactorAdd,
                    iAttackFactorMul,
                    iVictimFactorAdd,
                    iVictimFactorMul,
                    iBaseCrazy,
                    iExtraCrazy,
                    iLuckyHit,
                    iSkillFactorAdd,
                    iSkillFactorMul,
                    iChargeLevel])

    
    def GetDamFactor(self, dInfo):
        if 'RS' in dInfo:
            oReason = dInfo['RS']
            (iAttackFactorAdd, iAttackFactorMul) = oReason.Query('DamFactor1', (10000, 10000))
            (iVictimFactorAdd, iVictimFactorMul) = oReason.Query('DamFactor2', (10000, 10000))
            (iSkillFactorAdd, iSkillFactorMul) = oReason.Query('DamFactorSkillFactor', (10000, 10000))
            iLuckyHit = oReason.Query('LuckyHit', 0)
            return (iAttackFactorAdd, iAttackFactorMul, iVictimFactorAdd, iVictimFactorMul, iSkillFactorAdd, iSkillFactorMul, iLuckyHit)
        return (10000, 10000, 10000, 10000, 10000, 10000, 0)

    
    def SendCacheInfo(self, iPlayer):
        iNum = self.m_ShowArgs['Num'][iPlayer]
        cl_snetwar.GS2CShowDamageInfo(self.m_Cache[iPlayer][-iNum:], iPlayer)
        self.m_Cache[iPlayer] = []



class CShowWeaponInfo:
    
    def __init__(self):
        self.m_Flag = 'ShowWeaponInfo'
        self.m_WeaponInfo = { }
        self.m_ShowArgs = {
            'Interval': { } }
        self.m_Cache = { }

    
    def OpenShow(self, oHero, iFrame):
        oMainWeapon = oHero.m_WieldCon.GetCurWeapon()
        if not oMainWeapon:
            return 0
        pid = oHero.m_PlayerID
        iWeaponSID = oMainWeapon.m_SID
        if pid in self.m_WeaponInfo and iWeaponSID in self.m_WeaponInfo[pid]:
            self.CloseShow(oHero)
            return 0
        self.m_WeaponInfo[pid] = {
            iWeaponSID: {
                'Fire': 0,
                'Hit': 0,
                'Weakness': 0 } }
        self.m_ShowArgs['Interval'][pid] = iFrame
        self.SendWeaponInfo(oHero.m_Game, pid)
        cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_WEAPONFIRE, self.OnWeaponFire, self.m_Flag, iSub = -1, iOnce = 0)
        cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_ATTACK, self.OnAttack, self.m_Flag, iSub = ATTACKERSUBMSG_NORMAL, iOnce = 0)
        cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, self.OnChangeWeapon, self.m_Flag, iSub = -1, iOnce = 0)
        cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_UNHOLD_WEAPON, self.OnUnholdWeapon, self.m_Flag, iSub = -1, iOnce = 0)
        cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, self.OnRemovePlayer, self.m_Flag, iSub = -1, iOnce = 0)
        cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_PLAYERONREADY, self.OnPlayerReady, self.m_Flag, iSub = -1, iOnce = 0)
        return 1

    
    def CloseShow(self, oHero):
        pid = oHero.m_PlayerID
        self.m_WeaponInfo.pop(pid, { })
        self.m_ShowArgs['Interval'].pop(pid, { })
        oHero.Remove_Call_Out(self.m_Flag)
        cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_WEAPONFIRE, self.m_Flag)
        cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_ATTACK, self.m_Flag, iSub = ATTACKERSUBMSG_NORMAL)
        cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, self.m_Flag)
        cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_UNHOLD_WEAPON, self.m_Flag)
        cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, self.m_Flag)
        cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_PLAYERONREADY, self.m_Flag)

    
    def ValidInfo(self, oHero, dInfo):
        pid = oHero.m_PlayerID
        if pid not in self.m_WeaponInfo:
            return 0
        if 'Skill' not in dInfo:
            return 0
        oSkill = dInfo['Skill']
        if not oSkill.m_Base['Weapon']:
            return 0
        iWeaponSID = oSkill.m_Cache['ItemSID']
        dWeaponInfo = self.m_WeaponInfo[pid]
        if iWeaponSID not in dWeaponInfo:
            return 0
        iAttPerform = oSkill.m_Cache['AttPerform']
        if oSkill.m_Base['pfid'] != iAttPerform:
            return 0
        return 1

    
    def OnWeaponFire(self, oHero, dInfo):
        if not self.ValidInfo(oHero, dInfo):
            return None
        oSkill = dInfo['Skill']
        iWeaponSID = oSkill.m_Cache['ItemSID']
        self.m_WeaponInfo[oHero.m_PlayerID][iWeaponSID]['Fire'] += 1
        self.CallOut(oHero)

    
    def OnAttack(self, oHero, dInfo):
        if not self.ValidInfo(oHero, dInfo):
            return None
        oSkill = dInfo['Skill']
        iWeaponSID = oSkill.m_Cache['ItemSID']
        dWeaponInfo = self.m_WeaponInfo[oHero.m_PlayerID][iWeaponSID]
        dWeaponInfo['Hit'] += 1
        oReason = dInfo['RS']
        if oReason.Query('DamType') & DAM_TYPE_WEAKNESS:
            dWeaponInfo['Weakness'] += 1
        self.CallOut(oHero)

    
    def CallOut(self, oHero):
        pid = oHero.m_PlayerID
        if pid not in self.m_Cache:
            self.m_Cache[pid] = 1
            iInterval = self.m_ShowArgs['Interval'][pid]
            oHero.Call_Out(Functor(self.SendWeaponInfo, oHero.m_Game, pid), iInterval, self.m_Flag)

    
    def OnChangeWeapon(self, oHero, dInfo):
        pid = oHero.m_PlayerID
        if pid not in self.m_WeaponInfo:
            return None
        iWeaponSID = dInfo['ItemSID']
        if iWeaponSID not in self.m_WeaponInfo[pid]:
            return None
        cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_WEAPONFIRE, self.OnWeaponFire, self.m_Flag, iSub = -1, iOnce = 0)
        cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_ATTACK, self.OnAttack, self.m_Flag, iSub = ATTACKERSUBMSG_NORMAL, iOnce = 0)

    
    def OnUnholdWeapon(self, oHero, dInfo):
        pid = oHero.m_PlayerID
        if pid not in self.m_WeaponInfo:
            return None
        dWeaponInfo = self.m_WeaponInfo[pid]
        lstWeapon = oHero.m_WieldCon.GetHoldWeapon()
        for oWeapon, _ in lstWeapon:
            if oWeapon.m_SID in dWeaponInfo:
                return None
        
        cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_WEAPONFIRE, self.m_Flag)
        cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_ATTACK, self.m_Flag, iSub = ATTACKERSUBMSG_NORMAL)

    
    def OnRemovePlayer(self, oHero, dInfo):
        self.CloseShow(oHero)

    
    def OnPlayerReady(self, oHero, dInfo):
        pid = oHero.m_PlayerID
        self.SendWeaponInfo(oHero.m_Game, pid)

    
    def SendWeaponInfo(self, oGame, pid):
        if pid not in self.m_WeaponInfo:
            return None
        if pid in self.m_Cache:
            self.m_Cache.pop(pid)
        for iWeaponSID, dWeaponInfo in self.m_WeaponInfo[pid].items():
            iHit = dWeaponInfo['Hit']
            iFire = dWeaponInfo['Fire']
            iWeakness = dWeaponInfo['Weakness']
            fHitRatio = iHit * 100 / iFire if iFire else 0
            fWeaknessRatio = iWeakness * 100 / iHit if iHit else 0
            dExtInfo = {
                'SID': iWeaponSID,
                'HitRatio': fHitRatio,
                'WeaknessRatio': fWeaknessRatio }
            cl_snetwar.GS2CUpdateDataUI(oGame, pid, DATAUI_TYPE_WEAPON, dExtInfo)
        



class CCheckSkillAtt:
    
    def __init__(self):
        self.m_Flag = 'HeroSkillAttCheck'
        self.m_Open = False

    
    def OpenShow(self, oHero):
        self.m_Open = True
        cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_DEALTOTALDAM, self.OnDealTotalDam, self.m_Flag, -1, 0)
        cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, self.OnRemovePlayer, self.m_Flag, -1, 0)

    
    def CloseShow(self, oHero):
        self.m_Open = False
        cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_DEALTOTALDAM, self.m_Flag)
        cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, self.m_Flag)
        oHero.DelSavedData('PerformDamage')
        oHero.DelSavedData('WeaponDamage')

    
    def OnRemovePlayer(self, oHero, dInfo):
        self.CloseShow(oHero)

    
    def OnDealTotalDam(self, oHero, dInfo):
        if 'Skill' not in dInfo:
            return None
        oSkill = dInfo['Skill']
        iTotalDamage = cl_formula.CalDealTotalDam(dInfo) // 100
        if 'ItemID' in oSkill.m_Cache:
            dDamageInfo = oHero.SetDefaultSavedData('WeaponDamage', { })
            if oSkill.m_Base['PFType'] & PF_TYPE_ATTACK == PF_TYPE_ATTACK:
                iPerform = 0
            else:
                iPerform = oSkill.m_Base['pfid']
        else:
            dDamageInfo = oHero.SetDefaultSavedData('PerformDamage', { })
            iPerform = oSkill.m_Base['pfid']
        if iPerform in dDamageInfo:
            dDamageInfo[iPerform] += iTotalDamage
        else:
            dDamageInfo[iPerform] = iTotalDamage

    
    def GetPerformDamInfo(self, oHero):
        return oHero.QuerySavedData('PerformDamage', { })

    
    def GetWeaponDamInfo(self, oHero):
        return oHero.QuerySavedData('WeaponDamage', { })



class CShowDetailDamageValue:
    
    def __init__(self, oGame):
        self.m_Flag = 'ShowDetailDamageValue'
        self.m_Game = oGame
        self.m_SendInterval = 50
        self.m_Cache = { }
        self.m_StartFrame = { }

    
    def OpenShow(self, oHero):
        pid = oHero.m_PlayerID
        if pid in self.m_Cache:
            return None
        sFlag = self.m_Flag
        cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_DEALTOTALDAM, self.OnDealTotalDam, sFlag, -1, 0)
        cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, self.OnRemovePlayer, sFlag, -1, 0)
        iFrame = self.m_Game.GetFrameNum()
        self.m_Cache[pid] = { }
        self.m_StartFrame[pid] = iFrame
        oHero.Call_Out(Functor(self.SendCacheInfo, pid), self.m_SendInterval, sFlag)

    
    def CloseShow(self, oHero):
        pid = oHero.m_PlayerID
        if pid not in self.m_Cache:
            return None
        sFlag = self.m_Flag
        oHero.Remove_Call_Out(sFlag)
        self.SendCacheInfo(pid)
        cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_DEALTOTALDAM, sFlag)
        cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, sFlag)
        self.m_Cache.pop(pid, 0)
        self.m_StartFrame.pop(pid, 0)

    
    def OnRemovePlayer(self, oHero, dInfo):
        self.CloseShow(oHero)

    
    def AddDam(self, pid, iType, sName, iDam):
        if pid not in self.m_Cache:
            return None
        dHeroCache = self.m_Cache[pid]
        dTypeDam = dHeroCache.setdefault(iType, { })
        if sName not in dTypeDam:
            dTypeDam[sName] = iDam
        else:
            dTypeDam[sName] += iDam

    
    def OnDealTotalDam(self, oHero, dInfo):
        pid = oHero.m_PlayerID
        iTotalDam = 0
        for iDam, _ in dInfo['TrueChange'] + dInfo['ExcessChange']:
            iTotalDam += iDam // 100
        
        oSkill = dInfo.get('Skill', None)
        if oSkill:
            iWeapon = oSkill.m_Base['Weapon']
            iPerformSID = oSkill.m_Base['pfid']
            sPerformName = str(iPerformSID)
            if iWeapon:
                iDamType = DAMTYPE_WEAPON
                oPerform = oHero.GetPerform(iPerformSID, iWeapon)
                if oPerform:
                    sPerformName = '%s-%s' % (oPerform.m_Name, iPerformSID)
                else:
                    iPfType = oSkill.m_Base['PFType']
                    iDamType = DAMTYPE_PERFORM
                    if iPfType == PF_TYPE_CAREERPF:
                        sPerformName = '职业技能'
                    elif iPfType == PF_TYPE_THROW:
                        sPerformName = '投掷技能'
                    else:
                        oPerform = oHero.GetPerform(oSkill.m_Base['pfid'])
                        if oPerform:
                            sPerformName = '%s-%s' % (oPerform.m_Name, iPerformSID)
            None.AddDam(pid, iDamType, sPerformName, iTotalDam)
        else:
            sAllReason = str(dInfo['RS'])
            sDamName = ''
            for sReason in sAllReason.split('|'):
                if 'PF' not in sReason and 'ST' not in sReason:
                    continue
                sSID = sReason[2:]
                if not sSID.isdigit():
                    break
                iSID = int(sSID)
                if 'PF' in sReason:
                    clsPerform = cl_perform.GetPerformModule(iSID)
                    if clsPerform:
                        sDamName = '技能-%s-%s' % (iSID, clsPerform.m_Name)
                    elif 'ST' in sReason:
                        clsState = cl_state.GetStateClass(iSID)
                        if clsState:
                            sDamName = '状态-%s-%s' % (iSID, clsState.m_Name)
                    break
            
            if not sDamName:
                sDamName = sAllReason
            self.AddDam(pid, DAMTYPE_OTHER, sDamName, iTotalDam)

    
    def SendCacheInfo(self, pid):
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        if not oWarMgr:
            return None
        oHero = oWarMgr.GetHeroByPlayer(pid)
        if not oHero or pid not in self.m_Cache or pid not in self.m_StartFrame:
            return None
        oHero.Call_Out(Functor(self.SendCacheInfo, pid), self.m_SendInterval, self.m_Flag)
        dHeroCache = self.m_Cache[pid]
        iStartFrame = self.m_StartFrame[pid]
        iCurFrame = oGame.GetFrameNum()
        iLastSecond = Frame2Time(iCurFrame - iStartFrame) // 100
        if iLastSecond <= 0:
            return None
        lstDetailDam = []
        for iType, dDamage in dHeroCache.items():
            iTotalDam = 0
            lstDam = []
            for sPerformName, iDam in dDamage.items():
                iTotalDam += iDam
                iPerformDps = iDam // iLastSecond
                lstDam.append([
                    sPerformName,
                    iPerformDps])
            
            iDps = iTotalDam // iLastSecond
            lstDetailDam.append([
                iType,
                iTotalDam,
                iDps,
                lstDam])
        
        cl_snetwar.GS2CShowDetailDam(lstDetailDam, pid)


