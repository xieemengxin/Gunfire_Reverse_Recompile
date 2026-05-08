# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/reportsaveelement.pyc
# RelativePath: clientlogic/cl_warmgr/reportsaveelement.pyc
# Source Generated with Decompyle++
# File: reportsaveelement.pyc (Python 3.6)

from cl_warmgr.mobject import CBaseElement
from cl_commondefines import SETTLE_LOSEWAR, WARRIOR_HERO, TYPE_RELIFE_GSCASH, OP_SAVE_TEMPREPORT, OP_DEL_TEMPREPORT, LEAVE_TYPE_NORECORDE
from cl_only import SendAlert, PythonError
import cl_msgcenter
import cllib.lib_server as lib_server
import cllib.lib_flag as lib_flag

class CSingleGamePlayerReportSave(CBaseElement):
    
    def __init__(self, oGame, nid, oData):
        CBaseElement.__init__(self, oGame, nid, oData)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_PlayerID = 0

    
    def Init(self):
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, 'PlayerReportSave')

    
    def Release(self):
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, 'PlayerReportSave')
        if self.IsOpenTempReport():
            self.DoneAttention()
        self.m_WarMgr = None

    
    def OnAddAllPlayer(self, oWarMgr, oTarget, dInfo):
        if self.IsOpenTempReport():
            self.AddAttention()

    
    def AddAttention(self):
        lstHero = self.m_WarMgr.GetAllHero()
        for iHero in lstHero:
            cl_msgcenter.AddAttentionFunc(self, iHero, cl_msgcenter.MSG_WAR_DIE, self.OnDie, 'PlayerReportSave')
            cl_msgcenter.AddAttentionFunc(self, iHero, cl_msgcenter.MSG_WAR_RELIFE, self.OnRelife, 'PlayerReportSave')
        

    
    def DoneAttention(self):
        lstHero = self.m_WarMgr.GetAllHero()
        for iHero in lstHero:
            cl_msgcenter.DoneAttention(self, iHero, cl_msgcenter.MSG_WAR_DIE, 'PlayerReportSave')
            cl_msgcenter.DoneAttention(self, iHero, cl_msgcenter.MSG_WAR_RELIFE, 'PlayerReportSave')
        

    
    def GetPlayerID(self):
        if not self.m_PlayerID:
            self.m_PlayerID = self.m_WarMgr.GetAllPlayer()[0]
        return self.m_PlayerID

    
    def GetHeroObj(self):
        iPlayer = self.GetPlayerID()
        return self.m_WarMgr.GetHeroByPlayer(iPlayer)

    
    def IsOpenTempReport(self):
        if self.m_WarMgr.IsSingleGame():
            return True
        return False

    
    def OnDie(self, oListener, oHero, dInfo):
        if oHero.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
            return None
        (iType, _, _) = oHero.GetFirstRelifeInfo()
        if iType != TYPE_RELIFE_GSCASH:
            return None
        oDieElement = self.m_Game.m_WarMgr.GetComponent('PVEDieElement')
        if oDieElement and not oDieElement.IsDirectDie(iType, oHero):
            self.HandleReport(OP_SAVE_TEMPREPORT)

    
    def OnRelife(self, oListener, oHero, dInfo):
        self.HandleReport(OP_DEL_TEMPREPORT)

    
    def SaveTempReport(self, pid):
        iType = SETTLE_LOSEWAR
        if lib_flag.g_IsMobile:
            iLeaveType = LEAVE_TYPE_NORECORDE
        else:
            SendAlert('err', 'need suitable leavetype')
            iLeaveType = 0
        dWarEndReport = self.m_WarMgr.CreateWarEndReport(pid, iType, True)
        
        try:
            dBigDataReport = self.m_WarMgr.CreateWarEndBigDataAnalyseInfo(pid, iType, dWarEndReport)
        except:
            PythonError()
            dBigDataReport = { }

        dLevelEndReport = self.m_WarMgr.CreateLevelEndReport(pid, iType, iLeaveType)
        dTempReport = {
            'WarEndReport': dWarEndReport,
            'BigDataReport': dBigDataReport,
            'LevelEndReport': dLevelEndReport,
            'GameID': self.m_Game.m_ID }
        return dTempReport

    
    def HandleReport(self, iOP):
        oHero = self.GetHeroObj()
        dReport = {
            'FightIndex': oHero.Query('FightIndex'),
            'Round': self.m_WarMgr.m_Round,
            'Cycle': self.m_WarMgr.m_Cycle,
            'WarNo': self.m_WarMgr.m_SID,
            'OPType': iOP }
        pid = self.GetPlayerID()
        if iOP == OP_SAVE_TEMPREPORT:
            dReport['TempReport'] = self.SaveTempReport(pid)
        lib_server.L2STempReport(0, self.m_Game.m_ID, pid, dReport)



def GetComponentClass(oWarMgr):
    return CSingleGamePlayerReportSave

