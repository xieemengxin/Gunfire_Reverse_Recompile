# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betree/pfai/mobject.pyc
# RelativePath: clientlogic/cl_betree/pfai/mobject.pyc
# Source Generated with Decompyle++
# File: mobject.pyc (Python 3.6)

from cl_commondefines import MONSTER_PFAI_DODGE, PF_GROUP_CHECK_ALL, PF_GROUP_CHECK_ALLCD, PF_GROUP_CHECK_FIRST, FIGHT3_KEY_EVACT_FORBID_ELUDE, MONSTER_PFAI_CATCH
from cl_only import WeakProxy
from cl_object.logging import BehaviorLog
import cl_math

def CheckPFGroupFirst(oPerformAI, oOwner, iPerform, iFirst, dExtraInfo):
    if iFirst and iPerform in oPerformAI.m_CheckPFCanUse:
        oCheckFunc = oPerformAI.m_CheckPFCanUse[iPerform]
        if not oCheckFunc(oOwner, dExtraInfo):
            return 1
    return 0


def CheckPFGroupAll(oPerformAI, oOwner, iPerform, iFirst, dExtraInfo):
    if iPerform in oPerformAI.m_CheckPFCanUse:
        oCheckFunc = oPerformAI.m_CheckPFCanUse[iPerform]
        if not oCheckFunc(oOwner, dExtraInfo):
            return 1
    return 0


def CheckPFGroupAllCD(oPerformAI, oOwner, iPerform, iFirst, dExtraInfo):
    if oOwner.m_Perform.InColdTime(iPerform):
        return 1
    return 0

g_CheckFPGroupFunc = {
    PF_GROUP_CHECK_ALLCD: CheckPFGroupAllCD,
    PF_GROUP_CHECK_ALL: CheckPFGroupAll,
    PF_GROUP_CHECK_FIRST: CheckPFGroupFirst }

def GetCheckFPGroupFunc(idx):
    if idx in g_CheckFPGroupFunc:
        return g_CheckFPGroupFunc[idx]


class CBasePerformAI(object):
    m_SID = 200101
    m_Name = '先驱'
    m_PFGroup = { }
    m_CheckPFCanUseByDifficulty = { }
    m_ChoosePFInfo = { }
    m_CheckPFCanUse = { }
    m_UseBulletPF = ()
    m_FillBulletData = (7136, 15, 3)
    m_PFGroupCheck = { }
    
    def __init__(self, oOwner):
        self.m_Owner = oOwner.m_ID
        self.m_Game = WeakProxy(oOwner.m_Game)
        self.m_CanUsePF = { }
        self.m_CurGroup = -1
        if self.m_CheckPFCanUseByDifficulty:
            dCheckPFCanUse = { }
            dCheckPFCanUse.update(self.m_CheckPFCanUse)
            oWarMgr = self.m_Game.m_WarMgr
            tDifficulty = (oWarMgr.m_Round, oWarMgr.m_Cycle)
            if tDifficulty in self.m_CheckPFCanUseByDifficulty:
                dCheckPFCanUse.update(self.m_CheckPFCanUseByDifficulty[tDifficulty])
            self.m_CheckPFCanUse = dCheckPFCanUse

    
    def Release(self):
        self.m_Game = None
        self.m_CanUsePF = { }
        self.m_Owner = 0

    
    def ChoosePFGroup(self, oOwner, iType, dExtraInfo):
        oTarget = dExtraInfo.get('Enemy', None)
        if not oTarget:
            return { }
        if iType not in self.m_ChoosePFInfo:
            return { }
        if iType == MONSTER_PFAI_DODGE and oOwner.QueryBitAttr('LogicKey') & FIGHT3_KEY_EVACT_FORBID_ELUDE:
            iType = MONSTER_PFAI_CATCH
        iDodgeAngle = oOwner.m_Agent.GetData('DodgeAngle', 0)
        if iType == MONSTER_PFAI_DODGE and not iDodgeAngle:
            return { }
        tChoosePFInfo = ()
        fDis = cl_math.CalDistance(oOwner.GetPos(), oTarget.GetPos())
        iHPPercent = oOwner.HP() * 100 // oOwner.QueryAttr('HPMax')
        iHpArmorPercent = (oOwner.HP() + oOwner.Armor()) * 100 // (oOwner.QueryAttr('HPMax') + oOwner.QueryAttr('ArmorMax'))
        for tRestrict, tInfo in self.m_ChoosePFInfo[iType].items():
            (fMinDis, fMaxDis, iMinHpPercent, iMaxHPPercent, iMinHpArmorPercent, iMaxHpArmorPercent, iPhase) = tRestrict
            if fMinDis <= fDis and (fDis <= fMaxDis or iMinHpPercent < iHPPercent) and (iHPPercent <= iMaxHPPercent or iMinHpArmorPercent < iHpArmorPercent) and iHpArmorPercent <= iMaxHpArmorPercent and iPhase in (0, oOwner.m_Phase):
                tChoosePFInfo = tInfo
                break
        
        for dAction in tChoosePFInfo:
            dAllPFInfo = dAction.get('choose')
            if iType == MONSTER_PFAI_DODGE:
                (iMinAngle, iMaxAngle) = dAction['angle']
                if iDodgeAngle < iMinAngle or iDodgeAngle > iMaxAngle:
                    continue
                continue
            self.UpdateGroupCanUse(oOwner, dAllPFInfo, dExtraInfo)
            dFilterPFInfo = self.FilterChoosePFByLimitDistance(oOwner, dAllPFInfo, dExtraInfo)
            dChosen = self.ChooseByWeight(oOwner, dFilterPFInfo)
            if dChosen:
                return dChosen
        
        return { }

    
    def FilterChoosePFByLimitDistance(self, oOwner, dAllPFInfo, dExtraInfo):
        fChoosePFMinDis = dExtraInfo['ChoosePFMinDis'] if 'ChoosePFMinDis' in dExtraInfo else 0
        fChoosePFMaxDis = dExtraInfo['ChoosePFMaxDis'] if 'ChoosePFMaxDis' in dExtraInfo else 0
        if not fChoosePFMinDis > 0 or fChoosePFMaxDis > 0:
            return dAllPFInfo
        dFilterPFInfo = { }
        for iPFGroup, iPivot in dAllPFInfo.items():
            dPFGroup = self.m_PFGroup[iPFGroup]
            if not dPFGroup:
                continue
            tFirstPerform = dPFGroup[0] if 0 in dPFGroup else None
            if not tFirstPerform:
                continue
            iPerformSID = tFirstPerform[0]
            oPerform = oOwner.m_Perform.GetPerform(iPerformSID)
            if not oPerform:
                continue
            fPerformDistance = oPerform.GetAttDistance()
            if fChoosePFMinDis > 0 and fPerformDistance < fChoosePFMinDis:
                continue
            if fChoosePFMaxDis > 0 and fPerformDistance > fChoosePFMaxDis:
                continue
            dFilterPFInfo[iPFGroup] = iPivot
        
        return dFilterPFInfo

    
    def CheckNoUse(self, oOwner, iPerform, iFirstPF, dExtraInfo):
        if iFirstPF and 'BanFirstPF' in dExtraInfo and dExtraInfo['BanFirstPF'] == iPerform:
            return 1
        oPerform = oOwner.m_Perform.GetPerform(iPerform)
        if not oPerform:
            return 1
        if not oOwner.m_Perform.IsEnabled(iPerform):
            return 1
        if oOwner.IsForbid(oPerform.m_CheckForbid, oPerform.m_PassRule):
            return 1
        if iFirstPF and not oOwner.m_Perform.HasCover(iPerform):
            return 1
        return 0

    
    def UpdateGroupCanUse(self, oOwner, dPFGroup, dExtraInfo):
        self.m_CanUsePF = { }
        for iPFGroup in dPFGroup:
            dGroupCanUse = { }
            if iPFGroup not in self.m_PFGroup:
                BehaviorLog.Alert('技能AI%d未配置技能组%d' % (self.m_SID, iPFGroup))
                continue
            for i, (iPerform, _, _, _) in self.m_PFGroup[iPFGroup].items():
                bCanUse = True
                iFirst = i == 0
                if self.CheckNoUse(oOwner, iPerform, iFirst, dExtraInfo):
                    break
                for iCheckTpye in g_CheckFPGroupFunc:
                    if iCheckTpye & self.m_PFGroupCheck[iPFGroup] == iCheckTpye and GetCheckFPGroupFunc(iCheckTpye)(self, oOwner, iPerform, iFirst, dExtraInfo):
                        bCanUse = False
                        break
                
                if not bCanUse:
                    break
                dGroupCanUse[iPerform] = 1
            
            self.m_CanUsePF[iPFGroup] = dGroupCanUse
        

    
    def IsPFGroupCanUse(self, iPFGroup):
        if iPFGroup not in self.m_CanUsePF:
            return False
        for iPerform, _, _, _ in self.m_PFGroup[iPFGroup].values():
            if iPerform not in self.m_CanUsePF[iPFGroup]:
                return False
        
        return True

    
    def ChooseByWeight(self, oOwner, dAllPFInfo):
        iSumWeight = 0
        dChooseInfo = { }
        for iPFGroup in dAllPFInfo:
            if self.IsPFGroupCanUse(iPFGroup):
                iSumWeight += dAllPFInfo[iPFGroup]
                dChooseInfo[iPFGroup] = dAllPFInfo[iPFGroup]
        
        if iSumWeight <= 0:
            return { }
        iRandom = oOwner.m_Game.Random(iSumWeight)
        for iPFGroup, iWeight in dChooseInfo.items():
            iRandom -= iWeight
            if iRandom >= 0:
                continue
            self.m_CurGroup = iPFGroup
            return self.m_PFGroup[iPFGroup]
        
        return { }

    
    def NeedFillBullet(self, oOwner, iAttackCnt, dExtraInfo):
        if not self.m_FillBulletData:
            return 0
        (iPerform, iMinBullet, fRatio) = self.m_FillBulletData
        if iAttackCnt <= iMinBullet:
            return 0
        if self.m_Game.Random(100) > iAttackCnt * fRatio:
            return 0
        if iPerform in self.m_CheckPFCanUse:
            oCheckFunc = self.m_CheckPFCanUse[iPerform]
            if not oCheckFunc(oOwner, dExtraInfo):
                return 0
        return iPerform

    
    def GetFillBullet(self):
        if not self.m_FillBulletData:
            return 0
        return self.m_FillBulletData[0]


