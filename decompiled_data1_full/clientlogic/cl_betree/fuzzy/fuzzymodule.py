# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betree/fuzzy/fuzzymodule.pyc
# RelativePath: clientlogic/cl_betree/fuzzy/fuzzymodule.pyc
# Source Generated with Decompyle++
# File: fuzzymodule.pyc (Python 3.6)

from cl_only import GAME_FRAME
from cl_commondefines import FIGHT_LOGIC_CHARGE, GAMETYPE_LIMITLIVE, FIGHT_LOGIC_OVERALLGUERRILLA, FIGHT_LOGIC_OVERALLCHARGE
import cl_math
from .mobject import CFuzzy
from .term import CFzAND
from .defines import SHAPE_LEFTSHOULDER, SHAPE_RIGHTSHOULDER, SHAPE_TRIANGULAR

class CFuzzyAttack(CFuzzy):
    
    def InitializeFuzzyModule(self):
        (oVeryDesirable, oDesirable, oUndesirable) = self.InitDesirability()
        oFzVarDistance = self.CreateFLV('DisToTarget')
        oDisClose = oFzVarDistance.AddSet('Target_Close', SHAPE_LEFTSHOULDER, 0, 25, 150)
        oDisMedium = oFzVarDistance.AddSet('Target_Medium', SHAPE_TRIANGULAR, 25, 150, 300)
        oDisFar = oFzVarDistance.AddSet('Target_Far', SHAPE_RIGHTSHOULDER, 150, 300, 1000)
        oFzVarAmmo = self.CreateFLV('AmmoStatus')
        oAmmoLoads = oFzVarAmmo.AddSet('Ammo_Loads', SHAPE_RIGHTSHOULDER, 10, 30, 100)
        oAmmoOkay = oFzVarAmmo.AddSet('Ammo_Okay', SHAPE_TRIANGULAR, 0, 10, 30)
        oAmmoLow = oFzVarAmmo.AddSet('Ammo_Low', SHAPE_TRIANGULAR, 0, 0, 10)
        self.AddRule(CFzAND(oDisClose, oAmmoLoads), oUndesirable)
        self.AddRule(CFzAND(oDisClose, oAmmoOkay), oUndesirable)
        self.AddRule(CFzAND(oDisClose, oAmmoLow), oUndesirable)
        self.AddRule(CFzAND(oDisMedium, oAmmoLoads), oVeryDesirable)
        self.AddRule(CFzAND(oDisMedium, oAmmoOkay), oVeryDesirable)
        self.AddRule(CFzAND(oDisMedium, oAmmoLow), oDesirable)
        self.AddRule(CFzAND(oDisFar, oAmmoLoads), oDesirable)
        self.AddRule(CFzAND(oDisFar, oAmmoOkay), oUndesirable)
        self.AddRule(CFzAND(oDisFar, oAmmoLow), oUndesirable)

    
    def GetDesirability(self, oAgent):
        fDistToTarget = 200
        iAmmo = 8
        self.Fuzzify('DisToTarget', fDistToTarget)
        self.Fuzzify('AmmoStatus', iAmmo)
        fDesirabilityScore = self.DeFuzzify('Desirability', iMethod = 1)
        return fDesirabilityScore



class CFarCharge(CFuzzy):
    m_Name = '远程追击'
    
    def InitializeFuzzyModule(self):
        (oVeryDesirable, oDesirable, oUndesirable) = self.InitDesirability()
        oFzChargeTargetCnt = self.CreateFLV('ChargeTarget')
        oTarLess = oFzChargeTargetCnt.AddSet('ChargeTarget_Less', SHAPE_LEFTSHOULDER, 0, 1, 2)
        oTarMedium = oFzChargeTargetCnt.AddSet('ChargeTarget_Medium', SHAPE_TRIANGULAR, 1, 2, 3)
        oTarMuch = oFzChargeTargetCnt.AddSet('ChargeTarget_Much', SHAPE_RIGHTSHOULDER, 2, 3, 10)
        oHp = self.CreateFLV('HP')
        oHpHigh = oHp.AddSet('HP_High', SHAPE_RIGHTSHOULDER, 50, 70, 100)
        oHpLow = oHp.AddSet('HP_Low', SHAPE_LEFTSHOULDER, 0, 50, 70)
        self.AddRule(CFzAND(oTarMuch, oHpHigh), oUndesirable)
        self.AddRule(CFzAND(oTarMuch, oHpLow), oUndesirable)
        self.AddRule(CFzAND(oTarMedium, oHpHigh), oVeryDesirable)
        self.AddRule(CFzAND(oTarMedium, oHpLow), oDesirable)
        self.AddRule(CFzAND(oTarLess, oHpHigh), oVeryDesirable)
        self.AddRule(CFzAND(oTarLess, oHpLow), oVeryDesirable)

    
    def GetDesirability(self, oAgent):
        oOwner = oAgent.m_OwnerObj
        oTarget = oAgent.GetLockEnemy()
        oSceneData = oAgent.m_SceneData
        if oTarget:
            iSightNum = oSceneData.CheckSightNum(oTarget.m_ID, 3, GAME_FRAME)
        else:
            iSightNum = 0
        self.Fuzzify('ChargeTarget', min(oSceneData.GetMonsterFightLogicNum(FIGHT_LOGIC_CHARGE, oOwner.m_ID) + iSightNum, 10))
        iHPPercent = oOwner.HP() * 100 // oOwner.QueryAttr('HPMax')
        self.Fuzzify('HP', iHPPercent)
        fDesirabilityScore = self.DeFuzzify('Desirability', iMethod = 1)
        return fDesirabilityScore



class CFarGuerrilla(CFuzzy):
    m_Name = '移动追击'
    
    def InitializeFuzzyModule(self):
        (oVeryDesirable, oDesirable, oUndesirable) = self.InitDesirability()
        oFzSeePassFrame = self.CreateFLV('SeePass')
        iSee1 = 4 * GAME_FRAME
        iSee2 = 7 * GAME_FRAME
        iSee3 = 9 * GAME_FRAME
        oSeePassLess = oFzSeePassFrame.AddSet('SeePass_Less', SHAPE_LEFTSHOULDER, 0, iSee1, iSee2)
        oSeePassMedium = oFzSeePassFrame.AddSet('SeePass_Medium', SHAPE_TRIANGULAR, iSee1, iSee2, iSee3)
        oSeePassMuch = oFzSeePassFrame.AddSet('SeePass_Much', SHAPE_RIGHTSHOULDER, iSee2, iSee3, 10 * GAME_FRAME)
        self.AddRule(oSeePassLess, oUndesirable)
        self.AddRule(oSeePassMedium, oDesirable)
        self.AddRule(oSeePassMuch, oVeryDesirable)

    
    def GetDesirability(self, oAgent):
        iPastFrame = oAgent.GetLockEnemyPastSightFrame()
        self.Fuzzify('SeePass', min(iPastFrame, 10 * GAME_FRAME))
        return self.DeFuzzify('Desirability', iMethod = 1)



class CFarSquareGuerrilla(CFuzzy):
    m_Name = '四方位游击'
    
    def InitializeFuzzyModule(self):
        (oVeryDesirable, oDesirable, oUndesirable) = self.InitDesirability()
        oFzSeePassFrame = self.CreateFLV('SeePass')
        iSee1 = 3 * GAME_FRAME
        iSee2 = 6 * GAME_FRAME
        iSee3 = 8 * GAME_FRAME
        oSeePassLess = oFzSeePassFrame.AddSet('SeePass_Less', SHAPE_LEFTSHOULDER, 0, iSee1, iSee2)
        oSeePassMedium = oFzSeePassFrame.AddSet('SeePass_Medium', SHAPE_TRIANGULAR, iSee1, iSee2, iSee3)
        oSeePassMuch = oFzSeePassFrame.AddSet('SeePass_Much', SHAPE_RIGHTSHOULDER, iSee2, iSee3, 10 * GAME_FRAME)
        self.AddRule(oSeePassLess, oVeryDesirable)
        self.AddRule(oSeePassMedium, oDesirable)
        self.AddRule(oSeePassMuch, oUndesirable)

    
    def GetDesirability(self, oAgent):
        iPastFrame = oAgent.GetLockEnemyPastSightFrame()
        self.Fuzzify('SeePass', min(iPastFrame, 10 * GAME_FRAME))
        return self.DeFuzzify('Desirability', iMethod = 1)



class CFarHide(CFuzzy):
    m_Name = '掩体'
    
    def InitializeFuzzyModule(self):
        (oVeryDesirable, oDesirable, oUndesirable) = self.InitDesirability()
        oHp = self.CreateFLV('HP')
        oHpHigh = oHp.AddSet('HP_High', SHAPE_RIGHTSHOULDER, 50, 70, 100)
        oHpLow = oHp.AddSet('HP_Low', SHAPE_LEFTSHOULDER, 0, 50, 70)
        oFzSeePassFrame = self.CreateFLV('SeePass')
        iSee1 = 3 * GAME_FRAME
        iSee2 = 6 * GAME_FRAME
        iSee3 = 8 * GAME_FRAME
        oSeePassLess = oFzSeePassFrame.AddSet('SeePass_Less', SHAPE_LEFTSHOULDER, 0, iSee1, iSee2)
        oSeePassMedium = oFzSeePassFrame.AddSet('SeePass_Medium', SHAPE_TRIANGULAR, iSee1, iSee2, iSee3)
        oSeePassMuch = oFzSeePassFrame.AddSet('SeePass_Much', SHAPE_RIGHTSHOULDER, iSee2, iSee3, 10 * GAME_FRAME)
        oFzSetHideDis = self.CreateFLV('HideDis')
        fDis1 = 4
        fDis2 = 7
        fDis3 = 10
        oDisNear = oFzSetHideDis.AddSet('HideDis_Near', SHAPE_LEFTSHOULDER, 0, fDis1, fDis2)
        oDisMed = oFzSetHideDis.AddSet('HideDis_Med', SHAPE_TRIANGULAR, fDis1, fDis2, fDis3)
        oDisFar = oFzSetHideDis.AddSet('HideDis_Far', SHAPE_RIGHTSHOULDER, fDis2, fDis3, 100)
        self.AddRule(oSeePassMuch, oUndesirable)
        self.AddRule(oDisFar, oUndesirable)
        self.AddRule(CFzAND(oSeePassLess, oDisNear), oVeryDesirable)
        self.AddRule(CFzAND(oSeePassLess, oHpHigh, oDisMed), oDesirable)
        self.AddRule(CFzAND(oSeePassLess, oHpLow, oDisMed), oVeryDesirable)
        self.AddRule(CFzAND(oSeePassMedium, oHpHigh, oDisNear), oDesirable)
        self.AddRule(CFzAND(oSeePassLess, oHpLow, oDisNear), oVeryDesirable)
        self.AddRule(CFzAND(oSeePassMedium, oDisMed), oDesirable)

    
    def GetDesirability(self, oAgent):
        oOwner = oAgent.m_OwnerObj
        iHPPercent = oOwner.HP() * 100 // oOwner.QueryAttr('HPMax')
        self.Fuzzify('HP', iHPPercent)
        iPastFrame = oAgent.GetLockEnemyPastSightFrame()
        self.Fuzzify('SeePass', min(iPastFrame, 10 * GAME_FRAME))
        fHideDis = oAgent.GetNearestHidePosDis(0, oAgent)
        self.Fuzzify('HideDis', min(fHideDis, 100))
        return self.DeFuzzify('Desirability', iMethod = 1)



class CGrenadeHide(CFuzzy):
    m_Name = '投雷掩体'
    
    def InitializeFuzzyModule(self):
        (oVeryDesirable, oDesirable, oUndesirable) = self.InitDesirability()
        oHp = self.CreateFLV('HP')
        oHpHigh = oHp.AddSet('HP_High', SHAPE_RIGHTSHOULDER, 40, 80, 100)
        oHpLow = oHp.AddSet('HP_Low', SHAPE_LEFTSHOULDER, 0, 40, 80)
        oFzSetHideDis = self.CreateFLV('HideDis')
        fDis1 = 4
        fDis2 = 7
        fDis3 = 10
        oDisNear = oFzSetHideDis.AddSet('HideDis_Near', SHAPE_LEFTSHOULDER, 0, fDis1, fDis2)
        oDisMed = oFzSetHideDis.AddSet('HideDis_Med', SHAPE_TRIANGULAR, fDis1, fDis2, fDis3)
        oDisFar = oFzSetHideDis.AddSet('HideDis_Far', SHAPE_RIGHTSHOULDER, fDis2, fDis3, 100)
        self.AddRule(CFzAND(oHpHigh, oDisFar), oUndesirable)
        self.AddRule(CFzAND(oHpHigh, oDisMed), oUndesirable)
        self.AddRule(CFzAND(oHpHigh, oDisNear), oDesirable)
        self.AddRule(CFzAND(oHpLow, oDisFar), oDesirable)
        self.AddRule(CFzAND(oHpLow, oDisMed), oVeryDesirable)
        self.AddRule(CFzAND(oHpLow, oDisNear), oVeryDesirable)

    
    def GetDesirability(self, oAgent):
        oOwner = oAgent.m_OwnerObj
        iHPPercent = oOwner.HP() * 100 // oOwner.QueryAttr('HPMax')
        self.Fuzzify('HP', iHPPercent)
        fHideDis = oAgent.GetNearestHidePosDis(0, oAgent)
        self.Fuzzify('HideDis', min(fHideDis, 100))
        return self.DeFuzzify('Desirability', iMethod = 1)



class CGrenadeGuerrilla(CFuzzy):
    m_Name = '投雷游击'
    
    def InitializeFuzzyModule(self):
        (oVeryDesirable, oDesirable, oUndesirable) = self.InitDesirability()
        oHp = self.CreateFLV('HP')
        oHpHigh = oHp.AddSet('HP_High', SHAPE_RIGHTSHOULDER, 40, 80, 100)
        oHpLow = oHp.AddSet('HP_Low', SHAPE_LEFTSHOULDER, 0, 40, 80)
        oFzVarDistance = self.CreateFLV('DisToTarget')
        oDisClose = oFzVarDistance.AddSet('Target_Close', SHAPE_LEFTSHOULDER, 0, 5, 10)
        oDisMedium = oFzVarDistance.AddSet('Target_Medium', SHAPE_TRIANGULAR, 5, 10, 15)
        oDisFar = oFzVarDistance.AddSet('Target_Far', SHAPE_RIGHTSHOULDER, 10, 15, 100)
        self.AddRule(oDisClose, oVeryDesirable)
        self.AddRule(CFzAND(oDisMedium, oHpHigh), oDesirable)
        self.AddRule(CFzAND(oDisMedium, oHpLow), oVeryDesirable)
        self.AddRule(CFzAND(oDisFar, oHpHigh), oUndesirable)
        self.AddRule(CFzAND(oDisFar, oHpLow), oDesirable)

    
    def GetDesirability(self, oAgent):
        oOwner = oAgent.m_OwnerObj
        oTarget = oAgent.GetLockEnemy()
        fDistToTarget = cl_math.CalDistance(oOwner.GetPos(), oTarget.GetPos()) if oTarget else 100
        iHPPercent = oOwner.HP() * 100 // oOwner.QueryAttr('HPMax')
        self.Fuzzify('DisToTarget', fDistToTarget)
        self.Fuzzify('HP', iHPPercent)
        fDesirabilityScore = self.DeFuzzify('Desirability', iMethod = 1)
        return fDesirabilityScore



class COverallCharge(CFuzzy):
    m_Name = '全局追击'
    m_MaxCF = 20
    
    def InitializeFuzzyModule(self):
        (oVeryDesirable, oDesirable, oUndesirable) = self.InitDesirability()
        oHp = self.CreateFLV('HP')
        oHpLow = oHp.AddSet('HP_Low', SHAPE_LEFTSHOULDER, 0, 40, 80)
        oHpHigh = oHp.AddSet('HP_High', SHAPE_RIGHTSHOULDER, 40, 80, 100)
        oOverallChargeCF = self.CreateFLV('OverallChargeCF')
        oLow = oOverallChargeCF.AddSet('OverallChargeCF_Low', SHAPE_LEFTSHOULDER, 0, 0.5, 1.5)
        oHigh = oOverallChargeCF.AddSet('OverallChargeCF_High', SHAPE_RIGHTSHOULDER, 0.5, 1.5, self.m_MaxCF)
        oFzVarDistance = self.CreateFLV('DisToTarget')
        oDisClose = oFzVarDistance.AddSet('Target_Close', SHAPE_LEFTSHOULDER, 0, 5, 10)
        oDisMedium = oFzVarDistance.AddSet('Target_Medium', SHAPE_TRIANGULAR, 5, 10, 30)
        oDisFar = oFzVarDistance.AddSet('Target_Far', SHAPE_RIGHTSHOULDER, 10, 30, 100)
        self.AddRule(oHigh, oUndesirable)
        self.AddRule(CFzAND(oDisMedium, oLow), oUndesirable)
        self.AddRule(CFzAND(oDisFar, oLow), oUndesirable)
        self.AddRule(CFzAND(oHpLow, oLow, oDisClose), oDesirable)
        self.AddRule(CFzAND(oHpHigh, oLow, oDisClose), oVeryDesirable)

    
    def GetDesirability(self, oAgent):
        oOwner = oAgent.m_OwnerObj
        fDistToTarget = oAgent.GetCache('DisToTarget', -1)
        if fDistToTarget == -1:
            oTarget = oAgent.GetLockEnemy()
            fDistToTarget = cl_math.CalDistance(oOwner.GetPos(), oTarget.GetPos()) if oTarget else 100
            oAgent.SetCache('DisToTarget', fDistToTarget)
        self.Fuzzify('DisToTarget', fDistToTarget)
        oSceneData = oAgent.m_SceneData
        fOverallChargeCF = oAgent.GetCache('OverAllChargeCF', -1)
        if fOverallChargeCF == -1:
            fOverallChargeCF = oSceneData.GetCombatForceByFightLogic(FIGHT_LOGIC_OVERALLCHARGE)
            oAgent.SetCache('OverAllChargeCF', fOverallChargeCF)
        fOverallGuerrillaCF = oAgent.GetCache('OverallGuerrillaCF', -1)
        if fOverallGuerrillaCF == -1:
            fOverallGuerrillaCF = oSceneData.GetCombatForceByFightLogic(FIGHT_LOGIC_OVERALLGUERRILLA)
            oAgent.SetCache('OverallGuerrillaCF', fOverallGuerrillaCF)
        if oOwner.m_CombatForce + fOverallChargeCF > fOverallGuerrillaCF:
            return 0
        if oOwner.m_CombatForce + fOverallChargeCF + fOverallGuerrillaCF > 6:
            return 0
        iHPPercent = oOwner.HP() * 100 // oOwner.QueryAttr('HPMax')
        self.Fuzzify('HP', iHPPercent)
        fOverAllChargeCF = min(fOverallChargeCF, self.m_MaxCF)
        self.Fuzzify('OverallChargeCF', fOverAllChargeCF)
        fDesirabilityScore = self.DeFuzzify('Desirability', iMethod = 1)
        return fDesirabilityScore



class COverallGuerrilla(CFuzzy):
    m_Name = '全局游击'
    m_MaxCF = 20
    
    def InitializeFuzzyModule(self):
        (oVeryDesirable, oDesirable, oUndesirable) = self.InitDesirability()
        oHp = self.CreateFLV('HP')
        oHpLow = oHp.AddSet('HP_Low', SHAPE_LEFTSHOULDER, 0, 40, 80)
        oHpHigh = oHp.AddSet('HP_High', SHAPE_RIGHTSHOULDER, 40, 80, 100)
        oFzVarDistance = self.CreateFLV('DisToTarget')
        oDisClose = oFzVarDistance.AddSet('Target_Close', SHAPE_LEFTSHOULDER, 0, 5, 10)
        oDisMedium = oFzVarDistance.AddSet('Target_Medium', SHAPE_TRIANGULAR, 5, 10, 30)
        oDisFar = oFzVarDistance.AddSet('Target_Far', SHAPE_RIGHTSHOULDER, 10, 30, 100)
        oOverallChargeCF = self.CreateFLV('OverallChargeCF')
        oLow = oOverallChargeCF.AddSet('OverallChargeCF_Low', SHAPE_LEFTSHOULDER, 0, 0.5, 1.5)
        oHigh = oOverallChargeCF.AddSet('OverallChargeCF_High', SHAPE_RIGHTSHOULDER, 0.5, 1.5, self.m_MaxCF)
        self.AddRule(oLow, oUndesirable)
        self.AddRule(CFzAND(oHigh, oDisClose), oUndesirable)
        self.AddRule(CFzAND(oHigh, oDisMedium), oVeryDesirable)
        self.AddRule(CFzAND(oHigh, oDisFar, oHpLow), oDesirable)
        self.AddRule(CFzAND(oHigh, oDisFar, oHpHigh), oVeryDesirable)

    
    def GetDesirability(self, oAgent):
        oOwner = oAgent.m_OwnerObj
        fOverallChargeCF = oAgent.GetCache('OverallChargeCF', -1)
        if fOverallChargeCF == -1:
            oSceneData = oAgent.m_SceneData
            fOverallChargeCF = oSceneData.GetCombatForceByFightLogic(FIGHT_LOGIC_OVERALLCHARGE)
            oAgent.SetCache('OverallChargeCF', fOverallChargeCF)
        fOverallGuerrillaCF = oAgent.GetCache('OverallGuerrillaCF', -1)
        if fOverallGuerrillaCF == -1:
            oSceneData = oAgent.m_SceneData
            fOverallGuerrillaCF = oSceneData.GetCombatForceByFightLogic(FIGHT_LOGIC_OVERALLGUERRILLA)
            oAgent.SetCache('OverallGuerrillaCF', fOverallGuerrillaCF)
        if oOwner.m_CombatForce + fOverallChargeCF + fOverallGuerrillaCF > 6:
            return 0
        fDistToTarget = oAgent.GetCache('DisToTarget', -1)
        if fDistToTarget == -1:
            oTarget = oAgent.GetLockEnemy()
            fDistToTarget = cl_math.CalDistance(oOwner.GetPos(), oTarget.GetPos()) if oTarget else 100
            oAgent.SetCache('DisToTarget', fDistToTarget)
        self.Fuzzify('DisToTarget', fDistToTarget)
        iHPPercent = oOwner.HP() * 100 // oOwner.QueryAttr('HPMax')
        self.Fuzzify('HP', iHPPercent)
        fOverAllChargeCF = min(fOverallChargeCF, self.m_MaxCF)
        self.Fuzzify('OverallChargeCF', fOverAllChargeCF)
        fDesirabilityScore = self.DeFuzzify('Desirability', iMethod = 1)
        return fDesirabilityScore



class COverallAwait(CFuzzy):
    m_Name = '全局待机'
    m_MaxCF = 20
    
    def InitializeFuzzyModule(self):
        (oVeryDesirable, oDesirable, oUndesirable) = self.InitDesirability()
        oHp = self.CreateFLV('HP')
        oHpLow = oHp.AddSet('HP_Low', SHAPE_LEFTSHOULDER, 0, 40, 80)
        oHpHigh = oHp.AddSet('HP_High', SHAPE_RIGHTSHOULDER, 40, 80, 100)
        oFzVarDistance = self.CreateFLV('DisToTarget')
        oDisClose = oFzVarDistance.AddSet('Target_Close', SHAPE_LEFTSHOULDER, 0, 5, 10)
        oDisMedium = oFzVarDistance.AddSet('Target_Medium', SHAPE_TRIANGULAR, 5, 10, 30)
        oDisFar = oFzVarDistance.AddSet('Target_Far', SHAPE_RIGHTSHOULDER, 10, 30, 100)
        oOverallChargeCF = self.CreateFLV('OverallChargeCF')
        oLow = oOverallChargeCF.AddSet('OverallChargeCF_Low', SHAPE_LEFTSHOULDER, 0, 0.5, 1.5)
        oHigh = oOverallChargeCF.AddSet('OverallChargeCF_High', SHAPE_RIGHTSHOULDER, 0.5, 1.5, self.m_MaxCF)
        self.AddRule(oLow, oUndesirable)
        self.AddRule(CFzAND(oHigh, oDisClose), oUndesirable)
        self.AddRule(CFzAND(oHigh, oDisFar), oVeryDesirable)
        self.AddRule(CFzAND(oHigh, oDisMedium, oHpLow), oDesirable)
        self.AddRule(CFzAND(oHigh, oDisMedium, oHpHigh), oUndesirable)

    
    def GetDesirability(self, oAgent):
        oOwner = oAgent.m_OwnerObj
        if oOwner.m_LineIdx:
            iType = oAgent.GetData('LevelType')
            if iType is None:
                oLevelCtrl = oOwner.m_Game.m_WarMgr.GetComponent('LevelCtrl')
                iLevel = oOwner.m_LineIdx[0]
                iType = oLevelCtrl.GetLevelTypeInFight(iLevel)
                oAgent.SetData('LevelType', iType)
            if iType == GAMETYPE_LIMITLIVE:
                return 0
        fDistToTarget = oAgent.GetCache('DisToTarget', -1)
        if fDistToTarget == -1:
            oTarget = oAgent.GetLockEnemy()
            fDistToTarget = cl_math.CalDistance(oOwner.GetPos(), oTarget.GetPos()) if oTarget else 100
            oAgent.SetCache('DisToTarget', fDistToTarget)
        self.Fuzzify('DisToTarget', fDistToTarget)
        fOverallChargeCF = oAgent.GetCache('OverallChargeCF', -1)
        if fOverallChargeCF == -1:
            oSceneData = oAgent.m_SceneData
            fOverallChargeCF = oSceneData.GetCombatForceByFightLogic(FIGHT_LOGIC_OVERALLCHARGE)
            oAgent.SetCache('OverallChargeCF', fOverallChargeCF)
        iHPPercent = oOwner.HP() * 100 // oOwner.QueryAttr('HPMax')
        self.Fuzzify('HP', iHPPercent)
        fOverAllChargeCF = min(fOverallChargeCF, self.m_MaxCF)
        self.Fuzzify('OverallChargeCF', fOverAllChargeCF)
        fDesirabilityScore = self.DeFuzzify('Desirability', iMethod = 1)
        return fDesirabilityScore


