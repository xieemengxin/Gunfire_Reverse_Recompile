# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_summon/barriersummon.pyc
# RelativePath: clientlogic/cl_summon/barriersummon.pyc
# Source Generated with Decompyle++
# File: barriersummon.pyc (Python 3.6)

from cl_commondefines import SIDE_TYPE_HERO, WARRIOR_SUMMON_BARRIER, ATTACKERSUBMSG_SUMMON, BLOCK_BY_SUMMON, FIGHT_KEY_WUDI, WARRIOR_DEVICE_BARRIER, GARDENER_HERO
from cl_resmgr.resdata import CSummonData
import cl_msgcenter
import cl_engphyobj
from . import mobject

class CBarrierSummon(mobject.CBaseSummon):
    m_Side = SIDE_TYPE_HERO
    m_FightType = WARRIOR_SUMMON_BARRIER
    m_ValidShowTips = 0
    m_SubAttackMsg = ATTACKERSUBMSG_SUMMON
    
    def OnInitAttr(self, clsData, dAddData):
        self.m_Shape = dAddData['ObjShape']
        self.m_CanAddBuff = dAddData['CanAddBuff'] if 'CanAddBuff' in dAddData else 1
        self.AddBitAttr('SpecialKey', 'CircleSummon', FIGHT_KEY_WUDI)
        if 'HPMax' in dAddData and dAddData['HPMax']:
            self.SetAttr('HPMax', dAddData['HPMax'], 0)
        else:
            self.SetAttr('HPMax', 100, 0)
        self.m_SendTarget = dAddData['SendMsgTarget']
        cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_RECEIVEDAMED, OnReceiveDamed, 'ReceiveDamed', iOnce = 0)

    
    def OnInitToScene(self, tPos):
        super(CBarrierSummon, self).OnInitToScene(tPos)
        oOwner = self.GetOwner()
        if oOwner.m_FightType == WARRIOR_DEVICE_BARRIER:
            self.SkillCheckArgs = oOwner.SkillCheckArgs
        if oOwner.m_SID == GARDENER_HERO:
            oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Scene)
            if oScene:
                if 'SpecalSphericalTarget' in oScene.m_CustomData:
                    setSpecialTarget = oScene.m_CustomData['SpecalSphericalTarget']
                    setSpecialTarget.add(self.m_ID)
                else:
                    oScene.m_CustomData['SpecalSphericalTarget'] = {
                        self.m_ID}

    
    def Remove(self, sReason):
        cl_msgcenter.DoneEvent(self, cl_msgcenter.MSG_WAR_RECEIVEDAMED, 'ReceiveDamed')
        oOwner = self.GetOwner()
        if oOwner and oOwner.m_SID == GARDENER_HERO:
            oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Scene)
            if oScene and 'SpecalSphericalTarget' in oScene.m_CustomData:
                setSpecialTarget = oScene.m_CustomData['SpecalSphericalTarget']
                if self.m_ID in setSpecialTarget:
                    setSpecialTarget.remove(self.m_ID)
        super().Remove(sReason)

    
    def SetOwner(self, oOwner):
        self.m_Owner = oOwner.m_ID
        self.m_OwnerPlayerID = oOwner.m_PlayerID
        self.m_ModelData = oOwner.m_ModelData

    
    def GetOwner(self):
        return self.m_Game.GetObject(self.m_Owner)

    
    def CheckAddBuff(self):
        if self.m_CanAddBuff:
            return True
        return False

    
    def AddExtraPhyModel(self, iPhyType, iLayer, dParam):
        oPhyModel = cl_engphyobj.CreatePhyModel(self, iPhyType, iLayer, dParam)
        if not oPhyModel:
            return None
        lstAllExtraPhyModel = self.SetDefault('ExtraPhyModel', [])
        lstAllExtraPhyModel.append(oPhyModel)

    
    def ClearAllExtraPhyModel(self):
        lstAllExtraPhyModel = self.Query('ExtraPhyModel', [])
        if not lstAllExtraPhyModel:
            return None
        for oPhyModel in lstAllExtraPhyModel:
            oPhyModel.E_Unstall()
        
        self.Set('ExtraPhyModel', [])



class CBarrierSummonData(CSummonData):
    m_SID = 1001
    m_Side = SIDE_TYPE_HERO
    m_Name = '屏障召唤物'
    m_Shape = 0
    m_FightType = WARRIOR_SUMMON_BARRIER


def OnReceiveDamed(oSummon, dMsgInfo):
    oTarget = oSummon.m_Game.GetObject(oSummon.m_SendTarget)
    if not oTarget:
        return None
    dInfo = {
        'Summon': oSummon.m_ID }
    if 'Skill' in dMsgInfo:
        dInfo['Skill'] = dMsgInfo['Skill']
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_BARRIER_BLOCK, oTarget, dInfo, iSub = BLOCK_BY_SUMMON)

