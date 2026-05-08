# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_signal/signal.pyc
# RelativePath: clientlogic/cl_signal/signal.pyc
# Source Generated with Decompyle++
# File: signal.pyc (Python 3.6)

from cl_commondefines import SIGNAL_TYPE_SCENE, SIGNAL_TYPE_ITEM
from cl_only import ChooseKey
import cl_msgcenter
import cl_warmgr.mobject
from . import load
from . import mobject
SIGNAL_LIVEFRAME = 750
SIGNAL_CDTIME = 250
SIGNAL_CDCOUNT = 5
SIGNAL_SCENETYPE_MAX = 2
SIGNAL_OBJTYPE_MAX = 2

class CSignalElement(cl_warmgr.mobject.CBaseElement):
    
    def __init__(self, oGame, nid, oData):
        super().__init__(oGame, nid, oData)
        self.m_SignalObjs = { }
        self.m_PlayerSignal = { }
        self.m_PlayerRecord = { }
        self.m_NotifyPos = []
        oGame.AddGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.OnLoadMapOK, 'SignalLoadMapOK')
        oGame.AddGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_ENTERWATCH, self.OnEnterWatch, 'SignalEnterWatch')

    
    def Release(self):
        self.m_Game.DoneGlobalAttention(self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, 'SignalLoadMapOK')
        self.m_Game.DoneGlobalAttention(self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_ENTERWATCH, 'SignalEnterWatch')
        for oSignal in self.m_SignalObjs.values():
            oSignal.Release()
        
        self.m_SignalObjs = { }
        self.m_PlayerSignal = { }
        self.m_PlayerRecord = { }
        super().Release()

    
    def NewSignalID(self):
        for idx in range(256):
            if idx in self.m_SignalObjs:
                continue
            return idx
        
        return 0

    
    def GetNotifyPos(self):
        if not self.m_NotifyPos:
            lstNotifyPos = []
            lstPlayer = self.m_Game.m_WarMgr.GetAllPlayer()
            for pid in lstPlayer:
                oHero = self.m_Game.m_WarMgr.GetHeroByPlayer(pid)
                if not oHero:
                    continue
                iPos = oHero.Query('TeamPos', 0)
                lstNotifyPos.append((iPos, pid))
            
            lstNotifyPos = [ tValue[1] for tValue in sorted(lstNotifyPos, key = (lambda x: x[0]), reverse = True) ]

            self.m_NotifyPos = lstNotifyPos
        return self.m_NotifyPos

    
    def IsInCD(self, pid):
        if pid not in self.m_PlayerRecord:
            return False
        dRecord = self.m_PlayerRecord[pid]
        iCurFrame = self.m_Game.GetFrameNum()
        iRecoreFrame = dRecord['Time']
        if iCurFrame >= iRecoreFrame + SIGNAL_CDTIME:
            return False
        iCnt = dRecord['Cnt']
        if iCnt < SIGNAL_CDCOUNT:
            return False
        return True

    
    def SetCDRecord(self, pid):
        iCurFrame = self.m_Game.GetFrameNum()
        dRecord = self.m_PlayerRecord.setdefault(pid, {
            'Time': iCurFrame,
            'Cnt': 0 })
        if iCurFrame >= dRecord['Time'] + SIGNAL_CDTIME:
            dRecord['Time'] = iCurFrame
            dRecord['Cnt'] = 1
            return None
        dRecord['Cnt'] += 1

    
    def ValidAddSceneSignal(self, pid, dParam):
        sid = dParam['SID']
        clsSignal = load.GetSignalCls(sid)
        if not clsSignal:
            return False
        if not clsSignal.m_Type == SIGNAL_TYPE_SCENE:
            return False
        if 'Weight' not in clsSignal.m_Notify:
            return False
        if 'Info' not in clsSignal.m_Notify:
            return False
        return not self.IsInCD(pid)

    
    def ValidAddObjSignal(self, pid, dParam):
        if self.IsInCD(pid):
            return False
        sid = dParam['SID']
        clsSignal = load.GetSignalCls(sid)
        if not clsSignal:
            return False
        if clsSignal.m_Type == SIGNAL_TYPE_SCENE:
            return False
        if 'Weight' not in clsSignal.m_Notify:
            return False
        if 'Info' not in clsSignal.m_Notify:
            return False
        return clsSignal.ValidAdd(self.m_Game, dParam)

    
    def ValidAddNotifySignal(self, pid, dParam):
        sid = dParam['SID']
        dSignal = load.GetTxtSignal(sid)
        if not dSignal:
            return False
        return not self.IsInCD(pid)

    
    def ValidAddPhotoSignal(self, pid, dParam):
        return not self.IsInCD(pid)

    
    def AddSignal(self, pid, dParam):
        sid = dParam['SID']
        iAttachID = dParam['Attach']
        oHero = self.m_Game.m_WarMgr.GetHeroByPlayer(pid)
        iScene = oHero.m_Scene
        iCurFrame = self.m_Game.GetFrameNum()
        iEndFrame = iCurFrame + SIGNAL_LIVEFRAME
        iSignal = self.NewSignalID()
        clsSignal = load.GetSignalCls(sid)
        self.AddShareTimes(iAttachID, pid, oHero)
        sKey = clsSignal.m_Key
        dPlayerSignal = self.m_PlayerSignal.setdefault(pid, { })
        lstSignal = dPlayerSignal.setdefault(sKey, [])
        if len(lstSignal) >= SIGNAL_SCENETYPE_MAX:
            self.RemoveSignal(lstSignal[0])
        self.TimeOutRemoveSignal()
        oSignal = clsSignal(iSignal, iEndFrame, iScene, self, dParam)
        self.m_SignalObjs[iSignal] = oSignal
        lstSignal.append(iSignal)
        self.SetCDRecord(pid)
        lstPlayer = dParam['Players'] if 'Players' in dParam else []
        oSignal.GS2CAddSignal(lstPlayer)

    
    def AddShareTimes(self, iAttachID, pid, oHero):
        oDrop = self.m_Game.GetObject(iAttachID)
        if not hasattr(oDrop, 'm_DropInfo'):
            return None
        if oDrop.m_FightType in mobject.g_GroupDropFightType:
            return None
        if oDrop.m_FightType in mobject.g_NoRecordShareTimesDrop:
            return None
        bSendMsg = False
        if isinstance(oDrop.m_DropInfo[0], int):
            if pid not in oDrop.m_ShareInfo:
                bSendMsg = True
                oDrop.m_ShareInfo[pid] = 1
            else:
                oDrop.m_ShareInfo[pid] += 1
        else:
            oIteam = oDrop.m_DropInfo[0]
            if pid not in oIteam.m_ShareInfo:
                bSendMsg = True
                oIteam.m_ShareInfo[pid] = 1
            else:
                oIteam.m_ShareInfo[pid] += 1
        if bSendMsg and pid == oDrop.m_Source:
            dMsgInfo = {
                'VID': iAttachID }
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SHAREGOODS, oHero, dMsgInfo)

    
    def AddItemSignal(self, who, oItem):
        pid = who.m_PlayerID
        sid = load.GetFightType2Signal(oItem.m_FightType)
        if not sid:
            return None
        dParam = {
            'Adder': pid,
            'AdderName': who.Name(),
            'SID': sid,
            'Attach': oItem.m_ID }
        self.AddSignal(pid, dParam)

    
    def AddNotify(self, pid, dParam):
        sid = dParam['SID']
        dSignal = load.GetTxtSignal(sid)
        if not dSignal:
            return None
        idx = ChooseKey(self.m_Game, dSignal['Weight'])
        if not idx or idx not in dSignal['Info']:
            return None
        self.SetCDRecord(pid)
        mobject.CTextSignal.GS2CAddSignal(self, pid, sid)

    
    def AddEmotionNotify(self, pid, dParam):
        sid = dParam['SID']
        self.SetCDRecord(pid)
        mobject.CTextSignal.GS2CAddSignal(self, pid, sid)
        oHero = self.m_Game.m_WarMgr.GetHeroByPlayer(pid)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_USINGEMOTION, oHero, {
            'SID': sid })

    
    def AddPhotoNotify(self, pid, dParam):
        self.SetCDRecord(pid)
        mobject.CTextSignal.GS2CAddPhoto(self, pid, dParam['SID'], dParam['Pos'], dParam['Rotate'])

    
    def RemoveSignal(self, iSignal, iNotify = 1):
        if iSignal not in self.m_SignalObjs:
            return None
        oSignal = self.m_SignalObjs.pop(iSignal)
        sKey = oSignal.m_Key
        pid = oSignal.m_Adder
        self.m_PlayerSignal[pid][sKey].remove(iSignal)
        if iNotify:
            oSignal.GS2CDelSignal([])
        oSignal.Release()

    
    def TimeOutRemoveSignal(self):
        lstSignal = []
        iCurFrame = self.m_Game.GetFrameNum()
        for iSignal, oSignal in self.m_SignalObjs.items():
            if oSignal.m_EndFrame < iCurFrame:
                lstSignal.append(iSignal)
        
        for iSignal in lstSignal:
            self.RemoveSignal(iSignal, 0)
        

    
    def OnLoadMapOK(self, oWarMgr, oTarget, dInfo):
        self.TimeOutRemoveSignal()
        iHero = dInfo['Hero']
        pid = dInfo['pid']
        oHero = self.m_Game.GetObject(iHero)
        iScene = oHero.m_Scene
        for oSignal in self.m_SignalObjs.values():
            if oSignal.m_Scene != iScene:
                continue
            if oSignal.m_Type == SIGNAL_TYPE_ITEM:
                oDrop = self.m_Game.GetObject(oSignal.m_AttachID)
                if not oDrop:
                    continue
                continue
            oSignal.SendObjNotify([
                pid])
            oSignal.GS2CAddSignal([
                pid])
        

    
    def OnEnterWatch(self, oWarMgr, oTarget, dInfo):
        pid = dInfo['pid']
        for oSignal in self.m_SignalObjs.values():
            if pid not in oSignal.m_PlayerRecord:
                continue
            oSignal.DelPlayerRecord(pid)
            oSignal.GS2CDelSignal([
                pid])
        


