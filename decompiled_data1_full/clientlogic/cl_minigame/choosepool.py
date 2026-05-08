# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_minigame/choosepool.pyc
# RelativePath: clientlogic/cl_minigame/choosepool.pyc
# Source Generated with Decompyle++
# File: choosepool.pyc (Python 3.6)

from cl_commondefines import MG_EQUIP, MG_RELIC, PLAYMODE_ROGUELIKE
from cl_cscommondef.cs_itemdef import ALL_BULLET
from cl_minigame.mg_equip import CDropEquipGameData
from cl_only import ChooseKey
import cl_item
import cl_formula

class CChoosePoolMgr(object):
    m_UseDifferBulletChoose = 1
    
    def __init__(self, oGame, iOwner):
        self.m_Game = oGame
        self.m_Owner = iOwner
        self.m_PreChoosePool = { }
        self.m_PreLoadData = {
            'Weapon': { },
            'Relic': { } }

    
    def Release(self):
        self.m_Game = None

    
    def GetOwner(self):
        return self.m_Game.GetObject(self.m_Owner)

    
    def PreChoose(self, dPassData, dExtInfo):
        self.m_PreChoosePool = { }
        oGame = self.m_Game
        oOwner = self.GetOwner()
        dPreLoadWeapon = { }
        dPreLoadRelic = { }
        self.m_PreLoadData = {
            'Weapon': dPreLoadWeapon,
            'Relic': dPreLoadRelic }
        for clsData in oGame.m_WarData.m_MiniGameData.values():
            iMiniGameSID = clsData.m_SID
            lstPass = dPassData.get(iMiniGameSID, [])
            if clsData.m_Type == MG_EQUIP:
                if 'NoWeapon' in dExtInfo:
                    self.m_PreChoosePool[iMiniGameSID] = []
                    continue
                if self.DifferBulletChoose(clsData, lstPass):
                    continue
                lstEquip = []
                clsChoose = clsData.GetChooseClass()
                iChooseLen = clsData.m_PreChooseLen - len(lstPass)
                dWeight = clsData.GetChooseWeight(oOwner)
                for _ in range(iChooseLen):
                    lstChooseEquip = clsChoose.Choose(oOwner, dWeight)
                    if lstChooseEquip:
                        lstEquip.append(lstChooseEquip)
                        for iEquip in lstChooseEquip:
                            dPreLoadWeapon[iEquip] = 1
                        
                
                lstPass.extend(lstEquip)
                self.m_PreChoosePool[iMiniGameSID] = lstPass
                continue
            if clsData.m_Type == MG_RELIC:
                self.m_PreChoosePool[iMiniGameSID] = []
        

    
    def QueryChoose(self, iMiniGameSID, dExtInfo = None):
        if iMiniGameSID not in self.m_PreChoosePool:
            return None
        if not dExtInfo:
            dExtInfo = { }
        lstPool = self.m_PreChoosePool[iMiniGameSID]
        if not lstPool:
            oGame = self.m_Game
            oOwner = oGame.GetObject(self.m_Owner)
            clsData = oGame.m_WarData.GetMiniGameData(iMiniGameSID)
            if clsData.m_Type == MG_RELIC:
                dMakeQuality = { }
                for iQlt, lstFormula in clsData.m_ChooseQuality.items():
                    dMakeQuality[iQlt] = cl_formula.GetResultByData(oOwner, lstFormula, { })
                
                if clsData.m_ChooseWeight:
                    dMakeWeight = dict(clsData.m_ChooseWeight)
                else:
                    setRelic = oOwner.m_RelicCon.GetAvailableRelic()
                    dMakeWeight = { 1: iRelic for iRelic in setRelic }
                dMakeWeightStandby = dict(clsData.m_ChooseWeightStandby)
                if 'lstWeightPop' in dExtInfo:
                    for iSID in dExtInfo['lstWeightPop']:
                        if iSID in dMakeWeight:
                            dMakeWeight.pop(iSID)
                        if iSID in dMakeWeightStandby:
                            dMakeWeightStandby.pop(iSID)
                    
                for iSID in clsData.m_FilterList:
                    if iSID in dMakeWeight:
                        dMakeWeight.pop(iSID)
                    if iSID in dMakeWeightStandby:
                        dMakeWeightStandby.pop(iSID)
                
                clsChoose = clsData.GetChooseClass()
                dExt = {
                    'Quality': dMakeQuality,
                    'WeightStandby': dMakeWeightStandby }
                dExt['LimitQuality'] = dExtInfo.get('LimitQuality', 0)
                return clsChoose.ChooseExt(oOwner, dMakeWeight, dExt)
            if clsData.m_Type == MG_EQUIP:
                dMakeWeight = clsData.GetChooseWeight(oOwner)
                if 'lstWeightPop' in dExtInfo:
                    for iSID in dExtInfo['lstWeightPop']:
                        if iSID in dMakeWeight:
                            dMakeWeight.pop(iSID)
                    
                clsChoose = clsData.GetChooseClass()
                return clsChoose.Choose(oOwner, dMakeWeight)
            dMakeWeight = dict(clsData.m_ChooseWeight)
            if 'lstWeightPop' in dExtInfo:
                for iSID in dExtInfo['lstWeightPop']:
                    if iSID in dMakeWeight:
                        dMakeWeight.pop(iSID)
                
            clsChoose = clsData.GetChooseClass()
            return clsChoose.Choose(oOwner, dMakeWeight)
        return lstPool.pop(0)

    
    def GetChoosePoolData(self):
        dData = { }
        dData.update(self.m_PreChoosePool)
        return dData

    
    def DifferBulletChoose(self, clsMiniGameData, lstPass):
        if not (self.m_UseDifferBulletChoose) or not (clsMiniGameData.m_FlagDifferBullet):
            return 0
        if not issubclass(clsMiniGameData, CDropEquipGameData):
            return 0
        oHero = self.GetOwner()
        if oHero.m_SID == 201:
            return 0
        if self.m_Game.m_WarMgr.m_PlayMode != PLAYMODE_ROGUELIKE:
            return 0
        iMiniGameSID = clsMiniGameData.m_SID
        lstAllBullet = ALL_BULLET
        if lstPass:
            lstResult = lstPass
            iLastSID = lstResult[-1][0]
            clsLastWeapon = cl_item.GetItemCls(iLastSID)
            iLastBulletType = clsLastWeapon.GetBulletType()
        else:
            lstResult = []
            iLastBulletType = 0
        iSameBulletProb = 10
        iDefaultWeight = (100 - iSameBulletProb) // (len(lstAllBullet) - 1)
        dBulletWeight = dict.fromkeys(lstAllBullet, iDefaultWeight)
        dBulletCount = dict.fromkeys(lstAllBullet, 0)
        oGame = self.m_Game
        lstNew = []
        iSize = clsMiniGameData.m_PreChooseLen * 2
        for _ in range(iSize - len(lstResult)):
            if iLastBulletType:
                dBulletWeight[iLastBulletType] = iSameBulletProb
            iTargetBulletType = ChooseKey(oGame, dBulletWeight)
            if iLastBulletType:
                dBulletWeight[iLastBulletType] = iDefaultWeight
            lstNew.append(iTargetBulletType)
            dBulletCount[iTargetBulletType] += 1
            iLastBulletType = iTargetBulletType
        
        dBullet = { }
        for iBullet, iNum in dBulletCount.items():
            dBullet[iBullet] = self.ChooseWeaponByBullet(clsMiniGameData, iBullet, iNum)
        
        for i, iBullet in enumerate(lstNew):
            lstNew[i] = dBullet[iBullet].pop(0)
        
        lstResult.extend(lstNew)
        self.m_PreChoosePool[iMiniGameSID] = lstResult
        for i in range(clsMiniGameData.m_PreChooseLen):
            iWeapon = lstResult[i][0]
            self.m_PreLoadData['Weapon'][iWeapon] = 1
        
        return 1

    
    def ChooseWeaponByBullet(self, clsMiniGameData, iTargetBulletType, iNum):
        oHero = self.GetOwner()
        dWeight = clsMiniGameData.GetChooseWeightByBullet(oHero, iTargetBulletType)
        lstWeapon = []
        clsChoose = clsMiniGameData.GetChooseClass()
        for _ in range(iNum):
            lstChooseEquip = clsChoose.Choose(oHero, dWeight)
            if lstChooseEquip:
                lstWeapon.append(lstChooseEquip)
        
        return lstWeapon


