# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_putdata.pyc
# RelativePath: clientlogic/cl_putdata.pyc
# Source Generated with Decompyle++
# File: cl_putdata.pyc (Python 3.6)

import cl_platformdata
import cl_hero.load
from cl_commondefines import PUT_HERO, PUT_WEAPON, PUT_RELIC, PUT_MONSTERRELIC, PUT_BENEDICTION
import cllib.lib_flag
g_StaticPutInfo = { }
g_InterTestInfo = { }
g_PutInfo = { }
g_InterTestInfo[PUT_HERO] = cl_hero.load.GetInternalPutHero()
g_InterTestInfo[PUT_WEAPON] = cl_platformdata.GetWeaponInternalPut()
g_InterTestInfo[PUT_RELIC] = cl_platformdata.GetRelicInternalPut()
g_InterTestInfo[PUT_MONSTERRELIC] = cl_platformdata.GetMonsterRelicInternalPut()
g_InterTestInfo[PUT_BENEDICTION] = cl_platformdata.GetBenedictionPut()
g_PutInfo[PUT_HERO] = cl_hero.load.GetHeroPut()
g_PutInfo[PUT_WEAPON] = cl_platformdata.GetWeaponPut()
g_PutInfo[PUT_RELIC] = cl_platformdata.GetRelicPut()
g_PutInfo[PUT_MONSTERRELIC] = cl_platformdata.GetMonsterRelicPut()
g_PutInfo[PUT_BENEDICTION] = cl_platformdata.GetBenedictionPut()

def GetPutState(iType, iSID):
    if iType not in g_PutInfo or iSID not in g_PutInfo[iType]:
        return 0
    if iType in g_StaticPutInfo and iSID in g_StaticPutInfo[iType]:
        return g_StaticPutInfo[iType][iSID]
    iState = g_PutInfo[iType][iSID]
    if not iState and iSID in g_InterTestInfo[iType]:
        if cllib.lib_flag.g_IsInternalRun:
            return 1
        return 0
    return iState


def GetNewPutState(iType, iSID):
    if not cllib.lib_flag.g_IsStableRun:
        if iType not in g_InterTestInfo or iSID not in g_InterTestInfo[iType]:
            return 0
        return 1
    if iType not in g_PutInfo or iSID not in g_PutInfo[iType]:
        return 0
    if iType in g_StaticPutInfo and iSID in g_StaticPutInfo[iType]:
        return g_StaticPutInfo[iType][iSID]
    return g_PutInfo[iType][iSID]

g_Different = { }
g_AllPutHero = []
g_AllPutWeapon = []
g_AllPutRelic = []
g_AllPutCurseRelic = []
g_AllPutMonsterRelic = set()

def GetDifferentInfo():
    return g_Different


def GetAllPutHero():
    return g_AllPutHero


def GetAllPutWeapon():
    return g_AllPutWeapon


def GetAllPutRelic():
    return g_AllPutRelic


def GetAllPutCurseRelic():
    return g_AllPutCurseRelic


def GetAllPutMonsterRelic():
    return g_AllPutMonsterRelic


def RefreshDifferentInfo():
    global g_Different
    g_Different = { }
    for iType, dPutInfo in g_PutInfo.items():
        g_Different[iType] = { }
        if iType == PUT_BENEDICTION:
            for iSID, iPutState in dPutInfo.items():
                g_Different[iType][iSID] = iPutState
            
        oFunc = GetNewPutState if iType == PUT_WEAPON else GetPutState
        for iSID, iPutState in dPutInfo.items():
            iServerState = oFunc(iType, iSID)
            if iServerState == iPutState:
                continue
            g_Different[iType][iSID] = iServerState
        
    


def RefreshAllPutHero():
    global g_AllPutHero
    g_AllPutHero = []
    for iSID in g_PutInfo[PUT_HERO]:
        if not GetPutState(PUT_HERO, iSID):
            continue
        g_AllPutHero.append(iSID)
    


def RefreshAllPutWeapon():
    global g_AllPutWeapon
    g_AllPutWeapon = []
    for iSID in g_PutInfo[PUT_WEAPON]:
        if not GetNewPutState(PUT_WEAPON, iSID):
            continue
        g_AllPutWeapon.append(iSID)
    


def RefreshAllPutRelic():
    global g_AllPutRelic, g_AllPutCurseRelic
    g_AllPutRelic = []
    g_AllPutCurseRelic = []
    setNormalNoPutRelic = cl_platformdata.GetNormalNoPutRelic()
    for iSID in g_PutInfo[PUT_RELIC]:
        if not GetPutState(PUT_RELIC, iSID):
            continue
        if iSID in setNormalNoPutRelic:
            continue
        g_AllPutRelic.append(iSID)
        if iSID in cl_platformdata.GetCurseRelic():
            g_AllPutCurseRelic.append(iSID)
    


def RefreshAllPutMonsterRelic():
    global g_AllPutMonsterRelic
    lstPutMonsterRelic = []
    for iSID in g_PutInfo[PUT_MONSTERRELIC]:
        if not GetPutState(PUT_MONSTERRELIC, iSID):
            continue
        lstPutMonsterRelic.append(iSID)
    
    g_AllPutMonsterRelic = set(lstPutMonsterRelic)


def Init():
    RefreshDifferentInfo()
    RefreshAllPutHero()
    RefreshAllPutWeapon()
    RefreshAllPutRelic()
    RefreshAllPutMonsterRelic()


def R_LSPutChange(resfunc, dPut):
    for (iType, iSID), iPut in dPut.items():
        if iType not in g_StaticPutInfo:
            g_StaticPutInfo[iType] = { }
        g_StaticPutInfo[iType][iSID] = iPut
    
    Init()

