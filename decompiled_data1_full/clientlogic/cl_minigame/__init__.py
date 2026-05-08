# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_minigame/__init__.pyc
# RelativePath: clientlogic/cl_minigame/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

import cl_msgcenter
import cl_netattr
import cl_formula

class CMiniGameMgr(object):
    
    def __init__(self, oGame):
        self.m_Game = oGame
        self.m_MiniGameID = 0
        self.m_MGameOwner = { }
        self.m_MGamePlayer = { }
        self.m_MGame = { }
        self.m_Cache = { }
        self.m_ExcludeCacheMG = { }

    
    def InitAttention(self):
        oWarMgr = self.m_Game.m_WarMgr
        self.m_Game.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERONREADY, OnPlayerReady, 'MiniGamePlayerReady')

    
    def Release(self):
        oWarMgr = self.m_Game.m_WarMgr
        self.m_Game.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERONREADY, 'MiniGamePlayerReady')
        self.m_MGameOwner = { }
        self.m_MGamePlayer = { }
        for oMiniGame in self.m_MGame.values():
            oMiniGame.Recycle()
            oMiniGame.Release()
        
        self.m_MGame = { }
        for lstMiniGame in self.m_Cache.values():
            for oMiniGame in lstMiniGame:
                oMiniGame.Release()
            
        
        self.m_Cache = { }
        self.m_Game = None

    
    def ValidCache(self, iSID):
        return iSID not in self.m_ExcludeCacheMG

    
    def AddExcludeCacheMG(self, iSID):
        self.m_ExcludeCacheMG[iSID] = 1

    
    def NewMiniGameID(self):
        self.m_MiniGameID += 1
        return self.m_MiniGameID

    
    def NewMiniGame(self, iSID, iOwner, iPlayer, dExtInfo = None, iSource = 0):
        if dExtInfo is None:
            dExtInfo = { }
        if iPlayer in self.m_MGamePlayer:
            return None
        oGame = self.m_Game
        clsData = oGame.m_WarData.GetMiniGameData(iSID)
        if not clsData:
            return None
        iMiniGameID = self.NewMiniGameID()
        if iSID not in self.m_Cache or not self.m_Cache[iSID]:
            oMiniGame = clsData.CheckShiftGameClass(oGame, iOwner)(oGame)
        else:
            oMiniGame = self.m_Cache[iSID].pop()
        clsData.InitGame(oMiniGame)
        oMiniGame.Init(iMiniGameID, iOwner, iPlayer, iSource, dExtInfo)
        oMiniGame.OnInit()
        if iOwner not in self.m_MGameOwner:
            self.m_MGameOwner[iOwner] = { }
        self.m_MGameOwner[iOwner][iMiniGameID] = iPlayer
        self.m_MGame[iMiniGameID] = oMiniGame
        return oMiniGame

    
    def DeleteMiniGame(self, oMiniGame):
        iMiniGameID = oMiniGame.m_ID
        if iMiniGameID not in self.m_MGame:
            return None
        self.m_MGame.pop(iMiniGameID)
        iOwner = oMiniGame.m_Owner
        iPlayer = self.m_MGameOwner[iOwner][iMiniGameID]
        self.PlayerLeaveMiniGame(iPlayer, iMiniGameID)
        self.m_MGameOwner[iOwner].pop(iMiniGameID)
        if not self.m_MGameOwner[iOwner]:
            self.m_MGameOwner.pop(iOwner)
        iSID = oMiniGame.m_SID
        if not self.ValidCache(iSID):
            oMiniGame.Release()
            return None
        oMiniGame.Recycle()
        if iSID not in self.m_Cache:
            self.m_Cache[iSID] = []
        self.m_Cache[iSID].append(oMiniGame)

    
    def DeleteOwnerMiniGame(self, iOwner):
        if iOwner not in self.m_MGameOwner:
            return None
        lstDel = list(self.m_MGameOwner[iOwner].keys())
        for iMiniGameID in lstDel:
            oMiniGame = self.GetMiniGame(iMiniGameID)
            self.DeleteMiniGame(oMiniGame)
        

    
    def PlayerEnterMiniGame(self, iPlayer, iMiniGameID):
        if iMiniGameID not in self.m_MGame:
            return None
        self.m_MGamePlayer[iPlayer] = iMiniGameID

    
    def PlayerLeaveMiniGame(self, iPlayer, iMiniGameID):
        if iPlayer in self.m_MGamePlayer and self.m_MGamePlayer[iPlayer] == iMiniGameID:
            self.m_MGamePlayer.pop(iPlayer)

    
    def GetMiniGame(self, iMiniGameID):
        if iMiniGameID not in self.m_MGame:
            return None
        return self.m_MGame[iMiniGameID]

    
    def GetMiniGameByPlayer(self, iPlayerID):
        if iPlayerID not in self.m_MGamePlayer:
            return None
        iMiniGameID = self.m_MGamePlayer[iPlayerID]
        return self.GetMiniGame(iMiniGameID)

    
    def GetPlayerMiniGameByOwner(self, iOwner, iPlayerID):
        if iOwner not in self.m_MGameOwner:
            return None
        dMGameData = self.m_MGameOwner[iOwner]
        for iMiniGameID, iMiniGamePlayer in dMGameData.items():
            if iMiniGamePlayer == iPlayerID:
                return self.GetMiniGame(iMiniGameID)
        

    
    def OnPlayerReady(self, dInfo):
        pid = dInfo['pid']
        oMiniGame = self.GetMiniGameByPlayer(pid)
        if oMiniGame:
            oMiniGame.OnPlayerReady()



def NewMiniGame(oGame, iSID, iOwenr, iPlayer, dExtInfo = None, iSource = 0):
    return oGame.m_MiniGameMgr.NewMiniGame(iSID, iOwenr, iPlayer, dExtInfo, iSource)


def OnPlayerReady(oWarMgr, oTarget, dInfo):
    oMiniGameMgr = oWarMgr.m_Game.m_MiniGameMgr
    oMiniGameMgr.OnPlayerReady(dInfo)


def GetMiniGameTimes(oGame, iRatio, iOriTimes, oOwner, oMaster, iMiniGame, iSource = 0):
    clsData = oGame.m_WarData.GetMiniGameData(iMiniGame)
    if not clsData:
        return 0
    iRatio = cl_formula.GetFormulaResult(oOwner, iRatio, { })
    dData = {
        'AID': oOwner.m_ID,
        'MiniGameType': clsData.m_Type,
        'Source': iSource,
        'Ratio': iRatio,
        'OriTimes': iOriTimes,
        'OverflowTimes': 0 }
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GETMINIGAMETIME, oMaster, dData, oGame = oGame)
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_OWNERGETMINIGAMETIME, oOwner, dData, oGame = oGame)
    iNewRatio = dData['Ratio']
    iNewOriTimes = dData['OriTimes']
    iTimes = dData['OverflowTimes']
    for _ in range(iNewOriTimes):
        if oGame.Random(10000) < iNewRatio:
            iTimes += 1
    
    return iTimes


def MiniGameAttrInfo(oMiniGameItem, iPropType, dInfo = None):
    lstAttrInfo = []
    for sAttr in cl_netattr.INFO_OBJECT_INIT[iPropType]:
        (iIdx, _, iType, iLen, iMode) = cl_netattr.INFO_PROP_NAME[sAttr]
        if dInfo and sAttr in dInfo:
            iValue = dInfo[sAttr]
        else:
            iValue = cl_netattr.GetPropValue(oMiniGameItem, sAttr, iMode)
        if iValue is None:
            continue
        lstAttrInfo.append((iIdx, iType, iLen, iValue))
    
    return lstAttrInfo


def MiniGameRelicAttrInfo(oMiniGameItem, iLevel, oGame = None):
    lstAttrInfo = []
    for sAttr in cl_netattr.INFO_OBJECT_INIT[cl_netattr.PROP_RELIC]:
        (iIdx, _, iType, iLen, iMode) = cl_netattr.INFO_PROP_NAME[sAttr]
        if sAttr == 'Level':
            iValue = iLevel
        else:
            iValue = cl_netattr.GetPropValue(oMiniGameItem, sAttr, iMode, oGame)
        if iValue is None:
            continue
        lstAttrInfo.append((iIdx, iType, iLen, iValue))
    
    return lstAttrInfo

