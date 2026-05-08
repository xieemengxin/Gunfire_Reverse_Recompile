# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/weaponanalyse.pyc
# RelativePath: clientlogic/cl_warmgr/weaponanalyse.pyc
# Source Generated with Decompyle++
# File: weaponanalyse.pyc (Python 3.6)

from cl_only import Frame2Time, GAME_FRAME, Functor
from cl_commondefines import PERFORM_POS_MINOR, PERFORM_POS_MAIN, WARRIOR_MONSTER, WARRIOR_HERO, LEVEL_TYPE_BOSS, DAM_TYPE_WEAKNESS, LEVEL_TYPE_FIGHT, ATTACKERSUBMSG_NORMAL, PF_TYPE_PETACTIVE
from cl_item.defines import EQUIP_MASK_WEAPON
from cl_warmgr.mobject import CBaseElement
from cl_object.logging import SkillLog
import cl_msgcenter
import cl_math
import cl_perform
import cl_item
import cl_item.cnet as cnet

class CWeaponAnalyse(CBaseElement):
    
    def __init__(self, oGame, nid, oData):
        super(CWeaponAnalyse, self).__init__(oGame, nid, oData)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Player = { }
        self.m_PlayerBigData = { }

    
    def Init(self):
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.OnAddPlayer, 'WeaponAna.AddPlayer', -1, 0)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.OnLevelStart, 'WeaponAna.LevelStart', -1, 0)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, self.OnLevelGoal, 'WeaponAna.LevelGoal', -1, 0)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, self.OnChangeweapon, 'WeaponAna.ChangeWeapon')
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DROPWEAPON, self.OnDrop, 'WeaponAna.Drop')
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_WIELDWEAPON, self.OnWield, 'WeaponAna.Widle')
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_REMOVEWEAPON, self.RemoveWeapon, 'WeaponAna.Remove')
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_UNHOLD_WEAPON, self.UnholdWeapon, 'WeaponAna.Unhold')
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, self.OnDie2, 'WeaponAna.Die2')
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_RELIFE, self.OnRelife, 'WeaponAna.Relife')
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_LEAVESCENE, self.OnLeaveScene, 'WeaponAna.LeaveScene')
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.OnPlayerMapLoadOK, 'WeaponAna.PlayerMapLoadOK')

    
    def AddAttention(self):
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_WEAPONFIRE, self.OnWeaponFire, 'WeaponAna.WeaponFire')
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_ATTACK_END, self.OnAttackEnd, 'WeaponAna.AttEnd')
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PERFORM_HALT, self.OnAttackEnd, 'WeaponAna.AttHalt')
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_ATTACK, self.OnAttack, 'WeaponAna.Attack', iSub = ATTACKERSUBMSG_NORMAL)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DEALTOTALDAM, self.OnDamage, 'WeaponAna.Dam', iSub = ATTACKERSUBMSG_NORMAL)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, self.OnDie, 'WeaponAna.Die')
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_KILL, self.OnKill, 'WeaponAna.Kill')

    
    def DoneAttention(self):
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_WEAPONFIRE, 'WeaponAna.WeaponFire')
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_ATTACK, 'WeaponAna.Attack', iSub = ATTACKERSUBMSG_NORMAL)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DEALTOTALDAM, 'WeaponAna.Dam', iSub = ATTACKERSUBMSG_NORMAL)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, 'WeaponAna.Die')
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_KILL, 'WeaponAna.Kill')

    
    def DelayDoneAttention(self):
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_ATTACK_END, 'WeaponAna.AttEnd')
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PERFORM_HALT, 'WeaponAna.AttHalt')

    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDPLAYER, 'WeaponAna.AddPlayer')
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_STARTFIGHT, 'WeaponAna.LevelStart')
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, 'WeaponAna.LevelGoal')
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, 'WeaponAna.ChangeWeapon')
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DROPWEAPON, 'WeaponAna.Drop')
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_WIELDWEAPON, 'WeaponAna.Widle')
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_REMOVEWEAPON, 'WeaponAna.Remove')
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_UNHOLD_WEAPON, 'WeaponAna.Unhold')
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, 'WeaponAna.Die2')
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_RELIFE, 'WeaponAna.Relife')
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_LEAVESCENE, 'WeaponAna.LeaveScene')
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, 'WeaponAna.PlayerMapLoadOK')
        self.DoneAttention()
        self.m_WarMgr = None
        super(CWeaponAnalyse, self).Release()

    
    def ExportWeaponAnalyse(self, pid):
        if pid not in self.m_Player:
            return { }
        dExport = { }
        dWeaponData = self.m_Player[pid]
        iNowFrame = self.m_WarMgr.m_Game.GetFrameNum()
        for iWeaponSID, oData in dWeaponData.items():
            oData.CalUseTime(iNowFrame)
            if oData.m_UseTime > 0:
                oHero = self.m_Game.m_WarMgr.GetHeroByPlayer(pid)
                dExport[iWeaponSID] = oData.ExportData()
                dExport[iWeaponSID].update({
                    'HeroSID': oHero.m_SID })
        
        return dExport

    
    def ClearWeaponAnalyse(self, pid):
        dWeaponData = self.m_Player[pid]
        for oData in dWeaponData.values():
            oData.Clear()
        
        dData = self.m_PlayerBigData.pop(pid, { })
        lstPlayer = self.m_Game.m_WarMgr.GetRoomPlayer()
        lstWeapon = []
        for iPlayer in lstPlayer:
            oHero = self.m_Game.m_WarMgr.GetHeroByPlayer(iPlayer)
            if not oHero:
                continue
            lstWeapon += oHero.m_WieldCon.GetAllItemByMask(EQUIP_MASK_WEAPON)
            lstWeapon += oHero.m_ExWeaponCon.GetAllItem()
            lstWeapon += oHero.m_WeaponStoreCon.GetAllItem()
        
        for oWeapon in lstWeapon:
            iWeapon = oWeapon.m_ID
            if iWeapon in dData:
                self.AddWeapon(pid, oWeapon.m_SID, iWeapon)
                dKeepData = dData[iWeapon].Save()
                self.m_PlayerBigData[pid][iWeapon].Load(dKeepData)
        

    
    def OnAddPlayer(self, oWarMgr, dInfo):
        pid = dInfo['pid']
        if pid not in self.m_Player:
            self.m_Player[pid] = { }
        if pid not in self.m_PlayerBigData:
            self.m_PlayerBigData[pid] = { }

    
    def OnLevelStart(self, oWarMgr, dInfo):
        if dInfo['LevelType'] not in (LEVEL_TYPE_FIGHT, LEVEL_TYPE_BOSS):
            return None
        self.AddAttention()

    
    def OnLevelGoal(self, oWarMgr, dInfo):
        if dInfo['LevelType'] not in (LEVEL_TYPE_FIGHT, LEVEL_TYPE_BOSS):
            return None
        self.DoneAttention()
        self.Call_Out(Functor(self.DelayDoneAttention), 1, 'DelayDoneAttention')
        for pid in self.m_Player:
            self.PlayerPauseUseTime(pid)
        

    
    def GetWeaponDataBySkill(self, oOwner, dInfo, iMainPF = 1, bBigData = False):
        if not oOwner:
            return None
        if 'Skill' not in dInfo:
            return None
        oSkill = dInfo['Skill']
        if 'ItemSID' not in oSkill.m_Cache or iMainPF:
            if 'AttPerform' not in oSkill.m_Cache or oSkill.m_Cache['AttPerform'] != oSkill.m_Base['pfid']:
                return None
        if not oOwner.m_FightType & WARRIOR_HERO:
            oOwner = oOwner.GetOwner()
            if not oOwner:
                return None
        pid = oOwner.m_PlayerID
        if not pid:
            SkillLog.Alert('pf%d owner pid error' % oSkill.m_Base['pfid'])
            return None
        if bBigData:
            iItemID = oSkill.m_Cache['ItemID']
            if iItemID not in self.m_PlayerBigData[pid]:
                return None
            return self.m_PlayerBigData[pid][iItemID]
        iItemSID = oSkill.m_Cache['ItemSID']
        if iItemSID not in self.m_Player[pid]:
            return None
        return self.m_Player[pid][iItemSID]

    
    def PlayerPauseUseTime(self, pid):
        iNowFrame = self.m_WarMgr.m_Game.GetFrameNum()
        for oData in self.m_Player[pid].values():
            oData.CalUseTime(iNowFrame)
            oData.m_LastUse = 0
        
        for oBigData in self.m_PlayerBigData[pid].values():
            oBigData.CalUseTime(iNowFrame)
            oBigData.m_LastUse = 0
        

    
    def OnWeaponFire(self, oWarMgr, oOwner, dInfo):
        if 'Skill' not in dInfo:
            return None
        oSkill = dInfo['Skill']
        iPerform = oSkill.m_Base['pfid']
        oData = self.GetWeaponDataBySkill(oOwner, dInfo, 0)
        if not oData:
            return None
        if iPerform not in oData.m_PFType:
            return None
        iPerformType = oData.m_PFType[iPerform]
        if iPerformType == PERFORM_POS_MAIN:
            oData.m_Attack += 1
        iNowFrame = oWarMgr.m_Game.GetFrameNum()
        oData.CalUseTime(iNowFrame)
        oData.m_LastUse = iNowFrame
        self.OnWeaponFire2(oWarMgr, oOwner, dInfo, iPerformType)

    
    def OnAttackEnd(self, oWarMgr, oOwner, dInfo):
        oData = self.GetWeaponDataBySkill(oOwner, dInfo, 0)
        if not oData:
            return None
        oSkill = dInfo['Skill']
        iTotalBullet = oSkill.m_Collect['TotalBullet'] if 'TotalBullet' in oSkill.m_Collect else 0
        oData.m_Bullet += iTotalBullet
        oBigData = self.GetWeaponDataBySkill(oOwner, dInfo, 0, True)
        if not oBigData:
            return None
        oBigData.m_Bullet += iTotalBullet

    
    def OnAttack(self, oWarMgr, oOwner, dInfo):
        if 'Skill' not in dInfo:
            return None
        oSkill = dInfo['Skill']
        iPerform = oSkill.m_Base['pfid']
        oData = self.GetWeaponDataBySkill(oOwner, dInfo, 0)
        if not oData:
            return None
        if iPerform not in oData.m_PFType:
            return None
        iPerformType = oData.m_PFType[iPerform]
        if iPerformType == PERFORM_POS_MAIN:
            oData.m_Hit += 1
        oReason = dInfo['RS']
        if oReason.Query('DamType') & DAM_TYPE_WEAKNESS and iPerformType == PERFORM_POS_MAIN:
            oData.m_Weakness += 1
        self.OnAttack2(oWarMgr, oOwner, dInfo, iPerformType)

    
    def OnDamage(self, oWarMgr, oOwner, dInfo):
        oData = self.GetWeaponDataBySkill(oOwner, dInfo)
        if oData:
            oData.m_EffectDam += sum(dInfo['TotalDam'])
            iExcessDam = 0
            for iDam, _ in dInfo['ExcessChange']:
                iExcessDam += iDam
            
            oData.m_ExcessDam += iExcessDam
        self.OnDamage2(oWarMgr, oOwner, dInfo)

    
    def OnDie(self, oWarMgr, oOwner, dInfo):
        if not (oOwner.m_PlayerID) or oOwner.m_PlayerID not in self.m_Player:
            return None
        self.PlayerPauseUseTime(oOwner.m_PlayerID)

    
    def OnKill(self, oWarMgr, oOwner, dInfo):
        if not oOwner:
            return None
        if 'Skill' not in dInfo:
            return None
        oSkill = dInfo['Skill']
        if 'AttPerform' not in oSkill.m_Cache:
            return None
        if not oOwner.m_FightType & WARRIOR_HERO:
            oOwner = oOwner.GetOwner()
            if not oOwner:
                return None
        pid = oOwner.m_PlayerID
        if not pid:
            SkillLog.Alert('pf%d owner pid error' % oSkill.m_Base['pfid'])
            return None
        if 'ItemSID' not in oSkill.m_Cache:
            return None
        iItemSID = oSkill.m_Cache['ItemSID']
        if iItemSID not in self.m_Player[pid]:
            return None
        oData = self.m_Player[pid][iItemSID]
        if not oData:
            return None
        iPerform = oSkill.m_Base['pfid']
        if iPerform not in oData.m_PFType:
            return None
        if iPerform in oData.m_PFMap['AttPerform'] or iPerform in oData.m_PFMap['MinorPerform']:
            oData.m_Kill += 1

    
    def OnChangeweapon(self, oWarMgr, oOwner, dInfo):
        iWeaponSID = dInfo['ItemSID']
        iWeaponID = dInfo['ItemID']
        pid = oOwner.m_PlayerID
        self.AddWeapon(pid, iWeaponSID)
        self.AddWeapon(pid, iWeaponSID, iWeaponID)
        self.PlayerPauseUseTime(pid)
        self.PlayerHoldWeapon(pid, iWeaponID)
        oWeapon = oOwner.m_WieldCon.GetItemByID(iWeaponID)
        if oWeapon:
            oWeaponData = self.m_PlayerBigData[pid][iWeaponID]
            oWeaponData.UpdateHoldInscription(oWeapon)

    
    def AddWeapon(self, pid, iWeaponSID, iWeaponID = None):
        if pid not in self.m_Player:
            self.m_Player[pid] = { }
        if pid not in self.m_PlayerBigData:
            self.m_PlayerBigData[pid] = { }
        if iWeaponSID not in self.m_Player[pid]:
            self.m_Player[pid][iWeaponSID] = CWeaponData(iWeaponSID)
        if iWeaponID and iWeaponID not in self.m_PlayerBigData[pid]:
            self.m_PlayerBigData[pid][iWeaponID] = CWeaponBigData(iWeaponSID, iWeaponID)

    
    def ExportWeaponAnalyseToBigData(self, pid):
        if pid not in self.m_PlayerBigData:
            return { }
        dWeaponData = self.m_PlayerBigData[pid]
        oHero = self.m_Game.m_WarMgr.GetHeroByPlayer(pid)
        if oHero:
            lstWeapon = []
            lstWeapon += oHero.m_WieldCon.GetAllItemByMask(EQUIP_MASK_WEAPON)
            lstWeapon += oHero.m_ExWeaponCon.GetAllItem()
            lstWeapon += oHero.m_WeaponStoreCon.GetAllItem()
            for oWeapon in lstWeapon:
                if oWeapon.m_ID in dWeaponData:
                    dWeaponData[oWeapon.m_ID].UpdateHoldInscription(oWeapon)
            
        dExport = { }
        iNowFrame = self.m_WarMgr.m_Game.GetFrameNum()
        for iWeaponID, oData in dWeaponData.items():
            oData.CalUseTime(iNowFrame)
            oData.CalHoldTime(iNowFrame, iNowFrame)
            dExport[iWeaponID] = oData.ExportToBigData()
        
        return dExport

    
    def PlayerUnholdWeapon(self, oWeaponData):
        iNowFrame = self.m_WarMgr.m_Game.GetFrameNum()
        oWeaponData.CalHoldTime(iNowFrame, -1)

    
    def PlayerHoldWeapon(self, pid, iWeaponID):
        iNowFrame = self.m_WarMgr.m_Game.GetFrameNum()
        self.m_PlayerBigData[pid][iWeaponID].m_LastHold = iNowFrame

    
    def PlayerHoldCurWeapon(self, oHero):
        oCurWeapon = oHero.m_WieldCon.GetCurWeapon()
        if not oCurWeapon:
            return None
        self.PlayerHoldWeapon(oHero.m_PlayerID, oCurWeapon.m_ID)

    
    def RemoveWeapon(self, oWarMgr, oOwner, dInfo):
        sReason = dInfo['Reason']
        if sReason == cnet.WIELD_TO_OTHERCOM:
            return None
        iWeaponSID = dInfo['SID']
        iWeaponID = dInfo['ItemID']
        oWeapon = dInfo['Weapon']
        pid = oOwner.m_PlayerID
        self.AddWeapon(pid, iWeaponSID, iWeaponID)
        oWeaponData = self.m_PlayerBigData[pid][iWeaponID]
        oWeaponData.UpdateHoldInscription(oWeapon)
        oWeaponData.m_AbandonTimes += 1
        if oWeaponData.m_FightBeginTime:
            iEndTime = self.m_WarMgr.m_Game.GetFrameNum()
            oWeaponData.CalFightTime(iEndTime)

    
    def OnWeaponFire2(self, oWarMgr, oOwner, dInfo, iPerformType):
        oBigData = self.GetWeaponDataBySkill(oOwner, dInfo, 0, True)
        if not oBigData:
            return None
        if iPerformType == PERFORM_POS_MAIN:
            oBigData.m_Attack += 1
        elif iPerformType == PERFORM_POS_MINOR:
            oBigData.m_MinorAttack += 1
        iNowFrame = oWarMgr.m_Game.GetFrameNum()
        oBigData.CalUseTime(iNowFrame)
        oBigData.m_LastUse = iNowFrame

    
    def OnAttack2(self, oWarMgr, oOwner, dInfo, iPerformType):
        oBigData = self.GetWeaponDataBySkill(oOwner, dInfo, 0, True)
        if not oBigData:
            return None
        if iPerformType == PERFORM_POS_MAIN:
            oBigData.m_Hit += 1
        elif iPerformType == PERFORM_POS_MINOR:
            oBigData.m_MinorHit += 1
        oReason = dInfo['RS']
        if oReason.Query('DamType') & DAM_TYPE_WEAKNESS:
            if iPerformType == PERFORM_POS_MAIN:
                oBigData.m_Weakness += 1
            elif iPerformType == PERFORM_POS_MINOR:
                oBigData.m_MinorWeakness += 1
        if not oOwner.m_FightType & WARRIOR_HERO == WARRIOR_HERO and oBigData.m_FightBeginTime:
            oBigData.m_FightBeginTime = self.m_WarMgr.m_Game.GetFrameNum()
        self.CalFightEnd(oBigData)
        iPerform = dInfo['Skill'].m_Base['pfid']
        clsPerform = cl_perform.GetPerformModule(iPerform)
        if not clsPerform or clsPerform.m_PFType == PF_TYPE_PETACTIVE:
            return None
        if 'CurHitPos' not in dInfo:
            SkillLog.Alert('pf%d no hitinfo' % iPerform)
            oVictim = self.m_Game.GetObject(dInfo['CurVID'])
            if not oVictim:
                return None
            vPos = oVictim.GetPos()
        else:
            vPos = dInfo['CurHitPos']
        iDistance = cl_math.CalDistance3D(vPos, oOwner.GetPos())
        if oBigData.m_Hit == 0:
            return None
        iAvgDistance = (iDistance + oBigData.m_AvgDistance * (oBigData.m_Hit - 1)) / oBigData.m_Hit
        oBigData.m_AvgDistance = round(iAvgDistance, 3)

    
    def OnDamage2(self, oWarMgr, oOwner, dInfo):
        if not oOwner:
            return None
        oWeaponBigData = None
        if oOwner.m_FightType & WARRIOR_HERO == WARRIOR_HERO:
            oWeapon = oOwner.m_WieldCon.GetCurWeapon()
            if not oWeapon:
                return None
            if oWeapon.m_ID not in self.m_PlayerBigData[oOwner.m_PlayerID]:
                self.AddWeapon(oOwner.m_PlayerID, oWeapon.m_SID, oWeapon.m_ID)
            oWeaponBigData = self.m_PlayerBigData[oOwner.m_PlayerID][oWeapon.m_ID]
            if not oWeaponBigData.m_FightBeginTime:
                oWeaponBigData.m_FightBeginTime = self.m_WarMgr.m_Game.GetFrameNum()
            elif oOwner.m_FightType & WARRIOR_MONSTER == WARRIOR_MONSTER:
                oHero = self.m_Game.GetObject(dInfo['CurVID'])
                if oHero.m_FightType & WARRIOR_HERO == WARRIOR_HERO:
                    oWeapon = oHero.m_WieldCon.GetCurWeapon()
                    if not oWeapon:
                        return None
                    if oWeapon.m_ID not in self.m_PlayerBigData[oHero.m_PlayerID]:
                        self.AddWeapon(oHero.m_PlayerID, oWeapon.m_SID, oWeapon.m_ID)
                    oWeaponBigData = self.m_PlayerBigData[oHero.m_PlayerID][oWeapon.m_ID]
                    if not oWeaponBigData.m_FightBeginTime:
                        oWeaponBigData.m_FightBeginTime = self.m_WarMgr.m_Game.GetFrameNum()
        if None:
            self.CalFightEnd(oWeaponBigData)

    
    def OnLeaveScene(self, oWarMgr, oOwner, dInfo):
        if not (oOwner.m_PlayerID) or oOwner.m_PlayerID not in self.m_Player:
            return None
        self.PlayerUnholdCurWeapon(oOwner)

    
    def OnDie2(self, oWarMgr, oOwner, dInfo):
        if not (oOwner.m_PlayerID) or oOwner.m_PlayerID not in self.m_Player:
            return None
        self.PlayerUnholdCurWeapon(oOwner)

    
    def OnRelife(self, oWarMgr, oOwner, dInfo):
        if not (oOwner.m_PlayerID) or oOwner.m_PlayerID not in self.m_Player:
            return None
        self.PlayerHoldCurWeapon(oOwner)

    
    def OnPlayerMapLoadOK(self, oWarMgr, oOwner, dInfo):
        if not (oOwner.m_PlayerID) or oOwner.m_PlayerID not in self.m_Player:
            return None
        self.PlayerHoldCurWeapon(oOwner)

    
    def CalFightEnd(self, oWeaponBigData):
        self.Remove_Call_Out('WeaponFight')
        self.Call_Out(Functor(self.FightEndTime, oWeaponBigData), 75, 'WeaponFight')

    
    def FightEndTime(self, oWeaponBigData):
        self.Remove_Call_Out('WeaponFight')
        if oWeaponBigData.m_FightBeginTime:
            iEndTime = self.m_WarMgr.m_Game.GetFrameNum()
            oWeaponBigData.CalFightTime(iEndTime)

    
    def UnholdWeapon(self, oWarMgr, oOwner, dInfo):
        pid = oOwner.m_PlayerID
        oItem = dInfo.get('oItem', None)
        if oItem:
            self.AddWeapon(pid, oItem.m_SID, oItem.m_ID)
            oWeaponData = self.m_PlayerBigData[pid][oItem.m_ID]
            if oWeaponData.m_FightBeginTime:
                iEndTime = self.m_WarMgr.m_Game.GetFrameNum()
                oWeaponData.CalFightTime(iEndTime)
            self.PlayerUnholdWeapon(oWeaponData)

    
    def PlayerUnholdCurWeapon(self, oHero):
        oCurWeapon = oHero.m_WieldCon.GetCurWeapon()
        if not oCurWeapon:
            return None
        pid = oHero.m_PlayerID
        if pid not in self.m_PlayerBigData:
            return None
        iItem = oCurWeapon.m_ID
        if iItem not in self.m_PlayerBigData[pid]:
            return None
        oData = self.m_PlayerBigData[pid][iItem]
        self.PlayerUnholdWeapon(oData)

    
    def OnDrop(self, oWarMgr, oOwner, dInfo):
        lstWeapon = dInfo['lstWeapon']
        pid = oOwner.m_PlayerID
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        iLayer = oLevelCtrl.m_LayerNum
        for oWeapon in lstWeapon:
            self.AddWeapon(pid, oWeapon.m_SID, oWeapon.m_ID)
            oWeaponData = self.m_PlayerBigData[pid][oWeapon.m_ID]
            oWeaponData.m_OutTimes += 1
            oWeaponData.m_OutLayer = iLayer
            oPerformCom = oWeapon.GetComponent('Inscription')
            lstInscription = oPerformCom.GetAllInscription(iFill = 0, iIgnoreDisable = 0)
            oWeaponData.m_LstInscription = lstInscription
            oWeaponData.m_HoldInscription = lstInscription
        

    
    def OnWield(self, oWarMgr, oOwner, dInfo):
        iWeaponSID = dInfo['SID']
        iWeaponID = dInfo['ID']
        iCurPlayer = oOwner.m_PlayerID
        self.AddWeapon(iCurPlayer, iWeaponSID, iWeaponID)
        oWeaponData = self.m_PlayerBigData[iCurPlayer][iWeaponID]
        for pid in self.m_PlayerBigData:
            if pid != iCurPlayer and iWeaponID in self.m_PlayerBigData[pid] and iWeaponID in self.m_PlayerBigData[pid][iWeaponID].m_LstLive:
                self.m_PlayerBigData[iCurPlayer][iWeaponID] = self.m_PlayerBigData[pid][iWeaponID]
                oWeaponData = self.m_PlayerBigData[iCurPlayer][iWeaponID]
                oWeaponData.m_ExchangeTimes += 1
                self.m_PlayerBigData[pid].pop(iWeaponID)
        
        if iWeaponID in oWeaponData.m_LstLive:
            oWeaponData.m_ReGetTimes += 1
        else:
            oWeaponData.m_LstLive.append(iWeaponID)
            oWeaponData.m_GetTimes += 1

    
    def LoadBigData(self, dBigData):
        for pid, dWeaponData in dBigData.items():
            dPlayerBigData = self.m_PlayerBigData.setdefault(pid, { })
            for iWeaponID, dLoadData in dWeaponData.items():
                if iWeaponID not in dPlayerBigData:
                    self.AddWeapon(pid, dLoadData['WeaponSID'], iWeaponID)
                oWeaponData = dPlayerBigData[iWeaponID]
                oWeaponData.Load(dLoadData)
            
        

    
    def SaveBigData(self):
        dBigData = { }
        for pid, dWeaponData in self.m_PlayerBigData.items():
            dBigData[pid] = { }
            for iWeaponID, oWeaponData in dWeaponData.items():
                dBigData[pid][iWeaponID] = oWeaponData.Save()
            
        
        return dBigData



class CWeaponData(object):
    m_SingleUseMax = 4 * GAME_FRAME
    
    def __init__(self, iWeaponSID):
        self.m_WeaponSID = iWeaponSID
        self.m_UseTime = 0
        self.m_LastUse = 0
        self.m_Attack = 0
        self.m_Hit = 0
        self.m_Weakness = 0
        self.m_EffectDam = 0
        self.m_ExcessDam = 0
        self.m_Bullet = 0
        self.m_Kill = 0
        self.m_PFType = { }
        self.m_PFMap = { }
        self.CalPFType()

    
    def Clear(self):
        self.m_UseTime = 0
        self.m_LastUse = 0
        self.m_Attack = 0
        self.m_Hit = 0
        self.m_Weakness = 0
        self.m_EffectDam = 0
        self.m_ExcessDam = 0
        self.m_Bullet = 0
        self.m_Kill = 0

    
    def CalPFType(self):
        clsWeapon = cl_item.GetItemCls(self.m_WeaponSID)
        dPerform = clsWeapon.m_ComponentAttr['Perform']
        dPerformAtt = dPerform['AttPerform']
        lstWeaponPerform = [
            dPerform['MinorPerform']] if 'MinorPerform' in dPerform else []
        lstPerformAtt = []
        lstMinorPerform = []
        for iPerform in lstWeaponPerform:
            if iPerform not in lstMinorPerform:
                lstMinorPerform.append(iPerform)
        
        for iPerform, _, _, _ in dPerformAtt.values():
            if iPerform not in lstWeaponPerform:
                lstWeaponPerform.append(iPerform)
            if iPerform not in lstPerformAtt:
                lstPerformAtt.append(iPerform)
        
        lstAllPerform = lstWeaponPerform[:]
        for iPerform in lstWeaponPerform:
            clsPerform = cl_perform.GetPerformModule(iPerform)
            if not clsPerform:
                continue
            lstAllPerform.extend(clsPerform.m_ExtPerform)
            if iPerform in lstPerformAtt:
                lstPerformAtt.extend(clsPerform.m_ExtPerform)
                continue
            if iPerform in lstMinorPerform:
                lstMinorPerform.extend(clsPerform.m_ExtPerform)
        
        self.m_PFMap['AttPerform'] = lstPerformAtt
        self.m_PFMap['MinorPerform'] = lstMinorPerform
        for iPerform in lstAllPerform:
            iPFType = self.GetPFType(iPerform)
            if iPFType == -1:
                SkillLog.Alert(f'''{iPerform} no pftype''')
                continue
            self.m_PFType[iPerform] = iPFType
        

    
    def GetPFType(self, iPerform):
        clsPerform = cl_perform.GetPerformModule(iPerform)
        if not clsPerform:
            return -1
        if clsPerform.m_IsMinor:
            iPFType = PERFORM_POS_MINOR
        else:
            iPFType = PERFORM_POS_MAIN
        return iPFType

    
    def CalUseTime(self, iNowFrame):
        if self.m_LastUse:
            self.m_UseTime += min(iNowFrame - self.m_LastUse, self.m_SingleUseMax)

    
    def ExportData(self):
        dData = {
            'Kill': self.m_Kill,
            'AttTimes': self.m_Attack,
            'Hit': self.m_Hit,
            'WHit': self.m_Weakness,
            'EffectDam': self.m_EffectDam,
            'ExcessDam': self.m_ExcessDam,
            'UseTime': Frame2Time(self.m_UseTime),
            'Bullet': self.m_Bullet }
        return dData

    
    def AnaData(self):
        iHitRatio = self.m_Hit * 100 // self.m_Attack if self.m_Attack else 0
        iWeakness = self.m_Weakness * 100 // self.m_Hit if self.m_Hit else 0
        iBulletEffect = self.m_EffectDam // self.m_Bullet // 100 if self.m_Bullet else 0
        iSceond = self.m_UseTime // GAME_FRAME
        iAttackEfficiency = self.m_EffectDam // iSceond // 100 if iSceond else 0
        iIdealEfficiency = (self.m_EffectDam + self.m_ExcessDam) // iSceond // 100 if iSceond else 0
        return (iHitRatio, iWeakness, iBulletEffect, iAttackEfficiency, iIdealEfficiency)

    
    def OriData(self):
        return (self.m_UseTime // GAME_FRAME, self.m_Attack, self.m_Hit, self.m_Weakness, self.m_EffectDam // 100, self.m_ExcessDam // 100, self.m_Bullet)



class CWeaponBigData(object):
    m_SingleUseMax = 4 * GAME_FRAME
    
    def __init__(self, iWeaponSID, iWeaponID):
        self.m_WeaponSID = iWeaponSID
        self.m_WeaponID = iWeaponID
        self.m_Attack = 0
        self.m_Hit = 0
        self.m_Weakness = 0
        self.m_UseTime = 0
        self.m_LastUse = 0
        self.m_Bullet = 0
        self.m_MinorAttack = 0
        self.m_MinorHit = 0
        self.m_MinorWeakness = 0
        self.m_OutTimes = 0
        self.m_GetTimes = 0
        self.m_AbandonTimes = 0
        self.m_ExchangeTimes = 0
        self.m_ReGetTimes = 0
        self.m_LstLive = []
        self.m_FightBeginTime = 0
        self.m_FightTime = 0
        self.m_HoldTime = 0
        self.m_LastHold = -1
        self.m_LstInscription = []
        self.m_HoldInscription = []
        self.m_OutLayer = 0
        self.m_AvgDistance = 0

    
    def ExportToBigData(self):
        dData = {
            'WeaponSID': self.m_WeaponSID,
            'AttTimes': self.m_Attack,
            'Hit': self.m_Hit,
            'WHit': self.m_Weakness,
            'UseTime': Frame2Time(self.m_UseTime),
            'Bullet': self.m_Bullet,
            'MinorAttTimes': self.m_MinorAttack,
            'MinorHit': self.m_MinorHit,
            'MinorWHit': self.m_MinorWeakness,
            'OutTimes': self.m_OutTimes,
            'GetTimes': self.m_GetTimes,
            'AbaTimes': self.m_AbandonTimes,
            'ExcTimes': self.m_ExchangeTimes,
            'RegTimes': self.m_ReGetTimes,
            'FightTime': Frame2Time(self.m_FightTime),
            'HoldTime': Frame2Time(self.m_HoldTime),
            'LstInscription': self.m_LstInscription,
            'HoldInscription': list(self.m_HoldInscription),
            'OutLayer': self.m_OutLayer,
            'AvgDistance': self.m_AvgDistance }
        return dData

    
    def Save(self):
        dData = {
            'WeaponSID': self.m_WeaponSID,
            'LstLive': self.m_LstLive,
            'HoldIns': self.m_HoldInscription }
        return dData

    
    def Load(self, dData):
        self.m_LstLive = dData['LstLive']
        self.m_HoldInscription = dData.get('HoldIns', [])

    
    def UpdateHoldInscription(self, oWeapon):
        oInscriptionCom = oWeapon.GetComponent('Inscription')
        if oInscriptionCom:
            self.m_HoldInscription = oInscriptionCom.GetAllInscription(iFill = 0, iIgnoreDisable = 0)

    
    def CalUseTime(self, iNowFrame):
        if self.m_LastUse:
            self.m_UseTime += min(iNowFrame - self.m_LastUse, self.m_SingleUseMax)

    
    def CalFightTime(self, iNowFrame):
        if self.m_FightBeginTime:
            self.m_FightTime += max(iNowFrame - self.m_FightBeginTime, self.m_SingleUseMax)
            self.m_FightBeginTime = 0

    
    def CalHoldTime(self, iNowFrame, iLastHold):
        if self.m_LastHold >= 0:
            self.m_HoldTime += iNowFrame - self.m_LastHold
            self.m_LastHold = iLastHold



def GetComponentClass(oWarManager):
    return CWeaponAnalyse

