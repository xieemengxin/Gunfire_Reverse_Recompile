# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_container/relictalentcon.pyc
# RelativePath: clientlogic/cl_container/relictalentcon.pyc
# Source Generated with Decompyle++
# File: relictalentcon.pyc (Python 3.6)

from cl_commondefines import BAG_TYPE_RELICTALENT, PF_TYPE_RELICTALENT, NPC_CB_VALUE, TYPE_RELIC, TYPE_TALENT, TYPE_CHOOSERELIC, TYPE_CHOOSETALENT, NWARRIOR_DROP_MAGIC_POWER, TYPE_CREATETALENT
from cl_object.logging import RelictalentLog
from cl_npc import net as npcnet
from cl_only import ChooseMulKeys, ShufferList, Functor
from cl_commondecorator import ChooseRewardEnd
import cl_container.performcon
import cl_perform
import cl_snetwar as warnet
import cl_msgcenter
import cl_notify
REASON_CHOOSE = 'choose'
REASON_AUTOCHOOSE = 'autochoose'
REASON_LOAD = 'load'
REASON_GM = 'gm'
CNT_GROWPF = 6

class CRelicTalentContainer(cl_container.performcon.CPerformContainer):
    m_BagType = BAG_TYPE_RELICTALENT
    m_Flag = 'RelicTalentCon'
    
    def __init__(self, oWarrior):
        super().__init__(oWarrior)
        self.m_RelicOption = []
        self.m_Relic = 0
        self.m_Talent = { }
        self.m_MagicPower = 0
        self.m_DamagePF = []
        self.m_DropReward = { }
        self.m_Notify = 0

    
    def Save(self):
        dData = super().Save()
        dData['RL'] = self.m_Relic
        dData['TL'] = self.m_Talent
        dData['MP'] = self.m_MagicPower
        return dData

    
    def Load(self, dData):
        if not dData:
            return None
        iRelic = dData.get('RL', 0)
        if not iRelic:
            return None
        self.m_MagicPower = dData['MP']
        self.AddRelic(iRelic, REASON_LOAD)
        for iSID, iLevel in dData['TL'].items():
            if not iLevel:
                self.m_Talent[iSID] = 0
                continue
            self.AddTalent(iSID, iLevel, REASON_LOAD)
        
        super().Load(dData)

    
    def Release(self):
        oGame = self.m_Game
        oOwner = oGame.GetObject(self.m_Owner)
        oWarmgr = oGame.m_WarMgr
        cl_msgcenter.DoneAttention(oOwner, oWarmgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.m_Flag)
        super().Release()

    
    def ClearAll(self):
        RelictalentLog.Debug(f'''{self.m_Game.m_ID} {self.m_PlayerID} clearall''')
        iRelic = self.m_Relic
        self.m_Relic = 0
        oOwner = self.m_Game.GetObject(self.m_Owner)
        self.RemovePerform(oOwner, iRelic)
        dTalent = self.m_Talent
        self.m_Talent = { }
        for iSID in dTalent:
            self.RemovePerform(oOwner, iSID)
        
        self.m_MagicPower = 0

    
    def ClearAllTalent(self, sReason):
        RelictalentLog.Debug(f'''{self.m_Game.m_ID} {self.m_PlayerID} clearalltalent {sReason}''')
        dTalent = self.m_Talent
        self.m_Talent = { }
        oOwner = self.m_Game.GetObject(self.m_Owner)
        for iSID in dTalent:
            self.RemovePerform(oOwner, iSID)
        

    
    def Refresh(self, dPlayer = None):
        if not self.m_Relic:
            return None
        oGame = self.m_Game
        warnet.GS2CAddRelicTalent(oGame, TYPE_RELIC, self.m_Relic, 1, self.m_Owner, dPlayer)
        if self.m_PlayerID not in dPlayer:
            return None
        for iSID, iLevel in self.m_Talent.items():
            if not iLevel:
                continue
            warnet.GS2CAddRelicTalent(oGame, TYPE_TALENT, iSID, iLevel, self.m_Owner, {
                self.m_PlayerID: 1 })
        

    
    def Init(self, lstRelicOption, iNotify):
        self.m_Notify = iNotify
        if not self.m_Relic:
            self.StartChooseRelic(lstRelicOption)

    
    def StartChooseRelic(self, lstRelicOption):
        self.m_RelicOption = lstRelicOption
        oGame = self.m_Game
        oOwner = oGame.GetObject(self.m_Owner)
        cl_msgcenter.AddAttentionFunc(oOwner, oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.AutoChooseRelic, self.m_Flag)
        oOwner.AddMapLoadOKCbFun(self.m_Flag, self.MapLoadChooseRelic, iPriority = 1, iOnce = 1)

    
    def MapLoadChooseRelic(self, oHero, dMsgInfo):
        return self.SendChooseRelic()

    
    def SendChooseRelic(self, iNextCB = 1):
        if not self.m_RelicOption:
            return 1
        oOwner = self.m_Game.GetObject(self.m_Owner)
        if iNextCB:
            func = self.OnChooseRelic
        else:
            func = self._OnChooseRelic
        warnet.GS2CChooseRelicTalent(oOwner, TYPE_RELIC, self.m_RelicOption)
        iMenuIdx = npcnet.SetNpcUICallBackFunction(oOwner, NPC_CB_VALUE, func)
        oOwner.Set('RelicTalentUIIdx', iMenuIdx)
        return 0

    
    def AutoChooseRelic(self, oOwner, oWarMgr, dMsgInfo):
        oOwner.RemoveMapLoadOKCbFun(self.m_Flag)
        npcnet.DelNpcUICallBackFunction(oOwner, oOwner.Query('RelicTalentUIIdx', 0), NPC_CB_VALUE)
        self._OnChooseRelic(oOwner, 0, REASON_AUTOCHOOSE)

    
    def OnChooseRelic(self, oHero, iAnswer):
        return self._OnChooseRelic(oHero, iAnswer)

    OnChooseRelic = ChooseRewardEnd(OnChooseRelic)
    
    def _OnChooseRelic(self, oHero, iAnswer, sReason = REASON_CHOOSE):
        if not self.m_RelicOption:
            return 1
        if iAnswer in self.m_RelicOption:
            iRelic = iAnswer
        elif iAnswer:
            RelictalentLog.Alert(f'''{self.m_Game.m_ID} {self.m_PlayerID} choose wrong relic {iAnswer} {self.m_RelicOption}''')
        iRelic = ShufferList(self.m_Game, self.m_RelicOption)[0]
        sReason = REASON_AUTOCHOOSE
        RelictalentLog.Debug(f'''{self.m_Game.m_ID} {self.m_PlayerID} choose relic {iAnswer} {iRelic} {sReason}''')
        dInfo = {
            'Option': self.m_RelicOption,
            'Choose': iRelic,
            'Auto': 1 if sReason == REASON_AUTOCHOOSE else 0 }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ADDRELICTALENT, oHero, dInfo, iSub = TYPE_CHOOSERELIC)
        self.m_RelicOption = { }
        self.AddRelic(iRelic, sReason)
        return 1

    
    def AddRelic(self, iRelic, sReason):
        oGame = self.m_Game
        if self.m_Relic:
            RelictalentLog.Alert(f'''{oGame.m_ID} {self.m_PlayerID} repeat add relic {iRelic} {self.m_Relic}''')
            return None
        clsPerform = cl_perform.GetPerformModule(iRelic)
        if not clsPerform:
            RelictalentLog.Alert(f'''{oGame.m_ID} {self.m_PlayerID} no relic {iRelic}''')
            return None
        if not (clsPerform.m_GrowPF) or len(clsPerform.m_GrowPF) != CNT_GROWPF:
            RelictalentLog.Alert(f'''{oGame.m_ID} {self.m_PlayerID} relic growpf err {iRelic} {clsPerform.m_GrowPF}''')
            return None
        oOwner = oGame.GetObject(self.m_Owner)
        RelictalentLog.Info(f'''{oGame.m_ID} {self.m_PlayerID} add relic {iRelic} {sReason}''')
        self.m_Relic = iRelic
        oPerform = self.AddPerform(oOwner, iRelic, 1, 1, 0)
        if not oPerform:
            RelictalentLog.Alert(f'''{oGame.m_ID} {self.m_PlayerID} add relic err {iRelic}''')
            return None
        self.m_DamagePF = oPerform.m_DamagePF
        if sReason != REASON_LOAD:
            self.m_Talent = dict.fromkeys(oPerform.m_GrowPF, 0)
            oWarMgr = oGame.m_WarMgr
            dPlayer = oWarMgr.GetRoomPlayer()
            warnet.GS2CAddRelicTalent(oGame, TYPE_RELIC, iRelic, 1, self.m_Owner, dPlayer)
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ADDRELICTALENT, oOwner, {
                'Relic': iRelic }, iSub = TYPE_RELIC)
            cl_msgcenter.DoneAttention(oOwner, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.m_Flag)

    
    def AddMagicPower(self, iCount, sReason):
        oGame = self.m_Game
        RelictalentLog.Info(f'''{oGame.m_ID} {self.m_PlayerID} add magicpower {iCount}''')
        self.m_MagicPower += iCount
        oOwner = oGame.GetObject(self.m_Owner)
        dMsgInfo = {
            'MagicPower': self.m_MagicPower,
            'ChangeMagicPowerValue': iCount,
            'FullPF': 0,
            'Reason': sReason }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_MAGICPOWERCHANGE, oOwner, dMsgInfo)
        oOwner.GS2CPropChange('MagicPower', self.m_MagicPower)

    
    def RewardByDrop(self, oHero, oDrop, iOption, iMagicPower, sReason):
        iDrop = oDrop.m_ID
        lstTalent = self.GetDropTalent(iDrop, iOption)
        if lstTalent:
            warnet.GS2CChooseRelicTalent(oHero, TYPE_TALENT, lstTalent)
            npcnet.SetNpcUICallBackFunction(oHero, NPC_CB_VALUE, Functor(self.DropChooseTalent, iDrop, sReason))
        else:
            oDrop.Remove('FullPick')
            if iMagicPower:
                self.AddMagicPower(iMagicPower, sReason)
                cl_notify.SendCommonNotify(self.m_Game, {
                    oHero.m_PlayerID: 1 }, self.m_Notify, {
                    '$get': str(iMagicPower) })

    
    def GetDropTalent(self, iDrop, iCount):
        lstSend = []
        if iDrop in self.m_DropReward:
            lstNewTalent = []
            iRemove = 0
            for iPF in self.m_DropReward[iDrop]:
                if iPF in self.m_Talent:
                    oPerform = self.GetPerform(iPF)
                    if oPerform and self.m_Talent[iPF] >= oPerform.m_MaxLevel:
                        iRemove += 1
                        continue
                    continue
                lstNewTalent.append(iPF)
            
            if iRemove:
                lstAddTalent = self.GetAvailableTalent(lstNewTalent, iRemove)
                lstNewTalent.extend(lstAddTalent)
                lstSend = lstAddTalent
            self.m_DropReward[iDrop] = lstNewTalent
        else:
            lstNewTalent = self.GetAvailableTalent([], iCount)
            self.m_DropReward[iDrop] = lstNewTalent
            lstSend = lstNewTalent
        if lstSend:
            oOwner = self.m_Game.GetObject(self.m_Owner)
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ADDRELICTALENT, oOwner, {
                'Drop': iDrop,
                'Talent': lstSend }, iSub = TYPE_CREATETALENT)
        return self.m_DropReward[iDrop]

    
    def GetAvailableTalent(self, lstExclude, iCount):
        dOption = { }
        for iPF, iLevel in self.m_Talent.items():
            if iPF in lstExclude:
                continue
            oPerform = self.GetPerform(iPF)
            if oPerform and iLevel >= oPerform.m_MaxLevel:
                continue
            dOption[iPF] = 10
        
        oGame = self.m_Game
        lstTalent = ChooseMulKeys(oGame, dOption, iCount)
        return lstTalent

    
    def DropChooseTalent(self, iDrop, sReason, oHero, iAnswer):
        if iDrop not in self.m_DropReward:
            return None
        lstOption = self.m_DropReward[iDrop]
        if not lstOption or iAnswer not in lstOption:
            return None
        oGame = self.m_Game
        if iAnswer not in self.m_Talent:
            RelictalentLog.Alert(f'''{oGame.m_ID} {self.m_PlayerID} choose talent answer err {iAnswer} {self.m_Talent}''')
            return None
        oPerform = self.GetPerform(iAnswer)
        if oPerform:
            iLevel = self.m_Talent[iAnswer] + 1
            if iLevel > oPerform.m_MaxLevel:
                RelictalentLog.Alert(f'''{oGame.m_ID} {self.m_PlayerID} choose talent level err {iAnswer} {iLevel}''')
                return None
        iLevel = 1
        RelictalentLog.Debug(f'''{oGame.m_ID} {self.m_PlayerID} choose talent {iAnswer} {iLevel}''')
        dInfo = {
            'Option': lstOption,
            'Choose': iAnswer,
            'Drop': iDrop }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ADDRELICTALENT, oHero, dInfo, iSub = TYPE_CHOOSETALENT)
        self.m_DropReward[iDrop] = []
        oPerform = self.AddTalent(iAnswer, iLevel, REASON_CHOOSE)
        if not oPerform:
            return None
        oDrop = oGame.GetObject(iDrop)
        if not oDrop or oDrop.m_FightType != NWARRIOR_DROP_MAGIC_POWER:
            return None
        iMagicPower = oDrop.m_MagicPower
        oDrop.Remove('Pick')
        if iMagicPower:
            self.AddMagicPower(iMagicPower, sReason)

    
    def AddTalent(self, iTalent, iLevel, sReason):
        iPFType = cl_perform.GetPerformClassAttr(iTalent, 'm_PFType')
        if iPFType != PF_TYPE_RELICTALENT:
            return None
        oGame = self.m_Game
        oOwner = oGame.GetObject(self.m_Owner)
        RelictalentLog.Info(f'''{oGame.m_ID} {self.m_PlayerID} add talent {iTalent} {iLevel} {sReason}''')
        oPerform = self.AddPerform(oOwner, iTalent, iLevel, 1, 0)
        if not oPerform:
            RelictalentLog.Alert(f'''{oGame.m_ID} {self.m_PlayerID} add talent err {iTalent} {iLevel}''')
            return None
        self.m_Talent[iTalent] = iLevel
        if sReason != REASON_LOAD:
            warnet.GS2CAddRelicTalent(oGame, TYPE_TALENT, iTalent, iLevel, self.m_Owner, {
                self.m_PlayerID: 1 })
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ADDRELICTALENT, oOwner, {
                'Talent': iTalent }, iSub = TYPE_TALENT)
        return oPerform

    
    def GetTalentWarReportInfo(self):
        dTalentWarInfo = { }
        for iTalent, iLevel in self.m_Talent.items():
            if not iLevel:
                continue
            dTalentWarInfo[iTalent] = iLevel
        
        return dTalentWarInfo

    
    def AllTalent(self):
        for iPF in self.m_Talent:
            clsPerform = cl_perform.GetPerformModule(iPF)
            if not clsPerform:
                return None
            self.AddTalent(iPF, clsPerform.m_MaxLevel, REASON_GM)
        

    
    def NeedCreateSeed(self):
        return 1

    
    def GetPerform(self, iPerform, iItem = 0):
        return super().GetPerform(iPerform)

    
    def GetItemByID(self, iItem):
        pass


