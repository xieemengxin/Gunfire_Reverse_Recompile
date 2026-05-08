# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/daytrialelement.pyc
# RelativePath: clientlogic/cl_warmgr/daytrialelement.pyc
# Source Generated with Decompyle++
# File: daytrialelement.pyc (Python 3.6)

from cl_warmgr.mobject import CBaseElement
from cl_cscommondef.cs_other import DAY_TRIAL
from cl_object.logging import WarobjLog
from cl_commondefines import NWARRIOR_DROP_GSCASH, WARRIOR_BOSS, BOSS_DONOT_COUNT, VIRTUAL_ITEM_DROP, NWARRIOR_DROP_GSCASH
from cl_platformdata import GetWeaponClassTag
from cl_only import SendAlert
import cl_msgcenter
import cl_playway
import cl_snetwar
import cl_putdata
import cl_item.load
import cl_perform.load
import cl_platformdata
import cl_reward

class CDayTrialElement(CBaseElement):
    
    def __init__(self, oGame, nid, oData):
        super().__init__(oGame, nid, oData)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_PlayWayInfo = { }
        self.m_PlayWay = []
        self.m_ItemInfo = { }
        self.m_ThemeItemList = []
        self.m_Theme = 0
        self.m_GoodItem = 0
        self.m_BadItem = 0
        self.m_GradeItem = 0
        self.m_DayGSCashRewardInfo = { }
        self.m_GlobalItem = oData.m_Config['m_GlobalItem']
        self.m_DayReward = oData.m_Config['m_DayReward']
        self.m_WeaponPut = set()

    
    def IsValidData(self):
        if DAY_TRIAL not in self.m_WarMgr.m_ExtraInfo or not self.m_WarMgr.m_ExtraInfo[DAY_TRIAL]:
            return False
        dData = self.m_WarMgr.m_ExtraInfo[DAY_TRIAL]
        if 'Layer' not in dData or not dData['Layer']:
            return False
        if 'Theme' not in dData or not dData['Theme']:
            return False
        if 'GoodItem' not in dData or not dData['GoodItem']:
            return False
        if 'BadItem' not in dData or not dData['BadItem']:
            return False
        return True

    
    def Init(self):
        if not self.IsValidData():
            WarobjLog.Alert(f'''每日试炼数据不合法 {self.m_WarMgr.m_ExtraInfo}''')
            return None
        self.m_PlayWayInfo = self.m_WarMgr.m_ExtraInfo[DAY_TRIAL]
        self.InitWeaponLimit()
        self.m_Game.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.OnPlayerMapLoadOK, 'DayTrialElement')
        self.m_Game.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.OnAddPlayer, 'DayTrialFrop')
        self.m_Game.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_DIE, self.OnBossDie, 'DayTrialBossDie')

    
    def InitAfter(self):
        if not self.m_PlayWayInfo:
            return None
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.AddAttentionFunc(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_WARMGR_LEVELCTRLINIT, self.Trigger, 'DayTrialElement')
        self.AddPlayWay()

    
    def InitWeaponLimit(self):
        clsTheme = cl_platformdata.GetDayTrialTheme(self.m_PlayWayInfo['Theme'])
        if not clsTheme:
            return None
        dWeaponClassTag = GetWeaponClassTag()
        setPutWeapon = set()
        setUnPutWeapon = set()
        lstPutRelicLimit = clsTheme.m_PutWeaponTag
        lstUnPutRelicLimit = clsTheme.m_UnPutWeaponTag
        for iTag in lstPutRelicLimit:
            if iTag not in dWeaponClassTag:
                continue
            setPutWeapon.update(dWeaponClassTag[iTag])
        
        for iTag in lstUnPutRelicLimit:
            if iTag not in dWeaponClassTag:
                continue
            setUnPutWeapon.update(dWeaponClassTag[iTag])
        
        setAllPutWeapon = set(cl_putdata.GetAllPutWeapon())
        if setPutWeapon:
            setAllPutWeapon = setAllPutWeapon & setPutWeapon
        if setUnPutWeapon:
            setAllPutWeapon = setAllPutWeapon - setUnPutWeapon
        self.m_WeaponPut = setAllPutWeapon

    
    def Release(self):
        self.m_ItemInfo = { }
        self.m_Game.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, 'DayTrialElement')
        self.m_Game.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYER, 'DayTrialFrop')
        self.m_Game.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_DIE, 'DayTrialBossDie')
        for oPlayWay in self.m_PlayWay:
            oPlayWay.Release()
        
        self.m_PlayWay = []
        self.m_WarMgr = None
        super().Release()

    
    def GetWarReportInfo(self):
        if not self.m_PlayWayInfo:
            return { }
        dInfo = {
            'Theme': self.m_PlayWayInfo['Theme'],
            'Good': self.m_PlayWayInfo['GoodItem'],
            'Bad': self.m_PlayWayInfo['BadItem'] }
        return dInfo

    
    def Trigger(self, oTarget, oLevelCtrl, dMsgInfo):
        iLayer = self.m_PlayWayInfo['Layer']
        if iLayer not in oLevelCtrl.m_LevelCtrlConf:
            WarobjLog.Alert(f'''每日试炼幕数 {iLayer} 不存在''')
            return None
        dData = { }
        dData[iLayer] = oLevelCtrl.m_LevelCtrlConf[iLayer]
        oLevelCtrl.m_LevelCtrlConf = dData
        oLevelCtrl.m_LayerNum = iLayer

    
    def AddPlayWay(self):
        iGood = self.m_PlayWayInfo['GoodItem']
        iBad = self.m_PlayWayInfo['BadItem']
        iTheme = self.m_PlayWayInfo['Theme']
        lstItemCls = []
        for iGlobalItem in self.m_GlobalItem:
            clsData = cl_platformdata.GetDayTrialItem(iGlobalItem)
            if not clsData:
                WarobjLog.Alert(f'''每日试炼全局条目 {iGlobalItem} 不存在''')
                continue
            lstItemCls.append(clsData)
        
        clsTheme = cl_platformdata.GetDayTrialTheme(iTheme)
        if not clsTheme:
            WarobjLog.Alert(f'''每日试炼主题 {iTheme} 不存在''')
        else:
            for iThemItem in clsTheme.m_ThemeItem:
                clsData = cl_platformdata.GetDayTrialItem(iThemItem)
                if not clsData:
                    WarobjLog.Alert(f'''每日试炼主题条目 {iThemItem} 不存在''')
                    continue
                self.m_ThemeItemList.append(iThemItem)
                lstItemCls.append(clsData)
            
            self.m_Theme = iTheme
            clsGradeItem = self.GetGradeItem(clsTheme)
            if clsGradeItem:
                lstItemCls.append(clsGradeItem)
        clsData = cl_platformdata.GetDayTrialItem(iGood)
        if not clsData:
            WarobjLog.Alert(f'''每日试炼增益条目 {iGood} 不存在''')
        else:
            lstItemCls.append(clsData)
            self.m_GoodItem = iGood
        clsData = cl_platformdata.GetDayTrialItem(iBad)
        if not clsData:
            WarobjLog.Alert(f'''每日试炼减益条目 {iBad} 不存在''')
        else:
            lstItemCls.append(clsData)
            self.m_BadItem = iBad
        self.m_ItemInfo = { }
        for clsItem in lstItemCls:
            self.m_ItemInfo[clsItem.m_SID] = []
            for iType, tParam in clsItem.m_Rule:
                oPlayWay = cl_playway.NewDayTrial(self, self.m_Game, clsItem.m_SID, iType, tParam)
                if not oPlayWay:
                    WarobjLog.Alert(f'''每日试炼规则 {iType} 不存在''')
                    continue
                self.m_PlayWay.append(oPlayWay)
                self.m_ItemInfo[clsItem.m_SID].append(oPlayWay)
            
        

    
    def OnPlayerMapLoadOK(self, oListener, oHero, dInfo):
        cl_snetwar.GS2CDayTrialInfo(oHero, self.m_PlayWayInfo['Theme'], self.m_ThemeItemList, self.m_GoodItem, self.m_BadItem)
        lstInfo = []
        for iItem, lstRule in self.m_ItemInfo.items():
            for oRule in lstRule:
                lstArgs = oRule.GetClientData(oHero)
                if lstArgs is not None:
                    lstInfo.append((iItem, lstArgs))
                    break
            
        
        cl_snetwar.GS2CDayTrialItemInfo(oHero, lstInfo)

    
    def OnAddPlayer(self, oDayTrial, oWarMgr, dInfo):
        oHero = dInfo['oCtrlHero']
        self.SetDayTrialGSCashInfo(oHero)
        dPlayerInfo = dInfo['CreateInfo']
        iTheme = oDayTrial.m_PlayWayInfo['Theme']
        clsTheme = cl_platformdata.GetDayTrialTheme(iTheme)
        if not clsTheme:
            return None
        setUnlockWeapon = self.m_WeaponPut
        setValidRelic = set(cl_putdata.GetAllPutRelic()) - set(cl_perform.load.GetGameExcludeRelic(oWarMgr.GetPlayType())) - set(clsTheme.m_RelicLimit)
        if not clsTheme.m_AllWeaponUnlock:
            setUnlockWeapon = (set(cl_item.load.GetUnlockWeapon()) | set(dPlayerInfo['Weapon']['Unlock'])) & setUnlockWeapon
        if not clsTheme.m_AllRelicUnlock:
            setValidRelic = (set(cl_perform.load.GetUnlockRelic()) | set(dPlayerInfo['Relic']['Unlock'])) & setValidRelic
        dIllus = {
            'Weapon': setUnlockWeapon,
            'Relic': setValidRelic }
        dIllusInfo = oHero.Query('Illus', { })
        dIllusInfo.update(dIllus)
        oHero.Set('Illus', dIllusInfo)

    
    def OnBossDie(self, oListener, oMonster, dInfo):
        if 'VID' not in dInfo:
            return None
        if oMonster.m_FightType & WARRIOR_BOSS != WARRIOR_BOSS or oMonster.m_FightType in BOSS_DONOT_COUNT:
            return None
        lstHero = self.m_Game.m_WarMgr.GetLiveHero()
        for iHero in lstHero:
            oHero = self.m_Game.GetObject(iHero)
            if not oHero or oHero.m_ID not in self.m_DayGSCashRewardInfo:
                continue
            oHero.Set('TodayDayTrailStartCnt', self.m_PlayWayInfo['StartCnt'])
            (iPer, iNum) = self.m_DayGSCashRewardInfo.pop(iHero)
            vPos = cl_reward.GetDropBasePos(oMonster)
            lstDropInfo = [
                {
                    'GSCash': iNum }]
            dReward = {
                'item': VIRTUAL_ITEM_DROP,
                'info': {
                    'DropType': NWARRIOR_DROP_GSCASH,
                    'DropInfo': lstDropInfo,
                    'DropPos': vPos } }
            for _ in range(iPer):
                cl_reward.RewardItem(oHero.m_Game, oHero, [
                    dReward], 'daytrialreward', {
                    'Player': iHero,
                    'Abandoner': oMonster.m_ID })
            
        

    
    def SetDayTrialGSCashInfo(self, oHero):
        if not self.m_PlayWayInfo.get('StartCnt', 0):
            SendAlert('err', '每日试炼StartCnt数据异常：%s' % self.m_PlayWayInfo)
            return None
        (iFirstRewardNum, iCommonRewardNum, iPerNum) = self.m_DayReward
        iDayTrialStartCnt = oHero.Query('DayTrialStartCnt', 0)
        iRewardNum = 0
        if iDayTrialStartCnt == self.m_PlayWayInfo['StartCnt']:
            iRewardNum = iCommonRewardNum
        else:
            if 0 <= iDayTrialStartCnt and iDayTrialStartCnt < self.m_PlayWayInfo['StartCnt']:
                iRewardNum = iFirstRewardNum
        if not iRewardNum:
            return None
        iPer = iRewardNum // iPerNum
        if iPer > 100:
            SendAlert('err', '玩家%s 每日试炼奖励精魄数异常：%d' % (oHero.m_PlayerID, iPer))
            return None
        self.m_DayGSCashRewardInfo[oHero.m_ID] = (iPer, iPerNum)

    
    def GetGradeItem(self, clsTheme):
        if 'GradeItem' not in self.m_WarMgr.m_ExtraInfo[DAY_TRIAL]:
            return None
        iClientGradeItem = self.m_WarMgr.m_ExtraInfo[DAY_TRIAL]['GradeItem']
        tGradeItem = clsTheme.m_GradeItem
        if not tGradeItem:
            WarobjLog.Alert(f'''每日试炼{clsTheme.m_SID}主题不存在等级条目''')
            return None
        (_, iItem) = tGradeItem
        if iClientGradeItem != iItem:
            WarobjLog.Alert(f'''每日试炼等级条目错误,{iClientGradeItem} {iItem} 不一致''')
            return None
        clsData = cl_platformdata.GetDayTrialItem(iItem)
        if not clsData:
            WarobjLog.Alert(f'''每日试炼等级条目 {iItem} 不存在''')
            return None
        return clsData

    
    def GetReportData(self):
        return (self.m_Theme, self.m_GoodItem, self.m_BadItem)



def GetComponentClass(oMgrManager):
    return CDayTrialElement

