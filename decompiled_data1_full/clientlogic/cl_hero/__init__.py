# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_hero/__init__.pyc
# RelativePath: clientlogic/cl_hero/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_only import Functor, PythonError, RaiseError, PRODUCT_MIN_CSUMMON_ID, PRODUCT_MIN_NPC_ID, SendAlert, GAME_FRAME, TraceLog, DeepCopy, GAME_FRAME_INF
from cl_commondefines import RELIC_TYPE_CURSE, DEFEND_TREND_NONE, STATE_DUALWIELD, MAX_GSCASH, BIGDATA_WARCASH, TYPE_RELIFE_ALL, LINK_DISCONNECT, WARRIOR_HERO, DEFEND_TREND_SHIELD, DEFEND_TREND_ARMOR, BASEATTR_REFRESH, PF_SWITCHWEAPON, FORBID_FILLBULLET, FORBID_SWITCHWEAPON, FORBID_ATTACK, CHANGEWARCASHSUBMSG_COST, CHANGEWARCASHSUBMSG_ADD, ADJUST_GRADEPF, GAMBLER_HERO, OBJECT_CURPET, EXECUTOR_HERO, INKMASTER_HERO, ADD_DEVICE_ENERGY, COST_DEVICE_ENERGY, OBJECT_OWNER, OBJECT_SERVANT, OBJECT_DEVICE, GetAllCanAddGsCashPlayMode, PF_SHIFT, GARDENER_HERO, BASEATTR_CLIENT, PF_TYPE_TALENT, PF_TYPE_RELIC, PF_TYPE_BENEDICTION
from cl_commondefines import SKILLRET_SUCCESS, SKILLRET_FAIL, DEFAULT_HERO
from cl_object.logging import WarcashLog, CashLog, ErrLog, WarobjLog, SeasonLog
from cl_propdata import PC_SEND_BC
from cllib.lib_only import RunMobileData
from cl_formula import g_HeroGradeAttr
from cl_putdata import PUT_HERO, GetPutState
import itertools
import importlib
import cl_hero.load
import cl_warrior
import cl_netattr
import cl_formula
import cl_hero.herostatus
import cl_container.itemcon
import cl_container.talentcon
import cl_container.reliccon
import cl_container.benedictioncon
import cl_container.bulletcon
import cl_container.bulletchangecon
import cl_container.cheekcon
import cl_container.emotioncon
import cl_container.gamblercon
import cl_container.flawcon
import cl_container.inkcon
import cl_container.taskcon
import cl_container.weaponskincon
import cl_container.herosidepetcon
import cl_container.deviceperformcon
import cl_container.petcon
import cl_container.wandcon
import cl_container.dicecon
import cl_container.backpackcon
import cl_container.gardenercon
import cl_container.s8con
import cl_drop
import cl_msgcenter
import cl_forbid
import cl_item.cnet
import cl_item.defines as itemdef
import cl_action
import cl_shop.herobuy
import cl_snetwar
import cl_object.dielog
import cl_sublimation
import cl_reward
import cl_achievement.mobject
import cl_progressunlock
import cl_anima
import cl_war
import cl_newunlockprogress.mobject
import cllib.lib_flag as lib_flag
import cl_extraattr
import cl_seasontalent
import cl_season.mobject
import cl_device.mobject
import cli_player
import cl_perform.net
from . import linerandom
MAX_DYINGTIMES = 99
MAX_UPGRADERELIC = 10000

class CBaseHeroData(object):
    m_SID = 101
    m_HeroName = '英雄'
    m_Shape = 101
    m_Career = 150
    m_InitGrade = 1
    m_MaxGrade = 1
    m_GradeInfo = { }
    m_AttPerform = 0
    m_DefendTrend = DEFEND_TREND_NONE
    m_PerformList = ()
    m_HeroPerform = { }
    m_CommonPerform = (PF_SWITCHWEAPON,)
    m_BaseAttr = { }
    m_CustomConArgs = { }
    
    def ResetGradeFormulaAttr(self, oHero, oWarHeroData):
        iRefreshFlag = BASEATTR_REFRESH
        dAttr = { }
        dAttr.update(self.m_BaseAttr)
        if oWarHeroData:
            dAttr.update(oWarHeroData.m_BaseAttr)
        cl_formula.ResetGradeFormulaAttr(oHero, dAttr, oHero.m_Grade, iRefreshFlag)

    
    def InitBaseAttr(self, oHero):
        oWarHeroData = oHero.m_Game.m_WarData.GetHeroData(oHero.m_SID)
        oHero.m_HeroName = self.m_HeroName
        oHero.m_Shape = self.m_Shape
        oHero.m_Career = self.m_Career
        oHero.m_AttPerform = self.m_AttPerform
        oHero.m_PerformList = self.m_PerformList
        oHero.m_CommonPerform = self.m_CommonPerform
        if not oHero.m_Grade:
            oHero.m_Grade = self.m_InitGrade
        self.ResetGradeFormulaAttr(oHero, oWarHeroData)
        oHero.m_DefendTrend = self.m_DefendTrend
        oHero.m_Speed = oHero.QueryAttr('MoveSpeed')
        oHero.m_HP = oHero.QueryAttr('HPMax')
        oHero.m_Armor = oHero.QueryAttr('ArmorMax')
        oHero.m_Shield = oHero.QueryAttr('ShieldMax')
        oHero.m_Energy = oHero.QueryAttr('EnergyMax')
        if self.m_DefendTrend & ~DEFEND_TREND_SHIELD:
            oHero.AttrForceSet('ShieldMax', 0, 'DefendTrend')
            oHero.AttrForceSet('RShield', 0, 'DefendTrend')
        if self.m_DefendTrend & ~DEFEND_TREND_ARMOR:
            oHero.AttrForceSet('ArmorMax', 0, 'DefendTrend')
        oHero.m_HeroPerform = DeepCopy(self.m_HeroPerform)
        oHero.m_CustomConArgs = self.m_CustomConArgs



class CBaseHero(cl_warrior.CWarrior):
    m_Type = 'Hero'
    m_FightType = WARRIOR_HERO
    m_PropChangeBCType = PC_SEND_BC
    m_PFSwitchedMsg = {
        'Career': cl_msgcenter.MSG_WAR_SWITCH_CAREER_PERFORM }
    m_GroundMaxDis = 30
    
    def __init__(self, oGame, nid, pid):
        super(CBaseHero, self).__init__(oGame, nid)
        self.m_PlayerID = pid
        self.m_OwnerPlayerID = pid
        self.m_OwnerName = ''
        self.m_HeroName = ''
        self.m_WarCash = 0
        self.m_TotalGainWarCash = 0
        self.m_InitGSCash = 0
        self.m_WarGSCash = 0
        self.m_NpcUICallBack = None
        self.m_UICallBack = { }
        self.m_UIMenuIdx = 1
        self.m_NpcUIMenuIdx = 1
        self.m_ClientSummonID = PRODUCT_MIN_CSUMMON_ID
        self.m_TalentCon = None
        self.m_BenedictionCon = None
        self.m_RelicCon = None
        self.m_BulletChangeCon = None
        self.m_GamblerCon = None
        self.m_UndergoScene = set()
        self.m_Online = LINK_DISCONNECT
        self.m_ClientFrame = 0
        self.m_DieLogMgr = cl_object.dielog.CDieLogMgr(oGame, self.m_ID)
        iSeed = oGame.Random(10000)
        self.m_LineRandom = linerandom.CLinearRandom(iSeed)
        self.m_Busted = 0
        self.m_TeamPF = 1
        self.m_WaitingSkill = { }
        self.m_WeaponWaitingSkill = { }
        self.m_PerformWaitingSkill = { }
        self.m_FramingSkill = { }
        self.m_FramingCache = { }
        self.m_CurUIFlag = ()
        self.m_MapLoadOKCBFun = { }
        self.m_MapLoadOKMsg = { }
        self.m_CoverCbFun = { }
        self.m_SplitPacket = { }
        self.m_Servant = 0
        self.m_HeroPerform = { }
        self.m_Resistance = cl_extraattr.CResistance('Resistance', 0)
        self.m_PerformCDRate = cl_extraattr.CPerformCDRate()
        self.m_WarCashInfo = { }
        self.m_OnGame = 1
        self.m_CustomConArgs = { }
        self.m_ExtraPickUpRule = []
        self.m_DeviceEnergy = 0
        self.m_RelicTalentCon = None
        self.m_DeviceMgr = None
        self.m_DevicePerformCon = None
        self.m_PetCon = None
        self.m_WandCon = None
        self.m_DiceCon = None
        self.m_BackpackCon = None
        self.m_S8Con = None
        self.m_FuncModeInfo = { }
        self.m_FuncModeExtraInfo = { }
        self.m_SeasonTalent = { }
        self.m_Settled = False
        self.m_SeasonCon = None
        self.m_SeasonSaveKey = ''
        self.SetAttr('ChargeSpeed', 100, BASEATTR_REFRESH | BASEATTR_CLIENT)
        self.SetAttr('JumpHeight', 100, BASEATTR_REFRESH | BASEATTR_CLIENT)

    
    def Release(self):
        if self.m_ReleaseFlag:
            return None
        self.OnSettleWar()
        cl_msgcenter.DoneEvent(self, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, 'InitHeroMapLoadOK')
        if lib_flag.g_IsAuthorityRun:
            cl_msgcenter.DoneEvent(self, cl_msgcenter.MSG_WAR_AFTERADDCASH, 'CollectWarCashInfo')
        self.m_TaskCon.Release()
        super(CBaseHero, self).Release()
        self.m_BuyMgr.Release()
        self.m_BulletCon.Release()
        self.m_ItemCon.Release()
        self.m_TalentCon.Release()
        self.m_BenedictionCon.Release()
        self.m_RelicCon.Release()
        self.m_WieldCon.Release()
        self.m_BulletChangeCon.Release()
        self.m_DieLogMgr.Release()
        self.m_ExWeaponCon.Release()
        self.m_WeaponStoreCon.Release()
        self.m_WeaponSkinCon.Release()
        self.m_HeroSidePetCon.Release()
        self.SeasonConRelease()
        if self.m_SID in g_CustomCon and 'ReleaseFunc' in g_CustomCon[self.m_SID]:
            releasefunc = g_CustomCon[self.m_SID]['ReleaseFunc']
            releasefunc(self)
        self.m_GamblerCon = None
        self.m_ItemCon = None
        self.m_TalentCon = None
        self.m_BenedictionCon = None
        self.m_RelicCon = None
        self.m_WieldCon = None
        self.m_BulletChangeCon = None
        self.m_DieLogMgr = None
        self.m_ExWeaponCon = None
        self.m_WeaponStoreCon = None
        self.m_TaskCon = None
        self.m_RelicTalentCon = None
        self.m_Resistance = None
        self.m_PerformCDRate = None
        self.m_SeasonTaskMgr = None
        self.m_WeaponSkinCon = None
        self.m_HeroSidePetCon = None
        self.m_DevicePerformCon = None
        self.m_DeviceMgr = None
        self.m_PetCon = None
        self.m_WandCon = None
        self.m_DiceCon = None
        self.m_BackpackCon = None
        self.m_MapLoadOKCBFun = { }
        self.m_MapLoadOKMsg = { }
        self.m_CoverCbFun = { }
        self.m_SeasonCon = None

    
    def InitHero(self, iHeroGrade, iPlayerGrade, iHeroSID):
        import cl_container.relictalentcon
        self.m_SID = iHeroSID
        self.m_Grade = iHeroGrade
        self.m_PlayerGrade = iPlayerGrade
        oData = GetHeroData(iHeroSID)
        oData.InitBaseAttr(self)
        if self.m_SID in g_CustomCon and 'InitFunc' in g_CustomCon[self.m_SID]:
            initfunc = g_CustomCon[self.m_SID]['InitFunc']
            initfunc(self, self.m_CustomConArgs)
        self.InitWarValue()
        self.m_Perform.SetOwner(self)
        self.m_ShootStatusMgr = cl_hero.herostatus.CShootStatusMgr(self)
        self.m_BuyMgr = cl_shop.herobuy.CHeroBuyMgr(self.m_Game, self.m_ID)
        self.m_WieldCon = cl_container.itemcon.CWieldContainer(self.m_Game, self.m_ID)
        self.m_ExWeaponCon = cl_container.itemcon.CExWeaponContainer(self.m_Game, self.m_ID)
        self.m_WeaponStoreCon = cl_container.itemcon.CWeaponStoreContainer(self.m_Game, self.m_ID)
        self.m_ItemCon = cl_container.itemcon.CItemContainer(self.m_Game, self.m_ID)
        self.m_TalentCon = cl_container.talentcon.CTalentContainer(self)
        self.m_BenedictionCon = cl_container.benedictioncon.CBenedictionContainer(self)
        self.m_RelicCon = cl_container.reliccon.CRelicContainer(self)
        self.m_BulletCon = cl_container.bulletcon.CBulletContainer(self.m_Game, self.m_ID, self.m_PlayerID)
        self.m_UnlockProgressCon = cl_progressunlock.CProgressUnlock(self.m_Game, self.m_ID, self.m_PlayerID)
        self.m_BulletChangeCon = cl_container.bulletchangecon.CBulletChangeContainer(self)
        self.m_Achievement = cl_achievement.mobject.CAchievementStatMgr(self.m_Game, self.m_ID, self.m_PlayerID)
        self.m_CheekCon = cl_container.cheekcon.CCheekContainer(self.m_Game, self.m_ID, self.m_PlayerID)
        self.m_EmotionCon = cl_container.emotioncon.CEmotionContainer(self.m_Game, self.m_ID, self.m_PlayerID)
        self.m_NewUnlockProgressMgr = cl_newunlockprogress.mobject.CUnlockProgressMgr(self.m_Game, self.m_ID, self.m_PlayerID)
        self.m_TaskCon = cl_container.taskcon.CTaskContainer(self)
        self.m_SeasonTaskMgr = cl_season.mobject.CSeasonTaskMgr(self.m_Game, self.m_ID, self.m_PlayerID)
        self.m_WeaponSkinCon = cl_container.weaponskincon.CWeaponSkinContainer(self.m_Game, self.m_ID, self.m_PlayerID)
        self.m_HeroSidePetCon = cl_container.herosidepetcon.CHeroSidePetContainer(self.m_Game, self.m_ID, self.m_PlayerID)
        iSeasonNum = self.m_Game.m_WarMgr.m_SeasonNum
        InitSeasonCon(iSeasonNum, self)
        self.SetCtrlModelData()
        self.AddHeroGradePerform()
        self.GiveInitWeapon()
        cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.OnMapLoadOK, 'InitHeroMapLoadOK', -1, 0)
        if lib_flag.g_IsAuthorityRun:
            cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_AFTERADDCASH, self.OnAddCash, 'CollectWarCashInfo', -1, 0)

    
    def OnAddCash(self, oHero, dInfo):
        iAdd = -dInfo['Cash']
        if iAdd < 0:
            return None
        sReason = dInfo['Reason']
        lstUnDealInfo = self.m_WarCashInfo.setdefault('UnDealInfo', [])
        lstUnDealInfo.append((sReason, iAdd))

    
    def OnSettleWar(self):
        if self.m_Settled:
            return None
        self.m_Settled = True
        who = cli_player.GetPlayer(self.m_PlayerID, self.m_Game.m_ID)
        if who:
            who.UnbindHero()
        self.DisableUnlockProgressCon()
        self.m_UnlockProgressCon = None
        if self.m_Achievement:
            self.m_Achievement.Release()
            self.m_Achievement = None
        if self.m_NewUnlockProgressMgr:
            self.m_NewUnlockProgressMgr.Release()
            self.m_NewUnlockProgressMgr = None
        if self.m_SeasonTaskMgr:
            self.m_SeasonTaskMgr.Release()
            self.m_SeasonTaskMgr = None

    
    def DisableUnlockProgressCon(self):
        if self.m_UnlockProgressCon:
            self.m_UnlockProgressCon.Release()

    
    def GS2CCreateInfo(self):
        self.HeroNetAddTo({
            self.m_PlayerID: 1 })
        cl_netattr.ExtHeroProp(self)
        self.m_WieldCon.Refresh()
        self.m_ExWeaponCon.Refresh()
        self.m_WeaponStoreCon.Refresh()
        self.m_Perform.Refresh()
        self.m_State.Refresh()
        self.m_BulletChangeCon.Refresh()
        self.m_TaskCon.Refresh()
        if self.m_RelicCon:
            self.m_RelicCon.SelfRefresh()
        self.m_HeroSidePetCon.SelfRefresh()
        self.SeasonConSelfRefresh()
        self.GS2CPropChange('CurWeapon')
        self.GS2CPropChange('DeputyWeapon')
        self.RefreshRelifeInfo()
        self.m_EmotionCon.Refresh()
        self.m_SeasonTaskMgr.Refresh()
        cl_snetwar.GS2CPerformanceInfo(self.m_PlayerID, 1)
        self.SyncExtraPickUpRule()
        self.RefreshFuncMode()

    
    def GetHeroBaseProp(self):
        return cl_netattr.GetHeroBaseProp(self)

    
    def SetPlayerID(self, iNewID):
        self.m_PlayerID = iNewID
        if self.m_Perform:
            self.m_Perform.m_PlayerID = iNewID
        if self.m_TalentCon:
            self.m_TalentCon.m_PlayerID = iNewID
        if self.m_RelicCon:
            self.m_RelicCon.m_PlayerID = iNewID
        if self.m_BenedictionCon:
            self.m_BenedictionCon.m_PlayerID = iNewID

    
    def Name(self):
        return self.m_OwnerName

    
    def SetName(self, sName):
        if sName == self.m_OwnerName:
            return None
        self.m_OwnerName = sName
        self.GS2CPropChange('Name')

    
    def HeroName(self):
        return self.m_HeroName

    
    def MaxRelicNum(self):
        return self.m_RelicCon.MaxRelicNum()

    
    def MapSendPacket(self, dPlayer):
        cl_netattr.MakeHeroAddPacket(self, dPlayer)

    
    def WarGrade(self):
        return self.m_Grade

    
    def SetGrade(self, iGrade):
        self.m_Grade = iGrade

    
    def RandomSeed(self):
        return self.m_LineRandom.GetSeed()

    
    def DebugStatus(self):
        return self.Query('DebugStatus', 0)

    
    def GetPerformSIDByType(self, iPFType):
        lstPerform = super().GetPerformSIDByType(iPFType)
        lstPerform.extend(self.m_RelicCon.GetPerformSIDByType(iPFType))
        lstPerform.extend(self.m_TalentCon.GetPerformSIDByType(iPFType))
        lstPerform.extend(self.m_BenedictionCon.GetPerformSIDByType(iPFType))
        if self.m_RelicTalentCon:
            lstPerform.extend(self.m_RelicTalentCon.GetPerformSIDByType(iPFType))
        if self.m_DevicePerformCon:
            lstPerform.extend(self.m_DevicePerformCon.GetPerformSIDByType(iPFType))
        return lstPerform

    
    def GetHeroDetailData(self, dInfo = None, bCreateSeed = False):
        dData = { }
        dData['SID'] = self.m_SID
        dData['SET'] = self.Save()
        dData['TL'] = self.m_TalentCon.Save()
        dData['RL'] = self.m_RelicCon.Save()
        dData['WP'] = self.m_WieldCon.SaveEquip()
        dData['STA'] = self.m_State.Save()
        dData['BE'] = self.m_BenedictionCon.Save()
        dData['TK'] = self.m_TaskCon.Save()
        dData['FM'] = dict(self.m_FuncModeInfo)
        dData['HS'] = self.m_HeroSidePetCon.Save()
        dData.update(self.SeasonConSave(bCreateSeed))
        if not bCreateSeed:
            dData['WS'] = self.m_WeaponSkinCon.Save()
            dData['WEP'] = self.m_ExWeaponCon.SaveEquip()
            dData['WEPS'] = self.m_WeaponStoreCon.SaveEquip()
            dData['BT'] = self.m_BulletCon.Save()
            dData['HP'] = self.m_HP if not self.IsDying() else max(100, self.QueryAttr('HPMax') // 10)
            dData['SD'] = self.m_Shield
            dData['EY'] = self.m_Energy
            dData['AR'] = self.m_Armor
            dData['CH'] = self.m_WarCash
            dData['GSCH'] = self.m_WarGSCash
            dData['TCH'] = self.m_TotalGainWarCash
            dData['SEAT'] = self.m_SeasonTalent
            dData['EHP'] = self.m_ExcessHP
            dData['ESD'] = self.m_ExcessShield
            dData['EAR'] = self.m_ExcessArmor
            dAllAttr = { }
            for sAttr in g_HeroGradeAttr:
                oAttr = self.GetAttr(sAttr)
                dAttr = oAttr.Save()
                if dAttr:
                    dAllAttr[sAttr] = dAttr
            
            dData['AT'] = dAllAttr
            if self.m_SID in g_CustomCon and 'SaveFunc' in g_CustomCon[self.m_SID]:
                savefunc = g_CustomCon[self.m_SID]['SaveFunc']
                savefunc(self, dData)
            oDieElement = self.m_Game.m_WarMgr.GetComponent('PVEDieElement')
            if oDieElement:
                dRelife = oDieElement.Save(self.m_ID)
            else:
                dRelife = { }
            dData['RLF'] = dRelife
            dData['DEAD'] = 1 if self.IsRealDied() else 0
            if dInfo and 'BossLevelGoal' in dInfo:
                oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
                if oLevelCtrl and oLevelCtrl.m_CurNode:
                    iLevel = oLevelCtrl.m_CurNode.m_Level
                    vPos = self.GetPos()
                    tFace = self.GetFacing()
                    dData['BLG'] = {
                        'Level': iLevel,
                        'Pos': vPos,
                        'Facing': tFace }
            dData['UPC'] = self.m_UnlockProgressCon.Save() if self.m_UnlockProgressCon else { }
            dData['NUPM'] = self.m_NewUnlockProgressMgr.Save() if self.m_NewUnlockProgressMgr else { }
            dData['ACHI'] = self.m_Achievement.Save() if self.m_Achievement else { }
        else:
            dData['PID'] = self.m_PlayerID
            dData['GD'] = self.m_Grade
            if self.m_PetCon:
                dData['SPC'] = self.m_PetCon.SaveSeed()
        return dData

    
    def LoadHero(self, dHero):
        self.Set('Loading', 1)
        for sAttr, dAttr in dHero['AT'].items():
            oAttr = self.GetAttr(sAttr)
            if oAttr:
                oAttr.Load(self, dAttr)
        
        self.Load(dHero.get('SET', { }))
        self.m_TalentCon.Load(dHero['TL'])
        self.m_RelicCon.Load(dHero['RL'])
        self.m_WeaponSkinCon.Load(dHero.get('WS', { }))
        self.m_WieldCon.LoadEquip(dHero.get('WP', { }))
        self.m_ExWeaponCon.LoadEquip(dHero.get('WEP', { }))
        self.m_WeaponStoreCon.LoadEquip(dHero.get('WEPS', { }))
        self.m_BulletCon.Load(dHero['BT'])
        self.m_UnlockProgressCon.Load(dHero.get('UPC', { }))
        self.m_NewUnlockProgressMgr.Load(dHero.get('NUPM', { }))
        self.m_Achievement.Load(dHero.get('ACHI', { }))
        self.m_BenedictionCon.Load(dHero.get('BE', { }))
        self.m_TaskCon.Load(dHero.get('TK', { }))
        self.m_HeroSidePetCon.Load(dHero.get('HS', { }))
        self.SeasonConLoad(dHero)
        self.m_State.Load(dHero.get('STA', { }))
        self.Set('STA', dHero.get('STA', { }))
        self.AddSeasonTalent(dHero.get('SEAT', { }))
        self.m_FuncModeInfo = dHero.get('FM', { })
        self.LoadExcessAttr('HP', dHero.get('EHP', 0))
        self.LoadExcessAttr('Shield', dHero.get('ESD', 0))
        self.LoadExcessAttr('Armor', dHero.get('EAR', 0))
        self.m_HP = dHero['HP']
        self.m_Shield = dHero['SD']
        self.m_Armor = dHero.get('AR', self.QueryAttr('ArmorMax'))
        self.m_Energy = dHero.get('EY', 0)
        self.m_WarCash = dHero['CH']
        self.m_TotalGainWarCash = dHero.get('TCH', 0)
        if self.m_SID in g_CustomCon and 'LoadFunc' in g_CustomCon[self.m_SID]:
            loadfunc = g_CustomCon[self.m_SID]['LoadFunc']
            loadfunc(self, dHero)
        oDieElement = self.m_Game.m_WarMgr.GetComponent('PVEDieElement')
        if oDieElement:
            oDieElement.Load(self.m_ID, dHero['RLF'])
        iRealDead = dHero.get('DEAD', 0)
        if iRealDead:
            self.RealDie()
            self.m_Game.m_WarMgr.RemoveLivePlayer(self.m_PlayerID)
        self.Set('Loading', 0)

    
    def GetHeroWeaponDetailData(self):
        dData = {
            'WP': self.m_WieldCon.SaveEquip(),
            'WEP': self.m_ExWeaponCon.SaveEquip(),
            'WEPS': self.m_WeaponStoreCon.SaveEquip() }
        return dData

    
    def GetOwnObjectID(self, iObjectType):
        if iObjectType == OBJECT_OWNER:
            return self.m_ID
        if iObjectType == OBJECT_DEVICE:
            return self.GetDeviceID()
        if iObjectType == OBJECT_SERVANT:
            return self.m_Servant
        if iObjectType == OBJECT_CURPET:
            return self.m_PetCon.m_CurPet
        return 0

    
    def SetRelifeInfo(self, dInfo):
        self.Set('RelifeInfo', dInfo)

    
    def AddRelifeInfo(self, iType, sKey, iTime, iTimes, iPriority, iMaxTimes = 0):
        super().AddRelifeInfo(iType, sKey, iTime, iTimes, iPriority, iMaxTimes = iMaxTimes)
        self.RefreshRelifeInfo(iSelfInfoChange = 1)

    
    def ModifyRelifeCnt(self, iType, sKey, iModify, iMaxModify = 0):
        if iType not in TYPE_RELIFE_ALL:
            return 0
        dInfo = self.Query('RelifeInfo', { })
        dType = dInfo.setdefault(iType, { })
        if sKey not in dType:
            return 0
        (iTime, iTimes, iMaxTimes, iPriority) = dType[sKey]
        iMaxTimes += iMaxModify
        if iMaxTimes < 0:
            iMaxTimes = 0
        iNewTimes = iTimes + iModify
        if iNewTimes < 0:
            iNewTimes = 0
        elif iNewTimes > iMaxTimes:
            iNewTimes = iMaxTimes
        dType[sKey] = [
            iTime,
            iNewTimes,
            iMaxTimes,
            iPriority]
        self.Set('RelifeInfo', dInfo)
        self.RefreshRelifeInfo(iSelfInfoChange = 1)
        return iNewTimes - iTimes

    
    def CostRelifeTimes(self, iType, sKey):
        super().CostRelifeTimes(iType, sKey)
        self.RefreshRelifeInfo(iSelfInfoChange = 1)

    
    def RefreshRelifeInfo(self, iSelfInfoChange = 0):
        lstHeroInfo = []
        if iSelfInfoChange:
            lstHero = [
                self.m_ID]
            lstPlayer = self.m_Game.m_WarMgr.GetRoomPlayer()
        else:
            lstHero = self.m_Game.m_WarMgr.GetAllHero()
            lstPlayer = [
                self.m_PlayerID]
        for iHero in lstHero:
            lstAllInfo = []
            oHero = self.m_Game.GetObject(iHero)
            if oHero:
                for iType in TYPE_RELIFE_ALL:
                    (iRest, iTotal) = oHero.GetRelifeTimesAndMaxTimesByType(iType)
                    lstAllInfo.append((iType, iRest, iTotal))
                
            lstHeroInfo.append((iHero, lstAllInfo))
        
        cl_snetwar.GS2CRelifeInfo(self.m_Game, lstHeroInfo, lstPlayer)

    
    def InitDyingSecond(self, iSecond):
        iMaxDyingSecond = self.QuerySavedData('MaxDyingSecond')
        if iSecond > iMaxDyingSecond:
            self.SetSavedData('MaxDyingSecond', iSecond)
        self.RefreshDyingSecond(sReason = 'init')

    
    def RefreshDyingSecond(self, sReason = 'refresh'):
        iSecond = self.GetRestDyingSecond()
        self.SetSavedData('RestDyingSecond', iSecond)
        self.GS2CPropChange('RestDyingSecond', iSecond)
        WarobjLog.Debug('%d %d %d curdyingsecond %s %s' % (self.m_Game.m_ID, self.m_PlayerID, self.m_ID, iSecond, sReason))

    
    def CostDyingTimes(self):
        self.AddDeadPunishmentTimes(sReason = 'cost')
        iDyingTimes = self.QuerySavedData('DyingTimes', 0) + 1
        iDyingTimes = min(MAX_DYINGTIMES, iDyingTimes)
        self.SetSavedData('DyingTimes', iDyingTimes)
        self.GS2CPropChange('DyingTimes', iDyingTimes)

    
    def GetRestDyingSecond(self):
        iMaxDyingSecond = self.QuerySavedData('MaxDyingSecond')
        iDeadPunishmentTimes = self.QuerySavedData('DeadPunishmentTimes')
        if not self.m_Agent:
            oDieElement = self.m_Game.m_WarMgr.GetComponent('PVEDieElement')
            iMinDyingSecond = oDieElement.m_MinDyingSecond
            iRestDyingSecond = max(iMaxDyingSecond - oDieElement.m_TimesSubSecond * iDeadPunishmentTimes, iMinDyingSecond)
        else:
            iRestDyingSecond = iMaxDyingSecond
        dTempDyingSecond = self.Query('TempDyingSecond', { })
        iAdd = 10000
        iMul = 10000
        for _Add, _Mul in dTempDyingSecond.values():
            iAdd += _Add
            if _Mul < -10000:
                _Mul = -10000
            iMul = iMul * (10000 + _Mul) // 10000
        
        if iAdd < 0:
            iAdd = 0
        iRestDyingSecond = iRestDyingSecond * iAdd * iMul // 10000 // 10000
        return iRestDyingSecond

    
    def AddTempDyingSecond(self, sKey, iAdd, iMul, sReason = 'addtemp'):
        dTempDyingSecond = self.SetDefault('TempDyingSecond', { })
        dTempDyingSecond[sKey] = (iAdd, iMul)
        self.RefreshDyingSecond(sReason = sReason)

    
    def RecoverTempDyingSecond(self, sKey, sReason = 'recovertemp'):
        dTempDyingSecond = self.Query('TempDyingSecond', { })
        if sKey in dTempDyingSecond:
            dTempDyingSecond.pop(sKey)
        self.RefreshDyingSecond(sReason = sReason)

    
    def GetDeadPunishmentTimes(self):
        return self.QuerySavedData('DeadPunishmentTimes')

    
    def AddDeadPunishmentTimes(self, iAdd = 1, sReason = 'add'):
        iNowPunishmentTimes = self.GetDeadPunishmentTimes()
        if (not iAdd or iNowPunishmentTimes == 0) and iAdd < 0:
            return None
        iRealAdd = iAdd
        if iNowPunishmentTimes < -iAdd:
            iRealAdd = -iNowPunishmentTimes
        iResult = min(MAX_DYINGTIMES, iRealAdd + iNowPunishmentTimes)
        self.SetSavedData('DeadPunishmentTimes', iResult)
        self.GS2CPropChange('DeadPunishmentTimes', iResult)
        self.RefreshDyingSecond(sReason = sReason)

    
    def AddSublimation(self, dSubliamation):
        oGame = self.m_Game
        WarobjLog.Debug('%d %d addsublimation %s' % (self.m_Game.m_ID, self.m_PlayerID, list(dSubliamation)))
        for iSID, iLevel in dSubliamation.items():
            lstReward = cl_sublimation.GetSublimationWarReward(iSID, iLevel)
            if lstReward:
                dExtInfo = {
                    'SourceLevel': iLevel,
                    'LogReward': 0 }
                cl_reward.RewardItem(oGame, self, lstReward, 'sublimation', dExtInfo)
        

    
    def AddAnimaModule(self, dAnimaModule):
        oGame = self.m_Game
        lstAnimaModule = list(dAnimaModule)
        WarobjLog.Debug('%d %d animamodule %s' % (self.m_Game.m_ID, self.m_PlayerID, lstAnimaModule))
        lstModuleInfo = []
        for iSID, (iStatu, iX, iY) in dAnimaModule.items():
            lstModuleInfo.append((iSID, iStatu, iX, iY))
            lstReward = cl_anima.GetAnimaModuleWarReward(iSID, 1)
            if lstReward:
                dExtInfo = {
                    'SourceLevel': 1,
                    'LogReward': 0 }
                cl_reward.RewardItem(oGame, self, lstReward, 'animamodule', dExtInfo)
        
        self.Set('AnimaModule', lstModuleInfo)

    
    def AddSeasonTalent(self, dSeasonTalent):
        oGame = self.m_Game
        SeasonLog.Debug('%d %d addseasontalent %s %s' % (oGame.m_ID, self.m_PlayerID, dSeasonTalent, self.m_SeasonTalent))
        oWarMgr = self.m_Game.m_WarMgr
        iSeasonNum = oWarMgr.m_SeasonNum
        dAllSeasonTalent = cl_seasontalent.GetSeasonTalentBySeasonNum(iSeasonNum)
        for iSID in dSeasonTalent:
            if iSID not in dAllSeasonTalent:
                SeasonLog.Alert('%d %d curseason:%s unknownseasontalent:%d %s' % (oGame.m_ID, self.m_PlayerID, iSeasonNum, iSID, dAllSeasonTalent))
                continue
            lstReward = cl_seasontalent.GetSeasonTalentWarReward(iSID)
            if lstReward:
                dExtInfo = {
                    'LogReward': 0 }
                cl_reward.RewardItem(oGame, self, lstReward, 'Talent', dExtInfo)
        
        self.m_SeasonTalent = dSeasonTalent

    
    def HasSeasonTalent(self, iSID):
        if iSID in self.m_SeasonTalent:
            return True
        return False

    
    def MaxCash(self):
        iGetMaxCash = self.Query('TempMaxCash', 0)
        if iGetMaxCash <= 0 or iGetMaxCash > 65535:
            return 65535
        return iGetMaxCash

    
    def ValidSendBuyItemReport(self, sReason):
        if 'PF5756' in sReason:
            return 0
        if 'ST1616' in sReason:
            return 0
        if 'ST1617' in sReason:
            return 0
        if 'ST1429' in sReason:
            return 0
        return 1

    
    def AddCash(self, iCash, sReason, iSendMsg = 1, iLog = 1):
        if not isinstance(iCash, int):
            RaiseError('%d warcash not int, %s % s' % (self.m_PlayerID, iCash, type(iCash)))
            iCash = int(iCash)
        dData = {
            'owner': self.m_ID,
            'Cash': iCash,
            'Reason': sReason }
        if iSendMsg:
            if iCash > 0:
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GETWARCASH, self, dData)
            elif iCash < 0:
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_COSTWARCASH, self, dData)
        iCash = dData['Cash']
        iTemp = self.m_WarCash + iCash
        if iTemp < 0:
            RaiseError('%d warcash < 0, %d %d %s' % (self.m_PlayerID, self.m_WarCash, iCash, sReason))
            return 0
        if iTemp > self.MaxCash():
            iTemp = self.MaxCash()
        iTrueAdd = iTemp - self.m_WarCash
        if iLog:
            WarcashLog.Info('%d %d %d %d %s' % (self.m_Game.m_ID, self.m_PlayerID, iTrueAdd, iTemp, sReason))
        self.m_WarCash = iTemp
        self.GS2CPropChange('WarCash')
        if iCash < 0 or self.ValidSendBuyItemReport(sReason):
            self.m_Game.m_WarMgr.HandleBuyItemReport(self.m_PlayerID, iCash, sReason, BIGDATA_WARCASH)
        else:
            self.m_TotalGainWarCash += iCash
        iSub = CHANGEWARCASHSUBMSG_COST if iCash < 0 else CHANGEWARCASHSUBMSG_ADD
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_AFTERADDCASH, self, {
            'owner': self.m_ID,
            'Cash': iTrueAdd,
            'TotalCash': self.m_WarCash,
            'Reason': sReason,
            'PreCash': iCash }, iSub = iSub)
        return iTrueAdd

    
    def Cash(self):
        return self.m_WarCash

    
    def AddGSCash(self, iCash, sReason):
        if not isinstance(iCash, int):
            RaiseError('%d wargscash not int, %s % s' % (self.m_PlayerID, iCash, type(iCash)))
            iCash = int(iCash)
        if self.m_Game.m_WarMgr.m_PlayMode not in GetAllCanAddGsCashPlayMode():
            SendAlert('err', '英雄%d在错误玩法模式%s增加战场外金币(%d),%s' % (self.m_PlayerID, self.m_Game.m_WarMgr.m_PlayMode, iCash, sReason))
            return 0
        if not iCash:
            return 0
        if iCash < 0:
            SendAlert('err', '英雄%d增加的战场外金币量为负数(%d),%s' % (self.m_PlayerID, iCash, sReason))
            return 0
        iNew = self.m_WarGSCash + iCash
        CashLog.Debug('%d add %d %d %s' % (self.m_PlayerID, iCash, iNew, sReason))
        iLimit = MAX_GSCASH
        if iNew > iLimit:
            CashLog.Debug('%s limit %s %s %s %s' % (self.m_PlayerID, iCash, iNew, iLimit, sReason))
            iNew = iLimit
        self.m_WarGSCash = iNew
        dData = {
            'owner': self.m_ID,
            'Cash': iCash,
            'Reason': sReason,
            'TotalCash': self.m_WarGSCash }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ADDGSCASH, self, dData)
        self.GS2CPropChange('WarGSCash')
        return iCash

    
    def InitGSCash(self, iCash):
        self.m_InitGSCash = iCash
        self.m_WarGSCash = iCash
        self.GS2CPropChange('WarGSCash')

    
    def GSCash(self):
        return self.m_WarGSCash

    
    def ConsumeGSCash(self, iCash, sReason):
        if not isinstance(iCash, int):
            RaiseError('%d wargscash not int, %s % s' % (self.m_PlayerID, iCash, type(iCash)))
            iCash = int(iCash)
        if not iCash:
            return 0
        if iCash < 0:
            SendAlert('err', '英雄%d消费的战场外金币量为负数(%d),%s' % (self.m_PlayerID, iCash, sReason))
            return 0
        iTemp = self.m_WarGSCash - iCash
        if iTemp < 0:
            RaiseError('%d wargscash < 0, %d %d %s' % (self.m_PlayerID, self.m_WarGSCash, iCash, sReason))
            return 0
        CashLog.Info('%d -%d %d %s' % (self.m_PlayerID, iCash, iTemp, sReason))
        self.m_WarGSCash = iTemp
        dData = {
            'owner': self.m_ID,
            'Cash': iCash,
            'Reason': sReason,
            'TotalCash': self.m_WarGSCash }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CONSUMEGSCASH, self, dData)
        self.GS2CPropChange('WarGSCash')
        return iCash

    
    def SetGSCash(self, iCash, iCurChangeNo = -1):
        pass

    
    def Cheat(self):
        self.m_Busted = 1

    
    def IsCheat(self):
        return self.m_Busted

    
    def IncMenuIdx(self):
        self.m_NpcUIMenuIdx += 1
        if self.m_NpcUIMenuIdx > 65535:
            self.m_NpcUIMenuIdx = 1

    
    def AddKey(self, dKey, sReason):
        oWarMgr = self.m_Game.m_WarMgr
        oTeamInfoElement = oWarMgr.GetComponent('TeamInfo')
        if oTeamInfoElement:
            oTeamInfoElement.m_KeyCon.AddKey(dKey, sReason)
        else:
            SendAlert('err', '%d战场未配置队伍信息插件, 无法添加队伍钥匙' % oWarMgr.m_SID)

    
    def CostKey(self, dKey, sReason):
        oWarMgr = self.m_Game.m_WarMgr
        oTeamInfoElement = oWarMgr.GetComponent('TeamInfo')
        if oTeamInfoElement:
            oTeamInfoElement.m_KeyCon.CostKey(dKey, sReason)

    
    def ValidCostKey(self, dKey):
        oWarMgr = self.m_Game.m_WarMgr
        oTeamInfoElement = oWarMgr.GetComponent('TeamInfo')
        if oTeamInfoElement:
            return oTeamInfoElement.m_KeyCon.ValidCostKey(dKey)
        return 0

    
    def CheckCartoonStart(self, iActNum, dNetData):
        if iActNum not in self.m_WaitingSkill:
            return None
        dCartoonStart = self.m_WaitingSkill[iActNum]['CartoonStart']
        for iNode in dNetData:
            if iNode not in dCartoonStart:
                dCartoonStart[iNode] = self.m_Game.GetFrameNum()
        

    
    def WaitToPerform(self, iPerform, dData, iWaitFrame):
        if iPerform in self.m_PerformWaitingSkill:
            return False
        iActNum = dData['ActNum']
        self.m_PerformWaitingSkill[iPerform] = iActNum
        self.m_WaitingSkill[iActNum] = {
            'CartoonStart': { },
            'NetData': [],
            'Perform': iPerform }
        self.CheckCartoonStart(iActNum, dData['Net'])
        func = Functor(self.UsePerformWaitingSkill, iPerform, dData, iActNum)
        self.Call_Out(func, iWaitFrame, 'WaitToPerform')
        return True

    
    def UsePerformWaitingSkill(self, iPerform, dData, iActNum):
        dWait = self.m_WaitingSkill.pop(iActNum, { })
        if not dWait:
            return None
        if iPerform in self.m_PerformWaitingSkill:
            self.m_PerformWaitingSkill.pop(iPerform)
        if 'Custom' in dData:
            dData['Custom']['CartoonStart'] = dWait['CartoonStart']
        else:
            dData['Custom'] = {
                'CartoonStart': dWait['CartoonStart'] }
        iRet = cl_war.UseCachePerform(self, iPerform, dData, dWait['NetData'])
        if iRet == SKILLRET_FAIL:
            cl_perform.net.GS2CSkillFail(self, iActNum)

    
    def WaitToAttack(self, iPerform, dData, iWaitFrame):
        iWeapon = dData['Weapon'] if 'Weapon' in dData else 0
        lstActNum = self.m_WeaponWaitingSkill.setdefault(iWeapon, [])
        if len(lstActNum) >= 5:
            return False
        iActNum = dData['ActNum']
        dData['CacheAttack'] = 1
        if not lstActNum:
            self.m_WaitingSkill[iActNum] = {
                'CartoonStart': { },
                'NetData': [],
                'Perform': iPerform,
                'Data': dData }
            self.CheckCartoonStart(iActNum, dData['Net'])
            func = Functor(self.UseWeaponWaitingSkill, iPerform, dData, iActNum)
            self.Call_Out(func, iWaitFrame, 'WaitToAttack')
        else:
            self.m_WaitingSkill[iActNum] = {
                'CartoonStart': { },
                'NetData': [],
                'Perform': iPerform,
                'Data': dData }
        lstActNum.append(iActNum)
        return True

    
    def UseWeaponWaitingSkill(self, iPerform, dData, iActNum):
        iWeapon = dData['Weapon'] if 'Weapon' in dData else 0
        if iWeapon not in self.m_WeaponWaitingSkill:
            return None
        lstActNum = self.m_WeaponWaitingSkill[iWeapon]
        if iActNum not in lstActNum:
            return None
        lstActNum.remove(iActNum)
        dWait = self.m_WaitingSkill.pop(iActNum, { })
        if 'Custom' in dData:
            dData['Custom']['CartoonStart'] = dWait['CartoonStart']
        else:
            dData['Custom'] = {
                'CartoonStart': dWait['CartoonStart'] }
        iRet = cl_war.UseCachePerform(self, iPerform, dData, dWait['NetData'])
        if iRet == SKILLRET_SUCCESS:
            if lstActNum:
                iNextActNum = lstActNum[0]
                if iNextActNum not in self.m_WaitingSkill:
                    WarobjLog.Debug('game:%s player: %s %s no nextactnum %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iPerform, iActNum, iNextActNum))
                    for iActNum in lstActNum:
                        self.m_WaitingSkill.pop(iActNum, None)
                        cl_perform.net.GS2CSkillFail(self, iActNum)
                    
                    self.m_WeaponWaitingSkill.pop(iWeapon, None)
                    return None
                iPerform = self.m_WaitingSkill[iNextActNum]['Perform']
                dData = self.m_WaitingSkill[iNextActNum]['Data']
                iWeapon = dData['Weapon'] if 'Weapon' in dData else 0
                oPerform = self.GetPerform(iPerform, iWeapon)
                if not oPerform:
                    return None
                iWaitFrame = oPerform.m_Container.GetColdTime(iPerform)
                if iWaitFrame > 0:
                    func = Functor(self.UseWeaponWaitingSkill, iPerform, dData, iNextActNum)
                    self.Call_Out(func, iWaitFrame, 'WaitToAttack')
                else:
                    WarobjLog.Debug('game:%s player: %s waitcd invalid %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iPerform, iWaitFrame))
                    self.UseWeaponWaitingSkill(iPerform, dData, iNextActNum)
        else:
            cl_perform.net.GS2CSkillFail(self, iActNum)
            for iActNum in lstActNum:
                self.m_WaitingSkill.pop(iActNum, None)
                cl_perform.net.GS2CSkillFail(self, iActNum)
            
            self.m_WeaponWaitingSkill.pop(iWeapon, None)

    
    def HaltWaitSkill(self, iActNum):
        dWait = self.m_WaitingSkill.pop(iActNum, None)
        if not dWait:
            return None
        cl_perform.net.GS2CSkillFail(self, iActNum)
        iPerform = dWait['Perform']
        if iPerform in self.m_PerformWaitingSkill:
            self.m_PerformWaitingSkill.pop(iPerform, None)
        elif 'Data' in dWait:
            dData = dWait['Data']
            iWeapon = dData['Weapon'] if 'Weapon' in dData else 0
            if iWeapon in self.m_WeaponWaitingSkill:
                lstActNum = self.m_WeaponWaitingSkill[iWeapon]
                if iActNum in lstActNum:
                    lstActNum.remove(iActNum)

    
    def ClearWaitSkill(self):
        for iActNum in self.m_WaitingSkill:
            cl_perform.net.GS2CSkillFail(self, iActNum)
        
        self.m_WaitingSkill = { }
        self.m_WeaponWaitingSkill = { }
        self.m_PerformWaitingSkill = { }
        self.Remove_Call_Out('WaitToAttack')
        self.Remove_Call_Out('WaitToPerform')

    
    def CacheWaitingSkill(self, iActNum, dNetData):
        if iActNum not in self.m_WaitingSkill:
            return None
        self.CheckCartoonStart(iActNum, dNetData)
        self.m_WaitingSkill[iActNum]['NetData'].append(dNetData)

    
    def CacheFramingSkill(self, iActNum, dNetData):
        if iActNum not in self.m_FramingCache:
            self.m_FramingCache[iActNum] = []
        self.m_FramingCache[iActNum].append(dNetData)

    
    def QueryAttrForecast(self, sAttr):
        if sAttr == 'ShootStatus':
            return self.ShootStatus()

    
    def SwitchSnipe(self, iOpen):
        return self.m_ShootStatusMgr.SwitchSnipe(self, iOpen)

    
    def SyncSnipeChange(self):
        self.GS2CPropChange('ShootStatus')

    
    def ShootStatus(self):
        return self.m_ShootStatusMgr.GetSnipeStatus()

    
    def SnipeShape(self):
        oCurWeapon = self.m_WieldCon.GetCurWeapon()
        if not oCurWeapon:
            return 0
        return oCurWeapon.GetComponent('Snipe').GetSnipeShape()

    
    def ValidSwitchWeapon(self, iPos):
        return self.m_ShootStatusMgr.ValidSwitchWeapon(self, iPos)

    
    def SwitchWeapon(self, iPos):
        return self.m_ShootStatusMgr.SwitchWeapon(self, iPos)

    
    def ValidOpenDualWield(self):
        return self.m_ShootStatusMgr.ValidDualWield(self)

    
    def InDualWield(self):
        return self.m_ShootStatusMgr.IsDualWield(self)

    
    def OpenDualWield(self):
        return self.m_ShootStatusMgr.DualWield(self)

    
    def CloseDualWield(self):
        if self.m_ReleaseFlag:
            return None
        return self.m_ShootStatusMgr.CloseDualWield(self)

    
    def GetInitWeaponSID(self):
        oData = GetHeroData(self.m_SID)
        return oData.m_InitWeapon

    
    def GetWeaponByID(self, iItemID):
        oWeapon = self.m_WieldCon.GetItemByID(iItemID)
        if not oWeapon:
            oWeapon = self.m_ExWeaponCon.GetItemByID(iItemID)
        return oWeapon

    
    def HaltDualWieldState(self):
        iState = STATE_DUALWIELD
        oState = self.m_State.GetItemBySID(iState)
        if oState:
            self.m_State.RemoveItem(oState.m_ID)

    
    def SyncWeaponChange(self, iHoldPos = itemdef.MAIN_HOLD):
        if iHoldPos & itemdef.MAIN_HOLD:
            self.GS2CPropChange('CurWeapon')
        if iHoldPos & itemdef.DEPUTY_HOLD:
            self.GS2CPropChange('DeputyWeapon')

    
    def CurWeapon(self):
        return self.m_WieldCon.CurWeaponDesc(itemdef.MAIN_HOLD)

    
    def Desc(self):
        return self.m_WieldCon.GetAllItemDesc(self)

    
    def DeputyWeapon(self):
        return self.m_WieldCon.CurWeaponDesc(itemdef.DEPUTY_HOLD)

    
    def MoveStatus(self):
        return 0

    
    def IsForbid(self, iType, dPassRule = None, iWeapon = 0, iCache = 0):
        if dPassRule:
            lstForbidRule = []
            if iWeapon:
                oWeapon = self.m_WieldCon.GetItemByID(iWeapon)
                if oWeapon:
                    lstForbidRule.extend(oWeapon.m_ForbidRuleInfo.keys())
                else:
                    for oWeapon, _ in self.m_WieldCon.GetHoldWeapon():
                        lstForbidRule.extend(oWeapon.m_ForbidRuleInfo.keys())
                    
            for iRule in itertools.chain(self.m_ForbidRuleInfo.keys(), lstForbidRule):
                if iRule in dPassRule:
                    continue
                dForbid = cl_forbid.GetRule2Forbid(iRule)
                if iType in dForbid:
                    ErrLog.Debug('player: %s, forbidruleid: %s' % (self.m_PlayerID, iRule))
                    return 1
            
        elif iType in self.m_ForbidTypeInfo:
            ForbidTypeInfoLog(self, self.m_ForbidTypeInfo, iType, iCache)
            return 1
        if iWeapon:
            oWeapon = self.m_WieldCon.GetItemByID(iWeapon)
            if oWeapon and iType in oWeapon.m_ForbidTypeInfo:
                ForbidTypeInfoLog(self, oWeapon.m_ForbidTypeInfo, iType, iCache)
                return 1
        for oWeapon, _ in self.m_WieldCon.GetHoldWeapon():
            if iType in oWeapon.m_ForbidTypeInfo:
                ForbidTypeInfoLog(self, oWeapon.m_ForbidTypeInfo, iType, iCache)
                return 1
        
        return 0

    
    def AddExtraPickUpRule(self, iRule):
        if iRule in self.m_ExtraPickUpRule:
            return None
        if iRule not in cl_drop.EXTRAPICKUPRULE_FUNC:
            return None
        self.m_ExtraPickUpRule.append(iRule)
        self.SyncExtraPickUpRule()

    
    def RemoveExtraPickUpRule(self, iRule):
        if iRule not in self.m_ExtraPickUpRule:
            return None
        self.m_ExtraPickUpRule.remove(iRule)
        self.SyncExtraPickUpRule()

    
    def SyncExtraPickUpRule(self):
        cl_snetwar.GS2CChangeExtraPickUpRule(self.m_PlayerID, self.m_ExtraPickUpRule)

    
    def UpdateFuncMode(self, iMode, iTimes, dInfo):
        if iTimes < 0:
            WarobjLog.Debug('%s %s update times err %s %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iMode, iTimes, self.m_FuncModeInfo))
            return None
        self.m_FuncModeInfo[iMode] = iTimes
        self.m_FuncModeExtraInfo[iMode] = dInfo
        dNetInfo = { }
        dNetInfo.update(dInfo)
        dNetInfo['Times'] = iTimes
        cl_snetwar.GS2CSwitchFuncMode(self.m_PlayerID, iMode, dNetInfo)

    
    def AddFuncModeTimes(self, iMode, iTimes):
        if iTimes <= 0:
            WarobjLog.Debug('%s %s add times err %s %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iMode, iTimes, self.m_FuncModeInfo))
            return None
        dFuncModeInfo = self.m_FuncModeInfo
        if iMode not in dFuncModeInfo:
            WarobjLog.Debug('%s %s add no mode %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iMode, self.m_FuncModeInfo))
            return None
        dFuncModeInfo[iMode] += iTimes
        cl_snetwar.GS2CSwitchFuncMode(self.m_PlayerID, iMode, {
            'Times': dFuncModeInfo[iMode] })

    
    def CostFuncModeTimes(self, iMode, iCost):
        if not iCost:
            WarobjLog.Debug('%s %s cost times err %s %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iMode, iCost, self.m_FuncModeInfo))
            return None
        if iMode in self.m_FuncModeInfo:
            if self.m_FuncModeInfo[iMode] <= iCost:
                self.m_FuncModeInfo[iMode] = 0
            else:
                self.m_FuncModeInfo[iMode] -= iCost
            cl_snetwar.GS2CSwitchFuncMode(self.m_PlayerID, iMode, {
                'Times': self.m_FuncModeInfo[iMode] })

    
    def LoadFuncMode(self, dLoadInfo):
        self.m_FuncModeInfo = dLoadInfo
        self.RefreshFuncMode()

    
    def RefreshFuncMode(self):
        for iMode, iTimes in self.m_FuncModeInfo.items():
            dNetInfo = { }
            if iMode in self.m_FuncModeExtraInfo:
                dNetInfo.update(self.m_FuncModeExtraInfo[iMode])
            dNetInfo['Times'] = iTimes
            cl_snetwar.GS2CSwitchFuncMode(self.m_PlayerID, iMode, dNetInfo)
        

    
    def GetFuncModeTimes(self, iMode):
        if iMode not in self.m_FuncModeInfo:
            return 0
        return self.m_FuncModeInfo[iMode]

    
    def GetFuncMode(self):
        return self.m_FuncModeInfo

    
    def GetFunModeInfo(self, iMode, iKey):
        dFuncModeExtraInfo = self.m_FuncModeExtraInfo
        if iMode not in dFuncModeExtraInfo or iKey not in dFuncModeExtraInfo[iMode]:
            return 0
        return dFuncModeExtraInfo[iMode][iKey]

    
    def ClearTransFactorInState(self, tStateUseTransFactor, sKey):
        if self.m_SID == GARDENER_HERO:
            dPlant = self.m_GardenerCon.m_PlantDict
            if not dPlant:
                return None
            for oPlant in list(dPlant.values()):
                for iState in tStateUseTransFactor:
                    lstState = oPlant.m_State.GetItems(iState)
                    if not lstState:
                        continue
                    for oState in lstState:
                        dTransFactor = oState.GetArgValue('TransDamFactor', { })
                        dTransFactor.pop(sKey, 0)
                    
                
            
            return None
        for iState in tStateUseTransFactor:
            lstState = self.m_State.GetItems(iState)
            if not lstState:
                continue
            for oState in lstState:
                dTransFactor = oState.GetArgValue('TransDamFactor', { })
                dTransFactor.pop(sKey, 0)
            
        

    
    def GetStateUseTransFactor(self):
        tStateUseTransFactor = ()
        oHeroData = cl_hero.GetHeroData(self.m_SID)
        if not oHeroData:
            return tStateUseTransFactor
        tStateUseTransFactor = oHeroData.m_StateUseTransFactor
        return tStateUseTransFactor

    
    def GetMaxBullet(self, iBulletSID):
        if not cl_item.load.HasBulletType(iBulletSID):
            return 9999
        return self.m_BulletCon.ReturnMaxBullet(iBulletSID)

    
    def GetPerform(self, iPerform, iItemID = 0, iOwnPfid = 0):
        if self.m_ReleaseFlag:
            return None
        if iOwnPfid:
            oPerform = self.m_BulletChangeCon.GetPerform(iOwnPfid, iPerform)
            return oPerform
        if iItemID:
            oItem = self.m_WieldCon.GetItemByID(iItemID)
            if oItem:
                oPerformCom = oItem.GetComponent('Perform')
                if not oPerformCom:
                    return None
                return oPerformCom.GetPerform(iPerform)
        oPerform = self.m_Perform.GetPerform(iPerform)
        if oPerform:
            return oPerform
        clsPerform = cl_perform.GetPerformModule(iPerform)
        if clsPerform:
            iPfType = clsPerform.m_PFType
            if iPfType in g_Type2GetPerform:
                func = g_Type2GetPerform[iPfType]
                oPerform = func(self, iPerform, iItemID)
                if oPerform:
                    return oPerform
        oSeasonCon = self.m_SeasonCon
        if oSeasonCon:
            oPerform = oSeasonCon.GetPerform(iPerform, iItemID)
        return oPerform

    
    def GetCareerPerform(self):
        dPerform = self.m_HeroPerform
        if 'Career' not in dPerform:
            return None
        iCareerPerform = dPerform['Career']
        return self.GetPerform(iCareerPerform)

    
    def GetThrowPerform(self):
        dPerform = self.m_HeroPerform
        if 'Throw' not in dPerform:
            return None
        iThrowPerform = dPerform['Throw']
        return self.GetPerform(iThrowPerform)

    
    def GetCareerPerformID(self):
        dPerform = self.m_HeroPerform
        if 'Career' not in dPerform:
            return 0
        return dPerform['Career']

    
    def GetThrowPerformID(self):
        dPerform = self.m_HeroPerform
        if 'Throw' not in dPerform:
            return 0
        return dPerform['Throw']

    
    def GetShiftPerform(self):
        return self.GetPerform(PF_SHIFT)

    
    def SwitchPerform(self, sType, iPerform):
        dPerform = self.m_HeroPerform
        if sType not in dPerform:
            return None
        iOldPerform = dPerform[sType]
        if iPerform == iOldPerform:
            return None
        oNewPerform = self.GetPerform(iPerform)
        if not oNewPerform:
            return None
        oOldPerform = self.GetPerform(iOldPerform)
        if oOldPerform:
            oOldPerform.Disable(self)
        oNewPerform.Enable(self)
        dPerform[sType] = iPerform
        if self.m_Agent:
            self.m_Agent.SwitchPerform(sType, iPerform)
        if sType in self.m_PFSwitchedMsg:
            cl_msgcenter.SendMsg(self.m_PFSwitchedMsg[sType], self, {
                'NewPerform': iPerform,
                'OldPerform': iOldPerform })
        self.m_Perform.GS2CPerformAdd(oNewPerform)

    
    def GiveInitWeapon(self):
        oWeapon = cl_item.CreateEquip(self.m_Game, self.GetInitWeaponSID(), 0)
        if not oWeapon:
            return None
        oWeapon.SetOwner(self.m_ID)
        oWeapon.PutToContainer(oWeapon.GetTargetContainer(self), 'Init')
        oBulletCom = oWeapon.GetComponent('Bullet')
        oBulletCom.BulletModify(oBulletCom.QueryAttr('MaxBullet'), iSendMsg = 0)

    
    def AddHeroGradePerform(self):
        oData = GetHeroData(self.m_SID)
        iInitGrade = oData.m_InitGrade
        dGradeInfo = oData.m_GradeInfo
        for iGrade in range(iInitGrade, self.m_Grade + 1):
            if iGrade not in dGradeInfo:
                continue
            iPerform = dGradeInfo[iGrade]['Perform']
            iTruePerform = self.m_Game.m_WarData.GetTruePassive(ADJUST_GRADEPF, iPerform)
            if iTruePerform:
                self.AddPerform(iTruePerform, 1)
        

    
    def Online(self):
        return self.m_Online

    
    def SetLinkStatus(self, iStatus):
        if self.m_Online == iStatus:
            return None
        self.m_Online = iStatus
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CHANGE_PLAYER_LINKSTATUS, self, {
            'Hero': self.m_ID,
            'LinkStatus': iStatus })
        self.GS2CPropChange('Online')

    
    def NewClientSummonID(self):
        self.m_ClientSummonID += 1
        if self.m_ClientSummonID >= PRODUCT_MIN_NPC_ID:
            self.m_ClientSummonID = PRODUCT_MIN_CSUMMON_ID + 1
        return self.m_ClientSummonID

    
    def CreateClientSummon(self, iTrueSummonID):
        dSummon = self.Query('CSummon', { })
        iClientID = self.NewClientSummonID()
        dSummon[iClientID] = iTrueSummonID
        self.Set('CSummon', dSummon)
        return iClientID

    
    def SetClientSummon(self, iCSummonID, iTrueSummonID):
        dSummon = self.Query('CSummon', { })
        dSummon[iCSummonID] = iTrueSummonID
        self.Set('CSummon', dSummon)

    
    def GetCSummonTrueID(self, iCSummonID):
        dSummon = self.Query('CSummon', { })
        if iCSummonID in dSummon:
            return dSummon[iCSummonID]
        return iCSummonID

    
    def EnterScene(self, iOldScene):
        super(CBaseHero, self).EnterScene(iOldScene)
        if self.m_Scene:
            self.m_UndergoScene.add(self.m_Scene)
        self.GS2CPropChange('Scene', self.m_Scene)

    
    def LeaveScene(self, iNewScene):
        super(CBaseHero, self).LeaveScene(iNewScene)
        self.Set('CSummon', { })

    
    def LeaveGame(self):
        if not self.m_OnGame:
            return None
        dMsgInfo = {
            'Hero': self.m_ID }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_PLAYERLEAVEGAME, self, dMsgInfo)
        if 'Halt' in dMsgInfo:
            return None
        self.m_OnGame = 0
        self.StopShieldRecover('Quit')
        self.m_TaskCon.PauseSelf('LeaveGame')
        self.AllPerformDisable()
        self.SwitchSnipe(0)
        if self.m_Servant:
            oServant = self.m_Game.GetObject(self.m_Servant)
            if oServant:
                oServant.Remove('PlayerRelease')
            self.m_Servant = 0
        if self.m_PetCon:
            self.m_PetCon.PetLeaveBattle(iLeaveGame = 1)
        self.LeaveScene(0)

    
    def AllPerformDisable(self, iNotify = 0):
        self.m_Perform.AllPerformDisable(iNotify)
        self.m_State.DisableAllState(0)
        self.m_TalentCon.AllPerformDisable(iNotify)
        self.m_RelicCon.AllPerformDisable(iNotify)
        self.m_BenedictionCon.AllPerformDisable(iNotify)
        self.m_BulletChangeCon.AllPerformDisable(iNotify)
        self.SeasonConAllPerformDisable(iNotify)

    
    def DieClearEffect(self):
        self.SwitchSnipe(0)
        super(CBaseHero, self).DieClearEffect()

    
    def OnGoto(self):
        oGame = self.m_Game
        iSelf = self.m_ID
        lstPlayer = oGame.m_WarMgr.GetRoomPlayer()
        cl_snetwar.GS2CTeamInfo(oGame, [
            iSelf], dict.fromkeys(lstPlayer, 1))
        if not self.m_Agent:
            oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Scene)
            lstHero = list(oScene.GetHeros()) if oScene else []
            if iSelf in lstHero:
                lstHero.remove(iSelf)
            cl_snetwar.GS2CTeamInfo(oGame, lstHero, {
                self.m_PlayerID: 1 })

    
    def NetAddTo(self, dPlayer):
        if not dPlayer:
            return None
        for func in self.m_ExtPacketFunc.values():
            func(self, dPlayer)
        

    
    def HeroNetAddTo(self, dPlayer):
        super(CBaseHero, self).NetAddTo(dPlayer)
        self.m_WieldCon.Refresh(dPlayer)
        self.m_ItemCon.Refresh(dPlayer)
        self.m_BulletCon.Refresh(dPlayer)
        self.m_TalentCon.Refresh(dPlayer)
        self.m_RelicCon.Refresh(dPlayer)
        self.m_BenedictionCon.Refresh(dPlayer)
        self.SeasonConRefresh(dPlayer)

    
    def OnPlayerReady(self, iNewLogin):
        oGame = self.m_Game
        iPlayer = self.m_PlayerID
        if iNewLogin:
            self.GS2CCreateInfo()
            lstAllPlayer = oGame.m_WarMgr.GetAllPlayer()
            for pid in lstAllPlayer:
                if pid == iPlayer:
                    continue
                obj = oGame.m_WarMgr.GetHeroByPlayer(pid)
                if obj:
                    obj.HeroNetAddTo({
                        iPlayer: 1 })
            
        self.SwitchSnipe(0)
        cl_action.HaltAllCasting(self, 'MapLoadOk')

    
    def ValidEnterNewScene(self, iScene):
        if iScene not in self.m_UndergoScene:
            return 1
        return 0

    
    def SetTeamPF(self, iOpen):
        if self.m_TeamPF == iOpen:
            return None
        self.m_TeamPF = 1 if iOpen else 0

    
    def GetRemoveCurseRelicValid(self):
        return self.Query('CurseRelic', 0)

    
    def SetRemoveCurseRelicValid(self, iValid):
        self.Set('CurseRelic', iValid)
        self.GS2CPropChange('CurseRelic')
        lstRefresh = self.m_RelicCon.GetAllRelicByType(RELIC_TYPE_CURSE)
        self.m_RelicCon.RefreshRelicItemInfo(lstRefresh)

    
    def GetRollRelicCnt(self):
        return self.QuerySavedData('RollRelicCnt', 0)

    
    def SetRollRelicCnt(self, iCnt):
        iCnt = max(iCnt, 0)
        self.SetSavedData('RollRelicCnt', iCnt)
        self.GS2CPropChange('RollRelicCnt')

    
    def GetUpgradeRelicCnt(self):
        return self.QuerySavedData('UpgradeRelicCnt', 0)

    
    def SetUpgradeRelicCnt(self, iCnt):
        iCnt = max(iCnt, 0)
        if iCnt > MAX_UPGRADERELIC:
            iCnt = MAX_UPGRADERELIC
        self.SetSavedData('UpgradeRelicCnt', iCnt)

    
    def BurstCount(self):
        return self.Query('BurstCount', 0)

    
    def SetBurstCount(self, iCount):
        self.Set('BurstCount', iCount)
        self.GS2CPropChange('BurstCount')

    
    def AddBurstCount(self, iAdd):
        iBurstCount = max(self.Query('BurstCount', 0) + iAdd, 0)
        self.Set('BurstCount', iBurstCount)
        self.GS2CPropChange('BurstCount')

    
    def GetMaxRelicRollNum(self):
        return self.Query('MaxRelicRollNum', 0)

    
    def AddMaxRelicRollNum(self, iAdd):
        iMax = max(self.GetMaxRelicRollNum() + iAdd, 0)
        self.Set('MaxRelicRollNum', iMax)
        self.GS2CPropChange('MaxRelicRollNum')

    
    def GetRelicChooseAllCnt(self):
        return self.QuerySavedData('RelicChooseAllCnt', 0)

    
    def SetRelicChooseAllCnt(self, iCnt):
        self.SetSavedData('RelicChooseAllCnt', iCnt)
        self.GS2CPropChange('RelicChooseAllCnt')

    
    def HPModifyDam(self, iAttack, lstChange):
        if iAttack and iAttack != self.m_ID:
            oAttack = self.m_Game.GetObject(iAttack)
            if oAttack and oAttack.m_PlayerID and self.CheckDamTraceCD():
                sText = f'''hpmodifydam {self.m_SID} recvdam from {oAttack.m_SID} {oAttack.m_ID}'''
                SendAlert('err', sText)
                TraceLog('err', sText)
                return ([
                    0,
                    0,
                    0], [], [])
        return super().HPModifyDam(iAttack, lstChange)

    
    def Resistance(self):
        return self.m_Resistance.m_CurValue

    
    def MagicPower(self):
        if not self.m_RelicTalentCon:
            return 0
        return self.m_RelicTalentCon.m_MagicPower

    
    def NewUIMenuIdx(self):
        self.m_UIMenuIdx += 1
        if self.m_UIMenuIdx > 65535:
            self.m_UIMenuIdx = 1
        return self.m_UIMenuIdx

    
    def AddMapLoadOKCbFun(self, sFlag, cFun, iPriority = 0, iOnce = 0):
        WarobjLog.Debug('%s %s addmaploadfunc %s %s %s %s' % (self.m_Game.m_ID, self.m_PlayerID, sFlag, cFun, iPriority, iOnce))
        dMapLoadOKCBFun = self.m_MapLoadOKCBFun.setdefault(iPriority, { })
        dMapLoadOKCBFun[sFlag] = (cFun, iOnce)

    
    def RemoveMapLoadOKCbFun(self, sFlag, iPriority = 0):
        WarobjLog.Debug('%s %s removemaploadfunc %s %s' % (self.m_Game.m_ID, self.m_PlayerID, sFlag, iPriority))
        if iPriority not in self.m_MapLoadOKCBFun:
            return None
        if sFlag in self.m_MapLoadOKCBFun[iPriority]:
            self.m_MapLoadOKCBFun[iPriority].pop(sFlag)
            if not self.m_MapLoadOKCBFun[iPriority]:
                self.m_MapLoadOKCBFun.pop(iPriority)
            if self.m_CurUIFlag == (iPriority, sFlag):
                self.m_CurUIFlag = ()

    
    def OnMapLoadOK(self, oOwner, dMsgInfo):
        for tCurFlag, (cOldFun, iOnce) in self.m_CoverCbFun.items():
            (iPriority, sFlag) = tCurFlag
            iPriority = int(iPriority)
            if cOldFun:
                self.m_MapLoadOKCBFun[iPriority][sFlag] = (cOldFun, iOnce)
                continue
            if iPriority in self.m_MapLoadOKCBFun:
                self.m_MapLoadOKCBFun[iPriority].pop(sFlag, 0)
        
        self.m_CoverCbFun = { }
        self.m_MapLoadOKMsg = dMsgInfo
        lstPriority = sorted(self.m_MapLoadOKCBFun, reverse = True)
        dFinishFunc = { }
        for iPriority in lstPriority:
            iOver = 1
            dFinishFunc[iPriority] = []
            dMapLoadOKCBFun = self.m_MapLoadOKCBFun[iPriority]
            for sFlag, (cFun, iOnce) in dMapLoadOKCBFun.items():
                self.m_CurUIFlag = (iPriority, sFlag)
                iOver = cFun(self, dMsgInfo)
                if not iOver:
                    break
                if iOnce:
                    dFinishFunc[iPriority].append(sFlag)
            
            if not iOver:
                break
        else:
            self.m_CurUIFlag = ()
        for iPriority in dFinishFunc:
            if iPriority not in self.m_MapLoadOKCBFun:
                continue
            dMapLoadOKCBFun = self.m_MapLoadOKCBFun[iPriority]
            for sFlag in dFinishFunc[iPriority]:
                dMapLoadOKCBFun.pop(sFlag, 0)
            
            if not dMapLoadOKCBFun:
                self.m_MapLoadOKCBFun.pop(iPriority)
        

    
    def DoNextMapLoadOKCbFun(self):
        self.m_NpcUICallBack = None
        if not self.m_CurUIFlag:
            ErrLog.Alert('game:%s player: %s uiflag err  %s' % (self.m_Game.m_ID, self.m_PlayerID, self.m_MapLoadOKCBFun))
            return None
        (iCurPriority, sCurFlag) = self.m_CurUIFlag
        iCurPriority = int(iCurPriority)
        lstPriority = sorted(self.m_MapLoadOKCBFun, reverse = True)
        if iCurPriority not in lstPriority:
            ErrLog.Alert('game:%s player: %s mapload priority:%s err  %s' % (self.m_Game.m_ID, self.m_PlayerID, self.m_CurUIFlag, self.m_MapLoadOKCBFun))
            return None
        iCurPriIdx = lstPriority.index(iCurPriority)
        dFinishFunc = { }
        for iPriorityIdx in range(iCurPriIdx, len(lstPriority)):
            iOver = 1
            iPriority = lstPriority[iPriorityIdx]
            dFinishFunc[iPriority] = []
            lstFlag = list(self.m_MapLoadOKCBFun[iPriority])
            if iPriorityIdx == iCurPriIdx:
                iIndex = lstFlag.index(sCurFlag) + 1
            else:
                iIndex = 0
            iFuncLen = len(lstFlag)
            if iIndex >= iFuncLen:
                continue
            for iTemp in range(iIndex, iFuncLen):
                sFlag = lstFlag[iTemp]
                (cFun, iOnce) = self.m_MapLoadOKCBFun[iPriority][sFlag]
                self.m_CurUIFlag = (iPriority, sFlag)
                iOver = cFun(self, self.m_MapLoadOKMsg)
                if not iOver:
                    break
                if iOnce:
                    dFinishFunc[iPriority].append(sFlag)
            
            if not iOver:
                break
        else:
            self.m_CurUIFlag = ()
        (_, iOnce) = self.m_MapLoadOKCBFun[iCurPriority][sCurFlag]
        if iOnce:
            lstFinshFunc = dFinishFunc.setdefault(iCurPriority, [])
            lstFinshFunc.append(sCurFlag)
        for iPriority in dFinishFunc:
            if iPriority not in self.m_MapLoadOKCBFun:
                continue
            dMapLoadOKCBFun = self.m_MapLoadOKCBFun[iPriority]
            for sFlag in dFinishFunc[iPriority]:
                dMapLoadOKCBFun.pop(sFlag, 0)
            
            if not dMapLoadOKCBFun:
                self.m_MapLoadOKCBFun.pop(iPriority)
        

    
    def CoverCbFun(self, sFlag, cFun, iPriority = 0, iOnce = 1):
        tCurFlag = (iPriority, sFlag)
        if self.m_CurUIFlag:
            if self.m_CurUIFlag == tCurFlag:
                cFun(self)
            if tCurFlag in self.m_CoverCbFun:
                return None
            if iPriority not in self.m_MapLoadOKCBFun:
                self.m_MapLoadOKCBFun[iPriority] = { }
            (cOldFun, iOldOnce) = self.m_MapLoadOKCBFun[iPriority][sFlag] if sFlag in self.m_MapLoadOKCBFun[iPriority] else (None, iOnce)
            self.m_MapLoadOKCBFun[iPriority][sFlag] = (cFun, iOnce)
            self.m_CoverCbFun[tCurFlag] = (cOldFun, iOldOnce)
        else:
            self.m_CurUIFlag = tCurFlag
            cFun(self)

    
    def Call_Out_Lockable(self, func, iDelay, sFlag):
        self.Call_Out(func, iDelay, sFlag)

    
    def Remove_Call_Out_Lockable(self, sFlag):
        self.Remove_Call_Out(sFlag)

    
    def LockableCallBack(self, sKey):
        pass

    
    def ClearImmobilize(self, sKey, iSourceTarget):
        pass

    
    def GetDeviceSID(self):
        if not self.m_DeviceMgr:
            return 0
        return self.m_DeviceMgr.m_DeviceSID

    
    def GetDeviceID(self):
        if not self.m_DeviceMgr:
            return 0
        return self.m_DeviceMgr.m_Device

    
    def GetDevice(self):
        if not self.m_DeviceMgr:
            return None
        return self.m_DeviceMgr.GetDevice()

    
    def CheckDeciveStatus(self, iDeployed, iActive):
        if not self.m_DeviceMgr:
            return False
        return self.m_DeviceMgr.CheckDeciveStatus(iDeployed, iActive)

    
    def DeviceEnergy(self, iMaxDeviceEnergy = 0):
        if not iMaxDeviceEnergy:
            iMaxDeviceEnergy = self.MaxDeviceEnergy()
        iNowFrame = self.m_Game.GetFrameNum()
        iFrame = self.Query('CalDeviceEnergyFrame', iNowFrame)
        iAddFrame = iNowFrame - iFrame
        self.Set('CalDeviceEnergyFrame', iNowFrame)
        if iAddFrame > 0 and self.Query('DeviceEnergyStatus'):
            iRDeviceEnergy = self.QueryAttr('RDeviceEnergy')
            if iRDeviceEnergy > 0:
                iAdd = iRDeviceEnergy * iAddFrame // GAME_FRAME
                self.TrueDeviceEnergyModify(self.m_DeviceEnergy, iAdd, False, iMaxDeviceEnergy)
        if self.m_DeviceEnergy > iMaxDeviceEnergy:
            self.m_DeviceEnergy = iMaxDeviceEnergy
        return self.m_DeviceEnergy

    
    def DeviceEnergyModify(self, iChange):
        iOld = self.DeviceEnergy()
        return self.TrueDeviceEnergyModify(iOld, iChange, True)

    
    def TrueDeviceEnergyModify(self, iOld, iChange, iSendPropChange, iMax = 0):
        if not iChange:
            return 0
        if iChange > 0:
            if self.IsDead():
                return 0
            iChangeSub = ADD_DEVICE_ENERGY
        elif not iOld:
            return 0
        iChangeSub = COST_DEVICE_ENERGY
        dInfo = {
            'Alter': iChange }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CHANGE_DEVICE_ENERGY_BEFORE, self, dInfo, iSub = iChangeSub)
        iChange = dInfo['Alter']
        if not iMax:
            iMax = self.MaxDeviceEnergy()
        iNew = iOld + iChange
        if iNew > iMax:
            iNew = iMax
        elif iNew < 0:
            iNew = 0
        self.m_DeviceEnergy = iNew
        if iSendPropChange:
            self.GS2CPropChange('DeviceEnergy', iNew)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CHANGE_DEVICE_ENERGY, self, {
            'Alter': iChange,
            'TrueAlter': iNew - iOld }, iSub = iChangeSub)
        return iOld - iNew

    
    def MaxDeviceEnergy(self):
        return self.QueryAttr('MaxDeviceEnergy')

    
    def RDeviceEnergy(self):
        return self.QueryAttr('RDeviceEnergy')

    
    def UpdateDeviceEnergyRecoverStatus(self):
        if self.Query('StopDeviceEnergyRecoverInfo'):
            bRecover = False
        else:
            iRDeviceEnergy = self.QueryAttr('RDeviceEnergy')
            if iRDeviceEnergy <= 0:
                bRecover = False
            else:
                bRecover = True
        if self.Query('DeviceEnergyStatus'):
            self.Remove_Call_Out('DeviceEnergyRecoverStatusEnterStop')
            self.DeviceEnergy()
            if not bRecover:
                self.Set('DeviceEnergyStatus', 0)
                self.GS2CPropChange('DeviceEnergy')
                self.GS2CPropChange('DeviceEnergyStatus')
            elif bRecover:
                self.DeviceEnergy()
                self.Set('DeviceEnergyStatus', 1)
                self.GS2CPropChange('DeviceEnergy')
                self.GS2CPropChange('DeviceEnergyStatus')
        if None:
            self.Call_Out(self.UpdateDeviceEnergyRecoverStatus, GAME_FRAME, 'DeviceEnergyRecoverStatusEnterStop')

    
    def StopDeviceEnergyRecover(self, sFlag, iRestartFrame = 0):
        dStop = self.SetDefault('StopDeviceEnergyRecoverInfo', { })
        if sFlag in dStop:
            return None
        dStop[sFlag] = 1
        if iRestartFrame > 0:
            self.Call_Out(Functor(self.StartDeviceEnergyRecover, sFlag), iRestartFrame, 'DeviceEnergyRecoverSchedule' + sFlag)
        if len(dStop) == 1:
            self.UpdateDeviceEnergyRecoverStatus()

    
    def StartDeviceEnergyRecover(self, sFlag):
        dStop = self.SetDefault('StopDeviceEnergyRecoverInfo', { })
        if sFlag in dStop:
            self.Remove_Call_Out('DeviceEnergyRecoverSchedule' + sFlag)
            dStop.pop(sFlag)
        if not dStop:
            self.UpdateDeviceEnergyRecoverStatus()

    
    def ResetByDie(self):
        super().ResetByDie()
        self.StopDeviceEnergyRecover('Die')

    
    def OnRelife(self):
        super().OnRelife()
        self.StartDeviceEnergyRecover('Die')

    
    def IsOpenExtendBag(self, iType):
        return self.Query('ExtendBag', 0) & iType

    
    def SwitchExtendBag(self, iType, iOpen):
        sKey = 'ExtendBag'
        iExtendBag = self.Query(sKey, 0)
        if iOpen:
            iExtendBag = iExtendBag | iType
        else:
            iExtendBag = iExtendBag ^ iType
        self.Set(sKey, iExtendBag)
        self.GS2CPropChange(sKey)

    
    def SaveWeaponAttMode(self, iWeaponSID, iAttMode):
        dWeaponMode = self.SetDefaultSavedData('WeaponModeIdx', { })
        if iWeaponSID not in dWeaponMode:
            dWeaponMode[iWeaponSID] = [
                iAttMode,
                -1]
        else:
            dWeaponMode[iWeaponSID][0] = iAttMode

    
    def SaveWeaponCliMode(self, iWeaponSID, iCliMode):
        dWeaponMode = self.SetDefaultSavedData('WeaponModeIdx', { })
        if iWeaponSID not in dWeaponMode:
            dWeaponMode[iWeaponSID] = [
                -1,
                iCliMode]
        else:
            dWeaponMode[iWeaponSID][1] = iCliMode

    
    def GetWeaponMode(self, iWeaponSID):
        dWeaponMode = self.QuerySavedData('WeaponModeIdx', { })
        if iWeaponSID not in dWeaponMode:
            return [
                -1,
                -1]
        return dWeaponMode[iWeaponSID]

    
    def UpdatePos(self, tVec):
        oCopyHero = self.GetHeroCopyHero()
        if not oCopyHero:
            return None
        if oCopyHero.m_MoveCtrl and oCopyHero.m_Scene:
            
            try:
                oCopyHero.m_MoveCtrl.UpdateCtrlFrame(oCopyHero, self.m_Game.GetFrameNum())
            except:
                PythonError()


    
    def GetHeroCopyHero(self):
        who = cli_player.GetPlayer(self.m_PlayerID, self.m_Game.m_ID)
        if not who:
            return None
        return who.GetCopyHero()

    
    def SetCurSeasonCon(self, oSeasonCon, sSaveKey):
        self.m_SeasonCon = oSeasonCon
        self.m_SeasonSaveKey = sSaveKey

    
    def SeasonConRelease(self):
        oSeasonCon = self.m_SeasonCon
        if oSeasonCon:
            oSeasonCon.Release()

    
    def SeasonConRefresh(self, dPlayer):
        oSeasonCon = self.m_SeasonCon
        if oSeasonCon:
            oSeasonCon.Refresh(dPlayer)

    
    def SeasonConSelfRefresh(self):
        oSeasonCon = self.m_SeasonCon
        if oSeasonCon:
            oSeasonCon.SelfRefresh()

    
    def SeasonConLoad(self, dData):
        oSeasonCon = self.m_SeasonCon
        if oSeasonCon:
            sSaveKey = self.m_SeasonSaveKey
            oSeasonCon.Load(dData.get(sSaveKey, { }))

    
    def SeasonConSave(self, bCreateSeed):
        dData = { }
        oSeasonCon = self.m_SeasonCon
        if (not oSeasonCon or bCreateSeed) and not oSeasonCon.NeedCreateSeed():
            return { }
        sSaveKey = self.m_SeasonSaveKey
        dData[sSaveKey] = oSeasonCon.Save()
        return dData

    
    def SeasonConAllPerformDisable(self, iNotify):
        oSeasonCon = self.m_SeasonCon
        if oSeasonCon:
            oSeasonCon.AllPerformDisable(iNotify)



class CCtrlHero(CBaseHero):
    
    def OnInitToScene(self, tPos):
        super(CCtrlHero, self).OnInitToScene(tPos)
        self.SetSpeed(self.QueryAttr('MoveSpeed'))

    
    def EnterScene(self, iOldScene):
        super().EnterScene(iOldScene)
        self.m_MoveCtrl.Stop(self)

    
    def LeaveScene(self, iNewScene):
        super(CCtrlHero, self).LeaveScene(iNewScene)
        self.Stop()
        self.m_Game.m_SkillMgr.AttackLeaveScene(self.m_ID)
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Scene)
        if oScene:
            oScene.DelPlayer(self.m_PlayerID, self.m_ID)
        if self.m_Scene:
            self.RemoveFromScene()


if 'g_HeroMoudleObj' not in globals():
    g_HeroMoudleObj = { }

def NewCtrlHero(oGame, iHero, pid, iHeroSID, iHeroGrade, iPlayerGrade):
    if iHeroSID not in cl_hero.load.GetAllLoadHero() or not GetPutState(PUT_HERO, iHeroSID):
        WarobjLog.Alert('%d createhero err %s %s' % (oGame.m_ID, pid, iHeroSID))
        iHeroSID = DEFAULT_HERO
    oHero = CCtrlHero(oGame, iHero, pid)
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CREATEHERO, oHero, {
        'Hero': oHero.m_ID,
        'HeroSID': iHeroSID })
    oHero.InitHero(iHeroGrade, iPlayerGrade, iHeroSID)
    return oHero


def GetHeroData(iHeroSID):
    if iHeroSID not in cl_hero.load.GetAllLoadHero():
        return None
    if iHeroSID not in g_HeroMoudleObj:
        
        try:
            if RunMobileData():
                mod = importlib.import_module('cl_hero.mobile.h%3d' % iHeroSID)
            else:
                mod = importlib.import_module('cl_hero.pc.h%3d' % iHeroSID)
            g_HeroMoudleObj[iHeroSID] = mod.CHeroData()
        except:
            PythonError()
            return None

    return g_HeroMoudleObj[iHeroSID]


def ForbidTypeInfoLog(oHero, dForbidTypeInfo, iType, iCache):
    if iCache or iType not in (FORBID_FILLBULLET, FORBID_SWITCHWEAPON, FORBID_ATTACK):
        return None
    sForbid = ''
    for iForbidType in dForbidTypeInfo:
        sForbid += '%s, ' % iForbidType
    
    ErrLog.Debug('player: %s, forbidType: %s, type: %s' % (oHero.m_PlayerID, sForbid, iType))


def InitGamblerCon(oHero, dData):
    oHero.m_GamblerCon = cl_container.gamblercon.CGamblerContainer(oHero.m_Game, oHero)


def LoadGamblerCon(oHero, dData):
    oHero.m_GamblerCon.Load(dData.get('GBC', { }))


def ReleaseGamblerCon(oHero):
    oHero.m_GamblerCon.Release()


def SaveGamblerCon(oHero, dData):
    dData['GBC'] = oHero.m_GamblerCon.Save()


def InitFlawCon(oHero, dData):
    oHero.m_FlawCon = cl_container.flawcon.CFlawContainer(oHero.m_Game, oHero, dData)


def LoadFlawCon(oHero, dData):
    oHero.m_FlawCon.Load(dData.get('GBC', { }))


def ReleaseFlawCon(oHero):
    oHero.m_FlawCon.Release()


def SaveFlawCon(oHero, dData):
    dData['EXC'] = oHero.m_FlawCon.Save()


def InitInkCon(oHero, dData):
    oHero.m_InkCon = cl_container.inkcon.CInkContainer(oHero.m_Game, oHero, dData)


def LoadInkCon(oHero, dData):
    oHero.m_InkCon.Load(dData.get('IC', { }))


def ReleaseInkCon(oHero):
    oHero.m_InkCon.Release()


def SaveInkCon(oHero, dData):
    dData['IC'] = oHero.m_InkCon.Save()


def InitGardenerCon(oHero, dData):
    oHero.m_GardenerCon = cl_container.gardenercon.CGardenerContainer(oHero.m_Game, oHero, dData)


def ReleaseGardenerCon(oHero):
    oHero.m_GardenerCon.Release()

g_CustomCon = {
    GARDENER_HERO: {
        'InitFunc': InitGardenerCon,
        'ReleaseFunc': ReleaseGardenerCon },
    INKMASTER_HERO: {
        'InitFunc': InitInkCon,
        'ReleaseFunc': ReleaseInkCon,
        'SaveFunc': SaveInkCon,
        'LoadFunc': LoadInkCon },
    EXECUTOR_HERO: {
        'InitFunc': InitFlawCon,
        'ReleaseFunc': ReleaseFlawCon,
        'SaveFunc': SaveFlawCon,
        'LoadFunc': LoadFlawCon },
    GAMBLER_HERO: {
        'InitFunc': InitGamblerCon,
        'ReleaseFunc': ReleaseGamblerCon,
        'SaveFunc': SaveGamblerCon,
        'LoadFunc': LoadGamblerCon } }

def InitRelicTalentCon(oHero):
    if oHero.m_RelicTalentCon:
        return None
    oHero.m_RelicTalentCon = cl_container.relictalentcon.CRelicTalentContainer(oHero)
    oHero.SetCurSeasonCon(oHero.m_RelicTalentCon, 'RT')


def InitDeviceCon(oHero):
    if oHero.m_DeviceMgr:
        return None
    oHero.m_DeviceMgr = cl_device.mobject.CDeviceMgr(oHero)
    oHero.m_DevicePerformCon = cl_container.deviceperformcon.CDevicePerformContainer(oHero)
    oHero.SetCurSeasonCon(oHero.m_DeviceMgr, 'DM')


def InitPetCon(oHero):
    if oHero.m_PetCon:
        return None
    oHero.m_PetCon = cl_container.petcon.CPetContainer(oHero)
    oHero.SetCurSeasonCon(oHero.m_PetCon, 'PC')


def InitWandCon(oHero):
    if oHero.m_WandCon:
        return None
    oHero.m_WandCon = cl_container.wandcon.CWandContainer(oHero)
    oHero.SetCurSeasonCon(oHero.m_WandCon, 'WC')


def InitDiceCon(oHero):
    if oHero.m_DiceCon:
        return None
    oHero.m_DiceCon = cl_container.dicecon.CDiceContainer(oHero)
    oHero.SetCurSeasonCon(oHero.m_DiceCon, 'DC')


def InitBackpackCon(oHero):
    if oHero.m_BackpackCon:
        return None
    oHero.m_BackpackCon = cl_container.backpackcon.CBackpackContainer(oHero)
    oHero.SetCurSeasonCon(oHero.m_BackpackCon, 'BC')


def InitS8Con(oHero):
    if oHero.m_S8Con:
        return None
    oHero.m_S8Con = cl_container.s8con.CS8Container(oHero)
    oHero.SetCurSeasonCon(oHero.m_S8Con, 'SEIGHT')

g_SeasonConInit = {
    1: InitRelicTalentCon,
    2: InitDeviceCon,
    3: InitPetCon,
    5: InitWandCon,
    6: InitDiceCon,
    7: InitBackpackCon,
    8: InitS8Con }

def InitSeasonCon(iSeason, oHero):
    if iSeason not in g_SeasonConInit:
        return None
    func = g_SeasonConInit[iSeason]
    func(oHero)


def GetTalentPerform(oHero, iPerformSID, iItem):
    return oHero.m_TalentCon.GetPerform(iPerformSID)


def GetRelicPerform(oHero, iPerformSID, iItem):
    return oHero.m_RelicCon.GetPerform(iPerformSID)


def GetBenePerform(oHero, iPerformSID, iItem):
    return oHero.m_BenedictionCon.GetPerform(iPerformSID)

g_Type2GetPerform = {
    PF_TYPE_BENEDICTION: GetBenePerform,
    PF_TYPE_RELIC: GetRelicPerform,
    PF_TYPE_TALENT: GetTalentPerform }
