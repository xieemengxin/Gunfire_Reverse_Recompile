# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/monsterspelement.pyc
# RelativePath: clientlogic/cl_warmgr/monsterspelement.pyc
# Source Generated with Decompyle++
# File: monsterspelement.pyc (Python 3.6)

from cl_commondefines import LEVEL_TYPE_HALL, LEVEL_TYPE_HIDE, LEVEL_TYPE_BOSS, WARRIOR_ELITE, MONSTER_CLASSIFY_PETROCHEMICAL, MONSTER_CLASSIFY_BOXMONSTER, MONSTER_CLASSIFY_MASK, MONSTER_TYPE_MASK, WARRIOR_MONSTER, MODE_REAL_ENDLESS
from cl_only import ChooseKey, SendAlert
from cl_warmgr.mobject import CBaseElement
import cl_msgcenter
import cl_formula
import cl_perform.load
import cl_perform.monsteraf
import cl_only

class CMonsterSuperElement(CBaseElement):
    m_FullExcludeMonsterAf = (6107, 6108)
    m_ExcludeClassify = (MONSTER_CLASSIFY_PETROCHEMICAL, MONSTER_CLASSIFY_BOXMONSTER)
    m_ExcludeType = (WARRIOR_ELITE,)
    
    def __init__(self, oGame, nid, oData):
        super(CMonsterSuperElement, self).__init__(oGame, nid, oData)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_SuperConfig = oData.m_SuperConfig
        self.m_AffixConfig = oData.m_AffixConfig
        self.m_MonsterInfo = { }
        self.m_LevelSuperNum = { }
        self.m_RoomSuperNum = { }
        self.m_RoomSuperAf = { }
        self.m_LevelSuperAf2Monster = { }
        self.m_LevelDisableAutoSuper = { }
        self.m_MonsterAfLib = cl_only.DeepCopy(cl_perform.load.GetMonsterAfLib())
        self.m_ExChooseRatio = { }
        self.m_ExSuperNum = { }
        self.m_LockLevel = set()
        self.m_AfAdjust = cl_perform.monsteraf.GetMonsterAfAdjust(self.m_WarMgr.m_Round, self.m_WarMgr.m_Cycle, self.m_WarMgr.m_SeasonNum)

    
    def InitAfter(self):
        oWarMgr = self.m_WarMgr
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.AddAttentionFunc(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_CREATEMONSTER, self.OnCreateMonster, 'MonsterSuper.CreateMonster')
        self.m_Game.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_DIE, self.OnDie, 'MonsterSuper.Die')
        self.m_Game.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_MONSTER_SUPER, self.OnMonsterSuper, 'MonsterSuper.MonsterSuper')

    
    def Release(self):
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneAttention(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_CREATEMONSTER, 'MonsterSuper.CreateMonster')
        self.m_Game.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_DIE, 'MonsterSuper.Die')
        self.m_Game.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_MONSTER_SUPER, 'MonsterSuper.MonsterSuper')
        self.m_WarMgr = None
        super(CMonsterSuperElement, self).Release()

    
    def GetMonsterSuperLevel(self, iLevelType):
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            return 0
        iDefaultLevel = oLevelCtrl.m_LayerNum
        dModeConfig = self.GetMonsterConfigByMode(self.m_SuperConfig)
        dLayerConfig = dModeConfig.get(iLevelType)
        if not dLayerConfig:
            return iDefaultLevel
        iCurLayer = self.m_WarMgr.GetBaseLayer(iDefaultLevel)
        dLayer = dLayerConfig.get(iCurLayer)
        if not dLayer:
            return iDefaultLevel
        iLevel = dLayer['SuperLevel']
        if not iLevel:
            return iDefaultLevel
        return iLevel

    
    def GetMonsterConfigByMode(self, dConfig):
        sGameMode = 'Default'
        if self.m_WarMgr.IsEndless():
            sGameMode = MODE_REAL_ENDLESS
        dModeConfig = dConfig.get(sGameMode, { })
        return dModeConfig

    
    def CalSuperLimit(self, tLimit):
        iLimit = cl_formula.GetFormulaResult(self, tLimit)
        return iLimit

    
    def IsCanMonsterSuper(self, tChooseRatio, oMonster):
        for iClassify in self.m_ExcludeClassify:
            if oMonster.m_FightType & MONSTER_CLASSIFY_MASK == iClassify:
                return False
        
        for iType in self.m_ExcludeType:
            if oMonster.m_FightType & MONSTER_TYPE_MASK == iType:
                return False
        
        iRatio = cl_formula.GetFormulaResult(self, tChooseRatio)
        for iExRatio in self.m_ExChooseRatio.values():
            iRatio += iExRatio
        
        if iRatio <= 0:
            return False
        iRand = self.m_Game.Random(100)
        return iRand < iRatio

    
    def CloseLevelAutoSuper(self, iLevel):
        self.m_LevelDisableAutoSuper[iLevel] = 1

    
    def LockLevel(self, iLevel):
        self.m_LockLevel.add(iLevel)

    
    def UnlockLevel(self, iLevel):
        self.m_LockLevel.remove(iLevel)

    
    def OnCreateMonster(self, oSelf, oLevelCtrl, dInfo):
        (iLevel, _, _) = dInfo['LineIdx']
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        iLevelType = oLevelNode.m_LevelType
        iCycle = self.m_WarMgr.m_Cycle
        if iLevelType == LEVEL_TYPE_HALL or iLevelType == LEVEL_TYPE_BOSS:
            return None
        if iLevelType == LEVEL_TYPE_HIDE or iCycle == 0 or iLevel in self.m_LevelDisableAutoSuper:
            self.SuperMonsterOffRule(oLevelCtrl, dInfo, iLevelType)
        elif iLevel not in self.m_LockLevel:
            self.SuperMonsterByRule(oLevelCtrl, dInfo, iLevelType)

    
    def AdjustMonsterAf(self, oMonster, dAf):
        if oMonster.m_FightType in self.m_AfAdjust:
            for iAf, iAdjust in self.m_AfAdjust[oMonster.m_FightType].items():
                if iAf in dAf:
                    dAf[iAf] += iAdjust
                    if dAf[iAf] < 0:
                        dAf[iAf] = 0
                        continue
                if iAdjust > 0:
                    dAf[iAf] = iAdjust
            

    
    def RandomMonsterSuperInfo(self, oMonster, lstChoosed, iLevelType):
        iRound = self.m_WarMgr.m_Round
        iCycle = self.m_WarMgr.m_Cycle
        dMonsterAfLib = self.m_MonsterAfLib.get(iRound + iCycle, { })
        if not dMonsterAfLib:
            SendAlert('err', '周目:%d 轮回:%d 未配置怪物词缀抽取' % (iRound, iCycle))
            return (0, 0)
        iLevel = self.GetMonsterLevelID(oMonster)
        dLevelAf2Monster = self.m_LevelSuperAf2Monster[iLevel] if iLevel in self.m_LevelSuperAf2Monster else { }
        dModeConfig = self.GetMonsterConfigByMode(self.m_AffixConfig)
        dExcConfig = dModeConfig.get(iLevelType, { })
        dExc = dExcConfig.get((iRound, iCycle), { })
        dAfAll = { }
        iFightType = oMonster.m_FightType
        for iAf, (iWeight, iMaxCnt) in dMonsterAfLib.items():
            if iAf in dExc:
                iExcFightType = dExc[iAf]
                if not iExcFightType:
                    continue
                if iFightType & iExcFightType == iExcFightType:
                    continue
                continue
            if iMaxCnt and iAf in dLevelAf2Monster and len(dLevelAf2Monster[iAf]) >= iMaxCnt:
                continue
            dAfAll[iAf] = iWeight
        
        if lstChoosed:
            if len(lstChoosed) >= len(dAfAll):
                lstExc = self.m_FullExcludeMonsterAf
            else:
                lstExc = lstChoosed
            dAfAll = dict(((k, v) for k, v in dAfAll.items() if k not in lstExc))
        for iBanPF in oMonster.m_BanPF:
            dAfAll.pop(iBanPF, 0)
        
        self.AdjustMonsterAf(oMonster, dAfAll)
        iAfPF = ChooseKey(self.m_Game, dAfAll)
        if not iAfPF:
            iAfPF = 0
        iPlusPF = 0
        lstAttrPlus = oMonster.m_AttrPlusPF
        if lstAttrPlus:
            iRand = self.m_Game.Random(len(lstAttrPlus))
            iPlusPF = lstAttrPlus[iRand]
        return (iAfPF, iPlusPF)

    
    def SuperMonsterByRule(self, oLevelCtrl, dInfo, iLevelType):
        iCurLayer = self.m_WarMgr.GetBaseLayer(oLevelCtrl.m_LayerNum)
        dModeConfig = self.GetMonsterConfigByMode(self.m_SuperConfig)
        dLayerConfig = dModeConfig.get(iLevelType, { })
        dLayer = dLayerConfig.get(iCurLayer)
        if not dLayer:
            return None
        iMonster = dInfo['Monster']
        oMonster = self.m_Game.GetObject(iMonster)
        if not oMonster:
            return None
        iCurLevel = oLevelCtrl.m_LevelNum
        dLevelLimit = dLayer['LevelConfig'].get(iCurLevel)
        if not dLevelLimit:
            return None
        iLevelLimit = self.CalSuperLimit(dLevelLimit['LevelLimit'])
        iLevelLive = self.CalSuperLimit(dLevelLimit['LevelLive'])
        for _, iExLimit in self.m_ExSuperNum.items():
            iLevelLimit += iExLimit * 3
            iLevelLive += iExLimit
        
        iLevel = iLevelType * 100 + iCurLayer * 10 + iCurLevel
        dLevelCnt = self.m_LevelSuperNum.setdefault(iLevel, {
            'Cnt': 0,
            'Live': 0 })
        if dLevelCnt['Cnt'] >= iLevelLimit or dLevelCnt['Live'] >= iLevelLive:
            return None
        iRoomIdx = dInfo['LineIdx'][1]
        iRoom = iLevel * 1000 + iRoomIdx
        dRoomCnt = self.m_RoomSuperNum.setdefault(iRoom, {
            'Cnt': 0,
            'Live': 0 })
        iRoomLimit = self.CalSuperLimit(dLevelLimit['RoomLimit'])
        iRoomLive = self.CalSuperLimit(dLevelLimit['RoomLive'])
        for _, iExLimit in self.m_ExSuperNum.items():
            iRoomLimit += iExLimit
            iRoomLive += iExLimit
        
        if len(oLevelCtrl.m_CurNode.m_RoomList) > 1:
            if dRoomCnt['Cnt'] >= iRoomLimit or dRoomCnt['Live'] >= iRoomLive:
                return None
        iSuperLv = self.GetMonsterSuperLevel(iLevelType)
        if iSuperLv <= 0:
            return None
        if not self.IsCanMonsterSuper(dLayer['ChooseRatio'], oMonster):
            return None
        dAfChoosed = self.m_RoomSuperAf.setdefault(iRoom, { })
        (iAfPF, iPlusPF) = self.RandomMonsterSuperInfo(oMonster, tuple(dAfChoosed.values()), iLevelType)
        if not iAfPF or not iPlusPF:
            SendAlert('err', '怪物%d强化有误，af:%s plus:%s' % (oMonster.m_SID, iAfPF, iPlusPF))
            return None
        dLevelCnt['Cnt'] += 1
        dLevelCnt['Live'] += 1
        dRoomCnt['Cnt'] += 1
        dRoomCnt['Live'] += 1
        dAfChoosed[iMonster] = iAfPF
        self.m_MonsterInfo[iMonster] = (iLevel, iRoom)
        oMonster.MonsterSuper(iSuperLv, iPlusPF, iAfPF)

    
    def SuperMonsterOffRule(self, oLevelCtrl, dInfo, iLevelType):
        if 'SuperInfo' not in dInfo:
            return None
        iMonster = dInfo['Monster']
        oMonster = self.m_Game.GetObject(iMonster)
        if not oMonster:
            return None
        iSuperLv = self.GetMonsterSuperLevel(iLevelType)
        if iSuperLv <= 0:
            return None
        iAfPF = dInfo['SuperInfo']['affix']
        iPlusPF = dInfo['SuperInfo']['plusatt']
        oMonster.MonsterSuper(iSuperLv, iPlusPF, iAfPF)

    
    def OnDie(self, oSelf, obj, dInfo):
        if not obj.m_FightType & WARRIOR_MONSTER:
            return None
        iMonster = obj.m_ID
        tSuperInfo = obj.Query('MonsterSuper', None)
        if tSuperInfo:
            iAfPF = tSuperInfo[1]
            iLevel = self.GetMonsterLevelID(obj)
            if iLevel in self.m_LevelSuperAf2Monster and iAfPF in self.m_LevelSuperAf2Monster[iLevel]:
                self.m_LevelSuperAf2Monster[iLevel][iAfPF].pop(iMonster, 0)
        if iMonster not in self.m_MonsterInfo:
            return None
        (iLevel, iRoom) = self.m_MonsterInfo.pop(iMonster)
        self.m_LevelSuperNum[iLevel]['Live'] -= 1
        self.m_RoomSuperNum[iRoom]['Live'] -= 1
        self.m_RoomSuperAf[iRoom].pop(iMonster, None)

    
    def GetMonsterLevelID(self, oMonster):
        if oMonster.m_LineIdx:
            return oMonster.m_LineIdx[0]
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        return oLevelCtrl.m_CurNode.m_Level

    
    def OnMonsterSuper(self, oSelf, oMonster, dInfo):
        tSuperInfo = oMonster.Query('MonsterSuper', None)
        if not tSuperInfo:
            return None
        iLevel = self.GetMonsterLevelID(oMonster)
        dLevelAf2Monster = self.m_LevelSuperAf2Monster.setdefault(iLevel, { })
        iAfPF = tSuperInfo[1]
        if iAfPF not in dLevelAf2Monster:
            dLevelAf2Monster[iAfPF] = { }
        dLevelAf2Monster[iAfPF][oMonster.m_ID] = 1



def GetComponentClass(oMgrManager):
    return CMonsterSuperElement

