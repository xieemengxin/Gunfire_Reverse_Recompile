# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_container/inkcon.pyc
# RelativePath: clientlogic/cl_container/inkcon.pyc
# Source Generated with Decompyle++
# File: inkcon.pyc (Python 3.6)

from cl_only import WeakProxy, Time2Frame, Functor, PY_FLAG_DEAD
from cl_cscommondef import PF_SUBMSG_CAREERPF, PICK_INKBEAD, WARRIOR_HERO, WARRIOR_MONSTER, WARRIOR_BOSS, INKVALUE_ADD, INKVALUE_SUB
from cl_cscommondef import g_HeroAreaEventType, g_AreaType, HERO_SPHERE_AREAEVENT, HERO_INNERSPHERE_AREAEVENT, HERO_OUTERSPHERE_AREAEVENT, SPHERE_INKAREA, DOUBLESPHERE_INKAREA, RECTANGLE_INKAREA, ALL_INKAREA, CLIENTACTIVE_INK_MINOR
from cl_commondefines import MODEL_TYPE_SPHERE, STATE_TIME_LIMIT, STATE_TIME_FOREVER, SCENE_EVT_SHAPE_RECTANGLE, NWARRIOR_DROP_INKBEAD, CBEHAVIOR_SPHERE_AREAEVENT, CBEHAVIOR_DOUBLESPHERE_AREAEVENT
from cl_pxlayer import PXLAYER_EBULLET
from cl_object.logging import WarobjLog
import cl_msgcenter
import cl_engphyobj
import cl_object.reason
import cl_state
import cl_formula
import cl_math
import cl_snetwar
import math
INKPERFORM = [
    1326,
    1918,
    1920,
    1921]
INKAREA_MANAGER_STATE = 33068
INKAREA_HERO_STATE = 33097
INKAREA_MONSTER_STATE = 33154
INKBEAD_SID = 5531
SPECIALINKBEAD_SID = 5532

class CInkContainer(object):
    
    def __init__(self, oGame, oWarrior, dData):
        self.m_Game = oGame
        self.m_Owner = WeakProxy(oWarrior)
        self.m_Flag = 'Ink-%s' % oWarrior.m_PlayerID
        self.m_InkBeadNum = 2
        self.m_InkBead = { }
        self.m_InkValuePF = dData.get('InkValuePF', 0)
        self.m_MaxInkValue = dData.get('MaxInkValue', 0)
        self.m_PickInkBeadAdd = dData.get('PickInkBeadAdd', 0)
        self.m_InkValueThreshold = {
            INKVALUE_SUB: [],
            INKVALUE_ADD: [] }
        self.m_HeroInInkArea = { }
        self.m_MonsterInInkArea = { }
        self.m_SphereInkAreaEvent = { }
        self.m_InkAreaRecord = { }
        self.m_InkAreaSquareByType = { }
        self.m_InkAreaSquareFromThrow = { }
        self.m_CallOut = { }
        self.m_LimitInkValue = 1
        self.m_AreaIsOpened = 0
        self.InitEvent()

    
    def Save(self):
        dData = {
            'CurInkValue': self.GetCurInkValue() }
        return dData

    
    def Load(self, dData):
        iCurInkValue = dData.get('CurInkValue', 0)
        if iCurInkValue:
            self.ModifyInkValue(iCurInkValue, 'Load')

    
    def InitEvent(self):
        oGame = self.m_Game
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        self.m_InkAreaRecord = { { }: iType for iType in g_AreaType[:3] }
        self.m_InkAreaSquareByType = { { }: iType for iType in g_AreaType }
        cl_msgcenter.AddFunction(self.m_Owner, cl_msgcenter.MSG_WAR_PERFORM_END, self.OnCareerPerformEnd, self.m_Flag, iSub = PF_SUBMSG_CAREERPF, iOnce = 0, iPriority = -1)
        cl_msgcenter.AddFunction(self.m_Owner, cl_msgcenter.MSG_WAR_PERFORM_HALT, self.OnCareerPerformEnd, self.m_Flag, iSub = PF_SUBMSG_CAREERPF, iOnce = 0, iPriority = -1)
        cl_msgcenter.AddFunction(self.m_Owner, cl_msgcenter.MSG_WAR_LEAVESCENE, self.OnLeaveScene, self.m_Flag, iOnce = 0)
        cl_msgcenter.AddFunction(self.m_Owner, cl_msgcenter.MSG_WAR_PLAYERONREADY, self.OnReady, self.m_Flag, iOnce = 0)
        cl_msgcenter.AddAttentionFunc(self.m_Owner, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_ROOMGOAL, self.OnRoomGoal, self.m_Flag)
        oGame.AddGlobalAttention(self.m_Owner.m_ID, cl_msgcenter.MSG_WAR_MONSTER_START_HATE, self.OnMonsterStartHate, self.m_Flag)
        oGame.AddGlobalAttention(self.m_Owner.m_ID, cl_msgcenter.MSG_WAR_DIE, self.OnDie, self.m_Flag)

    
    def Release(self):
        oGame = self.m_Game
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneEvent(self.m_Owner, cl_msgcenter.MSG_WAR_PERFORM_END, self.m_Flag, iSub = PF_SUBMSG_CAREERPF)
        cl_msgcenter.DoneEvent(self.m_Owner, cl_msgcenter.MSG_WAR_PERFORM_HALT, self.m_Flag, iSub = PF_SUBMSG_CAREERPF)
        cl_msgcenter.DoneEvent(self.m_Owner, cl_msgcenter.MSG_WAR_ADDSTATE, self.m_Flag)
        cl_msgcenter.DoneEvent(self.m_Owner, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, self.m_Flag)
        cl_msgcenter.DoneEvent(self.m_Owner, cl_msgcenter.MSG_WAR_LEAVESCENE, self.m_Flag)
        cl_msgcenter.DoneEvent(self.m_Owner, cl_msgcenter.MSG_WAR_PLAYERONREADY, self.m_Flag)
        cl_msgcenter.DoneAttention(self.m_Owner, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_ROOMGOAL, self.m_Flag)
        oGame.DoneGlobalAttention(self.m_Owner.m_ID, cl_msgcenter.MSG_WAR_MONSTER_START_HATE, self.m_Flag)
        oGame.DoneGlobalAttention(self.m_Owner.m_ID, cl_msgcenter.MSG_WAR_DIE, self.m_Flag)
        for dTypeRecord in self.m_InkAreaRecord.values():
            for dRecord in dTypeRecord.values():
                dRecord.clear()
            
            dTypeRecord = { }
        
        self.m_InkAreaRecord = { }
        for dCall in self.m_CallOut.values():
            dCall.clear()
        
        self.m_CallOut = { }
        self.m_Owner = None
        self.m_Game = None

    
    def OnDie(self, oListener, oTarget, dInfo):
        if not oTarget or not self.CheckSameScene(oTarget.m_Scene):
            return None
        iFightType = oTarget.m_FightType
        if not iFightType & WARRIOR_MONSTER:
            return None
        if oTarget.m_ID in self.m_MonsterInInkArea:
            self.m_MonsterInInkArea.pop(oTarget.m_ID)
        oGame = self.m_Game
        oScene = oGame.m_SceneMgr.GetScene(oTarget.m_Scene)
        if not oScene:
            return None
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.GetLevelNode(oScene.m_Level)
        if not oLevelNode.CheckLevelPass():
            return None
        for iMonster in oScene.GetObjectsByType('Monster'):
            oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
            if not oMonster:
                continue
            return None
        
        self.ClearArea()

    
    def OnCareerPerformEnd(self, oTarget, dInfo):
        if 'pfid' not in dInfo['Skill'].m_Base or dInfo['Skill'].m_Base['pfid'] != oTarget.GetCareerPerformID():
            return None
        for iInkBead in list(self.m_InkBead):
            oInkBead = self.m_Game.GetObject(iInkBead)
            if oInkBead:
                self.RemoveInkBead(oInkBead, 'CareerPerformEnd')
        

    
    def OnMonsterStartHate(self, oListener, oTarget, dInfo):
        if self.m_AreaIsOpened or not (oTarget.m_FightType & WARRIOR_MONSTER) or oTarget.m_Scene != self.m_Owner.m_Scene:
            return None
        self.GeneralAreaByMode(self.m_Owner)

    
    def OnRoomGoal(self, oListener, oTarget, dInfo):
        if self.CheckSameScene(dInfo['oScene'].m_ID):
            self.ClearArea()

    
    def CheckSameScene(self, iTargetScene):
        if self.m_Owner.m_Scene != iTargetScene:
            return False
        return True

    
    def OnLeaveScene(self, oTarget, dInfo):
        self.ClearArea()
        dInkAreaInfo = self.GetInInkAreaInfoByType()
        if not dInkAreaInfo:
            return None
        dEffectInfo = {
            'MonsterEffect': 1,
            'DelayLeaveFrame': 0 }
        for iClearTarget, dAreaInfo in dict(dInkAreaInfo).items():
            oClearTarget = self.m_Game.GetObject(iClearTarget)
            if not oClearTarget:
                continue
            for iEventID in list(dAreaInfo):
                dEffectInfo['EventID'] = iEventID
                self.EffectInkArea(oClearTarget, dEffectInfo, iLeave = 1)
            
        

    
    def OnReady(self, oTarget, dInfo):
        if not dInfo['reenter']:
            return None
        if self.ValidDisplayArea():
            self.GeneralAreaByMode(oTarget)
        else:
            self.ClearArea()

    
    def GeneralAreaByMode(self, oTarget, bInit = True):
        oManagerState = oTarget.m_State.GetItemBySID(INKAREA_MANAGER_STATE)
        if not oManagerState:
            return None
        self.m_AreaIsOpened = 1
        iMode = oManagerState.GetCount()
        oGame = oTarget.m_Game
        lstPlayer = oGame.m_WarMgr.GetRoomPlayer()
        if iMode:
            cl_snetwar.GS2CTriggerBehavior(oGame, oTarget.m_ID, CBEHAVIOR_DOUBLESPHERE_AREAEVENT, lstPlayer, iStop = 1)
            cl_snetwar.GS2CTriggerBehavior(oGame, oTarget.m_ID, CBEHAVIOR_SPHERE_AREAEVENT, lstPlayer, iStop = 0)
            if bInit and HERO_SPHERE_AREAEVENT in self.m_SphereInkAreaEvent:
                oAreaEvent = self.m_SphereInkAreaEvent[HERO_SPHERE_AREAEVENT]
                if oAreaEvent:
                    oAreaEvent.Enable()
                
            if not bInit:
                for iAreaEventType in self.m_SphereInkAreaEvent:
                    oAreaEvent = self.m_SphereInkAreaEvent[iAreaEventType]
                    if not oAreaEvent:
                        continue
                    if iAreaEventType != HERO_SPHERE_AREAEVENT:
                        oAreaEvent.Disable()
                        continue
                    oAreaEvent.Enable()
                
            else:
                cl_snetwar.GS2CTriggerBehavior(oGame, oTarget.m_ID, CBEHAVIOR_SPHERE_AREAEVENT, lstPlayer, iStop = 1)
                cl_snetwar.GS2CTriggerBehavior(oGame, oTarget.m_ID, CBEHAVIOR_DOUBLESPHERE_AREAEVENT, lstPlayer, iStop = 0)
                if bInit:
                    oInnerAreaEvent = self.m_SphereInkAreaEvent[HERO_INNERSPHERE_AREAEVENT] if HERO_INNERSPHERE_AREAEVENT in self.m_SphereInkAreaEvent else None
                    oOuterAreaEvent = self.m_SphereInkAreaEvent[HERO_OUTERSPHERE_AREAEVENT] if HERO_OUTERSPHERE_AREAEVENT in self.m_SphereInkAreaEvent else None
                    if oInnerAreaEvent and oOuterAreaEvent:
                        oInnerAreaEvent.Enable()
                        oOuterAreaEvent.Enable()
                    else:
                        for iAreaEventType in self.m_SphereInkAreaEvent:
                            oAreaEvent = self.m_SphereInkAreaEvent[iAreaEventType]
                            if not oAreaEvent:
                                continue
                            if iAreaEventType == HERO_SPHERE_AREAEVENT:
                                oAreaEvent.Disable()
                                continue
                            oAreaEvent.Enable()
                        
        self.ClearInkAreaSquareRecord()

    
    def ClearArea(self):
        if not self.m_AreaIsOpened:
            return None
        self.m_AreaIsOpened = 0
        oGame = self.m_Game
        lstPlayer = oGame.m_WarMgr.GetRoomPlayer()
        for iBehavior in (CBEHAVIOR_SPHERE_AREAEVENT, CBEHAVIOR_DOUBLESPHERE_AREAEVENT):
            cl_snetwar.GS2CTriggerBehavior(oGame, self.m_Owner.m_ID, iBehavior, lstPlayer, iStop = 1)
        
        for iAreaEventType in self.m_SphereInkAreaEvent:
            oAreaEvent = self.m_SphereInkAreaEvent[iAreaEventType]
            if oAreaEvent:
                oAreaEvent.Disable()
        
        self.ClearInkAreaSquareRecord()

    
    def ValidDisplayArea(self):
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Owner.m_Scene)
        if oScene and oScene.m_SceneData.GetFightMonster():
            return True
        return False

    
    def CheckAreaIsOpened(self):
        return self.m_AreaIsOpened

    
    def ModifyInkValue(self, iValue, sReason, dExtra = None):
        if not iValue:
            return None
        oOwner = self.m_Owner
        if not oOwner:
            return None
        oPerform = oOwner.GetPerform(self.m_InkValuePF)
        if not oPerform:
            return None
        iOldVal = oPerform.CurPFBullet()
        oReason = cl_object.reason.CStrReason(sReason)
        dMsgInfo = {
            'Modify': iValue,
            'RS': oReason }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_BEFORE_CHANGE_INKVALUE, oOwner, dMsgInfo)
        if not dExtra or not dExtra.get('Fixed', 0):
            iValue = dMsgInfo['Modify']
        iNeedChange = iValue
        if iNeedChange > 0:
            if self.m_LimitInkValue and iOldVal > self.m_MaxInkValue - iNeedChange:
                iValue = self.m_MaxInkValue - iOldVal
            oPerform.AddPFBullet(iValue)
            iSubMsg = INKVALUE_ADD
        elif iOldVal < -iNeedChange:
            iValue = -iOldVal
        oPerform.CostPFBullet(-iValue)
        iSubMsg = INKVALUE_SUB
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CHANGE_INKVALUE, oOwner, {
            'NeedChange': iNeedChange,
            'RealChange': iValue,
            'RS': oReason }, iSub = iSubMsg)
        self.RefreshInkValueThreshold(iOldVal, oPerform.CurPFBullet(), iSubMsg)

    
    def RefreshInkValueThreshold(self, iOldVal, iNowVal, iDirect):
        for iThreshold, _, func in self.m_InkValueThreshold[iDirect]:
            if iDirect == INKVALUE_ADD:
                if iOldVal >= iThreshold or iNowVal < iThreshold:
                    continue
                continue
            if iDirect == INKVALUE_SUB:
                if iNowVal >= iThreshold or iOldVal < iThreshold:
                    continue
                continue
            func(self.m_Owner, {
                'Threshold': iThreshold,
                'Direct': iDirect,
                'OldVal': iOldVal,
                'NowVal': iNowVal })
        

    
    def AddInkValueThreshold(self, iThreshold, iDirect, sKey, func, iUnique):
        if iDirect not in self.m_InkValueThreshold:
            return None
        if iUnique:
            lstInkValueThreshold = []
            for iCheckThreshold, sCheckKey, fCheckFunc in self.m_InkValueThreshold[iDirect]:
                if sCheckKey == sKey:
                    continue
                lstInkValueThreshold.append((iCheckThreshold, sCheckKey, fCheckFunc))
            
            self.m_InkValueThreshold[iDirect] = lstInkValueThreshold
        self.m_InkValueThreshold[iDirect].append((iThreshold, sKey, func))

    
    def ClearInkValueThreshold(self, iClearThreshold, iDirect, sClearKey):
        if iDirect not in self.m_InkValueThreshold:
            return None
        lstInkValueThreshold = []
        for iThreshold, sKey, func in self.m_InkValueThreshold[iDirect]:
            if iClearThreshold == iThreshold and sClearKey == sKey:
                continue
            lstInkValueThreshold.append((iThreshold, sKey, func))
        
        self.m_InkValueThreshold[iDirect] = lstInkValueThreshold

    
    def GetCurInkValue(self):
        oPerform = self.m_Owner.GetPerform(self.m_InkValuePF)
        if oPerform:
            iCurPFBullet = oPerform.CurPFBullet()
            if iCurPFBullet:
                return iCurPFBullet
        return 0

    
    def GetMaxInkValue(self):
        return self.m_MaxInkValue

    
    def ModifyMaxInkValue(self, iModify):
        if iModify < 0 and -iModify > self.m_MaxInkValue:
            iModify = -(self.m_MaxInkValue)
        self.m_MaxInkValue += iModify
        return iModify

    
    def SetLimitInkValue(self, iLimit):
        self.m_LimitInkValue = iLimit

    
    def CreateInkBead(self, oSkill, lstPos, fCheckDis):
        iScene = oSkill.m_Base['Scene']
        if not iScene:
            return None
        oGame = self.m_Game
        oScene = oGame.m_SceneMgr.GetScene(iScene)
        if not oScene:
            return None
        oAttack = self.m_Owner
        vAttack = oAttack.GetPos()
        iCreateCount = 0
        lstIllegalPos = []
        iNeedNum = self.GetInkBeadNum()
        if not iNeedNum:
            return None
        dInfo = {
            'AddInkValue': self.GetPickInkBeadAdd(),
            'SID': INKBEAD_SID,
            'InkBeadType': PICK_INKBEAD }
        for vPos in lstPos:
            if not cl_math.CheckDistance(vPos, vAttack, fCheckDis):
                lstIllegalPos.append(vPos)
            dMsgInfo = {
                'DropInfo': dInfo }
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_BEFORECREATEINKBEAD, oAttack, dMsgInfo)
            oInkBead = oGame.GetResMgr().CreateDrop(iScene, NWARRIOR_DROP_INKBEAD, vPos, [
                dMsgInfo['DropInfo']], { }, iOwner = oAttack.m_ID)
            self.m_InkBead[oInkBead.m_ID] = 1
            iCreateCount += 1
            if iCreateCount >= iNeedNum:
                break
        
        if lstIllegalPos:
            WarobjLog.Warn('%s %s level:%s inkbead create illegalpos:%s attackpos:%s' % (oGame.m_ID, oAttack.m_ID, oScene.m_Level, lstIllegalPos, vAttack))

    
    def PickUpAllInkBead(self):
        for iInkBead in list(self.m_InkBead):
            oInkBead = self.m_Game.GetObject(iInkBead)
            if oInkBead:
                oInkBead.DelayPick(self.m_Owner)
        

    
    def RemoveInkBead(self, oInkBead, sReason):
        if oInkBead.m_ID in self.m_InkBead:
            oInkBead.Remove(sReason)
            self.m_InkBead.pop(oInkBead.m_ID)

    
    def GetInkBeadNum(self):
        return self.m_InkBeadNum

    
    def ModifyInkBeadNum(self, iModify):
        if iModify < 0 and -iModify > self.m_InkBeadNum:
            iModify = -(self.m_InkBeadNum)
        self.m_InkBeadNum += iModify
        return iModify

    
    def GetPickInkBeadAdd(self):
        return self.m_PickInkBeadAdd

    
    def CheckTargetInInkArea(self, iTarget):
        return self.CheckTargetInInkAreaNum(iTarget) > 0

    
    def CheckTargetInInkAreaNum(self, iTarget):
        oTarget = self.m_Game.GetObject(iTarget)
        if oTarget:
            iFightType = oTarget.m_FightType
            if iFightType & WARRIOR_HERO and iTarget in self.m_HeroInInkArea:
                return len(self.m_HeroInInkArea[iTarget])
            if iFightType & WARRIOR_MONSTER and iTarget in self.m_MonsterInInkArea:
                return len(self.m_MonsterInInkArea[iTarget])
        return 0

    
    def AddInkAreaByType(self, iTarget, iFightType, iArea):
        if not iTarget or not iArea:
            return None
        dAddInkArea = self.GetInInkAreaInfoByType(iFightType)
        if iTarget in dAddInkArea:
            dAddInkArea[iTarget][iArea] = 1
        else:
            dAddInkArea[iTarget] = {
                iArea: 1 }

    
    def ClearInkAreaByType(self, iTarget, iFightType, iArea):
        if not iTarget or not iArea:
            return None
        dClearInkArea = self.GetInInkAreaInfoByType(iFightType)
        if iTarget in dClearInkArea and iArea in dClearInkArea[iTarget]:
            dClearInkArea[iTarget].pop(iArea)
            if not dClearInkArea[iTarget]:
                dClearInkArea.pop(iTarget)

    
    def GetInInkAreaInfoByType(self, iFightType = 0):
        dInInkAreaInfo = { }
        if not iFightType:
            dInInkAreaInfo.update(self.m_HeroInInkArea)
            dInInkAreaInfo.update(self.m_MonsterInInkArea)
        elif iFightType & WARRIOR_HERO:
            dInInkAreaInfo = self.m_HeroInInkArea
        elif iFightType & WARRIOR_MONSTER:
            dInInkAreaInfo = self.m_MonsterInInkArea
        return dInInkAreaInfo

    
    def GetNumInInkAreaByType(self, iFightType = 0):
        return len(self.GetInInkAreaInfoByType(iFightType))

    
    def AddInkAreaRecord(self, iType, iEventID, dRecord):
        if not iType or not dRecord:
            return None
        self.m_InkAreaRecord[iType][iEventID] = dRecord
        if iType == RECTANGLE_INKAREA and self.IsFromMinor(dRecord):
            self.RecordRectangleInkAreaSquare(iEventID, dRecord, bRecordPointByType = False)
        self.ClearInkAreaSquareRecord()

    
    def DumpInkAreaRecord(self, iType, iEventID):
        if iType not in self.m_InkAreaRecord or iEventID not in self.m_InkAreaRecord[iType]:
            return None
        if iEventID != self.m_Owner.m_ID:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_INKAREADISAPPEAR_DUMP, self.m_Owner, {
                'EventID': iEventID })
        dRecord = self.m_InkAreaRecord[iType].pop(iEventID)
        if iType == RECTANGLE_INKAREA and self.IsFromMinor(dRecord):
            self.m_InkAreaSquareFromThrow.pop(iEventID, { })
        self.ClearInkAreaSquareRecord()

    
    def IsFromMinor(self, dRecord):
        oThrowPerform = self.m_Owner.GetThrowPerform()
        if oThrowPerform and dRecord['RSPerform'] in (oThrowPerform.m_SID, CLIENTACTIVE_INK_MINOR):
            return True
        return False

    
    def ClearInkAreaSquareRecord(self):
        for iType in g_AreaType:
            if iType in self.m_InkAreaSquareByType and self.m_InkAreaSquareByType[iType]:
                self.m_InkAreaSquareByType[iType] = { }
        
        self.m_InkAreaSquareByType[ALL_INKAREA] = { }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_INKAREASQUARERECORD_CHANGE, self.m_Owner, { })

    
    def GetInkAreaRecord(self, iType, iEventID):
        if iType not in self.m_InkAreaRecord or iEventID not in self.m_InkAreaRecord[iType]:
            return []
        return self.m_InkAreaRecord[iType][iEventID]

    
    def GetInkAreaSquareByEventID(self, iEventID):
        for iType in self.m_InkAreaRecord:
            if iEventID in self.m_InkAreaRecord[iType]:
                dRecord = self.m_InkAreaRecord[iType][iEventID]
                if iType == RECTANGLE_INKAREA:
                    (iLength, iWidth) = dRecord['Range']
                    return math.ceil(iLength * iWidth * 4)
                if iType == SPHERE_INKAREA:
                    iRadius = dRecord['Range']
                    return math.ceil(math.pi * iRadius ** 2)
        
        return 0

    
    def GetCurInkAreaSquareByType(self, iType):
        if iType not in self.m_InkAreaSquareByType:
            return 0
        if not self.m_InkAreaSquareByType[iType]:
            if iType == ALL_INKAREA:
                for iRecordType in self.m_InkAreaRecord:
                    self.RecordSquareByType(iRecordType, iRecordInAll = 1)
                
            else:
                self.RecordSquareByType(iType)
        return len(self.m_InkAreaSquareByType[iType])

    
    def RecordSquareByType(self, iType, iRecordInAll = 0):
        if iType == DOUBLESPHERE_INKAREA:
            oInnerAttachEvent = self.GetSphereInkAreaEventByType(HERO_INNERSPHERE_AREAEVENT)
            oOuterAttachEvent = self.GetSphereInkAreaEventByType(HERO_OUTERSPHERE_AREAEVENT)
            if oInnerAttachEvent and oOuterAttachEvent:
                if not oInnerAttachEvent.E_IsTrigger() or not oOuterAttachEvent.E_IsTrigger():
                    return None
        for iEventID, dRecord in self.m_InkAreaRecord[iType].items():
            if iType == RECTANGLE_INKAREA:
                self.RecordRectangleInkAreaSquare(iEventID, dRecord, iRecordInAll)
                continue
            oOwner = self.m_Game.GetObject(iEventID)
            if not oOwner:
                continue
            vPos = oOwner.GetPos()
            vOffsetCenter = (round(vPos[0]), vPos[1], round(vPos[2]))
            if iType == SPHERE_INKAREA:
                if oOwner.m_FightType & WARRIOR_HERO:
                    oSphereEvent = self.GetSphereInkAreaEventByType(HERO_SPHERE_AREAEVENT)
                    if oSphereEvent and not oSphereEvent.E_IsTrigger():
                        continue
                    continue
                iRadius = dRecord['Range']
                self.RecordSphereSquare(vOffsetCenter, iRadius, iRecordInAll)
                continue
            (iOuterRadius, iInnerRadius) = dRecord['Range']
            self.RecordDoubleSphereSquare(vOffsetCenter, iOuterRadius, iInnerRadius, iRecordInAll)
        

    
    def GetCurSquareFromThrow(self):
        dAllPointInfo = { }
        for dInfo in self.m_InkAreaSquareFromThrow.values():
            for tPoint in dInfo:
                if tPoint not in dAllPointInfo:
                    dAllPointInfo[tPoint] = 1
            
        
        return len(dAllPointInfo)

    
    def RecordRectangleInkAreaSquare(self, iEventID, dRecord, iRecordInAll = 0, bRecordPointByType = True):
        vPos = dRecord['Pos']
        tRange = dRecord['Range']
        vDir = dRecord['Dir']
        vOffsetCenter = (round(vPos[0]), vPos[1], round(vPos[2]))
        self.RecordRectangleSquare(iEventID, vOffsetCenter, tRange, vDir, iRecordInAll, bRecordPointByType)

    
    def RecordSphereSquare(self, vPos, iRadius, iRecordInAll):
        vLeftHeight = (vPos[0] - iRadius, vPos[1], vPos[2] + iRadius)
        iRange = 2 * iRadius + 1
        for iZOffset in range(1, iRange):
            for iXOffset in range(1, iRange):
                vTar = (vLeftHeight[0] + iXOffset, vLeftHeight[1], vLeftHeight[2] - iZOffset)
                if not cl_math.CheckDistance(vPos, vTar, iRadius):
                    continue
                self.RecordPointByType(vTar[0], vTar[2], SPHERE_INKAREA, iRecordInAll)
            
        

    
    def RecordDoubleSphereSquare(self, vPos, iOuterRadius, iInnerRadius, iRecordInAll):
        vLeftHeight = (vPos[0] - iOuterRadius, vPos[1], vPos[2] + iOuterRadius)
        for iZOffset in range(1, 2 * iOuterRadius + 1):
            for iXOffset in range(1, 2 * iOuterRadius + 1):
                vTar = (vLeftHeight[0] + iXOffset, vLeftHeight[1], vLeftHeight[2] - iZOffset)
                if iInnerRadius < cl_math.CalDistance(vPos, vTar) and not (cl_math.CalDistance(vPos, vTar) < iOuterRadius):
                    continue
                self.RecordPointByType(vTar[0], vTar[2], DOUBLESPHERE_INKAREA, iRecordInAll)
            
        

    
    def RecordRectangleSquare(self, iEventID, vPos, tRange, vDir, iRecordInAll, bRecordPointByType):
        vReverseDir = (-vDir[0], vDir[1], -vDir[2])
        (iLength, iWidth) = tRange
        vHeightCenter = cl_math.Vec3DisplaceDir(vPos, vDir, iLength)
        vLeftHPoint = cl_math.Vec3DisplaceDir(vHeightCenter, (-vDir[2], vDir[1], vDir[0]), iWidth)
        vRightHPoint = cl_math.Vec3DisplaceDir(vHeightCenter, (vDir[2], vDir[1], -vDir[0]), iWidth)
        vRightLPoint = cl_math.Vec3DisplaceDir(vRightHPoint, vReverseDir, 2 * iLength)
        vLeftLPoint = cl_math.Vec3DisplaceDir(vLeftHPoint, vReverseDir, 2 * iLength)
        lstPointX = [
            vLeftHPoint[0],
            vRightHPoint[0],
            vRightLPoint[0],
            vLeftLPoint[0]]
        lstPointZ = [
            vLeftHPoint[2],
            vRightHPoint[2],
            vRightLPoint[2],
            vLeftLPoint[2]]
        (iLeft, iRight, iBottom, iTop) = (round(min(lstPointX)), round(max(lstPointX)), round(min(lstPointZ)), round(max(lstPointZ)))
        vLeftHeight = (iLeft, vPos[1], iTop)
        for iZOffset in range(1, abs(iTop - iBottom) + 1):
            for iXOffset in range(1, abs(iRight - iLeft) + 1):
                vTar = (vLeftHeight[0] + iXOffset, vLeftHeight[1], vLeftHeight[2] - iZOffset)
                vRoundX = vTar[0]
                vRoundZ = vTar[2]
                if not (self.GetVectorCross(vLeftHPoint, vRightHPoint, vTar) * self.GetVectorCross(vRightLPoint, vLeftLPoint, vTar) >= 0) and self.GetVectorCross(vRightHPoint, vRightLPoint, vTar) * self.GetVectorCross(vLeftLPoint, vLeftHPoint, vTar) >= 0:
                    continue
                if bRecordPointByType:
                    self.RecordPointByType(vRoundX, vRoundZ, RECTANGLE_INKAREA, iRecordInAll)
                    continue
                self.RecordPointFromThrow(iEventID, vRoundX, vRoundZ)
            
        

    
    def GetVectorCross(self, vLeftPoint, vRightPoint, vTar):
        return (vRightPoint[0] - vLeftPoint[0]) * (vTar[2] - vLeftPoint[2]) - (vTar[0] - vLeftPoint[0]) * (vRightPoint[2] - vLeftPoint[2])

    
    def RecordPointByType(self, vX, vZ, iRecordType, iRecordInAll):
        if (vX, vZ) not in self.m_InkAreaSquareByType[iRecordType]:
            self.m_InkAreaSquareByType[iRecordType][(vX, vZ)] = 1
        if iRecordInAll and (vX, vZ) not in self.m_InkAreaSquareByType[ALL_INKAREA]:
            self.m_InkAreaSquareByType[ALL_INKAREA][(vX, vZ)] = 1

    
    def RecordPointFromThrow(self, iEventID, vX, vZ):
        if iEventID not in self.m_InkAreaSquareFromThrow:
            self.m_InkAreaSquareFromThrow[iEventID] = { }
        if (vX, vZ) not in self.m_InkAreaSquareFromThrow[iEventID]:
            self.m_InkAreaSquareFromThrow[iEventID][(vX, vZ)] = 1

    
    def AddSphereInkAreaEvent(self, iAreaEventType, oEvent):
        if iAreaEventType in g_HeroAreaEventType:
            self.m_SphereInkAreaEvent[iAreaEventType] = oEvent

    
    def ClearSphereInkAreaEvent(self, iAreaEventType):
        if iAreaEventType in g_HeroAreaEventType and iAreaEventType in self.m_SphereInkAreaEvent:
            oEvent = self.m_SphereInkAreaEvent[iAreaEventType]
            oEvent.Unstall()
            oEvent = None
            self.m_SphereInkAreaEvent.pop(iAreaEventType)

    
    def GetSphereInkAreaEventByType(self, iAreaEventType):
        if iAreaEventType in g_HeroAreaEventType and iAreaEventType in self.m_SphereInkAreaEvent:
            return self.m_SphereInkAreaEvent[iAreaEventType]

    
    def CreateRectangleInkArea(self, oTarget, dInfo):
        
        def ClearFunc(oListener, oLifeCycle):
            for iTriggerObj in lstInScene[:]:
                SceneLeaveFunc(None, {
                    'VID': iTriggerObj })
            
            self.DumpInkAreaRecord(iAreaType, iSceneEvtID)
            oScene = oGame.m_SceneMgr.GetScene(iScene)
            if not oScene:
                return None
            oScene.RemoveSceneEvent(iSceneEvtID)

        
        def SceneLeaveFunc(oListener, dData):
            iTriggerObj = dData['VID']
            obj = oGame.GetObject(iTriggerObj)
            if not self.ValidTrigger(obj):
                return None
            if iTriggerObj in lstInScene:
                lstInScene.remove(iTriggerObj)
            self.EffectInkArea(obj, dInfo, iLeave = 1)

        
        def SceneEnterFunc(oListener, dData):
            iTriggerObj = dData['VID']
            obj = oGame.GetObject(iTriggerObj)
            if not self.ValidTrigger(obj):
                return None
            lstInScene.append(iTriggerObj)
            self.EffectInkArea(obj, dInfo, iLeave = 0)

        oGame = self.m_Game
        iScene = oTarget.m_Scene
        oScene = oGame.m_SceneMgr.GetScene(iScene)
        if not oScene:
            return None
        lstInScene = []
        iAreaType = RECTANGLE_INKAREA
        lstArgs = [
            dInfo['Pos'],
            (dInfo['HalfX'], dInfo['HalfY'], dInfo['HalfZ'])]
        iSceneEvtID = oScene.AddSceneEvent(oTarget, SceneEnterFunc, SceneLeaveFunc, SCENE_EVT_SHAPE_RECTANGLE, lstArgs, dInfo)
        dInfo['EventID'] = iSceneEvtID
        dRecord = {
            'RSPerform': dInfo['RSPerform'],
            'Pos': dInfo['Pos'],
            'Range': (round(dInfo['HalfX']), round(dInfo['HalfZ'])),
            'Dir': dInfo['Dir'] }
        if 'LifeCycle' in dInfo:
            oLifeCycle = dInfo['LifeCycle']
            if oLifeCycle:
                dRecord['LifeCycle'] = oLifeCycle
                oLifeCycle.AddDisableFunc(ClearFunc)
        self.AddInkAreaRecord(iAreaType, iSceneEvtID, dRecord)
        iStayTime = cl_formula.GetResultByData(oTarget, dInfo['StayTime'], { })
        self.Call_Out(iSceneEvtID, Time2Frame(iStayTime), Functor(ClearFunc, None, None))

    
    def CreateSphereInkArea(self, oTarget, fRadius, dInfo):
        
        def ClearFunc(oListener, oLifeCycle):
            for iTarget in lstInScene[:]:
                oClearTarget = oTarget.m_Game.GetObject(iTarget)
                if not oClearTarget:
                    continue
                OnTrigger(oClearTarget, 1)
            
            self.DumpInkAreaRecord(iAreaType, oTarget.m_ID)
            if oTarget.m_FightType & WARRIOR_HERO:
                self.ClearSphereInkAreaEvent(HERO_SPHERE_AREAEVENT)
            else:
                oAttachEvent.Unstall()

        
        def OnTrigger(obj, iLeave):
            if not self.ValidTrigger(obj):
                return None
            if not iLeave:
                lstInScene.append(obj.m_ID)
            elif obj.m_ID in lstInScene:
                lstInScene.remove(obj.m_ID)
            self.EffectInkArea(obj, dInfo, iLeave)

        oGame = self.m_Game
        lstInScene = []
        iAreaType = SPHERE_INKAREA
        dOuterShape = {
            'Shape': MODEL_TYPE_SPHERE,
            'Radius': fRadius }
        oAttachEvent = cl_engphyobj.CreateAttachEventObject(oGame, oTarget, PXLAYER_EBULLET, dOuterShape, OnTrigger)
        oAttachEvent.rigidbody.E_SetKinematic(1)
        dInfo['EventID'] = oTarget.m_ID
        dRecord = {
            'RSPerform': dInfo['RSPerform'],
            'Range': int(fRadius) }
        if 'LifeCycle' in dInfo:
            oLifeCycle = dInfo['LifeCycle']
            if oLifeCycle:
                dRecord['LifeCycle'] = oLifeCycle
                oLifeCycle.AddDisableFunc(ClearFunc)
        self.AddInkAreaRecord(iAreaType, oTarget.m_ID, dRecord)
        if oTarget.m_FightType & WARRIOR_HERO:
            self.AddSphereInkAreaEvent(HERO_SPHERE_AREAEVENT, oAttachEvent)
            return oAttachEvent

    
    def CreateDoubleSphereInkArea(self, oTarget, fOuterRadius, fInnerRadius, dInfo):
        
        def ClearFunc(oListener, oLifeCycle):
            for iTarget in lstInScene[:]:
                oClearTarget = oTarget.m_Game.GetObject(iTarget)
                if not oClearTarget:
                    continue
                OnOuterTrigger(oClearTarget, 1)
            
            self.DumpInkAreaRecord(iAreaType, oTarget.m_ID)
            self.ClearSphereInkAreaEvent(HERO_INNERSPHERE_AREAEVENT)
            self.ClearSphereInkAreaEvent(HERO_OUTERSPHERE_AREAEVENT)

        
        def OnOuterTrigger(obj, iLeave):
            if obj.m_ID == self.m_Owner.m_ID:
                return None
            if not self.ValidTrigger(obj):
                return None
            if not iLeave:
                lstInScene.append(obj.m_ID)
            elif obj.m_ID in lstInScene:
                lstInScene.remove(obj.m_ID)
            self.EffectInkArea(obj, dInfo, iLeave)

        
        def OnInnerTrigger(obj, iLeave):
            if obj.m_ID != self.m_Owner.m_ID and obj.m_FightType & WARRIOR_BOSS != WARRIOR_BOSS:
                iLeave = iLeave ^ 1
                OnOuterTrigger(obj, iLeave)

        oGame = self.m_Game
        lstInScene = []
        iAreaType = DOUBLESPHERE_INKAREA
        dOuterShape = {
            'Shape': MODEL_TYPE_SPHERE,
            'Radius': fOuterRadius }
        oOuterAttachEvent = cl_engphyobj.CreateAttachEventObject(oGame, oTarget, PXLAYER_EBULLET, dOuterShape, OnOuterTrigger)
        oOuterAttachEvent.rigidbody.E_SetKinematic(1)
        self.AddSphereInkAreaEvent(HERO_OUTERSPHERE_AREAEVENT, oOuterAttachEvent)
        dInnerShape = {
            'Shape': MODEL_TYPE_SPHERE,
            'Radius': fInnerRadius }
        oInnerAttachEvent = cl_engphyobj.CreateAttachEventObject(oGame, oTarget, PXLAYER_EBULLET, dInnerShape, OnInnerTrigger)
        oInnerAttachEvent.rigidbody.E_SetKinematic(1)
        self.AddSphereInkAreaEvent(HERO_INNERSPHERE_AREAEVENT, oInnerAttachEvent)
        dInfo['EventID'] = oTarget.m_ID
        dRecord = {
            'RSPerform': dInfo['RSPerform'],
            'Range': (int(fOuterRadius), int(fInnerRadius)) }
        if 'LifeCycle' in dInfo:
            oLifeCycle = dInfo['LifeCycle']
            if oLifeCycle:
                dRecord['LifeCycle'] = oLifeCycle
                oLifeCycle.AddDisableFunc(ClearFunc)
        self.AddInkAreaRecord(iAreaType, oTarget.m_ID, dRecord)
        return (oOuterAttachEvent, oInnerAttachEvent)

    
    def SwitchSphereInkAreaByType(self, lstType, iEnable = 1):
        for iAreaEventType in lstType:
            oAreaEvent = self.GetSphereInkAreaEventByType(iAreaEventType)
            if not oAreaEvent:
                continue
            if iEnable or self.ValidDisplayArea():
                oAreaEvent.Enable()
                continue
            oAreaEvent.Disable()
        

    
    def ValidTrigger(self, obj):
        if not obj or not (obj.m_ID):
            return False
        iFightType = obj.m_FightType
        if not iFightType & WARRIOR_HERO or iFightType & WARRIOR_MONSTER:
            return False
        if iFightType & WARRIOR_HERO and obj.m_ID != self.m_Owner.m_ID:
            return False
        return True

    
    def EffectInkArea(self, obj, dInfo, iLeave):
        oOwner = self.m_Owner
        (iState, iStateTime, iPerformLevel, iDelayLeaveFrame) = (0, 0, 0, 0)
        if obj.m_FightType & WARRIOR_HERO:
            iState = INKAREA_HERO_STATE
            iStateTime = cl_formula.GetResultByData(oOwner, dInfo['HeroStateTime'], { }) if 'HeroStateTime' in dInfo else 0
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_BEFORE_HEROTRIGGERINKAREA, oOwner, dInfo, iSub = iLeave + 1)
        elif obj.m_FightType & WARRIOR_MONSTER and 'MonsterEffect' in dInfo and 'DelayLeaveFrame' in dInfo:
            iMonsterEffect = cl_formula.GetResultByData(oOwner, dInfo['MonsterEffect'], { })
            if iMonsterEffect:
                iState = INKAREA_MONSTER_STATE
                iStateTime = dInfo['MonsterStateTime'] if 'MonsterStateTime' in dInfo else 0
                iPerformLevel = iMonsterEffect
                iDelayLeaveFrame = cl_formula.GetResultByData(oOwner, dInfo['DelayLeaveFrame'], { })
        if not iLeave:
            self.AddInkAreaByType(obj.m_ID, obj.m_FightType, iArea = dInfo['EventID'])
            if iState:
                self._EnterInkArea(obj, iState, iStateTime, iPerformLevel)
            else:
                self.ClearInkAreaByType(obj.m_ID, obj.m_FightType, iArea = dInfo['EventID'])
                if iState:
                    self._LeaveInkArea(obj, iState, iDelayLeaveFrame)
        return cl_formula.GetResultByData(oOwner, dInfo['HeroStateTime'], { })

    
    def _EnterInkArea(self, obj, iState, iStateTime, iPerformLevel = 0):
        dArgs = {
            'AID': self.m_Owner.m_ID,
            'RS': cl_object.reason.CStrReason('inkconcreate'),
            'arg': { },
            'PFLV': iPerformLevel }
        iTimeType = STATE_TIME_LIMIT if iStateTime else STATE_TIME_FOREVER
        oState = cl_state.AddState(obj, iState, iTimeType, Time2Frame(iStateTime), dArgs)
        if oState:
            oState.Enable(obj)

    
    def _LeaveInkArea(self, obj, iState, iDelayLeaveFrame = 0):
        lstState = obj.m_State.GetItems(iState)
        for oTargetState in lstState:
            if not oTargetState or oTargetState.m_Attacker != self.m_Owner.m_ID:
                continue
            if iDelayLeaveFrame:
                oTargetState.SetTime(obj, iDelayLeaveFrame, 0)
                continue
            if self.CheckTargetInInkArea(obj.m_ID):
                continue
            obj.m_State.RemoveItem(oTargetState.m_ID)
        

    
    def Call_Out(self, iKey, iFrame, func):
        iCallFrame = self.m_Game.GetFrameNum() + iFrame
        if iCallFrame not in self.m_CallOut:
            self.m_CallOut[iCallFrame] = { }
            self.m_Owner.Call_Out(self.CallBack, iFrame, self.m_Flag)
        lstFunc = self.m_CallOut[iCallFrame].setdefault(iKey, [])
        lstFunc.append(func)

    
    def CallBack(self):
        iCurFrame = self.m_Game.GetFrameNum()
        if iCurFrame not in self.m_CallOut:
            return None
        dCallOut = self.m_CallOut.pop(iCurFrame)
        for lstFunc in dCallOut.values():
            for func in lstFunc:
                func()
            
        
        dCallOut.clear()

    
    def DelayCallBack(self, iKey, iDelayFrame):
        for iFrame, dFuncInfo in self.m_CallOut.items():
            if iKey in dFuncInfo:
                lstFunc = self.m_CallOut[iFrame].pop(iKey)
                iCallFrame = (iFrame - self.m_Game.GetFrameNum()) + iDelayFrame
                self.Call_Out(iKey, iCallFrame, lstFunc[0])
                break
        

    
    def ClearTargetCallOut(self, iKey):
        dEmptyCall = { }
        for iCallFrame, dCall in self.m_CallOut.items():
            dCall.pop(iKey, { })
            if not dCall:
                dEmptyCall[iCallFrame] = 1
        
        for iCallFrame in dEmptyCall:
            self.m_CallOut.pop(iCallFrame)
        


