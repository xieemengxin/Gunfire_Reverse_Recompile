# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/custom/talent/customaction.pyc
# RelativePath: clientlogic/cl_platformdata/custom/talent/customaction.pyc
# Source Generated with Decompyle++
# File: customaction.pyc (Python 3.6)

import cl_formula
import cl_snetwar
from cl_commondefines import GAMBLER_CHOOSE_EQUITY, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_ALL, PICK_SPECIALINKBEAD, INKMASTER_HERO, NWARRIOR_VIRTUAL_DYNCEVENT, WARRIOR_MONSTER, HERO_INNERSPHERE_AREAEVENT, HERO_OUTERSPHERE_AREAEVENT, DOUBLESPHERE_INKAREA, RECTANGLE_INKAREA, STATE_TIME_LIMIT, SPHERE_INKAREA, HERO_SPHERE_AREAEVENT, BIG_LION_STATE
from cl_container.inkcon import INKAREA_MONSTER_STATE, INKAREA_HERO_STATE, INKAREA_MANAGER_STATE, SPECIALINKBEAD_SID
from cl_only import Functor, PY_FLAG_DEAD, Time2Frame
import cl_evact
import cl_state
import cl_math

def CustomAction3212(oWarrior, oLifeCycle, dInfo):
    
    def Reset(oTarget, oLifeCycle):
        oTarget.m_GamblerCon.SetMix2LowProb(0)

    iProb = cl_formula.GetResultByData(oWarrior, dInfo['Mix2LowProb'], {
        'LifeCycle': oLifeCycle })
    oWarrior.m_GamblerCon.SetMix2LowProb(iProb)
    oLifeCycle.AddDisableFunc(Reset)


def CustomAction3218(oWarrior, oEventCB, dInfo):
    oPerform = oWarrior.GetPerform(dInfo['Perform'], 0)
    if not oPerform:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oPerform.AddCanUseCount()
    iAssignQuality = oWarrior.m_GamblerCon.GetCurCombQuality()
    iQualityNum = cl_formula.GetResultByData(oWarrior, dInfo['QualityNum'], dEventInfo, dMsgInfo)
    iQuality = oWarrior.m_GamblerCon.TryAppendQuality(iAssignQuality, GAMBLER_CHOOSE_EQUITY, True, iQualityNum)
    dArgs = {
        'CardNum': dInfo['CardNum'],
        'Quality': iQuality }
    if 'ThrowMsg' in dInfo:
        dArgs['ThrowMsg'] = dInfo['ThrowMsg']
    cl_snetwar.GS2CNotifyStartSkill(oWarrior.m_Game, oWarrior.m_PlayerID, dInfo['Perform'], oPerform.m_ID, 0, dArgs)


def CustomAction3606(oWarrior, oEventCB, dInfo):
    if oWarrior.m_SID != INKMASTER_HERO:
        return None
    oPerform = oEventCB.GetObject()
    if not oPerform:
        return None
    if 'Clear' in dInfo:
        oPerform.SetArgValue('RemainFrame', { })
        return None
    oInkCon = oWarrior.m_InkCon
    dInkAreaInfo = oInkCon.GetInInkAreaInfoByType(oWarrior.m_FightType)
    if oWarrior.m_ID not in dInkAreaInfo or not dInkAreaInfo[oWarrior.m_ID]:
        return None
    dRemainFrame = oPerform.GetArgValue('RemainFrame', { })
    iProlongFrame = dInfo['ProlongFrame']
    for iEvent in dInkAreaInfo[oWarrior.m_ID]:
        oOwner = oWarrior.m_Game.GetObject(iEvent)
        if not oOwner:
            continue
        if oOwner.m_FightType == NWARRIOR_VIRTUAL_DYNCEVENT:
            iProlongFrame = GetRealProlongFrame(oWarrior, oEventCB, dRemainFrame, iProlongFrame, iEvent, dInfo['HeroTypeMaxProlong'])
            if iProlongFrame:
                dRemainFrame[iEvent] += iProlongFrame
                oInkCon.DelayCallBack(iEvent, iProlongFrame)
                ProlongHeroEffect(oWarrior, dInfo, iProlongFrame)
                continue
        if oOwner.m_FightType & WARRIOR_MONSTER:
            lstState = oOwner.m_State.GetItems(INKAREA_MONSTER_STATE)
            for oState in lstState:
                if oState.m_Attacker != oWarrior.m_ID:
                    continue
                iProlongFrame = GetRealProlongFrame(oWarrior, oEventCB, dRemainFrame, iProlongFrame, oState.m_ID, dInfo['MonsterTypeMaxProlong'])
                if iProlongFrame:
                    dRemainFrame[oState.m_ID] += iProlongFrame
                    cl_state.AddTime(oState, oOwner, iProlongFrame, oState.GetTime())
                    ProlongHeroEffect(oWarrior, dInfo, iProlongFrame)
            
    
    oPerform.SetArgValue('RemainFrame', dRemainFrame)


def GetRealProlongFrame(oWarrior, oEventCB, dRemainFrame, iProlongFrame, iTarget, iMaxProlongFrame):
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iMaxProlongFrame = cl_formula.GetResultByData(oWarrior, iMaxProlongFrame, dEventInfo, dMsgInfo)
    if iTarget not in dRemainFrame:
        dRemainFrame[iTarget] = 0
    if dRemainFrame[iTarget] >= iMaxProlongFrame:
        return 0
    iProlongFrame = min(iProlongFrame, iMaxProlongFrame - dRemainFrame[iTarget])
    return iProlongFrame


def ProlongHeroEffect(oWarrior, dInfo, iProlongFrame):
    oState = oWarrior.m_State.GetItemBySID(INKAREA_HERO_STATE)
    if oState and oState.m_TimeType == STATE_TIME_LIMIT:
        cl_state.AddTime(oState, oWarrior, iProlongFrame, oState.GetTime())


def CustomAction3607(oWarrior, oEventCB, dInfo):
    iState = dInfo['StateSID']
    oPerform = oEventCB.GetObject()
    if not oPerform:
        return None
    lstRecord = oPerform.GetArgValue('Record', [])
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'MonsterDie' in dInfo:
        if 'VID' not in dMsgInfo:
            return None
        iVictim = dMsgInfo['VID']
        if iVictim in lstRecord:
            lstRecord.remove(iVictim)
        else:
            return None
        iCurVictim = GetNearVictim(oWarrior, iVictim, dInfo['CheckDis'])
    elif 'CurVID' not in dMsgInfo:
        return None
    iCurVictim = dMsgInfo['CurVID']
    if iCurVictim in lstRecord:
        return None
    if len(lstRecord) >= dInfo['Max']:
        iRemoveVictim = lstRecord.pop(0)
        oRemoveVictim = oWarrior.m_Game.GetObject(iRemoveVictim)
        if oRemoveVictim:
            oRemoveVictim.m_State.RemoveItemBySource(iState, oWarrior.m_ID)
    if not iCurVictim:
        return None
    lstRecord.append(iCurVictim)
    oPerform.SetArgValue('Record', lstRecord)
    dTransInfo = oEventCB.GetCBTransInfo()
    dTransInfo['TargetList'] = [
        iCurVictim]
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, iState, 0, {
        'Buff': dInfo['Buff'] }, 1, 1)


def GetNearVictim(oWarrior, iVictim, fCheckDis):
    oGame = oWarrior.m_Game
    oVictim = oGame.GetObject(iVictim)
    if not oVictim:
        return 0
    iScene = oVictim.m_Scene
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return 0
    lstMonster = oScene.GetObjectsByType('Monster')
    dTarget = { }
    for iTarget in lstMonster:
        if iTarget == iVictim:
            continue
        oCurTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oCurTarget:
            continue
        dTarget[iTarget] = 1
    
    dDis = oGame.Scene_GetTargetDisMap(iVictim, list(dTarget), 1)
    iNearVictim = 0
    if dDis:
        iChooseVictim = min(dDis, key = dDis.get)
        if dDis[iChooseVictim] <= fCheckDis:
            iNearVictim = iChooseVictim
    return iNearVictim


def CustomAction3610(oWarrior, oEventCB, dInfo):
    
    def ClearFunc(oWarrior, oLifeCycle):
        lstAreaInfo = [
            (SPHERE_INKAREA, dInfo['1918_DefaultRadius']),
            (DOUBLESPHERE_INKAREA, dInfo['1921_DefaultRadius'])]
        for iAreaType, iDefaultRadius in lstAreaInfo:
            dRecord = oInkCon.GetInkAreaRecord(iAreaType, oWarrior.m_ID)
            if dRecord:
                dInfo['OuterRadius'] = iDefaultRadius
                UpdateSphereInkArea(oWarrior, oInkCon, dInfo, dRecord, dData, iAreaType)
        

    if oWarrior.m_SID != INKMASTER_HERO:
        return None
    oLifeCycle = oEventCB.GetCBLifeCycle()
    dData = {
        'LifeCycle': oLifeCycle }
    if 'InnerRadius' not in dInfo:
        iAreaType = SPHERE_INKAREA
    else:
        iAreaType = DOUBLESPHERE_INKAREA
    oInkCon = oWarrior.m_InkCon
    dRecord = oInkCon.GetInkAreaRecord(iAreaType, oWarrior.m_ID)
    if dRecord:
        UpdateSphereInkArea(oWarrior, oInkCon, dInfo, dRecord, dData, iAreaType)
    oLifeCycle.AddUniqueDisableFunc(oEventCB.Key(), ClearFunc, iCover = 0)


def UpdateSphereInkArea(oWarrior, oInkCon, dInfo, dRecord, dData, iAreaType):
    oManagerState = oWarrior.m_State.GetItemBySID(INKAREA_MANAGER_STATE)
    if not oManagerState:
        return None
    dInfo['LifeCycle'] = dRecord['LifeCycle']
    dInfo['RSPerform'] = dRecord['RSPerform']
    oInkCon.DumpInkAreaRecord(iAreaType, oWarrior.m_ID)
    bValid = oInkCon.ValidDisplayArea()
    if iAreaType == SPHERE_INKAREA:
        oInkCon.ClearSphereInkAreaEvent(HERO_SPHERE_AREAEVENT)
        fRadius = cl_formula.GetResultByData(oWarrior, dInfo['OuterRadius'], dData)
        oAttachEvent = oInkCon.CreateSphereInkArea(oWarrior, fRadius, dInfo)
        if not bValid or not oManagerState.GetCount():
            oAttachEvent.Disable()
        else:
            oInkCon.ClearSphereInkAreaEvent(HERO_INNERSPHERE_AREAEVENT)
            oInkCon.ClearSphereInkAreaEvent(HERO_OUTERSPHERE_AREAEVENT)
            fOuterRadius = cl_formula.GetResultByData(oWarrior, dInfo['OuterRadius'], dData)
            fInnerRadius = cl_formula.GetResultByData(oWarrior, dInfo['InnerRadius'], dData)
            (oOuterAttachEvent, oInnerAttachEvent) = oInkCon.CreateDoubleSphereInkArea(oWarrior, fOuterRadius, fInnerRadius, dInfo)
            if not bValid or oManagerState.GetCount():
                oOuterAttachEvent.Disable()
                oInnerAttachEvent.Disable()


def CustomAction3611(oWarrior, oEventCB, dInfo):
    oPerform = oEventCB.GetObject()
    if not oPerform:
        return None
    iSpecialCreate = oPerform.GetArgValue('SpecialCreate', 0)
    if iSpecialCreate <= 0:
        return None
    if oWarrior.m_SID != INKMASTER_HERO:
        return None
    oInkCon = oWarrior.m_InkCon
    iNeedNum = oInkCon.GetInkBeadNum()
    oPerform.AddArgValue('InkBeadCount', 1)
    iInkBeadCount = oPerform.GetArgValue('InkBeadCount', 0)
    if iInkBeadCount >= iNeedNum:
        oPerform.SetArgValue('InkBeadCount', 0)
    else:
        iProb = round(1 / iNeedNum, 2) * 100
        if oWarrior.m_Game.Random(100) + 1 > iProb:
            return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'DropInfo' not in dMsgInfo:
        return None
    oPerform.AddArgValue('SpecialCreate', -1)
    if not oPerform.GetArgValue('SpecialCreate', 0):
        oPerform.SetArgValue('InkBeadCount', 0)
    dDropInfo = dict(dMsgInfo['DropInfo'])
    dSpecialInfo = {
        'InkBeadType': PICK_SPECIALINKBEAD,
        'SID': SPECIALINKBEAD_SID }
    dDropInfo.update(dSpecialInfo)
    dMsgInfo['DropInfo'] = dDropInfo


def CustomAction3612(oWarrior, oEventCB, dInfo):
    if oWarrior.m_SID != INKMASTER_HERO:
        return None
    oInkCon = oWarrior.m_InkCon
    if 'Clear' in dInfo:
        for iAreaType in (SPHERE_INKAREA, DOUBLESPHERE_INKAREA):
            oInkCon.DumpInkAreaRecord(iAreaType, oWarrior.m_ID)
        
        for iAreaEventType in (HERO_SPHERE_AREAEVENT, HERO_INNERSPHERE_AREAEVENT, HERO_OUTERSPHERE_AREAEVENT):
            oInkCon.ClearSphereInkAreaEvent(iAreaEventType)
        
    else:
        oPerform = oEventCB.GetObject()
        if not oPerform:
            return None
        oManagerState = oWarrior.m_State.GetItemBySID(INKAREA_MANAGER_STATE)
        if not oManagerState:
            return None
        oLifeCycle = oEventCB.GetCBLifeCycle()
        dData = {
            'LifeCycle': oLifeCycle }
        dInfo['LifeCycle'] = oLifeCycle
        dInfo['RSPerform'] = oPerform.m_SID
        bValid = oInkCon.ValidDisplayArea()
        fRadius = cl_formula.GetResultByData(oWarrior, dInfo['1918_Radius'], dData)
        oAttachEvent = oInkCon.CreateSphereInkArea(oWarrior, fRadius, dInfo)
        if not bValid or not oManagerState.GetCount():
            oAttachEvent.Disable()
        fOuterRadius = cl_formula.GetResultByData(oWarrior, dInfo['1921_OuterRadius'], dData)
        fInnerRadius = cl_formula.GetResultByData(oWarrior, dInfo['1921_InnerRadius'], dData)
        (oOuterAttachEvent, oInnerAttachEvent) = oInkCon.CreateDoubleSphereInkArea(oWarrior, fOuterRadius, fInnerRadius, dInfo)
        if not bValid or oManagerState.GetCount():
            oOuterAttachEvent.Disable()
            oInnerAttachEvent.Disable()


def CustomAction3617(oWarrior, oEventCB, dInfo):
    
    def ClearFunc(oWarrior, oLifeCycle):
        oPerform = oWarrior.GetPerform(iPerform)
        if not oPerform:
            return None
        for iEventID in list(dPathInfo):
            DelayDumpFunc(iEventID)
            oInkCon.ClearTargetCallOut(iEventID)
        
        LeaveCurArea(oInkCon, oWarrior, oPerform, dInfo)

    
    def DelayDumpFunc(iEventID):
        oPerform = oWarrior.GetPerform(iPerform)
        if not oPerform:
            return None
        dPathInfo.pop(iEventID, None)
        oPerform.SetArgValue('PathInfo', dPathInfo)
        oInkCon.DumpInkAreaRecord(RECTANGLE_INKAREA, iEventID)

    if oWarrior.m_SID != INKMASTER_HERO:
        return None
    oPerform = oEventCB.GetObject()
    if not oPerform:
        return None
    iPerform = oPerform.m_SID
    vCurPos = oWarrior.GetPos()
    vCurDir = oWarrior.GetFacing()
    oInkCon = oWarrior.m_InkCon
    dPathInfo = oPerform.GetArgValue('PathInfo', { })
    iLastEventID = 0
    if dPathInfo:
        iLastEventID = list(dPathInfo)[-1]
        vLastPos = dPathInfo[iLastEventID]
        if 'Clear' not in dInfo and cl_math.CheckDistance(vCurPos, vLastPos, dInfo['CheckMin']):
            oInkCon.DelayCallBack(iLastEventID, dInfo['ProLongFrame'])
            return None
        fLength = cl_math.CalDistance3D(vCurPos, vLastPos)
        vDir = cl_math.Vec3Minus(vCurPos, vLastPos)
        vCenter = cl_math.Vec3DisplaceDir(vLastPos, vDir, fLength)
        fHalfHorizontalLength = cl_math.CalDistance(vCurPos, vLastPos) / 2
    else:
        vCenter = vCurPos
        vDir = vCurDir
        fHalfHorizontalLength = dInfo['HalfZ']
    oLifeCycle = oEventCB.GetCBLifeCycle()
    if 'Clear' in dInfo:
        LeaveCurArea(oInkCon, oWarrior, oPerform, dInfo)
        oPerform.SetArgValue('CurEvent', 0)
        oPerform.SetArgValue('PathInfo', { })
        dExtInfo = {
            'Pos': vCenter,
            'HalfZ': fHalfHorizontalLength if fHalfHorizontalLength else dInfo['HalfZ'],
            'Dir': (vDir[0], 0, vDir[2]),
            'Key': oEventCB.Key(),
            'RSPerform': oPerform.m_SID,
            'LifeCycle': oLifeCycle }
        dInfo.update(dExtInfo)
        oInkCon.CreateRectangleInkArea(oWarrior, dInfo)
        return None
    iEventID = oWarrior.m_Game.NewNoSceneObjID()
    dRecord = {
        'RSPerform': oPerform.m_SID,
        'Pos': vCenter,
        'Range': (round(dInfo['HalfX']), round(fHalfHorizontalLength)),
        'Dir': (vDir[0], 0, vDir[2]) }
    oInkCon.AddInkAreaRecord(RECTANGLE_INKAREA, iEventID, dRecord)
    oInkCon.Call_Out(iEventID, dInfo['DelayFrame'], Functor(DelayDumpFunc, iEventID))
    dPathInfo[iEventID] = vCurPos
    oPerform.SetArgValue('PathInfo', dPathInfo)
    if oInkCon.ValidTrigger(oWarrior):
        LeaveCurArea(oInkCon, oWarrior, oPerform, dInfo)
        dInfo['EventID'] = iEventID
        oInkCon.EffectInkArea(oWarrior, dInfo, iLeave = 0)
        oPerform.SetArgValue('CurEvent', iEventID)
    oLifeCycle.AddUniqueDisableFunc(oEventCB.Key(), ClearFunc, iCover = 0)


def LeaveCurArea(oInkCon, oWarrior, oPerform, dInfo):
    iCurEventID = oPerform.GetArgValue('CurEvent', 0)
    if iCurEventID and oInkCon.ValidTrigger(oWarrior):
        dInfo['EventID'] = iCurEventID
        oInkCon.EffectInkArea(oWarrior, dInfo, iLeave = 1)


def CustomActionMarkHitTarget(oWarrior, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'CurVID' not in dMsgInfo:
        return None
    pfobj = oEventCB.GetObject()
    if not pfobj:
        return None
    iVictim = dMsgInfo['CurVID']
    dHitMarkInfo = pfobj.SetArgValueDefault('HitMarkInfo', { })
    iNowFrame = oWarrior.m_Game.GetFrameNum()
    iLimitFrame = Time2Frame(dInfo['DamLimitTime'])
    if iVictim in dHitMarkInfo:
        lstRecordHitInfo = dHitMarkInfo[iVictim]
        lstHitInfo = []
        for iHitFrame in lstRecordHitInfo:
            if iHitFrame + iLimitFrame >= iNowFrame:
                lstHitInfo.append(iHitFrame)
        
        lstHitInfo.append(iNowFrame)
        iHitCount = len(lstHitInfo)
        if iHitCount >= dInfo['RewardMarkCount']:
            dHitMarkInfo[iVictim] = []
            if not pfobj.CheckLiteCD():
                pfobj.SetLiteCD(dInfo['CodeTime'])
                oWarrior.EnergyModify(dInfo['RecoverEnergy'])
            return None
        dHitMarkInfo[iVictim] = lstHitInfo
    else:
        dHitMarkInfo[iVictim] = [
            iNowFrame]


def CustomAction3709(oWarrior, oLifeCycle, dInfo):
    
    def ClearFunc(oWarrior, oLifeCycle):
        oPerform = oWarrior.GetPerform(dInfo['Perform'])
        if not oPerform:
            return None
        oPerform.Disable(oWarrior, iNotify = 1)

    oState = oWarrior.m_State.GetItemBySID(BIG_LION_STATE)
    if not oState:
        return None
    oPerform = oWarrior.GetPerform(dInfo['Perform'])
    if not oPerform:
        return None
    oPerform.Enable(oWarrior, iNotify = 1)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CustomAction3816_Hit(oWarrior, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'CurVID' not in dMsgInfo:
        return None
    iVictim = dMsgInfo['CurVID']
    iState = dInfo['State']
    oState = oWarrior.m_State.GetItemBySID(iState)
    if not oState:
        return None
    dHitInfo = oState.SetArgValueDefault('HitInfo', { })
    iNowFrame = oWarrior.m_Game.GetFrameNum()
    iDeceleration = -1 * cl_formula.GetResultByData(oWarrior, dInfo['Deceleration'], oEventCB.GetCBEventInfo(), dMsgInfo)
    iCDFrame = iNowFrame + dInfo['Frame']
    if iVictim not in dHitInfo:
        if not iDeceleration:
            return None
        dHitInfo[iVictim] = (iDeceleration, iCDFrame)
        oState.AddArgValue('Deceleration', iDeceleration)
        oState.m_LifeCycle.CallFunc('Refresh', oWarrior)
        if not oWarrior.Find_Call_Out('CustomAction3816_UpdateTimer'):
            UpdateTimer(oWarrior, iState)
        return None
    (iOldCount, _) = dHitInfo[iVictim]
    if not iDeceleration:
        dHitInfo.pop(iVictim)
        oState.AddArgValue('Deceleration', -iOldCount)
        oState.m_LifeCycle.CallFunc('Refresh', oWarrior)
        return None
    if iOldCount != iDeceleration:
        oState.AddArgValue('Deceleration', -iOldCount + iDeceleration)
        oState.m_LifeCycle.CallFunc('Refresh', oWarrior)
    dHitInfo[iVictim] = (iDeceleration, iCDFrame)


def UpdateTimer(oWarrior, iState):
    oState = oWarrior.m_State.GetItemBySID(iState)
    if not oState:
        return None
    dHitInfo = oState.GetArgValue('HitInfo', { })
    sTimeKey = 'CustomAction3716_UpdateTimer'
    if not dHitInfo:
        oWarrior.Remove_Call_Out(sTimeKey)
        return None
    iHit = min(dHitInfo, key = (lambda x: dHitInfo[x][1]))
    (_, iNewMinCDFrame) = dHitInfo[iHit]
    if not oWarrior.Find_Call_Out(sTimeKey):
        oWarrior.Call_Out(Functor(CustomAction3816_Update, oWarrior, iState), iNewMinCDFrame - oWarrior.m_Game.GetFrameNum(), sTimeKey)


def CustomAction3816_Update(oWarrior, iState):
    oState = oWarrior.m_State.GetItemBySID(iState)
    if not oState:
        return None
    dHitInfo = oState.GetArgValue('HitInfo', { })
    if not dHitInfo:
        return None
    iFrame = oWarrior.m_Game.GetFrameNum()
    iAllDeceleration = 0
    dPopHit = { }
    for iHit, (iDeceleration, iCDFrame) in dHitInfo.items():
        if iCDFrame != iFrame:
            continue
        iAllDeceleration += iDeceleration
        dPopHit[iHit] = 1
    
    for iHit in dPopHit:
        dHitInfo.pop(iHit)
    
    if iAllDeceleration:
        oState.AddArgValue('Deceleration', -iAllDeceleration)
        oState.m_LifeCycle.CallFunc('Refresh', oWarrior)
    UpdateTimer(oWarrior, iState)


def CustomAction3816_End(oWarrior, oLifeCycle, dInfo):
    oWarrior.Remove_Call_Out('CustomAction3816_UpdateTimer')

