# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/checkcheatelement.pyc
# RelativePath: clientlogic/cl_warmgr/checkcheatelement.pyc
# Source Generated with Decompyle++
# File: checkcheatelement.pyc (Python 3.6)

from cl_warmgr.mobject import CBaseElement
from cl_object.logging import CheatLog
import os
import re
import math
import cl_msgcenter
import cl_snetwar
import cllib.lib_flag
if cllib.lib_flag.g_IsLogicLayer:
    from clclient.clc_pyerror import g_PyError
g_UseSwitch = True

class CCheckCheatElement(CBaseElement):
    
    def __init__(self, oGame, nid, oData):
        super(CCheckCheatElement, self).__init__(oGame, nid, oData)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_CallFlag = 'WarMgr.CheckCheatElement'
        self.m_WatcherList = { }

    
    def Init(self):
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.InitPlayer, 'AddAllPlayer' + self.m_CallFlag, -1, 0)

    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, 'AddAllPlayer' + self.m_CallFlag)
        self.DoneAttention(self.m_WarMgr.GetAllHero())
        self.m_WarMgr = None
        self.m_WatcherList = { }
        super(CCheckCheatElement, self).Release()

    
    def InitPlayer(self, oWarMgr, dInfo):
        lstHero = oWarMgr.GetAllHero()
        for iHero in lstHero:
            self.m_WatcherList[iHero] = self.GetInitCashInfo(iHero)
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_ADDGSCASH, self.OnAddGSCash, 'CheckAddGSCash')
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_CONSUMEGSCASH, self.OnConsumeGSCash, 'CheckConsumeGSCash')
        

    
    def DoneAttention(self, lstHero):
        oWarMgr = self.m_WarMgr
        for iHero in lstHero:
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_ADDGSCASH, 'CheckAddGSCash')
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_CONSUMEGSCASH, 'CheckConsumeGSCash')
        

    
    def CheckLevelCash(self, iHero, iCash, iGSCash):
        oHero = self.m_Game.GetObject(iHero)
        if not self.NeedCheck(oHero):
            return None
        iOldGSCash = self.RestoreRandomValue(iHero, 'WarGSCash')
        if iGSCash != iOldGSCash:
            self.Cheat(oHero, 'level check illegal WarGSCash %s old:%s' % (iGSCash, iOldGSCash), iValidNotify = 1)

    
    def CheckPyErrorBusted(self, oHero):
        if 'g_PyError' not in globals():
            return None
        if not self.NeedCheck(oHero):
            return None
        if g_PyError.m_Busted:
            self.Cheat(oHero, 'pyerrEvidence', iValidNotify = 1)

    
    def CheckCashChange(self, oHero, dInfo, sType):
        iHero = oHero.m_ID
        if not self.NeedCheck(oHero):
            self.DoneAttention([
                iHero])
            return None
        iAdd = dInfo['Cash']
        iNow = dInfo['TotalCash']
        self.CheckCheatByThreshold(oHero, sType, iAdd)
        iRecordCash = self.RestoreRandomValue(iHero, sType)
        if iNow > iAdd + iRecordCash:
            iValidNotify = 1 if sType == 'WarGSCash' else 0
            self.Cheat(oHero, 'use illegal %s %s %s %s' % (sType, iNow, iRecordCash, iAdd), iValidNotify)
        else:
            self.m_WatcherList[iHero][sType] = self.GetRandomValue(iNow)

    
    def OnAddCash(self, oWarMgr, oHero, dInfo):
        self.CheckCashChange(oHero, dInfo, 'WarCash')

    
    def OnAddGSCash(self, oWarMgr, oHero, dInfo):
        self.CheckCashChange(oHero, dInfo, 'WarGSCash')

    
    def OnConsumeGSCash(self, oWarMgr, oHero, dInfo):
        dInfo['Cash'] = -dInfo['Cash']
        self.CheckCashChange(oHero, dInfo, 'WarGSCash')

    
    def GetInitCashInfo(self, iHero):
        oHero = self.m_Game.GetObject(iHero)
        if not oHero:
            return { }
        tCash = self.GetRandomValue(oHero.Cash())
        tGSCash = self.GetRandomValue(oHero.GSCash())
        return {
            'WarCash': tCash,
            'WarGSCash': tGSCash }

    
    def GetRandomValue(self, iVal):
        iRandom = 10 + self.m_Game.Random(999)
        return (iVal + iRandom, iRandom)

    
    def RestoreRandomValue(self, iHero, sType):
        if iHero not in self.m_WatcherList:
            return 0
        tRecord = self.m_WatcherList[iHero][sType]
        if len(tRecord) == 2:
            (iValue, iRandom) = tRecord
            return iValue - iRandom
        return 0

    
    def CheckCheatByThreshold(self, oHero, sType, iVal):
        if not self.NeedCheck(oHero):
            return None
        iThreshold = self.GetThreshold(sType)
        if iThreshold is not None and iThreshold < iVal:
            iValidNotify = 1 if sType == 'WarGSCash' else 0
            if sType == 'WarCash' and oHero.m_RelicCon.IsEnabled(5727):
                iValidNotify = 0
            self.Cheat(oHero, '%s val:%d t:%d' % (sType, iVal, iThreshold), iValidNotify)

    
    def UsePlugin(self, oHero):
        if not self.NeedCheck(oHero):
            return None
        self.Cheat(oHero, 'plug-in', iValidNotify = 0)

    
    def GetThreshold(self, sType):
        iPlayType = self.m_WarMgr.GetPlayType() if sType != 'Speed' else 0
        (iDifficulty, iRound) = self.m_WarMgr.GetWarDifficultyInfo()
        if sType in ('WarCash', 'Speed'):
            (iDifficulty, iRound) = (0, 0)
        return self.m_Game.GetWarData().GetThreshold(sType, iPlayType, iDifficulty, iRound)

    
    def NeedCheck(self, oHero):
        if oHero.IsCheat():
            return 0
        return 1

    
    def Cheat(self, oHero, sReason, iValidNotify = 0):
        pid = oHero.m_PlayerID
        oWarMgr = oHero.m_Game.m_WarMgr
        CheatLog.Warn('%d %d cheat %s' % (self.m_Game.m_ID, pid, sReason))
        oHero.Cheat()
        if cllib.lib_flag.g_IsStandaloneClient and not (cllib.lib_flag.g_IsAuthorityRun):
            ColletProgress(oHero)
            if pid != oWarMgr.GetWarMasterPlayer():
                return None
            CheatLog.Warn('%d forbidgame %s' % (pid, sReason))
            if iValidNotify and g_UseSwitch and not oWarMgr.IsSingleGame():
                cl_snetwar.GS2CConfirmCheat(pid, 1)



def GetComponentClass(oMgrManager):
    return CCheckCheatElement


def ColletProgress(oHero):
    lstPName = []
    
    try:
        lstLines = os.popen('tasklist /fo csv').readlines()
        lstLines = lstLines[1:]
    except:
        lstLines = []

    
    try:
        RE = re.compile('\\"(.+?)\\",.+')
        for sLine in lstLines:
            oMatch = RE.match(sLine)
            if oMatch:
                sName = oMatch.group(1)
                sName = sName.rstrip('.exe')
                if sName not in lstPName:
                    lstPName.append(sName)
        
        lstPName = sorted(lstPName)
    except:
        lstPName = []

    iMax = 100
    if not lstPName:
        lstPName = lstLines
        iMax = 20
    iSplit = math.ceil(len(lstPName) / iMax)
    for _ in range(iSplit):
        CheatLog.Info('%s %s' % (oHero.m_PlayerID, lstPName[:iMax]))
        lstPName = lstPName[iMax:]
        if not lstPName:
            break
    

