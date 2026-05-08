# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_seasonplay/season7/s7goodsdata.pyc
# RelativePath: clientlogic/cl_seasonplay/season7/s7goodsdata.pyc
# Source Generated with Decompyle++
# File: s7goodsdata.pyc (Python 3.6)

from cl_only import Functor, ChooseKey
from cl_platformdata import GetModuleByMaxPoint, GetTargetPointCrystal, GetS7CrystalByType, GetAllS7Module, GetS7ModuleByTag, GetModuleTag, GetS7ModuleByTag, GetCrystalTypePoint
from cl_cscommondef import QUALITY_NORMAL
from cl_object.logging import BackpackLog
from . import GetCrystalPerformCls
import cl_formula

class CS7GoodsData(object):
    m_SID = 0
    m_Name = ''
    m_InternalGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 0
    m_ShowMaxPoint = 0


def GetRandomModule(oGame, oHero, iAddModuleTagWeight, dChooseModule, dHasMaxModule, dHasChooseModule, dExcludeType = None, dHistoryChooseModule = None, dModuleOrderWeight = None):
    dResultModule = { }
    dAllModule = oHero.m_BackpackCon.GetUnLockModule()
    dExcludeModule = { }
    if dExcludeType:
        dNowTag = { }
        for oModule in oHero.m_BackpackCon.m_Module.values():
            dTag = GetModuleTag(oModule.m_SID)
            dNowTag.update(dTag)
        
        setExclude = set(dExcludeType) - set(dNowTag)
        for iTag in setExclude:
            dExcludeModule.update(GetS7ModuleByTag(iTag))
        
    if dHistoryChooseModule is None:
        dHistoryChooseModule = { }
        setHistoryChooseModule = set()
    else:
        setHistoryChooseModule = set(dHistoryChooseModule) - set(dHasChooseModule)
    dRecordExcludeModule = { }
    dRecordHasMaxModule = { }
    if dModuleOrderWeight is None:
        dModuleOrderWeight = { }
    for iModule, iQuality in dChooseModule:
        if iModule not in dAllModule:
            continue
        if (iModule, iQuality) in dHasChooseModule or (iModule, iQuality) in setHistoryChooseModule:
            continue
        if (iModule, iQuality) in dHasMaxModule:
            dRecordHasMaxModule[(iModule, iQuality)] = 1
            continue
        if dExcludeType and iModule in dExcludeModule:
            dRecordExcludeModule[(iModule, iQuality)] = 1
            continue
        dResultModule[(iModule, iQuality)] = 1
    
    for iModule, iQuality in list(dResultModule):
        if iModule in dModuleOrderWeight:
            dResultModule[(iModule, iQuality)] = dModuleOrderWeight[iModule]
            continue
        iThisAddHasModule = cl_formula.GetResultByData(oHero, iAddModuleTagWeight, {
            'Module': iModule,
            'ModuleInfo': dResultModule })
        dResultModule[(iModule, iQuality)] = 100 + iThisAddHasModule
    
    if not dResultModule:
        if dRecordExcludeModule:
            for iModule, iQuality in dRecordExcludeModule:
                dResultModule[(iModule, iQuality)] = 100
            
        elif setHistoryChooseModule:
            for iModule, iQuality in setHistoryChooseModule:
                dResultModule[(iModule, iQuality)] = 100
            
        else:
            for iModule, iQuality in dRecordHasMaxModule:
                dResultModule[(iModule, iQuality)] = 100
            
    return ChooseKey(oGame, dResultModule)


def GetRandomCrystal(oGame, dChooseCrystal, dFilterCrystal, dExclusionCrystal):
    dResultCrystal = { }
    for iCrystal, iWeight in dChooseCrystal.items():
        if iCrystal in dFilterCrystal or iCrystal in dExclusionCrystal:
            continue
        dResultCrystal[iCrystal] = iWeight
    
    if not dResultCrystal:
        BackpackLog.Alert('%s choose resultcrystal err %s %s %s' % (oGame.m_ID, dChooseCrystal, dFilterCrystal, dExclusionCrystal))
        for iCrystal, iWeight in dChooseCrystal.items():
            if iCrystal in dFilterCrystal:
                continue
            dResultCrystal[iCrystal] = iWeight
        
        if not dResultCrystal:
            return 0
    return ChooseKey(oGame, dResultCrystal)


def ChooseModuleByPoint(dPoint, iAddTagWeight, dExcludeTag, dModuleOrderWeight, oGame, oHero, dHasChooseModule, dHistoryChooseModule, dCacheModuleInfo):
    iPoint = ChooseKey(oGame, dPoint)
    dAllModule = GetModuleByMaxPoint(iPoint)
    if not dAllModule:
        return ()
    oBackpackCon = oHero.m_BackpackCon
    dHasMaxModule = oBackpackCon.GetMaxModule()
    tResult = GetRandomModule(oGame, oHero, iAddTagWeight, dAllModule, dHasMaxModule, dHasChooseModule, dExcludeTag, dHistoryChooseModule = dHistoryChooseModule, dModuleOrderWeight = dModuleOrderWeight)
    if not tResult:
        if dCacheModuleInfo:
            tResult = ChooseKey(oGame, dCacheModuleInfo)
            for iModuleSID in dCacheModuleInfo:
                if iModuleSID in dHistoryChooseModule:
                    dHistoryChooseModule.pop(iModuleSID, 0)
            
        if not tResult:
            return ()
    return tResult


def ChooseCrystalByTypeAndPointRange(tCrystalType, iMinPoint, iMaxPoint, oGame, oHero, dFilterCrystal):
    dTargetTypeCrystal = { }
    for iCrystalType in tCrystalType:
        dTargetTypeCrystal.update(GetS7CrystalByType(iCrystalType))
    
    if not dTargetTypeCrystal:
        return ()
    dTotalPoint = { 1: iPoint for iPoint in range(iMinPoint, iMaxPoint + 1) }
    iTotalPoint = ChooseKey(oGame, dTotalPoint)
    if iTotalPoint <= 0:
        BackpackLog.Alert('%s %s not crystalgood point %s %s' % (oGame.m_ID, oHero.m_PlayerID, iMinPoint, iMaxPoint))
        return ()
    dTargetPointCrystal = GetTargetPointCrystal(iTotalPoint)
    if not dTargetPointCrystal:
        return ()
    oBackpackCon = oHero.m_BackpackCon
    dAllCrystal = oHero.m_BackpackCon.GetUnLockCrystal()
    dResult = { 1: iCrystalSID for iCrystalSID in set(dTargetTypeCrystal) & set(dTargetPointCrystal) & set(dAllCrystal) }
    dExclusionCrystal = oBackpackCon.GetExclusionCrystal()
    iChooseCrystal = GetRandomCrystal(oGame, dResult, dFilterCrystal, dExclusionCrystal)
    if not iChooseCrystal:
        iChooseCrystal = ChooseKey(oGame, dFilterCrystal)
        if not iChooseCrystal:
            return ()
        clsCrystalData = GetCrystalPerformCls(iChooseCrystal)
        if not clsCrystalData:
            BackpackLog.Alert('%s %s not crystalgood %s' % (oGame.m_ID, oHero.m_PlayerID, iChooseCrystal))
            return ()
        iTotalPoint = ChooseKey(oGame, clsCrystalData.m_CanChoosePoint)
    return (iChooseCrystal, iTotalPoint)


def GetModuleByPointAndTag(iPoint, dTag, dExcludeModule, oGame, oHero):
    oBackpackCon = oHero.m_BackpackCon
    if not oBackpackCon:
        return []
    dGetModule = { }
    dModuleByPoint = GetModuleByMaxPoint(iPoint)
    dGetModule.update(dModuleByPoint)
    for iTag in dTag:
        dModule = GetS7ModuleByTag(iTag)
        dModuleByTag = { QUALITY_NORMAL: (iModuleSID, QUALITY_NORMAL) for iModuleSID in dModule }
        dGetModule.update(dModuleByTag)
    
    if not dGetModule:
        return []
    lstGetModule = []
    dAllModule = oBackpackCon.GetUnLockModule()
    for iModule, iQuality in dGetModule:
        if iModule not in dAllModule:
            continue
        if iModule in dExcludeModule:
            continue
        lstGetModule.append((iModule, iQuality))
    
    return lstGetModule


def ChooseCrystalWeightConfig(dCrystalConfig, oGame, oHero, dFilterCrystal):
    if not dCrystalConfig:
        return ()
    dChooseCrystalWeight = { }
    oBackpackCon = oHero.m_BackpackCon
    dAllUnlockCrystal = oHero.m_BackpackCon.GetUnLockCrystal()
    dExclusionCrystal = oBackpackCon.GetExclusionCrystal()
    dCrystalTypePoint = GetCrystalTypePoint()
    dChooseCrystal = { }
    dBackupChooseCrystal = { }
    for iCrystalType, dPointWeight in dCrystalConfig.items():
        if iCrystalType not in dCrystalTypePoint:
            continue
        dCrystalPoint = dCrystalTypePoint[iCrystalType]
        for iPoint in dPointWeight:
            if iPoint not in dCrystalPoint:
                continue
            lstCrystal = dCrystalPoint[iPoint]
            for iCrystalSID in lstCrystal:
                if iCrystalSID not in dAllUnlockCrystal:
                    continue
                tChoose = (iCrystalSID, iPoint)
                if iCrystalSID in dExclusionCrystal:
                    dBackupChooseCrystal[tChoose] = 100
                    continue
                if tChoose in dFilterCrystal:
                    continue
                if iCrystalType not in dChooseCrystal:
                    dChooseCrystal[iCrystalType] = { }
                if iPoint not in dChooseCrystal[iCrystalType]:
                    dChooseCrystal[iCrystalType][iPoint] = { }
                dChooseCrystal[iCrystalType][iPoint][iCrystalSID] = 100
            
        
    
    for iCrystalType, dPointWeight in dCrystalConfig.items():
        if iCrystalType not in dChooseCrystal:
            continue
        for iPoint, iWeight in dPointWeight.items():
            if iPoint not in dChooseCrystal[iCrystalType]:
                continue
            dChooseCrystalWeight[(iCrystalType, iPoint)] = iWeight
        
    
    if not dChooseCrystalWeight:
        if dFilterCrystal:
            return ChooseKey(oGame, dFilterCrystal)
        if dBackupChooseCrystal:
            return ChooseKey(oGame, dBackupChooseCrystal)
        BackpackLog.Alert('%s %s not crystalpackgood %s %s %s %s %s' % (oGame.m_ID, oHero.m_PlayerID, dCrystalConfig, dFilterCrystal, dBackupChooseCrystal, dExclusionCrystal, dAllUnlockCrystal))
        return ()
    (iCrystalType, iPoint) = ChooseKey(oGame, dChooseCrystalWeight)
    iCrystalSID = ChooseKey(oGame, dChooseCrystal[iCrystalType][iPoint])
    return (iCrystalSID, iPoint)

from cl_commondefines import CRTSTAL_FIVEDIR, CRTSTAL_ONEDIR, CRTSTAL_RAWMATERIAL, CRTSTAL_TWODIR, S7GOODS_ALL_DEPOLY, S7GOODS_SINGLE_DEPOLY, S7MODULE_TAG_BLOOM, S7MODULE_TAG_FIRESTONE, S7MODULE_TAG_THUNDERKNIFE, S7MODULE_TAG_TOXICFOG
from cl_newformula import Func836, Func855

class CS7GoodsData1001(CS7GoodsData):
    m_SID = 1001
    m_Name = '10点组件全选包（准备室自选）'
    m_GoodsDataType = S7GOODS_ALL_DEPOLY
    m_InternalGoodRule = (Functor(GetModuleByPointAndTag, 10, { }, {
        2120: 0 }),)
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 0
    m_ShowMaxPoint = 0


class CS7GoodsData1002(CS7GoodsData):
    m_SID = 1002
    m_Name = '6/8组件包（常规）'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseModuleByPoint, {
        6: 50,
        8: 50 }, (lambda *a: min(int(Func836(*a) * 1500), 1500) // Func855(*a, **{
'iDefault': 1 })), {
        S7MODULE_TAG_BLOOM: 0,
        S7MODULE_TAG_TOXICFOG: 0,
        S7MODULE_TAG_THUNDERKNIFE: 0,
        S7MODULE_TAG_FIRESTONE: 0 }, {
        2120: 0 }), Functor(ChooseModuleByPoint, {
        6: 50,
        8: 50 }, (lambda *a: min(int(Func836(*a) * 750), 750) // Func855(*a, **{
'iDefault': 1 })), {
        S7MODULE_TAG_BLOOM: 0,
        S7MODULE_TAG_TOXICFOG: 0,
        S7MODULE_TAG_THUNDERKNIFE: 0,
        S7MODULE_TAG_FIRESTONE: 0 }, {
        2120: 0 }), Functor(ChooseModuleByPoint, {
        6: 50,
        8: 50 }, 0, {
        S7MODULE_TAG_BLOOM: 0,
        S7MODULE_TAG_TOXICFOG: 0,
        S7MODULE_TAG_THUNDERKNIFE: 0,
        S7MODULE_TAG_FIRESTONE: 0 }, {
        2120: 0 }), Functor(ChooseModuleByPoint, {
        6: 50,
        8: 50 }, 0, {
        S7MODULE_TAG_BLOOM: 0,
        S7MODULE_TAG_TOXICFOG: 0,
        S7MODULE_TAG_THUNDERKNIFE: 0,
        S7MODULE_TAG_FIRESTONE: 0 }, {
        2120: 0 }))
    m_ExtraGoodRule = (Functor(ChooseModuleByPoint, {
        6: 50,
        8: 50 }, 0, {
        S7MODULE_TAG_BLOOM: 0,
        S7MODULE_TAG_TOXICFOG: 0,
        S7MODULE_TAG_THUNDERKNIFE: 0,
        S7MODULE_TAG_FIRESTONE: 0 }, {
        2120: 0 }), Functor(ChooseModuleByPoint, {
        6: 50,
        8: 50 }, 0, {
        S7MODULE_TAG_BLOOM: 0,
        S7MODULE_TAG_TOXICFOG: 0,
        S7MODULE_TAG_THUNDERKNIFE: 0,
        S7MODULE_TAG_FIRESTONE: 0 }, {
        2120: 0 }))
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 0


class CS7GoodsData1003(CS7GoodsData):
    m_SID = 1003
    m_Name = '8/10组件包（BOSS关）'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseModuleByPoint, {
        8: 50,
        6: 50 }, (lambda *a: min(int(Func836(*a) * 1500), 1500) // Func855(*a, **{
'iDefault': 1 })), {
        S7MODULE_TAG_BLOOM: 0,
        S7MODULE_TAG_TOXICFOG: 0,
        S7MODULE_TAG_THUNDERKNIFE: 0,
        S7MODULE_TAG_FIRESTONE: 0 }, {
        2120: 0 }), Functor(ChooseModuleByPoint, {
        8: 50,
        6: 50 }, (lambda *a: min(int(Func836(*a) * 750), 750) // Func855(*a, **{
'iDefault': 1 })), {
        S7MODULE_TAG_BLOOM: 0,
        S7MODULE_TAG_TOXICFOG: 0,
        S7MODULE_TAG_THUNDERKNIFE: 0,
        S7MODULE_TAG_FIRESTONE: 0 }, {
        2120: 0 }), Functor(ChooseModuleByPoint, {
        8: 100 }, 0, {
        S7MODULE_TAG_BLOOM: 0,
        S7MODULE_TAG_TOXICFOG: 0,
        S7MODULE_TAG_THUNDERKNIFE: 0,
        S7MODULE_TAG_FIRESTONE: 0 }, {
        2120: 0 }), Functor(ChooseModuleByPoint, {
        8: 100 }, 0, {
        S7MODULE_TAG_BLOOM: 0,
        S7MODULE_TAG_TOXICFOG: 0,
        S7MODULE_TAG_THUNDERKNIFE: 0,
        S7MODULE_TAG_FIRESTONE: 0 }, {
        2120: 0 }))
    m_ExtraGoodRule = (Functor(ChooseModuleByPoint, {
        10: 100 }, 0, { }, { }), Functor(ChooseModuleByPoint, {
        8: 50,
        6: 50 }, 0, {
        S7MODULE_TAG_BLOOM: 0,
        S7MODULE_TAG_TOXICFOG: 0,
        S7MODULE_TAG_THUNDERKNIFE: 0,
        S7MODULE_TAG_FIRESTONE: 0 }, { }), Functor(ChooseModuleByPoint, {
        8: 50,
        6: 50 }, 0, {
        S7MODULE_TAG_BLOOM: 0,
        S7MODULE_TAG_TOXICFOG: 0,
        S7MODULE_TAG_THUNDERKNIFE: 0,
        S7MODULE_TAG_FIRESTONE: 0 }, { }), Functor(ChooseModuleByPoint, {
        10: 100 }, 0, { }, { }))
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 0


class CS7GoodsData1050(CS7GoodsData):
    m_SID = 1050
    m_Name = '水晶商品-素材'
    m_GoodsDataType = S7GOODS_ALL_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalByTypeAndPointRange, (CRTSTAL_RAWMATERIAL,), 1, 1),)
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 0
    m_ShowMaxPoint = 0


class CS7GoodsData1051(CS7GoodsData):
    m_SID = 1051
    m_Name = '水晶商品-1点'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            1: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            1: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            1: 100 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 0
    m_ShowMaxPoint = 1


class CS7GoodsData1052(CS7GoodsData):
    m_SID = 1052
    m_Name = '水晶商品-2点'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            2: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            2: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            2: 100 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 2


class CS7GoodsData1053(CS7GoodsData):
    m_SID = 1053
    m_Name = '水晶商品-3点'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            3: 50 },
        CRTSTAL_ONEDIR: {
            3: 50 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            3: 50 },
        CRTSTAL_ONEDIR: {
            3: 50 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            3: 50 },
        CRTSTAL_ONEDIR: {
            3: 50 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 3


class CS7GoodsData1054(CS7GoodsData):
    m_SID = 1054
    m_Name = '水晶商品-4点'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            4: 50 },
        CRTSTAL_ONEDIR: {
            4: 50 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            4: 50 },
        CRTSTAL_ONEDIR: {
            4: 50 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            4: 50 },
        CRTSTAL_ONEDIR: {
            4: 50 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 4


class CS7GoodsData1055(CS7GoodsData):
    m_SID = 1055
    m_Name = '水晶商品-5点'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            5: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            5: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            5: 100 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 5


class CS7GoodsData1056(CS7GoodsData):
    m_SID = 1056
    m_Name = '水晶商品-6点'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            6: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            6: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            6: 100 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 6


class CS7GoodsData1057(CS7GoodsData):
    m_SID = 1057
    m_Name = '水晶商品-7点'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            7: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            7: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            7: 100 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 7


class CS7GoodsData1058(CS7GoodsData):
    m_SID = 1058
    m_Name = '水晶商品-8点'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            8: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            8: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            8: 100 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 8


class CS7GoodsData1059(CS7GoodsData):
    m_SID = 1059
    m_Name = '水晶商品-9点'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            9: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            9: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            9: 100 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 9


class CS7GoodsData1060(CS7GoodsData):
    m_SID = 1060
    m_Name = '水晶商品-10点'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            10: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            10: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            10: 100 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 10


class CS7GoodsData1061(CS7GoodsData):
    m_SID = 1061
    m_Name = '水晶商品-11点'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            11: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            11: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            11: 100 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 11


class CS7GoodsData1062(CS7GoodsData):
    m_SID = 1062
    m_Name = '水晶商品-12点'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            12: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            12: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            12: 100 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 12


class CS7GoodsData1063(CS7GoodsData):
    m_SID = 1063
    m_Name = 'BOSS水晶-6点'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            6: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            6: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            6: 100 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 6


class CS7GoodsData1064(CS7GoodsData):
    m_SID = 1064
    m_Name = 'BOSS水晶-7点'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            7: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            7: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            7: 100 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 7


class CS7GoodsData1065(CS7GoodsData):
    m_SID = 1065
    m_Name = 'BOSS水晶-8点'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            8: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            8: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            8: 100 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 8


class CS7GoodsData1066(CS7GoodsData):
    m_SID = 1066
    m_Name = 'BOSS水晶-9点'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            9: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            9: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            9: 100 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 9


class CS7GoodsData1067(CS7GoodsData):
    m_SID = 1067
    m_Name = 'BOSS水晶-10点'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            10: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            10: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            10: 100 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 10


class CS7GoodsData1068(CS7GoodsData):
    m_SID = 1068
    m_Name = 'BOSS水晶-11点'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            11: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            11: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            11: 100 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 11


class CS7GoodsData1069(CS7GoodsData):
    m_SID = 1069
    m_Name = 'BOSS水晶-12点'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            12: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            12: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            12: 100 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 12


class CS7GoodsData1070(CS7GoodsData):
    m_SID = 1070
    m_Name = 'BOSS水晶-13点'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            13: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            13: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            13: 100 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 13


class CS7GoodsData1071(CS7GoodsData):
    m_SID = 1071
    m_Name = 'BOSS水晶-14点'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            14: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            14: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            14: 100 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 14


class CS7GoodsData1072(CS7GoodsData):
    m_SID = 1072
    m_Name = 'BOSS水晶-15点'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            15: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            15: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            15: 100 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 15


class CS7GoodsData1073(CS7GoodsData):
    m_SID = 1073
    m_Name = '水晶商品-4点-一幕'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            4: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            4: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            4: 100 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 4


class CS7GoodsData1074(CS7GoodsData):
    m_SID = 1074
    m_Name = '水晶商品-3点-一幕'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            3: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            3: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            3: 100 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 3


class CS7GoodsData1103(CS7GoodsData):
    m_SID = 1103
    m_Name = '水晶商品-3点-6选项'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            3: 100 },
        CRTSTAL_ONEDIR: {
            3: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            3: 100 },
        CRTSTAL_ONEDIR: {
            3: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            3: 100 },
        CRTSTAL_ONEDIR: {
            3: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            3: 100 },
        CRTSTAL_ONEDIR: {
            3: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            3: 100 },
        CRTSTAL_ONEDIR: {
            3: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            3: 100 },
        CRTSTAL_ONEDIR: {
            3: 100 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 3


class CS7GoodsData1104(CS7GoodsData):
    m_SID = 1104
    m_Name = '水晶商品-4点-6选项'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            4: 100 },
        CRTSTAL_ONEDIR: {
            4: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            4: 100 },
        CRTSTAL_ONEDIR: {
            4: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            4: 100 },
        CRTSTAL_ONEDIR: {
            4: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            4: 100 },
        CRTSTAL_ONEDIR: {
            4: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            4: 100 },
        CRTSTAL_ONEDIR: {
            4: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            4: 100 },
        CRTSTAL_ONEDIR: {
            4: 100 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 4


class CS7GoodsData1105(CS7GoodsData):
    m_SID = 1105
    m_Name = '水晶商品-5点-6选项'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            5: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            5: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            5: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            5: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            5: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            5: 100 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 5


class CS7GoodsData1200(CS7GoodsData):
    m_SID = 1200
    m_Name = '水晶商品-一幕准备室'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            3: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            3: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            3: 100 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 3


class CS7GoodsData1201(CS7GoodsData):
    m_SID = 1201
    m_Name = '水晶商品-一幕（天赋0）'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            3: 20 },
        CRTSTAL_ONEDIR: {
            3: 80 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            3: 20 },
        CRTSTAL_ONEDIR: {
            3: 80 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            3: 20 },
        CRTSTAL_ONEDIR: {
            3: 80 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 3


class CS7GoodsData1202(CS7GoodsData):
    m_SID = 1202
    m_Name = '水晶商品-二幕（天赋0）'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            3: 20 },
        CRTSTAL_ONEDIR: {
            3: 80 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            3: 20 },
        CRTSTAL_ONEDIR: {
            3: 80 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            3: 20 },
        CRTSTAL_ONEDIR: {
            3: 80 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 3


class CS7GoodsData1203(CS7GoodsData):
    m_SID = 1203
    m_Name = '水晶商品-三幕（天赋0）'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            3: 20 },
        CRTSTAL_ONEDIR: {
            3: 80 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            3: 20 },
        CRTSTAL_ONEDIR: {
            3: 80 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            3: 20 },
        CRTSTAL_ONEDIR: {
            3: 80 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 3


class CS7GoodsData1204(CS7GoodsData):
    m_SID = 1204
    m_Name = '水晶商品-四幕（天赋0）'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            4: 20 },
        CRTSTAL_ONEDIR: {
            4: 80 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            4: 20 },
        CRTSTAL_ONEDIR: {
            4: 80 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            4: 20 },
        CRTSTAL_ONEDIR: {
            4: 80 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            4: 20 },
        CRTSTAL_ONEDIR: {
            4: 80 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            4: 20 },
        CRTSTAL_ONEDIR: {
            4: 80 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            4: 20 },
        CRTSTAL_ONEDIR: {
            4: 80 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 4


class CS7GoodsData1205(CS7GoodsData):
    m_SID = 1205
    m_Name = '水晶商品-一幕（天赋1）'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            2: 40,
            3: 10,
            4: 2 },
        CRTSTAL_ONEDIR: {
            3: 40,
            4: 8 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            2: 40,
            3: 10,
            4: 2 },
        CRTSTAL_ONEDIR: {
            3: 40,
            4: 8 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            2: 40,
            3: 10,
            4: 2 },
        CRTSTAL_ONEDIR: {
            3: 40,
            4: 8 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 4


class CS7GoodsData1206(CS7GoodsData):
    m_SID = 1206
    m_Name = '水晶商品-二幕（天赋1）'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            2: 30,
            3: 15,
            4: 2 },
        CRTSTAL_ONEDIR: {
            3: 45,
            4: 8 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            2: 30,
            3: 15,
            4: 2 },
        CRTSTAL_ONEDIR: {
            3: 45,
            4: 8 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            2: 30,
            3: 15,
            4: 2 },
        CRTSTAL_ONEDIR: {
            3: 45,
            4: 8 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 4


class CS7GoodsData1207(CS7GoodsData):
    m_SID = 1207
    m_Name = '水晶商品-三幕（天赋1）'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            3: 20,
            4: 4 },
        CRTSTAL_ONEDIR: {
            3: 60,
            4: 16 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            3: 20,
            4: 4 },
        CRTSTAL_ONEDIR: {
            3: 60,
            4: 16 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            3: 20,
            4: 4 },
        CRTSTAL_ONEDIR: {
            3: 60,
            4: 16 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 4


class CS7GoodsData1208(CS7GoodsData):
    m_SID = 1208
    m_Name = '水晶商品-四幕（天赋1）'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            4: 15 },
        CRTSTAL_ONEDIR: {
            4: 45,
            5: 40 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            4: 15 },
        CRTSTAL_ONEDIR: {
            4: 45,
            5: 40 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            4: 15 },
        CRTSTAL_ONEDIR: {
            4: 45,
            5: 40 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            4: 15 },
        CRTSTAL_ONEDIR: {
            4: 45,
            5: 40 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            4: 15 },
        CRTSTAL_ONEDIR: {
            4: 45,
            5: 40 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_TWODIR: {
            4: 15 },
        CRTSTAL_ONEDIR: {
            4: 45,
            5: 40 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 5


class CS7GoodsData1211(CS7GoodsData):
    m_SID = 1211
    m_Name = 'BOSS水晶-一幕天赋0'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            10: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            10: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            10: 100 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 10


class CS7GoodsData1212(CS7GoodsData):
    m_SID = 1212
    m_Name = 'BOSS水晶-一幕天赋1'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            10: 30,
            11: 40,
            12: 30 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            10: 30,
            11: 40,
            12: 30 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            10: 30,
            11: 40,
            12: 30 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 12


class CS7GoodsData1213(CS7GoodsData):
    m_SID = 1213
    m_Name = 'BOSS水晶-一幕天赋2'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            12: 30,
            13: 40,
            14: 20,
            15: 10 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            12: 30,
            13: 40,
            14: 20,
            15: 10 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            12: 30,
            13: 40,
            14: 20,
            15: 10 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 15


class CS7GoodsData1214(CS7GoodsData):
    m_SID = 1214
    m_Name = 'BOSS水晶-二幕'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            8: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            8: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            8: 100 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 8


class CS7GoodsData1215(CS7GoodsData):
    m_SID = 1215
    m_Name = 'BOSS水晶-三幕'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            8: 50 },
        CRTSTAL_FIVEDIR: {
            8: 50 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            8: 50 },
        CRTSTAL_FIVEDIR: {
            8: 50 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_ONEDIR: {
            8: 50 },
        CRTSTAL_FIVEDIR: {
            8: 50 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 8


class CS7GoodsData1216(CS7GoodsData):
    m_SID = 1216
    m_Name = 'BOSS水晶-四幕'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            8: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            8: 100 } }), Functor(ChooseCrystalWeightConfig, {
        CRTSTAL_FIVEDIR: {
            8: 100 } }))
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 1
    m_ShowMaxPoint = 8


class CS7GoodsData1217(CS7GoodsData):
    m_SID = 1217
    m_Name = '赛季挑战关卡奖励掉落模块'
    m_GoodsDataType = S7GOODS_SINGLE_DEPOLY
    m_InternalGoodRule = (Functor(ChooseModuleByPoint, {
        6: 50,
        8: 50 }, (lambda *a: min(int(Func836(*a) * 1000), 1000) // Func855(*a, **{
'iDefault': 1 })), {
        S7MODULE_TAG_BLOOM: 0,
        S7MODULE_TAG_TOXICFOG: 0,
        S7MODULE_TAG_THUNDERKNIFE: 0,
        S7MODULE_TAG_FIRESTONE: 0 }, {
        2120: 300 }),)
    m_ExtraGoodRule = ()
    m_RefreshCanRepeat = 0
    m_CanRefresh = 0
    m_ShowMaxPoint = 0

g_AllGoodsData = {
    1001: CS7GoodsData1001,
    1002: CS7GoodsData1002,
    1003: CS7GoodsData1003,
    1050: CS7GoodsData1050,
    1051: CS7GoodsData1051,
    1052: CS7GoodsData1052,
    1053: CS7GoodsData1053,
    1054: CS7GoodsData1054,
    1055: CS7GoodsData1055,
    1056: CS7GoodsData1056,
    1057: CS7GoodsData1057,
    1058: CS7GoodsData1058,
    1059: CS7GoodsData1059,
    1060: CS7GoodsData1060,
    1061: CS7GoodsData1061,
    1062: CS7GoodsData1062,
    1063: CS7GoodsData1063,
    1064: CS7GoodsData1064,
    1065: CS7GoodsData1065,
    1066: CS7GoodsData1066,
    1067: CS7GoodsData1067,
    1068: CS7GoodsData1068,
    1069: CS7GoodsData1069,
    1070: CS7GoodsData1070,
    1071: CS7GoodsData1071,
    1072: CS7GoodsData1072,
    1073: CS7GoodsData1073,
    1074: CS7GoodsData1074,
    1103: CS7GoodsData1103,
    1104: CS7GoodsData1104,
    1105: CS7GoodsData1105,
    1200: CS7GoodsData1200,
    1201: CS7GoodsData1201,
    1202: CS7GoodsData1202,
    1203: CS7GoodsData1203,
    1204: CS7GoodsData1204,
    1205: CS7GoodsData1205,
    1206: CS7GoodsData1206,
    1207: CS7GoodsData1207,
    1208: CS7GoodsData1208,
    1211: CS7GoodsData1211,
    1212: CS7GoodsData1212,
    1213: CS7GoodsData1213,
    1214: CS7GoodsData1214,
    1215: CS7GoodsData1215,
    1216: CS7GoodsData1216,
    1217: CS7GoodsData1217 }

def GetS7GoodsData(iSID):
    if iSID not in g_AllGoodsData:
        return None
    return g_AllGoodsData[iSID]

