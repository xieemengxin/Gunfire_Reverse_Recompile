# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/mobject.pyc
# RelativePath: clientlogic/cl_perform/mobject.pyc
# Source Generated with Decompyle++
# File: mobject.pyc (Python 3.6)

from cl_commondefines import BASEATTR_REFRESH, BASEATTR_CLIENT, DEBUG_STATUS_NOPFCD, WARRIOR_HERO, PERFORM_POS_EXT, PERFORM_POS_MAIN
from cl_commondefines import PF_TYPE_ATIVE, ITEMPERFORM_ENABLE_HOLD, ITEMPERFORM_ENABLE_UNHOLD, ITEMPERFORM_ENABLE_BOTH
from cl_commondefines import SKILLRET_FAIL, SKILLRET_SUCCESS, SKILLRET_CACHE
from cl_only import GAME_FRAME_TIME
from cl_object.baseattr import NewAttr
from cl_object.logging import SkillLog
import cl_formula
import cl_notify
import cl_msgcenter
import cl_msgcenter.eventcbobj
import cl_netattr

class CBasePerform(object):
    m_SID = 0
    m_Name = ''
    m_PFType = PF_TYPE_ATIVE
    m_Level = 1
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_BaseAttrData = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_CDPerform = 0
    m_IsMinor = 0
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD
    m_ClientNeed = False
    m_UnCrtByOwnerSign = 0
    m_UseCurWeapon = 0
    m_CycleTrigger = 0
    
    def __init__(self, oOwner, iLevel):
        self.m_ID = oOwner.m_Game.NewNoSceneObjID()
        self.m_Key = 'PF%d-%d' % (self.m_SID, self.m_ID)
        if self.m_CycleTrigger:
            self.m_EventCB = cl_msgcenter.eventcbobj.CCycleEventCB(self.m_CBFuncAction, self.m_Key)
        else:
            self.m_EventCB = cl_msgcenter.eventcbobj.CEventCB(self.m_CBFuncAction, self.m_Key)
        self.m_Owner = oOwner.m_ID
        self.m_Container = None
        self.m_Game = oOwner.m_Game
        self.m_Enable = 0
        self.m_Level = iLevel
        self.m_Stack = 1
        if self.m_Level < 1 or self.m_Level > self.m_MaxLevel:
            SkillLog.Error('%s init perform %d level %d' % (oOwner.m_ID, self.m_SID, self.m_Level))
            self.m_Level = self.m_MaxLevel
        self.m_MainPerform = 0
        self.m_AppendAttr = { }
        self.m_AppendTmpAttr = { }
        self.m_ArgData = { }
        self.m_Item = 0
        self.m_AttPerformIdx = 255
        self.m_Attr = { }
        for sAttr, val in self.m_BaseArgData.items():
            iValue = cl_formula.GetFormulaResultByLV(self, val, self.m_Level)
            self.m_ArgData[sAttr] = iValue
        
        self.ResetGradeFormulaAttr()
        self.OnInit()

    
    def Release(self):
        for oAttr in self.m_Attr.values():
            oAttr.ClearAll()
        
        self.m_Attr = { }
        self.m_Game = None
        self.m_Container = None

    
    def OnInit(self):
        pass

    
    def Name(self):
        return self.m_Name

    
    def Level(self):
        return self.m_Level

    
    def GetLifeCycleLevel(self):
        return self.m_Level

    
    def Stack(self):
        return self.m_Stack

    
    def Type(self):
        return 'Perform'

    
    def Key(self):
        return self.m_Key

    
    def SetLevel(self, oWarrior, iLevel):
        if iLevel < 1 or iLevel > self.m_MaxLevel:
            return None
        if self.m_Enable:
            self.SetArgValue('ChangeLeveling', 1)
            self.Disable(oWarrior)
            self.m_Level = iLevel
            self.OnSetLevel()
            self.Enable(oWarrior)
            self.DelArgValue('ChangeLeveling')
        else:
            self.m_Level = iLevel
            self.OnSetLevel()

    
    def OnSetLevel(self):
        pass

    
    def SetStack(self, iStack):
        iAdd = iStack - self.m_Stack
        self.AddStack(iAdd)

    
    def AddStack(self, iAdd):
        oOwner = self.GetOwner()
        iStack = self.m_Stack + iAdd
        if iStack < 0:
            iStack = 0
        elif self.m_MaxStack and iStack > self.m_MaxStack:
            iStack = self.m_MaxStack
        if self.m_Enable:
            self.Disable(oOwner)
            self.m_Stack = iStack
            self.Enable(oOwner)
        else:
            self.m_Stack = iStack

    
    def GS2CPerformPropChange(self, sAttr, iVal = 0):
        cl_netattr.GS2CItemPropChange(self, sAttr, iVal, 1)

    
    def RefreshAttr(self, sAttr, iValue):
        if not self.m_Owner:
            return None
        if not self.m_Game:
            SkillLog.Alert('PF%s game was released.' % self.m_SID)
            return None
        self.GS2CPerformPropChange(sAttr, iValue)
        if sAttr in ('ColdTime', 'MaxCover'):
            self.m_Container.RefreshColdTimeAttr(self.m_SID, sAttr)

    
    def ResetGradeFormulaAttr(self):
        iRefreshFlag = BASEATTR_REFRESH
        cl_formula.ResetNoSceneObjGradeFormulaAttr(self, self.m_BaseAttrData, self.GetLifeCycleLevel(), iRefreshFlag)

    
    def AttrCache(self):
        return { }

    
    def GetAttr(self, sAttr):
        if sAttr not in self.m_Attr:
            return None
        return self.m_Attr[sAttr]

    
    def SetAttr(self, sAttr, iValue, iRefresh):
        if sAttr not in self.m_Attr:
            oAttr = NewAttr(self, sAttr, iValue, iRefresh)
            self.m_Attr[sAttr] = oAttr
        else:
            oAttr = self.m_Attr[sAttr]
            oAttr.ChangeBase(self, iValue)

    
    def DirectSetAttr(self, sAttr, oAttr):
        self.m_Attr[sAttr] = oAttr
        oAttr.Refresh(self)

    
    def CalAttr(self, sAttr):
        oAttr = self.m_Attr[sAttr]
        if oAttr.m_Refresh:
            oAttr.Refresh(self)
        return oAttr.GetValue(self)

    
    def QueryAttrNet(self, sAttr):
        if sAttr not in self.m_Attr:
            return 0
        return self.CalAttr(sAttr)

    
    def QueryAttrForecast(self, sAttr):
        if sAttr not in self.m_Attr:
            return (0, 0, 0, 0)
        oAttr = self.m_Attr[sAttr]
        (iBase, iAdd, iMulPositive, iMulNegative) = oAttr.GetForecastValue(self)
        return (iBase, iAdd, iMulPositive, iMulNegative)

    
    def AttrChange(self, sAttr, sKey, iRatio, iAdd, iRefresh = 1):
        if iRefresh:
            self.m_Attr[sAttr].AddValue(self, iRatio, iAdd, sKey)
        else:
            self.m_Attr[sAttr].AddValue(None, iRatio, iAdd, sKey)

    
    def AttrClear(self, sAttr, sKey, iRefresh = 1):
        if iRefresh:
            self.m_Attr[sAttr].ClearValue(self, sKey)
        else:
            self.m_Attr[sAttr].ClearValue(None, sKey)

    
    def AttrForceSet(self, sAttr, iValue, sKey, iRefresh = 1):
        if iRefresh:
            self.m_Attr[sAttr].SetForceValue(self, iValue, sKey)
        else:
            self.m_Attr[sAttr].SetForceValue(None, iValue, sKey)

    
    def AttrForceClear(self, sAttr, sKey, iRefresh = 1):
        if iRefresh:
            self.m_Attr[sAttr].ClearForceValue(self, sKey)
        else:
            self.m_Attr[sAttr].ClearForceValue(None, sKey)

    
    def GetMyItem(self):
        oItem = None
        oWarrior = self.m_Game.GetObject(self.m_Owner)
        if not oWarrior:
            return oItem
        if self.m_Item:
            oItem = oWarrior.m_WieldCon.GetItemByID(self.m_Item)
            if not oItem and oWarrior.m_WandCon:
                oItem = oWarrior.m_WandCon.GetWandByID(self.m_Item)
        if not oItem and self.m_UseCurWeapon:
            oItem = oWarrior.m_WieldCon.GetCurWeapon()
        return oItem

    
    def GetOwner(self):
        return self.m_Game.GetObject(self.m_Owner)

    
    def SetCDTime(self, oWarrior, iFrame):
        self.m_Container.RefreshColdTime(self.m_SID, iFrame)

    
    def GetCDTime(self, oWarrior):
        if 'ColdTime' not in self.m_Attr:
            return 0
        iCDTime = self.CalAttr('ColdTime')
        return iCDTime // GAME_FRAME_TIME

    
    def DelCDTime(self, oWarrior):
        self.m_Container.DelColdTime(self.m_SID)

    
    def InColdTime(self):
        if self.m_Container.InColdTime(self.m_SID):
            return 1
        return 0

    
    def GetMaxCover(self, oWarrior):
        if 'MaxCover' not in self.m_Attr:
            return 1
        iMaxCover = self.CalAttr('MaxCover')
        return iMaxCover

    
    def HasCover(self):
        return self.m_Container.HasCover(self.m_SID)

    
    def GetUseInterval(self, oWarrior):
        if 'UseInterval' not in self.m_Attr:
            return 0
        iUseInterval = self.CalAttr('UseInterval')
        return iUseInterval // GAME_FRAME_TIME

    
    def InUseInterval(self):
        return self.m_Container.InUseInterval(self.m_SID)

    
    def GetArgValue(self, sArgs, iDefault = 0):
        if sArgs not in self.m_ArgData:
            return iDefault
        return self.m_ArgData[sArgs]

    
    def SetArgValue(self, sArgs, val):
        self.m_ArgData[sArgs] = val

    
    def SetArgValueDefault(self, sArgs, val):
        if sArgs not in self.m_ArgData:
            self.m_ArgData[sArgs] = val
            return val
        return self.m_ArgData[sArgs]

    
    def AddArgValue(self, sArgs, iAdd):
        if sArgs not in self.m_ArgData:
            self.m_ArgData[sArgs] = iAdd
            return None
        self.m_ArgData[sArgs] += iAdd

    
    def DelArgValue(self, sArgs):
        if sArgs in self.m_ArgData:
            self.m_ArgData.pop(sArgs)

    
    def PopArgValue(self, sArgs, default = 0):
        return self.m_ArgData.pop(sArgs, default)

    
    def GetAppendAttr(self, sAttr):
        iRet = 0
        if sAttr in self.m_AppendAttr:
            iRet += self.m_AppendAttr[sAttr]
        if sAttr in self.m_AppendTmpAttr:
            iRet += self.m_AppendTmpAttr[sAttr]
        return iRet

    
    def DelAppendAttr(self, sAttr):
        if sAttr in self.m_AppendTmpAttr:
            self.m_AppendTmpAttr.pop(sAttr)
        if sAttr in self.m_AppendAttr:
            self.m_AppendAttr.pop(sAttr)

    
    def AddAppendAttr(self, sAttr, iVal, iTmp):
        if iTmp:
            dData = self.m_AppendTmpAttr
        else:
            dData = self.m_AppendAttr
        if sAttr not in dData:
            dData[sAttr] = iVal
        else:
            dData[sAttr] += iVal

    
    def SetAppendAttr(self, sAttr, iVal, iTmp):
        if iTmp:
            dData = self.m_AppendTmpAttr
        else:
            dData = self.m_AppendAttr
        dData[sAttr] = iVal

    
    def Disable(self, oWarrior, iNotify = 0, iReleaseFlag = 0):
        self.m_Enable = 0
        if iNotify:
            self.GS2CPerformPropChange('Enable', self.m_Enable)
        for iExtPerform in self.m_ExtPerform:
            oExtPF = self.m_Container.GetPerform(iExtPerform)
            if oExtPF:
                oExtPF.Disable(oWarrior, iNotify, iReleaseFlag)
        

    
    def Enable(self, oWarrior, iNotify = 0):
        self.m_Enable = 1
        if iNotify:
            self.GS2CPerformPropChange('Enable', self.m_Enable)
        self.ResetGradeFormulaAttr()
        for iExtPerform in self.m_ExtPerform:
            oExtPF = self.m_Container.GetPerform(iExtPerform)
            if oExtPF:
                oExtPF.Enable(oWarrior, iNotify)
        

    
    def Refresh(self):
        pass

    
    def GetPerformPos(self):
        if self.m_MainPerform:
            return PERFORM_POS_EXT
        return PERFORM_POS_MAIN



class CPerform(CBasePerform):
    m_ActionInfo = { }
    m_EndActionInfo = { }
    m_HaltActionInfo = { }
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_PassRule = { }
    m_SubMsg = -1
    m_CheckForbid = -1
    m_ForbidRule = 0
    m_Resend = 0
    m_IgnoreLayer = ()
    m_UseHeight = 0
    
    def __init__(self, oOwner, iLevel):
        super(CPerform, self).__init__(oOwner, iLevel)
        self.m_DisableUse = {
            'State': 0,
            'Replace': 0 }

    
    def DebugReplace(self, dCode):
        self.m_ActionInfo = {
            self.m_Level: dCode['Action'] }
        self.m_HaltActionInfo = {
            self.m_Level: dCode['Halt'] }
        self.m_EndActionInfo = {
            self.m_Level: dCode['End'] }

    
    def GetAttDistance(self):
        return self.CalAttr('AttDistance')

    
    def ModifyColdTime(self, oWarrior, iModifyTime):
        self.m_Container.ModifyColdTime(self.m_SID, iModifyTime)

    
    def IsDisableUse(self, iCheckReplace = 1):
        for sReason, iDisableUse in self.m_DisableUse.items():
            if (iDisableUse or sReason == 'Replace') and not iCheckReplace:
                continue
            return 1
        
        return 0

    
    def CanUse(self, oWarrior, dInfo):
        if not self.m_Enable:
            return SKILLRET_FAIL
        if not oWarrior.m_Scene:
            return SKILLRET_FAIL
        if oWarrior.IsDead() and 'IgnoreDie' not in dInfo:
            if 'Net' in dInfo:
                cl_notify.GS2CDebugMsg(self.m_Game, oWarrior.m_PlayerID, '【失败】死亡禁止施放技能%d' % self.m_SID)
            return SKILLRET_FAIL
        if oWarrior.Query('DebugStatus', 0) & DEBUG_STATUS_NOPFCD != DEBUG_STATUS_NOPFCD:
            if self.InUseInterval():
                if 'Net' in dInfo:
                    cl_notify.GS2CDebugMsg(self.m_Game, oWarrior.m_PlayerID, '%s处于使用间隔中...' % self.Name())
                return SKILLRET_FAIL
            if not self.m_Container.HasCover(self.m_SID) and not self.AllowPreUse(oWarrior):
                if 'Net' in dInfo:
                    iColdTime = self.m_Container.GetColdTime(self.m_SID)
                    if not oWarrior.WaitToPerform(self.m_SID, dInfo, iColdTime):
                        return SKILLRET_FAIL
                    return SKILLRET_CACHE
                return SKILLRET_FAIL
        iWeapon = dInfo['Weapon'] if 'Weapon' in dInfo else 0
        if oWarrior.IsForbid(self.m_CheckForbid, self.m_PassRule, iWeapon):
            if 'Net' in dInfo:
                cl_notify.GS2CDebugMsg(self.m_Game, oWarrior.m_PlayerID, '%s被禁止' % self.Name())
            return SKILLRET_FAIL
        return SKILLRET_SUCCESS

    
    def AllowPreUse(self, oWarrior):
        if oWarrior.m_FightType & WARRIOR_HERO == WARRIOR_HERO and self.m_Container.GetColdTime(self.m_SID) <= 2:
            self.m_Container.DelNowCoverColdTime(self.m_SID)
            return 1
        return 0

    
    def UsePerform(self, oWarrior, oSkill):
        if oWarrior.Query('DebugStatus', 0) & DEBUG_STATUS_NOPFCD != DEBUG_STATUS_NOPFCD and 'NoAddColdTime' not in self.m_BaseArgData:
            self.m_Container.AddColdTime(self.m_SID, self.GetCDTime(oWarrior), iActNum = oSkill.m_Base['ActNum'])
        self.m_Container.AddUseInterval(self.m_SID, self.GetUseInterval(oWarrior))
        self.SendUseMsg(oWarrior, oSkill)
        self.DoAction(oSkill)

    
    def DoAction(self, oSkill):
        func = self.m_ActionInfo[self.m_Level]
        func(oSkill)

    
    def SendUseMsg(self, oWarrior, oSkill):
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_PERFORM_START, oWarrior, {
            'Skill': oSkill,
            'UnCrtByOwnerSign': self.m_UnCrtByOwnerSign }, iSub = self.m_SubMsg)

    
    def Disable(self, oWarrior, iNotify = 1, iReleaseFlag = 0):
        super().Disable(oWarrior, iNotify = 1, iReleaseFlag = iReleaseFlag)

    
    def Enable(self, oWarrior, iNotify = 1):
        super().Enable(oWarrior, iNotify = 1)

    
    def DoEndAction(cls, oSkill):
        if 'PFLV' not in oSkill.m_Base:
            SkillLog.Debug('skillpflv err')
            return None
        iPFLV = oSkill.m_Base['PFLV']
        if iPFLV not in cls.m_EndActionInfo:
            return None
        func = cls.m_EndActionInfo[iPFLV]
        func(oSkill)

    DoEndAction = classmethod(DoEndAction)
    
    def DoHaltAction(cls, oSkill):
        iPFLV = oSkill.m_Base['PFLV']
        if iPFLV not in cls.m_HaltActionInfo:
            return None
        func = cls.m_HaltActionInfo[iPFLV]
        func(oSkill)

    DoHaltAction = classmethod(DoHaltAction)
    
    def PerformEnd(cls, oSkill):
        oWarrior = oSkill.GetAttack()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_PERFORM_END, oWarrior, {
            'Skill': oSkill }, iSub = cls.m_SubMsg, oGame = oSkill.m_Game)
        cls.DoEndAction(oSkill)

    PerformEnd = classmethod(PerformEnd)
    
    def PerformHalt(cls, oSkill):
        oWarrior = oSkill.GetAttack()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_PERFORM_HALT, oWarrior, {
            'Skill': oSkill }, iSub = cls.m_SubMsg, oGame = oSkill.m_Game)
        cls.DoHaltAction(oSkill)

    PerformHalt = classmethod(PerformHalt)
    
    def CheckMinUseEnergy(self, oWarrior):
        iMinUseEnergy = self.QueryAttrNet('MinUseEnergy')
        if iMinUseEnergy and iMinUseEnergy > oWarrior.m_Energy:
            return SKILLRET_FAIL
        return SKILLRET_SUCCESS

    
    def CostEnergy(self, oWarrior, oSkill):
        if 'EnergyCost' in self.m_ArgData and not oSkill.m_Collect.get('NoCostEnergy', 0):
            oWarrior.EnergyModify(-self.m_ArgData['EnergyCost'], oSkill = oSkill)


