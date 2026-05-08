# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/custom/state/customaction.pyc
# RelativePath: clientlogic/cl_platformdata/custom/state/customaction.pyc
# Source Generated with Decompyle++
# File: customaction.pyc (Python 3.6)

from cl_cscommondef import OBJ_SELF, MAIN_HOLD, DAM_TYPE_WEAKNESS
from cl_only import SendAlert, Frame2Time, Time2Frame, PY_FLAG_DEAD, OutputPos, PY_FLAG_DIED, DeepCopy
from cl_commondefines import WARRIOR_ELITE, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_ALL, WARRIOR_NORMAL, WARRIOR_BOSS, THUNDERSTEP_CONDUCT_DAMAGE, MODEL_TYPE_SPHERE, WARRIOR_MONSTER, STATE_TIME_FOREVER
from cl_commondefines import REASON_HITFLAW, UNBALANCE_WEAPON, UNBALANCE_OTHER, INKMASTER_HERO, TOXIC_FOG, TOXIC_DAM, DAM_USE_ARMOR, VIRTUAL_ITEM_GOLDENCUP, FAKEMG_GOLDENCUP, NWARRIOR_DROP_DEMON
from cl_commondefines import STATE_TIME_LIMIT, BLOCK_BY_SERVANT, WARRIOR_HERO, CURE_TYPE_PERFORM, DAM_USE_HP, DEFEND_TREND_NONE, DEFEND_TREND_SHIELD, DEFEND_TREND_ARMOR, DAM_USE_SHIELD, NWARRIOR_NPC_PASSBOX
from cl_commondefines import DAM_TYPE_WEAPON, OBJ_ATTACK, OBJ_VICTIM, OBJ_ENEMY, DAM_TYPE_NORMAL, HERO_CHASED_STATE, WANDABILITY_ADDEXTCONCOMP, WANDABILITY_ADDEXTACTCOMP, DAM_TYPE_FIRE, PAIR_WAND, WAND_COMP_TYPE_CONDITION
from cl_commondefines import FIGHT3_KEY_EVACT_IGNELECORRISION, STATE_PAINFULREVERSE, DISABLE_TYPE_STATE, ABNORMAL_DEFAULT, MAX_SPEEDEFFECTBY_CORRISION_ABNORMAL, ATT_SHAPE_SPHERE
from cl_object.logging import RelictalentLog, TaskLog, WarobjLog
from cl_object.reason import REASON_TYPE_PERFORM
from cl_pxlayer import PXLAYER_TRIDSTEVENT, PXMASK_MONSTER
from cl_only import Functor, CopyDict
from cl_platformdata.custom.seasonpassive.customaction import AddFogPoisonState
import cl_gamedebug as debug
import cl_snetwar
import cl_math
import cl_action
import cl_state
import cl_formula
import cl_evact
import cl_object.reason
import cl_object
import cl_msgcenter
import cl_engphyobj
import cl_condition
import cl_war
import cl_evcon

def CustomAction1554(oTarget, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Relic' in dMsgInfo:
        return dMsgInfo['Relic']
    return 0


def CustomAction8076(oTarget, oLifeCycle, dInfo):
    if 'Init' in dInfo:
        oTarget.Set('Frame8076', oTarget.m_Game.GetFrameNum())
    elif 'Time' in dInfo:
        iEnergy = oTarget.Query('Energy8076', 0)
        if iEnergy:
            oTarget.EnergyModify(iEnergy)
            return None
        oTarget.Set('Frame8076', oTarget.m_Game.GetFrameNum())
    elif 'Reserve' in dInfo:
        iFrameNum = oTarget.Query('Frame8076', 0)
        if not iFrameNum:
            return None
        iFrame = oTarget.m_Game.GetFrameNum() - iFrameNum
        oTarget.Set('Energy8076', iFrame * dInfo['Reserve'])


def CustomAction32587(oWarrior, oEventCB, dInfo):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    iCount = 0
    for iTarget in dTransInfo['TargetList']:
        oTarget = oWarrior.m_Game.GetObject(iTarget)
        if not oTarget:
            continue
        if oTarget.m_FightType & WARRIOR_NORMAL == WARRIOR_NORMAL:
            iCount += dInfo['Normal'] + dInfo['ExAdd']
            continue
        if oTarget.m_FightType & WARRIOR_ELITE == WARRIOR_ELITE:
            iCount += dInfo['Elite'] + dInfo['ExAdd']
            continue
        if oTarget.m_FightType & WARRIOR_BOSS == WARRIOR_BOSS:
            iCount += dInfo['Boss'] + dInfo['ExAdd']
    
    return iCount


def CustomAction7951(oTarget, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'AID' not in dMsgInfo:
        return None
    oTarget.Set('Rewarder', dMsgInfo['AID'])


def CustomAction8098(oTarget, oLifeCycle, dInfo):
    iScene = oTarget.m_Scene
    oGame = oTarget.m_Game
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return None
    iAttractSID = dInfo['AttractSID']
    if dInfo['Operate'] == 'Add':
        fMaxDis = dInfo['MaxDis']
        oTargetPos = oTarget.GetPos()
        oState = oLifeCycle.GetObject()
        iRemainTime = oState.GetRemainTime()
        iNoAttractSID = dInfo['NoAttractSID']
        for iHero in oScene.GetHeros():
            oHero = oGame.GetObject(iHero)
            if not oHero or oHero.IsDead():
                continue
            if not cl_math.CheckDistance3D(oTargetPos, oHero.GetPos(), fMaxDis):
                continue
            if oHero.m_State.GetItemBySID(iNoAttractSID):
                continue
            cl_action.StateAddState(oHero, oLifeCycle, iAttractSID, Frame2Time(iRemainTime), { })
        
    elif dInfo['Operate'] == 'Remove':
        for iHero in oScene.GetHeros():
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            oHero.m_State.RemoveAllItemBySID(iAttractSID)
        
    elif dInfo['Operate'] == 'AddStateTime':
        iTime = Time2Frame(dInfo['Time']) if 'Time' in dInfo else 0
        iMaxTime = Time2Frame(dInfo['MaxTime']) if 'MaxTime' in dInfo else 0
        oOwnState = oLifeCycle.GetObject()
        if oOwnState:
            cl_state.AddTime(oOwnState, oTarget, iTime, iMaxTime)
        for iHero in oScene.GetHeros():
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            oTargetState = oHero.m_State.GetItemBySID(iAttractSID)
            if not oTargetState:
                continue
            cl_state.AddTime(oTargetState, oHero, iTime, iMaxTime)
        


def CustomAction7023(oTarget, oEventCB, dInfo):
    dTransInfo = oEventCB.GetCBTransInfo()
    lstTar = []
    oGame = oTarget.m_Game
    lstMonsterID = oTarget.Query('AffiliateMonster', [])
    for iMonster in lstMonsterID:
        oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
        if not oMonster:
            continue
        lstTar.append(iMonster)
    
    dTransInfo['TargetList'] = lstTar


def CustomAction8100(oTarget, oLifeCycle, dInfo):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    oGame = oTarget.m_Game
    iScene = oTarget.m_Scene
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return None
    vFirstSealWallPos = oTarget.Query('FirstSealWallPos')
    if not vFirstSealWallPos:
        return None
    lstSealWallID = oTarget.Query('SealWallID')
    if not lstSealWallID:
        return None
    vCenterPos = oTarget.GetPos()
    lstVertices = []
    lstVertices.append(vCenterPos)
    lstFace = []
    iOffsetAngle = 25
    iFlag = -1
    for idx, iSealWall in enumerate(lstSealWallID):
        oSealWall = oGame.GetObject(iSealWall)
        if not oSealWall:
            return None
        vFinalPos = oSealWall.Query('CircumPathFinalPos')
        if not vFinalPos:
            return None
        vSealWallPos = oSealWall.GetPos()
        if not cl_math.CheckDistance(vFinalPos, vSealWallPos, 1):
            return None
        vFace = cl_math.Vec3Minus(vSealWallPos, vCenterPos)
        lstFace.append(vFace)
        vOffsetFace = cl_math.RotateAroundVector(vFace, (0, 1, 0), iFlag * iOffsetAngle)
        lstVertices.append(cl_math.Vec3DisplaceDir(vCenterPos, vOffsetFace, 70))
        if idx == 0:
            lstVertices.append(cl_math.Vec3DisplacePos(vCenterPos, vFirstSealWallPos, 90))
        iFlag = -iFlag
    
    dTransferInfo = oState.m_Data.setdefault('SealWallTransfer', { })
    iTransferMax = dInfo['TransferMax'] if 'TransferMax' in dInfo else 3
    for iHero in oScene.GetHeros():
        oHero = oGame.GetObject(iHero)
        if not oHero:
            continue
        if oHero.m_Servant:
            oServant = oGame.GetObject(oHero.m_Servant, PY_FLAG_DIED)
            if oServant:
                vPos = oServant.GetPos()
                if cl_math.PNPoly(lstVertices, (vPos[0], vPos[2])):
                    TransferServant(oTarget, oServant, lstFace, oLifeCycle.m_Key)
        if oHero.IsDeadNoDying():
            continue
        pid = oHero.m_PlayerID
        iCnt = dTransferInfo.setdefault(pid, 0)
        if iCnt >= iTransferMax:
            continue
        vPos = oHero.GetPos()
        if cl_math.PNPoly(lstVertices, (vPos[0], vPos[2])):
            TransferHero(oTarget, oHero, lstFace, lstVertices[1:])
            iCnt += 1
            dTransferInfo[pid] = iCnt
    


def TransferHero(oMonster, oHero, lstFace, lstVertices):
    vCenterPos = oMonster.GetPos()
    iAngle = cl_math.CalAngle2D(lstFace[0], lstFace[1])
    iOffsetAngle = iAngle // 2
    fDis = 45
    vTransferFace = cl_math.RotateAroundVector(lstFace[0], (0, 1, 0), iOffsetAngle)
    vTransferPos = cl_math.Vec3DisplaceDir(vCenterPos, vTransferFace, fDis)
    sText = 'gameid:%d %d %s transfer %s vertices:' % (oHero.m_Game.m_ID, oHero.m_PlayerID, OutputPos(oHero.GetPos()), OutputPos(vTransferPos))
    for vPos in lstVertices:
        sText += OutputPos(vPos)
    
    WarobjLog.Debug(sText)
    oHero.Stop()
    oHero.WalkTo(vTransferPos)


def TransferServant(oMonster, oServant, lstFace, sReason):
    vCenterPos = oMonster.GetPos()
    iAngle = cl_math.CalAngle2D(lstFace[0], lstFace[1])
    iOffsetAngle = iAngle // 2
    fDis = 45
    vTransferFace = cl_math.RotateAroundVector(lstFace[0], (0, 1, 0), iOffsetAngle)
    vTransferPos = cl_math.Vec3DisplaceDir(vCenterPos, vTransferFace, fDis)
    oServant.Stop()
    oServant.WalkTo(vTransferPos, sReason)


def CustomAction32101(oTarget, oLifeCycle, dInfo):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    if 'ImmobilizeFrame' not in oState.m_Data:
        return None
    oGame = oTarget.m_Game
    oAttack = oGame.GetObject(oState.m_StateInfo['AID'])
    if not oAttack:
        return None
    iVID = oTarget.m_ID
    sKey = 'st32101-%d' % iVID
    iCurFrame = oGame.GetFrameNum()
    iLastFrame = iCurFrame - max(oState.m_Data['ImmobilizeFrame'], oAttack.Query(sKey, 0))
    oAttack.Set(sKey, iCurFrame)
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, oAttack, {
        'StateSID': oState.m_SID,
        'LastFrame': iLastFrame,
        'VID': oTarget.m_ID,
        'CreateFrame': oState.m_CreateFrame })


def CustomAction32763(oTarget, oLifeCycle, dInfo):
    iProb = cl_formula.GetResultByData(oTarget, dInfo['Prob'], {
        'LifeCycle': oLifeCycle })
    oTarget.m_GamblerCon.SetProb(iProb)


def CustomAction32850(oTarget, oLifeCycle, dInfo):
    oReason = cl_object.reason.CStrReason('AtiveExplosion')
    oTarget.HPDirectModify('HP', 0, -oTarget.HP(), oReason)


def CustomAction33013(oTarget, oLifeCycle, dInfo):
    iPerform = dInfo['Perform']
    oPerform = oTarget.GetPerform(iPerform)
    if not oPerform:
        return None
    dTrans = oLifeCycle.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oLifeCycle.m_Key)
        return None
    lstTar = dTrans['TargetList']
    if not lstTar:
        return None
    iEnemy = lstTar[0]
    oEnemy = oTarget.m_Game.GetObject(iEnemy, PY_FLAG_DEAD)
    if not oEnemy:
        return None
    tEnemyPos = oEnemy.GetPos()
    oPerform.AddTemporaryCount()
    iPosX = int(tEnemyPos[0] * 100)
    iPosY = int(tEnemyPos[1] * 100)
    iPosZ = int(tEnemyPos[2] * 100)
    dTrueArgs = {
        'IsServer': 1,
        'PosX': iPosX,
        'PosY': iPosY,
        'PosZ': iPosZ,
        'EnemytSID': iEnemy }
    cl_snetwar.GS2CNotifyStartSkill(oTarget.m_Game, oTarget.m_PlayerID, iPerform, oPerform.m_ID, 0, dTrueArgs)


def CustomAction33027(oTarget, oEventCB, dInfo):
    oOwnState = oEventCB.GetObject()
    if not oOwnState:
        return None
    oGame = oTarget.m_Game
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iSourcePF = 0
    if 'RS' in dMsgInfo:
        oReason = dMsgInfo['RS']
        if oReason.m_Type == REASON_TYPE_PERFORM:
            iSourcePF = oReason.m_Perform
    iCheckCD = 1
    if 'ThunderPlusPF' in dInfo and iSourcePF == dInfo['ThunderPlusPF']:
        iCheckCD = 0
    iMergeGroup = 0
    if 'MergePF' in dInfo:
        for idx, lstMergePF in enumerate(dInfo['MergePF']):
            if iSourcePF in lstMergePF:
                iMergeGroup = idx + 1
                break
        
    if iCheckCD:
        sCDKey = '33027CD'
        sMergeKey = f'''33027Group{iMergeGroup}'''
        iCurFrame = oGame.GetFrameNum()
        iStartFrame = oOwnState.GetArgValue(sCDKey, 0)
        if iCurFrame < iStartFrame:
            if iMergeGroup:
                dMergeCDGroup = oOwnState.GetArgValue(sMergeKey, { })
                if iSourcePF in dMergeCDGroup:
                    return None
            return None
    if 'TotalDam' not in dMsgInfo:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iOwner = oTarget.m_ID
    iShareCount = dInfo['ShareCount']
    iDistance = dInfo['Distance']
    iScene = oTarget.m_Scene
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    lstMonster = oScene.GetObjectsByType('Monster')
    if iOwner in lstMonster:
        lstMonster.remove(iOwner)
    if lstMonster:
        lstTarMonster = []
        iShareCount = cl_formula.GetResultByData(oTarget, iShareCount, dEventInfo, dMsgInfo)
        dDis = oGame.Scene_GetTargetDisMap(iOwner, lstMonster)
        iCurMinTarget = min(dDis, key = dDis.get)
        if dDis[iCurMinTarget] <= iDistance:
            lstTarMonster = [
                iCurMinTarget]
        else:
            return None
        if iShareCount > 1:
            for _ in range(iShareCount - 1):
                dDis.pop(iCurMinTarget)
                if not dDis:
                    break
                iCurMinTarget = min(dDis, key = dDis.get)
                if dDis[iCurMinTarget] <= iDistance:
                    lstTarMonster.append(iCurMinTarget)
                    continue
            
        else:
            return None
    dTransInfo = oEventCB.GetCBTransInfo()
    dTransInfo['TargetList'] = lstTarMonster
    if iCheckCD:
        iCDFrame = iCurFrame + dInfo['CD']
        if iMergeGroup:
            dMergeCDGroup = oOwnState.GetArgValue(sMergeKey, { })
            if not dMergeCDGroup or iSourcePF in dMergeCDGroup:
                dMergeCDGroup = {
                    iSourcePF: 1 }
                dCDInfo = {
                    sMergeKey: dMergeCDGroup,
                    sCDKey: iCDFrame }
                oOwnState.UpdateArgValue(dCDInfo)
            else:
                dMergeCDGroup[iSourcePF] = 1
        else:
            dCDInfo = {
                sCDKey: iCDFrame }
            oOwnState.UpdateArgValue(dCDInfo)
    iShareDamageRatio = cl_formula.GetResultByData(oTarget, dInfo['ShareDamageRatio'], dEventInfo, dMsgInfo)
    cl_evact.EventTargetDamage(oTarget, oEventCB, sum(dMsgInfo['TotalDam']) * iShareDamageRatio // 100, DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 0, 0, 0, 0, 0, 0, 0, THUNDERSTEP_CONDUCT_DAMAGE)


def CustomActionThunderByDurativeSkill(oTarget, oEventCB, dInfo):
    iStateSID = dInfo['ThunderStateID']
    oStateCon = oTarget.m_State
    oState = oStateCon.GetItemBySID(iStateSID)
    if not oState:
        return None
    if 'ThunderPlus' not in oState.m_Data:
        oState.m_Data['ThunderPlus'] = { }
    dThunderPlus = oState.m_Data['ThunderPlus']
    if 'CareerStart' in dInfo:
        sKey = 'Career'
        iUseThunderCount = dInfo['UseThunderCount']
        dEventInfo = oEventCB.GetCBEventInfo()
        dMsgInfo = oEventCB.GetCBMsgInfo()
        iUseThunderCount = cl_formula.GetResultByData(oTarget, iUseThunderCount, dEventInfo, dMsgInfo)
        oState.AddCount(oTarget, -iUseThunderCount)
        dThunderPlus[sKey] = { }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_THUNDERPLUS, oTarget, { })
    elif 'CareerDam' in dInfo:
        sKey = 'Career'
        if sKey not in dThunderPlus:
            return None
        dTransInfo = oEventCB.GetCBTransInfo()
        if 'TargetList' not in dTransInfo:
            SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
            return None
        if not dTransInfo['TargetList']:
            return None
        iVictim = dTransInfo['TargetList'][0]
        oGame = oTarget.m_Game
        iNowFrame = oGame.GetFrameNum()
        if iVictim in dThunderPlus[sKey]:
            iLastEndFrame = dThunderPlus[sKey][iVictim]
            if iLastEndFrame > iNowFrame:
                return None
        iThunderCDTime = dInfo['ThunderCD']
        iThunderCDFrame = Time2Frame(iThunderCDTime)
        iEndFrame = iNowFrame + iThunderCDFrame
        dThunderPlus[sKey][iVictim] = iEndFrame
        iPerform = dInfo['Perform']
        cl_evact.EventCBUsePerform(oTarget, oEventCB, iPerform)
    elif 'CareerEnd' in dInfo:
        sKey = 'Career'
        dThunderPlus.pop(sKey, None)


def CustomActionThunderByNoDurativeSkill(oTarget, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    iStateSID = dInfo['ThunderStateID']
    oStateCon = oTarget.m_State
    oState = oStateCon.GetItemBySID(iStateSID)
    if not oState:
        return None
    if 'ThunderPlus' not in oState.m_Data:
        oState.m_Data['ThunderPlus'] = { }
    dThunderPlus = oState.m_Data['ThunderPlus']
    oSkill = dMsgInfo['Skill']
    oGame = oTarget.m_Game
    if 'StartSkill' in dInfo:
        if len(dThunderPlus) > 20:
            iNeedRemve = 0
            for iActNum in dThunderPlus:
                iNeedRemve = iActNum
            
            dThunderPlus.pop(iNeedRemve)
        iActnum = oSkill.m_Base['ActNum']
        if iActnum in dThunderPlus:
            RelictalentLog.Alert('%s, 玩家%s存储的强化技能行动编号重复' % (oGame.m_ID, oTarget.m_PlayerID))
        iUseThunderCount = dInfo['UseThunderCount']
        dEventInfo = oEventCB.GetCBEventInfo()
        iUseThunderCount = cl_formula.GetResultByData(oTarget, iUseThunderCount, dEventInfo, dMsgInfo)
        oState.AddCount(oTarget, -iUseThunderCount)
        dThunderPlus[iActnum] = { }
        oSkill.m_Collect['IsThunderPlus'] = 1
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_THUNDERPLUS, oTarget, { })
    elif 'SkillDam' in dInfo:
        if 'IsChildrenSkill' in dInfo:
            iActnum = oSkill.m_CacheData.m_ParentActnum
        else:
            iActnum = oSkill.m_Base['ActNum']
        if iActnum not in dThunderPlus:
            return None
        dTransInfo = oEventCB.GetCBTransInfo()
        if 'TargetList' not in dTransInfo:
            SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
            return None
        if not dTransInfo['TargetList']:
            return None
        iVictim = dTransInfo['TargetList'][0]
        iNowFrame = oGame.GetFrameNum()
        if iVictim in dThunderPlus[iActnum]:
            iLastEndFrame = dThunderPlus[iActnum][iVictim]
            if iLastEndFrame > iNowFrame:
                return None
        iThunderCDTime = dInfo['ThunderCD']
        iThunderCDFrame = Time2Frame(iThunderCDTime)
        iEndFrame = iNowFrame + iThunderCDFrame
        dThunderPlus[iActnum][iVictim] = iEndFrame
        iPerform = dInfo['Perform']
        cl_evact.EventCBUsePerform(oTarget, oEventCB, iPerform)


def CustomAction1882(oTarget, oLifeCycle, dInfo):
    
    def ClearFunc(oTarget, oLifeCycle):
        oAttachEvent.Unstall()

    
    def OnTrigger(obj, iLeave):
        if not obj.m_FightType & WARRIOR_MONSTER:
            return None
        if not iLeave:
            if not obj.m_State.CheckHasStateFrom(iState, iAttack = iAttack, iItem = 0):
                cl_action.StateAddState(obj, oLifeCycle, iState, iTime, {
                    'Att': dInfo['Att'] })
            SetStateStatisticsFromAttacker(obj, oLifeCycle, iAttack, iState, 'OnArea', iValue = 1)
        else:
            SetStateStatisticsFromAttacker(obj, oLifeCycle, iAttack, iState, 'OnArea', iValue = 0)

    oGame = oTarget.m_Game
    fRange = dInfo['Radius']
    iState = dInfo['StateSID']
    iTime = dInfo['StateTime']
    iAttack = oTarget.m_ID
    dShape = {
        'Shape': MODEL_TYPE_SPHERE,
        'Radius': fRange }
    oAttachEvent = cl_engphyobj.CreateAttachEventObject(oGame, oTarget, PXLAYER_TRIDSTEVENT, dShape, OnTrigger)
    oAttachEvent.rigidbody.E_SetKinematic(1)
    oLifeCycle.AddDisableFunc(ClearFunc)


def SetStateStatisticsFromAttacker(oTarget, oLifeCycle, iAttack, iStateSID, sAttr, iValue):
    
    def ClearFunc(oState, sAttr, oTarget, oLifeCycle):
        if not oState:
            return None
        oState.m_Data[sAttr] = 0

    lstState = oTarget.m_State.GetItems(iStateSID)
    if not lstState:
        return None
    for oState in lstState:
        if oState.m_Attacker == iAttack:
            oState.m_Data[sAttr] = iValue
            if iValue > 0:
                if oState.GetCount() < 1:
                    oState.AddCount(oTarget, iCnt = 1)
                oLifeCycle.AddDisableFunc(Functor(ClearFunc, oState, sAttr))
            break
    


def CustomAction1854(oTarget, oLifeCycle, dInfo):
    oState = oLifeCycle.GetObject()
    oAttack = oTarget.m_Game.GetObject(oState.m_StateInfo['AID'])
    if not oAttack or not (oAttack.m_FightType & WARRIOR_HERO):
        return None
    if oState.m_Reason.GetStrReason() == REASON_HITFLAW:
        iSubMsg = UNBALANCE_WEAPON
    else:
        iSubMsg = UNBALANCE_OTHER
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CAUSEUNBALANCE, oAttack, {
        'VID': oTarget.m_ID }, iSub = iSubMsg)


def CustomAction33145(oTarget, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    dInfo['Skill'] = dMsgInfo['Skill']
    oOwner = oTarget.GetOwner()
    if oOwner:
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_BARRIER_BLOCK, oOwner, dInfo, iSub = BLOCK_BY_SERVANT)


def CustomAction33120(oTarget, oLifeCycle, dInfo):
    oState = oLifeCycle.GetObject()
    iAttack = oState.m_Attacker
    oAttack = oState.m_Game.GetObject(iAttack)
    if not oAttack:
        return None
    pfobj = oAttack.GetPerform(TOXIC_DAM)
    if not pfobj:
        return None
    oToxicPerform = oAttack.GetPerform(TOXIC_FOG)
    if not oToxicPerform:
        return None
    iMaxCount = oToxicPerform.CalAttr('CommonMaxCount')
    dCustomData = {
        'ToxicStateSID': oState.m_SID,
        'MaxCount': iMaxCount }
    iVID = oState.m_Owner
    dData = {
        'Custom': dCustomData,
        'VID': iVID }
    cl_war.UsePerform(oAttack, pfobj, dData)


def CustomActionTocixEnd(oTarget, oLifeCycle, dInfo):
    oState = oLifeCycle.GetObject()
    oAttack = oTarget.m_Game.GetObject(oState.m_StateInfo['AID'])
    if not oAttack:
        return None
    oAttack.Add('AllTocixCount', -oState.GetCount())


def CustomAction1461(oTarget, oEventCB, dInfo):
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    oGame = oTarget.m_Game
    oAttack = oGame.GetObject(oState.m_Attacker, PY_FLAG_DEAD)
    if not oAttack:
        return None
    oWeapon = oAttack.m_WieldCon.GetCurWeapon()
    if not oWeapon:
        return None
    iPerform = dInfo['Perform']
    oPerform = cl_action.GetItemPerform(oWeapon, iPerform)
    if not oPerform:
        return None
    dArgs = {
        'Target': oState.m_Owner }
    oPerform.AddCanUseCount()
    cl_snetwar.GS2CNotifyStartSkill(oGame, oAttack.m_PlayerID, iPerform, oPerform.m_ID, oWeapon.m_ID, dArgs)


def CustomAction1896(oTarget, oLifeCycle, dInfo):
    oGame = oTarget.m_Game
    oState = oLifeCycle.GetObject()
    oSkill = oGame.m_SkillMgr.GetSkillBySource(dInfo['Perform'], oState.m_Attacker, oState.m_Item)
    if not oSkill:
        return 0
    sKey = dInfo['Key']
    if sKey not in oSkill.m_Collect:
        return 0
    dRecord = oSkill.m_Collect[sKey]
    if oTarget.m_ID in dRecord:
        return dRecord[oTarget.m_ID]
    return 0


def CustomAction33068(oTarget, oLifeCycle, dInfo):
    if oTarget.m_SID != INKMASTER_HERO:
        return None
    oInkCon = oTarget.m_InkCon
    if oInkCon.CheckAreaIsOpened():
        oInkCon.GeneralAreaByMode(oTarget, bInit = False)


def CustomAction33128(oWarrior, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iTarget = dMsgInfo['VID']
    oTarget = oWarrior.m_Game.GetObject(iTarget, PY_FLAG_DEAD)
    if not oTarget or not (oTarget.m_FightType & WARRIOR_MONSTER):
        return None
    oAgent = oTarget.m_Agent
    if oAgent:
        if iTarget in oAgent.m_SceneData.m_FightMonster:
            return None
        oAgent.SetActCheckVal(oWarrior.m_Owner, 1000, 1000, 1000)


def CustomAction33100(oTarget, oLifeCycle, dInfo):
    if oTarget.m_SID != INKMASTER_HERO:
        return None
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    sKey = oLifeCycle.Key()
    oInkCon = oTarget.m_InkCon
    dInfo['EventID'] = oTarget.m_ID
    dInfo['VirtualArea'] = 1
    if 'CostLevel' in dInfo and 'TriggerCount' in dInfo:
        iTriggerCount = cl_formula.GetResultByData(oTarget, dInfo['TriggerCount'], {
            'LifeCycle': oLifeCycle })
        sKey = f'''CurCount-{sKey}'''
        if cl_condition.CheckSceneFightMonster(oTarget, oLifeCycle):
            if cl_condition.StateCheckInAttackerInkArea(oTarget, oLifeCycle):
                pass
            if not (not cl_condition.GetStateStatistics(oTarget, oLifeCycle, oState.m_SID, 'InVirtual')):
                oState.UpdateArgValue({
                    sKey: oState.GetArgValue(sKey, 0) + 1 })
        if oState.GetArgValue(sKey, 0) >= iTriggerCount:
            oState.UpdateArgValue({
                sKey: 0 })
            cl_action.StateAddSelfCount(oTarget, oLifeCycle, -dInfo['CostLevel'])
        elif 'Enter' in dInfo or oInkCon.ValidTrigger(oTarget):
            oState.m_Data['InVirtual'] = 1
            oInkCon.EffectInkArea(oTarget, dInfo, iLeave = 0)
        elif 'Leave' in dInfo and oInkCon.ValidTrigger(oTarget):
            oState.m_Data['InVirtual'] = 0
            oInkCon.EffectInkArea(oTarget, dInfo, iLeave = 1)


def GetSavedStateCount(oWarrior, oLifeCycle, dInfo):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    sKey = '%d-StateCount-%d' % (dInfo['Pfid'], oState.m_SID)
    iCount = oWarrior.QuerySavedData(sKey, 0)
    if iCount:
        oState.SetCount(oWarrior, iCount)


def CustomAction33272(oWarrior, oEventCB, dInfo):
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    oGame = oWarrior.m_Game
    iScene = oWarrior.m_Scene
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return None
    lstMonster = oScene.GetObjectsByType('Monster')
    dDis = oGame.Scene_GetTargetDisMap(oWarrior.m_ID, lstMonster, 1)
    lstSortedDis = sorted(dDis.items(), key = (lambda x: x[1]))
    iNearVictim = 0
    for iTarget, fDis in lstSortedDis:
        if fDis > dInfo['CheckDis']:
            break
        if iTarget == oWarrior.m_ID:
            continue
        oCurTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oCurTarget:
            continue
        if not iNearVictim:
            iNearVictim = iTarget
        oTargetState = oCurTarget.m_State.GetItemBySID(oState.m_SID)
        if not oTargetState:
            continue
        iCount = oTargetState.GetCount()
        if iCount >= oState.m_MaxCount:
            continue
        iNearVictim = iTarget
    
    if iNearVictim:
        oNearVictim = oGame.GetObject(iNearVictim, PY_FLAG_DEAD)
        iInitCount = oState.GetCount()
        if oNearVictim:
            if 'PFLV' in oState.m_StateInfo and oState.m_StateInfo['PFLV'] <= 2:
                iStateFrame = oState.GetRemainTime()
            else:
                iStateFrame = dInfo['Frame']
            if not iStateFrame:
                return None
            iAttacker = oState.m_StateInfo['AID']
            oNearVictimState = oNearVictim.m_State.GetItemBySource(oState.m_SID, iAttacker)
            if oNearVictimState:
                oNearVictimState.AddCount(oNearVictim, iInitCount, iStateFrame)
            elif 'arg' in oState.m_StateInfo:
                pass
            
            dData = {
                'AID': oState.Reason(),
                'RS': oState.GetPerformID(),
                'pfid': oState.m_StateInfo['PFLV'] if 'PFLV' in oState.m_StateInfo else 0,
                'PFLV': oState.m_StateInfo['arg'],
                'arg': { } }
            oAddState = cl_state.AddState(oNearVictim, oState.m_SID, STATE_TIME_LIMIT, iStateFrame, dData)
            if not oAddState:
                return None
            oAddState.Enable(oNearVictim)
            oAddState.AddCount(oNearVictim, iInitCount, iStateFrame)


def CustomAction32006(oTarget, oLifeCycle, dArgs):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    oGame = oTarget.m_Game
    oAttack = oGame.GetObject(oState.m_StateInfo['AID'])
    if not oAttack:
        return None
    iLastFrame = oGame.GetFrameNum() - oState.m_CreateFrame
    dTransFactor = oState.GetArgValue('TransDamFactor', { })
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, oAttack, {
        'StateSID': oState.m_SID,
        'LastFrame': iLastFrame,
        'TransDamFactor': dTransFactor })


def CustomAction33041(oTarget, oEventCB, dInfo):
    iDefTrend = oTarget.m_DefendTrend
    if iDefTrend == DEFEND_TREND_NONE:
        return None
    iValue = dInfo['Value']
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iValue = cl_formula.GetResultByData(oTarget, iValue, dEventInfo, dMsgInfo)
    if not iValue:
        return None
    iStateID = dEventInfo['StateID']
    oState = oTarget.m_State.GetItem(iStateID)
    if not oState:
        return False
    iAID = oState.m_Attacker
    dData = {
        'ShowTips': 0 }
    oReason = dEventInfo['RS'].ExtInfo(dData)
    lstChange = [
        [
            iValue,
            oReason]]
    if oTarget.Query('Defend2HP', { }):
        oReason.SetInfo('DamType', CURE_TYPE_PERFORM | DAM_USE_HP)
        dCure = {
            'MainCure': lstChange,
            'FlowCure': [],
            'RS': oReason }
        oTarget.ReceiveCure(iAID, dCure)
    elif iDefTrend == DEFEND_TREND_SHIELD:
        oReason.SetInfo('DamType', CURE_TYPE_PERFORM | DAM_USE_SHIELD)
        oTarget.HPModifyCure(iAID, lstChange)
    elif iDefTrend == DEFEND_TREND_ARMOR:
        oReason.SetInfo('DamType', CURE_TYPE_PERFORM | DAM_USE_ARMOR)
        oTarget.HPModifyCure(iAID, lstChange)


def CustomAction33341(oTarget, oEventCB, dInfo):
    
    def ClearFunc(oTarget, oLifeCycle):
        for iPerform in oTarget.Query(sKey, { }):
            oChangePerform = oTarget.GetPerform(iPerform)
            if not oChangePerform:
                continue
            oChangePerform.m_ElementTypeObj.RemoveSetModify(sKey)
        
        if oTarget.m_Servant:
            ModifyServantElementType(oTarget, sKey, iDamType, iClear = 1)

    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    sKey = 'ChangePF-%s' % oLifeCycle.Key()
    if 'Init' in dInfo:
        iHeroSID = oTarget.m_SID
        if iHeroSID not in dInfo:
            return None
        dChangePF = { }
        dHeroInfo = dInfo[iHeroSID]
        iDebuffProb = dHeroInfo['DebuffProb']
        if 'ExtraPF' in dHeroInfo:
            dChangePF.update(dHeroInfo['ExtraPF'])
        if 'ServantExtraPF' in dHeroInfo and oTarget.m_Servant:
            dChangePF.update(dHeroInfo['ServantExtraPF'])
        for iPerform in list(dChangePF):
            dChangePF[iPerform] = iDebuffProb
        
        oCareer = oTarget.GetCareerPerform()
        if oCareer:
            dChangePF[oCareer.m_SID] = iDebuffProb
        oTarget.Set(sKey, dChangePF)
    elif 'ChangeWeapon' in dInfo:
        oWeapon = oTarget.m_WieldCon.GetCurWeapon()
        if not oWeapon:
            return None
        iDamType = oWeapon.m_ElementTypeObj.GetValue()
        for iPerform in oTarget.Query(sKey, { }):
            oPerform = oTarget.GetPerform(iPerform)
            if not oPerform:
                continue
            oPerform.m_ElementTypeObj.SetModify(sKey, iDamType)
        
        if oTarget.m_Servant:
            ModifyServantElementType(oTarget, sKey, iDamType, iClear = 0)
        oLifeCycle.AddUniqueDisableFunc(sKey, ClearFunc, iCover = 0)
    elif 'ChangeDebuffProb' in dInfo:
        dMsgInfo = oEventCB.GetCBMsgInfo()
        if 'Skill' not in dMsgInfo:
            return None
        oSkill = dMsgInfo['Skill']
        iEventPF = oSkill.m_Base['pfid']
        dChangePF = oTarget.Query(sKey, { })
        if iEventPF not in dChangePF:
            return None
        if 'DebuffProb' in oSkill.m_Cache:
            iOldProb = oSkill.m_Cache['DebuffProb']
        else:
            iOldProb = 0
        iNewProb = dChangePF[iEventPF]
        if iOldProb < iNewProb:
            oSkill.m_Cache['DebuffProb'] = iNewProb


def ModifyServantElementType(oTarget, sKey, iDamType, iClear):
    oServant = oTarget.m_Game.GetObject(oTarget.m_Servant)
    if not oServant:
        return None
    for iPerform in oTarget.Query(sKey, { }):
        oPerform = oServant.GetPerform(iPerform)
        if not oPerform:
            continue
        if iClear:
            oPerform.m_ElementTypeObj.RemoveSetModify(sKey)
            continue
        oPerform.m_ElementTypeObj.SetModify(sKey, iDamType)
    


def CustomAction33335(oTarget, oLifeCycle, dArgs):
    oState = oLifeCycle.GetObject()
    oAttacker = oTarget.m_Game.GetObject(oState.m_Attacker)
    if not oAttacker:
        return None
    dStateInfo = oState.m_StateInfo
    if 'arg' not in dStateInfo:
        return None
    dStateArg = dStateInfo['arg']
    if 'Cache' not in dStateArg:
        return None
    dCache = dStateArg['Cache']
    if 'ItemID' not in dCache or 'Radius' not in dCache:
        return None
    iItem = dCache['ItemID']
    iRadius = dCache['Radius']
    oWeapon = oAttacker.m_WieldCon.GetItemByID(iItem)
    if not oWeapon:
        return None
    oPerformCom = oWeapon.GetComponent('Perform')
    oPerform = oPerformCom.GetPerform(dArgs['Perform'])
    if not oPerform:
        return None
    dCustomData = {
        'Radius': iRadius + oTarget.m_ModelRadius }
    dPerform = {
        'Custom': dCustomData,
        'VID': oTarget.m_ID }
    cl_war.UsePerform(oAttacker, oPerform, dPerform)


def CustomAction33402(oTarget, oEventCB, dArgs):
    
    def ClearPerformPos(oTarget, oLifeCycle):
        oTarget.Delete('LastPos25778')

    oPerform = oTarget.GetPerform(dArgs['PerformID'])
    if not oPerform:
        SendAlert('err', '%s未配置触发技能-CustomAction33402' % oEventCB.m_Key)
        return None
    if 'LiveTime' not in dArgs:
        return None
    vCurPos = oTarget.GetPos()
    vLastPos = oTarget.Query('LastPos25778', (0, 0, 0))
    if cl_math.IsZero(vLastPos):
        vLastPos = vCurPos
        oTarget.Set('LastPos25778', vLastPos)
        return None
    if 'fLimitDis' not in dArgs:
        SendAlert('err', '%s未设置技能触发距离-CustomAction33402' % oEventCB.m_Key)
        return None
    fLimitDis = dArgs['fLimitDis']
    if cl_math.CheckDistance(vLastPos, vCurPos, fLimitDis):
        return None
    oWarMgr = oTarget.m_Game.m_WarMgr
    oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
    oScene = oTarget.m_Game.m_SceneMgr.GetScene(oTarget.m_Scene)
    oLevelNode = oLevelCtrl.GetLevelNode(oScene.m_Level)
    if not oLevelNode:
        SendAlert('err', '%s未获取到当前关卡实例-CustomAction33402' % oEventCB.m_Key)
        return None
    dPerformPos = oLevelNode.m_CustomData.get('25778PerformPos', { })
    vPerformPos = cl_math.Vec3MulF(cl_math.Vec3Add(vCurPos, vLastPos), 0.5)
    iGameFrame = oTarget.m_Game.GetFrameNum()
    dTempPerformPos = CopyDict(dPerformPos)
    fLimitDis -= (dArgs['AdjustCoverDis'] if 'AdjustCoverDis' in dArgs else 0)
    for iFrame, vLastPerformPos in dPerformPos.items():
        if iFrame <= iGameFrame:
            dTempPerformPos.pop(iFrame)
            continue
        if cl_math.CheckDistance(vLastPerformPos, vPerformPos, fLimitDis):
            oTarget.Set('LastPos25778', vLastPerformPos)
            oLevelNode.m_CustomData['25778PerformPos'] = dTempPerformPos
            return None
    
    iGameFrame += Time2Frame(dArgs['LiveTime'])
    dTempPerformPos[iGameFrame] = vPerformPos
    dArgs['LastPos'] = vPerformPos
    dData = {
        'Custom': {
            'LastPos': vPerformPos } }
    cl_war.UsePerform(oTarget, oPerform, dData)
    oLevelNode.m_CustomData['25778PerformPos'] = dTempPerformPos
    oTarget.Set('LastPos25778', vPerformPos)
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oLifeCycle.AddUniqueDisableFunc('ClearUpPerformPos25778', ClearPerformPos, iCover = 0)


def CustomAction33428(oWarrior, oLifeCycle, dArgs):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    dStateInfo = oState.m_StateInfo
    if 'arg' not in dStateInfo:
        return None
    dStateArg = dStateInfo['arg']
    oPerform = oWarrior.GetPerform(dStateArg['Perform'])
    if not oPerform:
        return None
    dCustom = {
        'vEnd': dStateArg['TargetPos'],
        'DirectPos': 1 }
    dData = {
        'Custom': dCustom }
    cl_war.UsePerform(oWarrior, oPerform, dData)

HERO_CAREER_MAP = {
    205: (1302,),
    206: (1304,),
    207: (1670,),
    212: (1312,),
    213: (1428, 1310, 12013),
    214: (1315,),
    215: (1316,),
    216: (1317,),
    217: (7153,),
    218: (1324,),
    219: (1326, 1918, 1920, 1921) }

def CustomActionCollectDurativeSkillInfo(oTarget, oEventCB, dInfo):
    oLifeCycle = oEventCB.GetCBLifeCycle()
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    if 'CacheInfo' not in oState.m_Data:
        oState.m_Data['CacheInfo'] = { }
    dCacheInfo = oState.m_Data['CacheInfo']
    dCacheInfo['PerformCnt'] = oState.GetCount()
    dCacheInfo['LastDamFrame'] = { }
    oState.SetCount(oTarget, 0)


def CustomActionCollectDurativeSkill(oTarget, oLifeCycle, dInfo):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    if 'CacheInfo' not in oState.m_Data:
        oState.m_Data['CacheInfo'] = { }
    dCacheInfo = oState.m_Data['CacheInfo']
    dCacheInfo['LastDamFrame'] = { }


def CustomActionClearStateInfo(oTarget, oLifeCycle, dInfo):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    if 'CacheInfo' not in oState.m_Data:
        return None
    dCacheInfo = oState.m_Data['CacheInfo']
    dCacheInfo.pop('PerformCnt', 0)


def CustomActionUsePerformByDurativeInfo(oTarget, oLifeCycle, dInfo):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    oEventCB = oState.m_EventCB
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'CacheInfo' not in oState.m_Data:
        return None
    dCacheInfo = oState.m_Data['CacheInfo']
    if 'PerformCnt' not in dCacheInfo or not dCacheInfo['PerformCnt']:
        return None
    if 'CurVID' not in dMsgInfo:
        return None
    if 'CheckPerform' in dInfo:
        if 'Skill' not in dMsgInfo:
            return None
        oSkill = dMsgInfo['Skill']
        if oSkill.m_Base['pfid'] not in HERO_CAREER_MAP[oTarget.m_SID]:
            return None
    oGame = oTarget.m_Game
    iCurFrame = oGame.GetFrameNum()
    dLastFrame = dCacheInfo['LastDamFrame']
    iVictim = dMsgInfo['CurVID']
    if iVictim in dLastFrame:
        iLastFrame = dLastFrame[iVictim]
        if iCurFrame - iLastFrame < Time2Frame(dInfo['CD']):
            return None
    dLastFrame[iVictim] = iCurFrame
    UseFallingStonePerformByArgs(oTarget, iVictim, dCacheInfo['PerformCnt'], dInfo)


def CustomActionCollectSkillInfo(oTarget, oEventCB, dInfo):
    oLifeCycle = oEventCB.GetCBLifeCycle()
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    iStateCount = oState.GetCount()
    if not iStateCount:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if not CheckCanCollectSkillInfo(oTarget, oState, dMsgInfo):
        return None
    oSkill = dMsgInfo['Skill']
    dCacheInfo = oState.m_Data['CacheInfo']
    iActnum = oSkill.m_Base['ActNum']
    oState.SetCount(oTarget, 0)
    dCacheInfo[iActnum] = {
        'Hit': { },
        'PerformCnt': iStateCount }


def CheckCanCollectSkillInfo(oTarget, oState, dMsgInfo):
    if 'Skill' not in dMsgInfo:
        return 0
    if 'CacheInfo' not in oState.m_Data:
        oState.m_Data['CacheInfo'] = { }
    dCacheInfo = oState.m_Data['CacheInfo']
    oSkill = dMsgInfo['Skill']
    if oSkill.m_Base['pfid'] not in HERO_CAREER_MAP[oTarget.m_SID]:
        return 0
    if len(dCacheInfo) > 20:
        for iActNum in dCacheInfo:
            dCacheInfo.pop(iActNum)
        
    iActnum = oSkill.m_Base['ActNum']
    if iActnum in dCacheInfo:
        return 0
    return 1


def CustomActionUsePerformByInfo(oTarget, oLifeCycle, dInfo):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    oEventCB = oState.m_EventCB
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    iChildrenSkill = cl_formula.GetResultByData(oTarget, dInfo['ChildrenSkill'], {
        'LifeCycle': oLifeCycle })
    if iChildrenSkill:
        iActnum = oSkill.m_CacheData.m_ParentActnum
    else:
        iActnum = oSkill.m_Base['ActNum']
    if 'CurVID' not in dMsgInfo:
        return None
    if 'CacheInfo' not in oState.m_Data:
        return None
    dCacheInfo = oState.m_Data['CacheInfo']
    if iActnum not in dCacheInfo:
        return None
    iVictim = dMsgInfo['CurVID']
    dHitInfo = dCacheInfo[iActnum]['Hit']
    if iVictim in dHitInfo:
        return None
    dHitInfo[iVictim] = 1
    iPerformCnt = dCacheInfo[iActnum]['PerformCnt']
    UseFallingStonePerformByArgs(oTarget, iVictim, iPerformCnt, dInfo)


def UseFallingStonePerformByArgs(oTarget, iVictim, iPerformCnt, dInfo):
    iPerform = dInfo['Perform']
    if not iPerformCnt % dInfo['Num']:
        iDouble = 1
    else:
        iDouble = 0
    dData = {
        'Att': dInfo['Att'] * 2 if iDouble else dInfo['Att'],
        'Cnt': iPerformCnt,
        'IsDouble': iDouble }
    oPerform = oTarget.GetPerform(iPerform)
    if not oPerform:
        return None
    dData = {
        'Custom': dData,
        'VID': iVictim }
    cl_war.UsePerform(oTarget, oPerform, dData)


def CustomAction33476(oTarget, oLifeCycle, dInfo):
    if 'ForceNum' not in dInfo or 'SID' not in dInfo or 'Radius' not in dInfo or 'OffsetY' not in dInfo:
        SendAlert('err', '%s lose arg' % oLifeCycle.m_Key)
        return None
    oGame = oTarget.m_Game
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    if not oLevelCtrl:
        return None
    iScene = oLevelCtrl.m_CurNode.m_Scene
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return None
    iForceNum = cl_formula.GetResultByData(oTarget, dInfo['ForceNum'], {
        'LifeCycle': oLifeCycle })
    vDropPos = ()
    vPos = ()
    lstNPC = oScene.GetObjectsByType('NPC')
    for iNPCID in lstNPC:
        oNpc = oGame.GetObject(iNPCID)
        if oNpc and oNpc.m_FightType == NWARRIOR_NPC_PASSBOX:
            vDir = oNpc.GetFacing()
            vPos = oNpc.GetPos()
            for _ in range(10):
                vDropPos = oGame.Scene_RandomPointSectorInMesh(iScene, vPos, vDir, 0, dInfo['Radius'], 0, 90)
                if vDropPos:
                    break
            
    
    pid = oTarget.m_PlayerID
    if not vPos:
        TaskLog.Alert('%s %s %s %s no npcpos' % (oGame.m_ID, iScene, pid, oLifeCycle.m_Key))
        return None
    if not vDropPos:
        vDropPos = (vPos[0], vPos[1] + dInfo['OffsetY'], vPos[2])
    dReward = {
        'item': VIRTUAL_ITEM_GOLDENCUP,
        'info': {
            'sid': dInfo['SID'],
            'Share': 0,
            'VisiblePlayer': {
                pid: 1 },
            'SetInfo': {
                'ForceNum': iForceNum },
            'DropPos': vDropPos } }
    dInfo = {
        FAKEMG_GOLDENCUP: (0, [
            dReward], { }) }
    oTarget.m_Game.GetResMgr().CreateDrop(iScene, NWARRIOR_DROP_DEMON, vDropPos, [
        dInfo], { }, {
        'DropSource': pid,
        'Quality': 2 }, iOwner = oTarget.m_ID)


def CustomActionCollectSkill(oTarget, oLifeCycle, dInfo):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    oEventCB = oState.m_EventCB
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if not CheckCanCollectSkillInfo(oTarget, oState, dMsgInfo):
        return None
    oSkill = dMsgInfo['Skill']
    dCacheInfo = oState.m_Data['CacheInfo']
    iActnum = oSkill.m_Base['ActNum']
    dCacheInfo[iActnum] = {
        'Hit': { } }


def CustomActionAddState(oTarget, oLifeCycle, dInfo):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    oEventCB = oState.m_EventCB
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    if oTarget.m_SID == 212:
        iActnum = oSkill.m_CacheData.m_ParentActnum
    else:
        iActnum = oSkill.m_Base['ActNum']
    if 'CurVID' not in dMsgInfo:
        return None
    if 'CacheInfo' not in oState.m_Data:
        return None
    dCacheInfo = oState.m_Data['CacheInfo']
    if iActnum not in dCacheInfo:
        return None
    iVictim = dMsgInfo['CurVID']
    dHitInfo = dCacheInfo[iActnum]['Hit']
    if iVictim in dHitInfo:
        return None
    dHitInfo[iVictim] = 1
    oGame = oTarget.m_Game
    oVictim = oGame.GetObject(iVictim, PY_FLAG_DEAD)
    if not oVictim:
        return None
    AddStateByArgs(oTarget, oState, oVictim, dInfo)


def CustomActionAddStateByDurativeInfo(oTarget, oLifeCycle, dInfo):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    oEventCB = oState.m_EventCB
    if 'CacheInfo' not in oState.m_Data:
        return None
    dCacheInfo = oState.m_Data['CacheInfo']
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'CurVID' not in dMsgInfo:
        return None
    if oTarget.m_SID in (207, 213, 219):
        if 'Skill' not in dMsgInfo:
            return None
        oSkill = dMsgInfo['Skill']
        if oSkill.m_Base['pfid'] not in HERO_CAREER_MAP[oTarget.m_SID]:
            return None
    oGame = oTarget.m_Game
    iCurFrame = oGame.GetFrameNum()
    dLastFrame = dCacheInfo['LastDamFrame']
    iVictim = dMsgInfo['CurVID']
    if iVictim in dLastFrame:
        iLastFrame = dLastFrame[iVictim]
        if iCurFrame - iLastFrame < Time2Frame(dInfo['CD']):
            return None
    dLastFrame[iVictim] = iCurFrame
    oGame = oTarget.m_Game
    oVictim = oGame.GetObject(iVictim, PY_FLAG_DEAD)
    if not oVictim:
        return None
    AddStateByArgs(oTarget, oState, oVictim, dInfo)


def AddStateByArgs(oTarget, oState, oVictim, dInfo):
    dData = {
        'AID': oTarget.m_ID,
        'RS': oState.Reason(),
        'pfid': oState.GetPerformID(),
        'PFLV': oState.m_StateInfo['PFLV'] if 'PFLV' in oState.m_StateInfo else 0,
        'arg': oState.m_StateInfo['arg'] if 'arg' in oState.m_StateInfo else { } }
    oAddState = cl_state.AddState(oVictim, dInfo['AddStateSID'], STATE_TIME_LIMIT, Time2Frame(dInfo['Time']), dData)
    if not oAddState:
        return None
    oAddState.Enable(oVictim)

HERO_NEXT_ATTACK_SKILL = {
    201: (1409,),
    205: (1302, 1410),
    206: (1304, 1411),
    207: (1412,),
    212: (1313, 1419),
    213: (1427,),
    214: (1315, 1422),
    215: (1316, 1423),
    216: (1317, 1424),
    217: (7153, 1426),
    218: (1324, 1429),
    219: (1431,) }

def CustomAction33533(oTarget, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    if not dInfo['FromWeapon']:
        pfid = oSkill.m_Base['pfid']
        iTargetSID = oTarget.m_SID
        if iTargetSID not in HERO_NEXT_ATTACK_SKILL or pfid not in HERO_NEXT_ATTACK_SKILL[iTargetSID]:
            return None
    oSkill.m_Collect['ST33533'] = 1
    iActNum = oSkill.m_Base['ActNum']
    iStateSID = dInfo['AddStateSID']
    iTargetID = oTarget.m_ID
    oSkill.AddEndFunc(Functor(CustomActionEndFunc, iStateSID, iTargetID))
    oStateCon = oTarget.m_State
    oState = oStateCon.GetItemBySID(iStateSID)
    if not oState:
        dData = {
            'AID': iTargetID,
            'RS': cl_object.reason.CStrReason(oEventCB.Key()) }
        oState = cl_state.AddState(oTarget, iStateSID, STATE_TIME_FOREVER, 0, dData)
        if not oState:
            return None
        oState.Enable(oTarget)
        oState.SetArgValue('SkillInfo', {
            iActNum: 1 })
    else:
        dSkillInfo = oState.GetArgValue('SkillInfo', { })
        dSkillInfo[iActNum] = 1
    dEventInfo = oEventCB.GetCBEventInfo()
    iStateID = dEventInfo['StateID']
    oStateCon.RemoveItem(iStateID)


def CustomActionEndFunc(iStateSID, iTargetID, oSkill):
    oTarget = oSkill.m_Game.GetObject(iTargetID)
    if not oTarget:
        return None
    oStateCon = oTarget.m_State
    oState = oStateCon.GetItemBySID(iStateSID)
    if not oState:
        return None
    iActNum = oSkill.m_Base['ActNum']
    dSkillInfo = oState.GetArgValue('SkillInfo', { })
    if iActNum not in dSkillInfo:
        return None
    dSkillInfo.pop(iActNum)
    if not dSkillInfo:
        oStateCon.RemoveItem(oState.m_ID)


def CustomAction33510Add(oTarget, oLifeCycle, dArgs):
    if not 'Transmit' or 'CurDam' not in dArgs:
        SendAlert('err', '参数Transmit或CurDam未配置')
        return None
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    iFinishTime = oTarget.m_Game.GetFrameNum() + oState.GetTime()
    dData = {
        'LifeCycle': oLifeCycle }
    iDam = cl_formula.GetResultByData(oTarget, dArgs['CurDam'], dData)
    if dArgs['Transmit']:
        if 'Transmit' not in oState.m_Data:
            oState.m_Data['Transmit'] = []
        oState.m_Data['Transmit'].append((iDam, iFinishTime))
        oState.m_Data['TransmitNum'] = len(oState.m_Data['Transmit'])
        if 'TransmitDam' not in oState.m_Data:
            oState.m_Data['TransmitDam'] = iDam
        else:
            oState.m_Data['TransmitDam'] += iDam
    elif 'NoTransmit' not in oState.m_Data:
        oState.m_Data['NoTransmit'] = []
    oState.m_Data['NoTransmit'].append((iDam, iFinishTime))
    if 'Dam' not in oState.m_Data:
        oState.m_Data['Dam'] = iDam
    else:
        oState.m_Data['Dam'] += iDam


def CustomAction33510Update(oTarget, oLifeCycle, dArgs):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    iCurFrame = oTarget.m_Game.GetFrameNum()
    iIndex = 0
    if 'Transmit' in oState.m_Data:
        for iDam, iFrame in oState.m_Data['Transmit']:
            if iFrame >= iCurFrame:
                break
            iIndex += 1
            oState.m_Data['Dam'] -= iDam
            oState.m_Data['TransmitDam'] -= iDam
        
        if iIndex:
            oState.m_Data['Transmit'] = oState.m_Data['Transmit'][iIndex:]
            oState.m_Data['TransmitNum'] = len(oState.m_Data['Transmit'])
    if 'NoTransmit' in oState.m_Data:
        iIndex = 0
        for iDam, iFrame in oState.m_Data['NoTransmit']:
            if iFrame >= iCurFrame:
                break
            iIndex += 1
            oState.m_Data['Dam'] -= iDam
        
        if iIndex:
            oState.m_Data['NoTransmit'] = oState.m_Data['NoTransmit'][iIndex:]


def CustomAction8137(oWarrior, oLifeCycle, dArgs):
    oGame = oWarrior.m_Game
    iScene = oWarrior.m_Scene
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return None
    iAttack = oWarrior.m_ID
    iSide = oWarrior.m_Side
    iGroundHight = dArgs['vCenterY']
    vCenterPos = (dArgs['vCenterX'], iGroundHight, dArgs['vCenterZ'])
    iOutDis = dArgs['OutDis']
    iDamage = cl_formula.GetResultByData(oWarrior, dArgs['Dam'], {
        'LifeCycle': oLifeCycle })
    iHight = dArgs['Hight']
    iInDis = dArgs['InDis']
    iLimitHight = iGroundHight + iHight
    if oGame.m_WarMgr.Query('DebugCurve'):
        debug.ClearDebugLine(oGame)
        debug.DebugCircle(oGame, vCenterPos, iInDis, debug.LINE_NORMAL)
        debug.DebugCircle(oGame, vCenterPos, iOutDis, debug.LINE_NORMAL)
        debug.DebugCircle(oGame, (vCenterPos[0], vCenterPos[1] + iHight, vCenterPos[2]), iInDis, debug.LINE_NORMAL)
        debug.DebugCircle(oGame, (vCenterPos[0], vCenterPos[1] + iHight, vCenterPos[2]), iOutDis, debug.LINE_NORMAL)
    for dObjestInfo in oScene.m_Objects.values():
        for iTarget in dObjestInfo:
            oTarget = oGame.GetObject(iTarget)
            if not cl_math.CheckTargetType(oGame, oTarget, iAttack, iSide, OBJ_ENEMY):
                continue
            vTargetPos = oTarget.GetPos()
            iTargetHight = vTargetPos[1]
            if iLimitHight < iTargetHight or iTargetHight < iGroundHight:
                continue
            fDis = cl_math.CalDistance(vTargetPos, vCenterPos)
            if fDis > iOutDis or fDis < iInDis:
                continue
            oReason = cl_object.reason.CStrReason('CustomAction8137', None, {
                'DamType': DAM_TYPE_WEAPON | DAM_TYPE_NORMAL | DAM_USE_ALL })
            dDamage = {
                'AID': iAttack,
                'CurVID': iTarget,
                'MainDam': [
                    (iDamage, oReason)],
                'FlowDam': [],
                'RS': oReason,
                'DamFactor': {
                    OBJ_VICTIM: { },
                    OBJ_ATTACK: { } } }
            oTarget.ReceiveDamage(iAttack, dDamage)
        
    


def On7157SkillEnd(iPerformSID, iStateSID, oSkill):
    oWarrior = oSkill.GetAttack()
    if not oWarrior:
        return None
    iSkillCnt = oWarrior.Query('7157WaitCnt', 0)
    iSkillCnt -= 1
    oWarrior.Set('7157WaitCnt', iSkillCnt)
    if iSkillCnt <= 0:
        UsePerform7157(oWarrior, iPerformSID, iStateSID)


def On7157UsePerformEnd(iStateSID, oSkill):
    oWarrior = oSkill.GetAttack()
    if not oWarrior:
        return None
    sKey = '7157UseCnt'
    iUseCnt = oWarrior.Query(sKey, 0)
    iUseCnt -= 1
    if iUseCnt > 0:
        oWarrior.Set(sKey, iUseCnt)
    else:
        oWarrior.Delete(sKey)
        cl_state.RemoveState(oWarrior, iStateSID)


def UsePerform7157(oWarrior, dPerform, iStateSID):
    oGame = oWarrior.m_Game
    oSkillMgr = oGame.m_SkillMgr
    sFlag = '7157Flag'
    iUseCnt = 0
    for iPerformSID, iCnt in dPerform.items():
        dCustom = {
            sFlag: 1 }
        if iCnt:
            dCustom['BallisticType'] = iCnt
        oPerform = oWarrior.GetPerform(iPerformSID, 0)
        if not oPerform:
            continue
        oWarrior.m_Perform.DelCoverColdTime(iPerformSID)
        cl_war.UsePerform(oWarrior, oPerform, {
            'Custom': dCustom })
        for oSkill in oSkillMgr.GetSkillBySID(iPerformSID):
            if sFlag not in oSkill.m_Custom:
                continue
            iUseCnt += 1
            oSkill.AddEndFunc(Functor(On7157UsePerformEnd, iStateSID))
        
    
    oWarrior.Set('7157UseCnt', iUseCnt)


def CustomAction7157(oWarrior, oLifeCycle, dArgs):
    for sArg in ('Perform', 'WaitPerform'):
        if sArg not in dArgs:
            SendAlert('err', '%s lose arg %s' % (oLifeCycle.m_Key, sArg))
            return None
    
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    iStateSID = oState.m_SID
    oSkillMgr = oWarrior.m_Game.m_SkillMgr
    iSkillCnt = 0
    dPerform = dArgs['Perform']
    for iPerformSID in oWarrior.m_Perform.GetAllPerformSID():
        lstSkill = oSkillMgr.GetSkillBySID(iPerformSID)
        if not lstSkill:
            continue
        for oSkill in lstSkill:
            if not (oSkill.m_Base) or oSkill.m_Base['pfid'] not in dArgs['WaitPerform']:
                continue
            iSkillCnt += 1
            oSkill.AddEndFunc(Functor(On7157SkillEnd, dPerform, iStateSID))
        
    
    if iSkillCnt:
        oWarrior.Set('7157WaitCnt', iSkillCnt)
    else:
        UsePerform7157(oWarrior, dPerform, iStateSID)


def CustomAction33607_1(oWarrior, oLifeCycle, dArgs):
    
    def ClearEvent(oOwner, oLifeCycle):
        cl_msgcenter.DoneAttention(oWarrior, iTarget, cl_msgcenter.MSG_WAR_DYING, sKey)
        cl_msgcenter.DoneAttention(oWarrior, iTarget, cl_msgcenter.MSG_WAR_LEAVESCENE, sKey)

    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    if 'ChaseTarget' not in oState.m_Data:
        return None
    iTarget = oState.m_Data['ChaseTarget']
    oTarget = oWarrior.m_Game.GetObject(iTarget, PY_FLAG_DEAD)
    if not oTarget:
        return None
    sKey = oLifeCycle.Key()
    cl_msgcenter.AddAttentionFunc(oWarrior, iTarget, cl_msgcenter.MSG_WAR_DYING, ClearChaseState, sKey)
    cl_msgcenter.AddAttentionFunc(oWarrior, iTarget, cl_msgcenter.MSG_WAR_LEAVESCENE, ClearChaseState, sKey)
    oLifeCycle.AddDisableFunc(ClearEvent)


def ClearChaseState(oWarrior, oHero, dMsgInfo):
    oState = oHero.m_State.GetItemBySID(HERO_CHASED_STATE)
    if not oState:
        return None
    dStateData = oState.m_Data
    if 'ChaseShark' not in dStateData:
        return None
    iShark = oWarrior.m_ID
    if iShark not in dStateData['ChaseShark']:
        return None
    dStateData['ChaseShark'].pop(iShark)
    oState.AddCount(oHero, -1)
    if not oState.GetCount():
        oHero.m_State.RemoveItem(oState.m_ID)


def CustomAction33607_2(oWarrior, oLifeCycle, dArgs):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    if 'ChaseTarget' not in oState.m_Data:
        return None
    iHero = oState.m_Data['ChaseTarget']
    oHero = oWarrior.m_Game.GetObject(iHero)
    oHeroChasedState = oHero.m_State.GetItemBySID(HERO_CHASED_STATE)
    if not oHeroChasedState:
        return None
    dStateData = oHeroChasedState.m_Data
    if 'ChaseShark' not in dStateData:
        return None
    iShark = oWarrior.m_ID
    if iShark not in dStateData['ChaseShark']:
        return None
    dStateData['ChaseShark'].pop(iShark)
    oHeroChasedState.AddCount(oHero, -1)
    if not oHeroChasedState.GetCount():
        oHero.m_State.RemoveItem(oHeroChasedState.m_ID)


def CustomAction33669_0(oTarget, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if not 'Ability' in dMsgInfo and dMsgInfo['Ability'] == WANDABILITY_ADDEXTCONCOMP:
        return None
    if 'Wand' not in dMsgInfo:
        return None
    iWandID = dMsgInfo['Wand']
    oWand = oTarget.m_WandCon.GetWandByID(iWandID)
    if not oWand:
        return None
    if not oWand.HasWandAbility(WANDABILITY_ADDEXTCONCOMP):
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oState = oLifeCycle.GetObject()
    dWandInfo = oState.SetArgValueDefault('WandInfo', { })
    if iWandID in dWandInfo:
        return None
    iConNum = 1
    dWandInfo[iWandID] = iConNum
    sKey = oEventCB.m_Key
    oWand.SetExtConComp(sKey, iConNum, iNotyfiy = 1)


def CustomAction33669_1(oTarget, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if not 'Ability' in dMsgInfo and dMsgInfo['Ability'] == WANDABILITY_ADDEXTCONCOMP:
        return None
    if 'Wand' not in dMsgInfo:
        return None
    iWandID = dMsgInfo['Wand']
    oWand = oTarget.m_WandCon.GetWandByID(iWandID)
    if not oWand:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oState = oLifeCycle.GetObject()
    dWandInfo = oState.GetArgValue('WandInfo', { })
    if iWandID not in dWandInfo:
        return None
    dWandInfo.pop(iWandID)
    sKey = oEventCB.m_Key
    oWand.DelExtConComp(sKey, iNotyfiy = 1)
    if not dWandInfo:
        oTarget.m_State.RemoveItem(oState.m_ID)


def CustomAction33669_2(oTarget, oLifeCycle, dInfo):
    sKey = oLifeCycle.Key()
    oState = oLifeCycle.GetObject()
    dWandInfo = oState.GetArgValue('WandInfo', { })
    iLoading = oState.GetArgValue('Loading', 0)
    for iWandID in dWandInfo:
        oWand = oTarget.m_WandCon.GetWandByID(iWandID)
        if not oWand:
            continue
        if iLoading:
            oWand.SetExtConComp(sKey, 1, iNotyfiy = 0)
            oWand.RecoveryExtConCompSaveInfo()
            continue
        oWand.SetExtConComp(sKey, 1, iNotyfiy = 1)
    


def CustomAction33693_0(oTarget, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if not 'Ability' in dMsgInfo and dMsgInfo['Ability'] == WANDABILITY_ADDEXTACTCOMP:
        return None
    if 'Wand' not in dMsgInfo:
        return None
    iWandID = dMsgInfo['Wand']
    oWand = oTarget.m_WandCon.GetWandByID(iWandID)
    if not oWand:
        return None
    if not oWand.HasWandAbility(WANDABILITY_ADDEXTACTCOMP):
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oState = oLifeCycle.GetObject()
    dWandInfo = oState.SetArgValueDefault('WandInfo', { })
    if iWandID in dWandInfo:
        return None
    iActNum = 1
    dWandInfo[iWandID] = iActNum
    sKey = oEventCB.m_Key
    oWand.SetExtActionComp(sKey, iActNum, iNotyfiy = 1)


def CustomAction33693_1(oTarget, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if not 'Ability' in dMsgInfo and dMsgInfo['Ability'] == WANDABILITY_ADDEXTACTCOMP:
        return None
    if 'Wand' not in dMsgInfo:
        return None
    iWandID = dMsgInfo['Wand']
    oWand = oTarget.m_WandCon.GetWandByID(iWandID)
    if not oWand:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oState = oLifeCycle.GetObject()
    dWandInfo = oState.GetArgValue('WandInfo', { })
    if iWandID not in dWandInfo:
        return None
    dWandInfo.pop(iWandID)
    sKey = oEventCB.m_Key
    oWand.DelExtActionComp(sKey, iNotyfiy = 1)
    if not dWandInfo:
        oTarget.m_State.RemoveItem(oState.m_ID)


def CustomAction33693_2(oTarget, oLifeCycle, dInfo):
    sKey = oLifeCycle.Key()
    oState = oLifeCycle.GetObject()
    dWandInfo = oState.GetArgValue('WandInfo', { })
    for iWandID in dWandInfo:
        oWand = oTarget.m_WandCon.GetWandByID(iWandID)
        if not oWand:
            continue
        oWand.SetExtActionComp(sKey, 1, iNotyfiy = 1)
    


def CustomAction33693_3(oTarget, oLifeCycle, dInfo):
    sKey = oLifeCycle.Key()
    oState = oLifeCycle.GetObject()
    dWandInfo = oState.GetArgValue('WandInfo', { })
    iLoading = oState.GetArgValue('Loading', 0)
    for iWandID in dWandInfo:
        oWand = oTarget.m_WandCon.GetWandByID(iWandID)
        if not oWand:
            continue
        if iLoading:
            oWand.SetExtActionComp(sKey, 1, iNotyfiy = 0)
            oWand.RecoveryExtActCompSaveInfo()
            continue
        oWand.SetExtActionComp(sKey, 1, iNotyfiy = 1)
    


def CustomAction33604(oTarget, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'SkillCount' not in dMsgInfo:
        return None
    iPerform = dInfo['HeavyPerform']
    oPerform = oTarget.GetPerform(iPerform)
    if not oPerform:
        return None
    iSkillCount = dMsgInfo['SkillCount']
    oLifeCycle = oEventCB.GetCBLifeCycle()
    oTalent = oTarget.m_TalentCon.GetPerform(dInfo['Talent'])
    oState = oTarget.m_State.GetItemBySID('HitState')
    iHitCount = oState.GetCount() if oState else 0
    if oTalent:
        if (oTalent.m_Level >= dInfo['TalentLevel'] or iHitCount >= dInfo['NoCostCount']) and iSkillCount == dInfo['HeavyCount']:
            iHeavyUseEnergy = 0
            oPerform.SetArgValue('EnergyCostH4', 0)
        else:
            iHeavyUseEnergy = dInfo['HeavyUseEnergy']
            oPerform.SetArgValue('EnergyCostH4', -dInfo['HeavyUseEnergy'])
    None.SetArgValue('SkillCount', iSkillCount)
    cl_action.CommonSetPerformForceAttr(oTarget, oLifeCycle, iPerform, 'MinUseEnergy', iHeavyUseEnergy)


def CustomAction33547(oTarget, oLifeCycle, dInfo):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    dArgValue = oState.GetArgValue('Soure', { })
    oGame = oTarget.m_Game
    for iSoureTarget in dArgValue:
        oSoureTarget = oGame.GetObject(iSoureTarget)
        if oSoureTarget:
            cl_action.StateReceiveDam(oTarget, oLifeCycle, dInfo['Dam'], DAM_TYPE_FIRE, 0, 0, 0, 0)
            break
        SendAlert('err', 'state33547 soure err %s %s' % (dArgValue, iSoureTarget))
    else:
        oTarget.m_State.RemoveItem(oState.m_ID)


def CustomAction33700(oTarget, oLifeCycle, dArgs):
    oState = oLifeCycle.GetObject()
    iCurCount = oState.GetCount()
    if iCurCount <= 0:
        return None
    oState.AddCount(oTarget, -1)
    dTempUseTimes = oState.SetArgValueDefault('CareerPfTempUseTimes', { })
    if not dTempUseTimes:
        return None
    sUseKey = sorted(dTempUseTimes, key = (lambda x: x[0]), reverse = True)[0]
    (iOldPriority, iOldTimes) = dTempUseTimes[sUseKey]
    iOldTimes -= 1
    if iOldTimes <= 0:
        dTempUseTimes.pop(sUseKey, None)
    else:
        dTempUseTimes[sUseKey] = (iOldPriority, iOldTimes)


def CustomAction33711(oTarget, oEventCB, dInfo):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTargetList = dTransInfo['TargetList']
    if not lstTargetList:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    oGame = oTarget.m_Game
    (iMinValue, iChooseTarget) = (0, 0)
    lstSelected = oState.GetArgValue('33711_Selected', [])
    for iTarget in lstTargetList:
        if iTarget in lstSelected:
            continue
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DIED)
        if not oTarget:
            continue
        iValue = oTarget.HP() + oTarget.Shield() + oTarget.Armor()
        if not not iMinValue:
            if iValue < iMinValue:
                iMinValue = iValue
                iChooseTarget = iTarget
                continue
    
    if not iChooseTarget:
        if lstSelected:
            lstChooseTarget = [
                lstSelected[0]]
            dTransInfo['TargetList'] = lstChooseTarget
            oState.SetArgValue('33711_Selected', lstChooseTarget)
        else:
            dTransInfo['TargetList'] = []
        return None
    if len(lstSelected) >= dInfo['MaxSize']:
        lstSelected.pop(0)
    lstSelected.append(iChooseTarget)
    oState.SetArgValue('33711_Selected', lstSelected)
    dTransInfo['TargetList'] = [
        iChooseTarget]


def CustomAction33732_0(oTarget, oEventCB, dArgs):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iWand = dMsgInfo['Wand']
    oWandCon = oTarget.m_WandCon
    oWand = oWandCon.GetWandByID(iWand)
    if not oWand:
        return None
    lstSameWand = oWandCon.GetSameWand(oWand)
    if len(lstSameWand) <= 1:
        return None
    for oTmp in lstSameWand:
        if oTmp.m_ID == oWand.m_ID:
            continue
        oTmpWand = oTmp
    
    oWand.m_ExtActCompInfo = oTmpWand.GetExtActCompSaveInfo()
    oWand.m_ExtActionCompCache = oWand.m_ExtActCompInfo
    oWand.RecoveryExtActCompSaveInfo(False)


def CustomAction33732_1(oTarget, oLifeCycle, dArgs):
    oWandCon = oTarget.m_WandCon
    for oWand in oWandCon.m_Wand.values():
        if oWand.m_SID != PAIR_WAND:
            continue
        oWand.m_ExtActionCompCache = oWand.m_ExtActCompInfo
        iCondIconNum = oWand.GetCompIconNum(WAND_COMP_TYPE_CONDITION)
        oWand.SetExtActionComp(oLifeCycle.Key(), iCondIconNum, 1)
        dExtActComp = oWand.m_ExtActCompInfo
        if dExtActComp:
            oWand.RecoveryExtActCompSaveInfo(False)
    


def CustomAction33732_2(oTarget, oEventCB, dArgs):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iWand = dMsgInfo['Wand']
    oWandCon = oTarget.m_WandCon
    oWand = oWandCon.GetWandByID(iWand)
    if not oWand:
        return None
    iCompType = dMsgInfo['CompType']
    iPos = dMsgInfo['CompPos']
    if 'AddComp' in dArgs:
        iCompSID = dMsgInfo['WandCompSID']
        iLevel = dMsgInfo['Quality']
        oWand.UpdateExtActCompCache(iCompType, iPos, iCompSID, iLevel, 1)
    elif not oWand.QueryTmp('WandUpgrade'):
        oWand.UpdateExtActCompCache(iCompType, iPos, 0, 0, 0)


def CustomAction33732_3(oTarget, oEventCB, dArgs):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iWand = dMsgInfo['Wand']
    oWandCon = oTarget.m_WandCon
    oWand = oWandCon.GetWandByID(iWand)
    if not oWand:
        return None
    oWand.TryUseExtActCompCache()


def CustomAction33744(oTarget, oLifeCycle, dArgs):
    oState = oLifeCycle.m_Owner
    oEventCB = oState.m_EventCB
    sKey = oEventCB.GetCBMsgInfo()['Key'] if 'Key' in oEventCB.GetCBMsgInfo() else ''
    sTargetKey = 'CState-%d' % oState.m_SID
    if not sKey or sKey != sTargetKey:
        return None
    oOwner = oState.GetOwner()
    oDiceContainer = oOwner.m_DiceCon
    iDice = oDiceContainer.GetDiceBySID(dArgs['iDiceSID'], bAssemble = True)
    if not iDice:
        return None
    oDiceContainer.AddDicePoints(iDice, -1, 'Process-%d' % iDice)


def LionEnableTargetEffectExtraArgs(oTarget, dExtraArgs):
    (iEffectRadius, iEffectHigh) = (0, 0)
    for iRadius, iHigh in dExtraArgs.values():
        if iRadius > iEffectRadius:
            iEffectRadius = iRadius
        if iHigh > iEffectHigh:
            iEffectHigh = iHigh
    
    sCommonKey = 'CommonLionLock'
    oTarget.ClearSkillCheckExtraArgs(sCommonKey)
    if iEffectRadius or iEffectHigh:
        oTarget.AddSkillCheckExtraArgs(sCommonKey, iEffectRadius, iEffectHigh)


def CustomAction8155_0(oTarget, oLifeCycle, dArgs):
    iCurRadius = cl_formula.GetResultByData(oTarget, dArgs['Radius'], {
        'LifeCycle': oLifeCycle })
    iCurHigh = cl_formula.GetResultByData(oTarget, dArgs['High'], {
        'LifeCycle': oLifeCycle })
    dExtraArgs = oTarget.SetDefault('LionLockCheckExtraArgs', { })
    dExtraArgs[oLifeCycle.m_Key] = (iCurRadius / 100, iCurHigh / 100)
    LionEnableTargetEffectExtraArgs(oTarget, dExtraArgs)


def CustomAction8155_1(oTarget, oLifeCycle, dArgs):
    dExtraArgs = oTarget.SetDefault('LionLockCheckExtraArgs', { })
    dExtraArgs.pop(oLifeCycle.m_Key, None)
    LionEnableTargetEffectExtraArgs(oTarget, dExtraArgs)


def CustomAction20027(oTarget, oLifeCycle, dArgs):
    if oTarget.QueryBitAttr('LogicKey') & FIGHT3_KEY_EVACT_IGNELECORRISION:
        return None
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    dStateInfo = oState.m_StateInfo
    dArgData = dStateInfo['arg']
    dCache = dArgData['Cache'] if 'Cache' in dArgData else { }
    if not dCache:
        iFactor = ABNORMAL_DEFAULT
    elif 'CorrisionAbnormalFactor' in dCache:
        pass
    
    iFactor = ABNORMAL_DEFAULT
    iMoveSpeedMul = 50 * iFactor
    if iMoveSpeedMul > MAX_SPEEDEFFECTBY_CORRISION_ABNORMAL:
        iMoveSpeedMul = MAX_SPEEDEFFECTBY_CORRISION_ABNORMAL
    if oTarget.m_State.GetItemBySID(STATE_PAINFULREVERSE):
        oLifeCycle.m_Apply['MoveSpeed'] = 1
        oTarget.AttrChange('MoveSpeed', iMoveSpeedMul, 0, oLifeCycle.Key(), iPreExclude = 0)
    else:
        dStateArg = {
            'MoveSpeedMul': -iMoveSpeedMul }
        dStateArg.update(dArgData)
        dData = {
            'AID': dStateInfo['AID'],
            'RS': oState.Reason(),
            'pfid': oState.GetPerformID(),
            'arg': dStateArg }
        oAddState = cl_state.AddState(oTarget, 1003, STATE_TIME_FOREVER, 0, dData)
        if not oAddState:
            return None
        oLifeCycle.AddDisableType(DISABLE_TYPE_STATE, {
            oTarget.m_ID: oAddState.m_ID })
        oAddState.Enable(oTarget)


def CustomAction33668(oTarget, oEventCB, dArgs):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'AID' not in dMsgInfo:
        return None
    iAttack = dMsgInfo['AID']
    if iAttack == oTarget.m_ID:
        return None
    iNowFrame = oTarget.m_Game.GetFrameNum()
    dDamInfo = oTarget.SetDefault('DamInfo33668', { })
    if iAttack not in dDamInfo or dDamInfo[iAttack] < iNowFrame:
        dDamInfo[iAttack] = iNowFrame + Time2Frame(dArgs['Time'])
        iLimitDam = dArgs['LimitDam']
        iTotalChange = 0
        for idx, iChange in enumerate(dMsgInfo['PredictChange']):
            if iTotalChange + iChange >= iLimitDam:
                dMsgInfo['PredictChange'][idx] = iLimitDam - iTotalChange
                iTotalChange = iLimitDam
                continue
            iTotalChange += iChange
        
    else:
        for idx, iChange in enumerate(dMsgInfo['PredictChange']):
            dMsgInfo['PredictChange'][idx] = 0
        
    dMsgInfo['ExcessChange'] = 0


def CustomAction1910(oTarget, oEventCB, dArgs):
    oState = oTarget.m_State.GetItemBySID(1910)
    if not oState:
        return None
    iCnt = oState.GetCount()
    dStateArg = oState.GetArgValue('ThrowColdTime')
    if not dStateArg:
        return None
    if iCnt == 0:
        for iThrow, iColdTime in dStateArg.items():
            oPerform = oTarget.GetPerform(iThrow)
            if not oPerform:
                continue
            oPerform.SetAttr('ColdTime', iColdTime, 1)
        
    elif iCnt == 1:
        for iThrow in dStateArg.keys():
            oPerform = oTarget.GetPerform(iThrow)
            if not oPerform:
                continue
            oPerform.SetAttr('ColdTime', 0, 1)
        


def CustomAction33932(oTarget, oLifeCycle, dInfo):
    oState = oLifeCycle.GetObject()
    if not oState.GetArgValue('Spread'):
        return None
    oGame = oTarget.m_Game
    iAttacker = oState.m_Attacker
    oAttacker = oGame.GetObject(iAttacker)
    if not oAttacker:
        return None
    iNowCount = oState.GetCount()
    if iNowCount < dInfo['MinSpreadCount']:
        return None
    iCurFrameNum = oGame.GetFrameNum()
    if oAttacker.Query('st33932CD', 0) >= iCurFrameNum:
        return None
    oAttacker.Set('st33932CD', iCurFrameNum + Time2Frame(dInfo['CDTime']))
    dMask = {
        'Mask': PXMASK_MONSTER,
        'PassID': oTarget.m_ID,
        'ExcludeFlag': PY_FLAG_DEAD }
    vPos = oTarget.GetPos()
    iScene = oTarget.m_Scene
    setHitMonster = cl_math.GetAttackTargetList(oGame, iScene, ATT_SHAPE_SPHERE, [
        vPos,
        dInfo['Dis']], dMask)
    if not setHitMonster:
        return None
    (iMinCount, oTargetMonster, oTargetState) = (0, None, None)
    iAddFrame = Time2Frame(dInfo['AddTime'])
    for iMonster in setHitMonster:
        oMonster = oGame.GetObject(iMonster)
        if not oMonster:
            continue
        oMonserState = oMonster.m_State.GetItemBySource(oState.m_SID, iAttacker)
        if not oMonserState:
            iCount = 0
        else:
            iCount = oMonserState.GetCount()
        if not not iMinCount:
            if iCount < iMinCount:
                iMinCount = iCount
                oTargetMonster = oMonster
                oTargetState = oMonserState
                continue
    
    if oTargetState:
        if oTargetState.IsCountFull():
            iExtraCount = iNowCount
        else:
            iExtraCount = iNowCount + iMinCount - oTargetState.m_MaxCount
            oTargetState.AddCount(oTargetMonster, iNowCount, iAddFrame)
        if iExtraCount > 0:
            oPerform = oAttacker.GetPerform(dInfo['ExtraPerform'])
            if not oPerform:
                return None
            dData = {
                'LifeCycle': oLifeCycle }
            iExtraAttBase = cl_formula.GetResultByData(oTarget, dInfo['Att'], dData)
            iExtraAttRatio = cl_formula.GetResultByData(oAttacker, dInfo['ExtraAttRatio'], dData)
            dPerform = {
                'Custom': {
                    'Att': iExtraAttBase * iExtraAttRatio * iExtraCount // 100 },
                'VID': oTargetMonster.m_ID }
            cl_war.UseOnlyServerPerform(oTarget, oPerform, dPerform)
        else:
            oState = AddFogPoisonState(oAttacker, oTargetMonster, oState.GetPerformID(), iAddFrame, sReason = oState.Reason())
            if oState:
                oState.AddCount(oTarget, iNowCount, iAddFrame)


def CustomAction39735(oWarrior, oEventCB, dInfo):
    oState = oEventCB.GetObject()
    iAttack = oState.m_Attacker
    oAttack = oWarrior.m_Game.GetObject(iAttack, PY_FLAG_DEAD)
    if not oAttack or not (oAttack.m_BackpackCon):
        return None
    oWeapon = oAttack.m_WieldCon.GetCurWeapon(MAIN_HOLD)
    if not oWeapon:
        return None
    iPerformSID = dInfo['PerformSID']
    oPerform2 = oAttack.GetPerformIfNoThenNew(iPerformSID)
    if not oPerform2:
        return None
    iTargetPerform = dInfo['iTargetPerform']
    lCandidates = []
    for dPerform in oAttack.m_BackpackCon.m_Perform.values():
        if iTargetPerform in dPerform:
            lCandidates.append(dPerform[iTargetPerform])
    
    if not lCandidates:
        return None
    oPerform = max(lCandidates, key = (lambda p: p[0]))[1]
    iDamage = oPerform.GetArgValue('DamRatio') // 100
    dData = {
        'Dam': iDamage,
        'UseTrajectory': 1 }
    dPerform = {
        'Custom': dData }
    dData['LockTarget'] = [
        oWarrior.m_ID]
    dPerform['VID'] = oWarrior.m_ID
    dData['LockTrigger'] = oWarrior.m_ID
    cl_war.UsePerform(oAttack, oPerform2, dPerform)
    sKey = str(iTargetPerform) + 'CDMark'
    iFrame = Time2Frame(dInfo['CDTime'])
    iNowFrame = oWarrior.m_Game.GetFrameNum()
    dMarkCDInfo = oWarrior.SetDefault(sKey, { })
    dMarkCDInfo[iAttack] = (iNowFrame, iFrame)
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CUSTOMSTATECOUNTCHANGE, oAttack, {
        'StateSID': oState.m_SID,
        'Count': oState.GetCount(),
        'VID': oWarrior.m_ID })


def CheckInImmobilizeOrSneer(oTarget, iToleranceTime):
    if oTarget.Query('Sneer') or oTarget.Query('Immobilize'):
        return 1
    iSneerFrame = oTarget.Query('SneerCDMark', 0)
    iImmobilizeFrame = oTarget.Query('ImmobilizeCDMark', 0)
    iTargetFrame = oTarget.m_Game.GetFrameNum() - Time2Frame(iToleranceTime)
    if iSneerFrame >= iTargetFrame or iImmobilizeFrame >= iTargetFrame:
        return 1
    return 0


def CustomAction51668(oWarrior, oEventCB, dData):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'CurVID' not in dMsgInfo:
        return None
    iTarget = dMsgInfo['CurVID']
    oGame = oWarrior.m_Game
    if not oGame:
        return None
    oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
    if not oTarget or not (oTarget.m_FightType & WARRIOR_MONSTER):
        return None
    if not CheckInImmobilizeOrSneer(oTarget, 150):
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iExtraDamRatio = cl_formula.GetResultByData(oWarrior, dData['ExtraDamRatio'], dEventInfo, dMsgInfo)
    iTrueExtraDamRatio = 0
    if iExtraDamRatio:
        sKey = oEventCB.m_Key
        tLastFrame = oTarget.Query(sKey, (0, 0))
        iImmobilizeFrame = oTarget.Query('ImmobilizeCDMark', 0)
        iSneerFrame = oTarget.Query('SneerCDMark', 0)
        if tLastFrame != (iImmobilizeFrame, iSneerFrame):
            iTrueExtraDamRatio = iExtraDamRatio
            oTarget.Set(sKey, (iImmobilizeFrame, iSneerFrame))
    iDamRatio = cl_formula.GetResultByData(oWarrior, dData['DamRatio'], dEventInfo, dMsgInfo)
    sKey = oEventCB.m_Key
    dMsgInfo['DamFactor'][OBJ_ATTACK][sKey] = (0, iDamRatio + iTrueExtraDamRatio, 0)


def CustomAction8169_0(oTarget, oLifeCycle, dInfo):
    oGame = oTarget.m_Game
    if not oGame:
        return None
    iSummon = oLifeCycle.m_Owner.GetArgValue('LimitMoveSummon')
    oSummon = oGame.GetObject(iSummon)
    if not oSummon:
        return None
    tCenter = oSummon.GetPos()
    fRadius = oSummon.QueryAttr('HitRange')
    oGame.SetLimitMove(oTarget.m_ID, tCenter, fRadius)


def CustomAction8169_1(oTarget, oLifeCycle, dInfo):
    oGame = oTarget.m_Game
    if not oGame:
        return None
    oGame.UnsetLimitMove(oTarget.m_ID)


def CustomAction39760(oWarrior, oEventCB, dData):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo or not dTransInfo['TargetList']:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    oGame = oWarrior.m_Game
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iTarget = dTransInfo['TargetList'][0]
    oTarget = oGame.GetObject(iTarget)
    iVal = 0
    if oTarget:
        oOwner = oGame.GetObject(oTarget.m_Owner)
        if oOwner:
            iHPSum = oOwner.HP() + oOwner.Shield() + oOwner.Armor()
            iBossHPRate = cl_formula.GetResultByData(oWarrior, dData['BossHP'], dEventInfo, dMsgInfo)
            iRate = 100 + cl_formula.GetResultByData(oWarrior, dData['Rate'], dEventInfo, dMsgInfo)
            iVal = int(iHPSum * iBossHPRate * iRate / 1000000)
    oLifeCycle = dEventInfo['LifeCycle']
    oState = oLifeCycle.GetObject()
    oState.m_Data[dData['Key']] = iVal

