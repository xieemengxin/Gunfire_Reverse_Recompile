# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_signal/mobject.pyc
# RelativePath: clientlogic/cl_signal/mobject.pyc
# Source Generated with Decompyle++
# File: mobject.pyc (Python 3.6)

from cl_commondefines import NWARRIOR_NPC_RAREGOLDENCUP, DROP_REASON_WEAPONMARK, SIGNAL_TYPE_ITEM, DROP_REASON_NPCMARK, SIGNAL_TYPE_MONSTER, SIGNAL_TYPE_NPC, NWARRIOR_NPC, NWARRIOR_NPC_GOLDENCUP, NWARRIOR_NPC_LIMITGOLDENCUP, NWARRIOR_NPC_EXCHANGEGOLDENCUP, INTERACT_TYPE_FORBID, NWARRIOR_DROP_EQUIP, NWARRIOR_DROP_KEYITEM, NWARRIOR_DROP_RELIC, SIGNAL_TYPE_SCENE, SIGPOS_SELF, WARRIOR_MONSTER, SIGNAL_TYPE_DYING, WARRIOR_HERO, SIGNAL_TYPE_FRIEND, SIGNAL_TYPE_DEFENDNPC, NWARRIOR_DROP_RAREITEM, NWARRIOR_DROP_MAGIC_POWER, NWARRIOR_DROP_DEVICECOMP, DROP_REASON_DEVICECOMPONENT, NWARRIOR_DROP_PETEGG, NWARRIOR_DROP_RELIC_MYSTERY, NWARRIOR_DROP_MAGIC_WAND, NWARRIOR_DROP_WANDCOMP, NWARRIOR_DROP_DICE, NWARRIOR_DROP_S7MODULE, NWARRIOR_DROP_S7CRYSTAL
from cl_only import GAME_FRAME, ChooseKey
import cl_msgcenter
import cl_notify
import cl_perform
from . import net
g_CanShareDropFightType = {
    NWARRIOR_DROP_EQUIP,
    NWARRIOR_DROP_RELIC,
    NWARRIOR_DROP_KEYITEM,
    NWARRIOR_DROP_RAREITEM,
    NWARRIOR_DROP_DEVICECOMP,
    NWARRIOR_DROP_RELIC_MYSTERY,
    NWARRIOR_DROP_MAGIC_WAND,
    NWARRIOR_DROP_WANDCOMP,
    NWARRIOR_DROP_DICE,
    NWARRIOR_DROP_S7MODULE,
    NWARRIOR_DROP_S7CRYSTAL}
g_GroupDropFightType = {
    NWARRIOR_DROP_MAGIC_POWER,
    NWARRIOR_DROP_PETEGG}
g_CanShareRelicFightType = {
    NWARRIOR_DROP_RELIC,
    NWARRIOR_DROP_RELIC_MYSTERY}
g_CanShareDropName = {
    NWARRIOR_DROP_WANDCOMP}
g_NoRecordShareTimesDrop = {
    NWARRIOR_DROP_WANDCOMP}

class CTextSignal(object):
    
    def GS2CAddSignal(cls, oMgr, pid, sid):
        oGame = oMgr.m_Game
        oHero = oGame.m_WarMgr.GetHeroByPlayer(pid)
        iScene = oHero.m_Scene
        oScene = oGame.m_SceneMgr.GetScene(iScene)
        if not oScene:
            return None
        dPlayer = oScene.GetPlayers()
        net.GS2CSignInfo(oGame, dPlayer, oHero.m_ID, sid)

    GS2CAddSignal = classmethod(GS2CAddSignal)
    
    def GS2CAddPhoto(cls, oMgr, pid, sid, tPos, tRotate):
        oGame = oMgr.m_Game
        oHero = oGame.m_WarMgr.GetHeroByPlayer(pid)
        iScene = oHero.m_Scene
        oScene = oGame.m_SceneMgr.GetScene(iScene)
        if not oScene:
            return None
        dPlayer = oScene.GetPlayers()
        net.GS2CPhotoInfo(oGame, dPlayer, oHero.m_ID, sid, tPos, tRotate)

    GS2CAddPhoto = classmethod(GS2CAddPhoto)
    
    def SendTextNotify(cls, oMgr, iAdder, iTarget, dParam, dType):
        oGame = oMgr.m_Game
        sName = dParam['AdderName']
        lstNotifyPos = oMgr.GetNotifyPos()
        iLen = len(lstNotifyPos)
        if iAdder == iTarget:
            iType = SIGPOS_SELF
        elif iAdder not in lstNotifyPos:
            return None
        if iTarget not in lstNotifyPos:
            return None
        iPosa = lstNotifyPos.index(iAdder)
        iPost = lstNotifyPos.index(iTarget)
        iType = SIGPOS_SELF - iLen - iPosa - 1 if iPosa < iPost else SIGPOS_SELF - iLen - iPosa
        if iType not in dType:
            return None
        cl_notify.SendCommonNotify(oGame, [
            iTarget], dType[iType], {
            '$$playername': sName })

    SendTextNotify = classmethod(SendTextNotify)


class CBaseSignal(object):
    m_Type = 0
    m_SID = 0
    m_Name = ''
    m_Notify = { }
    m_Key = 'Obj'
    
    def __init__(self, iSignal, iEndFrame, iScene, oMgr, dParam):
        self.m_ID = iSignal
        self.m_EndFrame = iEndFrame
        self.m_Scene = iScene
        self.m_SignalMgr = oMgr
        self.m_Adder = dParam['Adder']
        self.m_AdderName = dParam['AdderName']
        self.m_PlayerRecord = []
        self.OnInit(dParam)

    
    def OnInit(self, dParam):
        pass

    
    def Release(self):
        self.OnRelease()
        self.m_SignalMgr = None

    
    def OnRelease(self):
        pass

    
    def GetDesc(self):
        return []

    
    def AddPlayerRecord(self, lstPlayer):
        for pid in lstPlayer:
            if pid in self.m_PlayerRecord:
                continue
            self.m_PlayerRecord.append(pid)
        

    
    def DelPlayerRecord(self, pid):
        if pid in self.m_PlayerRecord:
            self.m_PlayerRecord.remove(pid)

    
    def GetNotifyInfo(self):
        return {
            '$$playername': self.m_AdderName }

    
    def GetSignalAddPlayer(self):
        oGame = self.m_SignalMgr.m_Game
        oScene = oGame.m_SceneMgr.GetScene(self.m_Scene)
        if not oScene:
            return { }
        dPlayer = oScene.GetPlayers()
        lstPlayer = []
        oWarMgr = oGame.m_WarMgr
        oWatch = oWarMgr.GetComponent('WatchElement')
        for pid in dPlayer.keys():
            if not oWarMgr.IsInRoom(pid):
                continue
            if oWatch and pid in oWatch.m_WatchPlayer:
                continue
            lstPlayer.append(pid)
        
        return lstPlayer

    
    def GetSignalDelPlayer(self):
        oGame = self.m_SignalMgr.m_Game
        oScene = oGame.m_SceneMgr.GetScene(self.m_Scene)
        if not oScene:
            return { }
        dPlayer = oScene.GetPlayers()
        lstPlayer = []
        for pid in self.m_PlayerRecord:
            if pid not in dPlayer:
                continue
            lstPlayer.append(pid)
        
        return lstPlayer

    
    def SendObjNotify(self, lstPlayer):
        oGame = self.m_SignalMgr.m_Game
        lstNotifyPos = self.m_SignalMgr.GetNotifyPos()
        iLen = len(lstNotifyPos)
        idx = ChooseKey(oGame, self.m_Notify['Weight'])
        if not idx or idx not in self.m_Notify['Info']:
            return None
        lstNewPlayer = []
        for pid in lstPlayer:
            if pid in self.m_PlayerRecord:
                continue
            lstNewPlayer.append(pid)
            if self.m_Adder == pid:
                iType = SIGPOS_SELF
            elif self.m_Adder not in lstNotifyPos:
                return None
            if pid not in lstNotifyPos:
                return None
            iPosa = lstNotifyPos.index(self.m_Adder)
            iPost = lstNotifyPos.index(pid)
            iType = SIGPOS_SELF - iLen - iPosa - 1 if iPosa < iPost else SIGPOS_SELF - iLen - iPosa
            if iType not in self.m_Notify['Info'][idx]:
                return None
            dNotify = self.GetNotifyInfo()
            cl_notify.SendCommonNotify(oGame, [
                pid], self.m_Notify['Info'][idx][iType], dNotify)
            self.AddPlayerRecord(lstNewPlayer)
        

    
    def GS2CAddSignal(self, lstPlayer):
        if not lstPlayer:
            lstPlayer = self.GetSignalAddPlayer()
        if not lstPlayer:
            return None
        self.SendObjNotify(lstPlayer)
        oGame = self.m_SignalMgr.m_Game
        net.GS2CAddSignal(oGame, lstPlayer, {
            self.m_Key: [
                self] })

    
    def GS2CDelSignal(self, lstPlayer):
        if not lstPlayer:
            lstPlayer = self.GetSignalDelPlayer()
        if not lstPlayer:
            return None
        oGame = self.m_SignalMgr.m_Game
        net.GS2CDelSignal(oGame, lstPlayer, [
            self.m_ID])

    
    def ValidAdd(cls, oGame, dParam):
        return True

    ValidAdd = classmethod(ValidAdd)


class CSceneSignal(CBaseSignal):
    m_Type = SIGNAL_TYPE_SCENE
    m_Key = 'Scene'
    
    def OnInit(self, dParam):
        self.m_Pos = dParam['Pos']

    
    def GetDesc(self):
        oGame = self.m_SignalMgr.m_Game
        iCurFrame = oGame.GetFrameNum()
        iRemainFrame = max(0, self.m_EndFrame - iCurFrame)
        iRemainTime = int(iRemainFrame / GAME_FRAME)
        return [
            self.m_ID,
            self.m_SID,
            iRemainTime,
            self.m_Pos,
            self.m_AdderName]



class CBaseObjSignal(CBaseSignal):
    
    def OnInit(self, dParam):
        self.m_AttachID = dParam['Attach']

    
    def GetDesc(self):
        oGame = self.m_SignalMgr.m_Game
        iCurFrame = oGame.GetFrameNum()
        iRemainFrame = max(0, self.m_EndFrame - iCurFrame)
        iRemainTime = int(iRemainFrame / GAME_FRAME)
        return [
            self.m_ID,
            self.m_SID,
            iRemainTime,
            self.m_AttachID,
            self.m_AdderName]



class CDropObjSignal(CBaseObjSignal):
    m_Type = SIGNAL_TYPE_ITEM
    
    def OnInit(self, dParam):
        super(CDropObjSignal, self).OnInit(dParam)
        oGame = self.m_SignalMgr.m_Game
        oGame.AddGlobalAttention(self.m_AttachID, cl_msgcenter.MSG_WAR_PICK, self.OnDropDelete, 'SignalPickDrop%d' % self.m_AttachID)
        oGame.AddGlobalAttention(self.m_AttachID, cl_msgcenter.MSG_WAR_DROPREPLACE, self.OnDropDelete, 'SignalDropReplace%d' % self.m_AttachID)
        oDrop = oGame.GetObject(self.m_AttachID)
        self.ShareDropInScene()
        self.m_DropName = self.GetDropName(oDrop)

    
    def ShareDropInScene(self):
        oGame = self.m_SignalMgr.m_Game
        oScene = oGame.m_SceneMgr.GetScene(self.m_Scene)
        oDrop = oGame.GetObject(self.m_AttachID)
        iOwner = oDrop.m_Owner
        if not iOwner or not oScene:
            return None
        if oDrop.m_FightType in g_CanShareRelicFightType:
            oDrop.Set('DropReason', DROP_REASON_NPCMARK)
            oDrop.GS2CPropChange('DropReason')
        elif oDrop.m_FightType == NWARRIOR_DROP_EQUIP:
            oDrop.Set('DropReason', DROP_REASON_WEAPONMARK)
            oDrop.GS2CPropChange('DropReason')
        elif oDrop.m_FightType in g_GroupDropFightType:
            return None
        if oDrop.m_FightType == NWARRIOR_DROP_DEVICECOMP:
            oDrop.Set('DropReason', DROP_REASON_DEVICECOMPONENT)
            oDrop.GS2CPropChange('DropReason')
        if not oDrop.VaildCanShare():
            return None
        oDrop.SetOwner(0)
        dPlayer = oScene.GetPlayers()
        dNewPlayer = dict(dPlayer)
        if self.m_Adder in dNewPlayer:
            dNewPlayer.pop(self.m_Adder)
        oDrop.NetAddTo(dNewPlayer)

    
    def GetDropName(self, oDrop):
        iFightType = oDrop.m_FightType
        if iFightType in (NWARRIOR_DROP_EQUIP, NWARRIOR_DROP_KEYITEM, NWARRIOR_DROP_RAREITEM, NWARRIOR_DROP_MAGIC_WAND, NWARRIOR_DROP_DICE, NWARRIOR_DROP_S7MODULE):
            oItem = oDrop.m_DropInfo[0]
            if oItem:
                return oItem.Name()
        if iFightType in g_CanShareRelicFightType:
            iPerformSID = oDrop.m_DropInfo[0]
            clsPerform = cl_perform.GetPerformModule(iPerformSID)
            if clsPerform:
                return clsPerform.m_Name
        if iFightType in g_CanShareDropName:
            return oDrop.Name()
        return '无名'

    
    def OnDropDelete(self, oDrop, oTarget, dInfo):
        if oDrop.m_ID == self.m_AttachID:
            self.m_SignalMgr.RemoveSignal(self.m_ID)

    
    def OnRelease(self):
        oGame = self.m_SignalMgr.m_Game
        oGame.DoneGlobalAttention(self.m_AttachID, cl_msgcenter.MSG_WAR_PICK, 'SignalPickDrop%d' % self.m_AttachID)
        oGame.DoneGlobalAttention(self.m_AttachID, cl_msgcenter.MSG_WAR_DROPREPLACE, 'SignalDropReplace%d' % self.m_AttachID)

    
    def GetNotifyInfo(self):
        sName = self.m_DropName
        return {
            '$name': sName,
            '$$playername': self.m_AdderName }

    
    def ValidAdd(cls, oGame, dParam):
        iDrop = dParam['Attach']
        oDrop = oGame.GetObject(iDrop)
        if not oDrop:
            return False
        if oDrop.m_FightType in g_GroupDropFightType:
            return oDrop.m_Group != 0
        if oDrop.m_FightType in g_CanShareRelicFightType and not (oDrop.m_Share):
            return False
        return oDrop.m_FightType in g_CanShareDropFightType

    ValidAdd = classmethod(ValidAdd)
    
    def GS2CAddSignal(self, lstPlayer):
        oGame = self.m_SignalMgr.m_Game
        oDrop = oGame.GetObject(self.m_AttachID)
        if oDrop and oDrop.m_FightType in g_GroupDropFightType:
            iGroup = oDrop.m_Group
            if not iGroup:
                return None
            oWarMgr = oGame.m_WarMgr
            dInfo = oWarMgr.GetDropGroupInfo(iGroup)
            if not dInfo:
                return None
            (iSignalID, iSignalSID, iRemainTime, _, sAdderName) = self.GetDesc()
            lstHeroID = [ oWarMgr.GetHeroIDByPlayerID(pid) for pid in lstPlayer ] if lstPlayer else list(dInfo)
            for iHero in lstHeroID:
                if iHero not in dInfo:
                    continue
                iDrop = dInfo[iHero]
                oHeroDrop = oGame.GetObject(iDrop)
                if not oHeroDrop:
                    continue
                pid = oWarMgr.GetPlayerIDByHeroID(iHero)
                lstSendPlayer = [
                    pid]
                self.SendObjNotify(lstSendPlayer)
                net.GS2CAddSignalByInfo(oGame, lstSendPlayer, [], [
                    [
                        iSignalID,
                        iSignalSID,
                        iRemainTime,
                        iDrop,
                        sAdderName]], [])
            
        else:
            super().GS2CAddSignal(lstPlayer)



class CNpcObjSignal(CBaseObjSignal):
    m_Type = SIGNAL_TYPE_NPC
    
    def OnInit(self, dParam):
        super(CNpcObjSignal, self).OnInit(dParam)
        oGame = self.m_SignalMgr.m_Game
        oNpc = oGame.GetObject(self.m_AttachID)
        if not oNpc:
            return None
        cl_msgcenter.AddFunction(oNpc, cl_msgcenter.MSG_WAR_NPCINTERACT, self.OnInteract, 'NpcIteractSignal', -1, 0)

    
    def GetSignalAddPlayer(self):
        oGame = self.m_SignalMgr.m_Game
        oNpc = oGame.GetObject(self.m_AttachID)
        if not oNpc:
            return []
        lstPlayer = super(CNpcObjSignal, self).GetSignalAddPlayer()
        if oNpc.m_FightType not in [
            NWARRIOR_NPC_GOLDENCUP,
            NWARRIOR_NPC_LIMITGOLDENCUP,
            NWARRIOR_NPC_RAREGOLDENCUP,
            NWARRIOR_NPC_EXCHANGEGOLDENCUP]:
            return lstPlayer
        lstNewPlayer = []
        for pid in lstPlayer:
            if pid in self.m_PlayerRecord:
                continue
            if oNpc.GetPlayerInteractType(pid) == INTERACT_TYPE_FORBID:
                continue
            lstNewPlayer.append(pid)
        
        return lstNewPlayer

    
    def OnInteract(self, oNpc, dInfo):
        if oNpc.m_ID != self.m_AttachID:
            return None
        if oNpc.m_FightType not in [
            NWARRIOR_NPC_GOLDENCUP,
            NWARRIOR_NPC_LIMITGOLDENCUP,
            NWARRIOR_NPC_EXCHANGEGOLDENCUP]:
            return None
        pid = dInfo['Hero']
        if not pid != self.m_Adder:
            return None
        self.m_SignalMgr.RemoveSignal(self.m_ID)

    
    def OnRelease(self):
        oGame = self.m_SignalMgr.m_Game
        oNpc = oGame.GetObject(self.m_AttachID)
        if not oNpc:
            return None
        cl_msgcenter.DoneEvent(oNpc, cl_msgcenter.MSG_WAR_NPCINTERACT, 'NpcIteractSignal')

    
    def ValidAdd(cls, oGame, dParam):
        iNpc = dParam['Attach']
        oNpc = oGame.GetObject(iNpc)
        if not oNpc:
            return False
        if not oNpc.m_FightType & NWARRIOR_NPC:
            return False
        if not oNpc.ValidShare():
            return False
        return True

    ValidAdd = classmethod(ValidAdd)


class CMonsterSignal(CBaseObjSignal):
    m_Type = SIGNAL_TYPE_MONSTER
    
    def OnInit(self, dParam):
        super(CMonsterSignal, self).OnInit(dParam)
        oWarMgr = self.m_SignalMgr.m_Game.m_WarMgr
        cl_msgcenter.AddAttentionFunc(oWarMgr, self.m_AttachID, cl_msgcenter.MSG_WAR_DIE, self.OnMonsterDie, 'SignalMonsterDead')

    
    def OnMonsterDie(self, oWarMgr, oMonster, dInfo):
        if oMonster.m_ID == self.m_AttachID:
            self.m_SignalMgr.RemoveSignal(self.m_ID)

    
    def OnRelease(self):
        oWarMgr = self.m_SignalMgr.m_Game.m_WarMgr
        cl_msgcenter.DoneAttention(oWarMgr, self.m_AttachID, cl_msgcenter.MSG_WAR_DIE, 'SignalMonsterDead')

    
    def GetNotifyInfo(self):
        oGame = self.m_SignalMgr.m_Game
        oMonster = oGame.GetObject(self.m_AttachID)
        return {
            '$name': oMonster.Name(),
            '$$playername': self.m_AdderName }

    
    def ValidAdd(cls, oGame, dParam):
        iMonster = dParam['Attach']
        oMonster = oGame.GetObject(iMonster)
        if not oMonster:
            return False
        return oMonster.m_FightType & WARRIOR_MONSTER

    ValidAdd = classmethod(ValidAdd)


class CDyingPlayerSignal(CBaseObjSignal):
    m_Type = SIGNAL_TYPE_FRIEND
    
    def OnInit(self, dParam):
        super(CDyingPlayerSignal, self).OnInit(dParam)
        oWarMgr = self.m_SignalMgr.m_Game.m_WarMgr
        cl_msgcenter.AddAttentionFunc(oWarMgr, self.m_AttachID, cl_msgcenter.MSG_WAR_DIE, self.OnMonsterDie, 'SignalHeroDead')

    
    def OnMonsterDie(self, oWarMgr, oHero, dInfo):
        if oHero.m_ID == self.m_AttachID:
            self.m_SignalMgr.RemoveSignal(self.m_ID)

    
    def OnRelease(self):
        oWarMgr = self.m_SignalMgr.m_Game.m_WarMgr
        cl_msgcenter.DoneAttention(oWarMgr, self.m_AttachID, cl_msgcenter.MSG_WAR_DIE, 'SignalHeroDead')

    
    def ValidAdd(cls, oGame, dParam):
        iHero = dParam['Attach']
        oHero = oGame.GetObject(iHero)
        if not oHero:
            return False
        return oHero.m_FightType & WARRIOR_HERO

    ValidAdd = classmethod(ValidAdd)


class CNormalPlayerSignal(CBaseObjSignal):
    m_Type = SIGNAL_TYPE_DYING
    
    def OnInit(self, dParam):
        super(CNormalPlayerSignal, self).OnInit(dParam)
        oWarMgr = self.m_SignalMgr.m_Game.m_WarMgr
        cl_msgcenter.AddAttentionFunc(oWarMgr, self.m_AttachID, cl_msgcenter.MSG_WAR_RELIFE, self.OnHeroRelife, 'SignalHeroRelife')

    
    def OnHeroRelife(self, oWarMgr, oHero, dInfo):
        if oHero.m_ID == self.m_AttachID:
            self.m_SignalMgr.RemoveSignal(self.m_ID)

    
    def OnRelease(self):
        oWarMgr = self.m_SignalMgr.m_Game.m_WarMgr
        cl_msgcenter.DoneAttention(oWarMgr, self.m_AttachID, cl_msgcenter.MSG_WAR_RELIFE, 'SignalHeroRelife')

    
    def ValidAdd(cls, oGame, dParam):
        iHero = dParam['Attach']
        oHero = oGame.GetObject(iHero)
        if not oHero:
            return False
        if not oHero.m_FightType & WARRIOR_HERO:
            return False
        if oHero.IsDead():
            return False
        return True

    ValidAdd = classmethod(ValidAdd)


class CTeamInfoSignal(CBaseObjSignal):
    m_Key = 'TeamInfo'
    m_Type = SIGNAL_TYPE_DYING
    
    def OnInit(self, dParam):
        super(CTeamInfoSignal, self).OnInit(dParam)
        self.m_OwnerName = dParam['OwnerName']
        self.m_AttachType = dParam['Type']

    
    def GetDesc(self):
        oGame = self.m_SignalMgr.m_Game
        iCurFrame = oGame.GetFrameNum()
        iRemainFrame = max(0, self.m_EndFrame - iCurFrame)
        iRemainTime = int(iRemainFrame / GAME_FRAME)
        return [
            self.m_ID,
            self.m_SID,
            iRemainTime,
            self.m_AttachID,
            self.m_AdderName,
            self.m_OwnerName,
            self.m_AttachType]



class CDefendNpcObjSignal(CBaseObjSignal):
    m_Type = SIGNAL_TYPE_DEFENDNPC
    
    def GS2CAddSignal(self, lstPlayer):
        oGame = self.m_SignalMgr.m_Game
        if lstPlayer:
            net.GS2CAddSignal(oGame, lstPlayer, {
                self.m_Key: [
                    self] })
        lstPlayer2 = oGame.m_WarMgr.GetLivePlayer()
        if lstPlayer2:
            self.SendObjNotify(lstPlayer2)


