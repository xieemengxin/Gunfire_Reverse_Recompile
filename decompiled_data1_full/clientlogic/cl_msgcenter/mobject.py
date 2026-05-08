# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_msgcenter/mobject.pyc
# RelativePath: clientlogic/cl_msgcenter/mobject.pyc
# Source Generated with Decompyle++
# File: mobject.pyc (Python 3.6)

from cl_commondefines import RESCUE_SUBMSG_START, PF_SUBMSG_THROW, ATTACKERSUBMSG_BUILD, ATTACKERSUBMSG_NORMAL, DUAL_STATE_END, DUAL_STATE_BEGIN, WARRIOR_MASK, PF_SUBMSG_CAREERPF, PF_SUBMSG_SWITCHWEAPON, PF_SUBMSG_SAVE, PF_SUBMSG_FILLBULLET, PF_SUBMSG_CAREERPF, SMITHNPCSUBMSG_ADD_INSCRIPTION, SMITHNPCSUBMSG_UPGRADE, SMITHNPCSUBMSG_RECAST, RELIC_SUBMSG_GENERATE_DROP, RELIC_SUBMSG_GENERATE_GOOD, RELIC_SUBMSG_GENERATE_CHOOSE, RELIC_SUBMSG_GENERATE_SURVIVOR, DPSUBMSG_DEFAULT, DPSUBMSG_NOFIRE, PF_PER_SKILL, PF_SUBMSG_CLIENTACTIVE, PF_SUBMSG_COMMON, PICK_INKBEAD, PICK_SPECIALINKBEAD, CRT_RANGECHECK_ENTER, CRT_RANGECHECK_EXIT, RELIC_SUBMSG_GENERATE_LOTTERY, CHARGECARTOON_SUBMSG_START, S7_ALL_PERFORM_ENABLE
from cl_object.logging import WarobjLog, ErrLog
from cl_only import TraceLog, PythonError
import cl_perform
import cl_msgcenter
from .defines import g_Core_Msg, MSG_WAR_CUSTOM_USEPERFORM_BEFORE, MSG_WAR_MAIN_ATTACK, MSG_WAR_RESCUE, MSG_WAR_WEAPONPEOFROM_START, MSG_WARMGR_LEVELNODEFINISH, MSG_CMD_JUMP, MSG_WAR_CURE, MSG_WAR_RECEIVEDAM, MSG_WAR_STATE, MSG_WAR_ATTACKPF, MSG_WAR_PERFORM, MSG_WAR_ATTACK, MSG_WAR_DEALTOTALDAM, MSG_WAR_ASSISTKILL, MSG_WAR_KILL, MSG_WAR_PREDICTDAM, MSG_WAR_DUALSTATE, MSGSUBOFFSET, MSG_WAR_ADDIMMOBILIZE, MSG_WAR_UNHOLD_WEAPON, MSG_CMD_MOVE, MSG_CMD_OPENSNIPE, MSG_WAR_SHIELD_CURE, MSG_WAR_CAUSEDEBUFF, MSG_WAR_COSTBULLET, MSG_WAR_PERFORM_HALT, MSG_WAR_PERFORM_END, MSG_WAR_ATTACK_END, MSG_WAR_WEAPONFIRE, MSG_WAR_DP, MSG_WAR_PICK, MSG_WAR_DIE_BEFORE_MAIN, MSG_WAR_RECEIVEDAMED, MSG_WAR_BREAKARMOR, MSG_WAR_DIE_BEFORE, MSG_WAR_PERFORM_START, GetMsgKey, MSG_WAR_PREDICTDAMED, MSG_WAR_BEFORESMITHNPC, MSG_WAR_GENERATE_RELIC_BEFORE, MSG_WAR_ENTERSCENE, MSG_WAR_TALENT_CHOOSE_BEFORE, MSG_WARMSG_PHASESTART, MSG_WAR_TRIGGERCARTOON, MSG_WAR_TRIGGERCRT_RANGECHECK, MSG_WAR_BARRIER_COLLIDED, MSG_WAR_HALT_CASTINGSKILL, MSG_WARMGR_LEVELNODEINIT, MSG_WAR_BEFORE_CHANGE_INKVALUE, MSG_WAR_USE_CAREERPF, MSG_WAR_INITGOODS, MSG_WAR_SHOPREFRESH, MSG_WAR_UPGRADEREWARD_CREATE, MSG_WAR_EVENTNPC_REWARD_RELIC, MSG_WAR_CHARGECARTOON_TRIGGER, MSG_WAR_CUSTOMSTATE_START, MSG_WAR_S7_CONTAINER_OPERATION

class CEventControl(object):
    m_UsePriority = [
        MSG_WARMGR_LEVELNODEFINISH,
        GetMsgKey(MSG_WAR_PICK, PICK_INKBEAD),
        GetMsgKey(MSG_WAR_PICK, PICK_SPECIALINKBEAD),
        MSG_WAR_PICK,
        MSG_WAR_PREDICTDAMED,
        GetMsgKey(MSG_WAR_PERFORM_START, PF_SUBMSG_THROW),
        GetMsgKey(MSG_WAR_PERFORM_START, PF_SUBMSG_COMMON),
        GetMsgKey(MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF),
        GetMsgKey(MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF),
        MSG_WAR_DIE_BEFORE,
        MSG_WAR_BREAKARMOR,
        MSG_WAR_RECEIVEDAMED,
        MSG_WAR_ENTERSCENE,
        MSG_WAR_ATTACK,
        GetMsgKey(MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL),
        MSG_WAR_CUSTOM_USEPERFORM_BEFORE,
        MSG_WAR_TALENT_CHOOSE_BEFORE,
        MSG_WARMSG_PHASESTART,
        MSG_WAR_TRIGGERCARTOON,
        MSG_WAR_BARRIER_COLLIDED,
        MSG_WAR_TRIGGERCRT_RANGECHECK,
        GetMsgKey(MSG_WAR_TRIGGERCRT_RANGECHECK, CRT_RANGECHECK_ENTER),
        MSG_WARMGR_LEVELNODEINIT,
        MSG_WAR_BEFORE_CHANGE_INKVALUE,
        MSG_WAR_INITGOODS,
        MSG_WAR_SHOPREFRESH,
        MSG_WAR_UPGRADEREWARD_CREATE,
        MSG_WAR_DIE_BEFORE_MAIN,
        GetMsgKey(MSG_WAR_GENERATE_RELIC_BEFORE, RELIC_SUBMSG_GENERATE_DROP),
        GetMsgKey(MSG_WAR_GENERATE_RELIC_BEFORE, RELIC_SUBMSG_GENERATE_GOOD),
        GetMsgKey(MSG_WAR_GENERATE_RELIC_BEFORE, RELIC_SUBMSG_GENERATE_CHOOSE),
        GetMsgKey(MSG_WAR_GENERATE_RELIC_BEFORE, RELIC_SUBMSG_GENERATE_LOTTERY),
        MSG_WAR_EVENTNPC_REWARD_RELIC,
        GetMsgKey(MSG_WAR_CHARGECARTOON_TRIGGER, CHARGECARTOON_SUBMSG_START),
        GetMsgKey(MSG_WAR_WEAPONFIRE, DPSUBMSG_DEFAULT),
        MSG_WAR_CUSTOMSTATE_START,
        GetMsgKey(MSG_WAR_ATTACKPF, ATTACKERSUBMSG_NORMAL),
        GetMsgKey(MSG_WAR_S7_CONTAINER_OPERATION, S7_ALL_PERFORM_ENABLE)]
    
    def __init__(self):
        self.m_RegisterEvent = { }

    
    def Release(self):
        for objRegister in self.m_RegisterEvent.values():
            objRegister.Release()
        
        self.m_RegisterEvent = { }

    
    def AddFunction(self, iMsg, func, sKey, iSub, iOnce, iPriority):
        iKey = GetMsgKey(iMsg, iSub)
        if iKey not in self.m_RegisterEvent:
            if iKey in self.m_UsePriority:
                self.m_RegisterEvent[iKey] = CNewPriorityControl(iKey)
            else:
                self.m_RegisterEvent[iKey] = CNewRegisterControl(iKey)
        self.m_RegisterEvent[iKey].AddFunction(func, sKey, iOnce, iPriority)

    
    def DoneEvent(self, iMsg, sKey, iSub):
        iKey = GetMsgKey(iMsg, iSub)
        if iKey not in self.m_RegisterEvent:
            return None
        objRegister = self.m_RegisterEvent[iKey]
        objRegister.DoneEvent(sKey)

    
    def ReceiveMsg(self, oListener, iMsg, dInfo = None, iSub = -1):
        lstKey = [
            GetMsgKey(iMsg, iSub)]
        if iSub != -1:
            lstKey.append(GetMsgKey(iMsg, -1))
        for iKey in lstKey:
            if iKey not in self.m_RegisterEvent:
                return None
            objRegister = self.m_RegisterEvent[iKey]
            objRegister.DoEvent(oListener, dInfo)
        



class CNewRegisterControl(object):
    
    def __init__(self, iKey):
        self.m_Msg = iKey
        self.m_NotEmpty = 0
        self.m_InService = 0
        self.m_Function = { }
        self.m_DelayAddFunc = { }
        self.m_Done = { }

    
    def Release(self):
        self.m_Function = { }
        self.m_DelayAddFunc = { }

    
    def AddFunction(self, func, sKey, iOnce, _iPriority):
        if self.m_InService:
            if sKey in self.m_Done:
                del self.m_Done[sKey]
            self.m_DelayAddFunc[sKey] = (iOnce, func)
            return None
        self.m_Function[sKey] = (iOnce, func)
        self.m_NotEmpty = 1

    
    def DoneEvent(self, sKey):
        if self.m_InService:
            self.m_Done[sKey] = 1
            return None
        if sKey in self.m_Function:
            del self.m_Function[sKey]
        if sKey in self.m_DelayAddFunc:
            del self.m_DelayAddFunc[sKey]
        if not self.m_Function:
            self.m_NotEmpty = 0

    
    def DoEvent(self, oListener, dEvent):
        self.m_InService += 1
        for sKey in self.m_Function:
            if self.m_Done and sKey in self.m_Done:
                continue
            (iOnce, func) = self.m_Function[sKey]
            if iOnce:
                self.m_Done[sKey] = 1
            func(oListener, dEvent)
        
        self.m_InService -= 1
        if self.m_InService > 0:
            return None
        if self.m_Done:
            for sKey in self.m_Done:
                self.DoneEvent(sKey)
            
            self.m_Done = { }
        if self.m_DelayAddFunc:
            self.m_Function.update(self.m_DelayAddFunc)
            self.m_DelayAddFunc = { }
            self.m_NotEmpty = 1

    
    def DoCoreEvent(self, oListener, dEvent):
        self.m_InService += 1
        for sKey in self.m_Function:
            if self.m_Done and sKey in self.m_Done:
                continue
            
            try:
                (iOnce, func) = self.m_Function[sKey]
                if iOnce:
                    self.m_Done[sKey] = 1
                func(oListener, dEvent)
            except:
                PythonError()

        
        self.m_InService -= 1
        if self.m_InService > 0:
            return None
        if self.m_Done:
            for sKey in self.m_Done:
                self.DoneEvent(sKey)
            
            self.m_Done = { }
        if self.m_DelayAddFunc:
            self.m_Function.update(self.m_DelayAddFunc)
            self.m_DelayAddFunc = { }
            self.m_NotEmpty = 1



class CNewPriorityControl(object):
    
    def __init__(self, iKey):
        self.m_Msg = iKey
        self.m_NotEmpty = 0
        self.m_InService = 0
        self.m_DelayAddFunc = { }
        self.m_Function = { }
        self.m_NeedToSort = False

    
    def Release(self):
        self.m_Function = { }
        self.m_DelayAddFunc = { }

    
    def AddFunction(self, func, sKey, iOnce, iPriority):
        if self.m_InService > 0:
            self.m_DelayAddFunc[sKey] = (func, iOnce, iPriority)
            return None
        if iPriority not in self.m_Function:
            self.m_Function[iPriority] = { }
            self.m_NeedToSort = True
        self.m_Function[iPriority][sKey] = (func, iOnce)
        self.m_NotEmpty = 1

    
    def DoneEvent(self, sKey):
        for dPriority in self.m_Function.values():
            if sKey in dPriority:
                dPriority.pop(sKey)
                break
        
        if sKey in self.m_DelayAddFunc:
            self.m_DelayAddFunc.pop(sKey)
        for dPriority in self.m_Function.values():
            if dPriority:
                break
        else:
            self.m_NotEmpty = 0

    
    def DoEvent(self, oListener, dEvent):
        if self.m_NeedToSort:
            dSorted = { }
            lstPriority = sorted(self.m_Function, reverse = True)
            for iPriority in lstPriority:
                dSorted[iPriority] = self.m_Function[iPriority]
            
            self.m_Function = dSorted
            self.m_NeedToSort = False
        iHalt = 0
        self.m_InService += 1
        for dPriority in self.m_Function.values():
            for sKey in list(dPriority):
                if sKey not in dPriority:
                    continue
                if 'Halt' in dEvent or 'HaltPriMsg' in dEvent:
                    iHalt = 1
                    break
                (func, iOnce) = dPriority[sKey]
                if iOnce:
                    self.DoneEvent(sKey)
                func(oListener, dEvent)
            
            if iHalt:
                break
        
        self.m_InService -= 1
        if self.m_InService > 0:
            return None
        if self.m_DelayAddFunc:
            dDelay = self.m_DelayAddFunc
            self.m_DelayAddFunc = { }
            for sKey, (func, iOnce, iPriority) in dDelay.items():
                self.AddFunction(func, sKey, iOnce, iPriority)
            

    
    def DoCoreEvent(self, oListener, dEvent):
        if self.m_NeedToSort:
            dSorted = { }
            lstPriority = sorted(self.m_Function, reverse = True)
            for iPriority in lstPriority:
                dSorted[iPriority] = self.m_Function[iPriority]
            
            self.m_Function = dSorted
            self.m_NeedToSort = False
        iHalt = 0
        self.m_InService += 1
        for dPriority in self.m_Function.values():
            for sKey in list(dPriority):
                if sKey not in dPriority:
                    continue
                if 'Halt' in dEvent or 'HaltPriMsg' in dEvent:
                    iHalt = 1
                    break
                
                try:
                    (func, iOnce) = dPriority[sKey]
                    if iOnce:
                        self.DoneEvent(sKey)
                    func(oListener, dEvent)
                except:
                    PythonError()

            
            if iHalt:
                break
        
        self.m_InService -= 1
        if self.m_InService > 0:
            return None
        if self.m_DelayAddFunc:
            dDelay = self.m_DelayAddFunc
            self.m_DelayAddFunc = { }
            for sKey, (func, iOnce, iPriority) in dDelay.items():
                self.AddFunction(func, sKey, iOnce, iPriority)
            



class CMsgCenter(object):
    
    def __init__(self, oGame):
        self.m_Game = oGame
        self.m_AttentionList = { }
        self.m_ExtendFunc = { }
        for iKey, tFunc in GetAllStaticExtendFunc().items():
            self.m_ExtendFunc[iKey] = list(tFunc)
        

    
    def Release(self):
        for oAttention in self.m_AttentionList.values():
            oAttention.Release()
        
        self.m_AttentionList = { }
        self.m_ExtendFunc = { }
        self.m_Game = None

    
    def ReceiveMsg(self, iOwner, iMsg, dInfo):
        if not iOwner:
            return None
        if dInfo and 'sub' in dInfo:
            iSub = dInfo['sub']
        else:
            iSub = -1
        lstKey = [
            GetMsgKey(iMsg, iSub)]
        if iSub != -1:
            lstKey.append(GetMsgKey(iMsg, -1))
        for iKey in lstKey:
            if iKey not in self.m_AttentionList:
                return None
            self.m_AttentionList[iKey].ReceiveMsg(iOwner, iKey, dInfo)
        

    
    def AddAttentionFunc(self, iListener, iTarget, iMsg, iSub, func, sKey):
        if not self.m_Game:
            sText = 'msgcenter nogame %s' % sKey
            TraceLog('err', sText)
            ErrLog.Alert(sText)
            return None
        iKey = GetMsgKey(iMsg, iSub)
        if iKey not in self.m_AttentionList:
            self.m_AttentionList[iKey] = CAttention(self.m_Game, iMsg)
            if iMsg in g_Core_Msg:
                self.AddExtendFunc(iKey, self.m_AttentionList[iKey].ReceiveCoreMsg)
            else:
                self.AddExtendFunc(iKey, self.m_AttentionList[iKey].ReceiveMsg)
        self.m_AttentionList[iKey].AddAttentionFunc(iTarget, iListener, func, sKey)
        oTarget = self.m_Game.GetObject(iTarget)
        if oTarget:
            oTarget.ReceiveAttention(iKey)

    
    def DoneAttention(self, iListener, iTarget, iMsg, iSub, sKey):
        iKey = GetMsgKey(iMsg, iSub)
        if iKey not in self.m_AttentionList:
            return None
        self.m_AttentionList[iKey].DoneAttention(iTarget, iListener, sKey)

    
    def RemoveAttention(self, iListener, iTarget, iMsg, iSub):
        iKey = GetMsgKey(iMsg, iSub)
        if iKey not in self.m_AttentionList:
            return None
        self.m_AttentionList[iKey].RemoveAttention(iTarget, iListener)

    
    def ClearAttention(self, iTarget, iKey):
        if iKey not in self.m_AttentionList:
            return None
        self.m_AttentionList[iKey].ClearAttention(iTarget)

    
    def AddExtendFunc(self, iKey, func):
        if iKey in self.m_ExtendFunc:
            self.m_ExtendFunc[iKey].append(func)
        else:
            self.m_ExtendFunc[iKey] = [
                func]



class CAttention(object):
    
    def __init__(self, oGame, iMsg):
        self.m_Msg = iMsg
        self.m_Game = oGame
        self.m_AttentionFunc = { }

    
    def AddAttentionFunc(self, iOwner, iListener, func, sKey):
        if iOwner not in self.m_AttentionFunc:
            self.m_AttentionFunc[iOwner] = { }
        if iListener not in self.m_AttentionFunc[iOwner]:
            self.m_AttentionFunc[iOwner][iListener] = { }
        self.m_AttentionFunc[iOwner][iListener][sKey] = func

    
    def DoneAttention(self, iOwner, iListener, sKey):
        if iOwner in self.m_AttentionFunc and iListener in self.m_AttentionFunc[iOwner] and sKey in self.m_AttentionFunc[iOwner][iListener]:
            del self.m_AttentionFunc[iOwner][iListener][sKey]
            if not self.m_AttentionFunc[iOwner][iListener]:
                del self.m_AttentionFunc[iOwner][iListener]

    
    def RemoveAttention(self, iOwner, iListener):
        if iOwner in self.m_AttentionFunc and iListener in self.m_AttentionFunc[iOwner]:
            del self.m_AttentionFunc[iOwner][iListener]

    
    def ClearAttention(self, iOwner):
        if iOwner in self.m_AttentionFunc:
            del self.m_AttentionFunc[iOwner]

    
    def ReceiveMsg(self, oOwner, iKey, dInfo):
        if not oOwner:
            return None
        iOwner = oOwner.m_ID
        if iOwner not in self.m_AttentionFunc:
            return None
        dListenInfo = self.m_AttentionFunc[iOwner]
        for iListener in list(dListenInfo):
            if iListener not in dListenInfo:
                continue
            oListener = self.m_Game.GetObject(iListener)
            if not oListener:
                self.RemoveAttention(iOwner, iListener)
                continue
            for sKey in list(dListenInfo[iListener]):
                if iListener not in dListenInfo:
                    break
                if sKey not in dListenInfo[iListener]:
                    continue
                func = dListenInfo[iListener][sKey]
                func(oListener, oOwner, dInfo)
            
        

    
    def ReceiveCoreMsg(self, oOwner, iKey, dInfo):
        if not oOwner:
            return None
        iOwner = oOwner.m_ID
        if iOwner not in self.m_AttentionFunc:
            return None
        dListenInfo = self.m_AttentionFunc[iOwner]
        for iListener in list(dListenInfo):
            if iListener not in dListenInfo:
                continue
            oListener = self.m_Game.GetObject(iListener)
            if not oListener:
                self.RemoveAttention(iOwner, iListener)
                continue
            for sKey in list(dListenInfo[iListener]):
                if iListener not in dListenInfo:
                    break
                if sKey not in dListenInfo[iListener]:
                    continue
                func = dListenInfo[iListener][sKey]
                
                try:
                    func(oListener, oOwner, dInfo)
                except:
                    PythonError()

            
        

    
    def Release(self):
        self.m_AttentionFunc = { }
        self.m_Game = None



class CGameGlobalAttention(object):
    
    def __init__(self, oGame):
        self.m_Attention = { }
        self.m_Game = oGame

    
    def AddAttention(self, iListener, iMsg, cbfunc, sKey):
        if iMsg not in self.m_Attention:
            self.m_Attention[iMsg] = { }
            if iMsg in g_Core_Msg:
                self.m_Game.m_MsgCenter.AddExtendFunc(iMsg, self.ReceiveCoreMsg)
            else:
                self.m_Game.m_MsgCenter.AddExtendFunc(iMsg, self.ReceiveMsg)
        if iListener not in self.m_Attention[iMsg]:
            self.m_Attention[iMsg][iListener] = { }
        self.m_Attention[iMsg][iListener][sKey] = cbfunc

    
    def DoneAttention(self, iListener, iMsg, sKey):
        if iMsg not in self.m_Attention:
            return None
        if iListener not in self.m_Attention[iMsg]:
            return None
        if sKey not in self.m_Attention[iMsg][iListener]:
            return None
        self.m_Attention[iMsg][iListener].pop(sKey)

    
    def RemoveAttention(self, iListener):
        for _, dPlayer in self.m_Attention.items():
            if iListener in dPlayer:
                dPlayer.pop(iListener)
        

    
    def ReceiveMsg(self, oOwner, iMsg, dMsgInfo):
        if not self.m_Attention[iMsg]:
            return None
        for iListener, dAttention in list(self.m_Attention[iMsg].items()):
            oListener = self.m_Game.GetObject(iListener)
            if not oListener:
                self.RemoveAttention(iListener)
                continue
            for _, func in list(dAttention.items()):
                func(oListener, oOwner, dMsgInfo)
            
        

    
    def ReceiveCoreMsg(self, oOwner, iMsg, dMsgInfo):
        if not self.m_Attention[iMsg]:
            return None
        for iListener, dAttention in list(self.m_Attention[iMsg].items()):
            oListener = self.m_Game.GetObject(iListener)
            if not oListener:
                self.RemoveAttention(iListener)
                continue
            for _, func in list(dAttention.items()):
                
                try:
                    func(oListener, oOwner, dMsgInfo)
                except:
                    PythonError()

            
        

    
    def Release(self):
        self.m_Game = None
        self.m_Attention = { }



def MsgHaltCastingSkill(oOwner, iKey, dInfo):
    if not oOwner:
        return None
    if not oOwner.m_FightType & WARRIOR_MASK:
        return None
    if 'UnCrtByOwnerSign' in dInfo and dInfo['UnCrtByOwnerSign']:
        return None
    oGame = oOwner.m_Game
    iWeapon = 0
    pfid = 0
    if 'Skill' in dInfo:
        oSkill = dInfo['Skill']
        iWeapon = oSkill.m_Base['Weapon']
        pfid = oSkill.m_Base['pfid']
    elif 'Weapon' in dInfo:
        iWeapon = dInfo['Weapon']
    for iActNum, dCasting in oOwner.GetAllCasting():
        iPerform = dCasting['pfid']
        clsPerform = cl_perform.GetPerformModule(iPerform)
        dHaltInfo = clsPerform.m_HaltInfo
        if (iKey in dHaltInfo or pfid) and pfid in clsPerform.m_IgnoreHalt:
            continue
        if iWeapon and dCasting['Weapon'] and iWeapon != dCasting['Weapon']:
            continue
        oSkill = oGame.m_SkillMgr.GetSkill(oOwner.m_ID, iActNum)
        oSkill.Halt()
    
    dInfo['MsgKey'] = iKey
    cl_msgcenter.SendMsg(MSG_WAR_HALT_CASTINGSKILL, oOwner, dInfo)
    if not oOwner.m_PlayerID:
        return None
    oRescueElement = oOwner.m_Game.m_WarMgr.GetComponent('RescueElement')
    if oRescueElement:
        iPerform = 0
        if 'Skill' in dInfo:
            oSkill = dInfo['Skill']
            iPerform = oSkill.m_Base['pfid']
            if iPerform in oRescueElement.m_IgnoreHalt:
                return None
        if iKey not in oRescueElement.m_HaltInfo or not oRescueElement.m_HaltInfo[iKey]:
            return None
        if oOwner.m_ID in oRescueElement.m_RescueCache:
            WarobjLog.Info(f'''msghaltrescue {iKey} {oOwner.m_PlayerID} {oOwner.m_ID} {iPerform}''')
        oRescueElement.HaltRescue(oOwner, dInfo)


def SkillCacheEvent(oOwner, iKey, dInfo):
    if 'Skill' not in dInfo:
        return None
    oSkill = dInfo['Skill']
    if iKey in oSkill.m_Event:
        dEvent = oSkill.m_Event[iKey]
        lstRemove = []
        for sKey, (func, iOnce, iPriority) in dEvent.items():
            func(oOwner, dInfo)
            if iOnce:
                lstRemove.append(sKey)
        
        for sKey in lstRemove:
            dEvent.pop(sKey)
        

g_StaticExtendFunc = {
    RESCUE_SUBMSG_START * MSGSUBOFFSET + MSG_WAR_RESCUE: (MsgHaltCastingSkill,),
    DUAL_STATE_END * MSGSUBOFFSET + MSG_WAR_DUALSTATE: (MsgHaltCastingSkill,),
    DUAL_STATE_BEGIN * MSGSUBOFFSET + MSG_WAR_DUALSTATE: (MsgHaltCastingSkill,),
    MSG_WAR_USE_CAREERPF: (MsgHaltCastingSkill,),
    MSG_WAR_WEAPONPEOFROM_START: (MsgHaltCastingSkill,),
    MSG_WAR_ADDIMMOBILIZE: (MsgHaltCastingSkill,),
    MSG_WAR_UNHOLD_WEAPON: (MsgHaltCastingSkill,),
    MSG_CMD_JUMP: (MsgHaltCastingSkill,),
    MSG_CMD_OPENSNIPE: (MsgHaltCastingSkill,),
    MSG_WAR_PERFORM_START: (MsgHaltCastingSkill, SkillCacheEvent),
    MSG_CMD_MOVE: (MsgHaltCastingSkill,),
    MSG_WAR_CAUSEDEBUFF: (SkillCacheEvent,),
    MSG_WAR_SHIELD_CURE: (SkillCacheEvent,),
    MSG_WAR_COSTBULLET: (SkillCacheEvent,),
    MSG_WAR_PERFORM_HALT: (SkillCacheEvent,),
    MSG_WAR_PERFORM_END: (SkillCacheEvent,),
    MSG_WAR_ATTACK_END: (SkillCacheEvent,),
    MSG_WAR_WEAPONFIRE: (SkillCacheEvent,),
    MSG_WAR_DP: (MsgHaltCastingSkill, SkillCacheEvent) }
MSG_SUB_LIST = {
    MSG_WAR_TRIGGERCRT_RANGECHECK: (CRT_RANGECHECK_ENTER, CRT_RANGECHECK_EXIT),
    MSG_WAR_GENERATE_RELIC_BEFORE: (RELIC_SUBMSG_GENERATE_DROP, RELIC_SUBMSG_GENERATE_GOOD, RELIC_SUBMSG_GENERATE_CHOOSE, RELIC_SUBMSG_GENERATE_SURVIVOR),
    MSG_WAR_MAIN_ATTACK: (ATTACKERSUBMSG_NORMAL, ATTACKERSUBMSG_BUILD),
    MSG_WAR_BEFORESMITHNPC: (SMITHNPCSUBMSG_UPGRADE, SMITHNPCSUBMSG_RECAST, SMITHNPCSUBMSG_ADD_INSCRIPTION),
    MSG_WAR_CURE: (ATTACKERSUBMSG_NORMAL, ATTACKERSUBMSG_BUILD),
    MSG_WAR_RECEIVEDAM: (ATTACKERSUBMSG_NORMAL, ATTACKERSUBMSG_BUILD),
    MSG_WAR_STATE: (ATTACKERSUBMSG_NORMAL, ATTACKERSUBMSG_BUILD),
    MSG_WAR_ATTACKPF: (ATTACKERSUBMSG_NORMAL, ATTACKERSUBMSG_BUILD),
    MSG_WAR_PERFORM: (ATTACKERSUBMSG_NORMAL, ATTACKERSUBMSG_BUILD),
    MSG_WAR_ATTACK: (ATTACKERSUBMSG_NORMAL, ATTACKERSUBMSG_BUILD),
    MSG_WAR_ASSISTKILL: (ATTACKERSUBMSG_NORMAL, ATTACKERSUBMSG_BUILD),
    MSG_WAR_KILL: (ATTACKERSUBMSG_NORMAL, ATTACKERSUBMSG_BUILD),
    MSG_WAR_DEALTOTALDAM: (ATTACKERSUBMSG_NORMAL, ATTACKERSUBMSG_BUILD),
    MSG_WAR_PREDICTDAM: (ATTACKERSUBMSG_NORMAL, ATTACKERSUBMSG_BUILD),
    MSG_WAR_PERFORM_END: (PF_SUBMSG_CAREERPF, PF_SUBMSG_FILLBULLET, PF_SUBMSG_SAVE, PF_SUBMSG_SWITCHWEAPON, PF_SUBMSG_THROW, PF_PER_SKILL),
    MSG_WAR_PERFORM_START: (PF_SUBMSG_CAREERPF, PF_SUBMSG_FILLBULLET, PF_SUBMSG_SAVE, PF_SUBMSG_SWITCHWEAPON, PF_SUBMSG_THROW, PF_PER_SKILL, PF_SUBMSG_CLIENTACTIVE),
    MSG_WAR_ATTACK_END: (DPSUBMSG_DEFAULT, DPSUBMSG_NOFIRE),
    MSG_WAR_DP: (DPSUBMSG_DEFAULT, DPSUBMSG_NOFIRE) }
g_StaticExtendFuncAutoSub = {
    MSG_WAR_TRIGGERCRT_RANGECHECK: (SkillCacheEvent,),
    MSG_WAR_MAIN_ATTACK: (SkillCacheEvent,),
    MSG_WAR_PERFORM_END: (SkillCacheEvent,),
    MSG_WAR_PERFORM_START: (MsgHaltCastingSkill, SkillCacheEvent),
    MSG_WAR_CURE: (SkillCacheEvent,),
    MSG_WAR_KILL: (SkillCacheEvent,),
    MSG_WAR_PREDICTDAM: (SkillCacheEvent,),
    MSG_WAR_DEALTOTALDAM: (SkillCacheEvent,),
    MSG_WAR_RECEIVEDAM: (SkillCacheEvent,),
    MSG_WAR_ATTACKPF: (SkillCacheEvent,),
    MSG_WAR_PERFORM: (SkillCacheEvent,),
    MSG_WAR_ATTACK: (SkillCacheEvent,),
    MSG_WAR_ATTACK_END: (SkillCacheEvent,),
    MSG_WAR_DP: (MsgHaltCastingSkill, SkillCacheEvent) }

def GetAllStaticExtendFunc():
    dAllStaticExtendFunc = { }
    dAllStaticExtendFunc.update(g_StaticExtendFunc)
    dAllStaticExtendFunc.update(g_StaticExtendFuncAutoSub)
    for iMsg in g_StaticExtendFuncAutoSub:
        if iMsg in MSG_SUB_LIST:
            for iSub in MSG_SUB_LIST[iMsg]:
                iKey = GetMsgKey(iMsg, iSub)
                dAllStaticExtendFunc[iKey] = g_StaticExtendFuncAutoSub[iMsg]
            
    
    return dAllStaticExtendFunc

