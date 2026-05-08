# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_container/benedictioncon.pyc
# RelativePath: clientlogic/cl_container/benedictioncon.pyc
# Source Generated with Decompyle++
# File: benedictioncon.pyc (Python 3.6)

from cl_commondefines import BAG_TYPE_BENEDICTION, PF_TYPE_BENEDICTION, BENE_SOURCE_LAYER, BENE_SOURCE_ALL
from cl_object.logging import WarbenedictionLog
import cl_container.performcon
import cl_perform.load
import cl_duonet.dn_cl_container_talentcon as benedictionnet
import cl_msgcenter

def GS2CAddBenediction(oGame, iHero, iBenedictionSID, iBasicLevel, iType, iLayer, dPlayer, iReplaceSID):
    if not dPlayer:
        dPlayer = oGame.GetRealPlayers()
    netData = {
        'iBenedictionSID': iBenedictionSID,
        'iBasicLevel': iBasicLevel,
        'iType': iType,
        'iLayer': iLayer,
        'iHero': iHero,
        'iReplaceSID': iReplaceSID,
        'oGame': oGame,
        'dPlayer': dPlayer }
    benedictionnet.DN_GS2CAddBenediction(netData)


def GS2CRemoveBenediction(oGame, iHero, iBenedictionSID):
    dPlayer = oGame.GetRealPlayers()
    netData = {
        'iBenedictionSID': iBenedictionSID,
        'iHero': iHero,
        'oGame': oGame,
        'dPlayer': dPlayer }
    benedictionnet.DN_GS2CRemoveBenediction(netData)


class CBenedictionContainer(cl_container.performcon.CPerformContainer):
    m_BagType = BAG_TYPE_BENEDICTION
    
    def Save(self):
        dData = super(CBenedictionContainer, self).Save()
        dLayer = { }
        dReplace = { }
        dSource = { }
        for iSID, oPerform in self.m_Perform.items():
            dLayer[iSID] = oPerform.m_Layer
            if oPerform.m_ReplaceSID:
                dReplace[iSID] = oPerform.m_ReplaceSID
            dSource[iSID] = oPerform.m_SourceType
        
        dData['LY'] = dLayer
        dData['RP'] = dReplace
        dData['SC'] = dSource
        return dData

    
    def Load(self, dData):
        if not dData:
            return None
        super(CBenedictionContainer, self).Load(dData)
        dLayer = dData.get('LY', { })
        dReplace = dData.get('RP', { })
        dSource = dData.get('SC', { })
        for iSID, iLevel in dData['PF'].items():
            if iSID not in dLayer:
                self.AddBenediction(iSID, iLevel, 'load', iSource = dSource.get(iSID, BENE_SOURCE_LAYER))
                continue
            self.AddBenediction(iSID, iLevel, 'load', {
                'Layer': dLayer[iSID] }, dReplace.get(iSID, 0), iSource = dSource.get(iSID, BENE_SOURCE_LAYER))
        

    
    def RemoveBenediction(self, iBenediction):
        oBenediction = self.GetPerform(iBenediction)
        if not oBenediction:
            return False
        oOwner = self.m_Game.GetObject(self.m_Owner)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_REMOVEBENED_BEFORE, oOwner, {
            'Bene': iBenediction })
        self.RemovePerform(oOwner, iBenediction)
        self.GS2CRemoveBenediction(iBenediction)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_REMOVEBENED, oOwner, {
            'Bene': iBenediction })
        return True

    
    def Refresh(self, dPlayer = None):
        for oPerform in self.m_Perform.values():
            if oPerform.m_SourceType != BENE_SOURCE_LAYER:
                continue
            self.GS2CAddBenediction(oPerform, dPlayer)
        
        super(CBenedictionContainer, self).Refresh(dPlayer)

    
    def AddBenediction(self, iBenediction, iLevel, sReason, dExtInfo = None, iReplaceSID = 0, iSource = BENE_SOURCE_LAYER):
        iPFType = cl_perform.GetPerformClassAttr(iBenediction, 'm_PFType')
        if iPFType != PF_TYPE_BENEDICTION:
            return None
        oOwner = self.m_Game.GetObject(self.m_Owner)
        WarbenedictionLog.Info('%d %d add %d %d %d %s' % (self.m_Game.m_ID, self.m_PlayerID, iBenediction, iLevel, iSource, sReason))
        oBenediction = self.AddPerform(oOwner, iBenediction, iLevel, 1, 0)
        if not oBenediction:
            return None
        oBenediction.m_SourceType = iSource
        if not oBenediction.m_Layer:
            oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
            iLayer = oLevelCtrl.m_LayerNum if oLevelCtrl else 0
            oBenediction.m_Layer = iLayer
        if iReplaceSID:
            oBenediction.m_ReplaceSID = iReplaceSID
        if dExtInfo:
            oBenediction.m_Layer = dExtInfo.get('Layer', 0)
        if iSource == BENE_SOURCE_LAYER:
            self.GS2CAddBenediction(oBenediction)
        dInfo = {
            'Bene': iBenediction,
            'AddLayer': oBenediction.m_Layer,
            'Reason': sReason }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ADDBENED, oOwner, dInfo)
        return oBenediction

    
    def HasBenediction(self, iBenediction):
        oBenediction = self.GetPerform(iBenediction)
        if oBenediction:
            return True
        return False

    
    def GS2CAddBenediction(self, oBenediction, dPlayer = None):
        iBenediction = oBenediction.m_SID
        iLevel = oBenediction.Level()
        iType = 1 if oBenediction.m_Career else 0
        iLayer = oBenediction.m_Layer
        iReplaceSID = oBenediction.m_ReplaceSID
        GS2CAddBenediction(self.m_Game, self.m_Owner, iBenediction, iLevel, iType, iLayer, dPlayer, iReplaceSID)

    
    def GS2CPerformAdd(self, oPerform, dPlayer = None):
        pass

    
    def GS2CRemoveBenediction(self, iTalentSID):
        GS2CRemoveBenediction(self.m_Game, self.m_Owner, iTalentSID)

    
    def GetBenedictionSID(self, iSource = BENE_SOURCE_ALL):
        lstBenediction = []
        for oPerform in self.m_Perform.values():
            if oPerform.m_PFType != PF_TYPE_BENEDICTION:
                continue
            if iSource != BENE_SOURCE_ALL and oPerform.m_SourceType != iSource:
                continue
            lstBenediction.append(oPerform.m_SID)
        
        return lstBenediction

    
    def GetBenediction(self, iSource):
        lstBenediction = []
        for oPerform in self.m_Perform.values():
            if oPerform.m_PFType != PF_TYPE_BENEDICTION:
                continue
            if oPerform.m_SourceType != iSource:
                continue
            lstBenediction.append(oPerform)
        
        return lstBenediction


