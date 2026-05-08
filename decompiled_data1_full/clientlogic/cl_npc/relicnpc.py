# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_npc/relicnpc.pyc
# RelativePath: clientlogic/cl_npc/relicnpc.pyc
# Source Generated with Decompyle++
# File: relicnpc.pyc (Python 3.6)

from cl_commondefines import NPC_CB_DICT
from cl_cscommondef import QUALITY_TYPE_HIGH
from cl_only import SendAlert
import cl_msgcenter
from . import mobject
from . import net

class CRelicNPC(mobject.CNPC):
    
    def __init__(self, *args):
        super().__init__(*args)
        iLayer = 1
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        if oLevelCtrl:
            iLayer = oLevelCtrl.m_LayerNum
        self.m_TotalNum = 4 * (iLayer - 1)
        self.m_PlayerUse = { }

    
    def OnInteract(self, oHero):
        iUseNum = self.m_PlayerUse.setdefault(oHero.m_PlayerID, 0)
        net.GS2CNpcModifyItem(oHero, self.m_ID, self.m_TotalNum, iUseNum)
        net.SetNpcUICallBackFunction(oHero, NPC_CB_DICT, self.PlayerChoose, self)

    
    def PlayerChoose(self, oHero, dChoose):
        oRelicCon = oHero.m_RelicCon
        lstNonexistent = []
        pid = oHero.m_PlayerID
        for iRelicSID in list(dChoose):
            if iRelicSID not in oRelicCon.m_Perform:
                lstNonexistent.append(iRelicSID)
                dChoose.pop(iRelicSID)
        
        if lstNonexistent:
            SendAlert('err', f'''game: {oHero.m_Game.m_ID} {pid} nonexistent relic {lstNonexistent}''')
        iRemainNum = self.m_TotalNum - self.m_PlayerUse[pid]
        for iRelicSID, iModify in dChoose.items():
            if iModify <= 0:
                continue
            iShowQuality = oRelicCon.GetShowQuality(iRelicSID)
            iOldQuality = iShowQuality
            for _ in range(iModify):
                if iShowQuality >= QUALITY_TYPE_HIGH:
                    SendAlert('err', f'''game: {oHero.m_Game.m_ID} {pid} {iRelicSID} quality can\'t modify {iModify} number''')
                    break
                if iRemainNum <= 0:
                    break
                iShowQuality *= 2
                iRemainNum -= 1
                self.m_PlayerUse[pid] += 1
            
            oRelicCon.SetShowQuality(iRelicSID, iShowQuality)
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CHANGE_RELIC_SHOWQUALITY, oHero, {
                'OldQuality': iOldQuality,
                'iPerform': iRelicSID })
        
        oRelicCon.GS2CUpdateShowQuality(dChoose.keys())


