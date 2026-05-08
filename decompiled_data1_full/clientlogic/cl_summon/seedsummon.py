# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_summon/seedsummon.pyc
# RelativePath: clientlogic/cl_summon/seedsummon.pyc
# Source Generated with Decompyle++
# File: seedsummon.pyc (Python 3.6)

from cl_only import Functor
from cl_commondefines import SIDE_TYPE_HERO, WARRIOR_SUMMON_SEED, FIGHT_KEY_WUDI
import cl_msgcenter
import cl_netattr
import cl_scene
from . import mobject

class CSeedSummon(mobject.CBaseSummon):
    m_Side = SIDE_TYPE_HERO
    m_FightType = WARRIOR_SUMMON_SEED
    m_ValidShowTips = 0
    
    def __str__(self):
        return '%s|%s|%s|%s|%s|%s|%s|%s' % (self.__class__, self.m_GameID, self.m_PlayerID, self.m_SID, self.m_ID, self.m_Scene, self.m_Name, self.m_Pos)

    
    def MapSendPacket(self, dPlayer):
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        if oOwner.m_PlayerID not in dPlayer:
            return None
        dPlayer = {
            oOwner.m_PlayerID: 1 }
        cl_netattr.MakeSummonAddPacket(self, dPlayer)

    
    def OnInitAttr(self, clsData, dAddData):
        self.AddBitAttr('SpecialKey', 'InitBitAttr', FIGHT_KEY_WUDI)
        cl_msgcenter.AddAttentionFunc(self, self.m_Owner, cl_msgcenter.MSG_WAR_LEAVESCENE, OwnerLeaveScene, 'OwnerLeaveScene')

    
    def Remove(self, sReason):
        cl_msgcenter.DoneAttention(self, self.m_Owner, cl_msgcenter.MSG_WAR_LEAVESCENE, 'OwnerLeaveScene')
        super().Remove(sReason)

    
    def RemoveOnlyServer(self, sReason, iDelayFrame):
        cl_msgcenter.DoneAttention(self, self.m_Owner, cl_msgcenter.MSG_WAR_LEAVESCENE, 'OwnerLeaveScene')
        oHero = self.GetOwner()
        if not oHero:
            self.Remove(sReason)
            return None
        self.Remove_Call_Out('Remove')
        oHero.Remove_Call_Out('RemoveOnlyServer')
        oHero.Call_Out(Functor(DelaySendMapDel, oHero, self.m_ID), iDelayFrame, 'RemoveOnlyServer')
        if self.m_RemoveAction:
            self.m_RemoveAction(self)
            self.m_RemoveAction = None
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_REMOVEOBJ, self, {
            'Reason': sReason })
        if self.m_Scene:
            self.LeaveScene(0)
        self.Release()
        if self.m_Scene:
            
            try:
                self.m_Game.Scene_DelObject(self.m_ID)
            except RuntimeError:
                print('Seed %d 已经从场景内删除' % self.m_ID)

            
            try:
                self.m_Game.DeleteObject(self.m_ID)
            except RuntimeError:
                print('Seed %d 物件已经删除过' % self.m_ID)

            self.m_Game = None
        else:
            self.RemoveFromList()

    
    def SetOwner(self, oOwner):
        self.m_Owner = oOwner.m_ID
        self.m_OwnerPlayerID = oOwner.m_PlayerID

    
    def GetOwner(self):
        return self.m_Game.GetObject(self.m_Owner)

    
    def IsNeglectAttack(self, oSkill):
        return False



def OwnerLeaveScene(oSeed, oOwner, dMsgInfo):
    oOwner.m_GardenerCon.RemoveSeed(oSeed.m_ID, 'LeaveScene')


def DelaySendMapDel(oHero, iSeedID):
    dData = {
        'oGame': oHero.m_Game,
        'iTarget': iSeedID,
        'iType': WARRIOR_SUMMON_SEED,
        'dPlayer': {
            oHero.m_PlayerID: 1 } }
    cl_scene.GS2CMapDelByDate(dData)

