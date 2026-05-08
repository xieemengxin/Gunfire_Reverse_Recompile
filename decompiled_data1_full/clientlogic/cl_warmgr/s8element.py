# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/s8element.pyc
# RelativePath: clientlogic/cl_warmgr/s8element.pyc
# Source Generated with Decompyle++
# File: s8element.pyc (Python 3.6)

from cl_only import Functor, Time2Frame, ChooseKey, SendAlert
from cl_commondefines import NWARRIOR_NPC_PASSBOX, PF_SUBMSG_COMMON, PF_SUBMSG_S8THIRDACTIVE, COMMON_SEASON_DAMEAGE
from cl_warmgr.mobject import CSeasonElement
from cl_object.reason import REASON_TYPE_PERFORM
import cl_msgcenter

class CS8Element(CSeasonElement):
    
    def __init__(self, oGame, nid, oData):
        super().__init__(oGame, nid, oData)
        self.m_CallFlag = 'S8Element'
        self.m_WarMgr = oGame.m_WarMgr
        self.m_Enable = 0
        dConfig = self.m_Data.m_Config
        self.m_EnableRound = dConfig.get('EnableRound', [
            3])
        self.m_S8DamagePerform = dConfig.get('S8DamagePerform', { })

    
    def CheckEnable(self):
        return self.m_Enable

    
    def Init(self):
        oWarMgr = self.m_WarMgr
        if oWarMgr.m_Round not in self.m_EnableRound:
            return None
        super().Init()
        cl_msgcenter.AddAttentionFunc(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.OnAddPlayer, self.m_CallFlag)
        self.m_Enable = 1
        oWarMgr.Set('PutS8ShopNpc', 1)

    
    def Release(self):
        self.m_Enable = 0
        super().Release()
        self.m_WarMgr = None
        self.m_Game = None

    
    def OnAddPlayer(self, oElement, oWarMgr, dInfo):
        oHero = dInfo['oCtrlHero']
        cl_msgcenter.AddAttentionFunc(self, oHero.m_ID, cl_msgcenter.MSG_WAR_PERFORM_START, self.OnPerformStart, self.m_CallFlag, iSub = PF_SUBMSG_COMMON)
        cl_msgcenter.AddAttentionFunc(self, oHero.m_ID, cl_msgcenter.MSG_WAR_PERFORM_START, self.OnPerformStart, self.m_CallFlag, iSub = PF_SUBMSG_S8THIRDACTIVE)

    
    def GetS8DamageInfo(self, iTotalDam, dInfo):
        if 'Skill' in dInfo:
            oSkill = dInfo['Skill']
            iPerform = oSkill.m_Base['pfid']
            if iPerform in self.m_S8DamagePerform:
                return {
                    self.m_S8DamagePerform[iPerform]: iTotalDam }
        if 'RS' in dInfo and dInfo['RS'].m_Type == REASON_TYPE_PERFORM:
            iPerform = dInfo['RS'].m_Perform
            if iPerform in self.m_S8DamagePerform:
                return {
                    self.m_S8DamagePerform[iPerform]: iTotalDam }
        return { }

    
    def OnPerformStart(self, _oListener, _oHero, dMsgInfo):
        oSkill = dMsgInfo['Skill']
        iPerform = oSkill.m_Base['pfid']
        if iPerform not in self.m_S8DamagePerform:
            return None
        oSkill.m_Collect['ExShowTips'] = COMMON_SEASON_DAMEAGE



def GetComponentClass(oWarManager):
    return CS8Element

