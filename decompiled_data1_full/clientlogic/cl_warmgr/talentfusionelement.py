# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/talentfusionelement.pyc
# RelativePath: clientlogic/cl_warmgr/talentfusionelement.pyc
# Source Generated with Decompyle++
# File: talentfusionelement.pyc (Python 3.6)

from cl_warmgr.mobject import CBaseElement
from cl_commondefines import NPC_CB_VALUELIST, LEVEL_TYPE_BOSS
from cl_npc import net
from cl_only import ChooseKey, DeepCopy
from cl_object.logging import WarobjLog
from cl_commondecorator import ChooseRewardEnd
import cl_msgcenter
import cl_perform

class CTalentFusionElement(CBaseElement):
    
    def __init__(self, oGame, nid, oData):
        super().__init__(oGame, nid, oData)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_CallFlag = 'TalentFusionElement'
        self.m_InitLayer = self.m_Data.m_Config.get('InitLayer', 0)
        self.m_ChooseNum = self.m_Data.m_Config.get('ChooseNum', (0, 0))
        self.m_CommonTalentWeight = self.m_Data.m_Config.get('CommonTalentWeight', 0)
        self.m_MaxNum = self.m_Data.m_Config.get('MaxNum', 0)
        self.m_ExChooseWeightInfo = self.m_Data.m_Config.get('ExChooseWeightInfo', { })
        self.m_ChooseWeight = self.m_Data.m_Config.get('ChooseWeight', 0)
        self.m_GenCommonTalent = { }
        self.m_ChooseInfo = { }

    
    def Init(self):
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_CallFlag, -1, 0)

    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_CallFlag)
        for iHero in self.m_WarMgr.GetAllHero():
            oHero = self.m_Game.GetObject(iHero)
            if not oHero:
                continue
            cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_ADDTALENT, self.m_CallFlag)
            oHero.RemoveMapLoadOKCbFun(self.m_CallFlag)
        
        super(CTalentFusionElement, self).Release()
        self.m_WarMgr = None

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        oGame = self.m_Game
        for iHero in oWarMgr.GetAllHero():
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            oHero.AddMapLoadOKCbFun(self.m_CallFlag, self.OnMapLoadOk)
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_ADDTALENT, self.CheckTalent, self.m_CallFlag, -1, 0)
        

    
    def CheckTalent(self, oTarget, dInfo):
        oTalentCon = oTarget.m_TalentCon
        if oTalentCon.CheckHasAllTalent():
            cl_msgcenter.DoneEvent(oTarget, cl_msgcenter.MSG_WAR_ADDTALENT, self.m_CallFlag)
            oTalentCon.ClearBanTalent(self.m_CallFlag)

    
    def OnMapLoadOk(self, oTarget, dInfo):
        if oTarget.m_PlayerID in self.m_ChooseInfo:
            return 1
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        if oLevelCtrl.m_LayerNum == self.m_InitLayer and oLevelCtrl.m_CurLType == LEVEL_TYPE_BOSS:
            if oTarget.m_PlayerID not in self.m_GenCommonTalent:
                lstTalent = self.GenCommonTalent(oTarget)
                self.m_GenCommonTalent[oTarget.m_PlayerID] = lstTalent
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_COMMONTALENT_GEN, oTarget, {
                    'CommonTalentGen': lstTalent })
            net.GS2CCommonTalentChoose(oTarget, self.m_GenCommonTalent[oTarget.m_PlayerID])
            net.SetNpcUICallBackFunction(oTarget, NPC_CB_VALUELIST, self.PlayerChoose)
            return 0
        return 1

    
    def Save(self):
        dData = { }
        dData['CI'] = self.m_ChooseInfo
        return DeepCopy(dData)

    
    def Load(self, dData):
        if not dData:
            return None
        self.m_ChooseInfo = dData['CI']

    
    def PlayerChoose(self, oHero, lstChoose):
        oGame = self.m_Game
        iPlayerID = oHero.m_PlayerID
        self.m_ChooseInfo[iPlayerID] = True
        if len(lstChoose) > 4:
            WarobjLog.Alert('game:%d, gencommontalent num err %s, %s' % (oGame.m_ID, iPlayerID, lstChoose))
            return 1
        iCommonTalentMaxNum = self.m_ChooseNum[1]
        lstCommonTalentChoose = lstChoose[:iCommonTalentMaxNum]
        lstBanTalentChoose = lstChoose[iCommonTalentMaxNum:]
        if iPlayerID not in self.m_GenCommonTalent:
            WarobjLog.Alert('game:%d, gencommontalent err %s, %s' % (oGame.m_ID, iPlayerID, lstChoose))
            return 1
        lstAllCommonTalent = self.m_GenCommonTalent[iPlayerID]
        dCommonTalent = { }
        for iTalent in lstCommonTalentChoose:
            if iTalent == 0:
                continue
            if iTalent not in lstAllCommonTalent:
                WarobjLog.Alert('game:%d, commontalent choose err %s, %s' % (oGame.m_ID, iPlayerID, lstChoose))
                return 1
            dCommonTalent[iTalent] = self.m_ChooseWeight
        
        dBanTalent = { 1: iTalent for iTalent in lstBanTalentChoose }
        if oHero.m_TalentCon.AddBanTalent(self.m_CallFlag, dBanTalent):
            oHero.m_TalentCon.AddCommonTalent(self.m_CallFlag, dCommonTalent)
            WarobjLog.Debug('game:%d, talentfusion choose %s, %s, %s' % (oGame.m_ID, iPlayerID, dCommonTalent, dBanTalent))
        return 1

    PlayerChoose = ChooseRewardEnd(PlayerChoose)
    
    def GenCommonTalent(self, oHero):
        dCommonTalentLib = cl_perform.load.GetCommonTalentLib()
        dChoose = { }
        for iCareer, dTalent in dCommonTalentLib.items():
            if iCareer == oHero.m_Career:
                continue
            for iTalent in dTalent:
                if iTalent in self.m_ExChooseWeightInfo:
                    dChoose[iTalent] = self.m_ExChooseWeightInfo[iTalent]
                    continue
                dChoose[iTalent] = self.m_ChooseWeight
            
        
        lstResult = []
        iChooseNum = self.m_ChooseNum[0]
        for _ in range(iChooseNum):
            iTalent = ChooseKey(self.m_Game, dChoose)
            if not iTalent:
                break
            lstResult.append(iTalent)
            dChoose.pop(iTalent)
        
        return lstResult

    
    def CheckIsCommonTalent(self, oHero, iPerform):
        dTalent = oHero.m_TalentCon.GetCommonTalent(self.m_CallFlag)
        if iPerform in dTalent:
            return True
        return False



def GetComponentClass(oMgrManager):
    return CTalentFusionElement

