# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_item/baseitem.pyc
# RelativePath: clientlogic/cl_item/baseitem.pyc
# Source Generated with Decompyle++
# File: baseitem.pyc (Python 3.6)

from cl_commondefines import BASEATTR_REFRESH
from cl_cscommondef import ITEM_GRADE_MIN
from cl_only import RaiseError, DeepCopy, WeakProxy
from cl_object.baseattr import NewAttr
from cl_object.lifecycle import CLifeCycle
from cl_object.logging import WarobjLog
from . import defines as itemdef
from . import component
import cl_netattr
import cl_msgcenter.eventcbobj
import cl_formula
import cl_item
import cl_msgcenter
SPECIALATTR_CUR = 0
SPECIALATTR_MIN = 1
SPECIALATTR_MAX = 2
SPECIALATTR_BASE = 3

class CBaseItem(object):
    m_SID = 0
    m_Name = ''
    m_Shape = 0
    m_Type = 0
    m_ItemAttr = { }
    m_ComponentAttr = { }
    m_AddAction = None
    m_Action = (None, None)
    m_MaxAmount = 1
    m_MaxGroup = 0
    m_MaxGrade = 0
    m_CBFuncAction = { }
    
    def __init__(self, oGame, iTemp = 0, iPointID = 0, dTmp = None):
        if not iTemp:
            self.m_ID = oGame.NewNoSceneObjID() if not iPointID else iPointID
            self.m_Game = oGame
        else:
            self.m_ID = 0
            self.m_Game = None
        self.m_Key = 'I%d-%d' % (self.m_SID, self.m_ID)
        self.m_LifeCycle = CLifeCycle()
        self.m_EventCB = None
        self.m_Owner = 0
        self.m_Grade = -1
        self.m_BaseGrade = -1
        self.m_ExtGradeInfo = { }
        self.m_Container = None
        self.m_Flag = 0
        self.m_Amount = 0
        self.m_Component = { }
        self.m_Attention = { }
        self.m_Data = { }
        self.m_TmpData = dTmp if dTmp else { }
        self.m_Enable = 0
        self.m_InitData = None
        self.m_PrivateAttr = { }
        self.m_WarPickInfo = { }
        self.m_ShareInfo = { }
        self.m_Source = 0
        self.m_SpecialAttr = { }
        self.m_SpecialAttrChange = { }
        self.m_Mode = { }

    
    def Init(self, iGrade = 1):
        self.m_LifeCycle.Init(self, self.m_Action[0], self.m_Action[1])
        self.m_EventCB = cl_msgcenter.eventcbobj.CEventCB(self.m_CBFuncAction, self.m_Key)
        cl_formula.ResetNoSceneObjGradeFormulaAttr(self, self.m_ItemAttr, self.m_Grade, BASEATTR_REFRESH)
        self.SetBaseGrade(iGrade)
        self._InitComponent()
        self.InitSpecialAttrChange()

    
    def SetAttr(self, sAttr, iValue, iRefresh):
        self.m_PrivateAttr[sAttr] = NewAttr(self, sAttr, iValue, iRefresh)

    
    def DirectSetAttr(self, sAttr, oAttr):
        self.m_PrivateAttr[sAttr] = oAttr
        oAttr.Refresh(self)

    
    def SetGrade(self, iGrade):
        if iGrade == self.m_Grade:
            return None
        if self.m_MaxGrade and iGrade > self.m_MaxGrade:
            if 'OverMaxGrade' not in self.m_TmpData:
                iGame = self.m_Game.m_ID if self.m_Game else 0
                WarobjLog.Alert('%s setgrade %s %s %s %s %s' % (iGame, iGrade, self.m_SID, self.m_MaxGrade, self.m_BaseGrade, self.m_ExtGradeInfo))
            self.m_TmpData['OverMaxGrade'] = 1
            iGrade = self.m_MaxGrade
        if iGrade < ITEM_GRADE_MIN:
            iGrade = ITEM_GRADE_MIN
        self.m_Grade = iGrade
        for sAttr, iValue in self.m_ItemAttr.items():
            iValue = cl_formula.GetFormulaResultByLV(self, iValue, self.m_Grade)
            self.m_PrivateAttr[sAttr].ChangeBase(self, iValue)
        
        if self.m_Owner:
            self.GS2CItemPropChange('Grade')
        self.OnSetGrade()

    
    def SetBaseGrade(self, iBaseGrade, iSendMsg = 0):
        if iBaseGrade == self.m_BaseGrade:
            return None
        if iBaseGrade < ITEM_GRADE_MIN:
            iGame = self.m_Game.m_ID if self.m_Game else 0
            RaiseError(f'''{iGame} setbasegrade {self.m_SID} {iBaseGrade}''')
            iBaseGrade = ITEM_GRADE_MIN
        iOldBaseGrade = self.m_BaseGrade
        if iSendMsg:
            oOwner = self.m_Game.GetObject(self.m_Owner)
            dMsgInfo = {
                'ChangeGrade': iBaseGrade - iOldBaseGrade,
                'ItemType': self.m_Type,
                'ItemID': self.m_ID }
            if oOwner:
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CHANGE_ITEMBASEGRADE_BEFORE, oOwner, dMsgInfo)
                if 'GradeTransfer' in dMsgInfo and dMsgInfo['GradeTransfer']:
                    self.m_BaseGrade = iOldBaseGrade
                else:
                    self.m_BaseGrade = iBaseGrade
            else:
                self.m_BaseGrade = iBaseGrade
            iExtGrade = self.GetExtGrade()
            self.SetGrade(self.m_BaseGrade + iExtGrade)
            iHoldPos = self.GetComponent('Hold').HoldPos()
            if oOwner:
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CHANGE_WEAPONBASEGRADE, oOwner, {
                    'ItemID': self.m_ID,
                    'HoldType': iHoldPos,
                    'UpGrade': iBaseGrade > iOldBaseGrade })
            else:
                self.m_BaseGrade = iBaseGrade
                iExtGrade = self.GetExtGrade()
                self.SetGrade(self.m_BaseGrade + iExtGrade)
        return self.m_Game.m_ID

    
    def InitSpecialAttrChange(self):
        if not self.m_SpecialAttr:
            return None
        for sAttr in self.m_SpecialAttr:
            self.m_SpecialAttrChange[sAttr] = {
                'Factor': { },
                'Add': 0 }
        

    
    def CanUpgrade(self):
        return 0

    
    def Upgrade(self):
        self.SetBaseGrade(self.m_BaseGrade + 1, iSendMsg = 1)

    
    def Key(self):
        return self.m_Key

    
    def TraceName(self):
        sCom = ''
        for sName, oCom in self.m_Component.items():
            sText = oCom.TraceName()
            if sText:
                sCom += '%s: (%s), ' % (sName, sText)
        
        return '%s<TN:%s><COM:%s>' % (self.Name(), self.Query('TraceNo'), sCom)

    
    def Release(self):
        for oAttr in self.m_PrivateAttr.values():
            oAttr.ClearAll()
        
        self.m_PrivateAttr = { }
        for oComponent in self.m_Component.values():
            oComponent.Release()
        
        self.m_Component = { }
        self.m_Container = None
        self.m_LifeCycle.Release()
        self.m_LifeCycle = None
        self.m_Game = None

    
    def Create(self):
        self.m_Amount = 1
        if not self.m_ID:
            self.m_InitData = self.Save()

    
    def InitTemp(self):
        if self.m_InitData:
            dTmpData = DeepCopy(self.m_InitData)
            self.Load(dTmpData)

    
    def Refresh(self):
        oPerformCom = self.GetComponent('Perform')
        if oPerformCom:
            oPerformCom.Refresh()

    
    def _InitComponent(self):
        for sCom, dParser in self.m_ComponentAttr.items():
            self.m_Component[sCom] = component.CreateItemComponent(self, sCom, dParser)
        

    
    def AddComponent(self, sName, dParser):
        if sName in self.m_Component:
            return None
        self.m_Component[sName] = component.CreateItemComponent(self, sName, dParser)
        return self.m_Component[sName]

    
    def RemoveComponent(self, sName):
        if sName not in self.m_Component:
            return None
        oComponent = self.m_Component.pop(sName)
        oComponent.Release()

    
    def GetComponent(self, sName):
        if sName not in self.m_Component:
            return None
        return self.m_Component[sName]

    
    def AttrChange(self, sAttr, iMul, iAdd, sKey, iRefresh = 1, iRemoveClear = 0):
        obj = self if iRefresh else None
        self.m_PrivateAttr[sAttr].AddValue(obj, iMul, iAdd, sKey)
        if iRemoveClear:
            self.m_LifeCycle.m_OwnerApplied[(sAttr, sKey)] = 1

    
    def AttrClear(self, sAttr, sKey, iRefresh = 1):
        obj = self if iRefresh else None
        self.m_PrivateAttr[sAttr].ClearValue(obj, sKey)

    
    def ItemAttrForceSet(self, sAttr, iValue, sKey, iRefresh = 1, iRemoveClear = 0, iPriority = 0):
        obj = self if iRefresh else None
        self.m_PrivateAttr[sAttr].SetForceValue(obj, iValue, sKey, iPriority)
        if iRemoveClear:
            self.m_LifeCycle.m_OwnerItemForceApplied[(sAttr, sKey)] = 1

    
    def ItemAttrForceClear(self, sAttr, sKey, iRefresh = 1):
        obj = self if iRefresh else None
        self.m_PrivateAttr[sAttr].ClearForceValue(obj, sKey)

    
    def GetItemAttr(self, sAttr):
        if sAttr not in self.m_PrivateAttr:
            return None
        return self.m_PrivateAttr[sAttr]

    
    def QueryAttr(self, sAttr):
        oAttr = self.m_PrivateAttr[sAttr]
        if oAttr.m_Refresh:
            oAttr.Refresh(self)
        return oAttr.GetValue(self)

    
    def QueryAttrNet(self, sAttr):
        if sAttr not in self.m_PrivateAttr:
            return 0
        oAttr = self.m_PrivateAttr[sAttr]
        if oAttr.m_Refresh:
            oAttr.Refresh(self)
        return oAttr.GetValue(self)

    
    def QueryAttrForecast(self, sAttr):
        if sAttr not in self.m_PrivateAttr:
            return (0, 0, 0, 0)
        oAttr = self.m_PrivateAttr[sAttr]
        (iBase, iAdd, iMulPositive, iMulNegative) = oAttr.GetForecastValue(self)
        return (iBase, iAdd, iMulPositive, iMulNegative)

    
    def QueryItemBaseAttr(self, sAttr):
        if sAttr not in self.m_ItemAttr:
            return 0
        return self.m_ItemAttr[sAttr]

    
    def RefreshAttr(self, sAttr, iValue):
        pass

    
    def MainType(self):
        return self.m_Type & itemdef.ITEM_MAIN_MASK

    
    def ClassType(self):
        return self.m_Type & itemdef.ITEM_CLASS_MASK

    
    def Type(self):
        return self.m_Type

    
    def Name(self):
        return self.m_Name

    
    def Shape(self):
        return self.m_Shape

    
    def SetOwner(self, iOwner):
        self.m_Owner = iOwner

    
    def GetOwner(self):
        if not self.m_ID:
            return None
        return self.m_Game.GetObject(self.m_Owner)

    
    def InitSource(self, iSource):
        if self.m_Source:
            return None
        if not self.m_Game.m_WarMgr.Query('RecycleSelf', 1):
            iSource = 0
        self.m_Source = iSource

    
    def GetMaxAmount(self):
        return self.m_MaxAmount

    
    def Amount(self):
        return self.m_Amount

    
    def AddAmount(self, iAdd, sReason):
        self.m_Amount += iAdd
        self.OnAmountChange()
        if self.m_Amount < 0:
            RaiseError('%d addamount %d %d %s' % (self.m_SID, iAdd, self.m_Amount, sReason))

    
    def SetAmount(self, iAmount, sReason):
        self.m_Amount = iAmount
        self.OnAmountChange()
        if self.m_Amount < 0:
            RaiseError('%d setamount %d %s' % (self.m_SID, self.m_Amount, sReason))

    
    def Flag(self):
        return self.m_Flag

    
    def SetFlag(self, k, v):
        if v:
            self.m_Flag |= k
        else:
            self.m_Flag &= ~k

    
    def Set(self, key, value):
        self.m_Data[key] = value

    
    def Query(self, key, default = 0):
        if key not in self.m_Data:
            return default
        return self.m_Data[key]

    
    def SetTmp(self, key, value):
        self.m_TmpData[key] = value

    
    def AddTmp(self, key, value):
        if key not in self.m_TmpData:
            self.m_TmpData[key] = value
        else:
            self.m_TmpData[key] += value

    
    def QueryTmp(self, key, default = 0):
        if key not in self.m_TmpData:
            return default
        return self.m_TmpData[key]

    
    def RemoveTmp(self, key):
        if key not in self.m_TmpData:
            return None
        self.m_TmpData.pop(key)

    
    def SetDefaultTmp(self, key, default = 0):
        if key not in self.m_TmpData:
            self.m_TmpData[key] = default
            return default
        return self.m_TmpData[key]

    
    def AddAttention(self, iMsg, func, sKey):
        if iMsg not in self.m_Attention:
            self.m_Attention[iMsg] = { }
        self.m_Attention[iMsg][sKey] = func

    
    def DoneAttention(self, iMsg, sKey):
        if iMsg not in self.m_Attention:
            return None
        if sKey not in self.m_Attention[iMsg]:
            return None
        self.m_Attention[iMsg].pop(sKey)

    
    def SendMsg(self, iMsg, dMsgInfo = None):
        if iMsg not in self.m_Attention:
            return None
        dEvent = self.m_Attention[iMsg]
        oOwner = self.GetOwner()
        if dMsgInfo:
            for sKey in list(dEvent):
                if sKey not in dEvent:
                    continue
                func = dEvent[sKey]
                func(oOwner, dMsgInfo)
            
        else:
            for sKey in list(dEvent):
                if sKey not in dEvent:
                    continue
                func = dEvent[sKey]
                func(self, oOwner)
            

    
    def GetItemContainer(self):
        return self.m_Container

    
    def AddToContainer(self, oContainer):
        if not self.m_ID:
            return None
        self.m_Owner = oContainer.m_Owner
        self.m_Container = WeakProxy(oContainer)
        self.m_WarPickInfo[self.GetOwner().m_PlayerID] = 1
        self.m_LifeCycle.Enable(self.GetOwner())
        self.OnAddToContainer()
        self.SendMsg(itemdef.MSG_ITEM_ADD)

    
    def RemoveFromContainer(self, sReason = ''):
        if not self.m_ID:
            return None
        self.m_LifeCycle.Disable(self.GetOwner())
        self.SendMsg(itemdef.MSG_ITEM_REMOVE)
        self.OnRemoveFromContainer()
        self.m_Owner = 0
        self.m_Container = None
        self.m_TmpData = { }

    
    def CanCombine(self, obj):
        if self.GetMaxAmount() - self.Amount() <= 0:
            return 0
        if obj and self.m_SID != obj.m_SID:
            return 0
        return 1

    
    def Desc(self):
        return [
            self.Shape()]

    
    def PutToContainer(self, lstCon, sReason):
        iPut = 0
        for oItemCon in lstCon:
            if not oItemCon.ValidGive(self):
                continue
            if oItemCon.AddCombineItem(self, sReason):
                iPut = 1
                if not self.m_Amount:
                    break
        
        return iPut

    
    def GS2CItemPropChange(self, sAttr, iVal = 0, dPlayer = None):
        cl_netattr.GS2CItemPropChange(self, sAttr, iVal, 0, dPlayer)

    
    def SetWarPickInfo(self, dWarPick):
        self.m_WarPickInfo.update(dWarPick)

    
    def GetWarPickInfo(self):
        return self.m_WarPickInfo

    
    def Save(self):
        dWarPickInfo = { }
        dWarPickInfo.update(self.m_WarPickInfo)
        dComInfo = { }
        for sName, oCom in self.m_Component.items():
            dCom = oCom.Save()
            if dCom:
                dComInfo[sName] = oCom.Save()
        
        dData = {
            'ID': self.m_ID,
            'BaseGrade': self.m_BaseGrade,
            'SID': self.m_SID,
            'Data': self.m_Data,
            'Amount': self.m_Amount,
            'WarPickInfo': dWarPickInfo,
            'Com': dComInfo }
        return dData

    
    def Load(self, dData):
        self.m_Data = dData.get('Data', { })
        self.m_WarPickInfo = dData.get('WarPickInfo', { })
        iAmount = dData.get('Amount', 0)
        self.SetAmount(iAmount, 'Load')
        iBaseGrade = cl_item.GetBaseGrade(dData)
        self.SetBaseGrade(iBaseGrade)
        dCom = dData.get('Com', { })
        for sName, dComData in dCom.items():
            oCom = self.GetComponent(sName)
            if not oCom:
                continue
            oCom.Load(dComData)
        

    
    def CustomAttrValue(self, sAttr):
        iValue = None
        if sAttr == 'CurBullet':
            oBulletCom = self.GetComponent('Bullet')
            if not oBulletCom:
                return 0
            return oBulletCom.Bullet()
        if sAttr == 'FillPerform':
            oBulletCom = self.GetComponent('Bullet')
            if not oBulletCom:
                return 0
            return oBulletCom.GetFillPerform()
        if sAttr == 'FillPerformID':
            oBulletCom = self.GetComponent('Bullet')
            if not oBulletCom:
                return 0
            return oBulletCom.GetFillPerformID()
        if sAttr == 'AttPerformIdx':
            oPerformCom = self.GetComponent('Perform')
            if not oPerformCom:
                return 0
            return oPerformCom.GetAttPerformIdx()
        if sAttr == 'Inscription':
            oInscriptionCom = self.GetComponent('Inscription')
            if not oInscriptionCom:
                return [
                    0,
                    0,
                    0,
                    0,
                    0,
                    0]
            return oInscriptionCom.GetAllInscription()
        if sAttr == 'BulletState':
            oBulletCom = self.GetComponent('Bullet')
            if not oBulletCom:
                return 0
            return oBulletCom.BulletState()
        if sAttr == 'AddInscriptionTimes':
            oInscriptionCom = self.GetComponent('Inscription')
            if not oInscriptionCom:
                return 0
            return oInscriptionCom.GetExtraInscriptionTimes()
        if sAttr == 'Enhance':
            oEnhanceCom = self.GetComponent('Enhance')
            if not oEnhanceCom:
                return []
            return oEnhanceCom.GetAllEnhance()
        if sAttr == 'SealedInscription':
            oInscriptionCom = self.GetComponent('Inscription')
            if not oInscriptionCom:
                return [
                    0,
                    0,
                    0]
            return oInscriptionCom.GetSealedInscription()
        if sAttr == 'ExtGradeGroup':
            return self.GetExtGradeGroup()
        if sAttr == 'DisableInscription':
            oInscriptionCom = self.GetComponent('Inscription')
            if not oInscriptionCom:
                return []
            return oInscriptionCom.GetDisableInscription()
        if sAttr == 'ShareInscription':
            oInscriptionCom = self.GetComponent('Inscription')
            if not oInscriptionCom:
                return []
            return oInscriptionCom.GetShareInscription()
        if sAttr == 'CliModeIdx':
            oOwner = self.GetOwner()
            if oOwner:
                dWeaponModeIdx = oOwner.QuerySavedData('WeaponModeIdx', { })
                iSID = self.m_SID
                if iSID in dWeaponModeIdx:
                    return dWeaponModeIdx[iSID][1]
        return iValue

    
    def AttrCache(self):
        dData = {
            'AID': self.m_Owner,
            'ItemID': self.m_ID,
            'ItemSID': self.m_SID,
            'ItemType': self.m_Type,
            'ItemGrade': self.m_Grade,
            'ItemKey': self.m_Key,
            'ItemAmount': self.m_Amount }
        for sAttr in self.m_PrivateAttr:
            iValue = self.QueryAttr(sAttr)
            dData[sAttr] = iValue
        
        for oCom in self.m_Component.values():
            dData.update(oCom.AttrCache())
        
        return dData

    
    def EventCache(self):
        oPerformCom = self.GetComponent('Perform')
        if oPerformCom:
            return oPerformCom.EventCache()
        return { }

    
    def GetSpecialAttr(self, sAttr, default = 0):
        if sAttr in self.m_SpecialAttr:
            return self.m_SpecialAttr[sAttr][SPECIALATTR_CUR]
        return default

    
    def GetSpecialAttrMax(self, sAttr, default = 0):
        if sAttr in self.m_SpecialAttr:
            return self.m_SpecialAttr[sAttr][SPECIALATTR_MAX]
        return default

    
    def CalSpecialAttr(self, sAttr, iRefresh):
        if sAttr in self.m_SpecialAttr:
            (iOldValue, iMinValue, iMaxValue, iBaseValue) = self.m_SpecialAttr[sAttr]
            iAdd = self.m_SpecialAttrChange[sAttr]['Add']
            iCurValue = iBaseValue + iAdd
            if iCurValue < iMinValue:
                iCurValue = iMinValue
            elif iMaxValue and iCurValue > iMaxValue:
                iCurValue = iMaxValue
            if iOldValue != iCurValue:
                self.m_SpecialAttr[sAttr][SPECIALATTR_CUR] = iCurValue
                self.GS2CItemPropChange(sAttr, iCurValue)
                dMsgInfo = {
                    'ItemID': self.m_ID,
                    'Add': iAdd }
                if sAttr in itemdef.SPECIAL_ATTR_MSG:
                    self.SendMsg(itemdef.SPECIAL_ATTR_MSG[sAttr], dMsgInfo)
                elif iRefresh:
                    self.GS2CItemPropChange(sAttr, iCurValue)

    
    def ChangeSpecialAttr(self, sAttr, iAdd, sKey, iRefresh = 0):
        if not iAdd:
            return None
        if sAttr in self.m_SpecialAttr:
            dFactor = self.m_SpecialAttrChange[sAttr]['Factor']
            if sKey in dFactor:
                iActAdd = iAdd - dFactor[sKey]
            else:
                iActAdd = iAdd
            dFactor[sKey] = iAdd
            self.m_SpecialAttrChange[sAttr]['Add'] += iActAdd
            self.CalSpecialAttr(sAttr, iRefresh)

    
    def ChangeSpecialAttrMax(self, sAttr, iAdd):
        if not iAdd:
            return None
        if sAttr in self.m_SpecialAttr:
            self.m_SpecialAttr[sAttr][SPECIALATTR_MAX] += iAdd
            self.CalSpecialAttr(sAttr, iRefresh = 0)

    
    def AddSpecialAttrBase(self, sAttr, iAdd, iRefresh = 0):
        if not iAdd:
            return None
        if sAttr in self.m_SpecialAttr:
            (_, iMinValue, iMaxValue, iOldBaseValue) = self.m_SpecialAttr[sAttr]
            iCurBaseValue = iOldBaseValue + iAdd
            if iCurBaseValue < iMinValue:
                iCurBaseValue = iMinValue
            elif iMaxValue and iCurBaseValue > iMaxValue:
                iCurBaseValue = iMaxValue
            if iCurBaseValue != iOldBaseValue:
                self.m_SpecialAttr[sAttr][SPECIALATTR_BASE] = iCurBaseValue
                self.CalSpecialAttr(sAttr, iRefresh)
            elif iRefresh:
                self.CalSpecialAttr(sAttr, iRefresh)

    
    def QueryAttrSpecial(self, sAttr):
        if sAttr in self.m_SpecialAttr:
            return self.m_SpecialAttr[sAttr][SPECIALATTR_CUR]
        return 0

    
    def SpecialAttrClear(self, sAttr, sKey):
        if sAttr not in self.m_SpecialAttrChange:
            oOwner = self.GetOwner()
            pid = oOwner.m_PlayerID if oOwner else 0
            WarobjLog.Alert('%s %s %s clear no specialattr %s %s' % (self.m_Game.m_ID, pid, self.m_SID, sAttr, sKey))
            return None
        if sKey not in self.m_SpecialAttrChange[sAttr]['Factor']:
            return None
        iSub = self.m_SpecialAttrChange[sAttr]['Factor'].pop(sKey)
        self.m_SpecialAttrChange[sAttr]['Add'] -= iSub
        self.CalSpecialAttr(sAttr, iRefresh = 0)

    
    def ChangeMode(self, iMode, iStatus):
        self.m_Mode[iMode] = iStatus
        dMsgInfo = {
            'ItemID': self.m_ID,
            'Mode': iMode,
            'Status': iStatus }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ITEM_CHANGE_MODE, self.GetOwner(), dMsgInfo)

    
    def GetModeStatus(self, iMode):
        if iMode not in self.m_Mode:
            return 0
        return self.m_Mode[iMode]

    
    def AddExtGrade(self, sKey, iGroup, iExtGrade):
        self.m_ExtGradeInfo[sKey] = (iGroup, iExtGrade)
        self.RefreshGrade()

    
    def ClearExtGrade(self, sKey):
        if sKey not in self.m_ExtGradeInfo:
            return None
        self.m_ExtGradeInfo.pop(sKey)
        self.RefreshGrade()

    
    def ClearAllExtGrade(self):
        self.m_ExtGradeInfo = { }
        self.RefreshGrade()

    
    def RefreshGrade(self):
        iExtGrade = self.GetExtGrade()
        self.SetGrade(self.m_BaseGrade + iExtGrade)
        if self.m_Owner:
            self.GS2CItemPropChange('ExtGradeGroup')

    
    def GetExtGrade(self):
        iExtGrade = 0
        for _, iGrade in self.m_ExtGradeInfo.values():
            iExtGrade += iGrade
        
        return iExtGrade

    
    def GetExtGradeGroup(self):
        if not self.m_ExtGradeInfo:
            return []
        dGroup = { }
        for iGroup, iGrade in self.m_ExtGradeInfo.values():
            dGroup[iGroup] = dGroup.get(iGroup, 0) + iGrade
        
        lstExtGrade = []
        for iGroup, iGrade in dGroup.items():
            if not iGrade:
                continue
            lstExtGrade.append((iGroup, iGrade))
        
        lstExtGrade.sort()
        return lstExtGrade

    
    def CheckHasExtGrade(self, sKey):
        if sKey in self.m_ExtGradeInfo:
            return True
        return False

    
    def OnSetGrade(self):
        pass

    
    def OnAddToContainer(self):
        pass

    
    def OnRemoveFromContainer(self):
        pass

    
    def OnBeReplaced(self, oOther):
        pass

    
    def GetTargetContainer(self, oHero):
        pass

    
    def ValidDrop(self):
        return 1

    
    def ValidAddToContainer(self, oContainer):
        if self.m_MaxGroup and self.m_MaxGroup <= len(oContainer.GetAllItemBySID(self.m_SID)):
            return 0
        return 1

    
    def ValidBeReplaced(self, oOther):
        return 1

    
    def OnAmountChange(self):
        pass


