# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/skill.pyc
# RelativePath: clientlogic/cl_perform/skill.pyc
# Source Generated with Decompyle++
# File: skill.pyc (Python 3.6)

from cl_only import Functor, GAME_FRAME, CopyDict, PythonError
from cl_commondefines import WARRIOR_PERFORM, CRT_CHECK_SERVER, CRT_CHECK_CLIENT, WARRIOR_MONSTER, SERVER_ACTION_NUM_MAX, WARRIOR_DEVICE_BARRIER, WARRIOR_HERO, FROM_OWNER, FORM_TEAMMATE
from cl_commondefines import WARRIOR_SUMMON_BARRIER
from cl_commondefines import CRT_TRIGGER_MSG_CONST
from cl_object.logging import SkillLog, OptimizationLog
import time
import cl_perform
import cl_perform.load
import cl_perform.skillcache as skillcache
import cl_perform.net as pfnet
import cl_world
import cl_msgcenter
import cllib.lib_flag as lib_flag
PLAYER_CRT_NUM = 10 if lib_flag.g_IsMobileRun else 20
NO_SEND_CRT_NUM = PLAYER_CRT_NUM * 2
SEND_EMPTY = 1
NO_SEND = 2

class CSkill(object):
    
    def __init__(self, oGame, iSkillID):
        self.m_Game = oGame
        self.m_SkillID = iSkillID
        self.m_GameID = oGame.m_ID
        self.m_CheckType = 0
        self.m_TempInitCrt = None
        self.m_CrtStack = []
        self.m_CurCartoon = []
        self.m_CallOut = { }
        self.m_SpeedCallOut = { }
        self.m_SuspendSource = { }
        self.m_SuspendCallOut = { }
        self.m_SuspendSpeedCallOut = { }
        self.m_SuspendLastSpeed = 0
        self.m_NetReceiveCache = []
        self.m_Base = { }
        self.m_Cartoon = { }
        self.m_Collect = { }
        self.m_Update = { }
        self.m_Custom = { }
        self.m_Cache = { }
        self.m_Event = { }
        self.m_EndFunc = []
        self.m_CastingEndFunc = []
        self.m_CartoonIndex = { }
        self.m_NetSend = { }
        self.m_NetReceive = { }
        self.m_NetBuffer = []
        self.m_CacheData = skillcache.CSkillCacheData()
        self.m_PreProcessNetData = False
        self.m_HaltRS = None
        self.m_CrtBuff = { }
        self.m_VarCache = { }
        self.m_CutForTeam = 0
        self.m_CutForSingleGame = 0
        self.m_Resend = 0
        self.m_NetResend = { }

    
    def Init(self, oAttack, pfobj, dData):
        iActNum = dData['ActNum'] if 'ActNum' in dData else oAttack.GetActionNum()
        self.m_Base = {
            'Time': time.time(),
            'AID': oAttack.m_ID,
            'pid': oAttack.m_OwnerPlayerID,
            'Scene': oAttack.m_Scene,
            'pfid': pfobj.m_SID,
            'PFLV': pfobj.m_Level,
            'PFKey': '%s-%s-%s' % (pfobj.Key(), iActNum, oAttack.m_OwnerPlayerID),
            'PFType': pfobj.m_PFType,
            'RS': oAttack.AttReason(pfobj, iActNum),
            'ActNum': iActNum,
            'vStart': dData['vStart'] if 'vStart' in dData else oAttack.GetPos(),
            'vEnd': dData['vEnd'] if 'vEnd' in dData else oAttack.GetPos(),
            'VID': dData['VID'] if 'VID' in dData else 0,
            'Weapon': dData['Weapon'] if 'Weapon' in dData else 0,
            'AttrObj': dData['AttrObj'] if 'AttrObj' in dData else pfobj.m_ID,
            'ModelHeight': oAttack.m_ModelHeight }
        if self.m_Base['AID'] == self.m_Base['VID'] and oAttack.m_FightType & WARRIOR_MONSTER == WARRIOR_MONSTER:
            SkillLog.Alert('%s MonsterPF %s attack equal victim' % (self.m_Game.m_ID, self.m_Base['pfid']))
        self.m_Custom = dData['Custom'] if 'Custom' in dData else { }
        self.m_Base['netexclude'] = 0
        self.m_CutForSingleGame = 0
        self.m_CutForTeam = 0
        if self.m_Base['pid']:
            iScenePlayerCrtNum = self.m_Game.m_SkillMgr.m_ScenePlayerCrtNum[self.m_Base['Scene']]
            if iScenePlayerCrtNum > PLAYER_CRT_NUM:
                self.m_CutForTeam = NO_SEND if iScenePlayerCrtNum >= NO_SEND_CRT_NUM else SEND_EMPTY
        if 'Net' in dData:
            self.m_CheckType = CRT_CHECK_CLIENT
            self.m_CacheData = dData['CtrlCache']
            self.m_PreProcessNetData = True
            self.m_NetReceive = self.PreProcessClientData(dData['Net'])
            self.m_Base['netexclude'] = oAttack.m_PlayerID
            if self.m_Game.m_WarMgr.IsSingleGame():
                self.m_CutForSingleGame = 1
            else:
                self.m_CheckType = CRT_CHECK_SERVER
                cl_perform.skillcache.CacheInitData(self)
        self.m_Resend = None.m_Resend
        oItem = pfobj.GetMyItem()
        if 'dCache' in self.m_Custom:
            dCustomCache = self.m_Custom['dCache']
            self.m_Cache = dCustomCache
        else:
            self.m_Cache = oAttack.AttrCache()
            self.m_Cache.update(oAttack.MixPFAttrCache(pfobj.AttrCache()))
            if oItem:
                self.m_Cache.update(oItem.AttrCache())
        self.m_Event = oAttack.EventCache()
        if oItem:
            dEvent = oItem.EventCache()
            for iMsg, dInfo in dEvent.items():
                if iMsg not in self.m_Event:
                    self.m_Event[iMsg] = { }
                self.m_Event[iMsg].update(dInfo)
            
        if 'CastingEndFunc' in dData:
            self.m_CastingEndFunc.append(dData['CastingEndFunc'])
        self.m_Custom['IgnoreLayer'] = pfobj.m_IgnoreLayer
        if 'TransDamFactor' in self.m_Custom:
            self.m_Collect['DamFactor'] = CopyDict(self.m_Custom['TransDamFactor'])

    
    def Start(self, oAttack, pfobj):
        self.m_CurCartoon = []
        pfobj.UsePerform(oAttack, self)
        if self.m_HaltRS:
            self.Halt2(self.m_HaltRS)
            return None
        self.NetSkillStart()
        self.TryEnd()

    
    def StartOnlyServer(self, oAttack, pfobj):
        self.m_CurCartoon = []
        pfobj.UsePerform(oAttack, self)
        self.NetPacketBuffer()
        self.End()

    
    def GetCartoonBuffList(self, iNodeID):
        if iNodeID in self.m_Cartoon and not (self.m_Cartoon[iNodeID]['cls'].m_ContinueShoot):
            lstBuffID = self.m_CrtBuff[iNodeID] if iNodeID in self.m_CrtBuff else []
        else:
            lstBuffID = []
        return lstBuffID

    
    def PassCrtBuff(self, iParentID, iChildID):
        if iParentID in self.m_CrtBuff:
            self.m_CrtBuff[iChildID] = self.m_CrtBuff[iParentID][:]

    
    def PreProcessClientData(self, dNetData):
        if not self.m_PreProcessNetData:
            return dNetData
        for iNodeID, dNodeData in dNetData.items():
            self.PreProcessClientNodeData(iNodeID, dNodeData)
        
        return dNetData

    
    def PreProcessClientNodeData(self, iNodeID, dNodeData):
        if not self.m_PreProcessNetData:
            return dNodeData
        if 'Ray' in dNodeData:
            oAttack = self.GetAttack()
            lstNewRay = []
            dCrtBuff = { }
            lstBuffID = self.GetCartoonBuffList(iNodeID)
            for vHitPos, vNormal, iVictim, iHitPart in dNodeData['Ray']:
                if not iVictim:
                    lstNewRay.append((vHitPos, vNormal, iVictim, iHitPart))
                    break
                iTrueVictim = oAttack.GetCSummonTrueID(iVictim)
                oVictim = self.m_Game.GetObject(iTrueVictim)
                if not oVictim:
                    continue
                if oVictim.m_FightType == WARRIOR_PERFORM:
                    if not oVictim.m_NeglectAttack:
                        lstNewRay.append((vHitPos, vNormal, iTrueVictim, iHitPart))
                    elif iTrueVictim not in lstBuffID and oVictim.SkillCheckHitPos(self, dNodeData['Frame'], vHitPos):
                        lstBuffID.append(iTrueVictim)
                    continue
                if oVictim.m_FightType == WARRIOR_DEVICE_BARRIER:
                    if iTrueVictim not in lstBuffID and oVictim.ActiveStatus() and oVictim.SkillCheckHitPos(self, dNodeData['Frame'], vHitPos):
                        lstBuffID.append(iTrueVictim)
                        iThroughSub = FROM_OWNER if oAttack.m_ID == oVictim.m_Owner else FORM_TEAMMATE
                        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_BARRIER_THROUGH, oVictim, {
                            'VID': iTrueVictim,
                            'Skill': self }, oGame = self.m_Game, iSub = iThroughSub)
                    continue
                if oVictim.m_FightType == WARRIOR_SUMMON_BARRIER:
                    if not oVictim.CheckAddBuff():
                        continue
                    oDevice = oVictim.GetOwner()
                    if oDevice.m_ID not in lstBuffID and oVictim.SkillCheckHitPos(self, dNodeData['Frame'], vHitPos):
                        lstBuffID.append(oDevice.m_ID)
                        iThroughSub = FROM_OWNER if oAttack.m_ID == oDevice.m_Owner else FORM_TEAMMATE
                        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_BARRIER_THROUGH, oDevice, {
                            'VID': oDevice.m_ID,
                            'Skill': self }, oGame = self.m_Game, iSub = iThroughSub)
                    continue
                lstNewRay.append((vHitPos, vNormal, iTrueVictim, iHitPart))
                if lstBuffID:
                    dCrtBuff[iTrueVictim] = tuple(lstBuffID)
            
            dNodeData['Ray'] = lstNewRay
            if dCrtBuff:
                dNodeData['CrtUpdateBuff'] = dCrtBuff
            if lstBuffID:
                self.m_CrtBuff[iNodeID] = lstBuffID
        return dNodeData

    
    def NetTriggerUpdate(self, dNetData, iPre = 1):
        if not self.m_Base:
            return None
        self.m_Update = { }
        self.m_CurCartoon = []
        for iNodeID in list(dNetData):
            if iNodeID not in self.m_CrtStack:
                dRecv = dNetData[iNodeID]
                self.m_NetReceiveCache.append((iNodeID, dRecv))
                continue
            dCartoon = self.m_Cartoon[iNodeID]
            clsCartoon = dCartoon['cls']
            if 'Source' in dNetData[iNodeID] and not (clsCartoon.m_WorldLineOutFrame):
                continue
            if iPre:
                self.m_NetReceive[iNodeID] = self.PreProcessClientNodeData(iNodeID, dNetData[iNodeID])
            if 'WaitNet' in dCartoon:
                dCartoon.pop('WaitNet')
            if 'Enable' not in dCartoon:
                clsCartoon.DelayInit(self, dCartoon)
            else:
                clsCartoon.Update(self, dCartoon)
            if self.m_HaltRS:
                self.Halt2(self.m_HaltRS)
                return None
        
        self.m_NetReceive = { }
        if self.m_NetReceiveCache:
            self.UpdateReceiveCache()
        self.NetSkillTrigger()
        self.TryEnd()

    
    def Update(self, lstNode):
        self.m_CurCartoon = []
        self.m_Update = { }
        for iNodeID in lstNode:
            if iNodeID not in self.m_CrtStack:
                continue
            dCartoon = self.m_Cartoon[iNodeID]
            clsCartoon = dCartoon['cls']
            clsCartoon.Update(self, dCartoon)
            if self.m_HaltRS:
                self.Halt2(self.m_HaltRS)
                return None
        
        if self.m_NetReceiveCache:
            self.UpdateReceiveCache()
        self.NetSkillTrigger()
        self.TryEnd()

    
    def TimerUpdate(self):
        iFrame = self.m_Game.GetFrameNum()
        if iFrame in self.m_CallOut:
            lstNode = self.m_CallOut.pop(iFrame)
            self.Update(lstNode)
        if iFrame in self.m_SpeedCallOut:
            lstNode = self.m_SpeedCallOut.pop(iFrame)
            self.Update(lstNode)

    
    def CheckReceiveCache(self, iID):
        if iID in self.m_NetReceive:
            return True
        if self.m_NetReceiveCache:
            for iNode, dRecv in self.m_NetReceiveCache:
                if iNode == iID:
                    self.m_NetReceive[iNode] = self.PreProcessClientNodeData(iNode, dRecv)
                    self.m_NetReceiveCache.remove((iNode, dRecv))
                    return True
            
        return False

    
    def UpdateReceiveCache(self):
        lstNew = []
        self.m_NetReceiveCache = self.m_NetReceiveCache[:50]
        for iNodeID, dRecv in self.m_NetReceiveCache[:]:
            if (iNodeID, dRecv) not in self.m_NetReceiveCache:
                continue
            if iNodeID in self.m_CrtStack:
                dCartoon = self.m_Cartoon[iNodeID]
                clsCartoon = dCartoon['cls']
                if 'Source' in dRecv and not (clsCartoon.m_WorldLineOutFrame):
                    continue
                self.m_NetReceive[iNodeID] = self.PreProcessClientNodeData(iNodeID, dRecv)
                clsCartoon.Update(self, dCartoon)
                if self.m_HaltRS:
                    self.Halt2(self.m_HaltRS)
                    return None
                continue
            lstNew.append((iNodeID, dRecv))
        
        self.m_NetReceiveCache = lstNew
        self.m_NetReceive = { }

    
    def AddStack(self, dCartoon):
        self.m_Cartoon[dCartoon['ID']] = dCartoon
        self.m_CrtStack.append(dCartoon['ID'])
        if dCartoon['Casting']:
            oAttack = self.GetAttack()
            if oAttack:
                oAttack.StartCastingSkill(self, self.m_CastingEndFunc)
        if self.m_Base['pid'] and dCartoon['cls'].m_CutClient:
            self.m_Game.m_SkillMgr.m_ScenePlayerCrtNum[self.m_Base['Scene']] += dCartoon['cls'].m_CutClient

    
    def PopStack(self, dCartoon):
        if not self.m_Base:
            return None
        iCartoonID = dCartoon['ID']
        if iCartoonID not in self.m_CrtStack:
            return None
        if self.m_Base['pid'] and dCartoon['cls'].m_CutClient:
            self.m_Game.m_SkillMgr.m_ScenePlayerCrtNum[self.m_Base['Scene']] -= dCartoon['cls'].m_CutClient
        self.m_CrtStack.remove(iCartoonID)
        if not dCartoon['Casting']:
            return None
        for iNode in self.m_CrtStack:
            if self.m_Cartoon[iNode]['Casting']:
                return None
        
        oAttack = self.GetAttack()
        if oAttack:
            oAttack.OverCastingSkill(self)

    
    def SetCurCartoon(self, iNodeID):
        self.m_CurCartoon.append(iNodeID)

    
    def PopCurCartoon(self, iNodeID):
        if iNodeID not in self.m_CurCartoon:
            SkillLog.Alert('%s nodeid:%s not in curcartoon, pf:%s' % (self.m_Game.m_ID, iNodeID, self.m_Base['pfid'] if 'pfid' in self.m_Base else 0))
            return None
        self.m_CurCartoon.remove(iNodeID)

    
    def GetCartoonIndex(self, iSID):
        if iSID not in self.m_CartoonIndex:
            self.m_CartoonIndex[iSID] = 0
        iIndex = self.m_CartoonIndex[iSID]
        self.m_CartoonIndex[iSID] += 1
        return iIndex

    
    def GetCurCartoon(self):
        if not self.m_CurCartoon:
            return { }
        return self.m_Cartoon[self.m_CurCartoon[-1]]

    
    def GetCartoonBySID(self, iSID):
        dCartoon = self.GetCurCartoon()
        dChecked = { }
        while True:
            if dCartoon:
                cls = dCartoon['cls']
                if cls.m_SID == iSID:
                    break
                iID = dCartoon['ID']
                if iID in dChecked:
                    raise Exception('Cartoon出现循环引用了，会导致死循环: (%d, %s): %s' % (iID, cls, dChecked))
                dChecked[iID] = cls
                if 'Parent' not in dCartoon:
                    return { }
                dCartoon = self.m_Cartoon[dCartoon['Parent']]
                continue
        return dCartoon

    
    def GetCartoonByID(self, iNodeID):
        if iNodeID in self.m_Cartoon:
            return self.m_Cartoon[iNodeID]
        return { }

    
    def GetCurStackFlyCartoon(self):
        dCartoon = self.GetCurCartoon()
        dChecked = { }
        while True:
            if dCartoon:
                cls = dCartoon['cls']
                if 'Distance' in dCartoon:
                    break
                if 'Parent' not in dCartoon:
                    return None
                iID = dCartoon['ID']
                if iID in dChecked:
                    raise Exception('Cartoon出现循环引用了，会导致死循环: (%d, %s): %s' % (iID, cls, dChecked))
                dChecked[iID] = cls
                dCartoon = self.m_Cartoon[dCartoon['Parent']]
                continue
        return dCartoon

    
    def SendCurCartoonTriggerMsg(self, dInfo = None, sSubMsgKey = ''):
        dCartoon = self.GetCurCartoon()
        oAttack = self.GetAttack()
        if dCartoon and oAttack:
            dMsg = {
                'Skill': self,
                'Cartoon': dCartoon }
            if 'CurVID' in self.m_Update and self.m_Update['CurVID']:
                dMsg['CurVID'] = self.m_Update['CurVID']
            if dInfo:
                dMsg.update(dInfo)
            if not sSubMsgKey or sSubMsgKey not in CRT_TRIGGER_MSG_CONST:
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_TRIGGERCARTOON, oAttack, dMsg, oGame = self.m_Game)
            else:
                iSub = CRT_TRIGGER_MSG_CONST[sSubMsgKey]
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_TRIGGERCARTOON, oAttack, dMsg, iSub = iSub, oGame = self.m_Game)

    
    def SendSkillTriggerMsg(self, dExtraMsg):
        oAttack = self.GetAttack()
        if oAttack:
            dMsg = {
                'Skill': self }
            dMsg.update(dExtraMsg)
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_TRIGGERSKILL, oAttack, dMsg, oGame = self.m_Game)

    
    def Call_Out(self, iFrame, iNodeID, iAffectedBySpeed = 0):
        if iFrame < 1:
            iSID = self.m_Cartoon[iNodeID]['cls'].m_SID
            iDebug = self.m_Base.get('Debug', 0)
            SkillLog.Alert('%s skill:%d cartoon:%d callout delay invalid %d %s' % (self.m_Game.m_ID, self.m_Base['pfid'], iSID, iFrame, iDebug))
            iFrame = 1
        dCallOut = self.m_CallOut
        if iAffectedBySpeed:
            oAttack = self.GetAttack()
            if oAttack:
                iFrame = oAttack.GetChangeSpeedDelayFrame(iFrame)
                dCallOut = self.m_SpeedCallOut
        iCallFrame = self.m_Game.GetFrameNum() + iFrame
        if iCallFrame in dCallOut:
            dCallOut[iCallFrame].append(iNodeID)
        else:
            dCallOut[iCallFrame] = [
                iNodeID]
        self.m_Game.m_SkillMgr.Timer(self, iFrame, iAffectedBySpeed)

    
    def Call_Out_NoSuspend(self, iFrame, iNodeID):
        self.m_Game.m_SkillMgr.TimerNoSuspend(self, iFrame, iNodeID)

    
    def CallBackNoSuspend(self, iNode):
        self.Update([
            iNode])

    
    def SuspendCallOut(self, sKey):
        oAttack = self.GetAttack()
        if not oAttack:
            SkillLog.Alert('%s suspendcallout noattack %s %s' % (self.m_Game.m_ID, sKey, self.m_Base))
            return None
        if self.m_SuspendSource:
            self.m_SuspendSource[sKey] = 1
            return None
        self.m_SuspendSource[sKey] = 1
        self.m_SuspendLastSpeed = oAttack.m_ActionSpeed
        oSkillMgr = self.m_Game.m_SkillMgr
        oSkillMgr.RemoveTimer(self, iAffectedBySpeed = 1)
        oSkillMgr.RemoveTimer(self, iAffectedBySpeed = 0)
        for iCartoonID in self.m_CrtStack:
            dCartoon = self.m_Cartoon[iCartoonID]
            dCartoon['cls'].OnSuspend(self, dCartoon)
        
        iNowFrame = self.m_Game.GetFrameNum()
        dCallOut = self.m_SuspendCallOut
        for iCallFrame, lstNode in self.m_CallOut.items():
            iFrame = iCallFrame - iNowFrame
            if iFrame in dCallOut:
                dCallOut[iFrame].extend(lstNode)
                continue
            dCallOut[iFrame] = lstNode
        
        self.m_CallOut = { }
        dSpeedCallOut = self.m_SuspendSpeedCallOut
        for iCallFrame, lstNode in self.m_SpeedCallOut.items():
            iFrame = iCallFrame - iNowFrame
            if iFrame in dSpeedCallOut:
                dSpeedCallOut[iFrame].extend(lstNode)
                continue
            dSpeedCallOut[iFrame] = lstNode
        
        self.m_SpeedCallOut = { }

    
    def RestoreCallOut(self, sKey):
        if 'AID' not in self.m_Base:
            return None
        oAttack = self.GetAttack()
        if not oAttack:
            return None
        self.m_SuspendSource.pop(sKey, 0)
        if self.m_SuspendSource:
            return None
        for iCartoonID in self.m_CrtStack:
            dCartoon = self.m_Cartoon[iCartoonID]
            dCartoon['cls'].OnRestore(self, dCartoon)
        
        iNowFrame = self.m_Game.GetFrameNum()
        oSkillMgr = self.m_Game.m_SkillMgr
        dCallOut = self.m_CallOut
        for iFrame, lstNode in self.m_SuspendCallOut.items():
            if iFrame == 0:
                self.Update(lstNode)
                continue
            iCallTime = iNowFrame + iFrame
            if iCallTime in dCallOut:
                dCallOut[iCallTime].extend(lstNode)
                continue
            dCallOut[iCallTime] = lstNode
            oSkillMgr.Timer(self, iFrame, iAffectedBySpeed = 0)
        
        self.m_SuspendCallOut = { }
        iLastActionSpeed = self.m_SuspendLastSpeed
        self.m_SuspendLastSpeed = 0
        iCurActionSpeed = oAttack.m_ActionSpeed
        dSpeedCallOut = self.m_SpeedCallOut
        for iFrame, lstNode in self.m_SuspendSpeedCallOut.items():
            if iLastActionSpeed != iCurActionSpeed:
                iFrame = oAttack.GetChangeSpeedDelayFrame(iFrame, iLastActionSpeed)
            if iFrame == 0:
                self.Update(lstNode)
                continue
            iCallTime = iNowFrame + iFrame
            if iCallTime in dSpeedCallOut:
                dSpeedCallOut[iCallTime].extend(lstNode)
                continue
            dSpeedCallOut[iCallTime] = lstNode
            oSkillMgr.Timer(self, iFrame, iAffectedBySpeed = 1)
        
        self.m_SuspendSpeedCallOut = { }

    
    def ChangeSpeed(self, sOldKey, dFrameShaft):
        if self.m_SuspendSource or not (self.m_SpeedCallOut):
            return None
        oAttack = self.GetAttack()
        if not oAttack:
            return None
        for iCartoonID in self.m_CrtStack:
            dCartoon = self.m_Cartoon[iCartoonID]
            dCartoon['cls'].OnChangeSpeed(self, dCartoon)
        
        dCallOut = { }
        oSkillMgr = self.m_Game.m_SkillMgr
        oSkillMgr.RemoveTimer(self, iAffectedBySpeed = 1)
        iCurFrameNum = self.m_Game.GetFrameNum()
        for iOldCallFrameNum, lstNode in sorted(self.m_SpeedCallOut.items(), key = (lambda item: item[0])):
            if iOldCallFrameNum == iCurFrameNum:
                iNewFrame = 1
            else:
                iNewFrame = oAttack.GetDelayFrameOnChangeSpeed(iOldCallFrameNum, sOldKey, dFrameShaft)
                if iNewFrame <= 0:
                    iNewFrame = 1
            iCallFrameNum = iCurFrameNum + iNewFrame
            if iCallFrameNum in dCallOut:
                dCallOut[iCallFrameNum].extend(lstNode)
                continue
            dCallOut[iCallFrameNum] = lstNode
            oSkillMgr.Timer(self, iNewFrame, iAffectedBySpeed = 1)
        
        self.m_SpeedCallOut = dCallOut

    
    def AddEndFunc(self, func):
        self.m_EndFunc.append(func)

    
    def AddCastingEndFunc(self, func):
        self.m_CastingEndFunc.append(func)

    
    def GetHitTarget(self, sSuffix):
        sKey = 'HitTarget-%s' % sSuffix
        if sKey not in self.m_Collect:
            return { }
        return self.m_Collect[sKey]

    
    def RecordHitTarget(self, sSuffix):
        sKey = 'HitTarget-%s' % sSuffix
        if sKey not in self.m_Collect:
            self.m_Collect[sKey] = { }
        if 'LastVLST' in self.m_Update:
            lstVictim = self.m_Update['LastVLST']
            for iVictim in lstVictim:
                if iVictim not in self.m_Collect[sKey]:
                    self.m_Collect[sKey][iVictim] = 1
                    continue
                self.m_Collect[sKey][iVictim] += 1
            

    
    def Destory(self):
        if 'AID' not in self.m_Base:
            return None
        for func in self.m_EndFunc:
            func(self)
        
        self.DestoryAttr()

    
    def DestoryAttr(self):
        tKey = (self.m_Base['AID'], self.m_Base['ActNum'])
        iPerformSID = self.m_Base['pfid']
        if self.m_Base['pid']:
            for iCartoonID in self.m_CrtStack:
                dCartoon = self.m_Cartoon[iCartoonID]
                self.m_Game.m_SkillMgr.m_ScenePlayerCrtNum[self.m_Base['Scene']] -= dCartoon['cls'].m_CutClient
            
        self.m_CrtStack = []
        self.m_CallOut = { }
        self.m_SpeedCallOut = { }
        self.m_SuspendSource = { }
        self.m_SuspendCallOut = { }
        self.m_SuspendSpeedCallOut = { }
        self.m_SuspendLastSpeed = 0
        self.m_TempInitCrt = None
        self.m_Base = { }
        self.m_Cartoon = { }
        self.m_CartoonIndex = { }
        self.m_Collect = { }
        self.m_Custom = { }
        self.m_Cache = { }
        self.m_VarCache = { }
        self.m_Event = { }
        self.m_Update = { }
        self.m_PreProcessNetData = False
        self.m_HaltRS = None
        self.m_CrtBuff = { }
        self.m_EndFunc = []
        self.m_CastingEndFunc = []
        self.m_NetSend = { }
        self.m_NetReceive = { }
        self.m_NetReceiveCache = []
        self.m_NetBuffer = []
        self.m_NetResend = { }
        self.m_Game.m_SkillMgr.Recycle(tKey, iPerformSID)

    
    def TryEnd(self):
        if not self.m_Base:
            return None
        if self.m_CrtStack:
            return None
        self.End()

    
    def End(self):
        clsPerform = cl_perform.GetPerformModule(self.m_Base['pfid'])
        clsPerform.PerformEnd(self)
        self.Destory()

    
    def Halt(self, sReason = None):
        if sReason:
            self.m_HaltRS = sReason
        else:
            self.m_HaltRS = True
        if self.m_CurCartoon:
            return None
        self.Halt2(sReason)

    
    def Halt2(self, sReason):
        if sReason and sReason is not True:
            SkillLog.Debug('%d %d perform %d-%d halt %s' % (self.m_Game.m_ID, self.m_Base['netexclude'], self.m_Base['pfid'], self.m_Base['ActNum'], sReason))
        self.NetSkillTrigger()
        clsPerform = cl_perform.GetPerformModule(self.m_Base['pfid'])
        clsPerform.PerformHalt(self)
        oAttack = self.GetAttack()
        if oAttack:
            oAttack.OverCastingSkill(self)
        for iCartoonID in self.m_CrtStack:
            dCartoon = self.m_Cartoon[iCartoonID]
            dCartoon['cls'].ClearCartoonBullet(self, dCartoon)
        
        pfnet.GS2CSkillHalt(self)
        self.Destory()

    
    def GetAttack(self):
        if self.m_Base:
            return self.m_Game.GetObject(self.m_Base['AID'])

    
    def LogCheckErr(self, sMsg):
        if not (lib_flag.g_IsLogicLayer) and not (lib_flag.g_IsAuthorityRun):
            return None
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Base['Scene'])
        if oScene:
            sScene = '%s_%s' % (oScene.m_Map, oScene.m_Level)
        else:
            sScene = 'noscene'
        SkillLog.Debug('%s %s %s %s %s %s' % (self.m_Game.m_ID, self.m_Base['netexclude'], self.m_Base['pfid'], self.m_Base['ActNum'], sScene, sMsg))

    
    def Send(self, iNodeID, dData):
        if iNodeID in self.m_NetSend:
            self.m_NetSend[iNodeID].update(dData)
        else:
            self.m_NetSend[iNodeID] = dData
        if self.m_Resend:
            if iNodeID in self.m_NetResend:
                self.m_NetResend[iNodeID].update(dData)
            else:
                self.m_NetResend[iNodeID] = dData

    
    def SendBuffer(self, func, *args):
        self.m_NetBuffer.append((func, *args))

    
    def GetShowPlayer(self):
        if 'ShowPlayer' in self.m_Base:
            return self.m_Base['ShowPlayer']
        if 'Scene' not in self.m_Base:
            return { }
        self.m_Base['ShowPlayer'] = { }
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Base['Scene'])
        if not oScene:
            return self.m_Base['ShowPlayer']
        if self.m_Base['pid']:
            self.m_Base['HidePlayer'] = { }
            iOwnerHero = self.m_Base['AID']
            iOwnerPlayer = self.m_Base['pid']
            oAttack = self.GetAttack()
            if oAttack and not (oAttack.m_FightType & WARRIOR_HERO):
                iOwnerHero = oAttack.m_Owner
            oWarMgr = self.m_Game.m_WarMgr
            oWatchElement = oWarMgr.GetComponent('WatchElement')
            lstWatcher = oWatchElement.m_Focus2Watch[iOwnerHero] if oWatchElement and iOwnerHero in oWatchElement.m_Focus2Watch else []
            iUnShieldPF = 1 if self.m_Base['pfid'] in cl_perform.load.g_UnShieldTeamPFLibrary else 0
            for pid in oScene.m_Players:
                if pid == self.m_Base['netexclude']:
                    continue
                oHero = oWarMgr.GetHeroByPlayer(pid)
                if not oHero:
                    continue
                iShow = 1 if oHero.m_TeamPF else iUnShieldPF
                if iShow or not (self.m_CutForTeam) or oHero.m_ID in lstWatcher or pid == iOwnerPlayer:
                    self.m_Base['ShowPlayer'][pid] = 1
                    continue
                if iShow and self.m_CutForTeam == SEND_EMPTY and self.m_Base['Weapon']:
                    self.m_Base['HidePlayer'][pid] = 1
            
        else:
            self.m_Base['ShowPlayer'] = oScene.GetPlayers()
        return self.m_Base['ShowPlayer']

    
    def NetSkillStart(self):
        if not self.m_CutForSingleGame:
            dShowPlayer = self.GetShowPlayer()
            if dShowPlayer:
                pfnet.GS2CSkillStartCut(self, self.m_NetSend, dShowPlayer)
            if 'HidePlayer' in self.m_Base and self.m_Base['HidePlayer']:
                pfnet.GS2CSkillStartCut(self, { }, self.m_Base['HidePlayer'])
                pfnet.GS2CSkillHaltCut(self, self.m_Base['HidePlayer'])
        self.m_NetSend = { }
        self.NetPacketBuffer()

    
    def NetSkillTrigger(self):
        if self.m_NetSend and not (self.m_CutForSingleGame):
            dShowPlayer = self.GetShowPlayer()
            if dShowPlayer:
                pfnet.GS2CSkillTriggerCut(self, self.m_NetSend, dShowPlayer)
        self.m_NetSend = { }
        self.NetPacketBuffer()

    
    def NetPacketBuffer(self):
        if not self.m_NetBuffer:
            return None
        lstBuffer = self.m_NetBuffer
        self.m_NetBuffer = []
        for func, *args in lstBuffer:
            func(*args)
        

    
    def NetResend(self, iPlayer):
        pfnet.GS2CSkillResend(self, iPlayer, self.m_NetResend)

    
    def GetWaitNetFrame(self, iExtend = 0):
        return self.m_Game.GetFrameNum() + iExtend + 5 * GAME_FRAME

    
    def Release(self):
        self.m_Game = None

    
    def __str__(self):
        (iScene, sKey) = (self.m_Base['Scene'], self.m_Base['PFKey']) if self.m_Base else (0, '')
        return 'skill:%s-%s-%s' % (self.m_GameID, iScene, sKey)

    
    def __repr__(self):
        (iScene, sKey) = (self.m_Base['Scene'], self.m_Base['PFKey']) if self.m_Base else (0, '')
        return 'skill:%s-%s-%s' % (self.m_GameID, iScene, sKey)



class CSkillManager(cl_world.CObject):
    
    def __init__(self, oGame, iID):
        super(CSkillManager, self).__init__(oGame, iID)
        self.m_Stack = []
        self.m_Using = { }
        self.m_UsingKeyBySID = { }
        self.m_Bullet = { }
        self.m_Init = 0
        self.m_ScenePlayerCrtNum = { }
        self.m_SkillID = 0
        self.m_SkillLog = { }

    
    def Init(self):
        if self.m_Init:
            return None
        self.m_Init = 1
        self.HeartBeat()

    
    def NewSkill(self, oAttack, pfobj, dData):
        if not self.m_Init:
            return None
        if oAttack.m_Scene not in self.m_ScenePlayerCrtNum:
            self.m_ScenePlayerCrtNum[oAttack.m_Scene] = 0
        if self.m_Stack:
            oSkill = self.m_Stack.pop(0)
        else:
            iSkillID = self.NewSkillID()
            oSkill = CSkill(self.m_Game, iSkillID)
        oSkill.Init(oAttack, pfobj, dData)
        iActNum = oSkill.m_Base['ActNum']
        if iActNum > SERVER_ACTION_NUM_MAX:
            oAttack.SetLastActionNum(iActNum)
        tKey = (oSkill.m_Base['AID'], iActNum)
        if tKey in self.m_Using:
            oOldSkill = self.m_Using[tKey]
            if oOldSkill and oOldSkill.m_Base:
                SkillLog.Info('%d %d pf%s actnum %s repeat' % (self.m_Game.m_ID, oAttack.m_PlayerID, oOldSkill.m_Base['pfid'], tKey))
                oOldSkill.Halt('repeat')
        self.m_Using[tKey] = oSkill
        iPerform = pfobj.m_SID
        if iPerform not in self.m_UsingKeyBySID:
            self.m_UsingKeyBySID[iPerform] = { }
        self.m_UsingKeyBySID[iPerform][tKey] = 1
        if lib_flag.g_IsInternalRun and iPerform not in (1623, 1624, 1627, 1631):
            iAttack = oAttack.m_ID
            iMonsterID = self.m_Game.m_WarMgr.Query('TestMonster', 0)
            if iMonsterID != iAttack:
                if iAttack not in self.m_SkillLog:
                    self.m_SkillLog[iAttack] = { }
                iCurFrame = self.m_Game.GetFrameNum()
                if iCurFrame not in self.m_SkillLog[iAttack]:
                    for dPreInfo in self.m_SkillLog[iAttack].values():
                        if len(dPreInfo) >= 5:
                            OptimizationLog.Debug('%s %s skill %s' % (self.m_Game.m_ID, oAttack.m_PlayerID, list(dPreInfo.keys())))
                    
                    self.m_SkillLog[iAttack] = {
                        iCurFrame: { } }
                self.m_SkillLog[iAttack][iCurFrame][(iPerform, oSkill.m_Base['ActNum'])] = 1
        return oSkill

    
    def Recycle(self, tKey, iPerform):
        if tKey not in self.m_Using:
            return None
        oSkill = self.m_Using.pop(tKey)
        self.m_UsingKeyBySID[iPerform].pop(tKey)
        self.m_Stack.append(oSkill)

    
    def NewSkillID(self):
        self.m_SkillID += 1
        if self.m_SkillID > 65535:
            dInfo = { }
            for tKey, oSkill in self.m_Using.items():
                dInfo[tKey] = oSkill.m_Base['pfid'] if 'pfid' in oSkill.m_Base else 0
            
            SkillLog.Alert('%s unrecycled skill %s' % (self.m_Game.m_ID, dInfo))
            self.m_SkillID = 1
        return self.m_SkillID

    
    def GetSkill(self, iAttack, iActNum):
        if (iAttack, iActNum) in self.m_Using:
            return self.m_Using[(iAttack, iActNum)]

    
    def GetSkillBySID(self, iSID):
        if iSID not in self.m_UsingKeyBySID:
            return []
        lstSkill = []
        dKey = self.m_UsingKeyBySID[iSID]
        for tKey in dKey:
            lstSkill.append(self.m_Using[tKey])
        
        return lstSkill

    
    def GetSkillBySource(self, iSID, iAttack, iItem):
        if iSID not in self.m_UsingKeyBySID:
            return None
        dKey = self.m_UsingKeyBySID[iSID]
        for tKey in dKey:
            oSkill = self.m_Using[tKey]
            if iAttack and oSkill.m_Base['AID'] != iAttack:
                continue
            if iItem and oSkill.m_Base['Weapon'] != iItem:
                continue
            return oSkill
        

    
    def RemoveTimer(self, oSkill, iAffectedBySpeed = 0):
        self.Remove_Call_Out('SkillCall%s-%s' % (oSkill.m_Base['PFKey'], iAffectedBySpeed))

    
    def Timer(self, oSkill, iFrame, iAffectedBySpeed = 0):
        if 'AID' not in oSkill.m_Base:
            return None
        self.Call_Out(Functor(self.CallBack, oSkill.m_Base['AID'], oSkill.m_Base['ActNum']), iFrame, 'SkillCall%s-%s' % (oSkill.m_Base['PFKey'], iAffectedBySpeed))

    
    def CallBack(self, iAttack, iActNum):
        oSkill = self.GetSkill(iAttack, iActNum)
        if oSkill:
            oSkill.TimerUpdate()

    
    def TimerNoSuspend(self, oSkill, iFrame, iNode):
        if 'AID' not in oSkill.m_Base:
            return None
        self.Call_Out(Functor(self.CallBackNoSuspend, oSkill.m_Base['AID'], oSkill.m_Base['ActNum'], iNode), iFrame, 'SkillCallNoSuspend-%s' % oSkill.m_Base['PFKey'])

    
    def CallBackNoSuspend(self, iAttack, iActNum, iNode):
        oSkill = self.GetSkill(iAttack, iActNum)
        if oSkill:
            oSkill.CallBackNoSuspend(iNode)

    
    def HeartBeat(self):
        self.Call_Out(self.HeartBeat, 5 * GAME_FRAME, 'SkillHeartBeat')
        iNowFrame = self.m_Game.GetFrameNum()
        lstRemove = []
        for oSkill in self.m_Using.values():
            if oSkill.m_CheckType & CRT_CHECK_CLIENT:
                for iCartoon in oSkill.m_CrtStack:
                    dCartoon = oSkill.m_Cartoon[iCartoon]
                    if 'WaitNet' not in dCartoon:
                        break
                    if dCartoon['WaitNet'] > iNowFrame:
                        break
                
        
        lstLog = []
        for oSkill in lstRemove:
            lstLog.append('%s_%s_%s' % (oSkill.m_Base['AID'], oSkill.m_Base['pfid'], oSkill.m_Base['ActNum']))
            oSkill.Halt('overtime')
        
        if lstLog:
            lstLog.insert(0, 'skill net halt')
            SkillLog.Info(' '.join(lstLog))

    
    def RegisterBullet(self, oBullet, iAttack, iActNum, iCartoonID):
        tkey = oBullet.Key()
        oSkill = self.GetSkill(iAttack, iActNum)
        if not oSkill:
            return None
        if tkey in self.m_Bullet:
            SkillLog.Error('%s %s repeat bullet key:%s' % (self.m_Game.m_ID, oSkill.m_Base['pfid'], tkey))
            return None
        if iCartoonID in oSkill.m_Cartoon:
            self.m_Bullet[tkey] = (iAttack, iActNum, iCartoonID)

    
    def GetBullet(self, tkey):
        if tkey not in self.m_Bullet:
            return None
        (objID, name) = tkey
        obj = self.m_Game.GetObject(objID)
        if not obj:
            return None
        if name:
            return obj.m_BulletDict.get(name, None)
        return obj

    
    def DeleteBullet(self, tkey, sReason):
        if tkey not in self.m_Bullet:
            return None
        (objID, name) = tkey
        obj = self.m_Game.GetObject(objID)
        if not obj:
            self.m_Bullet.pop(tkey)
            return None
        if name:
            com = obj.m_BulletDict.get(name, None)
            if com:
                com.Unstall()
            else:
                obj.Remove(sReason)
        None.m_Bullet.pop(tkey)

    
    def GetSkillCartoonByBullet(self, tkey):
        if tkey not in self.m_Bullet:
            return None
        (iAttack, iActNum, iCartoonID) = self.m_Bullet[tkey]
        oSkill = self.GetSkill(iAttack, iActNum)
        if oSkill and iCartoonID in oSkill.m_CrtStack:
            return (oSkill, oSkill.m_Cartoon[iCartoonID])
        self.DeleteBullet(tkey, 'notexist')

    
    def Release(self):
        self.m_Init = 0
        for oSkill in list(self.m_Using.values()):
            if not oSkill.m_Base:
                continue
            
            try:
                oSkill.Halt2(sReason = None)
            except:
                PythonError()
                if oSkill.m_Base:
                    oSkill.DestoryAttr()

        
        for oSkill in self.m_Stack:
            oSkill.Release()
        
        if self.m_Bullet:
            SkillLog.Error('%s skillmanager clear has bullet %s' % (self.m_Game.m_ID, self.m_Bullet.keys()))
        self.m_Bullet = { }
        self.m_Using = { }
        self.m_Stack = []
        self.RemoveFromList()

    
    def LeaveScene(self, iScene):
        for oSkill in list(self.m_Using.values()):
            if not oSkill.m_Base:
                continue
            if oSkill.m_Base['Scene'] != iScene:
                continue
            self.TryHaltSkill(oSkill)
        

    
    def AttackLeaveScene(self, iAttack):
        lstUseSkill = []
        for (iCurAttack, _), oSkill in self.m_Using.items():
            if iCurAttack == iAttack:
                lstUseSkill.append(oSkill)
        
        for oSkill in lstUseSkill:
            self.TryHaltSkill(oSkill)
        

    
    def TryHaltSkill(self, oSkill):
        if not oSkill.m_Base:
            return None
        
        try:
            oSkill.Halt()
        except:
            PythonError()
            if not oSkill.m_Base:
                return None
        else:
            oSkill.DestoryAttr()


    
    def OnPlayerMapLoadOK(self, pid, iScene):
        for oSkill in self.m_Using.values():
            if oSkill.m_Base['Scene'] != iScene:
                continue
            if oSkill.m_Resend:
                oSkill.NetResend(pid)
        



def NewSkillManager(oGame):
    iID = oGame.NewNPCID()
    oSkillMgr = CSkillManager(oGame, iID)
    oGame.CreateObject(iID, oSkillMgr)
    oSkillMgr.Init()
    return oSkillMgr

