# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_object/dielog.pyc
# RelativePath: clientlogic/cl_object/dielog.pyc
# Source Generated with Decompyle++
# File: dielog.pyc (Python 3.6)

from cl_only import Time2Frame
from cl_object.logging import DieLog
from cl_commondefines import WARRIOR_BOSS
import cl_msgcenter

class CDieLogMgr(object):
    
    def __init__(self, oGame, iOwner):
        self.m_Game = oGame
        self.m_Owner = iOwner
        self.m_DieLogData = []
        self.m_MaxLen = 1000
        self.m_ValidFrame = Time2Frame(1000)
        self.Init()

    
    def Init(self):
        oOwner = self.GetOwner()
        cl_msgcenter.AddFunction(oOwner, cl_msgcenter.MSG_WAR_DIE, self.PushLog, 'DieLog', -1, 0)
        cl_msgcenter.AddFunction(oOwner, cl_msgcenter.MSG_WAR_REVTOTALDAM, self.OnRevTotalDam, 'DieLog', -1, 0)

    
    def Release(self):
        oOwner = self.GetOwner()
        cl_msgcenter.DoneEvent(oOwner, cl_msgcenter.MSG_WAR_DIE, 'DieLog')
        cl_msgcenter.DoneEvent(oOwner, cl_msgcenter.MSG_WAR_REVTOTALDAM, 'DieLog')
        self.m_Game = None

    
    def GetOwner(self):
        return self.m_Game.GetObject(self.m_Owner)

    
    def OnRevTotalDam(self, oOwner, dInfo):
        self.AddDieLogData(dInfo['TotalDam'], dInfo['RS'], dInfo['OldHpData'], dInfo['NewHpData'])

    
    def AddDieLogData(self, lstTotalDam, oReason, lstOldData, lstCurData):
        iCurFrame = self.m_Game.GetFrameNum()
        tData = (iCurFrame, lstTotalDam, oReason.Query('InitDam'), oReason.GetStrReason(), lstOldData, lstCurData)
        self.m_DieLogData.append((iCurFrame, tData))
        if len(self.m_DieLogData) > self.m_MaxLen:
            self.m_DieLogData.pop(0)

    
    def PushLog(self, oOwner, dInfo):
        sPushLog = '%s %s %s %s die:' % (self.m_Game.m_ID, oOwner.m_PlayerID, oOwner.m_SID, oOwner.m_ID)
        iCurFrame = self.m_Game.GetFrameNum()
        for iFrame, tData in self.m_DieLogData:
            if iCurFrame - iFrame <= self.m_ValidFrame:
                sLog = '%d %s %d %s %s %s--' % tData
                sPushLog += sLog + ','
        
        self.m_DieLogData = []
        DieLog.Info(sPushLog)


