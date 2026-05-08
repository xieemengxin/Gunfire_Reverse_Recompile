# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_object/lifecycle.pyc
# RelativePath: clientlogic/cl_object/lifecycle.pyc
# Source Generated with Decompyle++
# File: lifecycle.pyc (Python 3.6)

from cl_only import WeakProxy, SendAlert, Functor, PythonError
from cl_commondefines import DISABLE_TYPE_STATE, DISABLE_TYPE_MSG, DISABLE_TYPE_RELIC, DISABLE_TYPE_SCENEEVENT, DISABLE_TYPE_KEY, DISABLE_TYPE_CALL, DISABLE_TYPE_SNAPMSG, DISABLE_TYPE_BULLET, DISABLE_TYPE_WARMSG, DISABLE_TYPE_TARGETSET
from cl_object.logging import OptimizationLog
import cl_msgcenter
import cllib.lib_flag as lib_flag

class CLifeCycle(object):
    m_AlertCnt = 20
    
    def __init__(self):
        self.m_Enable = 0
        self.m_Owner = None
        self.m_Key = ''
        self.m_StableKey = ''
        self.m_Func = { }
        self.m_DisableFuncList = []
        self.m_UniqueDisableFunc = { }
        self.m_Apply = { }
        self.m_ItemApply = { }
        self.m_PerformApply = { }
        self.m_OwnerApplied = { }
        self.m_OwnerItemForceApplied = { }
        self.m_Calling = 0
        self.m_DelayDisbale = False
        self.m_DelayRelease = False
        self.m_DisableType = { }
        self.m_DisableFlag = False
        self.m_Enabling = 0
        self.m_Disabling = 0

    
    def Init(self, obj, enableFunc, disableFunc):
        self.m_Owner = WeakProxy(obj)
        self.m_Key = self.m_Owner.Key()
        self.m_StableKey = '%s-%s' % (self.m_Owner.__class__.__name__, self.m_Owner.m_SID)
        self.m_Func['Enable'] = enableFunc
        self.m_Func['Disable'] = disableFunc

    
    def __str__(self):
        return 'lifecycle:%s' % self.m_Key

    
    def __repr__(self):
        return 'lifecycle:%s' % self.m_Key

    
    def RegisterFunc(self, sKey, cbFunc):
        self.m_Func[sKey] = cbFunc

    
    def DumpFunc(self, sKey):
        if sKey not in self.m_Func:
            return None
        self.m_Func.pop(sKey)

    
    def CallFunc(self, sFunc, oWarrior):
        if sFunc not in self.m_Func:
            return None
        func = self.m_Func[sFunc]
        if not func:
            return None
        if self.m_Calling >= self.m_AlertCnt:
            SendAlert('err', '%s %s CallFunc loop alert' % (self.m_Key, sFunc))
            return None
        self.m_Calling += 1
        func(oWarrior, self)
        self.m_Calling -= 1
        if self.m_Calling:
            return None
        if self.m_DelayDisbale:
            self.m_DelayDisbale = False
            if self.m_DisableFlag:
                self.PFAndStateDisable(oWarrior)
            else:
                self.Disable(oWarrior)
        if self.m_DelayRelease and not (self.m_Enabling) and not (self.m_Disabling):
            self.m_DelayRelease = False
            self.Release()

    
    def Release(self):
        if self.m_Calling:
            self.m_DelayRelease = True
            return None
        self.m_Owner = None
        self.m_Func = { }
        self.m_DisableFuncList = []
        self.m_UniqueDisableFunc = { }
        self.m_Apply = { }
        self.m_ItemApply = { }
        self.m_PerformApply = { }
        self.m_OwnerApplied = { }
        self.m_DisableType = { }

    
    def Enable(self, oWarrior):
        if self.m_Enable or not oWarrior:
            return None
        self.m_Enable = 1
        self.m_Enabling = 1
        self.CallFunc('Enable', oWarrior)
        self.m_Enabling = 0
        if self.m_DelayRelease:
            self.m_DelayRelease = False
            self.Release()

    
    def Disable(self, oWarrior, iRefresh = 1):
        if not (self.m_Enable) or not oWarrior:
            return None
        if self.m_Calling:
            self.m_DelayDisbale = True
            return None
        self.m_Enable = 0
        
        try:
            self.m_Disabling = 1
            self.CallFunc('Disable', oWarrior)
            self.m_Disabling = 0
            self._ClearApply(oWarrior, iRefresh)
        except:
            self.m_Disabling = 0
            PythonError()


    
    def PFAndStateDisable(self, oWarrior, iRefresh = 1):
        if not (self.m_Enable) or not oWarrior:
            return None
        if self.m_Calling:
            self.m_DelayDisbale = True
            self.m_DisableFlag = True
            return None
        self.m_Enable = 0
        
        try:
            self._ClearApply(oWarrior, iRefresh)
        except:
            PythonError()


    
    def _ClearApply(self, oWarrior, iRefresh = 1):
        if lib_flag.g_IsInternalRun and lib_flag.g_IsTradition and self.m_DisableFuncList:
            dCnt = { }
            dAlert = { }
            for func in self.m_DisableFuncList:
                if isinstance(func, Functor):
                    sKey = str(func)
                else:
                    sKey = func.__name__
                if sKey not in dCnt:
                    dCnt[sKey] = 0
                dCnt[sKey] += 1
            
            for sKey, iCnt in dCnt.items():
                if iCnt > 10:
                    dAlert[sKey] = iCnt
            
            if dAlert:
                OptimizationLog.Debug('lifecycle %s %s' % (self.m_Key, dAlert))
        if DISABLE_TYPE_MSG in self.m_DisableType:
            for iMsg, sLifeKey, iSub in self.m_DisableType[DISABLE_TYPE_MSG]:
                cl_msgcenter.DoneEvent(oWarrior, iMsg, sLifeKey, iSub)
            
        if DISABLE_TYPE_WARMSG in self.m_DisableType:
            for iWarMgr, iMsg, sLifeKey, iSub in self.m_DisableType[DISABLE_TYPE_WARMSG]:
                cl_msgcenter.DoneAttention(oWarrior, iWarMgr, iMsg, sLifeKey, iSub)
            
        if self.m_DisableFuncList:
            lstFunc = self.m_DisableFuncList
            self.m_DisableFuncList = []
            for func in lstFunc:
                func(oWarrior, self)
            
        if self.m_UniqueDisableFunc:
            lstFunc = self.m_UniqueDisableFunc.values()
            self.m_UniqueDisableFunc = { }
            for func in lstFunc:
                func(oWarrior, self)
            
        oGame = oWarrior.m_Game
        if DISABLE_TYPE_STATE in self.m_DisableType:
            for iObj, dState in self.m_DisableType[DISABLE_TYPE_STATE].items():
                obj = oGame.GetObject(iObj)
                if not obj or not (obj.m_State):
                    continue
                for iStateID in dState:
                    obj.m_State.RemoveItem(iStateID)
                
            
        if DISABLE_TYPE_RELIC in self.m_DisableType and not (oWarrior.m_Agent):
            oRelicCon = oWarrior.m_RelicCon
            for iPerform in self.m_DisableType[DISABLE_TYPE_RELIC]:
                oPerform = oRelicCon.GetPerform(iPerform)
                if oPerform:
                    oPerform.ClearDisableSource(self.m_Key)
                    oPerform.Enable(oWarrior)
            
        if DISABLE_TYPE_SCENEEVENT in self.m_DisableType:
            for iScene, dEvent in self.m_DisableType[DISABLE_TYPE_SCENEEVENT].items():
                oScene = oGame.m_SceneMgr.GetScene(iScene)
                if not oScene:
                    continue
                for iSceneEvtID in dEvent:
                    oScene.RemoveSceneEvent(iSceneEvtID)
                
            
        if DISABLE_TYPE_KEY in self.m_DisableType:
            for sLifeKey in self.m_DisableType[DISABLE_TYPE_KEY]:
                oWarrior.Delete(sLifeKey)
            
        if DISABLE_TYPE_CALL in self.m_DisableType:
            for sLifeKey in self.m_DisableType[DISABLE_TYPE_CALL]:
                oWarrior.Remove_Call_Out(sLifeKey)
            
        sKey = self.m_Key
        if DISABLE_TYPE_SNAPMSG in self.m_DisableType:
            for iMsgKey, iWeapon in self.m_DisableType[DISABLE_TYPE_SNAPMSG]:
                if iWeapon:
                    oWeapon = oWarrior.m_WieldCon.GetItemByID(iWeapon)
                    if not oWeapon:
                        continue
                    oPerformCom = oWeapon.GetComponent('Perform')
                    oPerformCom.RemoveTransEvent(iMsgKey, sKey)
                else:
                    dPriority = oWarrior.m_TransEvt[iMsgKey]
                    for dKeys in dPriority.values():
                        if sKey in dKeys:
                            dKeys.pop(sKey)
                            break
                    
            
        if DISABLE_TYPE_BULLET in self.m_DisableType:
            oCon = oWarrior.m_BulletChangeCon
            for iPerform, iOwnPfid in self.m_DisableType[DISABLE_TYPE_BULLET]:
                oPerform = oCon.GetPerform(iOwnPfid, iPerform)
                if not oPerform:
                    continue
                oPerform.Disable(oWarrior)
            
        if DISABLE_TYPE_TARGETSET in self.m_DisableType:
            for setTar, func in self.m_DisableType[DISABLE_TYPE_TARGETSET].values():
                func(oWarrior, self, setTar)
            
        self.m_DisableType = { }
        for sAttr in self.m_Apply:
            oWarrior.AttrClear(sAttr, sKey, iRefresh)
            oWarrior.AttrForceClear(sAttr, sKey, iRefresh)
        
        for iWeapon, sAttr in self.m_ItemApply:
            oWeapon = oWarrior.m_WieldCon.GetItemByID(iWeapon)
            if not oWeapon:
                continue
            oWeapon.AttrClear(sAttr, sKey, iRefresh)
            oWeapon.ItemAttrForceClear(sAttr, sKey, iRefresh)
        
        for iItem, iPerform, sAttr in self.m_PerformApply:
            oPerform = oWarrior.GetPerform(iPerform, iItem)
            if not oPerform:
                continue
            oPerform.AttrClear(sAttr, sKey, iRefresh)
            oPerform.AttrForceClear(sAttr, sKey, iRefresh)
        
        if self.m_Owner:
            for sAttr, sSourceKey in self.m_OwnerApplied:
                self.m_Owner.AttrClear(sAttr, sSourceKey, iRefresh)
            
            for sAttr, sSourceKey in self.m_OwnerItemForceApplied:
                self.m_Owner.ItemAttrForceClear(sAttr, sSourceKey, iRefresh)
            
        if self.m_DisableFuncList:
            lstFunc = self.m_DisableFuncList
            self.m_DisableFuncList = []
            if lib_flag.g_IsAuthorityRun:
                OptimizationLog.TraceAlert('%s remain disablefunc %s' % (self.m_Key, lstFunc))
            for func in lstFunc:
                func(oWarrior, self)
            
        if self.m_UniqueDisableFunc:
            lstFunc = self.m_UniqueDisableFunc.values()
            self.m_UniqueDisableFunc = { }
            if lib_flag.g_IsAuthorityRun and 'PF6920' not in self.m_Key:
                OptimizationLog.TraceAlert('%s remain uniquedisablefunc %s' % (self.m_Key, lstFunc))
            for func in lstFunc:
                func(oWarrior, self)
            
        self.m_Apply = { }
        self.m_ItemApply = { }
        self.m_PerformApply = { }
        self.m_OwnerApplied = { }
        self.m_OwnerItemForceApplied = { }

    
    def AddDisableType(self, iType, *args):
        if iType not in self.m_DisableType:
            self.m_DisableType[iType] = { }
        dData = self.m_DisableType[iType]
        if iType == DISABLE_TYPE_STATE:
            for iObj, iStateID in args[0].items():
                if iObj not in dData:
                    dData[iObj] = { }
                dData[iObj][iStateID] = 1
            
        elif iType in (DISABLE_TYPE_MSG, DISABLE_TYPE_SNAPMSG, DISABLE_TYPE_BULLET, DISABLE_TYPE_WARMSG):
            dData[args] = 1
        elif iType == DISABLE_TYPE_RELIC:
            for iRelic in args[0]:
                dData[iRelic] = 1
            
        elif iType == DISABLE_TYPE_SCENEEVENT:
            (iScene, iSceneEvtID) = args
            if iScene not in dData:
                dData[iScene] = { }
            dData[iScene][iSceneEvtID] = 1
        elif iType == DISABLE_TYPE_KEY:
            dData[args[0]] = 1
        elif iType == DISABLE_TYPE_CALL:
            for sKey in args[0]:
                dData[sKey] = 1
            
        elif iType == DISABLE_TYPE_TARGETSET:
            (sKey, setTar, func) = args
            if sKey in dData:
                setOldTar = dData[sKey][0]
                dData[sKey][0] = setOldTar | setTar
            else:
                dData[sKey] = [
                    setTar,
                    func]

    
    def AddDisableFunc(self, func):
        self.m_DisableFuncList.append(func)

    
    def AddUniqueDisableFunc(self, sKey, func, iCover):
        if sKey not in self.m_UniqueDisableFunc or iCover:
            self.m_UniqueDisableFunc[sKey] = func

    
    def AlreadyDoDisableFunc(self, oWarrior, sFunc):
        lstNew = []
        for func in self.m_DisableFuncList:
            if func.__name__ == sFunc:
                func(oWarrior, self)
                continue
            lstNew.append(func)
        
        self.m_DisableFuncList = lstNew

    
    def GetObject(self):
        return self.m_Owner

    
    def GetStableKey(self):
        return self.m_StableKey

    
    def Key(self):
        return self.m_Key

    
    def AttrCache(self):
        return self.m_Owner.AttrCache()

    
    def GetOwnerSourceWeapon(self):
        if not self.m_Owner:
            return None
        return self.m_Owner.GetMyItem()


