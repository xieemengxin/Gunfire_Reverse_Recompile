# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_monster/monsterattradjust.pyc
# RelativePath: clientlogic/cl_monster/monsterattradjust.pyc
# Source Generated with Decompyle++
# File: monsterattradjust.pyc (Python 3.6)

from cl_only import CELL_SPACESIZE
from cl_netattr import GS2CPropChange
from cl_commondefines import WARRIOR_ELITE, LEVEL_TYPE_HIDE, LEVEL_TYPE_FIGHT, LEVEL_TYPE_BOSS, WARRIOR_BOSS, MAX_LAYER
from cl_platformdata import GetMonsterAttrClassify
from cl_object.logging import OtherLog
import cl_formula

class CBaseAttrAdjust(object):
    m_AttrClassifyDefault = 0
    m_RelateAttr = {
        'HPMax': 'HP',
        'ShieldMax': 'Shield',
        'ArmorMax': 'Armor' }
    
    def __init__(self):
        self.m_LevelID = 0
        self.m_AttrInfo = { }

    
    def SetLevelID(self, iLevelID):
        self.m_LevelID = iLevelID

    
    def DoneAllAttrAdjust(self, obj):
        if not self.m_LevelID:
            return None
        oWarMgr = obj.m_Game.m_WarMgr
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.GetLevelNode(self.m_LevelID)
        if not oLevelNode:
            return None
        iLevelType = oLevelNode.m_LevelType
        iLayerNum = oLevelNode.m_LayerNum
        dLevelCtrlConf = oLevelCtrl.m_LevelCtrlConf
        if obj.m_FightType & WARRIOR_ELITE == WARRIOR_ELITE and not obj.Query('Demon'):
            dAttAdjust = dLevelCtrlConf[iLayerNum].get('EliteAttAdjust', { })
        else:
            dAttAdjust = dLevelCtrlConf[iLayerNum].get('MonsterAttAdjust', { })
        iCycle = oWarMgr.m_Cycle
        if iCycle in dAttAdjust:
            dAttAdjust = dAttAdjust[iCycle]
        else:
            dAttAdjust = dAttAdjust.get(0, { })
        if iLevelType in (LEVEL_TYPE_FIGHT, LEVEL_TYPE_HIDE):
            lstAttrGroup = dAttAdjust.get(iLevelType, { }).get(oLevelNode.m_LevelNum, [])
        else:
            lstAttrGroup = dAttAdjust.get(iLevelType, [])
        if iLevelType == LEVEL_TYPE_BOSS:
            lstAttrGroup = RidingAloneAttrAdjust(oWarMgr, iLayerNum, lstAttrGroup)
        if iLevelType != LEVEL_TYPE_BOSS:
            oSurvivorElement = oWarMgr.GetComponent('SurvivorElement')
            if oSurvivorElement:
                lstAttrGroup = oSurvivorElement.GetMonsterAttrAdjust(obj.m_FightType)
        oRoundElement = oWarMgr.GetComponent('RoundElement')
        dRoundAttrInfo = oRoundElement.m_MonsterAdjust if oRoundElement else { }
        dCycleAttrInfo = oRoundElement.m_CycleMonsterAdjust if oRoundElement else { }
        dRecvDamRatioInfo = oRoundElement.m_MonsterRecvDamAdjust if oRoundElement else { }
        dEndlessAttrInfo = oWarMgr.GetEndlessBossAttrAdjust() if obj.m_FightType & WARRIOR_BOSS == WARRIOR_BOSS else { }
        dAttrInfo = { }
        dAttrClassify = GetMonsterAttrClassify()
        iAttrClassify = dAttrClassify[obj.m_DataSID] if obj.m_DataSID in dAttrClassify else 0
        dClassifyAttrInfo = { }
        dDefaultAttr = dCycleAttrInfo.setdefault(self.m_AttrClassifyDefault, { })
        dClassifyAttrInfo.update(dDefaultAttr)
        if iAttrClassify in dCycleAttrInfo:
            dClassifyAttrInfo.update(dCycleAttrInfo[iAttrClassify])
        for sAttr, oMul, oAdd in lstAttrGroup:
            dAttr = dAttrInfo.setdefault(sAttr, { })
            dAttr['Mul'] = oMul
            dAttr['Add'] = oAdd
        
        for sAttr, iFactor in dRoundAttrInfo.items():
            dAttr = dAttrInfo.setdefault(sAttr, { })
            dAttr['Factor'] = iFactor
        
        for sAttr, iAdd in dClassifyAttrInfo.items():
            dAttr = dAttrInfo.setdefault(sAttr, { })
            iFactor = dAttr['Factor'] if 'Factor' in dAttr else 0
            iAdd = cl_formula.GetFormulaResult(obj, iAdd)
            dAttr['Factor'] = iFactor + iAdd
        
        for sAttr, iAdd in dEndlessAttrInfo.items():
            dAttr = dAttrInfo.setdefault(sAttr, { })
            iFactor = dAttr['Factor'] if 'Factor' in dAttr else 0
            iAdd = cl_formula.GetFormulaResult(obj, iAdd)
            dAttr['Factor'] = iFactor + iAdd
        
        for sAttr, dAdjustInfo in dAttrInfo.items():
            oMul = dAdjustInfo['Mul'] if 'Mul' in dAdjustInfo else 0
            oAdd = dAdjustInfo['Add'] if 'Add' in dAdjustInfo else 0
            oFactor = dAdjustInfo['Factor'] if 'Factor' in dAdjustInfo else 0
            self.AddAttr(obj, sAttr, oMul, oAdd, oFactor)
        
        self.ComAttAdjust(obj, dAttrInfo)
        self.ComRecvDamAdjust(obj, iAttrClassify, dRecvDamRatioInfo, iLayerNum)

    
    def ComAttAdjust(self, obj, dAttrInfo):
        if 'Att' not in dAttrInfo:
            return None
        dAdjustInfo = dAttrInfo['Att']
        oMul = dAdjustInfo['Mul'] if 'Mul' in dAdjustInfo else 0
        oAdd = dAdjustInfo['Add'] if 'Add' in dAdjustInfo else 0
        oFactor = dAdjustInfo['Factor'] if 'Factor' in dAdjustInfo else 0
        self.AddAttr(obj, 'ComAtt', oMul, oAdd, oFactor)

    
    def ComRecvDamAdjust(self, obj, iAttrClassify, dRecvDamRatioInfo, iLayerNum):
        if iAttrClassify not in dRecvDamRatioInfo:
            return None
        iLayerNum = min(MAX_LAYER, iLayerNum)
        dRecvDamRatio = dRecvDamRatioInfo[iAttrClassify]
        if iLayerNum not in dRecvDamRatio:
            return None
        iMul = dRecvDamRatio[iLayerNum]
        obj.ChangeBaseRecvDamRatio('ComRecvDamAdjust', 0, iMul)

    
    def ClearAllAttrAdjust(self, obj):
        if not self.m_LevelID:
            return None
        lstAttr = list(self.m_AttrInfo)
        for sAttr in lstAttr:
            self.DelAttr(obj, sAttr)
        

    
    def AddAttr(self, obj, sAttr, oMul, oAdd, oFactor):
        if sAttr in self.m_AttrInfo:
            return None
        iMul = cl_formula.GetFormulaResult(obj, oMul)
        iAdd = cl_formula.GetFormulaResult(obj, oAdd)
        iFactor = cl_formula.GetFormulaResult(obj, oFactor)
        iOldBase = obj.m_PrivateAttr[sAttr].m_BaseValue
        if sAttr == 'MoveSpeed':
            iNewBase = (iOldBase + iAdd) * (iMul + 10000) * 0.0001
            iNewBase = iNewBase * (10000 + iFactor) * 0.0001
            iNewBase = iNewBase * CELL_SPACESIZE
        else:
            iNewBase = (iOldBase + iAdd) * (iMul + 10000) // 10000
            iNewBase = iNewBase * (10000 + iFactor) // 10000
        obj.m_PrivateAttr[sAttr].ChangeBase(obj, iNewBase)
        self.m_AttrInfo[sAttr] = iOldBase
        self.UpdateBaseAttr(obj, sAttr)

    
    def DelAttr(self, obj, sAttr):
        if sAttr not in self.m_AttrInfo:
            return None
        iNewBase = self.m_AttrInfo[sAttr]
        obj.m_PrivateAttr[sAttr].ChangeBase(obj, iNewBase)
        self.m_AttrInfo.pop(sAttr)

    
    def UpdateBaseAttr(self, obj, sAttr):
        if sAttr in self.m_RelateAttr:
            sDestAttr = self.m_RelateAttr[sAttr]
            if hasattr(obj, 'm_%s' % sDestAttr):
                iVal = obj.QueryAttr(sAttr)
                setattr(obj, 'm_%s' % sDestAttr, iVal)
                GS2CPropChange(obj, sDestAttr)



def RidingAloneAttrAdjust(oWarMgr, iLayerNum, lstAttrGroup):
    oRidingAloneElement = oWarMgr.GetComponent('RidingAloneElement')
    if not oRidingAloneElement:
        return lstAttrGroup
    if iLayerNum not in oRidingAloneElement.m_AttrAdjust:
        return lstAttrGroup
    lstNewAttrGroup = []
    dAttrAdjust = oRidingAloneElement.m_AttrAdjust[iLayerNum]
    for sAttr, oMul, oAdd in lstAttrGroup:
        if sAttr in dAttrAdjust:
            lstNewAttrGroup.append((sAttr, dAttrAdjust[sAttr], 0))
            continue
        lstNewAttrGroup.append((sAttr, oMul, oAdd))
    
    return lstNewAttrGroup

