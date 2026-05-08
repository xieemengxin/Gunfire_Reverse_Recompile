# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_progressunlock/trigger.pyc
# RelativePath: clientlogic/cl_progressunlock/trigger.pyc
# Source Generated with Decompyle++
# File: trigger.pyc (Python 3.6)

from cl_commondefines import UNLOCK_TRIGGER_KILL, ATTACKERSUBMSG_NORMAL, WARRIOR_MONSTER
import cl_msgcenter
import cl_msgcenter.eventcbobj
import cl_platformdata

class CBaseTrigger(object):
    
    def __init__(self, oParent):
        self.m_Parent = oParent

    
    def Register(self, iSID, iProgress):
        pass

    
    def Release(self):
        self.m_Parent = None



class CKillTrigger(CBaseTrigger):
    
    def __init__(self, oParent):
        super(CKillTrigger, self).__init__(oParent)
        self.m_AllTarget = { }
        iOwner = self.m_Parent.m_Owner
        oGame = self.m_Parent.m_Game
        oGame.AddGlobalAttention(iOwner, cl_msgcenter.MSG_WAR_KILL, OnKill, 'UnlockTrigger_Kill', iSub = ATTACKERSUBMSG_NORMAL)

    
    def Release(self):
        iOwner = self.m_Parent.m_Owner
        oGame = self.m_Parent.m_Game
        oGame.DoneGlobalAttention(iOwner, cl_msgcenter.MSG_WAR_KILL, 'UnlockTrigger_Kill', iSub = ATTACKERSUBMSG_NORMAL)
        super(CKillTrigger, self).Release()

    
    def Register(self, iSID, iProgress):
        clsData = cl_platformdata.GetUnlockProgressCls(iSID)
        if type(clsData.m_TargetMonsterBase) == list:
            for target in clsData.m_TargetMonsterBase:
                lstSameTarget = self.m_AllTarget.setdefault(target, [])
                lstSameTarget.append(iSID)
            
        else:
            lstSameTarget = self.m_AllTarget.setdefault(clsData.m_TargetMonsterBase, [])
            lstSameTarget.append(iSID)

    
    def OnKill(self, dMsgInfo):
        iOwner = self.m_Parent.m_Owner
        oGame = self.m_Parent.m_Game
        oTarget = oGame.GetObject(dMsgInfo['VID'])
        if not oTarget or oTarget.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
            return None
        oHero = oGame.GetObject(iOwner)
        if not oHero or oHero.m_Scene != oTarget.m_Scene:
            return None
        iBase = oTarget.m_DataSID
        if iBase not in self.m_AllTarget:
            return None
        lstRemove = []
        lstSameTarget = self.m_AllTarget[iBase]
        oEventCB = None
        for iSID in lstSameTarget:
            if iSID in oHero.m_UnlockProgressCon.m_DoneProgress:
                lstRemove.append(iSID)
                continue
            clsData = cl_platformdata.GetUnlockProgressCls(iSID)
            if not clsData and clsData.m_CBFunc or oEventCB:
                oEventCB = cl_msgcenter.eventcbobj.CEventCB(None, 'UnlockProgress')
            oEventCB.InitEventCBInfo({
                'UnlockProgress': iSID }, dMsgInfo, iSID)
            clsData.m_CBFunc(oEventCB, oHero)
        
        for iSID in lstRemove:
            lstSameTarget.remove(iSID)
        
        if not lstSameTarget:
            self.m_AllTarget.pop(iBase)



def OnKill(oHero, oKiller, dMsgInfo):
    if not oHero.m_UnlockProgressCon:
        return None
    if not oKiller:
        return None
    oGame = oHero.m_Game
    iVictim = dMsgInfo['VID']
    oVictim = oGame.GetObject(iVictim)
    if oVictim:
        lstHero = oGame.m_WarMgr.GetRoomHero()
        for iHero in lstHero:
            if oVictim.Query('Injured%d' % iHero):
                break
        else:
            return None
    oTrigger = oHero.m_UnlockProgressCon.GetTrigger(UNLOCK_TRIGGER_KILL)
    if oTrigger:
        oTrigger.OnKill(dMsgInfo)

g_UnlockTrigger = {
    UNLOCK_TRIGGER_KILL: CKillTrigger }
