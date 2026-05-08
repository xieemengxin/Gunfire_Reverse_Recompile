# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_object/logging.pyc
# RelativePath: clientlogic/cl_object/logging.pyc
# Source Generated with Decompyle++
# File: logging.pyc (Python 3.6)

from cl_only import SendAlert, log_file, log_file_long, TimeStr, GetTraceText, PythonError
from cllib.lib_only import GetServerGroup
import time
import hashlib
import sys
import traceback
import cllib.lib_flag
if cllib.lib_flag.g_IsLogicLayer:
    import clclient.clc_rpc

class CLogging(object):
    m_AlertRecord = { }
    
    def __init__(self, sLogPath, iCloseAll = 0, iCloseDebug = 0, iServer = 1):
        self.m_LogPath = sLogPath
        if 'debug' in sLogPath:
            self.m_DebugPath = sLogPath
        else:
            self.m_DebugPath = 'debug/%s' % ''.join(sLogPath.split('/'))
        self.m_CloseAll = iCloseAll
        self.m_CloseDebug = iCloseDebug
        self.m_Server = iServer
        self.m_LocalWrite = 1

    
    def Switch(self, iCloseAll, iCloseDebug):
        self.m_CloseAll = iCloseAll
        self.m_CloseDebug = iCloseDebug

    
    def SwitchServerLog(self, iServer):
        self.m_Server = iServer

    
    def SwitchLocalWrite(self, iLocalWrite):
        self.m_LocalWrite = iLocalWrite

    
    def Error(self, sMsg):
        if self.m_CloseAll:
            return None
        self._Log('[Error]%s' % sMsg)
        SendAlert(self.m_LogPath, '%s [%s Error]' % (sMsg, self.m_LogPath))

    
    def Warn(self, sMsg):
        if self.m_CloseAll:
            return None
        self._Log('[Warn]%s' % sMsg)

    
    def Info(self, sMsg):
        if self.m_CloseAll:
            return None
        self._Log('[Info]%s' % sMsg)

    
    def Debug(self, sMsg):
        if self.m_CloseAll or self.m_CloseDebug:
            return None
        self._Log('[Debug]%s' % sMsg, iDebug = 1)

    
    def Raise(self, sMsg):
        if self.m_CloseAll:
            return None
        self._Log('[Rasie]%s' % sMsg)
        raise Exception(sMsg)

    
    def Alert(self, sMsg, bDelay = True):
        if self.m_CloseAll:
            return None
        self._Log('[Alert]%s' % sMsg)
        if self.m_LogPath in ('behavior',) and not (cllib.lib_flag.g_IsAuthorityRun):
            return None
        SendAlert(self.m_LogPath, '%s [%s Alert]' % (sMsg, self.m_LogPath))

    
    def TraceAlert(self, sMsg, iLimit = 43200):
        lstTraceText = GetTraceText()
        if self.CheckAlertLimet(''.join(lstTraceText), iLimit):
            return None
        self.Alert(sMsg)
        for sText in lstTraceText:
            log_file('err', sText)
        
        log_file('err', ' Msg: %s' % sMsg)

    
    def CheckAlertLimet(self, sMsg, iLimit = 86400):
        fNowTime = time.time()
        sMd5 = hashlib.md5(sMsg.encode('utf-8')).hexdigest()
        if sMd5 in self.m_AlertRecord and fNowTime - self.m_AlertRecord[sMd5] < iLimit:
            return True
        self.m_AlertRecord[sMd5] = int(fNowTime)
        return False

    
    def _Log(self, sMsg, iDebug = 0):
        sLogPath = self.m_DebugPath if iDebug else self.m_LogPath
        if self.m_LocalWrite:
            log_file(sLogPath, sMsg)
        if self.m_Server and cllib.lib_flag.g_IsLogicLayer:
            clclient.clc_rpc.CallFunc(0, 'myutil.logging.R_LogicLog', (sLogPath, TimeStr() + sMsg), None)



def Init():
    OldwarrewardLog.Switch(0, 1)
    if GetServerGroup() == 'interpressure':
        BehaviorLog.Switch(1, 1)
        LevelLog.Switch(1, 1)
        WarobjLog.Switch(1, 1)
    if cllib.lib_flag.g_IsLogicLayer:
        MoveLog.Switch(0, 1)
        SkillLog.Switch(0, 1)
        WarcashLog.SwitchLocalWrite(0)
        CrowdLog.Switch(1, 1)
        CashLog.SwitchLocalWrite(0)
    else:
        CrowdLog.Switch(0, 1)


def ClearTimeoutAlertRecord(iTimeout = 86400):
    for sMd5 in list(CLogging.m_AlertRecord.keys()):
        if time.time() - CLogging.m_AlertRecord[sMd5] > iTimeout:
            CLogging.m_AlertRecord.pop(sMd5)
    

if 'ErrLog' not in globals():
    ErrLog = CLogging('err')
    CashLog = CLogging('cash')
    GmRemotecmdLog = CLogging('gm/remotecmd')
    PacketLog = CLogging('packet')
    EvidenceLog = CLogging('evidence')
    PyextendLog = CLogging('pyextend')
    WarrelicLog = CLogging('warrelic')
    WartalentLog = CLogging('wartalent')
    WarbenedictionLog = CLogging('warbenediction')
    WarunlockprogressLog = CLogging('warunlockprogress')
    BehaviorLog = CLogging('behavior')
    SkillLog = CLogging('skill')
    WarobjLog = CLogging('warobj')
    WarshopLog = CLogging('warshop')
    OldwarrewardLog = CLogging('oldwarreward')
    WarrewardLog = CLogging('warreward')
    WarpayLog = CLogging('warpay')
    WarcashLog = CLogging('warcash')
    MoveLog = CLogging('move')
    SceneLog = CLogging('scene')
    LevelLog = CLogging('level')
    AutotestLog = CLogging('autotest')
    WarnpcLog = CLogging('warnpc')
    DieLog = CLogging('die')
    FightserverLog = CLogging('fightserver')
    CrowdLog = CLogging('crowdmove')
    LogicwarningLog = CLogging('logicwarning')
    SignalLog = CLogging('signal')
    CheatLog = CLogging('cheat')
    OptimizationLog = CLogging('optimization')
    CheekLog = CLogging('cheek')
    CgLog = CLogging('cg')
    OtherLog = CLogging('other')
    SuitLog = CLogging('suit')
    AchievementLog = CLogging('achievement')
    SurvivorLog = CLogging('survivor')
    WeaponstoreLog = CLogging('weaponstore')
    TaskLog = CLogging('task')
    EndlessLog = CLogging('endless')
    SeasonLog = CLogging('season')
    TeammateaiLog = CLogging('teammateai')
    RelictalentLog = CLogging('relictalent')
    DeviceLog = CLogging('device')
    PetLog = CLogging('pet')
    NewbietutorialLog = CLogging('newbietutorial')
    SeasonsuitLog = CLogging('seasonsuit')
    EventcbactionLog = CLogging('eventcbaction')
    WandLog = CLogging('wand')
    DiceLog = CLogging('dice')
    GardenerLog = CLogging('gardener')
    BackpackLog = CLogging('backpack')
    PlayerExtraElementLog = CLogging('playerextraelement')
    SeasoneightLog = CLogging('seasoneight')
    Init()
