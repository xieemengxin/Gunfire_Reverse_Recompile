# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_formula.pyc
# RelativePath: clientlogic/cl_formula.pyc
# Source Generated with Decompyle++
# File: cl_formula.pyc (Python 3.6)

# 去除伤害上限

from cl_commondefines import g_ElementDefAttrKey, DAM_TYPE_NORMAL, RELIC_TYPE_CURSE, BASEATTR_CLIENT, SCENEOBJ_TYPE, WARRIOR_MONSTER, WARRIOR_HERO, WARRIOR_SUMMON, DAM_TYPE_TRUE, OBJ_VICTIM, DAM_TYPE_PERSISTENCE, DAM_TYPE_PERFORM, DAM_TYPE_ENEMY, DAM_TYPE_FRIEND, DAM_USE_ALL, DAM_TYPE_WEAPON, DAM_USE_HP, DAM_USE_ARMOR, DAM_USE_SHIELD, WARRIOR_SERVANT, WARRIOR_DEVICE, WARRIOR_PET, LEVEL_TYPE_FIGHT, LEVEL_TYPE_BOSS, DAM_TYPE_WEAKNESS, WARRIOR_PET_HEROSIDE
from cl_only import Frame2Time
from cl_object.logging import SkillLog
import math
import re
import cl_math
import cl_perform
import cl_action
import cl_item.defines as itemdef
import cllib.lib_flag

def InternalCalDamage(func):
    
    def _InternalCalDamage(*args):
        (_, dDamage) = args
        r = func(*args)
        lstMainDam = dDamage['MainDam']
        lstFlowDam = dDamage['FlowDam']
        dFactor = dDamage['DamFactor']
        iLuckyHit = dDamage['LuckyHit'] if 'LuckyHit' in dDamage else 0
        for _, oReason in lstMainDam:
            iDamType = oReason.Query('DamType')
            for iType, dEachFactor in dFactor.items():
                if not dEachFactor:
                    continue
                iAdd = 10000
                iMul = 10000
                for _Add, _Mul, iMask in dEachFactor.values():
                    if iMask and iDamType & iMask == 0:
                        continue
                    iAdd += _Add
                    if _Mul < -10000:
                        _Mul = -10000
                    iMul = iMul * (10000 + _Mul) // 10000
                
                if iAdd < 0:
                    iAdd = 0
                oReason.SetInfo('DamFactor%s' % iType, (iAdd, iMul))
            
            oReason.SetInfo('LuckyHit', iLuckyHit)
        
        for _, oReason in lstFlowDam:
            iDamType = oReason.Query('DamType')
            for dEachFactor in dFactor.values():
                if not dEachFactor:
                    continue
                iAdd = 10000
                iMul = 10000
                for _Add, _Mul, iMask in dEachFactor.values():
                    if iMask and iDamType & iMask == 0:
                        continue
                    iAdd += _Add
                    if _Mul < -10000:
                        _Mul = -10000
                    iMul = iMul * (10000 + _Mul) // 10000
                
                if iAdd < 0:
                    iAdd = 0
                oReason.SetInfo('ShowFactorEff', (iAdd, iMul))
            
            oReason.SetInfo('LuckyHit', iLuckyHit)
        
        return r

    if cllib.lib_flag.g_IsAuthorityRun:
        return _InternalCalDamage
    return func

g_LimitInfo = { }

def CheckPerformBackHit(oVictim, oSkill):
    vStart = oSkill.m_Base['vStart']
    vEnd = oSkill.m_Base['vEnd']
    dx = vEnd[0] - vStart[0]
    dz = vEnd[2] - vStart[2]
    (fx, _, fz) = oVictim.GetFacing()
    iRes = fx * dx + fz * dz
    if iRes > 0:
        return 1
    return 0

g_HpTypeIndex = {
    'Shield': 0,
    'Armor': 1,
    'HP': 2 }
g_DamTypeSequence = ((0, 'Shield', DAM_USE_SHIELD), (1, 'Armor', DAM_USE_ARMOR), (2, 'HP', DAM_USE_HP))
g_CureTypeSequence = ((2, 'HP', DAM_USE_HP), (0, 'Shield', DAM_USE_SHIELD), (1, 'Armor', DAM_USE_ARMOR))
# g_MaxSingleDamage = 999999999
# g_MaxPerformDamage = 0xB2D05E00

def GetDamWeaponAttrExtEffect(oSkill, iDam, dArgs, dCopyWeaponArgs):
    for sAttr, iRatio in dArgs.items():
        iValue = oSkill.m_Cache[sAttr]
        iDam += iValue * iRatio // 100
    
    if dCopyWeaponArgs:
        iCopyAdd = 10000
        iCopyMul = 10000
        for _Add, _Mul in dCopyWeaponArgs.values():
            iCopyAdd += _Add
            if _Mul <= -10000:
                iCopyMul = 0
                break
            iCopyMul = iCopyMul * (10000 + _Mul) // 10000
        
        iDam = iDam * iCopyAdd * iCopyMul // 10000 // 10000
    return iDam


def CalWeaponDamage(oVictim, oSkill, dWeaponArgs, dArgs, dCopyWeaponArgs):
    iAtt = GetDamWeaponAttrExtEffect(oSkill, 0, dWeaponArgs, dCopyWeaponArgs)
    iMaxReducePercent = oSkill.m_Cache['MaxReducePercent'] if 'MaxReducePercent' in oSkill.m_Cache else 0
    if iMaxReducePercent > 0:
        dFlyCartoon = oSkill.GetCurStackFlyCartoon()
        if dFlyCartoon:
            fFlyMaxDis = dFlyCartoon['Distance']
            fFlyDis = min(fFlyMaxDis, cl_math.CalDistance3D(dFlyCartoon['Start'], dFlyCartoon['CurPos']))
            fReduceDis = oSkill.m_Cache['ReduceDis']
            if fFlyDis > fReduceDis:
                fMaxReducePercent = oSkill.m_Cache['MaxReducePercent']
                fReducePercent = fMaxReducePercent * (fFlyDis - fReduceDis) / (fFlyMaxDis - fReduceDis)
                iAtt = int(iAtt - iAtt * fReducePercent / 100)
    iAttack = oSkill.m_Base['AID']
    iHitArea = oSkill.m_Update['CurHitArea']
    iDamPartType = oVictim.GetDamamgePartType(iHitArea, iAttack)
    iElementType = oSkill.m_Cache['ElementType'] if 'ElementType' in oSkill.m_Cache else DAM_TYPE_NORMAL
    lstExtraFactorElement = oSkill.m_Custom['ExtraFactorElement'] if 'ExtraFactorElement' in oSkill.m_Custom else []
    iDamType = iElementType | DAM_TYPE_WEAPON | DAM_USE_ALL | iDamPartType
    if oSkill.m_Cache['Side'] == oVictim.m_Side:
        iDamType |= DAM_TYPE_FRIEND
    else:
        iDamType |= DAM_TYPE_ENEMY
    if dArgs:
        if 'IgnoreShield' in dArgs:
            iDamType &= ~DAM_USE_SHIELD
        if 'ForbidModifyType' in dArgs:
            oSkill.m_Base['RS'] = oSkill.m_Base['RS'].ExtInfo({
                'ForbidModifyType': dArgs['ForbidModifyType'] })
        if 'IgnoreWeakness' in dArgs:
            iDamType &= ~DAM_TYPE_WEAKNESS
    dExtInfo = {
        'DamType': iDamType,
        'ExtraFactorElement': lstExtraFactorElement,
        'InitDam': iAtt }
    dCurCartoon = oSkill.GetCurCartoon()
    if dCurCartoon and 'CopyTimes' in dCurCartoon:
        dExtInfo['CopyTimes'] = dCurCartoon['CopyTimes']
        iTotalMergeTimes = dCurCartoon['CopyTimes'] + 1
        dExtInfo['ExInfo'] = 1 | iTotalMergeTimes << 1
    oReason = oSkill.m_Base['RS'].ExtInfo(dExtInfo)
    return [
        iAtt,
        oReason]


def CalPerformDamage(oVictim, oSkill, iDam, iElementType, dArgs):
    iDamType = iElementType | DAM_TYPE_PERFORM | DAM_USE_ALL
    if dArgs:
        if 'IgnoreShield' in dArgs:
            iDamType &= ~DAM_USE_SHIELD
        if 'IgnoreArmor' in dArgs:
            iDamType &= ~DAM_USE_ARMOR
        if 'AddElementType' in dArgs:
            iDamType |= dArgs['AddElementType']
    if oSkill.m_Cache['Side'] == oVictim.m_Side:
        iDamType |= DAM_TYPE_FRIEND
    else:
        iDamType |= DAM_TYPE_ENEMY
    if 'CopyTimes' in oSkill.m_Collect:
        iCopyTimes = oSkill.m_Collect['CopyTimes']
        oReason = oSkill.m_Base['RS'].ExtInfo({
            'DamType': iDamType,
            'InitDam': iDam,
            'CopyTimes': iCopyTimes,
            'OtherInfo': dArgs })
    else:
        oReason = oSkill.m_Base['RS'].ExtInfo({
            'DamType': iDamType,
            'InitDam': iDam,
            'OtherInfo': dArgs })
    return [
        iDam,
        oReason]


def CalStateDamage(oAttack, oVictim, oState, iBaseDam, dState):
    iDamType = DAM_TYPE_PERSISTENCE | DAM_USE_ALL
    if oAttack.m_Side == oVictim.m_Side:
        iDamType |= DAM_TYPE_FRIEND
    else:
        iDamType |= DAM_TYPE_ENEMY
    oReason = dState['RS'].ExtInfo({
        'DamType': iDamType })
    dState['MainDam'] = [
        [
            iBaseDam,
            oReason]]


def CalDamage(oVictim, dDamage):
    lstMainDam = dDamage['MainDam']
    lstFlowDam = dDamage['FlowDam']
    dFactor = dDamage['DamFactor']
    for iMask, sDefKey in g_ElementDefAttrKey.items():
        iValue = oVictim.QueryAttr(sDefKey)
        if not iValue:
            continue
        dFactor[OBJ_VICTIM][sDefKey] = (-iValue, 0, iMask)
    
    if 'SkillFactor' not in dFactor and 'Skill' in dDamage:
        oSkill = dDamage['Skill']
        dSkillFactor = oSkill.m_Collect['DamFactor'] if 'DamFactor' in oSkill.m_Collect else { }
        dFactor['SkillFactor'] = dSkillFactor
    lstDam = []
    iLuckHitEff = dDamage['LuckyHitEff'] if 'LuckyHitEff' in dDamage else 1
    oResistance = oVictim.m_Resistance
    for iDam, oReason in lstMainDam:
        iDamType = oReason.Query('DamType')
        if iDamType & DAM_TYPE_TRUE == DAM_TYPE_TRUE:
            lstDam.append((iDam, oReason))
            continue
        for dEachFactor in dFactor.values():
            if not dEachFactor:
                continue
            iAdd = 10000
            iMul = 10000
            for _Add, _Mul, iMask in dEachFactor.values():
                if iMask and iDamType & iMask == 0:
                    continue
                iAdd += _Add
                if _Mul < -10000:
                    _Mul = -10000
                iMul = iMul * (10000 + _Mul) // 10000
            
            if iAdd < 0:
                iAdd = 0
            iDam = iDam * iAdd * iMul // 10000 // 10000
        
        if oResistance:
            iResistance = oResistance.GetResistanceByType(iDamType)
            iDam = iDam * (10000 - iResistance) // 10000
        if iLuckHitEff > 1:
            iDam = iDam * iLuckHitEff
            oReason.SetInfo('LuckyHitEff', iLuckHitEff)
        iDam = oVictim.ChangeDamageByPartType(iDam, iDamType, dDamage)
        if iDam <= 0:
            continue
        # iMaxDamage = g_MaxPerformDamage if iDamType & DAM_TYPE_PERFORM else g_MaxSingleDamage
        # if iDam > iMaxDamage:
        #     iDam = iMaxDamage
        iCopyTimes = oReason.Query('CopyTimes', 0)
        if iCopyTimes:
            iDam = iDam * (1 + iCopyTimes)
        lstDam.append((iDam, oReason))
    
    for iDam, oReason in lstFlowDam:
        iDamType = oReason.Query('DamType')
        if iDamType & DAM_TYPE_TRUE == DAM_TYPE_TRUE:
            lstDam.append((iDam, oReason))
            continue
        if oReason.Query('ThunderStrike', 0) and 'SkillFactor' in dFactor:
            dFactor['SkillFactor'] = { }
        for dEachFactor in dFactor.values():
            if not dEachFactor:
                continue
            iAdd = 10000
            iMul = 10000
            for _Add, _Mul, iMask in dEachFactor.values():
                if iMask and iDamType & iMask == 0:
                    continue
                iAdd += _Add
                if _Mul < -10000:
                    _Mul = -10000
                iMul = iMul * (10000 + _Mul) // 10000
            
            if iAdd < 0:
                iAdd = 0
            iDam = iDam * iAdd * iMul // 10000 // 10000
        
        if oResistance:
            iResistance = oResistance.GetResistanceByType(iDamType)
            iDam = iDam * (10000 - iResistance) // 10000
        if iLuckHitEff > 1 and oReason.Query('CalLuckyHit', 0):
            iDam = iDam * iLuckHitEff
            oReason.SetInfo('LuckyHitEff', iLuckHitEff)
        iDam = oVictim.ChangeDamageByPartType(iDam, iDamType, dDamage)
        if iDam <= 0:
            continue
        # iMaxDamage = g_MaxPerformDamage if iDamType & DAM_TYPE_PERFORM else g_MaxSingleDamage
        # if iDam > iMaxDamage:
        #     iDam = iMaxDamage
        iCopyTimes = oReason.Query('CopyTimes', 0)
        if iCopyTimes:
            iDam = iDam * (1 + iCopyTimes)
        lstDam.append((iDam, oReason))
    
    return lstDam

CalDamage = InternalCalDamage(CalDamage)

def CalDealTotalDam(dDamage):
    iEffectDam = sum(dDamage['TotalDam'])
    iExcessDam = 0
    for iDam, _ in dDamage['ExcessChange']:
        iExcessDam += iDam
    
    iTotalDam = iEffectDam + iExcessDam + dDamage['DeductionDamage']
    iModNum = iTotalDam % 100
    if iModNum:
        iTotalDam = (iTotalDam - iModNum) + 100
    return iTotalDam

g_AttrInfo = {
    'HPMax': {
        'client': 2,
        'times': 100 },
    'RHP': {
        'client': 2,
        'times': 100 },
    'ArmorMax': {
        'client': 2,
        'times': 100 },
    'ShieldMax': {
        'client': 2,
        'times': 100 },
    'RShield': {
        'client': 2,
        'times': 100 },
    'ShieldRecoverTime': {
        'client': 0,
        'times': 100 },
    'EnergyMax': {
        'client': 2,
        'times': 100 },
    'REnergy': {
        'client': 2,
        'times': 100 },
    'CrazyEff': {
        'client': 0,
        'times': 100 },
    'HardEff': {
        'client': 0,
        'times': 100 },
    'Att': {
        'client': 1,
        'times': 100 },
    'MaxDeviceEnergy': {
        'client': 2,
        'times': 100 },
    'RDeviceEnergy': {
        'client': 0,
        'times': 100 },
    'DefPhysical': {
        'client': 2,
        'times': 100 },
    'DefThunder': {
        'client': 2,
        'times': 100 },
    'DefCorrision': {
        'client': 2,
        'times': 100 },
    'DefFire': {
        'client': 2,
        'times': 100 },
    'DebuffProb': {
        'client': 0,
        'times': 1 },
    'MoveSpeed': {
        'client': 2,
        'times': 100 },
    'AttSpeed': {
        'client': 2,
        'times': 100 },
    'Toughness': {
        'client': 0,
        'times': 1 },
    'FillTime': {
        'client': 2,
        'times': 1 },
    'TurnSpeed': {
        'client': 0,
        'times': 1 },
    'TurnThresholdAngle': {
        'client': 1,
        'times': 1 },
    'TurnInterval': {
        'client': 1,
        'times': 1 },
    'AccuracyProb': {
        'client': 0,
        'times': 1 },
    'DefThump': {
        'client': 0,
        'times': 1 },
    'ThumpFrame': {
        'client': 0,
        'times': 1 },
    'DefKnockBack': {
        'client': 0,
        'times': 1 },
    'KnockBackFrame': {
        'client': 0,
        'times': 1 },
    'StruckIgnoreFrame': {
        'client': 0,
        'times': 1 },
    'AdsorbDis': {
        'client': 1,
        'times': 1 },
    'SaveTime': {
        'client': 1,
        'times': 1 },
    'DodgeProb': {
        'client': 0,
        'times': 1 },
    'IntervalTime': {
        'client': 0,
        'times': 1 },
    'HitRange': {
        'client': 2,
        'times': 100 },
    'Scale': {
        'client': 2,
        'times': 100 },
    'RelifeTime': {
        'client': 2,
        'times': 100 },
    'SkillInterval': {
        'client': 2,
        'times': 100 },
    'SpecialMHPWeight': {
        'client': 2,
        'times': 100 },
    'LifeTime': {
        'client': 0,
        'times': 1 } }
g_GradeAttr = ('HPMax', 'RHP', 'ArmorMax', 'ShieldMax', 'RShield', 'ShieldRecoverTime', 'CrazyEff', 'Att', 'MoveSpeed', 'AttSpeed', 'Toughness', 'FillTime', 'TurnSpeed', 'DefFire', 'DefCorrision', 'DefThunder', 'DefPhysical')
g_HeroGradeAttr = ('HPMax', 'RHP', 'ArmorMax', 'ShieldMax', 'RShield', 'ShieldRecoverTime', 'EnergyMax', 'REnergy', 'MoveSpeed', 'Toughness', 'DefPhysical', 'DefFire', 'DefCorrision', 'DefThunder', 'AdsorbDis', 'SaveTime', 'MaxDeviceEnergy', 'RDeviceEnergy')
g_MonsterAttr = ('HPMax', 'RHP', 'ArmorMax', 'ShieldMax', 'RShield', 'ShieldRecoverTime', 'CrazyEff', 'Att', 'MoveSpeed', 'AttSpeed', 'Toughness', 'TurnSpeed', 'StruckIgnoreFrame', 'DefFire', 'DefCorrision', 'DefThunder', 'DefPhysical', 'AccuracyProb', 'DefThump', 'ThumpFrame', 'DefKnockBack', 'KnockBackFrame', 'HardEff', 'TurnThresholdAngle', 'TurnInterval', 'DodgeProb', 'IntervalTime', 'EnergyMax', 'REnergy', 'SpecialMHPWeight')
g_ObstacleAttr = ('HPMax',)
g_MonsterPartAttr = ('HPMax',)
g_SummonAttr = ('HPMax', 'RHP', 'ArmorMax', 'ShieldMax', 'RShield', 'ShieldRecoverTime', 'CrazyEff', 'Att', 'HitRange', 'Scale', 'MoveSpeed', 'AttSpeed', 'Toughness', 'FillTime', 'TurnSpeed', 'DefFire', 'DefCorrision', 'DefThunder', 'DefPhysical')
g_ServantAttr = ('HPMax', 'RHP', 'ArmorMax', 'ShieldMax', 'RShield', 'ShieldRecoverTime', 'CrazyEff', 'Att', 'MoveSpeed', 'AttSpeed', 'Toughness', 'TurnSpeed', 'DefFire', 'DefCorrision', 'DefThunder', 'DefPhysical', 'EnergyMax', 'REnergy', 'AccuracyProb', 'SaveTime', 'LifeTime', 'HitRange')
g_DeviceAttr = ('HPMax', 'RHP', 'ArmorMax', 'ShieldMax', 'RShield', 'ShieldRecoverTime', 'CrazyEff', 'Att', 'MoveSpeed', 'AttSpeed', 'Toughness', 'FillTime', 'TurnSpeed', 'HitRange')
g_PetAttr = ('HPMax', 'RHP', 'ArmorMax', 'ShieldMax', 'RShield', 'ShieldRecoverTime', 'CrazyEff', 'Att', 'MoveSpeed', 'Scale', 'AttSpeed', 'RelifeTime', 'SkillInterval', 'DefFire', 'DefCorrision', 'DefThunder', 'DefPhysical', 'TurnSpeed', 'EnergyMax', 'REnergy', 'Toughness', 'DefThump', 'ThumpFrame', 'DefKnockBack', 'KnockBackFrame', 'StruckIgnoreFrame', 'AccuracyProb', 'HardEff', 'TurnThresholdAngle', 'DodgeProb', 'IntervalTime', 'SaveTime')
g_FightType2Attr = {
    WARRIOR_PET: g_PetAttr,
    WARRIOR_DEVICE: g_DeviceAttr,
    WARRIOR_SERVANT: g_ServantAttr,
    WARRIOR_SUMMON: g_SummonAttr,
    WARRIOR_MONSTER: g_MonsterAttr,
    WARRIOR_HERO: g_HeroGradeAttr }

def GetGradeAttrByFightType(iFightType):
    if iFightType in g_FightType2Attr:
        lstAttr = g_FightType2Attr[iFightType]
    elif iFightType & SCENEOBJ_TYPE in g_FightType2Attr:
        lstAttr = g_FightType2Attr[iFightType & SCENEOBJ_TYPE]
    else:
        lstAttr = g_GradeAttr
    return lstAttr


def ResetGradeAttr(oWarrior, dAttr, iRefreshFlag):
    iFightType = oWarrior.m_FightType
    lstAttr = GetGradeAttrByFightType(iFightType)
    for sAttr in lstAttr:
        dAttrInfo = g_AttrInfo[sAttr]
        iVal = dAttr[sAttr] if sAttr in dAttr else 0
        if dAttrInfo['client']:
            oWarrior.SetAttr(sAttr, iVal, iRefreshFlag | BASEATTR_CLIENT)
            continue
        oWarrior.SetAttr(sAttr, iVal, iRefreshFlag)
    


def ResetGradeFormulaAttr(oWarrior, dAttr, iGrade, iRefreshFlag):
    iFightType = oWarrior.m_FightType
    lstAttr = GetGradeAttrByFightType(iFightType)
    for sAttr in lstAttr:
        dAttrInfo = g_AttrInfo[sAttr]
        val = dAttr[sAttr] if sAttr in dAttr else 0
        iVal = GetFormulaResultByLV(oWarrior, val, iGrade)
        if dAttrInfo['client']:
            oWarrior.SetAttr(sAttr, iVal, iRefreshFlag | BASEATTR_CLIENT)
            continue
        oWarrior.SetAttr(sAttr, iVal, iRefreshFlag)
    


def GetPetGrowthFormula(oPet, sAttr, val):
    iOffset = oPet.m_OffsetRange[sAttr] * oPet.m_AttrOffset[sAttr] / 10
    oLevelCtrl = oPet.m_Game.m_WarMgr.GetComponent('LevelCtrl')
    iLevelCount = oLevelCtrl.GetLevelCount(LEVEL_TYPE_FIGHT) + oLevelCtrl.GetLevelCount(LEVEL_TYPE_BOSS)
    return int(GetFormulaResult(oPet, val) * (100 + iOffset) * (100 + oPet.m_AttrGrowth[sAttr] * max(0, iLevelCount - 3)) / 10000)


def GetPetOffsetFormula(oPet, sAttr, val):
    iOffset = oPet.m_OffsetRange[sAttr] * oPet.m_AttrOffset[sAttr] / 10
    return int(GetFormulaResult(oPet, val) * (100 - iOffset) / 100)

g_PetFormulaFunc = {
    'HPMax': GetPetGrowthFormula,
    'Att': GetPetGrowthFormula,
    'AttSpeed': GetPetOffsetFormula,
    'SkillInterval': GetPetOffsetFormula }

def GetPetNoGrowthFormula(clsData, sAttr, iAttrOffset):
    iOffset = clsData.m_OffsetRange[sAttr] * iAttrOffset // 10
    return int(clsData.m_BaseAttrInfo[sAttr] * (100 + iOffset) // 100)


def GetPetNegNoGrowthFormula(clsData, sAttr, iAttrOffset):
    iOffset = clsData.m_OffsetRange[sAttr] * iAttrOffset // 10
    return int(clsData.m_BaseAttrInfo[sAttr] * (100 - iOffset) // 100)

g_PetNoGrowthFunc = {
    'HPMax': GetPetNoGrowthFormula,
    'Att': GetPetNoGrowthFormula,
    'AttSpeed': GetPetNegNoGrowthFormula,
    'SkillInterval': GetPetNegNoGrowthFormula }

def ResetPetFormulaAttr(oWarrior, dAttr, iRefreshFlag, lstAttr = None):
    if not lstAttr:
        lstAttr = GetGradeAttrByFightType(WARRIOR_PET)
    bGrowth = ValidGrowth(oWarrior)
    for sAttr in lstAttr:
        dAttrInfo = g_AttrInfo[sAttr]
        val = dAttr[sAttr] if sAttr in dAttr else 0
        if sAttr in g_PetFormulaFunc and bGrowth:
            func = g_PetFormulaFunc[sAttr]
            iVal = func(oWarrior, sAttr, val)
        else:
            iVal = GetFormulaResult(oWarrior, val)
        if dAttrInfo['client']:
            oWarrior.SetAttr(sAttr, iVal, iRefreshFlag | BASEATTR_CLIENT)
            continue
        oWarrior.SetAttr(sAttr, iVal, iRefreshFlag)
    


def ValidGrowth(oWarrior):
    if oWarrior.m_FightType & WARRIOR_PET_HEROSIDE != WARRIOR_PET_HEROSIDE:
        return True
    return False

g_ItemPerformAttrClientRefresh = {
    'AddStateTime': 1,
    'ReduceDis': 0,
    'MaxReducePercent': 0,
    'LuckyHit': 0,
    'ThumpProb': 0 }

def ResetNoSceneObjGradeFormulaAttr(obj, dAttr, iGrade, iRefreshFlag):
    for sAttr, iVal in dAttr.items():
        iVal = GetFormulaResultByLV(obj, iVal, iGrade)
        iRefreshClient = g_ItemPerformAttrClientRefresh[sAttr] if sAttr in g_ItemPerformAttrClientRefresh else 1
        if iRefreshClient:
            obj.SetAttr(sAttr, iVal, iRefreshFlag | BASEATTR_CLIENT)
            continue
        obj.SetAttr(sAttr, iVal, iRefreshFlag)
    

QUERY_GET = 1
QUERYEXT_GET = 2
QUERYBASE_GET = 3
ATTR_GET = 4
FUNC_GET = 5
g_AttrGetFunc = {
    'Grade': ATTR_GET,
    'Speed': FUNC_GET,
    'AttSpeed': QUERY_GET,
    'MoveSpeed': QUERY_GET,
    'HP': FUNC_GET,
    'HPMax': QUERY_GET,
    'Armor': FUNC_GET,
    'ArmorMax': QUERY_GET,
    'Shield': FUNC_GET,
    'ShieldMax': QUERY_GET,
    'Energy': FUNC_GET,
    'EnergyMax': QUERY_GET,
    'Att': QUERY_GET,
    'Toughness': QUERY_GET,
    'RHP': QUERY_GET,
    'RShield': QUERY_GET,
    'BurstCount': FUNC_GET,
    'BAtt': QUERYBASE_GET,
    'BMoveSpeed': QUERYBASE_GET,
    'BAttSpeed': QUERYBASE_GET,
    'BHPMax': QUERYBASE_GET,
    'EAtt': QUERYEXT_GET,
    'EMoveSpeed': QUERYEXT_GET,
    'EAttSpeed': QUERYEXT_GET,
    'EHPMax': QUERYEXT_GET,
    'FillTime': QUERY_GET,
    'PreDodgeTime': ATTR_GET,
    'DodgeTime': ATTR_GET,
    'PostDodgeTime': ATTR_GET,
    'HitRange': QUERY_GET,
    'ChargeSpeed': QUERY_GET }

def GetWarriorAttr(sAttr, oWarrior):
    if sAttr not in g_AttrGetFunc:
        return 0
    iType = g_AttrGetFunc[sAttr]
    if iType == QUERY_GET:
        return oWarrior.QueryAttr(sAttr)
    if iType == QUERYEXT_GET:
        return oWarrior.QueryAttrExt(sAttr)
    if iType == QUERYBASE_GET:
        return oWarrior.QueryAttrBase(sAttr)
    if iType == ATTR_GET:
        return getattr(oWarrior, 'm_%s' % sAttr)
    return getattr(oWarrior, sAttr)()

g_ItemAttrGetFunc = {
    'Grade': ATTR_GET,
    'MaxBullet': QUERY_GET,
    'EffectDis': QUERY_GET,
    'AttDis': QUERY_GET,
    'Att': QUERY_GET,
    'FillTime': QUERY_GET,
    'AttSpeed': QUERY_GET,
    'CrazyEff': QUERY_GET,
    'Accuracy': QUERY_GET,
    'ElementType': ATTR_GET }

def GetItemAttr(sAttr, oItem):
    iType = QUERY_GET
    if sAttr in g_ItemAttrGetFunc:
        iType = g_ItemAttrGetFunc[sAttr]
    if iType == QUERY_GET:
        return oItem.QueryAttr(sAttr)
    if iType == ATTR_GET:
        return getattr(oItem, 'm_%s' % sAttr)
    return getattr(oItem, sAttr)()

ATTR_TRANS = 1
OTHER_TRANS = 2
QUERY_TRANS = 3
g_PartTransAttr = {
    'm_RunSpeedUpMul': ATTR_TRANS,
    'm_SprintSpeedUpMul': ATTR_TRANS,
    'HP': OTHER_TRANS,
    'MoveSpeed': OTHER_TRANS,
    'AttSpeed': QUERY_TRANS }

def LVFunc10(obj, lstFormula, dArgs):
    iGrade = dArgs[FML_ARG_LV]
    return lstFormula[1] * lstFormula[2] ** (iGrade - lstFormula[3]) * lstFormula[4] + lstFormula[5]


def LVFunc11(obj, lstFormula, dArgs):
    iGrade = dArgs[FML_ARG_LV]
    lstTmp = lstFormula[6:]
    dInfo = dict(enumerate(lstTmp))
    iPlayerCnt = obj.m_Game.m_WarMgr.GetAllPlayerCnt()
    if iPlayerCnt - 1 not in dInfo:
        return 0
    iFactor = dInfo[iPlayerCnt - 1]
    return (lstFormula[1] * lstFormula[2] ** (iGrade - lstFormula[3]) * lstFormula[4] + lstFormula[5]) * iFactor


def LVFunc12(obj, lstFormula, dArgs):
    iGrade = dArgs[FML_ARG_LV]
    return lstFormula[1] * (iGrade - lstFormula[2]) + lstFormula[3]


def LVFunc13(obj, lstFormula, dArgs):
    oGame = obj.m_Game
    iGrade = dArgs[FML_ARG_LV]
    iPlayerCnt = oGame.m_WarMgr.GetAllPlayerCnt()
    return lstFormula[1] * (iGrade - lstFormula[2]) + iPlayerCnt * lstFormula[3] + lstFormula[4]


def RandomFunc50(obj, lstFormula, dArgs):
    if lstFormula[2] < 0:
        iSign = -1
    elif lstFormula[2] > 0:
        iSign = 1
    else:
        return lstFormula[1]
    iTemp = abs(lstFormula[2])
    return lstFormula[1] + obj.m_Game.Random(iTemp) * iSign


def RandomFunc51(obj, lstFormula, dArgs):
    iBase = lstFormula[1]
    if not obj.m_Game:
        return iBase
    iPrecision = lstFormula[3]
    iRange = lstFormula[2] // iPrecision
    iOffset = obj.m_Game.Random(iRange * 2 + 1) - iRange
    iRet = iOffset * iPrecision + iBase
    return iRet


def RandomFunc52(obj, lstFormula, dArgs):
    if not obj.m_Game:
        return 0
    iBase = lstFormula[1]
    iMin = min(lstFormula[2], lstFormula[3])
    iRange = abs(lstFormula[3] - lstFormula[2])
    iOffset = obj.m_Game.Random(iRange) + iMin
    iRet = iBase * iOffset - lstFormula[4]
    return iRet


def RandomFunc53(obj, lstFormula, dArgs):
    iRandom = 0
    if lstFormula[4]:
        if lstFormula[4] < 0:
            iSign = -1
        elif lstFormula[4] > 0:
            iSign = 1
        iTemp = abs(lstFormula[4])
        iRandom = lstFormula[3] + obj.m_Game.Random(iTemp) * iSign
    else:
        iRandom = lstFormula[3]
    iRet = lstFormula[1] ** (obj.m_Grade - lstFormula[2])
    iRet = iRet * iRandom
    return iRet


def RandomFunc54(obj, lstFormula, dArgs):
    if not obj.m_Game:
        return 0
    return lstFormula[1] + lstFormula[2] * obj.m_Game.Random(lstFormula[3])


def AttrFunc105(obj, lstFormula, dArgs):
    iShieldMax = obj.ShieldMax()
    iShield = obj.Shield()
    return iShield * lstFormula[1] / iShieldMax / lstFormula[2]


def AttrFunc106(obj, lstFormula, dArgs):
    iCash = obj.m_WarCash
    iRatio = iCash * lstFormula[2] // 100
    iRatio = min(lstFormula[1], iRatio)
    return iRatio * lstFormula[3]


def CommonFunc201(obj, lstFormula, dArgs):
    oGame = obj.m_Game
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    if not oLevelCtrl:
        return 0
    return lstFormula[1] + oLevelCtrl.m_LayerNum * lstFormula[2] + oLevelCtrl.m_LevelNum * lstFormula[3]


def CommonFunc202(obj, lstFormula, dArgs):
    oGame = obj.m_Game
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    if not oLevelCtrl:
        return 0
    if 'QualityCoff' not in dArgs:
        return 0
    iQualityCoff = dArgs['QualityCoff'] / 100
    iRandMin = int(lstFormula[3] * 100)
    iRandMax = int(lstFormula[4] * 100)
    iRandCoff = (iRandMin + oGame.Random(iRandMax - iRandMin)) / 100
    iRet = int((oLevelCtrl.m_LayerNum * lstFormula[1] + oLevelCtrl.m_LevelNum * lstFormula[2]) * iQualityCoff * iRandCoff)
    return iRet


def CommonFunc203(obj, lstFormula, dArgs):
    if 'QualityCoff' not in dArgs:
        return 0
    iRet = int(lstFormula[1] * dArgs['QualityCoff'] // 100 + lstFormula[2])
    return iRet


def CommonFunc204(obj, lstFormula, dArgs):
    oGame = obj.m_Game
    iCnt = oGame.m_WarMgr.GetAllPlayerCnt()
    return (iCnt - lstFormula[1]) * lstFormula[2] + lstFormula[3]


def CommonFunc205(obj, lstFormula, dArgs):
    oGame = obj.m_Game
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    if not oLevelCtrl:
        return 0
    iRet = int((lstFormula[1] + oGame.m_WarMgr.m_Round) * lstFormula[2] ** (oLevelCtrl.m_LayerNum - lstFormula[3]) + lstFormula[4])
    return iRet


def CommonFunc206(obj, lstFormula, dArgs):
    oGame = obj.m_Game
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    if not oLevelCtrl:
        return 0
    iRet = int(oGame.m_WarMgr.m_Round + lstFormula[1])
    return iRet


def CommonFunc207(obj, lstFormula, dArgs):
    iCash = obj.m_WarCash
    iRet = iCash * lstFormula[1] // 100 + lstFormula[2]
    return iRet


def CommonFunc208(obj, lstFormula, dArgs):
    dMsgInfo = dArgs[FML_ARG_MSGINFO]
    iCost = dMsgInfo['Cost']
    return iCost * lstFormula[1] // 100 + lstFormula[2]


def CommonFunc209(obj, lstFormula, dArgs):
    oGame = obj.m_Game
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    if not oLevelCtrl:
        return 0
    iCnt = oGame.m_WarMgr.m_Round * lstFormula[1] + lstFormula[2]
    return int(iCnt)


def CommonFunc210(obj, lstFormula, dArgs):
    oGame = obj.m_Game
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    if not oLevelCtrl:
        return 0
    iRandMin = int(lstFormula[4] * 100)
    iRandMax = int(lstFormula[5] * 100)
    iRandCoff = (iRandMin + oGame.Random(max(0, iRandMax - iRandMin))) / 100
    iRet = int((lstFormula[1] + oLevelCtrl.m_LayerNum * lstFormula[2] + oLevelCtrl.m_LevelNum * lstFormula[3]) * iRandCoff)
    return iRet


def CommonFunc211(obj, lstFormula, dArgs):
    iCount = 0
    for oPerform in obj.m_RelicCon.GetAllPerform():
        if oPerform.m_RelicType == RELIC_TYPE_CURSE:
            iCount += 1
    
    return iCount * lstFormula[1] + lstFormula[2]


def CommonFunc212(obj, lstFormula, dArgs):
    oWarMgr = obj.m_Game.m_WarMgr
    iRound = oWarMgr.m_Round
    iPlayerCnt = oWarMgr.Query('GMSpawnCnt')
    if not iPlayerCnt:
        oRidingAloneElement = oWarMgr.GetComponent('RidingAloneElement')
        if oRidingAloneElement:
            iPlayerCnt = oRidingAloneElement.m_SpawnCnt
        else:
            iPlayerCnt = oWarMgr.GetAllPlayerCnt()
    iCnt = (iRound - lstFormula[1]) * lstFormula[2] + (iPlayerCnt - lstFormula[3]) * lstFormula[4] + lstFormula[5]
    return int(iCnt)


def CommonFunc213(obj, lstFormula, dArgs):
    oGame = obj.m_Game
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    iLayer = oLevelCtrl.m_LayerNum if oLevelCtrl else 0
    iLevel = oLevelCtrl.m_LevelNum if oLevelCtrl else 0
    return int(obj.m_WarCash * lstFormula[1] // 100 + iLayer * lstFormula[2] + iLevel * lstFormula[3])


def CommonFunc214(obj, lstFormula, dArgs):
    dTimes = obj.Query('HeroRefreshTimes', { })
    iVictim = dArgs[FML_ARG_VID]
    iTimes = dTimes[iVictim] if iVictim in dTimes else 0
    return int(lstFormula[1] * lstFormula[2] ** iTimes + lstFormula[3])


def CommonFunc215(obj, lstFormula, dArgs):
    return int(lstFormula[1] * lstFormula[2] ** obj.GetArgValue(lstFormula[3]) + lstFormula[4])


def CommonFunc216(obj, lstFormula, dArgs):
    oGame = obj.m_Game
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    iRound = oGame.m_WarMgr.m_Round
    return lstFormula[1] + oLevelCtrl.m_LayerNum * lstFormula[2] + oLevelCtrl.m_LevelNum * lstFormula[3] + iRound * lstFormula[4]


def CommonFunc217(obj, lstFormula, dArgs):
    dMsgInfo = dArgs[FML_ARG_MSGINFO]
    if 'Debuff' not in dMsgInfo:
        return 0
    dDebuffInfo = dMsgInfo['Debuff']
    iDebuffTime = dDebuffInfo['DebuffTime']
    return iDebuffTime * lstFormula[1] // 100 + lstFormula[2]


def CommonFunc218(obj, lstFormula, dArgs):
    dMsgInfo = dArgs[FML_ARG_MSGINFO]
    if 'OldHpData' not in dMsgInfo:
        return 0
    iHPIdx = g_HpTypeIndex['HP']
    lstOldHP = dMsgInfo['OldHpData'][iHPIdx]
    lstNewHP = dMsgInfo['NewHpData'][iHPIdx]
    return (lstNewHP - lstOldHP) * lstFormula[1] // 100 + lstFormula[2]


def CommonFunc219(obj, lstFormula, dArgs):
    oGame = obj.m_Game
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    iLayer = oLevelCtrl.m_LayerNum if oLevelCtrl else 0
    iLevel = oLevelCtrl.m_LevelNum if oLevelCtrl else 0
    return int(obj.m_WarGSCash * lstFormula[1] // 100 + iLayer * lstFormula[2] + iLevel * lstFormula[3] + lstFormula[4])


def CommonFunc220(obj, lstFormula, dArgs):
    dMsgInfo = dArgs[FML_ARG_MSGINFO]
    iChange = dMsgInfo['Amount']
    iCost = -iChange if iChange < 0 else 0
    return iCost * lstFormula[1] // 100 + lstFormula[2]


def PerformFunc301(obj, lstFormula, dArgs):
    oAttack = dArgs[FML_ARG_AOBJ]
    if not oAttack:
        return 0
    iHP = oAttack.HP()
    iShield = oAttack.Shield()
    return int((iHP + iShield) * lstFormula[1] // 100 + lstFormula[2])


def PerformFunc302(obj, lstFormula, dArgs):
    oVictim = dArgs[FML_ARG_VOBJ]
    if not oVictim:
        return 0
    return GetWarriorAttr(lstFormula[1], oVictim) * lstFormula[2] // 100 + lstFormula[3]


def PerformFunc303(obj, lstFormula, dArgs):
    oSkill = dArgs[FML_ARG_SKILLOBJ]
    sAttr = lstFormula[1]
    if sAttr not in oSkill.m_Cache:
        return 0
    return oSkill.m_Cache[sAttr] * lstFormula[2] // 100 + lstFormula[3]


def PerformFunc304(obj, lstFormula, dArgs):
    if not obj:
        return 0
    return (GetWarriorAttr(lstFormula[1], obj) + GetWarriorAttr(lstFormula[2], obj)) * lstFormula[3] // 100 + lstFormula[4]


def PerformFunc307(obj, lstFormula, dArgs):
    oAttack = dArgs[FML_ARG_AOBJ]
    if not oAttack:
        return 0
    return GetWarriorAttr(lstFormula[1], oAttack) * lstFormula[2] // 100 + lstFormula[3]


def PerformFunc308(obj, lstFormula, dArgs):
    if not obj:
        return 0
    return GetWarriorAttr(lstFormula[1], obj) * lstFormula[2] / 100 + lstFormula[3]


def PerformFunc309(obj, lstFormula, dArgs):
    oAttack = dArgs[FML_ARG_AOBJ]
    if not oAttack:
        return 0
    iHPMax = oAttack.QueryAttr('HPMax')
    iHp = oAttack.HP()
    return iHp * lstFormula[1] // iHPMax + lstFormula[2]


def PerformFunc310(obj, lstFormula, dArgs):
    iHPMax = obj.QueryAttr('HPMax')
    iHp = obj.HP()
    return iHp * lstFormula[1] // iHPMax + lstFormula[2]


def PerformFunc313(obj, lstFormula, dArgs):
    dPassive = dArgs[FML_ARG_PASSIVE]
    iLevel = dPassive['PFLV']
    return iLevel * lstFormula[1] + lstFormula[2]


def PerformFunc317(obj, lstFormula, dArgs):
    oSkill = dArgs[FML_ARG_SKILLOBJ]
    if 'BaseBullet' in oSkill.m_Collect:
        iBase = oSkill.m_Collect['BaseBullet']
    else:
        iBase = 0
        SkillLog.Error('Func317获取基础子弹消耗失败 技能SID%d' % oSkill.m_Base['pfid'])
    iExt = oSkill.m_Collect['ExtBulletUse'] if 'ExtBulletUse' in oSkill.m_Collect else 0
    return (iBase + iExt) * lstFormula[1] + lstFormula[2]


def PerformFunc318(obj, lstFormula, dArgs):
    oSkill = dArgs[FML_ARG_SKILLOBJ]
    iPerform = oSkill.m_Base['pfid']
    clsPerform = cl_perform.GetPerformModule(iPerform)
    return int(clsPerform.m_BulletUse * lstFormula[1] + lstFormula[2])


def PerformFunc320(obj, lstFormula, dArgs):
    dMsgInfo = dArgs[FML_ARG_MSGINFO]
    iAmount = dMsgInfo['Amount'] if 'Amount' in dMsgInfo else 0
    iAttr = obj.QueryAttr(lstFormula[1])
    return int(iAttr * iAmount * lstFormula[2]) // 100 + lstFormula[3]


def PerformFunc322(obj, lstFormula, dArgs):
    oVictim = dArgs[FML_ARG_VOBJ]
    oAttack = dArgs[FML_ARG_AOBJ]
    if not oVictim or not oAttack:
        return 0
    iDis = cl_math.CalDistance3D(oVictim.GetPos(), oAttack.GetPos())
    return int((iDis // lstFormula[1]) * lstFormula[2] + lstFormula[3])


def PerformFunc323(obj, lstFormula, dArgs):
    oVictim = dArgs[FML_ARG_VOBJ]
    if not oVictim:
        return 0
    dMsgInfo = dArgs[FML_ARG_MSGINFO]
    if 'IsDam' not in dMsgInfo or not dMsgInfo['IsDam']:
        return 0
    iLost = dMsgInfo['TotalDam'][0]
    iShieldMax = oVictim.ShieldMax()
    return int((iLost * 100 // iShieldMax) * lstFormula[1] + lstFormula[2])


def PerformFunc324(obj, lstFormula, dArgs):
    oVictim = dArgs[FML_ARG_VOBJ]
    if not oVictim:
        return 0
    dMsgInfo = dArgs[FML_ARG_MSGINFO]
    if 'IsDam' not in dMsgInfo or not dMsgInfo['IsDam']:
        return 0
    iLost = dMsgInfo['TotalDam'][2]
    iHPMax = oVictim.QueryAttr('HPMax')
    return int((iLost * 100 // iHPMax) * lstFormula[1] + lstFormula[2])


def PerformFunc325(obj, lstFormula, dArgs):
    iHPMax = obj.QueryAttr('HPMax')
    iHp = obj.HP()
    iShieldMax = obj.ShieldMax()
    iShield = obj.Shield()
    return int(((iHPMax + iShieldMax - iHp - iShield) * 100 // (iHPMax + iShieldMax)) * lstFormula[1] // 100 + lstFormula[2])


def PerformFunc326(obj, lstFormula, dArgs):
    dMsgInfo = dArgs[FML_ARG_MSGINFO]
    if 'IsDam' not in dMsgInfo or not dMsgInfo['IsDam']:
        return 0
    iLost = sum(dMsgInfo['TotalDam'])
    return int(iLost * lstFormula[1] // 100 + lstFormula[2])


def PerformFunc330(obj, lstFormula, dArgs):
    oSkill = dArgs[FML_ARG_SKILLOBJ]
    if not oSkill:
        return 0
    fRatio = cl_action.CalCrtFlyDis(oSkill, lstFormula[1]) / cl_action.CalCrtFlyMaxDis(oSkill, lstFormula[1])
    iChange = int(fRatio * lstFormula[2]) + lstFormula[3]
    return iChange


def PerformFunc331(obj, lstFormula, dArgs):
    oTalent = obj.m_TalentCon.GetPerform(lstFormula[1])
    if not oTalent:
        return 0
    iLevel = oTalent.m_Level
    return iLevel * lstFormula[2] + lstFormula[3]


def PerformFunc332(obj, lstFormula, dArgs):
    oVictim = dArgs[FML_ARG_VOBJ]
    if not oVictim:
        return 0
    iHp = oVictim.HP()
    iShield = oVictim.Shield()
    iArmor = oVictim.Armor()
    return (iHp * lstFormula[1] + iShield * lstFormula[2] + iArmor * lstFormula[3]) // 100 + lstFormula[4]


def PerformFunc333(obj, lstFormula, dArgs):
    oVictim = dArgs[FML_ARG_VOBJ]
    if not oVictim:
        return 0
    iHPNow = oVictim.HP()
    iHPMax = oVictim.QueryAttr('HPMax')
    return (iHPMax - iHPNow) * lstFormula[1] / iHPMax


def PerformFunc334(obj, lstFormula, dArgs):
    oState = obj.m_State.GetItemBySID(lstFormula[1])
    if not oState:
        return 0
    dPassive = dArgs[FML_ARG_PASSIVE]
    iLevel = dPassive['PFLV']
    iFrame = oState.GetTime()
    return Frame2Time(iFrame) * iLevel * lstFormula[2] // 100


def PerformFunc335(obj, lstFormula, dArgs):
    oSkill = dArgs[FML_ARG_SKILLOBJ]
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return 0
    iWeapon = oSkill.m_Base['Weapon']
    oWeapon = oAttack.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return 0
    oBulletCom = oWeapon.GetComponent('Bullet')
    if not oBulletCom:
        return 0
    return oBulletCom.Bullet() * lstFormula[1] // 100 + lstFormula[2]


def PerformFunc336(obj, lstFormula, dArgs):
    oSkill = dArgs[FML_ARG_SKILLOBJ]
    sKey = lstFormula[2]
    if sKey not in oSkill.m_Collect:
        return 0
    return lstFormula[1] ** oSkill.m_Collect[sKey] * lstFormula[3] + lstFormula[4]


def PerformFunc337(obj, lstFormula, dArgs):
    oSkill = dArgs[FML_ARG_SKILLOBJ]
    dTriggerCartoon = oSkill.m_Collect['TriggerCartoon'] if 'TriggerCartoon' in oSkill.m_Collect else { }
    if not dTriggerCartoon:
        return 0
    dCurCartoon = oSkill.GetCurCartoon()
    if not dCurCartoon:
        return 0
    iCurCartoon = dCurCartoon['ID']
    if iCurCartoon in dTriggerCartoon:
        iValue = dTriggerCartoon[iCurCartoon]
    elif 'Parent' in dCurCartoon:
        iValue = dTriggerCartoon[dCurCartoon['Parent']] if dCurCartoon['Parent'] in dTriggerCartoon else 0
    else:
        return 0
    return iValue * lstFormula[1] + lstFormula[2]


def PerformFunc338(obj, lstFormula, dArgs):
    dMsgInfo = dArgs[FML_ARG_MSGINFO]
    iTriggerNum = dMsgInfo['TriggerNum'] if 'TriggerNum' in dMsgInfo else 0
    return iTriggerNum * lstFormula[1] + lstFormula[2]


def PerformFunc339(obj, lstFormula, dArgs):
    oSkill = dArgs[FML_ARG_SKILLOBJ]
    if 'LastVLST' not in oSkill.m_Update:
        return 0
    iCnt = len(oSkill.m_Update['LastVLST'])
    return iCnt * lstFormula[1] + lstFormula[2]


def PerformFunc340(obj, lstFormula, dArgs):
    sKey = 'MoveDis%s' % lstFormula[1]
    (_, fDis) = obj.Query(sKey, (0, 0))
    return int(fDis) * lstFormula[2] + lstFormula[3]


def PerformFunc341(obj, lstFormula, dArgs):
    if not obj.m_FightType & WARRIOR_MONSTER == WARRIOR_MONSTER:
        return 0
    return obj.m_Phase + lstFormula[1]


def PerformFunc342(obj, lstFormula, dArgs):
    oGame = obj.m_Game
    iAttr = GetWarriorAttr(lstFormula[1], obj) * lstFormula[2] // 100 + lstFormula[3]
    iCnt = oGame.m_WarMgr.GetAllPlayerCnt() * lstFormula[4] // 100 + lstFormula[5]
    iResult = int(iAttr // iCnt)
    return iResult


def PerformFunc343(obj, lstFormula, dArgs):
    oBulletContainer = obj.m_BulletCon
    iHasBullet = oBulletContainer.Bullet(lstFormula[1])
    return iHasBullet * lstFormula[2] // 100 + lstFormula[3]


def StateFunc405(obj, lstFormula, dArgs):
    dState = dArgs[FML_ARG_STDICT]
    iStateID = dState['StateID']
    oState = obj.m_State.GetItem(iStateID)
    if not oState:
        return 0
    oGame = obj.m_Game
    iPassFrame = oGame.GetFrameNum() - oState.m_StartTime
    iTime = Frame2Time(iPassFrame)
    iSecond = iTime // 100
    return iSecond * lstFormula[1] // 100 + lstFormula[2]


def StateFunc406(obj, lstFormula, dArgs):
    dState = dArgs[FML_ARG_STDICT]
    if 'ArgData' not in dState:
        return 0
    dArgData = dState['ArgData']
    if 'Cache' not in dArgData:
        return 0
    dCache = dArgData['Cache']
    iAtt = dCache['Att'] if dCache and 'Att' in dCache else 0
    return iAtt * lstFormula[1] // 100 + lstFormula[2]


def StateFunc407(obj, lstFormula, dArgs):
    dState = dArgs[FML_ARG_STDICT]
    iLevel = dState['StateInfo']['PFLV'] if 'PFLV' in dState['StateInfo'] else 0
    if not iLevel:
        return 0
    return iLevel * lstFormula[1] + lstFormula[2]


def StateFunc408(obj, lstFormula, dArgs):
    return int(GetWarriorAttr(lstFormula[1], obj) * lstFormula[2] / 100 + lstFormula[3])


def StateFunc409(obj, lstFormula, dArgs):
    dState = dArgs[FML_ARG_STDICT]
    iLevel = dState['StateInfo']['PFLV'] if 'PFLV' in dState['StateInfo'] else 0
    if not iLevel:
        return 0
    return lstFormula[1] * lstFormula[2] ** (iLevel - lstFormula[3]) + lstFormula[4]


def StateFunc410(obj, lstFormula, dArgs):
    dState = dArgs[FML_ARG_STDICT]
    iStateID = dState['StateID']
    oState = obj.m_State.GetItem(iStateID)
    if not oState:
        return 0
    return int(oState.GetCount() * lstFormula[1] + lstFormula[2])


def StateFunc411(obj, lstFormula, dArgs):
    iShieldMax = obj.ShieldMax()
    iShield = obj.Shield()
    fRatio = iShield / iShieldMax if iShieldMax > 0 else 0
    return int(fRatio * lstFormula[1] + lstFormula[2])


def StateFunc412(obj, lstFormula, dArgs):
    dState = dArgs[FML_ARG_STDICT]
    iStateID = dState['StateID']
    oState = obj.m_State.GetItem(iStateID)
    if not oState:
        return lstFormula[3]
    iCurFrame = obj.m_Game.GetFrameNum()
    iBegFrame = oState.m_CreateFrame
    iFrame = lstFormula[2] - Frame2Time(iCurFrame - iBegFrame)
    return max(lstFormula[1], iFrame) + lstFormula[3]


def StateFunc413(obj, lstFormula, dArgs):
    dState = dArgs[FML_ARG_STDICT]
    iLevel = dState['StateInfo']['PFLV'] if 'PFLV' in dState['StateInfo'] else 0
    if not iLevel:
        return int(lstFormula[3])
    return int(GetWarriorAttr(lstFormula[1], obj) * iLevel * lstFormula[2] // 100 + lstFormula[3])


def StateFunc414(obj, lstFormula, dArgs):
    oState = obj.m_State.GetItemBySID(lstFormula[1])
    if not oState:
        return 0
    iFrame = oState.GetTime()
    return Frame2Time(iFrame) * lstFormula[2] // 100


def StateFunc415(obj, lstFormula, dArgs):
    dState = dArgs[FML_ARG_STDICT]
    if 'ArgData' not in dState:
        return 0
    dArgData = dState['ArgData']
    if 'AbnormalSourceDam' in dArgData:
        iDam = dArgData['AbnormalSourceDam']
    elif 'Cache' in dArgData:
        dCache = dArgData['Cache']
        iDam = dCache['Att'] if dCache and 'Att' in dCache else 0
    else:
        iDam = 0
    return iDam * lstFormula[1] // 100 + lstFormula[2]


def StateFunc416(obj, lstFormula, dArgs):
    dState = dArgs[FML_ARG_STDICT]
    iStateID = dState['StateID']
    oState = obj.m_State.GetItem(iStateID)
    if not oState:
        return 0
    oReason = oState.Reason()
    iWeapon = oReason.Query('Item', 0)
    oWeapon = obj.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return 0
    oBulletCom = oWeapon.GetComponent('Bullet')
    if not oBulletCom:
        return 0
    iMaxBullet = oBulletCom.MaxBullet()
    return oState.GetCount() * lstFormula[1] / math.ceil(iMaxBullet * lstFormula[2] / 100 + lstFormula[3])


def StateFunc417(obj, lstFormula, dArgs):
    iState = lstFormula[1]
    oState = obj.m_State.GetItemBySID(iState)
    if not oState:
        return 0
    return int(oState.GetCount() * lstFormula[2] + lstFormula[3])


def StateFunc418(obj, lstFormula, dArgs):
    dState = dArgs[FML_ARG_STDICT]
    iStateID = dState['StateID']
    oState = obj.m_State.GetItem(iStateID)
    if not oState:
        return 0
    iAttacker = oState.m_Attacker
    oAttacker = obj.m_Game.GetObject(iAttacker)
    if not oAttacker:
        return 0
    return int(GetWarriorAttr(lstFormula[1], oAttacker)) * lstFormula[2] // 100 + lstFormula[3]


def StateFunc419(obj, lstFormula, dArgs):
    dState = dArgs[FML_ARG_STDICT]
    iStateID = dState['StateID']
    oState = obj.m_State.GetItem(iStateID)
    if not oState:
        return 0
    iAttacker = oState.m_Attacker
    oAttacker = obj.m_Game.GetObject(iAttacker)
    if not oAttacker:
        return 0
    return oState.GetCount() * int(GetWarriorAttr(lstFormula[1], obj)) * lstFormula[2] // 100 + lstFormula[3]


def StateFunc420(obj, lstFormula, dArgs):
    dState = dArgs[FML_ARG_STDICT]
    iStateID = dState['StateID']
    oState = obj.m_State.GetItem(iStateID)
    if not oState:
        return 0
    iPointState = lstFormula[2]
    oPointState = obj.m_State.GetItemBySID(iPointState)
    if not oPointState:
        return 0
    return int(oState.GetCount() * lstFormula[1] + oPointState.GetCount() * lstFormula[3] + lstFormula[4])


def StateFunc421(obj, lstFormula, dArgs):
    oVictim = dArgs[FML_ARG_VOBJ]
    if not oVictim:
        return 0
    iState = lstFormula[1]
    oState = oVictim.m_State.GetItemBySID(iState)
    if not oState:
        return 0
    return int(oState.GetCount() * lstFormula[2] + lstFormula[3])


def ItemFunc505(obj, lstFormula, dArgs):
    dItem = dArgs[FML_ARG_ITEMINFO]
    iMaxBullet = dItem['MaxBullet']
    return iMaxBullet * lstFormula[1] // 100 + lstFormula[2]


def ItemFunc507(obj, lstFormula, dArgs):
    dItem = dArgs[FML_ARG_ITEMINFO]
    iAmount = dItem['ItemAmount']
    return iAmount * lstFormula[1] // 100 + lstFormula[2]


def ItemFunc508(obj, lstFormula, dArgs):
    dItem = dArgs[FML_ARG_ITEMINFO]
    iAmount = dItem['ItemAmount']
    return lstFormula[1] * lstFormula[2] ** (iAmount - lstFormula[3]) + lstFormula[4]


def ItemFunc509(obj, lstFormula, dArgs):
    dItem = dArgs[FML_ARG_ITEMINFO]
    sAttr = lstFormula[1]
    iValue = dItem[sAttr]
    return iValue * lstFormula[2] // 100 + lstFormula[3]


def ItemFunc510(obj, lstFormula, dArgs):
    dItem = dArgs[FML_ARG_ITEMINFO]
    iItem = dItem['ItemID']
    oCon = obj.m_WieldCon
    lstPos = oCon.m_Type2Pos[itemdef.EQUIP_TYPE_MAINWEAPON]
    for iPos in lstPos:
        oOtherItem = oCon.GetItem(iPos)
        if oOtherItem and oOtherItem.m_ID != iItem:
            sAttr = lstFormula[1]
            iValue = GetItemAttr(sAttr, oOtherItem)
            return iValue * lstFormula[2] // 100 + lstFormula[3]
    
    return 0


def ItemFunc511(obj, lstFormula, dArgs):
    dItemIfon = dArgs[FML_ARG_ITEMINFO]
    iCurBullet = dItemIfon['CurBullet']
    return iCurBullet * lstFormula[1] // 100 + lstFormula[2]

if 'g_FormulaFunc' not in globals():
    g_FormulaFunc = { }
    g_FormulaList = { }
g_FormulaDefines = {
    'Max\\((\\S+),(\\S+)\\)': 1,
    'Min\\((\\S+),(\\S+)\\)': 2,
    'Time\\((\\S+)\\)': 3,
    '(\\S+)\\*(\\S+)\\^\\(等级\\-(\\S+)\\)\\*(\\S+)\\+(\\S+)': 10,
    '\\((\\S+)\\*(\\S+)\\^\\(等级\\-(\\S+)\\)\\*(\\S+)\\+(\\S+)\\)\\*玩家系数\\[(\\S+)\\]': 11,
    '(\\S+)\\*\\(等级\\-(\\S+)\\)\\+(\\S+)': 12,
    '(\\S+)\\*\\(等级\\-(\\S+)\\)\\+(\\S+)\\*人数\\+(\\S+)': 13,
    '([-\\d]+)\\+R([-\\d]+)': 50,
    '(\\d+)\\+R\\((\\d+),(\\d+)\\)': 51,
    '(\\d+)\\*R\\((\\d+),(\\d+)\\)\\-(\\d+)': 52,
    '(\\S+)\\^\\(等级\\-(\\d+)\\)\\*\\(([-\\d]+)\\+R([-\\d]+)\\)': 53,
    '(\\S+)\\+(\\S+)\\*R(\\S+)': 54,
    '护盾当前容量比率\\*(\\S+)\\/(\\S+)': 105,
    'Min\\((\\S+),\\(金币持有数量\\*(\\S+)\\%\\)\\)\\*(\\d+)': 106,
    '(\\S+)\\+层数\\*(\\S+)\\+关数\\*(\\S+)': 201,
    '层数\\*(\\S+)\\+关数\\*(\\S+)\\)\\*品质系数\\*random\\((\\S+),(\\S+)': 202,
    '品质系数\\*(\\S+)\\+(\\S+)': 203,
    '\\(战场玩家数量\\-(\\S+)\\)\\*(\\S+)\\+(\\S+)': 204,
    '\\((\\S+)\\+周目\\)\\*(\\S+)\\^\\(幕数\\-(\\S+)\\)\\+(\\S+)': 205,
    '周目\\+(\\S+)': 206,
    '拥有金币\\*(\\S+)%\\+(\\S+)': 207,
    '弹夹扣弹数\\*(\\S+)%\\+(\\S+)': 208,
    '周目\\*(\\S+)\\+(\\S+)': 209,
    '(\\S+)\\+层数\\*(\\S+)\\+关数\\*(\\S+)\\)\\*random\\((\\S+),(\\S+)': 210,
    '诅咒遗物个数\\*(\\S+)\\+(\\S+)': 211,
    '\\(周目\\-(\\S+)\\)\\*(\\S+)\\+\\(人数\\-(\\S+)\\)\\*(\\S+)\\+(\\S+)': 212,
    '当前金币\\*(\\S+)%\\+层数\\*(\\S+)\\+关数\\*(\\S+)': 213,
    '(\\S+)\\*\\((\\S+)\\^刷新次数\\)\\+(\\S+)': 214,
    '(\\S+)\\*\\((\\S+)\\^Npc参数\\((\\S+)\\)\\)\\+(\\S+)': 215,
    '(\\S+)\\+层数\\*(\\S+)\\+关数\\*(\\S+)\\+周目\\*(\\S+)': 216,
    '造成元素异常状态时长\\*(\\S+)\\%\\+(\\S+)': 217,
    '当次血量变化\\*(\\S+)\\%\\+(\\S+)': 218,
    '当前精魄\\*(\\S+)%\\+层数\\*(\\S+)\\+关数\\*(\\S+)\\+(\\S+)': 219,
    '普攻消耗备弹数\\*(\\S+)%\\+(\\S+)': 220,
    '攻击者当前生命值加当前护盾\\*(\\S+)%\\+(\\S+)': 301,
    '受击者\\((\\S+)\\)\\*(\\S+)%\\+(\\S+)': 302,
    '技能快照\\((\\S+)\\)\\*(\\S+)%\\+(\\S+)': 303,
    '\\(拥有者\\((\\S+)\\)\\+拥有者\\((\\S+)\\)\\)\\*(\\S+)%\\+(\\S+)': 304,
    '攻击者\\((\\S+)\\)\\*(\\S+)%\\+(\\S+)': 307,
    '拥有者\\((\\S+)\\)\\*(\\S+)%\\+(\\S+)': 308,
    '攻击者生命比例\\*(\\S+)\\+(\\S+)': 309,
    '拥有者生命比例\\*(\\S+)\\+(\\S+)': 310,
    '技能等级\\*(\\S+)\\+(\\S+)': 313,
    '攻击技能子弹消耗数\\*(\\S+)\\+(\\S+)': 317,
    '攻击技能基础子弹消耗数\\*(\\S+)\\+(\\S+)': 318,
    '道具数量\\*拥有者\\((\\S+)\\)\\*(\\S+)\\%\\+(\\S+)': 320,
    '受击者距离\\/(\\S+)\\*(\\S+)\\+(\\S+)': 322,
    '事件损失护盾百分比\\*(\\S+)\\+(\\S+)': 323,
    '事件损失血量百分比\\*(\\S+)\\+(\\S+)': 324,
    '拥有者损失血量护盾百分比\\*(\\S+)\\%\\+(\\S+)': 325,
    '事件损失血盾甲和\\*(\\S+)\\%\\+(\\S+)': 326,
    '动画飞行距离比\\((\\S+)\\)\\*(\\S+)\\%\\+(\\S+)': 330,
    '天赋等级\\((\\S+)\\)\\*(\\S+)\\+(\\S+)': 331,
    '受击者当前生命值\\*(\\S+)%\\+受击者当前护盾值\\*(\\S+)%\\+受击者当前装甲值\\*(\\S+)%\\+(\\S+)': 332,
    '受击者损失血量百分比\\*(\\S+)': 333,
    '技能等级\\*拥有者拥有状态持续时间\\((\\S+)\\)\\*(\\S+)%': 334,
    '技能武器当前子弹数\\*(\\S+)\\%\\+(\\S+)': 335,
    '(\\S+)\\^技能统计信息\\((\\S+)\\)\\*(\\S+)\\+(\\S+)': 336,
    '当前动画触发次数\\*(\\S+)\\+(\\S+)': 337,
    '同时触发技能数\\*(\\S+)\\+(\\S+)': 338,
    '技能命中个数\\*(\\S+)\\+(\\S+)': 339,
    '记录移动距离\\((\\S+)\\)\\*(\\S+)\\+(\\S+)': 340,
    '当前阶段\\+(\\S+)': 341,
    '\\(拥有者\\((\\S+)\\)\\*(\\S+)%\\+(\\S+)\\)/战场玩家数量\\*(\\S+)%\\+(\\S+)': 342,
    '备弹数\\((\\S+)\\)\\*(\\S+)\\%\\+(\\S+)': 343,
    '状态自身持续时间\\(单位秒\\)\\*(\\S+)\\%\\+(\\S+)': 405,
    '状态来源快照攻击力\\*(\\S+)%\\+(\\S+)': 406,
    '状态来源技能等级\\*(\\S+)\\+(\\S+)': 407,
    '状态拥有者\\((\\S+)\\)\\*(\\S+)%\\+(\\S+)': 408,
    '(\\S+)\\*(\\S+)\\^\\(状态来源技能等级\\-(\\S+)\\)\\+(\\S+)': 409,
    '状态计数\\*(\\S+)\\+(\\S+)': 410,
    '状态拥有者护盾比例\\*(\\S+)\\+(\\S+)': 411,
    'max\\((\\S+),(\\S+)\\-当前帧数\\+状态开始帧数\\)\\+(\\S+)': 412,
    '状态拥有者\\((\\S+)\\)\\*状态来源技能等级\\*(\\S+)%\\+(\\S+)': 413,
    '拥有者拥有状态持续时间\\((\\S+)\\)\\*(\\S+)\\%': 414,
    '元素异常状态来源伤害\\*(\\S+)%\\+(\\S+)': 415,
    '状态计数\\*(\\S+)/\\(来源武器弹夹容量\\*(\\S+)\\%\\+(\\S+)\\)': 416,
    '拥有者指定状态计数\\((\\S+)\\)\\*(\\S+)\\+(\\S+)': 417,
    '状态添加者\\((\\S+)\\)\\*(\\S+)%\\+(\\S+)': 418,
    '状态计数\\*状态拥有者\\((\\S+)\\)\\*(\\S+)%\\+(\\S+)': 419,
    '状态计数\\*(\\S+)\\+拥有者指定状态计数\\((\\S+)\\)\\*(\\S+)\\+(\\S+)': 420,
    '受击者指定状态计数\\((\\S+)\\)\\*(\\S+)\\+(\\S+)': 421,
    '武器弹夹容量\\*(\\S+)\\%\\+(\\S+)': 505,
    '道具堆叠数\\*(\\S+)\\%\\+(\\S+)': 507,
    '(\\S+)\\*(\\S+)\\^\\(道具堆叠数\\-(\\S+)\\)\\+(\\S+)': 508,
    '武器\\((\\S+)\\)\\*(\\S+)%\\+(\\S+)': 509,
    '双子武器\\((\\S+)\\)\\*(\\S+)%\\+(\\S+)': 510,
    '武器当前子弹数\\*(\\S+)\\%\\+(\\S+)': 511 }
g_FormulaList = []
for sRe, iNo in g_FormulaDefines.items():
    g_FormulaList.append((re.compile(sRe), iNo))

g_FormulaFunc = {
    10: LVFunc10,
    11: LVFunc11,
    12: LVFunc12,
    13: LVFunc13,
    50: RandomFunc50,
    51: RandomFunc51,
    52: RandomFunc52,
    53: RandomFunc53,
    54: RandomFunc54,
    105: AttrFunc105,
    106: AttrFunc106,
    201: CommonFunc201,
    202: CommonFunc202,
    203: CommonFunc203,
    204: CommonFunc204,
    205: CommonFunc205,
    206: CommonFunc206,
    207: CommonFunc207,
    208: CommonFunc208,
    209: CommonFunc209,
    210: CommonFunc210,
    211: CommonFunc211,
    212: CommonFunc212,
    213: CommonFunc213,
    214: CommonFunc214,
    215: CommonFunc215,
    216: CommonFunc216,
    217: CommonFunc217,
    218: CommonFunc218,
    219: CommonFunc219,
    220: CommonFunc220,
    301: PerformFunc301,
    302: PerformFunc302,
    303: PerformFunc303,
    304: PerformFunc304,
    307: PerformFunc307,
    308: PerformFunc308,
    309: PerformFunc309,
    310: PerformFunc310,
    313: PerformFunc313,
    317: PerformFunc317,
    318: PerformFunc318,
    320: PerformFunc320,
    322: PerformFunc322,
    323: PerformFunc323,
    324: PerformFunc324,
    325: PerformFunc325,
    326: PerformFunc326,
    330: PerformFunc330,
    331: PerformFunc331,
    332: PerformFunc332,
    333: PerformFunc333,
    334: PerformFunc334,
    335: PerformFunc335,
    336: PerformFunc336,
    337: PerformFunc337,
    338: PerformFunc338,
    339: PerformFunc339,
    340: PerformFunc340,
    341: PerformFunc341,
    342: PerformFunc342,
    343: PerformFunc343,
    405: StateFunc405,
    406: StateFunc406,
    407: StateFunc407,
    408: StateFunc408,
    409: StateFunc409,
    410: StateFunc410,
    411: StateFunc411,
    412: StateFunc412,
    413: StateFunc413,
    414: StateFunc414,
    415: StateFunc415,
    416: StateFunc416,
    417: StateFunc417,
    418: StateFunc418,
    419: StateFunc419,
    420: StateFunc420,
    421: StateFunc421,
    505: ItemFunc505,
    507: ItemFunc507,
    508: ItemFunc508,
    509: ItemFunc509,
    510: ItemFunc510,
    511: ItemFunc511 }

def GetFormulaList():
    return g_FormulaList


def GetFunc(iType):
    if iType in g_FormulaFunc:
        return g_FormulaFunc[iType]

FML_ARG_STDICT = 1
FML_ARG_SKILLOBJ = 2
FML_ARG_PASSIVE = 3
FML_ARG_VOBJ = 4
FML_ARG_VID = 5
FML_ARG_DAM = 6
FML_ARG_LV = 7
FML_ARG_SIDE = 8
FML_ARG_SEC = 9
FML_ARG_ITEM = 10
FML_ARG_AOBJ = 11
FML_ARG_AID = 12
FML_ARG_BASEDAM = 13
FML_ARG_ITEMINFO = 14
FML_ARG_OBJ = 15
FML_ARG_MSGINFO = 16
FML_TYPE_ALLLV = 32768
FML_TYPE_INT = 0
FML_TYPE_PERFORM = 1
FML_TYPE_STATE = 2
FML_TYPE_COMMON = 3
FML_TYPE_RANDOM = 4

def GetFormulaType(lstFormula):
    if isinstance(lstFormula, int):
        return FML_TYPE_INT
    iFormula = lstFormula[0] % 1000
    if iFormula < 100:
        return FML_TYPE_RANDOM
    if iFormula < 200:
        return FML_TYPE_COMMON
    if iFormula < 400:
        return FML_TYPE_PERFORM
    if iFormula < 500:
        return FML_TYPE_STATE
    return FML_TYPE_COMMON


def GetFormulaResult(obj, func, dArgs = None):
    if isinstance(func, int):
        return func
    return int(func(obj, dArgs, { }, { }))


def GetLegacyFormulaResult(obj, lstFormula, dArgs = None):
    if isinstance(lstFormula, int):
        return lstFormula
    iFuncNo = lstFormula[0]
    if iFuncNo == 1:
        iLeft = GetLegacyFormulaResult(obj, lstFormula[1], dArgs)
        iRight = GetLegacyFormulaResult(obj, lstFormula[2], dArgs)
        iResult = iLeft if iLeft > iRight else iRight
    elif iFuncNo == 2:
        iLeft = GetLegacyFormulaResult(obj, lstFormula[1], dArgs)
        iRight = GetLegacyFormulaResult(obj, lstFormula[2], dArgs)
        iResult = iLeft if iLeft < iRight else iRight
    else:
        func = GetFunc(iFuncNo)
        iResult = int(func(obj, lstFormula, dArgs)) if func else 0
    return iResult


def GetResultByData(obj, func, dData, dMsgInfo = None, dOtherArgs = None):
    if not callable(func):
        return func
    return int(func(obj, dData, dMsgInfo, dOtherArgs))


def CalArgsFormula(oTarget, dArgs, dData, dMsgInfo = None, dOtherArgs = None):
    dRet = { }
    for sKey, lstFormula in dArgs.items():
        if isinstance(lstFormula, dict):
            dRet[sKey] = lstFormula
            continue
        dRet[sKey] = GetResultByData(oTarget, lstFormula, dData, dMsgInfo, dOtherArgs)
    
    return dRet


def GetFormulaResultByLV(obj, func, iGrade, iTimes = 1):
    if isinstance(func, (int, float)):
        return func * iTimes
    iNewResult = int(func(obj, {
        FML_ARG_LV: iGrade }, { }, { }))
    if iTimes == 1:
        return iNewResult
    return int(iNewResult * iTimes + 0.1)


def CheckFormula(who):
    import mkparser
    import mkparser.defines
    import notify
    TestList = {
        1: ('Max(10,30)', '(1,10,30,)'),
        2: ('Min(10,30)', '(2,10,30,)'),
        10: ('10300*1.05^(等级-1)*0.45+0', '(10,10300,1.05,1,0.45,0,)'),
        11: ('(10300*1.05^(等级-1)*0.45+0)*玩家系数[1,2,3,4]', '(11,10300,1.05,1,0.45,0,1,2,3,4,)'),
        12: ('100*(等级-1)+10', '(12,100,1,10,)'),
        13: ('100*(等级-1)+3*人数+1', '(13,100,1,3,1,)'),
        50: ('-13+R-5', '(50,-13,-5,)'),
        51: ('800+R(100,10)', '(51,800,100,10,)'),
        52: ('100*R(95,105)-1000', '(52,100,95,105,1000,)'),
        53: ('1.05^(等级-1)*(1000+R500)', '(53,1.05,1,1000,500,)'),
        54: ('30+10*R3', '(54,30,10,3,)'),
        105: ('护盾当前容量比率*10000/1', '(105,10000,1,)'),
        106: ('Min(100,(金币持有数量*10%))*100', '(106,100,10,100,)'),
        201: ('10+层数*-3+关数*5', '(201,10,-3,5,)'),
        202: ('(层数*50+关数*100)*品质系数*random(0.9,1.0)', '(202,50,100,0.9,1.0,)'),
        203: ('品质系数*200+0', '(203,200,0,)'),
        204: ('(战场玩家数量-1) * 50 + 10', '(204,1,50,10,)'),
        205: ('(3+周目)*2^(幕数-1)+10', '(205,3,2,1,10,)'),
        206: ('周目+1', '(206,1,)'),
        207: ('拥有金币*50%+0', '(207,50,0,)'),
        208: ('弹夹扣弹数*100%+0', '(208,100,0,)'),
        209: ('周目*1.5+1', '(209,1.5,1,)'),
        210: ('(10+层数*3+关数*5)*random(10,20)', '(210,10,3,5,10,20,)'),
        211: ('诅咒遗物个数*2+3', '(211,2,3,)'),
        212: ('(周目-1)*1.5+(人数-1)*2+3', '(212,1,1.5,1,2,3,)'),
        213: ('当前金币*30%+层数*150+关数*30', '(213,30,150,30,)'),
        214: ('1*(2^刷新次数)+4', '(214,1,2,4,)'),
        215: ('1*(1^Npc参数("RefreshTimes"))+1', '(215,1,1,"RefreshTimes",1,)'),
        216: ('10+层数*-3+关数*5+周目*10', '(216,10,-3,5,10,)'),
        217: ('造成元素异常状态时长*1%+0', '(217,1,0,)'),
        218: ('当次血量变化*-100%+0', '(218,-100,0,)'),
        219: ('当前精魄*30%+层数*150+关数*30+6', '(219,30,150,30,6,)'),
        220: ('普攻消耗备弹数*100%+0', '(220,100,0,)'),
        301: ('攻击者当前生命值加当前护盾*10%+0', '(301,10,0,)'),
        302: ('受击者(生命上限)*50%+0', '(302,"HPMax",50,0,)'),
        303: ('技能快照(子弹容量)*50%+0', '(303,"MaxBullet",50,0,)'),
        304: ('(拥有者(生命上限)+拥有者(护盾上限))*11%+0', '(304,"HPMax","ShieldMax",11,0,)'),
        307: ('攻击者(生命上限)*50%+0', '(307,"HPMax",50,0,)'),
        308: ('拥有者(生命上限)*50%+0', '(308,"HPMax",50,0,)'),
        309: ('攻击者生命比例*50+0', '(309,50,0,)'),
        310: ('拥有者生命比例*50+0', '(310,50,0,)'),
        313: ('技能等级*500+1000', '(313,500,1000,)'),
        317: ('攻击技能子弹消耗数*1+0', '(317,1,0,)'),
        318: ('攻击技能基础子弹消耗数*1+5', '(318,1,5,)'),
        320: ('道具数量*拥有者(生命上限)*0.05%+0', '(320,"HPMax",0.05,0,)'),
        322: ('受击者距离/2*3+4', '(322,2,3,4,)'),
        323: ('事件损失护盾百分比*1+0', '(323,1,0,)'),
        324: ('事件损失血量百分比*1+0', '(324,1,0,)'),
        325: ('拥有者损失血量护盾百分比*1%+0', '(325,1,0,)'),
        326: ('事件损失血盾甲和*50%+2', '(326,50,2,)'),
        330: ('动画飞行距离比(0)*100%+0', '(330,0,100,0,)'),
        331: ('天赋等级(2115)*3+5', '(331,2115,3,5,)'),
        332: ('受击者当前生命值*30%+受击者当前护盾值*0%+受击者当前装甲值*0%+0', '(332,30,0,0,0,)'),
        333: ('受击者损失血量百分比*-5000', '(333,-5000,)'),
        334: ('技能等级*拥有者拥有状态持续时间(101)*50%', '(334,101,50,)'),
        335: ('技能武器当前子弹数*50%+10', '(335,50,10,)'),
        336: ('2^技能统计信息("abcd")*50+0', '(336,2,"abcd",50,0,)'),
        337: ('当前动画触发次数*50+0', '(337,50,0,)'),
        338: ('同时触发技能数*15+6', '(338,15,6,)'),
        339: ('技能命中个数*150+6', '(339,150,6,)'),
        340: ('记录移动距离("abcd")*13+6', '(340,"abcd",13,6,)'),
        341: ('当前阶段+1', '(341,1,)'),
        342: ('(拥有者(生命上限)*50%+100)/战场玩家数量*100%+10', '(342,"HPMax",50,100,100,10,)'),
        343: ('备弹数(4508)*50%+100', '(343,4508,50,100,)'),
        405: ('状态自身持续时间(单位秒)*100000%+0', '(405,100000,0,)'),
        406: ('状态来源快照攻击力*50%+100', '(406,50,100,)'),
        407: ('状态来源技能等级*300+100', '(407,300,100,)'),
        408: ('状态拥有者(生命上限)*50%+1', '(408,"HPMax",50,1,)'),
        409: ('1000*1.05^(状态来源技能等级-1)+0', '(409,1000,1.05,1,0,)'),
        410: ('状态计数*300+100', '(410,300,100,)'),
        411: ('状态拥有者护盾比例*100+0', '(411,100,0,)'),
        412: ('max(300,300-当前帧数+状态开始帧数)+300', '(412,300,300,300,)'),
        413: ('状态拥有者(生命上限)*状态来源技能等级*50%+0', '(413,"HPMax",50,0,)'),
        414: ('拥有者拥有状态持续时间(101)*50%', '(414,101,50,)'),
        415: ('元素异常状态来源伤害*50%+100', '(415,50,100,)'),
        416: ('状态计数*5/(来源武器弹夹容量*100%+0)', '(416,5,100,0,)'),
        417: ('拥有者指定状态计数(7064)*1+0', '(417,7064,1,0,)'),
        418: ('状态添加者(生命上限)*1%+0', '(418,"HPMax",1,0,)'),
        419: ('状态计数*状态拥有者(生命上限)*1%+0', '(419,"HPMax",1,0,)'),
        420: ('状态计数*1+拥有者指定状态计数(7064)*1+0', '(420,1,7064,1,0,)'),
        421: ('受击者指定状态计数(7064)*1+0', '(421,7064,1,0,)'),
        505: ('武器弹夹容量*100%+200', '(505,100,200,)'),
        507: ('道具堆叠数*100%+0', '(507,100,0,)'),
        508: ('10000*0.9^(道具堆叠数-0)+-10000', '(508,10000,0.9,0,-10000,)'),
        509: ('武器(攻击力)*100%+50', '(509,"Att",100,50,)'),
        510: ('双子武器(攻击力)*100%+50', '(510,"Att",100,50,)'),
        511: ('武器当前子弹数*50%+10', '(511,50,10,)') }
    mkparser.g_EditorParser.CustomParserInfo()
    sText = '==================#r'
    for k in g_FormulaFunc:
        if k not in TestList:
            sText += '#Rmissing check %d #n#r' % k
    
    for value in TestList.values():
        (sStr, sResult) = value
        sAnalyseResult = mkparser.defines.AnalyseFormula('测试', sStr)
        if sAnalyseResult != sResult:
            sText += '#Rerr at#n: %s => %s != %s #r\n' % (sStr, sResult, sAnalyseResult)
    
    if len(sText) <= 20:
        notify.GS2CMessage(who.m_ID, '#GOK#n')
    else:
        print(sText)
        notify.GS2CMessage(who.m_ID, sText)
