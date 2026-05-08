# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_action/ac_pfative.pyc
# RelativePath: clientlogic/cl_action/ac_pfative.pyc
# Source Generated with Decompyle++
# File: ac_pfative.pyc (Python 3.6)

from cl_only import PY_FLAG_SERVANTTARGET, Functor, Frame2Time, Time2Frame, GAME_FRAME, ChooseKey, PY_FLAG_DEAD, SendAlert, GetRandomCard, CELL_SPACESIZE, CELL_REC, CTRL_FLAG_FOR_ALL, ShufferList, GAME_FRAME_INF, CopyDict, PY_FLAG_NONE, PY_FLAG_EXCLUDEMONSTERHATE, GAME_FRAME_SECOND
from cl_commondefines import DAM_TYPE_FIRE, DAM_TYPE_THUNDER, DAM_TYPE_CORRISION, DAM_TYPE_ELEMENT, FIGHT3_KEY_IGNELBEEXECUTED, TYPE_RELIFE_PASSIVE, BASEATTR_REFRESH, CRT_CHECK_SERVER, MONSTERAI_TYPE_DEFAULT, FAR_DISTANCE, MIDDLE_DISTANCE, DAM_TYPE_SCENE, MODEL_TYPE_BOX, WARRIOR_STONEPILLAR, GetPlayMode, CLOSE_DISTANCE, ATT_SHAPE_SPHERE, MODEL_TYPE_CAPSULE, MODEL_TYPE_SPHERE, MONSTERAI_TYPE_HATESEARCH, PARAM_LEVEL_MEDIUM_HIGH, WARRIOR_MONSTERBEACON, MODEL_TYPE_POINT, WARRIOR_BEACON, WARRIOR_BUILD, WARRIOR_BOSSCANNON, WARRIOR_OBSTACLE_SIMCTRL, DAM_TYPE_TRUE, DAM_MASK_ELEMENT, TYPE_RELIFE_PF, STATE_DYING, WARRIOR_SUMMON, SIDE_TYPE_MONSTER, SCENE_EVT_SHAPE_RECTANGLE, SCENE_EVT_SHAPE_SPHERE, PF_TYPE_BULLETCHANGE, FIGHT3_KEY_IGNOREKNOCKBACK, WARRIOR_HERO, WARRIOR_MONSTER, MONSTER_PART_SHIELD, DAM_USE_HP, WARRIOR_ELITE, DAM_USE_ARMOR, WARRIOR_BOSS, DAM_USE_SHIELD, DAM_TYPE_FRIEND, MISSING_DIS_EASY, MISSING_DIS_HARD, MISSING_DIS_NORMAL, STATE_TIME_LIMIT, STATE_TIME_FOREVER, DAM_USE_ALL, CURE_TYPE_PERFORM, OBJ_VICTIM, OBJ_ATTACK, DAM_TYPE_NORMAL, NWARRIOR_DROP_KEYITEM, PF_TYPE_SHOOT, PF_TYPE_CONSHOOT, PF_TYPE_CHARGE
from cl_commondefines import MONSERT_PART_ALLWEAKNESS, OBJ_ENEMY, DAM_TYPE_PERFORM, WARRIOR_SERVANT, SKILLCACHE_LSTINT, VICTIM_IGNORE_ALL, VICTIM_IGNORE_ONCE, FLAW_ISWEAKNESS, EXECUTOR_HERO, KILL_DAMAGE, INKMASTER_HERO, DIE_PRIORITY_KILL, EXECUTETYPE_ACTIVEPF, PAMOD_TYPE_DYNA
from cl_commondefines import SKILLCACHE_PARENTACTNUM, CRT_CHECK_CLIENT, EXTRA_THROW_PERFORM, PATHMODE_COLLISIONLESS, SKILLCACHE_LSTPOS, WARRIOR_SUMMON_SEED, GARDENER_HERO, WARRIOR_PLANT, TRIGGER_PARASITIC
from cl_commondefines import PLANT_PHASE_TREE, PLANT_PHASE_NORMAL
from cl_cscommondef import DEBUG_STATUS_NOPFCD
from cl_object.logging import SkillLog, WarobjLog, OtherLog
from cl_pxlayer import PXMASK_MOVEBLK, PXMASK_BLOCK, PXMASK_LIVEOBJ, PXMASK_OBJECT, PXMASK_SKILLBLK, PXMASK_MONSTER, PXMASK_SIGHTBLK, PXMASK_GROUNDBLK, PXLAYER_MONSTER, PXMASK_PLAYER
from cl_evact import CheckWeaponType2, TargetAddLionLockState, LionLockStateSearchEnemy
from cl_platformdata import GetGardenerAimThrowRadius, GetGardenerAimThrowElementType, GetGardenerAimThrowCreateMonsterInfo
import math
import functools
import cl_war
import cl_snetwar
import cl_formula
import cl_newformula
import cl_state
import cl_math
import cl_notify
import cl_gamedebug as debug
import cl_modeldefine
import cl_perform
import cl_perform.net
import cl_perform.skillcache
import cl_attachctrl
import cl_object
import cl_item
import cl_action
import cl_behavior
import cl_forbid
import cl_msgcenter
import cl_engphyobj

def PerformDamage(oSkill, dPerformArgs, dArgs = None):
    oGame = oSkill.m_Game
    iTarget = oSkill.m_Update['CurVID']
    oVictim = oGame.GetObject(iTarget, PY_FLAG_DEAD)
    if not oVictim:
        return None
    if not dArgs:
        dArgs = { }
    iAttack = oSkill.m_Base['AID']
    iElementType = oSkill.m_Cache['ElementType'] if 'ElementType' in oSkill.m_Cache else DAM_TYPE_NORMAL
    if 'TransmitAtt' in oSkill.m_Custom:
        iBaseDam = oSkill.m_Custom['TransmitAtt']
    elif 'ComAtt' in dPerformArgs:
        iBaseDam = oSkill.m_Cache['ComAtt'] * dPerformArgs['ComAtt'] // 100
    else:
        iBaseDam = dPerformArgs['Att']
    iBaseDam = int(iBaseDam)
    dBuffAttr = GetPFBuff(oSkill)
    if 'Att' in dBuffAttr:
        iBaseDam = iBaseDam * (100 + dBuffAttr['Att']) // 100
    lstMainDam = cl_formula.CalPerformDamage(oVictim, oSkill, iBaseDam, iElementType, dArgs)
    oSkill.m_Update[iTarget] = {
        'MainDam': [
            lstMainDam],
        'RS': lstMainDam[1] }
    oVictim.ReceivePerform(iAttack, oSkill)


def GetRelicGrade(oSkill, iRelic):
    oGame = oSkill.m_Game
    iTarget = oSkill.m_Base['AID']
    oAttack = oGame.GetObject(iTarget, PY_FLAG_DEAD)
    if not oAttack:
        return 0
    oPerform = oAttack.m_RelicCon.GetPerform(iRelic)
    if not oPerform:
        return 0
    return oPerform.GetLifeCycleLevel()


def WeaponDamage(oSkill, dWeaponArgs, dArgs, sendPFMsg = False):
    bExplosion = sendPFMsg
    oGame = oSkill.m_Game
    iTarget = oSkill.m_Update['CurVID']
    oVictim = oGame.GetObject(iTarget, PY_FLAG_DEAD)
    if not oVictim:
        return None
    dBuffAttr = GetPFBuff(oSkill)
    for sAttr, iMul in dBuffAttr.items():
        if sAttr in dWeaponArgs:
            dWeaponArgs[sAttr] = dWeaponArgs[sAttr] * (100 + iMul) // 100
    
    iSubTrajectory = dArgs['SubTrajectory'] if 'SubTrajectory' in dArgs else 0
    iExtCrazyEff = dArgs['CrazyEff'] if 'CrazyEff' in dArgs else 0
    iWeapon = dArgs['Weapon'] if 'Weapon' in dArgs else 0
    dCopyWeaponArgs = { }
    if 'CopyWeapon' in oSkill.m_Collect:
        dCopyWeapon = oSkill.m_Collect['CopyWeapon']
        dCurCartoon = oSkill.GetCurCartoon()
        if dCurCartoon:
            iCurCartoon = dCurCartoon['ID']
            dCopyCartoon = dCopyWeapon['CopyCartoon']
            if (iCurCartoon not in dCopyCartoon or 'ExtraCopy' in dArgs) and dArgs['ExtraCopy']:
                dCopyCartoon[iCurCartoon] = 1
                if oGame.Random(10000) < dCopyWeapon['CalProbability']:
                    dCopyWeaponArgs = dCopyWeapon['CopyArgs']
    (iBaseMainDam, oReason) = cl_formula.CalWeaponDamage(oVictim, oSkill, dWeaponArgs, dArgs, dCopyWeaponArgs)
    iCrazyEff = oSkill.m_Cache['CrazyEff']
    if iExtCrazyEff and iWeapon:
        clsWeapon = cl_item.GetItemCls(int(iWeapon))
        if clsWeapon:
            iChangeCrazyEff = iCrazyEff - clsWeapon.m_ItemAttr['CrazyEff']
            iCrazyEff = iExtCrazyEff + iChangeCrazyEff
    if 'CrazyEff' in dBuffAttr:
        iCrazyEff = iCrazyEff * (100 + dBuffAttr['CrazyEff']) // 100
    iLuckyHit = oSkill.m_Cache['LuckyHit'] if 'LuckyHit' in oSkill.m_Cache else 0
    if 'LuckyHit' in dBuffAttr:
        iLuckyHit += dBuffAttr['LuckyHit']
    oSkill.m_Update[iTarget] = {
        'MainDam': [
            [
                iBaseMainDam,
                oReason]],
        'CrazyEff': iCrazyEff,
        'LuckyHit': iLuckyHit,
        'RS': oReason }
    iAttack = oSkill.m_Base['AID']
    oVictim.ReceiveAttack(iAttack, oSkill, bExplosion, iSubTrajectory)
    if dCopyWeaponArgs:
        oCopyReason = oReason.ExtInfo({
            'CopyWeapon': 1 })
        oSkill.m_Update[iTarget]['MainDam'] = [
            [
                iBaseMainDam,
                oCopyReason]]
        oSkill.m_Update[iTarget]['RS'] = oCopyReason
        oVictim.ReceiveAttack(iAttack, oSkill, bExplosion, iSubTrajectory)


def GetPFBuff(oSkill):
    dBuffAttr = { }
    iTarget = oSkill.m_Update['CurVID']
    if 'PFBuff' in oSkill.m_Update:
        dBuff = oSkill.m_Update['PFBuff']
        lstBuff = dBuff[iTarget] if iTarget in dBuff else []
        for iBuffSourceID in lstBuff:
            oBuff = oSkill.m_Game.GetObject(iBuffSourceID)
            if oBuff:
                dBuffData = oBuff.GetBuffData()
                for sAttr in dBuffData:
                    iOld = dBuffAttr[sAttr] if sAttr in dBuffAttr else 0
                    dBuffAttr[sAttr] = iOld + dBuffData[sAttr]
                
        
    if 'ServantPFBuff' in oSkill.m_Custom:
        oAttack = oSkill.GetAttack()
        if oAttack and oAttack.m_FightType & WARRIOR_SERVANT:
            oOwner = oAttack.GetOwner()
            oDevice = oOwner.GetDevice()
            if oDevice:
                dBuffData = oDevice.GetBuffData()
                for sAttr in dBuffData:
                    iOld = dBuffAttr[sAttr] if sAttr in dBuffAttr else 0
                    dBuffAttr[sAttr] = iOld + dBuffData[sAttr]
                
            elif 'PassCrtBuff' in oSkill.m_Custom:
                lstBuff = oSkill.m_Custom['PassCrtBuff']
                for iBuffSourceID in lstBuff:
                    oBuff = oSkill.m_Game.GetObject(iBuffSourceID)
                    if oBuff:
                        dBuffData = oBuff.GetBuffData()
                        for sAttr in dBuffData:
                            iOld = dBuffAttr[sAttr] if sAttr in dBuffAttr else 0
                            dBuffAttr[sAttr] = iOld + dBuffData[sAttr]
                        
                
    return dBuffAttr


def TriggerEleAbnormal(oSkill, iDam, iElementType, AbnormalTime = 0):
    oGame = oSkill.m_Game
    iTarget = oSkill.m_Update['CurVID']
    oVictim = oGame.GetObject(iTarget, PY_FLAG_DEAD)
    if not oVictim:
        return None
    oReason = oSkill.m_Base['RS'].ExtInfo({
        'DamType': iElementType })
    oVictim.m_EleAbnormal.TryTriggerEleAbnormal(oSkill, iDam, oReason, AbnormalTime)


def SelfDamage(oSkill, iBaseDam, iDamSrc, iDamUse, iDamElement, iSendMsg):
    oGame = oSkill.m_Game
    iAttack = oSkill.m_Base['AID']
    oAttack = oGame.GetObject(iAttack, PY_FLAG_DEAD)
    if not oAttack:
        return None
    iDamType = iDamSrc | iDamUse | iDamElement | DAM_TYPE_FRIEND
    oReason = oSkill.m_Base['RS'].ExtInfo({
        'DamType': iDamType })
    dDamage = {
        'MainDam': [
            (iBaseDam, oReason)],
        'CurVID': iAttack,
        'FlowDam': [],
        'RS': oReason,
        'DamFactor': {
            OBJ_VICTIM: { },
            OBJ_ATTACK: { } } }
    oAttack.ReceiveDamage(iAttack, dDamage, iSendMsg)


def PerformCure(oSkill, iBaseCure, iPointTarget = 0):
    oGame = oSkill.m_Game
    iTarget = oSkill.m_Update['CurVID'] if not iPointTarget else iPointTarget
    oVictim = oGame.GetObject(iTarget, PY_FLAG_DEAD)
    if not oVictim:
        return None
    iType = CURE_TYPE_PERFORM | DAM_USE_ALL
    oReason = oSkill.m_Base['RS'].ExtInfo({
        'DamType': iType })
    dCure = {
        'MainCure': [
            [
                iBaseCure,
                oReason]],
        'FlowCure': [],
        'RS': oReason }
    oVictim.ReceiveCure(oSkill.m_Base['AID'], dCure)


def AttackerRemoveSelf(oSkill):
    oAttack = oSkill.GetAttack()
    if oAttack:
        oAttack.Remove('Skill')


def AttackerAddState(oSkill, iState, iTime, iWithPF, dArgs):
    if not oSkill.m_Base:
        return None
    TargetAddState(oSkill, iState, iTime, iWithPF, dArgs, oSkill.m_Base['AID'])


def AttackerRemoveState(oSkill, iState, bSameItem = False):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    if bSameItem:
        iItem = oSkill.m_Base['Weapon']
        lstState = oAttack.m_State.GetItems(iState)
        for oState in lstState:
            iStateItem = oState.m_Reason.Query('Item', 0)
            if iStateItem and iStateItem == iItem:
                oAttack.m_State.RemoveItem(oState.m_ID)
                break
        
    else:
        cl_state.RemoveState(oAttack, iState)


def VictimAddState(oSkill, iState, iTime, iWithPF, dArgs):
    if 'CurVID' in oSkill.m_Update:
        iTarget = oSkill.m_Update['CurVID']
    else:
        iTarget = oSkill.m_Base['VID']
    TargetAddState(oSkill, iState, iTime, iWithPF, dArgs, iTarget)


def VictimAddStateByObject(oSkill, iState, iTime, iWithPF, dArgs):
    if 'CurVID' in oSkill.m_Update:
        iTarget = oSkill.m_Update['CurVID']
    else:
        iTarget = oSkill.m_Base['VID']
    TargetAddState(oSkill, iState, iTime, iWithPF, dArgs, iTarget)


def TargetAddState(oSkill, iState, iTime, iWithPF, dArgs, iTarget):
    if iTime < 0:
        return None
    oTarget = oSkill.m_Game.GetObject(iTarget)
    if not oTarget:
        return None
    if 'Cache' in dArgs:
        dArgs['Cache'] = { }
        dArgs['Cache'].update(oSkill.m_Cache)
    oReason = oSkill.m_Base['RS'].ExtInfo({
        'ActNum': 0 })
    dData = {
        'AID': dArgs['AID'] if 'AID' in dArgs else oSkill.m_Base['AID'],
        'RS': oReason,
        'arg': dArgs,
        'pfid': oSkill.m_Base['pfid'],
        'PFLV': oSkill.m_Base['PFLV'],
        'ActNum': oSkill.m_Base['ActNum'] }
    if oSkill.m_Cache and 'Att' in oSkill.m_Cache:
        dData['Att'] = oSkill.m_Cache['Att']
    if iTime:
        iTimeType = STATE_TIME_LIMIT
        iTime = Time2Frame(iTime)
    else:
        iTimeType = STATE_TIME_FOREVER
    oState = cl_state.AddState(oTarget, iState, iTimeType, iTime, dData)
    if oState:
        oState.Enable(oTarget)
        if iWithPF:
            oSkill.AddEndFunc(Functor(ClearWithPFState, iTarget, oState.m_ID))
        sKey = 'pf%d_State' % oSkill.m_Base['pfid']
        dPFState = oSkill.m_Collect.setdefault(sKey, { })
        dPFState[oState.m_SID] = oState.m_ID
        dPFAddState = oSkill.m_Update.setdefault('PFAddState', { })
        dPFTargetAddState = dPFAddState.setdefault(iState, { })
        dPFTargetAddState[iTarget] = oState.m_ID
    return oState


def TargetRemoveState(oSkill, iState, iTarget):
    oTarget = oSkill.m_Game.GetObject(iTarget)
    if not oTarget:
        return None
    cl_state.RemoveState(oTarget, iState)


def ClearWithPFState(iTarget, iState, oSkill):
    oTarget = oSkill.m_Game.GetObject(iTarget)
    if not oTarget:
        return None
    oTarget.m_State.RemoveItem(iState)


def RemoveSelfState(oSkill, iState):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oState = oAttack.m_State.GetItemBySID(iState)
    if oState:
        oAttack.m_State.RemoveItem(oState.m_ID)


def GetAttackerStateCount(oSkill, iStateSID, dState = None):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return 0
    if not dState:
        dState = { }
    if iStateSID in dState:
        oState = oAttack.m_State.GetItem(dState[iStateSID])
    else:
        oState = oAttack.m_State.GetItemBySID(iStateSID)
    if oState:
        return oState.GetCount()
    return 0


def GetTargetStateCount(oSkill, iStateSID, iTarget, bFromSelf, bFromAttack = False, bFromWeapon = False):
    if bFromSelf and bFromAttack:
        SendAlert('err', '技能%d GetTargetStateCounte状态获取条件冲突' % oSkill.m_Base['pfid'])
        return 0
    oTarget = oSkill.m_Game.GetObject(iTarget)
    if not oTarget:
        return 0
    iCheckID = 0
    if bFromSelf:
        iCheckID = oTarget.m_ID
    elif bFromAttack:
        iCheckID = oSkill.m_Base['AID']
    if iCheckID:
        lstState = oTarget.m_State.GetItems(iStateSID)
        if not lstState:
            return 0
        for oState in lstState:
            if iCheckID != oState.m_Attacker:
                continue
            return oState.GetCount()
        
        return 0
    if bFromWeapon:
        iItem = oSkill.m_Base['Weapon']
        lstState = oTarget.m_State.GetItems(iStateSID)
        for oState in lstState:
            oReason = oState.m_Reason
            iStateItem = oReason.Query('Item', 0)
            if iStateItem and iStateItem == iItem:
                return oState.GetCount()
        
        return 0
    oState = oTarget.m_State.GetItemBySID(iStateSID)
    if oState:
        return oState.GetCount()
    return 0


def SetAttackerStateCount(oSkill, iStateSID, iCount):
    iCount = int(iCount)
    if iCount < 0:
        return None
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oState = oAttack.m_State.GetItemBySID(iStateSID)
    if not oState:
        return None
    oState.SetCount(oAttack, iCount)


def AddAttackerStateCount(oSkill, iStateSID, iAdd, iTime = 0, bFromAttack = False, bFromWeapon = False):
    iAdd = int(iAdd)
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    iAttack = oAttack.m_ID if bFromAttack else 0
    iItem = oSkill.m_Base['Weapon'] if bFromWeapon else 0
    oState = oAttack.m_State.GetStateBySource(iStateSID, iAttack, iItem)
    if not oState:
        return None
    if iTime:
        oState.AddCount(oAttack, iAdd, Time2Frame(iTime))
    else:
        oState.AddCount(oAttack, iAdd)


def AddFromAttackerStateCount(oSkill, iStateSID, iAdd, iTime = 0):
    if 'CurVID' in oSkill.m_Update:
        iTarget = oSkill.m_Update['CurVID']
    else:
        iTarget = oSkill.m_Base['VID']
    oTarget = oSkill.m_Game.GetObject(iTarget)
    if not oTarget:
        return None
    iAttack = oSkill.m_Base['AID']
    if not iAttack:
        return None
    oState = oTarget.m_State.GetItemBySource(iStateSID, iAttack)
    if not oState:
        return None
    iAdd = int(iAdd)
    if iTime:
        oState.AddCount(oTarget, iAdd, Time2Frame(iTime))
    else:
        oState.AddCount(oTarget, iAdd)


def SetAttackerStateArgValue(oSkill, iStateSID, sKey, iSet):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oState = oAttack.m_State.GetItemBySID(iStateSID)
    if not oState:
        return None
    oState.SetArgValue(sKey, iSet)


def CrtArgSightAccPos(oSkill, dCartoon):
    return GetAimTargetPosition(oSkill, dCartoon)


def CrtArgSightCentrePos(oSkill, dCartoon):
    return GetSceneCenterPosition(oSkill, dCartoon)


def GetAimTargetPosition(oSkill, dCartoon):
    vEnd = oSkill.m_Base['vEnd']
    return vEnd


def GetSceneCenterPosition(oSkill, dCartoon):
    vEnd = oSkill.m_Base['vEnd']
    return vEnd


def CrtArgSightDefaultDis(oSkill, iMax):
    return 0


def CrtArgSightCentrePosByDis(oSkill, iInner, iOutside, iDis):
    return GetSpherePointByRay(oSkill, iInner, iOutside, iDis)


def GetSpherePointByRay(oSkill, iInner, iOutside, iDis):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return oSkill.m_Base['vEnd']
    vPos = oAttack.GetPos()
    vPos = cl_math.Vec3Add(vPos, (0, oAttack.m_ModelHeight * 0.85, 0))
    vDir = oAttack.GetFacing()
    vTarget = cl_math.Vec3DisplaceDir(vPos, vDir, iDis)
    return vTarget


def CrtArgBodyPos(oSkill, fRange, fLower = 0, iCalShift = 0, iExtShiftProb = 0):
    iVictim = oSkill.m_Base['VID']
    oGame = oSkill.m_Game
    oVictim = oGame.GetObject(iVictim, PY_FLAG_DEAD)
    if oVictim:
        oAttack = oSkill.GetAttack()
        vPos = oVictim.GetPos()
        if iCalShift:
            iProb = 100 + iExtShiftProb - oAttack.QueryAttr('AccuracyProb')
            iShift = 0 if oGame.Random(100) >= iProb else 1
        else:
            iShift = 1
        if iShift and fRange > 0 and fRange > fLower:
            iRange = int((fRange - fLower) * CELL_SPACESIZE) - 1
            fDispR = (oGame.Random(iRange) + 1) * CELL_REC + fLower
            fDispR = -fDispR if oGame.Random(2) else fDispR
            fDispH = (oGame.Random(iRange) + 1) * CELL_REC + fLower
            fDispH = -fDispH if oGame.Random(2) else fDispH
            vStart = oAttack.GetPos()
            if vPos[0] == vStart[0] and vPos[2] == vStart[2]:
                x = vPos[0]
                z = vPos[2]
                SkillLog.Debug('pf%d victim:%d  attack:%d victimpos:%s attackpos:%s 攻击者和受害者x,z位置相同' % (oSkill.m_Base['pfid'], iVictim, oAttack.m_ID, vPos, vStart))
            else:
                (x, z) = cl_math.Vec2DisplaceDir((vPos[0], vPos[2]), (-(vPos[2] - vStart[2]), vPos[0] - vStart[0]), fDispR)
            vEnd = (x, vPos[1] + oVictim.m_ModelHeight * 0.8 + fDispH, z)
        else:
            vEnd = (vPos[0], vPos[1] + oVictim.m_ModelHeight * 0.85, vPos[2])
    else:
        vEnd = oSkill.m_Base['vEnd']
    return vEnd


def CrtArgTargetBodyShiftPos(oSkill, iCalShift, iExtShiftProb, fMinDis, fMaxDis, fMinX, fMaxX, fMinY, fMaxY):
    iVictim = oSkill.m_Base['VID']
    oGame = oSkill.m_Game
    oAttack = oSkill.GetAttack()
    oVictim = oGame.GetObject(iVictim, PY_FLAG_DEAD)
    if oAttack and oVictim:
        vPos = oVictim.GetPos()
        vStart = oAttack.GetPos()
        if iCalShift:
            iProb = 100 + iExtShiftProb - oAttack.QueryAttr('AccuracyProb')
            iShift = 0 if oGame.Random(100) >= iProb else 1
        else:
            iShift = 1
        if iShift and fMinDis < fMaxDis and fMinX <= fMaxX and fMinY <= fMaxY and not cl_math.IsPlaneEqual(vPos, vStart):
            fDis = cl_math.CalDistance3D(vPos, vStart)
            if fDis <= fMinDis:
                fRangeX = fMinX
                fRangeY = fMinY
            elif fDis >= fMaxDis:
                fRangeX = fMaxX
                fRangeY = fMaxY
            else:
                fRangeX = fMinX + (fDis - fMinDis) * (fMaxX - fMinX) / (fMaxDis - fMinDis)
                fRangeY = fMinY + (fDis - fMinDis) * (fMaxY - fMinY) / (fMaxDis - fMinDis)
            fDispR = oGame.Random(int(fRangeX * CELL_SPACESIZE)) * CELL_REC
            fDispR = -fDispR if oGame.Random(2) else fDispR
            fDispH = oGame.Random(int(fRangeY * CELL_SPACESIZE)) * CELL_REC
            fDispH = -fDispH if oGame.Random(2) else fDispH
            (x, z) = cl_math.Vec2DisplaceDir((vPos[0], vPos[2]), (-(vPos[2] - vStart[2]), vPos[0] - vStart[0]), fDispR)
            vEnd = (x, vPos[1] + oVictim.m_ModelHeight * 0.8 + fDispH, z)
        else:
            vEnd = (vPos[0], vPos[1] + oVictim.m_ModelHeight * 0.85, vPos[2])
    else:
        vEnd = oSkill.m_Base['vEnd']
    return vEnd

g_NormalMissingDis = {
    5: 2,
    6: 4,
    7: 6,
    8: 8,
    9: 12,
    10: 18,
    11: 18,
    12: 12,
    13: 8,
    14: 6,
    15: 4,
    16: 2 }
g_HardMissingDis = {
    4: 4,
    5: 8,
    6: 12,
    7: 17,
    8: 16,
    9: 13,
    10: 9,
    11: 8,
    12: 7,
    13: 4,
    14: 2 }
g_EasyMissingDis = {
    8: 2,
    9: 4,
    10: 7,
    11: 8,
    12: 9,
    13: 13,
    14: 16,
    15: 17,
    16: 12,
    17: 8,
    18: 4 }
g_MissingOffset = {
    MISSING_DIS_EASY: 0.2,
    MISSING_DIS_NORMAL: 0.2,
    MISSING_DIS_HARD: 0.2 }
g_MissingDis = {
    MISSING_DIS_EASY: g_EasyMissingDis,
    MISSING_DIS_NORMAL: g_NormalMissingDis,
    MISSING_DIS_HARD: g_HardMissingDis }

def CrtArgMissingPos(oSkill, fYRatio, *args):
    iVictim = oSkill.m_Base['VID']
    oGame = oSkill.m_Game
    oAttack = oSkill.GetAttack()
    oVictim = oGame.GetObject(iVictim, PY_FLAG_DEAD)
    if oAttack and oVictim:
        vPos = oVictim.GetPos()
        iBase = oAttack.QueryAttr('AccuracyProb')
        iCurFrame = oGame.GetFrameNum()
        dMoveDistance = oVictim.Query('RecentMoveDis', { })
        fDis = 0
        iTotalFrame = GAME_FRAME
        for iFrame in range(iCurFrame, iCurFrame - iTotalFrame - 1, -1):
            if iFrame not in dMoveDistance:
                if iFrame <= iCurFrame - 15:
                    iTotalFrame = iCurFrame - iFrame - 1
                    break
                if len(dMoveDistance) > 100:
                    dMoveDistance.clear()
                fFrameMove = cl_math.CalDistance3D(oGame.GetLastPos(iVictim, iFrame), oGame.GetLastPos(iVictim, iFrame - 1))
                dMoveDistance[iFrame] = fFrameMove
            fDis += dMoveDistance[iFrame]
        
        oVictim.Set('RecentMoveDis', dMoveDistance)
        fSpeed = (fDis / iTotalFrame) * GAME_FRAME
        iRound = oGame.m_WarMgr.m_Round
        fTotal = iBase - max(0, fSpeed * 100 - 300) * oAttack.m_AccuracyFactor / (15 * iRound * 0.5)
        if oGame.Random(100) > fTotal:
            iMissingDisType = oAttack.m_MissingDisType[iRound]
            fTypeOffset = g_MissingOffset[iMissingDisType]
            dTypeDis = g_MissingDis[iMissingDisType]
            iMissingIndex = ChooseKey(oGame, dTypeDis)
            fMin = max(0, (iMissingIndex - 0.5) * fTypeOffset)
            fMax = (iMissingIndex + 0.5) * fTypeOffset
            iRange = int((fMax - fMin) * CELL_SPACESIZE) - 1
            fDisp = (oGame.Random(iRange) + 1) * CELL_REC + fMin
            fDisp = -fDisp if oGame.Random(2) else fDisp
            vStart = oAttack.GetPos()
            if not cl_math.IsPlaneEqual(vPos, vStart):
                (x, z) = cl_math.Vec2DisplaceDir((vPos[0], vPos[2]), (-(vPos[2] - vStart[2]), vPos[0] - vStart[0]), fDisp)
            else:
                lstState = [ oState.m_SID for oState in oAttack.m_State.Values() ]
                iLastHate = 0
                dHate = { }
                oAgent = oAttack.m_Agent
                sTree = ''
                if oAgent:
                    iLastHate = oAgent.GetData('LastEnemyHate', 0)
                    dHate = oAgent.GetData('HateData', { })
                    oCurrentBT = oAgent.PYGetCurrentBT()
                    sTree = oCurrentBT.GetPathName() if oCurrentBT else ''
                oScene = oGame.m_SceneMgr.GetScene(oAttack.m_Scene)
                iLevel = oScene.m_Level if oScene else 0
                WarobjLog.Alert('%d %d %s attack%d-%s victim%d-%s-%d place same pos %s %s %s %s %s %s' % (oGame.m_ID, iLevel, oSkill.m_Base['pfid'], oAttack.m_SID, oAttack.m_ID, oVictim.m_SID, iVictim, oVictim.m_PlayerID, vStart, vPos, lstState, iLastHate, dHate, sTree))
                vDir = oVictim.GetFacing()
                if not vDir[0] and not vDir[2]:
                    x = vPos[0]
                    z = vPos[2]
                else:
                    (x, z) = cl_math.Vec2DisplaceDir((vPos[0], vPos[2]), (-vDir[2], vDir[0]), fDisp)
            if fYRatio:
                y = fDisp * fYRatio if oGame.Random(2) else -fDisp * fYRatio
            else:
                y = 0
            vEnd = (x, vPos[1] + oVictim.m_ModelHeight * 0.8 + y, z)
        else:
            vEnd = (vPos[0], vPos[1] + oVictim.m_ModelHeight * 0.85, vPos[2])
    else:
        vEnd = oSkill.m_Base['vEnd']
    return vEnd


def CrtArgTargetPos(oSkill, notContainDying = False):
    iVictim = oSkill.m_Base['VID']
    if notContainDying:
        oVictim = oSkill.m_Game.GetObject(iVictim)
    else:
        oVictim = oSkill.m_Game.GetObject(iVictim, PY_FLAG_DEAD)
    if oVictim:
        vEnd = oVictim.GetPos()
    else:
        vEnd = oSkill.m_Base['vEnd']
    return vEnd


def CrtArgTargetGroundPos(oSkill):
    iVictim = oSkill.m_Base['VID']
    oVictim = oSkill.m_Game.GetObject(iVictim, PY_FLAG_DEAD)
    if oVictim:
        vEnd = oVictim.GetPos()
    else:
        vEnd = oSkill.m_Base['vEnd']
    vRet = oSkill.m_Game.Scene_RaycastSingle(oSkill.m_Base['Scene'], vEnd, cl_math.Vec3Add(vEnd, (0, -15, 0)), PXMASK_BLOCK)
    if vRet[0] != -1:
        return vRet[1]
    return vEnd


def CrtArgTargetPosGroudPos(oSkill, vPos):
    vRet = oSkill.m_Game.Scene_RaycastSingle(oSkill.m_Base['Scene'], vPos, cl_math.Vec3Add(vPos, (0, 5, 0)), PXMASK_BLOCK)
    if vRet[0] != -1:
        return vRet[1]
    return vPos


def CrtArgSelfPos(oSkill):
    iAttack = oSkill.m_Base['AID']
    oAttack = oSkill.m_Game.GetObject(iAttack, PY_FLAG_DEAD)
    if oAttack:
        vPos = oAttack.GetPos()
        vPos = (vPos[0], vPos[1] + 0.1, vPos[2])
    else:
        vPos = oSkill.m_Base['vStart']
    return vPos


def CrtArgSelfCenterPos(oSkill):
    iAttack = oSkill.m_Base['AID']
    oAttack = oSkill.m_Game.GetObject(iAttack, PY_FLAG_DEAD)
    if oAttack:
        vPos = oAttack.GetPos()
        vPos = (vPos[0], vPos[1] + oAttack.m_ModelHeight / 2, vPos[2])
    else:
        vPos = oSkill.m_Base['vStart']
    return vPos


def CrtArgSelfTopPos(oSkill):
    iAttack = oSkill.m_Base['AID']
    oAttack = oSkill.m_Game.GetObject(iAttack, PY_FLAG_DEAD)
    if oAttack:
        vPos = oAttack.GetPos()
        fFixedTopHeight = cl_modeldefine.GetModelDefine(oAttack.m_Shape, 'FixedTopHeight')
        vPos = (vPos[0], vPos[1] + oAttack.m_ModelHeight + fFixedTopHeight, vPos[2])
    else:
        vPos = oSkill.m_Base['vStart']
    return vPos


def CrtArgWarriorPos(oSkill, iWarrior):
    oTarget = oSkill.m_Game.GetObject(iWarrior)
    if oTarget:
        return oTarget.GetPos()
    return oSkill.m_Base['vEnd']


def SkillStartPos(oSkill):
    return oSkill.m_Base['vStart']


def CrtArgSkillEndPos(oSkill):
    return oSkill.m_Base['vEnd']


def SetSkillVarCache(oSkill, key, var):
    oSkill.m_VarCache[key] = var


def UpdateSkillWeaponSpecialAttr(oSkill, sKey, iAdd):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    iItem = oSkill.m_Base['Weapon']
    oWeapon = oAttack.m_WieldCon.GetItemByID(iItem)
    if not oWeapon:
        return None
    oWeapon.AddSpecialAttrBase(sKey, iAdd, iRefresh = 1)


def GetSkillVarCache(oSkill, key):
    if key not in oSkill.m_VarCache:
        SkillLog.Error('skill%d err, no %s cache' % (oSkill.m_Base['pfid'], key))
        return None
    return oSkill.m_VarCache[key]


def AddSkillVarCache(oSkill, key, iVal):
    if key not in oSkill.m_VarCache:
        oSkill.m_VarCache[key] = iVal
    else:
        oSkill.m_VarCache[key] += iVal


def AddSkillVarCacheList(oSkill, sKey, iVal):
    lstCacheData = oSkill.m_VarCache.setdefault(sKey, [])
    lstCacheData.append(iVal)


def PopSkillVarCache(oSkill, sKey):
    if sKey not in oSkill.m_VarCache:
        SkillLog.Error('skill%d err, no %s cache' % (oSkill.m_Base['pfid'], sKey))
        return 0
    lstNum = oSkill.m_VarCache[sKey]
    iResult = lstNum.pop() if lstNum else None
    return iResult


def CheckHasSkillVarCache(oSkill, key):
    return key in oSkill.m_VarCache


def DebugBox(oGame, vPos, fAngle, vOffset, vSize, vAngle, vSymmetry):
    lstPoint = []
    lstOffset = [
        (0, 0, 0),
        (0, 0, 1),
        (0, 1, 0),
        (0, 1, 1),
        (1, 0, 0),
        (1, 0, 1),
        (1, 1, 0),
        (1, 1, 1)]
    for vTmp in lstOffset:
        vTmp = cl_math.Vec3Minus(cl_math.Vec3MulF(vTmp, 2), (1, 1, 1))
        vTmp = cl_math.Vec3MulV(vTmp, cl_math.Vec3MulF(vSize, 0.5))
        vTmp = cl_math.GetOffsetWorldPos((0, 0, 0), vTmp, vAngle)
        vTmp = cl_math.Vec3Add(vTmp, vOffset)
        vTmp = cl_math.Vec3MulV(vTmp, vSymmetry)
        vTmp = cl_math.GetOffsetWorldPos((0, 0, 0), vTmp, (0, fAngle, 0))
        vPoint = cl_math.Vec3Add(vPos, vTmp)
        lstPoint.append(vPoint)
    
    debug.ClearDebugLine(oGame, debug.LINE_BOX)
    for i in range(len(lstPoint)):
        for j in range(i + 1, len(lstPoint)):
            vPoint1 = lstPoint[i]
            vPoint2 = lstPoint[j]
            debug.DebugLine(oGame, vPoint1[0], vPoint1[1], vPoint1[2], vPoint2[0], vPoint2[1], vPoint2[2], 65280, debug.LINE_BOX)
        
    


def CrtArgCalcRectangleRandomMuzzlePos(oSkill, dCartoon, vOffset, vSize, vAngle, vRandomSymmetry):
    oGame = oSkill.m_Game
    iAttack = oSkill.m_Base['AID']
    oAttack = oGame.GetObject(iAttack, PY_FLAG_DEAD)
    if oAttack:
        vPos = oAttack.GetPos()
        tFacing = oAttack.GetFacing()
    else:
        vPos = oSkill.m_Base['vStart']
        tFacing = cl_math.Vec3Minus(oSkill.m_Base['vEnd'], vPos)
    fAngle = cl_math.CalAngle2D((0, 0, -1), tFacing)
    if tFacing[0] > 0:
        fAngle = -fAngle
    vSymmetry = []
    for iSymmetry in vRandomSymmetry:
        if iSymmetry:
            vSymmetry.append(oGame.Random(2) * 2 - 1)
            continue
        vSymmetry.append(1)
    
    oWarMgr = oGame.GetWarMgr()
    if oWarMgr.Query('DebugRay'):
        DebugBox(oGame, vPos, fAngle, vOffset, vSize, vAngle, vSymmetry)
    vRandom = []
    for iRandom in vSize:
        vRandom.append(oGame.Random(int(iRandom * 100)) / 100 - iRandom * 0.5)
    
    vRandom = cl_math.GetOffsetWorldPos((0, 0, 0), vRandom, vAngle)
    vOffset = cl_math.Vec3Add(vOffset, vRandom)
    vOffset = cl_math.Vec3MulV(vOffset, vSymmetry)
    vOffset = cl_math.GetOffsetWorldPos((0, 0, 0), vOffset, (0, fAngle, 0))
    vTar = cl_math.Vec3Add(vPos, vOffset)
    dCartoon['MuzzlePos'] = vTar
    return vTar


def GetMuzzlePos(oSkill):
    iAttack = oSkill.m_Base['AID']
    oAttack = oSkill.m_Game.GetObject(iAttack, PY_FLAG_DEAD)
    if oAttack:
        vPos = oAttack.GetPos()
    else:
        vPos = oSkill.m_Base['vStart']
    vStart = (vPos[0], vPos[1] + oSkill.m_Base['ModelHeight'] * 0.85, vPos[2])
    return vStart


def CrtArgMuzzlePos(oSkill, dCartoon):
    return GetMuzzlePosition(oSkill, dCartoon)


def GetMuzzlePosition(oSkill, dCartoon):
    vStart = GetMuzzlePos(oSkill)
    dCartoon['MuzzlePos'] = vStart
    return vStart


def CrtArgMuzzleAreaPos(oSkill, dCartoon, Name):
    return GetMuzzlePosition(oSkill, dCartoon)


def CrtArgCameraCenterPos(oSkill, dCartoon):
    return GetCameraCenterPosition(oSkill, dCartoon)


def GetCameraCenterPosition(oSkill, dCartoon):
    if 'CameraCenterPos' in oSkill.m_Custom:
        return oSkill.m_Custom['CameraCenterPos']
    iAttack = oSkill.m_Base['AID']
    oAttack = oSkill.m_Game.GetObject(iAttack, PY_FLAG_DEAD)
    if oAttack:
        vPos = oAttack.GetPos()
    else:
        vPos = oSkill.m_Base['vStart']
    vStart = (vPos[0], vPos[1] + oSkill.m_Base['ModelHeight'] * 0.85, vPos[2])
    dCartoon['MuzzlePos'] = vStart
    return vStart


def GetMonsterMuzzlePos(oSkill, vOffset):
    iAttack = oSkill.m_Base['AID']
    oAttack = oSkill.m_Game.GetObject(iAttack, PY_FLAG_DEAD)
    if oAttack:
        vPos = oAttack.GetPos()
        tFacing = oAttack.GetFacing()
        if oAttack.HasAttr('Scale'):
            oAttr = oAttack.GetAttr('Scale')
            iCurValue = oAttr.GetValue(oAttack)
            fRatio = iCurValue / 100
            if fRatio != 1:
                vOffset = cl_math.Vec3MulF(vOffset, fRatio)
            else:
                vPos = oSkill.m_Base['vStart']
                tFacing = cl_math.Vec3Minus(oSkill.m_Base['vEnd'], vPos)
    fAngle = None.CalAngle2D((0, 0, -1), tFacing)
    if tFacing[0] < 0:
        fAngle = -fAngle
    fDis = cl_math.CalDistance3D((0, 0, 0), (vOffset[0], 0, vOffset[2]))
    (ox, _, oz) = vPos
    (tx, ty, tz) = cl_math.Vec3Add(vPos, vOffset)
    (tx, tz) = cl_math.Vec2DestPosDir((ox, oz), (tx - ox, tz - oz), fDis, int(fAngle))
    vTar = (tx, ty, tz)
    return vTar


def CrtArgMonsterMuzzlePos(oSkill, dCartoon, vOffset):
    vTar = GetMonsterMuzzlePos(oSkill, vOffset)
    dCartoon['MuzzlePos'] = vTar
    return vTar


def CrtMonsterCustomMuzzlePos(oSKill, sFuncName, *args):
    iPerform = oSKill.m_Base['pfid']
    func = cl_perform.GetPerformModuleAttr(iPerform, sFuncName)
    if func:
        return func(oSKill, *args)
    return oSKill.m_Base['vStart']


def CrtArgCloseAttPos(oSkill, dCartoon):
    vStart = oSkill.m_Base['vStart']
    return vStart


def CrtArgCloseTarPos(oSkill, dCartoon):
    vEnd = oSkill.m_Base['vEnd']
    return vEnd


def CrtArgHitTransform(oSkill):
    pass


def CrtArgCustomPos(oSkill, dCartoon):
    if 'vEnd' in oSkill.m_Custom:
        vEnd = oSkill.m_Custom['vEnd']
    else:
        vEnd = oSkill.m_Base['vEnd']
    return vEnd


def CrtArgCustomStartPos(oSkill, dCartoon):
    if 'vStart' in oSkill.m_Custom:
        vStart = oSkill.m_Custom['vStart']
    else:
        vStart = oSkill.m_Base['vStart']
    return vStart


def CrtArgCustomTargetPos(oSkill):
    vPos = oSkill.m_Base['vStart']
    if 'LockTarget' in oSkill.m_Custom:
        oVictim = oSkill.m_Game.GetObject(oSkill.m_Custom['LockTarget'][0])
        if oVictim:
            vPos = oVictim.GetPos()
            vPos = [
                vPos[0],
                vPos[1] + oVictim.m_ModelHeight * 0.5,
                vPos[2]]
    return vPos


def CrtArgHitPos(oSkill):
    if 'CurHitPos' in oSkill.m_Update:
        vHitPos = oSkill.m_Update['CurHitPos']
    elif 'CurVID' in oSkill.m_Update:
        iVictim = oSkill.m_Update['CurVID']
        oVictim = oSkill.m_Game.GetObject(iVictim)
        vHitPos = oVictim.GetPos() if oVictim else oSkill.m_Base['vEnd']
    else:
        vHitPos = oSkill.m_Base['vEnd']
    return vHitPos


def CrtArgRandomNum(oSkill, iMin, iMax):
    if iMin > iMax:
        return 0
    return oSkill.m_Game.Random((iMax - iMin) + 1) + iMin


def CrtArgRandomIntList(oSkill, iMin, iMax, iSize):
    lstRet = []
    if iMin > iMax:
        return lstRet
    for _ in range(iSize):
        lstRet.append(oSkill.m_Game.Random((iMax - iMin) + 1) + iMin)
    
    return lstRet


def CrtArgDestPosDirPlane(oSkill, vPos, vDir, fDis, iAngle):
    vEnd = cl_math.Vec3DestPosDirPlane(vPos, vDir, fDis, int(iAngle))
    return vEnd


def CrtArgDestPosDir(oSkill, vPos, vDir, fDis, iAngle):
    vEnd = cl_math.Vec3DestPosDir(vPos, vDir, fDis, iAngle)
    return vEnd


def CrtArgRandomAngle(oSkill, dCartoon, vStart, vEnd, iHorizontalMin, iHorizontalMax, iVerticalMin, iVerticalMax, bDown):
    oGame = oSkill.m_Game
    vDir = cl_math.Vec3Minus(vEnd, vStart)
    tAxis = (0, 1, 0)
    iAngle = oGame.Random(iHorizontalMax - iHorizontalMin) + iHorizontalMin
    iAngle = iAngle if oGame.Random(2) else -iAngle
    vNewDir = cl_math.Vec3Normalize(cl_math.RotateAroundVector(vDir, tAxis, iAngle))
    if bDown and oGame.Random(2):
        tAxis = (0, -1, 0)
    tAxis = cl_math.VectorCross3D(vNewDir, tAxis)
    iAngle = oGame.Random(iVerticalMax - iVerticalMin) + iVerticalMin
    vNewDir = cl_math.Vec3Normalize(cl_math.RotateAroundVector(vNewDir, tAxis, iAngle))
    vNewEnd = cl_math.Vec3DisplaceDir(vStart, vNewDir, cl_math.CalDistance3D(vStart, vEnd))
    return vNewEnd


def CrtArgShiftAngle(oSkill, dCartoon, vStart, vEnd, iHorizontal, iVertical):
    vDir = cl_math.Vec3Minus(vEnd, vStart)
    tAxis = (0, 1, 0)
    iAngle = iHorizontal
    vNewDir = cl_math.Vec3Normalize(cl_math.RotateAroundVector(vDir, tAxis, iAngle))
    if iVertical != 0:
        if iVertical < 0:
            tAxis = (0, -1, 0)
        tAxis = cl_math.VectorCross3D(vNewDir, tAxis)
        iAngle = abs(iVertical)
        vNewDir = cl_math.Vec3Normalize(cl_math.RotateAroundVector(vNewDir, tAxis, iAngle))
    vNewEnd = cl_math.Vec3DisplaceDir(vStart, vNewDir, cl_math.CalDistance3D(vStart, vEnd))
    return vNewEnd


def CrtArgSetParabolaSpeed(oSkill, dCartoon, vStart, vEnd, fHorizontalSpeed, fVerticalAccelerate, fHeight = 0):
    fSecond = cl_math.CalDistance(vStart, vEnd) / fHorizontalSpeed
    fVerticalSpeed = ((vEnd[1] - vStart[1]) + fHeight) / fSecond + (-fVerticalAccelerate / 2) * fSecond
    vDir = cl_math.Vec3Normalize((vEnd[0] - vStart[0], 0, vEnd[2] - vStart[2]))
    vHorizontalSpeed = cl_math.Vec3MulF(vDir, fHorizontalSpeed)
    dCartoon['SpeedVector'] = (vHorizontalSpeed[0], fVerticalSpeed, vHorizontalSpeed[2])
    return dCartoon['SpeedVector']


def CalParabolaSpeed(vStart, vEnd, fVerticalAccelerate, fAngle):
    fHDistance = cl_math.CalDistance(vStart, vEnd)
    fVDistance = vEnd[1] - vStart[1]
    fTan = cl_math.TanAngle(fAngle)
    fCal = ((fVDistance - fTan * fHDistance) / fVerticalAccelerate) * 2
    if fCal <= 0:
        fHorizontalSpeed = 5
        fSpeed = fHorizontalSpeed / cl_math.CosAngle(fAngle)
    else:
        fSecond = fCal ** 0.5
        fSpeed = fHDistance / fSecond / cl_math.CosAngle(fAngle)
    return fSpeed


def CrtArgSetEndYByDistance(oSkill, dCartoon, vStart, vEnd, fRatio):
    vNewEnd = (vEnd[0], vEnd[1] + cl_math.CalDistance(vStart, vEnd) * fRatio, vEnd[2])
    return vNewEnd


def CrtArgGetCustomDir(oSkill, vStart, vEnd, vEuler, baseHorizontal = False):
    vDir = cl_math.Vec3Minus(vEnd, vStart)
    vCross = cl_math.VectorCross3D(vDir, (0, 1, 0))
    if vEuler[0] != 0:
        fOffsetAngle = vEuler[0]
        if baseHorizontal:
            fDis = cl_math.CalDistance3D(vStart, vEnd)
            fDisY = vStart[1] - vEnd[1]
            if fDis != 0:
                fOffsetAngle = math.asin(fDisY / fDis) * 180 / math.pi + fOffsetAngle
        vDir = cl_math.RotateAroundVector(vDir, vCross, fOffsetAngle)
    if vEuler[1] != 0:
        vDir = cl_math.RotateAroundVector(vDir, (0, 1, 0), vEuler[1])
    if vEuler[2] != 0:
        vTmp = cl_math.VectorCross3D((0, 1, 0), vCross)
        vDir = cl_math.RotateAroundVector(vDir, vTmp, vEuler[2])
    vDir = cl_math.Vec3Normalize(vDir)
    return vDir


def CrtArgGetStickerPos(oSkill, sid):
    pass


def VectorShiftForAttDir(oSkill, vVector, vShift):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return vVector
    vFacing = oAttack.GetFacing()
    if cl_math.IsZero(vFacing):
        return vVector
    iAngle = cl_math.CalAngle3D(vFacing, (0, 0, 1))
    if vFacing[0] < 0:
        iAngle = -iAngle
    vShift = cl_math.RotateAroundVector(vShift, (0, 1, 0), iAngle)
    return cl_math.Vec3Add(vVector, vShift)


def GetAllHeroCnt(oSkill, bAlive, bUseRidingAloneCnt = False):
    if bUseRidingAloneCnt:
        oWarMgr = oSkill.m_Game.m_WarMgr
        iPlayerCnt = oWarMgr.Query('GMSpawnCnt')
        if iPlayerCnt:
            return iPlayerCnt
        oRidingAloneElement = oWarMgr.GetComponent('RidingAloneElement')
        if oRidingAloneElement:
            return oRidingAloneElement.m_SpawnCnt
    if not bAlive:
        iScene = oSkill.m_Base['Scene']
        iAllHeroCnt = 0
        for iHeroID in oSkill.m_Game.m_WarMgr.GetAllHero():
            oHero = oSkill.m_Game.GetObject(iHeroID)
            if not oHero or iScene != oHero.m_Scene:
                continue
            iAllHeroCnt += 1
        
        return iAllHeroCnt
    return oSkill.m_CacheData.GetSkillCache('m_LiveHeroCnt', 0)


def GetRandomLivePlayer(oSkill, iAngle, bNotContainDying = False, fMaxDis = 0, bSkillVIDSecond = False, iFlag = PY_FLAG_NONE, bResetVID = False):
    oGame = oSkill.m_Game
    iAttack = oSkill.m_Base['AID']
    oAttack = oGame.GetObject(iAttack)
    if bResetVID:
        iVictim = 0
    else:
        iVictim = oSkill.m_Base['VID']
    if not oAttack:
        return iVictim
    lstLive = GetLiveHeroID(oSkill, bNotContainDying, fMaxDis)
    if not lstLive:
        return iVictim
    if bSkillVIDSecond and iVictim in lstLive:
        lstLive.remove(iVictim)
    lstRandom = []
    vOri = oAttack.GetPos()
    vFace = oAttack.GetFacing()
    if cl_math.IsZero(vFace):
        return iVictim
    fHalfCos = cl_math.CosAngle(iAngle // 2)
    for iLive in lstLive:
        oTarget = oGame.GetObject(iLive, iFlag)
        if not oTarget:
            continue
        vTar = oTarget.GetPos()
        vDir = cl_math.Vec3Minus(vTar, vOri)
        if cl_math.IsZero(vDir):
            fCos = 1
        else:
            fCos = cl_math.VectorDot2D(vDir, vFace) / cl_math.CalDistance3D((0, 0, 0), vDir) / cl_math.CalDistance3D((0, 0, 0), vFace)
        if fCos >= fHalfCos:
            lstRandom.append(iLive)
    
    if not lstRandom:
        return iVictim
    iIndex = oSkill.m_Game.Random(len(lstRandom))
    return lstRandom[iIndex]


def GetNearestPlayer(oSkill, iFromWarrior):
    oGame = oSkill.m_Game
    oTarget = oGame.GetObject(iFromWarrior)
    if not oTarget:
        return oSkill.m_Base['VID']
    lstLive = GetLiveHeroID(oSkill, False)
    if not lstLive:
        return oSkill.m_Base['VID']
    iRet = 0
    fMinDis = 268435455
    vTarget = oTarget.GetPos()
    for iLive in lstLive:
        oHero = oGame.GetObject(iLive)
        if not oHero:
            continue
        fDis = cl_math.CalDistance3D(vTarget, oHero.GetPos())
        if fDis < fMinDis:
            iRet = iLive
            fMinDis = fDis
    
    return iRet


def GetAttackerServantID(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack or not (oAttack.m_FightType & WARRIOR_HERO):
        return 0
    return oAttack.m_Servant


def GetAttackerOwnerID(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return 0
    return oAttack.m_Owner


def GetTargetOwnerID(oSkill, iTarget):
    oTarget = oSkill.m_Game.GetObject(iTarget)
    if not oTarget:
        return 0
    if not oTarget.m_Owner:
        return iTarget
    return oTarget.m_Owner


def SetSkillVictim(oSkill, iTarget):
    oSkill.m_Base['VID'] = iTarget


def SetCustomPos(oSkill, vPos):
    oSkill.m_Custom['vEnd'] = vPos


def ChangeAttackerShield(oSkill, iVal):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    ChangeDefValue(oSkill, oAttack, iVal, DAM_USE_SHIELD)


def ChangeAttackerArmor(oSkill, iVal):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    ChangeDefValue(oSkill, oAttack, iVal, DAM_USE_ARMOR)


def ChangeAttackerEnergy(oSkill, iChange, iReason = 0):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oAttack.EnergyModify(int(iChange), iReason, oSkill = oSkill)


def ChangeVictimDefValue(oSkill, iChange, iDamUseType):
    if 'CurVID' not in oSkill.m_Update:
        return None
    oVictim = oSkill.m_Game.GetObject(oSkill.m_Update['CurVID'])
    if not oVictim:
        return None
    ChangeDefValue(oSkill, oVictim, iChange, iDamUseType)


def ChangeDefValue(oSkill, oTarget, iVal, iDamUseType):
    oReason = oSkill.m_Base['RS'].ExtInfo({
        'ShowTips': 0,
        'DamType': DAM_TYPE_TRUE | iDamUseType })
    if iVal < 0:
        lstChange = [
            (-iVal, oReason)]
        oTarget.HPModifyDam(oTarget.m_ID, lstChange)
    elif iVal > 0:
        lstChange = [
            (iVal, oReason)]
        oTarget.HPModifyCure(oTarget.m_ID, lstChange)


def BreakUnBossVictimShield(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oGame = oSkill.m_Game
    iTarget = oSkill.m_Update['CurVID']
    oVictim = oGame.GetObject(iTarget, PY_FLAG_DEAD)
    if not oVictim:
        return None
    if oVictim.m_FightType & WARRIOR_BOSS == WARRIOR_BOSS:
        return None
    oReason = oSkill.m_Base['RS'].ExtInfo({
        'ShowTips': 0,
        'DamType': DAM_TYPE_TRUE | DAM_USE_ARMOR })
    iVal = oVictim.Armor()
    lstChange = [
        (iVal, oReason)]
    oVictim.HPModifyDam(oAttack.m_ID, lstChange)


def BreakVictimProtection(oSkill, iDamUse, bNoBoss, bNoElite):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oGame = oSkill.m_Game
    iTarget = oSkill.m_Update['CurVID']
    oVictim = oGame.GetObject(iTarget, PY_FLAG_DEAD)
    if not oVictim:
        return None
    iFightType = oVictim.m_FightType
    if bNoBoss and iFightType & WARRIOR_BOSS == WARRIOR_BOSS:
        return None
    if bNoElite and iFightType & WARRIOR_ELITE == WARRIOR_ELITE:
        return None
    oReason = oSkill.m_Base['RS'].ExtInfo({
        'ShowTips': 0,
        'DamType': DAM_TYPE_TRUE | iDamUse })
    iVal = 0
    if iDamUse & DAM_USE_SHIELD == DAM_USE_SHIELD:
        iVal += oVictim.Shield()
    if iDamUse & DAM_USE_ARMOR == DAM_USE_ARMOR:
        iVal += oVictim.Armor()
    if iDamUse & DAM_USE_HP == DAM_USE_HP:
        iVal += oVictim.HP()
    lstChange = [
        (iVal, oReason)]
    oVictim.HPModifyDam(oAttack.m_ID, lstChange)


def SubAttackerCareerPerformColdTime(oSkill, iPercent, iTime = 0):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    pfobj = oAttack.GetCareerPerform()
    iPerform = pfobj.m_SID
    iColdTimeFrame = oAttack.m_Perform.GetTotalColdTime(iPerform)
    if not iColdTimeFrame:
        return None
    iFrame = Time2Frame(iTime)
    if iPercent > 0:
        iMaxColdTimeFrame = oAttack.m_Perform.GetMaxColdTime(iPerform)
        iFrame += iMaxColdTimeFrame * iPercent // 100
    oAttack.m_Perform.ModifyColdTime(iPerform, -iFrame)


def AddAttackerPerformCD(oSkill, iPerform, iPercent):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    if oAttack.Query('DebugStatus', 0) & DEBUG_STATUS_NOPFCD == DEBUG_STATUS_NOPFCD:
        return None
    oPerform = oAttack.m_Perform.GetPerform(iPerform)
    if not oPerform:
        return None
    iPerformCDFrame = oPerform.GetCDTime(oAttack)
    iAddFrame = iPerformCDFrame * iPercent // 100
    oAttack.m_Perform.AddColdTime(iPerform, iAddFrame)


def ListPointOnSphere(oSkill, vRotate):
    lstDir = []
    a = 1 / math.sqrt(3) / 2
    lstTmp = [
        -1,
        1]
    fAngle = cl_math.CalAngle3D((0, 1, 0), vRotate)
    fVertical = cl_math.VectorCross3D((0, 1, 0), vRotate)
    for x in lstTmp:
        for y in lstTmp:
            for z in lstTmp:
                vDir = cl_math.Vec3MulF((x, y, z), a)
                if not cl_math.IsZero(fVertical):
                    vDir = cl_math.RotateAroundVector(vDir, fVertical, fAngle)
                lstDir.append(vDir)
            
        
    
    return lstDir


def DelAttackPerformCoverCD(oSkill, iPerform):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oPerform = oAttack.m_Perform.GetPerform(iPerform)
    if not oPerform:
        return None
    oAttack.m_Perform.DelCoverColdTime(iPerform)


def SetCrtValue(oSkill, sid, sAttr, iDefault = 0):
    dCartoon = oSkill.GetCartoonBySID(sid)
    if dCartoon:
        dCartoon[sAttr] = iDefault


def GetCrtValue(oSkill, sid, sAttr, iDefault = 0):
    dCartoon = oSkill.GetCartoonBySID(sid)
    if dCartoon and sAttr in dCartoon:
        return dCartoon[sAttr]
    return iDefault


def CalDirSplitPos(oSkill, sid, iIndex, iMax, iHRang, iVRang):
    dCartoon = oSkill.GetCartoonBySID(sid)
    vDir = cl_math.Vec3MulF(cl_math.Vec3Normalize(cl_math.Vec3Minus(dCartoon['Final'], dCartoon['Start'])), 100)
    if iMax > 1:
        tRight = cl_math.Vec3Normalize(cl_math.VectorCross3D((0, 1, 0), vDir))
        if iHRang != 0:
            iHRang = iHRang * iIndex // (iMax - 1) - iHRang // 2
            tUp = cl_math.Vec3Normalize(cl_math.VectorCross3D(tRight, vDir))
            vDir = cl_math.RotateAroundVector(vDir, tUp, iHRang)
        if iVRang != 0:
            iVRang = iVRang * iIndex // (iMax - 1) - iVRang // 2
            vDir = cl_math.RotateAroundVector(vDir, tRight, iVRang)
    return cl_math.Vec3Add(dCartoon['Start'], vDir)


def CalCircleSplitDir(oSkill, iIndex, iMax, iUpAngle):
    vDir = (1, 0, 0)
    if iMax > 1:
        iRange = (360 // iMax) * iIndex
        vDir = cl_math.RotateAroundVector(vDir, (0, 1, 0), iRange)
        vDir = cl_math.RotateAroundVector(vDir, (-vDir[2], 0, vDir[0]), iUpAngle)
    return vDir


def GetCartoonStart(oSkill, sid):
    return GetStartPositionInCrt(oSkill, sid)


def GetCartoonEnd(oSkill, sid):
    return GetEndPositionInCrt(oSkill, sid)


def GetStartPositionInCrt(oSkill, sid):
    dCartoon = oSkill.GetCartoonBySID(sid)
    if 'CheckStart' in dCartoon:
        return dCartoon['CheckStart']
    return dCartoon['Start']


def GetEndPositionInCrt(oSkill, sid):
    dCartoon = oSkill.GetCartoonBySID(sid)
    if 'Final' in dCartoon:
        return dCartoon['Final']
    return dCartoon['CurPos']


def GetCartoonCurPos(oSkill, sid):
    dCartoon = oSkill.GetCartoonBySID(sid)
    return dCartoon['CurPos']


def GetCartoonChargeLevel(oSkill, sid):
    dCartoon = oSkill.GetCartoonBySID(sid)
    return dCartoon['ChargeLevel']


def GetChargeCartoonChargeLevel(oSkill, sid):
    dCartoon = oSkill.GetCartoonBySID(sid)
    return dCartoon['ChargeLevel']


def GetTimerCartoonCurTimes(oSkill, sid):
    dCartoon = oSkill.GetCartoonBySID(sid)
    if 'CurTimes' in dCartoon:
        return dCartoon['CurTimes']
    return 0


def GetInkAreaCheckHeight(oSkill, sid):
    dCartoon = oSkill.GetCartoonBySID(sid)
    if 'HighestPoint' not in dCartoon or 'LowestPoint' not in dCartoon:
        return 0
    return dCartoon['HighestPoint'][1] - dCartoon['LowestPoint'][1]


def GetInkAreaCheckLength(oSkill, sid, fMax):
    dCartoon = oSkill.GetCartoonBySID(sid)
    vStart = dCartoon['Start']
    vEnd = dCartoon['End']
    vDir = cl_math.Vec3Minus(vEnd, vStart)
    vHorizontalDir = GetCartoonHorizontalDir(oSkill, sid)
    iAngle = cl_math.CalAngle3D(vHorizontalDir, vDir)
    return cl_math.CosAngle(iAngle) * fMax


def GetCartoonHorizontalDir(oSkill, sid):
    dCartoon = oSkill.GetCartoonBySID(sid)
    vStart = dCartoon['Start']
    vEnd = dCartoon['End']
    vEnd = (vEnd[0], vStart[1], vEnd[2])
    return cl_math.Vec3Minus(vEnd, vStart)


def CalCrtFlyDis(oSkill, sid):
    dCartoon = oSkill.GetCartoonBySID(sid)
    return cl_math.CalDistance3D(dCartoon['Start'], dCartoon['Final'])


def IsCrtFlyOverDis(oSkill, sid):
    dCartoon = oSkill.GetCartoonBySID(sid)
    if 'FlyOverDis' in dCartoon:
        return dCartoon['FlyOverDis']
    return False


def CalCrtFlyMaxDis(oSkill, sid):
    dCartoon = oSkill.GetCartoonBySID(sid)
    return dCartoon['Distance']


def GetCartoonHitTargetInOrder(oSkill, sid):
    iTarget = 0
    dCartoon = oSkill.GetCartoonBySID(sid)
    if 'AllVLST' in dCartoon:
        iCurIdx = dCartoon.get('TargetOrder', 0)
        lstAll = dCartoon['AllVLST']
        iLen = len(lstAll)
        if iCurIdx < iLen:
            iTarget = lstAll[iCurIdx]
            dCartoon['TargetOrder'] = (iCurIdx + 1) % iLen
    return iTarget


def GetCartoonHitTargetCount(oSkill, sid):
    dCartoon = oSkill.GetCartoonBySID(sid)
    if 'AllVLST' in dCartoon:
        return len(dCartoon['AllVLST'])
    return 0


def GetCartoonHitFirstTargetPos(oSkill, sid):
    dCartoon = oSkill.GetCartoonBySID(sid)
    lstHitInfo = dCartoon['AllHitInfo'] if 'AllHitInfo' in dCartoon else []
    if lstHitInfo:
        dFirstHitInfo = lstHitInfo[0]
        if dFirstHitInfo and 'HitPos' in dFirstHitInfo:
            return dFirstHitInfo['HitPos']
    return dCartoon['CurPos']


def GetCartoonHitTimes(oSkill, sid):
    dCartoon = oSkill.GetCartoonBySID(sid)
    if 'HitTimes' in dCartoon:
        return dCartoon['HitTimes']
    return 0


def GetCartoonHitPosLst(oSkill, sid):
    dCartoon = oSkill.GetCartoonBySID(sid)
    if 'HitPos' in dCartoon:
        return dCartoon['HitPos']
    return []


def GetCartoonFirstHitVectorNormal(oSkill, iSID):
    dCartoon = oSkill.GetCartoonBySID(iSID)
    iNodeID = dCartoon['ID']
    if iNodeID in oSkill.m_NetSend:
        dSend = oSkill.m_NetSend[iNodeID]
        lstRay = dSend['Ray'] if 'Ray' in dSend else []
        if lstRay:
            return lstRay[0][1]
    return (0, 0, 0)


def GetLiveHeroID(oSkill, bNotContainDying, fMaxDis = 0):
    oGame = oSkill.m_Game
    iScene = oSkill.m_Base['Scene']
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    lstHero = []
    if not oScene:
        return lstHero
    for iHero in oScene.GetHeros():
        oHero = oGame.GetObject(iHero)
        if not oHero or oHero.IsDeadNoDying():
            continue
        if bNotContainDying and oHero.IsDying():
            continue
        if fMaxDis:
            oAttack = oSkill.GetAttack()
            if not cl_math.CheckDistance3D(oAttack.GetPos(), oHero.GetPos(), fMaxDis):
                continue
            continue
        lstHero.append(iHero)
    
    return lstHero


def GetAllHeroIDByPyFlag(oSkill, iPyFlag):
    oGame = oSkill.m_Game
    iScene = oSkill.m_Base['Scene']
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    lstHero = []
    if not oScene:
        return lstHero
    for iHero in oScene.GetHeros():
        oHero = oGame.GetObject(iHero, iPyFlag)
        if not oHero:
            continue
        lstHero.append(iHero)
    
    return lstHero


def GetWeaponAttackDis(oSkill):
    return GetWeaponAttDis(oSkill)


def GetWeaponAttDis(oSkill):
    return oSkill.m_Cache['AttDis']


def GetWeaponBulletSpeed(oSkill):
    return oSkill.m_Cache['BulletSpeed']


def GetWeaponIntAttr(oSkill, sAttr):
    return int(oSkill.m_Cache[sAttr])


def GetCurWeaponAttr(oSkill, sAttr):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return 0
    if 'ItemID' not in oSkill.m_Cache:
        return 0
    iItemID = oSkill.m_Cache['ItemID']
    oItem = oAttack.m_WieldCon.GetItemByID(iItemID)
    if not oItem:
        return 0
    if sAttr in oItem.m_PrivateAttr:
        return oItem.QueryAttr(sAttr)
    return oItem.GetSpecialAttr(sAttr)


def GetTrapPerformCustomParam(oSkill, sParam, default):
    if 'TrapPerformInfo' not in oSkill.m_Cache:
        return default
    iPerform = oSkill.m_Base['pfid']
    dPerformInfo = oSkill.m_Cache['TrapPerformInfo']
    if iPerform not in dPerformInfo:
        return default
    dPerform = dPerformInfo[iPerform]
    iCurTimes = dPerform['CurTimes']
    lstParam = dPerform['CustomParam']
    if not lstParam:
        return default
    dParam = lstParam[iCurTimes % len(lstParam)]
    if sParam not in dParam:
        return default
    return dParam[sParam]


def GetSwitchWeaponTime(oSkill, iTarget):
    oGame = oSkill.m_Game
    iAttack = oSkill.m_Base['AID']
    oAttack = oGame.GetObject(iAttack)
    if not oAttack:
        return 0
    iTarget = oSkill.m_Base['Weapon']
    oCurWeapon = oAttack.m_WieldCon.GetCurWeapon()
    oTargetWeapon = oAttack.m_WieldCon.GetItemByPos(iTarget)
    if not oCurWeapon or not oTargetWeapon:
        return 0
    iUnwieldTime = oCurWeapon.QueryAttr('UnwieldTime')
    iWieldTime = oTargetWeapon.QueryAttr('WieldTime')
    return iUnwieldTime + iWieldTime


def GetNearestSpaceByPos(oSkill, vPos):
    if not vPos:
        return oSkill.m_Base['vEnd']
    (iRet, vPos) = oSkill.m_Game.Scene_GetSpace(oSkill.m_Base['Scene'], vPos)
    if not iRet:
        return oSkill.m_Base['vEnd']
    return vPos


def GetSkillEndLine(oSkill):
    vPos = oSkill.m_Base['vEnd']
    oAttack = oSkill.GetAttack()
    if oAttack:
        vNow = oAttack.GetPos()
        fGroundDis = oSkill.m_Game.Scene_GroundDistance(oAttack.m_Scene, (vPos[0], vPos[1] + 1, vPos[2]), 5, PXMASK_MOVEBLK, oAttack.m_ID)
        vPos = (vPos[0], (vPos[1] - fGroundDis) + 1, vPos[2])
        vPos = oSkill.m_Game.Scene_NavMeshRayCast(oSkill.m_Base['Scene'], vNow, vPos)
    return [
        vPos]


def GetLineByPos(oSkill, vPos):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return [
            oSkill.m_Base['vEnd']]
    vPos = oSkill.m_Game.Scene_NavMeshRayCast(oSkill.m_Base['Scene'], oAttack.GetPos(), vPos)
    return [
        vPos]


def GetLevelPosLine(oSkill, sName):
    oGame = oSkill.m_Game
    iAttack = oSkill.m_Base['AID']
    oAttack = oGame.GetObject(iAttack)
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    lstLine = []
    if oAttack and oAttack.m_LineIdx:
        oLine = oLevelCtrl.GetLineNode(oAttack.m_LineIdx)
        oLevelConfData = oLevelCtrl.m_LevelConfData
        iLevel = oLine.m_LevelNode.m_Level
        lstLine = oLevelConfData.GetLineConfig(iLevel, oLine.m_Name, 'posline', sName)
    return lstLine


def ChooseLevelPosLineNear(oSkill, lstName, vPos = None):
    oGame = oSkill.m_Game
    iAttack = oSkill.m_Base['AID']
    oAttack = oGame.GetObject(iAttack)
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    oLevelConfData = oLevelCtrl.m_LevelConfData
    dPosLine = { }
    if oAttack and oAttack.m_LineIdx:
        oLine = oLevelCtrl.GetLineNode(oAttack.m_LineIdx)
        iLevel = oLine.m_LevelNode.m_Level
        dPosLine = oLevelConfData.GetLineConfig(iLevel, oLine.m_Name, 'posline')
    if not vPos or cl_math.IsZero(vPos):
        oAttack = oSkill.GetAttack()
        vPos = oAttack.GetPos()
    iMinDis = 268435455
    lstRes = []
    for sName in lstName:
        if sName not in dPosLine:
            continue
        lstLine = dPosLine[sName]
        iDis = cl_math.CalDistance3D(lstLine[0], vPos)
        if iDis < iMinDis:
            iMinDis = iDis
            lstRes = lstLine
    
    return lstRes


def ChooseLevelPosLineRandom(oSkill, lstName):
    oGame = oSkill.m_Game
    iAttack = oSkill.m_Base['AID']
    oAttack = oGame.GetObject(iAttack)
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    dPosLine = { }
    if oAttack and oAttack.m_LineIdx:
        oLine = oLevelCtrl.GetLineNode(oAttack.m_LineIdx)
        oLevelConfData = oLevelCtrl.m_LevelConfData
        iLevel = oLine.m_LevelNode.m_Level
        dPosLine = oLevelConfData.GetLineConfig(iLevel, oLine.m_Name, 'posline')
    iIndex = oGame.Random(len(lstName))
    sName = lstName[iIndex]
    if sName in dPosLine:
        return dPosLine[sName]
    return []


def ChoosePosFromListNear(oSkill, vTarget, lstPos):
    iMinDis = 268435455
    vPos = vTarget
    for vValidPos in lstPos:
        iDis = cl_math.CalDistance3D(vTarget, vValidPos)
        if iDis < iMinDis:
            iMinDis = iDis
            vPos = vValidPos
    
    return vPos


def SetTeleportPos(oSkill, vPos):
    oSkill.m_Collect['TeleportPos'] = vPos


def GetMonsterKeepAwayPos(oSkill, fRange, iAngle, iRayNum):
    vPos = oSkill.m_Base['vEnd']
    oAttack = oSkill.GetAttack()
    if oAttack and oAttack.m_Agent and oAttack.m_MoveCtrl:
        oTarget = oAttack.m_Agent.GetLockEnemy()
        if oTarget:
            iRayNum = min(iRayNum, 10)
            fMinAngle = -iAngle
            fMaxAngle = iAngle
            vPos = oAttack.m_MoveCtrl.E_KeepAwayRayCastPos(oTarget.GetPos(), fRange, fMinAngle, fMaxAngle, iRayNum)
    return vPos


def GetSkillCollectPos(oSkill, sPosName):
    vPos = oSkill.m_Collect[sPosName] if sPosName in oSkill.m_Collect else (0, 0, 0)
    return vPos


def GetPerformArgValue(oSkill, sAttr, iDefault = 0):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return iDefault
    iPerform = oSkill.m_Base['pfid']
    iItem = oSkill.m_Base['Weapon']
    oPerform = oAttack.GetPerform(iPerform, iItem)
    if not oPerform:
        return iDefault
    return oPerform.GetArgValue(sAttr, iDefault)


def PerformAddArgValue(oSkill, sAttr, iAdd):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    iPerform = oSkill.m_Base['pfid']
    oPerform = oAttack.GetPerform(iPerform)
    if not oPerform:
        return None
    oPerform.AddArgValue(sAttr, iAdd)

g_LevelMonsterGrade = {
    101: 2,
    102: 4,
    103: 5,
    104: 8,
    105: 10,
    201: 12,
    202: 15,
    203: 18,
    204: 20,
    301: 22,
    302: 25,
    303: 28,
    304: 30,
    401: 31,
    402: 34,
    403: 36 }

def GetLevelMonsterGrade(oSkill):
    oLevelCtrl = oSkill.m_Game.m_WarMgr.GetComponent('LevelCtrl')
    iLayer = oLevelCtrl.m_LayerNum
    iLevel = oLevelCtrl.m_LevelNum
    iGrade = g_LevelMonsterGrade.get(iLayer * 100 + iLevel, 1)
    return iGrade


def IsOpenSnipe(oSkill):
    return oSkill.m_CacheData.IsOpenSnipe()


def GetBallisticType(oSkill):
    return oSkill.m_CacheData.GetBallisticType()


def GetTrajectory(oSkill):
    if 'Trajectory' not in oSkill.m_Cache:
        return 0
    iExtraTrajectory = min(1, oSkill.m_CacheData.m_ExtraTrajectory)
    return oSkill.m_Cache['Trajectory'] // 100 + iExtraTrajectory


def CalTrajectory(oSkill, fMul):
    if 'Trajectory' not in oSkill.m_Cache:
        return 0
    iTrajectory = oSkill.m_Cache['Trajectory']
    iTrajectory = iTrajectory * fMul
    (iResult, iExtra) = divmod(iTrajectory, 100)
    if oSkill.m_Game.Random(100) < iExtra:
        iResult += 1
    return int(iResult)


def GetPerformMode(oSkill):
    return oSkill.m_CacheData.GetPerformMode()


def GetAttackerAttr(oSkill, sAttr):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return 0
    return cl_formula.GetWarriorAttr(sAttr, oAttack)


def GetAttackerBaseAttr(oSkill, sAttr):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return 0
    if not oAttack.HasAttr(sAttr):
        return 0
    oAttr = oAttack.GetAttr(sAttr)
    return oAttr.GetBaseAttr()


def GetVictimAttr(oSkill, sAttr):
    return GetSkillVictimAttr(oSkill, sAttr)


def GetAttackerPerformAttr(oSkill, iPerform, sAttr):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return 0
    oPerform = oAttack.GetPerform(iPerform)
    if not oPerform or sAttr not in oPerform.m_Attr:
        return 0
    return oPerform.CalAttr(sAttr)


def GetAttackerCustomValue(oSkill, sAttr, iDefault = 0):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return iDefault
    return oAttack.GetCustomValue(sAttr, iDefault)


def GetCurVID(oSkill):
    if 'CurVID' in oSkill.m_Update:
        return oSkill.m_Update['CurVID']
    return 0


def GetSkillVID(oSkill):
    return oSkill.m_Base['VID']


def GetSkillAID(oSkill):
    iAttack = oSkill.m_Base['AID']
    return iAttack


def GetSkillVictimAttr(oSkill, sAttr):
    if 'CurVID' in oSkill.m_Update:
        iVictim = oSkill.m_Update['CurVID']
    else:
        iVictim = oSkill.m_Base['VID']
    oVictim = oSkill.m_Game.GetObject(iVictim)
    if not oVictim:
        return 0
    return cl_newformula.GetWarriorAttr(sAttr, oVictim)


def CalAttenuationByDis(oSkill, vPos, iBase, iMin, fMaxDis, fMinDis):
    oGame = oSkill.m_Game
    if fMaxDis <= fMinDis or iBase < iMin:
        iPerform = oSkill.m_Base['pfid'] if 'pfid' in oSkill.m_Base else 0
        SendAlert('err', f'''{oGame.m_ID} {iPerform} calattenuationbydis param err {iBase} {iMin} {fMaxDis} {fMinDis}''')
        return 0
    iVictim = oSkill.m_Update['CurVID']
    oVictim = oGame.GetObject(iVictim, PY_FLAG_DEAD)
    if not oVictim:
        return 0
    fDis = cl_math.CalDistance3D(vPos, oVictim.GetPos())
    if fDis < fMinDis:
        return iBase
    if fDis > fMaxDis:
        return iMin
    iResult = iBase - (fDis - fMinDis) * (iBase - iMin) / (fMaxDis - fMinDis)
    return int(iResult)


def GetPerformCD(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return 0
    iPerform = oSkill.m_Base['pfid']
    iItem = oSkill.m_Base['Weapon']
    oPerform = oAttack.GetPerform(iPerform, iItem)
    if not oPerform:
        return 0
    iCDFrame = oPerform.GetCDTime(oAttack)
    return Frame2Time(iCDFrame) / 100


def GetFirstHitPos(oSkill):
    lstHitInfo = oSkill.m_Update['HitInfo']
    if not lstHitInfo:
        return oSkill.m_Update['CurPos']
    lstHitInfo = oSkill.m_Update['HitInfo']
    dFirstHitInfo = lstHitInfo[0]
    if 'HitPos' in dFirstHitInfo:
        return dFirstHitInfo['HitPos']
    return (0, 0, 0)


def IgnoreCurVictimOnceAfterHit(oSkill):
    iCurVictim = oSkill.m_Update['CurVID']
    IgnoreOnceAfterHitById(oSkill, iCurVictim)


def IgnoreOnceAfterHitById(oSkill, iVictim):
    if 'IgnoreOnce' not in oSkill.m_Collect:
        oSkill.m_Collect['IgnoreOnce'] = { }
    oSkill.m_Collect['IgnoreOnce'][iVictim] = VICTIM_IGNORE_ONCE


def AddIgnoreTarget(oSkill, iTarget):
    if 'IgnoreOnce' not in oSkill.m_Collect:
        oSkill.m_Collect['IgnoreOnce'] = { }
    oSkill.m_Collect['IgnoreOnce'][iTarget] = VICTIM_IGNORE_ALL


def CheckVictimType(oSkill, iFightType, iSideType):
    if 'CurVID' not in oSkill.m_Update:
        return 0
    iCurVictim = oSkill.m_Update['CurVID']
    iAttack = oSkill.m_Base['AID']
    iSide = oSkill.m_Cache['Side']
    oGame = oSkill.m_Game
    oVictim = oGame.GetObject(iCurVictim)
    if oVictim and oVictim.m_FightType & iFightType == iFightType and cl_math.CheckTargetType(oGame, oVictim, iAttack, iSide, iSideType):
        return 1
    return 0


def CheckVictimSide(oSkill, iFightType, iSideType):
    if 'CurVID' not in oSkill.m_Update:
        return 0
    iCurVictim = oSkill.m_Update['CurVID']
    oVictim = oSkill.m_Game.GetObject(iCurVictim)
    if oVictim and oVictim.m_FightType & iFightType == iFightType and oVictim.m_Side & iSideType:
        return 1
    return 0


def CheckVictimSideType(oSkill, iType):
    if 'CurVID' not in oSkill.m_Update:
        return 0
    iCurVictim = oSkill.m_Update['CurVID']
    iAttack = oSkill.m_Base['AID']
    iSide = oSkill.m_Cache['Side']
    oGame = oSkill.m_Game
    oVictim = oGame.GetObject(iCurVictim)
    if oVictim and cl_math.CheckTargetType(oGame, oVictim, iAttack, iSide, iType):
        return 1
    return 0


def CheckTargetSID(oSkill, iSID):
    iVictim = oSkill.m_Base['VID']
    oVictim = oSkill.m_Game.GetObject(iVictim)
    if oVictim and oVictim.m_SID == iSID:
        return 1
    return 0


def CheckVictimSID(oSkill, iSID):
    if 'CurVID' not in oSkill.m_Update:
        return 0
    oVictim = oSkill.m_Game.GetObject(oSkill.m_Update['CurVID'])
    if oVictim and oVictim.m_SID == iSID:
        return 1
    return 0


def CheckVictimBuildIsPointClasses(oSkill, iType):
    if 'CurVID' not in oSkill.m_Update:
        return 0
    oVictim = oSkill.m_Game.GetObject(oSkill.m_Update['CurVID'])
    if not oVictim or not (oVictim.m_FightType & WARRIOR_BUILD):
        return 0
    if iType in oVictim.m_ClassifyList:
        return 1
    return 0


def CheckVictimInPointList(oSkill, lstVID):
    if 'CurVID' not in oSkill.m_Update:
        return 0
    if oSkill.m_Update['CurVID'] in lstVID:
        return 1
    return 0


def CheckVictimTouch(oSkill):
    if 'CurVID' not in oSkill.m_Update or 'Touch' not in oSkill.m_Update:
        return False
    iTarget = oSkill.m_Update['CurVID']
    if iTarget in oSkill.m_Update['Touch']:
        return True
    return False


def CheckHasTalent(oSkill, iTalent):
    oAttack = oSkill.GetAttack()
    oPerform = oAttack.m_TalentCon.GetPerform(iTalent)
    if not oPerform or not (oPerform.m_Enable):
        return False
    return True


def GetTalentLevel(oSkill, iTalent):
    oAttack = oSkill.GetAttack()
    oTalent = oAttack.m_TalentCon.GetPerform(iTalent)
    if not oTalent:
        return 0
    return oTalent.Level()


def GetAllTalentLevelSum(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return 0
    return oAttack.m_TalentCon.GetAllTalentLevelSum()


def CheckHasInscription(oSkill, iSID):
    if 'Inscription' in oSkill.m_Cache and iSID in oSkill.m_Cache['Inscription']:
        return 1
    return 0


def CheckHasState(oSkill, iSID):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return 0
    if oAttack.m_State.GetItemBySID(iSID):
        return 1
    return 0


def CheckWarriorHasState(oSkill, iWarrior, iState):
    oWarrior = oSkill.m_Game.GetObject(iWarrior)
    if oWarrior and oWarrior.m_State.GetItemBySID(iState):
        return 1
    return 0


def CheckHasStateFromAttacker(oSkill, iTarget, iState):
    oTarget = oSkill.m_Game.GetObject(iTarget)
    if not oTarget:
        return 0
    iAttack = oSkill.m_Base['AID']
    if not iAttack:
        return 0
    oState = oTarget.m_State.GetItemBySource(iState, iAttack)
    if oState:
        return 1
    return 0


def CheckTargetAlive(oSkill, iTarget):
    oTarget = oSkill.m_Game.GetObject(iTarget)
    if not oTarget or oTarget.IsDead():
        return 0
    return 1


def CheckHitWeakness(oSkill):
    if 'CurHitArea' not in oSkill.m_Update:
        return False
    return oSkill.m_Update['CurHitArea'] in MONSERT_PART_ALLWEAKNESS


def MonsterAttackerFacePos(oSkill, vPos, iTurnSpeed):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    if oAttack.m_FaceCtrl:
        oAttack.m_FaceCtrl.FacePos(oAttack, vPos, oSkill.m_Base['PFKey'], iTurnSpeed / GAME_FRAME)


def MonsterAttackerFaceLeastAnglePos(oSkill, lstPos, iTurnSpeed):
    oAttack = oSkill.GetAttack()
    vFacing = oAttack.GetFacing()
    vMinPos = None
    iMinAngle = 360
    vOwnerPos = oAttack.GetPos()
    for vPos in lstPos:
        iAngle = cl_math.CalAngle2D(cl_math.Vec3Minus(vPos, vOwnerPos), vFacing)
        if iAngle < iMinAngle:
            iMinAngle = iAngle
            vMinPos = vPos
    
    MonsterAttackerFacePos(oSkill, vMinPos, iTurnSpeed)


def MonsterFaceTarget(oSkill, iTarget, iTurnTime, iKeep):
    oAttack = oSkill.GetAttack()
    if not oAttack or not (oAttack.m_FaceCtrl):
        return None
    sKey = oSkill.m_Base['PFKey']
    oAttack.SetLockEnemy(iTarget)
    oAttack.m_FaceCtrl.FaceTarget(oAttack, iTarget, sKey, iTurnTime, iKeep)


def LockMonsterAttackerFace(oSkill):
    
    def EndUnlock(oSkill):
        if oAttack.m_FaceCtrl:
            oAttack.m_FaceCtrl.UnLockFace(oAttack, sKey)

    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    if oAttack.m_FaceCtrl:
        sKey = oSkill.m_Base['PFKey']
        oAttack.m_FaceCtrl.LockFace(oAttack, oAttack.GetFacing(), sKey)
        oSkill.AddEndFunc(EndUnlock)


def UnlockMonsterAttackerFace(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    if oAttack.m_FaceCtrl:
        sKey = oSkill.m_Base['PFKey']
        oAttack.m_FaceCtrl.UnLockFace(oAttack, sKey)


def MonsterAttackerFaceLockEnemy(oSkill, iKeep):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oAgent = oAttack.m_Agent
    if oAgent:
        oAgent.FaceLockEnemy(iKeep, oAgent)


def MonsterPauseAgent(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oAgent = oAttack.m_Agent
    if oAgent:
        sKey = oSkill.m_Base['PFKey']
        oAgent.PauseAgent(sKey)


def MonsterResumeAgent(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oAgent = oAttack.m_Agent
    if oAgent:
        sKey = oSkill.m_Base['PFKey']
        oAgent.ResumeAgent(sKey)


def CrtArgMonsterTurnDirPos(oSkill, vTarget, iTime, iTurnSpeed, fDis):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    if not iTurnSpeed:
        iTurnSpeed = oAttack.TurnSpeed()
    iShiftAngle = iTime * iTurnSpeed // 100
    vFace = oAttack.GetFacing()
    vPos = oAttack.GetPos()
    vDir = cl_math.Vec3Minus(vTarget, vPos)
    iMaxAngle = 0
    if not cl_math.IsZero(vDir):
        iMaxAngle = cl_math.CalAngle3D(vFace, vDir)
    iAngle = min(abs(iMaxAngle), abs(iShiftAngle))
    iCross = vFace[0] * vDir[2] - vFace[2] * vDir[0]
    if iCross > 0:
        iAngle = iAngle
    else:
        iAngle = -iAngle
    vTurnPos = cl_math.Vec3DestPosDir(vPos, vFace, fDis, iAngle)
    return vTurnPos


def CrtArgSelfFace(oSkill):
    iAttack = oSkill.m_Base['AID']
    oAttack = oSkill.m_Game.GetObject(iAttack, PY_FLAG_DEAD)
    if oAttack:
        vFacing = oAttack.GetFacing()
    else:
        vFacing = (0, 0, -100)
    return vFacing


def CrtArgSelfHeroCtrlToTargetFace(oSkill, vTarget):
    iAttack = oSkill.m_Base['AID']
    oAttack = oSkill.m_Game.GetObject(iAttack, PY_FLAG_DEAD)
    if oAttack:
        (ox, oy, oz) = oAttack.GetPos()
        (tx, ty, tz) = vTarget
        vFacing = (tx - ox, ty - oy, tz - oz)
    else:
        vFacing = (0, 0, -100)
    return vFacing


def CheckHeroFace(oSkill, vCurFacing, vTargetFacing, fAngle):
    if fAngle <= 0 or fAngle >= 360:
        SendAlert('err', '技能%d CheckHeroFace角度范围:0<Angle<360' % oSkill.m_Base['pfid'])
        return False
    return not cl_math.CheckVector2Angle(vCurFacing, vTargetFacing, int(fAngle / 2))


def CrtArgSelfModelDirection(oSkill):
    iAttack = oSkill.m_Base['AID']
    oAttack = oSkill.m_Game.GetObject(iAttack, PY_FLAG_DEAD)
    if oAttack:
        vDir = oAttack.GetDirection()
    else:
        vDir = (0, 0, -100)
    return vDir


def PushVictim(oSkill, vStart, fSpeed, fMaxDis, iPushProbability, angle = 0, iCartoonSID = -1, iIgnoreStruckCD = 0, iClient = 0, iFace2Dir = 0):
    
    def PushMoveEnd(iActNum, iAttackID, dCartoon, oOwner, iType):
        oTemSkill = oGame.m_SkillMgr.GetSkill(iAttackID, iActNum)
        if oTemSkill:
            if oOwner.IsDead():
                oTemSkill.Call_Out(1, dCartoon['ID'])
                return None
            clsCartoon = dCartoon['cls']
            clsCartoon.AddHitTarget(oTemSkill, dCartoon, oOwner.m_ID, { })
            oTemSkill.Call_Out(1, dCartoon['ID'])

    oGame = oSkill.m_Game
    iAngle = angle
    iVictim = oSkill.m_Update['CurVID']
    oVictim = oGame.GetObject(iVictim)
    if not oVictim or not (oVictim.m_MoveCtrl):
        return None
    if oVictim.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
        return None
    if iIgnoreStruckCD:
        oVictim.Set('StruckCDFrame', 0)
    dData = {
        'Skill': oSkill }
    iPush = oVictim.GetKnockedBack(dData, iPushProbability)
    if iPush:
        if cl_math.IsZero(vStart):
            vStart = oSkill.m_Base['vStart']
        fSecondOut = fMaxDis / fSpeed
        vTar = oVictim.GetPos()
        vDir = cl_math.Vec3Minus(vTar, vStart)
        if iAngle:
            iAttack = oSkill.m_Base['AID']
            vAttface = oGame.GetFacing(iAttack)
            vCross = cl_math.VectorCross3D((vDir[0], 0, vDir[2]), (vAttface[0], 0, vAttface[2]))
            if vCross[1] > 0:
                iAngle = 360 - iAngle
            vDir = cl_math.RotateAroundVector(vDir, (0, 1, 0), iAngle)
        cbFun = None
        if iCartoonSID > -1:
            dCartoon = oSkill.GetCartoonBySID(iCartoonSID)
            cbFun = Functor(PushMoveEnd, oSkill.m_Base['ActNum'], oSkill.m_Base['AID'], dCartoon)
        iMove = oVictim.m_MoveCtrl.PushMove(oVictim, vDir, fSpeed, fSecondOut, iClientAni = iClient, iFace2Dir = iFace2Dir, func = cbFun)
        if not iMove and iCartoonSID > -1:
            oSkill.Call_Out(1, dCartoon['ID'])
        elif iCartoonSID > -1:
            dCartoon = oSkill.GetCartoonBySID(iCartoonSID)
            oSkill.Call_Out(1, dCartoon['ID'])


def PushMoveVictim(oSkill, vStart, fSpeed, fMaxDis, vDir = (0, 0, 0), iCartoonSID = -1, bKnockBack = False, iFace2Dir = 0):
    
    def PushMoveEnd(iActNum, iAttackID, dCartoon, oOwner, iType):
        oTemSkill = oGame.m_SkillMgr.GetSkill(iAttackID, iActNum)
        if oTemSkill:
            if oOwner.IsDead():
                oTemSkill.Call_Out(1, dCartoon['ID'])
                return None
            clsCartoon = dCartoon['cls']
            clsCartoon.AddHitTarget(oTemSkill, dCartoon, oOwner.m_ID, { })
            oTemSkill.Call_Out(1, dCartoon['ID'])

    oGame = oSkill.m_Game
    iVictim = oSkill.m_Update['CurVID']
    oVictim = oGame.GetObject(iVictim)
    if not oVictim or not (oVictim.m_MoveCtrl):
        return None
    if oVictim.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
        return None
    if bKnockBack and oVictim.CheckLogicKey(FIGHT3_KEY_IGNOREKNOCKBACK):
        return None
    fSecondOut = fMaxDis / fSpeed
    if fSecondOut < GAME_FRAME_SECOND:
        fSecondOut = GAME_FRAME_SECOND
        WarobjLog.Alert('%d push time too short %f %f' % (oSkill.m_Base['pfid'], fMaxDis, fSpeed))
    if cl_math.IsZero(vDir):
        if cl_math.IsZero(vStart):
            vStart = oSkill.m_Base['vStart']
        vTar = oVictim.GetPos()
        vDir = cl_math.Vec3Minus(vTar, vStart)
    cbFun = None
    if iCartoonSID > -1:
        dCartoon = oSkill.GetCartoonBySID(iCartoonSID)
        cbFun = Functor(PushMoveEnd, oSkill.m_Base['ActNum'], oSkill.m_Base['AID'], dCartoon)
    iMove = oVictim.m_MoveCtrl.PushMove(oVictim, vDir, fSpeed, fSecondOut, iClientAni = 0, iFace2Dir = iFace2Dir, func = cbFun)
    if not iMove and iCartoonSID > -1:
        oSkill.Call_Out(1, dCartoon['ID'])


def PushHeroVictim(oSkill, vStart, fSpeed, fMaxDis, iPushProbability, downSpeed = 0, fGravaty = 9.8, angle = 0, bDirectRotation = False):
    if 'CurVID' not in oSkill.m_Update:
        return None
    oGame = oSkill.m_Game
    iVictim = oSkill.m_Update['CurVID']
    oVictim = oGame.GetObject(iVictim)
    if not oVictim or not (oVictim.m_MoveCtrl):
        return None
    if oVictim.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
        return None
    if oVictim.QueryBitAttr('LogicKey') & FIGHT3_KEY_IGNOREKNOCKBACK:
        return None
    if oGame.Random(10000) >= iPushProbability:
        return None
    if cl_math.IsZero(vStart):
        vStart = oSkill.m_Base['vStart']
    vTar = oVictim.GetPos()
    fSecondOut = fMaxDis / fSpeed
    vDir = cl_math.Vec3Minus(vTar, vStart)
    if cl_math.IsZero(vDir):
        vFacing = oVictim.GetFacing()
        vDir = (-vFacing[0], 0, -vFacing[2])
    if angle:
        if not bDirectRotation:
            iAttack = oSkill.m_Base['AID']
            vAttface = oGame.GetFacing(iAttack)
            vCross = cl_math.VectorCross3D((vDir[0], 0, vDir[2]), (vAttface[0], 0, vAttface[2]))
            if vCross[1] > 0:
                angle = 360 - angle
        vDir = cl_math.RotateAroundVector(vDir, (0, 1, 0), angle)
    oVictim.m_MoveCtrl.PushMove(oVictim, vDir, fSpeed, fSecondOut, downSpeed, fGravaty)


def BuildPushMoveServant(oSkill, fSpeed, fMaxDis, iCartoonSID):
    oGame = oSkill.m_Game
    iVictim = oSkill.m_Update['CurVID']
    oVictim = oGame.GetObject(iVictim, PY_FLAG_DEAD)
    if not oVictim:
        return None
    if not oVictim.m_FightType & WARRIOR_SERVANT:
        return None
    dCartoon = oSkill.GetCartoonBySID(iCartoonSID)
    iEntityID = dCartoon['EntityID']
    oEntity = oGame.GetObject(iEntityID)
    if not oEntity:
        return None
    vTar = oVictim.GetPos()
    fSecondOut = fMaxDis / fSpeed
    iAngle = int(dCartoon['Angle'])
    iAngle = iAngle + 30 if iAngle > 0 else iAngle - 30
    vFace = cl_math.RotateAroundVector(cl_math.Vec3Minus(dCartoon['Start'], dCartoon['CenterPos']), (0, 1, 0), iAngle)
    vFinalPos = cl_math.Vec3DisplaceDir(dCartoon['CenterPos'], vFace, cl_math.CalDistance3D(dCartoon['Start'], dCartoon['CenterPos']))
    vDir = cl_math.Vec3Minus(vFinalPos, vTar)
    oVictim.m_MoveCtrl.PushMove(oVictim, vDir, fSpeed, fSecondOut, iClientAni = 0)


def PerformThumpMonster(oSkill, iProp, iTime, iClient, iIgnoreStruckCD = 0):
    oGame = oSkill.m_Game
    iVictim = oSkill.m_Update['CurVID']
    oVictim = oGame.GetObject(iVictim, PY_FLAG_DEAD)
    if not oVictim:
        return None
    dData = { }
    if iTime:
        dData['ThumpFrame'] = Time2Frame(iTime)
    if iIgnoreStruckCD:
        dData['IgnoreStruckCD'] = 1
    oVictim.GetThumped(dData, iProp, iClient)


def MonsterTeleport(oSkill, lstPos):
    oGame = oSkill.m_Game
    oAttack = oGame.GetObject(oSkill.m_Base['AID'], PY_FLAG_DEAD)
    if not oAttack or not (oAttack.m_Scene):
        return None
    if lstPos:
        vTar = lstPos[0]
    else:
        vTar = oSkill.m_Collect['TeleportPos']
    vCur = oAttack.GetPos()
    if not oGame.Scene_IsDestPosAccessible(oAttack.m_Scene, vCur, vTar):
        oScene = oGame.m_SceneMgr.GetScene(oSkill.m_Base['Scene'])
        iLevel = oScene.m_Level if oScene else 0
        iPerform = oSkill.m_Base['pfid']
        iMonsterSID = oAttack.m_SID
        WarobjLog.Debug(f'''{oGame.m_ID} {iLevel} {iMonsterSID} {iPerform} telport err {vTar} {vCur}''')
        if not oAttack.m_Agent:
            return None
        vTar = oAttack.m_Agent.GetData('BornPos', None)
        if not vTar:
            return None
    oAttack.WalkTo(vTar)


def MonsterTeleportToListPos(oSkill, iIndex):
    oAttack = oSkill.m_Game.GetObject(oSkill.m_Base['AID'], PY_FLAG_DEAD)
    if not oAttack:
        return None
    lstPos = oSkill.m_Collect.get('TeleportPosList', [])
    if not lstPos or len(lstPos) <= iIndex:
        return None
    vPos = lstPos[iIndex]
    MonsterTeleportToPos(oSkill, vPos)


def MonsterTeleportToPos(oSkill, vPos):
    oAttack = oSkill.m_Game.GetObject(oSkill.m_Base['AID'], PY_FLAG_DEAD)
    if not oAttack:
        return None
    iRet = oSkill.m_Game.Scene_IsDestPosAccessible(oSkill.m_Base['Scene'], oAttack.m_Pos, vPos)
    if not iRet:
        return None
    oAttack.WalkTo(vPos)


def TeleportToNearestSpacePosByPos(oSkill, vPos):
    if not vPos:
        return None
    oAttack = oSkill.m_Game.GetObject(oSkill.m_Base['AID'], PY_FLAG_DEAD)
    if not oAttack:
        return None
    (iRet, vPos) = oSkill.m_Game.Scene_GetSpace(oSkill.m_Base['Scene'], vPos)
    if not iRet:
        return None
    sReason = 'pf%d' % oSkill.m_Base['pfid']
    oAttack.WalkTo(vPos, sReason)


def ServantTeleportToPos(oSkill, vPos):
    if not vPos:
        return None
    oGame = oSkill.m_Game
    oAttack = oGame.GetObject(oSkill.m_Base['AID'], PY_FLAG_DEAD)
    if not oAttack:
        return None
    oScene = oGame.m_SceneMgr.GetScene(oAttack.m_Scene)
    if not oScene:
        return None
    if not oScene.IsInSceneBound(vPos):
        SkillLog.Error('%d %d servant%d %d teleportpos%s err %d min%s max%s' % (oGame.m_ID, oAttack.m_OwnerPlayerID, oAttack.m_SID, oSkill.m_Base['pfid'], vPos, oScene.m_Level, oScene.m_BoundMin, oScene.m_BoundMax))
        return None
    fGroundDis = oGame.Scene_GroundDistance(oAttack.m_Scene, (vPos[0], vPos[1] + 0.2, vPos[2]), 10, PXMASK_GROUNDBLK, oAttack.m_ID)
    vPos = (vPos[0], vPos[1] + 0.2 - fGroundDis, vPos[2])
    sReason = 'pf%d' % oSkill.m_Base['pfid']
    oAttack.WalkTo(vPos, sReason)


def MonsterChooseRushPath(oSkill, iMiddlePosNum, iLeftFirst, iHalfAngle, fLastDis = 0.4):
    lstPath = []
    oGame = oSkill.m_Game
    oAttack = oSkill.GetAttack()
    iVictim = oSkill.m_Base['VID']
    oVictim = oGame.GetObject(iVictim)
    if not oAttack or not oVictim:
        SkillHaltSelf(oSkill)
        return lstPath
    vAttack = oAttack.GetPos()
    vVictim = oVictim.GetPos()
    iScene = oSkill.m_Base['Scene']
    if iScene != oVictim.m_Scene or cl_math.IsEqual(vAttack, vVictim):
        SkillHaltSelf(oSkill)
        return lstPath
    fGroundDis = oSkill.m_Game.Scene_GroundDistance(iScene, (vVictim[0], vVictim[1] + 0.2, vVictim[2]), 3, PXMASK_MOVEBLK, iVictim)
    if fGroundDis < 3:
        vVictim = (vVictim[0], (vVictim[1] - fGroundDis) + 0.1, vVictim[2])
    fPlaneDis = cl_math.CalDistance(vAttack, vVictim)
    oWarMgr = oGame.GetWarMgr()
    iDebug = oWarMgr.Query('DebugRay')
    if iDebug:
        debug.ClearDebugLine(oSkill.m_Game, debug.LINE_NORMAL)
    fHigh = max(vAttack[1], vVictim[1])
    fLow = min(vAttack[1], vVictim[1])
    vStart = (vAttack[0], fHigh, vAttack[2])
    vEnd = (vVictim[0], fHigh, vVictim[2])
    vCenterDir = cl_math.Vec3Minus(vStart, vEnd)
    iDirection = 1 if iLeftFirst else -1
    fIntervalDis = fPlaneDis / (iMiddlePosNum + 2)
    for i in range(iMiddlePosNum, 0, -1):
        iAngle = (oGame.Random(iHalfAngle) + iHalfAngle) * iDirection
        vPos = cl_math.Vec3DestPosDirPlane(vEnd, vCenterDir, fIntervalDis * (i + 2), iAngle)
        vCheckPos = (vPos[0], fLow - 10, vPos[2])
        if iDebug:
            (ox, oy, oz) = vPos
            (tx, ty, tz) = vCheckPos
            debug.DebugLine(oGame, ox, oy, oz, tx, ty, tz, 65280, debug.LINE_NORMAL)
        tRet = oGame.Scene_RaycastSingle(iScene, vPos, vCheckPos, PXMASK_MOVEBLK)
        if tRet[0] != -1:
            vPos = tRet[1]
        lstPath.append(vPos)
        iDirection = -iDirection
    
    fRaduis = oAttack.m_ModelRadius + oVictim.m_ModelRadius + fLastDis
    vNew = (vAttack[0], vVictim[1], vAttack[2])
    if cl_math.IsEqual(vNew, vVictim):
        oScene = oGame.m_SceneMgr.GetScene(iScene)
        iMap = oScene.SID() if oScene else 0
        SkillLog.Debug('ChooseRushPath error %s %s %s %s' % (vAttack, vVictim, iMap, oAttack.m_SID))
        SkillHaltSelf(oSkill)
        return []
    vCheck = cl_math.Vec3DisplacePos(vVictim, vNew, fRaduis)
    vFinal = oSkill.m_Game.Scene_NavMeshRayCast(iScene, vVictim, vCheck)
    lstPath.append(vFinal)
    if iDebug:
        iLen = 0.2
        for vPos in lstPath:
            vertices = []
            vertices.append(cl_math.Vec3Add(vPos, (iLen, 0.05, iLen)))
            vertices.append(cl_math.Vec3Add(vPos, (iLen, 0.05, -iLen)))
            vertices.append(cl_math.Vec3Add(vPos, (-iLen, 0.05, -iLen)))
            vertices.append(cl_math.Vec3Add(vPos, (-iLen, 0.05, iLen)))
            for i in range(4):
                (ox, oy, oz) = vertices[i]
                (tx, ty, tz) = vertices[(i + 1) % 4]
                debug.DebugLine(oGame, ox, oy, oz, tx, ty, tz, 65280, debug.LINE_NORMAL)
            
        
    oSkill.m_Collect['TeleportPosList'] = lstPath
    return lstPath


def StartBackSwing(oSkill, iTime):
    oAttack = oSkill.GetAttack()
    if oAttack:
        oAttack.StartBackSwingSkill(oSkill, Time2Frame(iTime))


def FillBullet(oSkill, iBullet, iNoConsumption):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    iItem = oSkill.m_Base['Weapon']
    oWeapon = oAttack.m_WieldCon.GetItemByID(iItem)
    if not oWeapon:
        return None
    bIsInitWeapon = oWeapon.IsInitWeapon()
    oBulletCom = oWeapon.GetComponent('Bullet')
    if not oBulletCom:
        return None
    iMaxBullet = oBulletCom.MaxBullet()
    iNowBullet = oBulletCom.Bullet()
    if iNowBullet >= iMaxBullet:
        return None
    iBulletSID = oBulletCom.BulletType()
    iBagBullet = oAttack.m_BulletCon.Bullet(iBulletSID)
    iCostPercent = oSkill.m_Collect['FillBulletCostPercent'] if 'FillBulletCostPercent' in oSkill.m_Collect else 100
    if not 'NoFillBulletUse' in oSkill.m_Collect or bIsInitWeapon or iNoConsumption:
        pass
    iNoUseBullet = not iCostPercent
    if not iBagBullet and not iNoUseBullet:
        return None
    if not iBullet or iNowBullet + iBullet > iMaxBullet:
        iBullet = iMaxBullet - iNowBullet
    if iBullet * iCostPercent / 100 > iBagBullet and not iNoUseBullet:
        iBullet = iBagBullet * 100 / iCostPercent
    if not iNoUseBullet:
        iCostBullet = iBullet * iCostPercent / 100
        oAttack.m_BulletCon.BulletModify(iBulletSID, -iCostBullet, 'fillbullet')
    iAdd = oBulletCom.BulletModify(iBullet)
    if iAdd:
        oSkill.m_Collect['SkillFillBullet'] = iAdd


def FillPFBullet(oSkill, iPerform, iAdd, iMaxBulletSync = 0):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    iItem = oSkill.m_Base['Weapon']
    oPerform = oAttack.GetPerform(iPerform, iItem)
    if oPerform and oPerform.m_PFType in (PF_TYPE_SHOOT, PF_TYPE_CONSHOOT, PF_TYPE_CHARGE):
        oPerform.AddPFBullet(iAdd, iMaxBulletSync = iMaxBulletSync)


def ConsumeClipBullet(oSkill, iBullet):
    if iBullet <= 0:
        return None
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    iItem = oSkill.m_Base['Weapon']
    oWeapon = oAttack.m_WieldCon.GetItemByID(iItem)
    if not oWeapon:
        return None
    oBulletCom = oWeapon.GetComponent('Bullet')
    if not oBulletCom:
        return None
    iSend = 0 if oSkill.m_Base['PFType'] == PF_TYPE_BULLETCHANGE else 1
    oSkill.m_Collect['SpecialBullet'] = iBullet
    oBulletCom.BulletModify(-iBullet, iSend)
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_WEAPONPERFROM_COSTBULLET, oAttack, {
        'Skill': oSkill,
        'ItemID': oWeapon.m_ID,
        'Cost': iBullet })


def ConsumeWeaponBagBullet(oSkill, iAmount):
    if iAmount < 0:
        return None
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    iItem = oSkill.m_Base['Weapon']
    oWeapon = oAttack.m_WieldCon.GetItemByID(iItem)
    if not oWeapon:
        return None
    oBulletCom = oWeapon.GetComponent('Bullet')
    if not oBulletCom:
        return None
    iBulletSID = oBulletCom.m_BulletType
    iHasBullet = oAttack.m_BulletCon.Bullet(iBulletSID)
    if iHasBullet == 0:
        return None
    if iHasBullet - iAmount < 0:
        iAmount = iHasBullet
    sKey = oSkill.m_Base['PFKey']
    oAttack.m_BulletCon.BulletModify(iBulletSID, -iAmount, sKey)


def ChangeWeaponBallisticType(oSkill, iAdd, iMax):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    iItem = oSkill.m_Base['Weapon']
    oWeapon = oAttack.m_WieldCon.GetItemByID(iItem)
    if not oWeapon:
        return None
    oWeapon.ChangeBallisticType(iAdd, iMax)


def ChangeMonsterBallisticType(oSkill, iMin, iMax):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    iType = oSkill.m_Game.Random((iMax - iMin) + 1) + iMin
    oSkill.m_CacheData.SetBallisticType(iType)


def SwitchAttPerform(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    iItem = oSkill.m_Base['Weapon']
    oWeapon = oAttack.m_WieldCon.GetItemByID(iItem)
    if not oWeapon:
        return None
    oComPerform = oWeapon.GetComponent('Perform')
    if not oComPerform:
        return None
    oComPerform.SwitchNextAttPerform(oAttack)


def SkillHaltSelf(oSkill):
    oSkill.Halt()


def SkillHaltOther(oSkill, iHaltSkill):
    oGame = oSkill.m_Game
    oSkillMgr = oGame.m_SkillMgr
    lstHaltSkill = oSkillMgr.GetSkillBySID(iHaltSkill)
    iAttack = oSkill.m_Base['AID']
    iWeapon = oSkill.m_Base['Weapon']
    iActNum = oSkill.m_Base['ActNum']
    for oHaltSkill in lstHaltSkill:
        if oHaltSkill.m_Base['AID'] != iAttack:
            continue
        if oHaltSkill.m_Base['ActNum'] == iActNum:
            continue
        if oHaltSkill.m_Base['Weapon'] != iWeapon:
            continue
        oHaltSkill.Halt()
    


def SkillHaltTargetPerform(oSkill, iTarget, iPerform):
    sKey = 'halt%d-%d' % (iTarget, iPerform)
    if sKey in oSkill.m_Collect:
        return None
    oSkill.m_Collect[sKey] = 1
    oGame = oSkill.m_Game
    oSkillMgr = oGame.m_SkillMgr
    lstSkill = oSkillMgr.GetSkillBySID(iPerform)
    for oHaltSkill in lstSkill:
        if oHaltSkill.m_Base['AID'] != iTarget:
            continue
        oHaltSkill.Halt()
    


def AddLogicKey(oSkill, iLogickey):
    
    def ClearBitApply(oSkill):
        oAttack.ClearBitAttr('LogicKey', sKey, iLogickey)

    oAttack = oSkill.GetAttack()
    if oAttack:
        sKey = oSkill.m_Base['PFKey']
        oAttack.AddBitAttr('LogicKey', sKey, iLogickey)
        oSkill.AddEndFunc(ClearBitApply)


def RemoveLogicKey(oSkill, iLogickey):
    oAttack = oSkill.GetAttack()
    if oAttack:
        sKey = oSkill.m_Base['PFKey']
        oAttack.ClearBitAttr('LogicKey', sKey, iLogickey)


def AddIgnoreStateEffect(oSkill, iEffectType):
    
    def ClearBitApply(oSkill):
        oAttack.ClearBitAttr('IgnoreSTEff', sKey, iEffectType)

    oAttack = oSkill.GetAttack()
    if oAttack:
        sKey = oSkill.m_Base['PFKey']
        oAttack.AddBitAttr('IgnoreSTEff', sKey, iEffectType)
        oSkill.AddEndFunc(ClearBitApply)


def RemoveIgnoreStateEffect(oSkill, iEffectType):
    oAttack = oSkill.GetAttack()
    if oAttack:
        sKey = oSkill.m_Base['PFKey']
        oAttack.ClearBitAttr('IgnoreSTEff', sKey, iEffectType)


def SceneEvtShapeInc(oGame, iScene, iAID, iShape, lstArgs, iIncFrame, fShapeInc, dEvtInfo, enterfunc, leavefunc):
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return None
    oAttack = oGame.GetObject(iAID, PY_FLAG_DEAD)
    if not oAttack:
        return None
    iSceneEvtID = dEvtInfo['EvtID']
    oScene.RemoveSceneEvent(iSceneEvtID)
    if iShape == SCENE_EVT_SHAPE_SPHERE:
        fRadius = lstArgs[1]
        lstArgs[1] = fRadius + fShapeInc
    elif iShape == SCENE_EVT_SHAPE_RECTANGLE:
        tHalf = lstArgs[1]
        lstArgs[1] = (tHalf[0] + fShapeInc, tHalf[1] + fShapeInc, tHalf[2] + fShapeInc)
    else:
        return None
    iSceneEvtID = oScene.AddSceneEvent(oAttack, enterfunc, leavefunc, iShape, lstArgs, { })
    dEvtInfo['EvtID'] = iSceneEvtID
    oGame.m_Timer.Call_Out(Functor(SceneEvtShapeInc, oGame, iScene, iAID, iShape, lstArgs, iIncFrame, fShapeInc, dEvtInfo, enterfunc, leavefunc), iIncFrame, 'AddSceneIncSceneEvt%d' % iSceneEvtID)


def AddSceneEventForState(oSkill, vPos, iTime, iShape, dEffArgs, iState, iStateTime, iLeaveRemoveState = 1, iFightType = WARRIOR_MONSTER, iLeaveSetTime = -1):
    
    def ClearSceneEvt(oGame, iScene):
        iSceneEvtID = dEvtInfo['EvtID']
        oGame.m_Timer.Remove_Call_Out('AddSceneIncSceneEvt%d' % iSceneEvtID)
        for iTriggerObj in list(lstInScene):
            SceneLeaveFunc(None, {
                'VID': iTriggerObj })
        
        dAllState.clear()
        oScene = oGame.m_SceneMgr.GetScene(iScene)
        if not oScene:
            return None
        oScene.RemoveSceneEvent(iSceneEvtID)

    
    def SceneEnterFunc(oListener, dMsgInfo):
        iTriggerObj = dMsgInfo['VID']
        if iTriggerObj in lstInScene:
            return None
        obj = oGame.GetObject(iTriggerObj)
        if obj.m_FightType & iFightType != iFightType:
            return None
        lstInScene.add(iTriggerObj)
        oState = cl_state.AddState(obj, iState, iStateTimeType, Time2Frame(iStateTime), dStateArgs)
        if oState:
            lstStateID = dAllState.setdefault(iTriggerObj, [])
            lstStateID.append(oState.m_ID)
            oState.Enable(obj)

    
    def SceneLeaveFunc(oListener, dMsgInfo):
        iTriggerObj = dMsgInfo['VID']
        obj = oGame.GetObject(iTriggerObj)
        if not obj:
            return None
        if iTriggerObj in lstInScene:
            lstInScene.remove(iTriggerObj)
            lstStateID = dAllState.get(iTriggerObj, [])
            if iLeaveRemoveState:
                for iStateID in lstStateID:
                    obj.m_State.RemoveItem(iStateID)
                
                dAllState.pop(iTriggerObj, None)
            elif iLeaveSetTime >= 0:
                for iStateID in lstStateID:
                    oState = obj.m_State.GetItem(iStateID)
                    if oState:
                        oState.SetTime(obj, Time2Frame(iLeaveSetTime), 0)
                

    oGame = oSkill.m_Game
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    if iShape == SCENE_EVT_SHAPE_SPHERE:
        lstArgs = [
            vPos,
            dEffArgs['Radius']]
    elif iShape == SCENE_EVT_SHAPE_RECTANGLE:
        lstArgs = [
            vPos,
            (dEffArgs['HalfX'], dEffArgs['HalfY'], dEffArgs['HalfZ'])]
    else:
        return None
    iScene = oSkill.m_Base['Scene']
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    (enterfunc, leavefunc) = (None, None)
    lstInScene = set()
    dAllState = { }
    enterfunc = SceneEnterFunc
    leavefunc = SceneLeaveFunc
    iSceneEvtID = oScene.AddSceneEvent(oAttack, enterfunc, leavefunc, iShape, lstArgs, { })
    iStateTimeType = STATE_TIME_LIMIT if iStateTime else STATE_TIME_FOREVER
    oReason = oSkill.m_Base['RS'].ExtInfo({
        'ActNum': oSkill.m_Base['ActNum'] })
    dStateArgs = {
        'AID': oAttack.m_ID,
        'RS': oReason,
        'arg': {
            'Pos': vPos } }
    oGame.m_Timer.Call_Out(Functor(ClearSceneEvt, oGame, iScene), Time2Frame(iTime), 'AddSceneClearSceneEvt')
    dEvtInfo = {
        'EvtID': iSceneEvtID }
    iIncFrame = Time2Frame(dEffArgs['IncTime']) if 'IncTime' in dEffArgs else 0
    fShapeInc = dEffArgs['ShapeInc'] if 'ShapeInc' in dEffArgs else 0
    if iIncFrame > 0 and fShapeInc > 0:
        oGame.m_Timer.Call_Out(Functor(SceneEvtShapeInc, oGame, iScene, oAttack.m_ID, iShape, lstArgs, iIncFrame, fShapeInc, dEvtInfo, enterfunc, leavefunc), iIncFrame, 'AddSceneIncSceneEvt%d' % iSceneEvtID)


def SummonAreaMonster(oSkill, iGroup, dAreaWeight, dNumWeight, iDelay = 0, iLimitExtAmount = -1):
    oLevelCtrl = oSkill.m_Game.m_WarMgr.GetComponent('LevelCtrl')
    oAttack = oSkill.GetAttack()
    if oAttack.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
        return None
    oLineNode = oLevelCtrl.GetLineNode(oAttack.m_LineIdx)
    if not oLineNode:
        return None
    oMonsterCtrl = oLineNode.m_MonsterCtrl
    tParam = (iGroup, dAreaWeight, dNumWeight, iDelay, iLimitExtAmount)
    oMonsterCtrl.AddSpawnInfo(tParam)
    oMonsterCtrl.StartSpawn(tParam, Owner = oAttack.m_ID)


def SummonMonster(oSkill, lstMonsterNo):
    oGame = oSkill.m_Game
    oAttack = oSkill.GetAttack()
    iScene = oAttack.m_Scene
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    oLine = oLevelCtrl.GetLineNode(oAttack.m_LineIdx)
    if not oLine:
        return None
    iLevel = oLine.m_LevelNode.m_Level
    oLevelConfData = oLevelCtrl.m_LevelConfData
    for iMonsterNo in lstMonsterNo:
        dInfo = oLevelConfData.GetMonsterInfo(iLevel, oLine.m_Name, iMonsterNo)
        if not dInfo:
            cl_notify.GS2CDebugMsg(oGame, oSkill.m_Base['VID'], '召唤怪物%d未在当前关卡%d中配置' % (iMonsterNo, oLine.m_LevelNode.m_Level))
            continue
        iSID = dInfo['MonsterSID']
        iGrade = dInfo['Grade']
        vPos = dInfo['Pos']
        tFace = dInfo['Facing']
        dAI = dInfo['AIConfig']
        dAI['MonsterNo'] = iMonsterNo
        dAI['GroupID'] = dInfo['GroupID']
        oMonster = oGame.m_ResMgr.CreateMonster(iScene, iSID, vPos, tFace, SIDE_TYPE_MONSTER, iGrade, dAI, oAttack.m_LineIdx, dExtInfo = {
            'Owner': oAttack.m_ID })
        oAttack.m_MonsterSummon[oMonster.m_ID] = iSID
    


def DelMonsterAttacker(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack or oAttack.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
        return None
    oAttack.Remove('Skill')


def DelSkillAttacker(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    if oAttack.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER and oAttack.m_FightType & WARRIOR_SUMMON != WARRIOR_SUMMON:
        return None
    oAttack.Remove('Skill')


def ResetMonsterPerformRecord(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    if oAttack.m_Agent:
        oAttack.m_Agent.SetData('PFRecord', { })


def GetMonsterPerformRecord(oSkill, iTargetPerform = 0):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return 0
    oAgent = oAttack.m_Agent
    if not oAgent:
        return 0
    dRecord = oAgent.GetData('PFRecord')
    if not dRecord:
        return 0
    iPerform = oSkill.m_Base['pfid'] if iTargetPerform == 0 else iTargetPerform
    iTimes = dRecord[iPerform] if iPerform in dRecord else 0
    return iTimes


def EndUsePerform(oSkill, iPerform):
    
    def EndFunc(oSkill):
        oAttack = oSkill.GetAttack()
        if oAttack:
            cl_war.UsePerform(oAttack, pfobj, { })

    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    pfobj = oAttack.GetPerform(iPerform)
    if not pfobj:
        return None
    oSkill.AddEndFunc(EndFunc)


def SaveStart(oSkill):
    oGame = oSkill.m_Game
    iAttack = oSkill.m_Base['AID']
    oAttack = oGame.GetObject(iAttack)
    if not oAttack:
        return None
    oTarget = oGame.GetObject(oSkill.m_Base['VID'])
    if not oTarget:
        WarobjLog.Alert('%s save %s no target' % (iAttack, oSkill.m_Base['VID']))
        return None
    oState = oTarget.m_State.GetItemBySID(STATE_DYING)
    oTarget.Set('Saving', 1)
    oState.StopCount(oTarget)
    oSkill.AddEndFunc(SaveEndFunc)
    cl_notify.SendCommonNotify(oGame, oGame.GetRealPlayers(), 2103, {
        '$$playername1': oAttack.Name(),
        '$$playername2': oTarget.Name() })
    WarobjLog.Info('%s %s save %s %s start' % (oAttack.m_PlayerID, iAttack, oTarget.m_PlayerID, oTarget.m_ID))


def SaveEndFunc(oSkill):
    oTarget = oSkill.m_Game.GetObject(oSkill.m_Base['VID'])
    if not oTarget:
        return None
    oTarget.Set('Saving', 0)
    oState = oTarget.m_State.GetItemBySID(STATE_DYING)
    iSaved = 1
    if oState:
        oState.StartCount(oTarget)
        iSaved = 0
    oAttack = oSkill.GetAttack()
    WarobjLog.Info('%s %s save %s %s end %s' % (oAttack.m_PlayerID if oAttack else 0, oAttack.m_ID, oTarget.m_PlayerID, oTarget.m_ID, iSaved))


def RelifeVictim(oSkill, dRelifeInfo):
    oGame = oSkill.m_Game
    if 'CurVID' in oSkill.m_Update:
        iVictim = oSkill.m_Update['CurVID']
    else:
        iVictim = oSkill.m_Base['VID']
    oTarget = oGame.GetObject(iVictim)
    if not oTarget:
        return None
    dReason = {
        'Type': TYPE_RELIFE_PF,
        'ActNum': oSkill.m_Base['ActNum'],
        'AID': oSkill.m_Base['AID'] }
    oDieElement = oGame.m_WarMgr.GetComponent('PVEDieElement')
    if oDieElement:
        oDieElement.DirectHeroRelife(oTarget, dReason, dRelifeInfo)


def AddClientEffect(oSkill, iShape, tPos, time = 0, vFace = None):
    
    def EndClientEffect(oSkill):
        if 'ClientEffectID' not in oSkill.m_Collect:
            return None
        if iEffectID not in oSkill.m_Collect['ClientEffectID']:
            return None
        dPlayer = oGame.GetRealPlayers()
        cl_snetwar.GS2CDeleteEffect(oGame, oSkill.m_Base['Scene'], iEffectID, dPlayer)
        oSkill.m_Collect['ClientEffectID'].remove(iEffectID)

    oGame = oSkill.m_Game
    iEffectID = oGame.NewNoSceneObjID()
    lstEffect = oSkill.m_Collect.setdefault('ClientEffectID', [])
    lstEffect.append(iEffectID)
    oSkill.m_Collect['ClientEffectID'] = lstEffect
    dPlayer = oGame.GetRealPlayers()
    cl_snetwar.GS2CAddEffect(oGame, oSkill.m_Base['Scene'], iEffectID, iShape, tPos, dPlayer, vFace)
    oSkill.AddEndFunc(EndClientEffect)
    if time:
        oGame.m_Timer.Call_Out(Functor(DelayEndClientEffect, oGame, oSkill.m_Base['AID'], oSkill.m_Base['ActNum'], iEffectID), Time2Frame(time), 'AddClientEffect%s-%s' % (oSkill.m_Base['PFKey'], iEffectID))


def DelayEndClientEffect(oGame, iAttack, iActNum, iEffectID):
    oSkill = oGame.m_SkillMgr.GetSkill(iAttack, iActNum)
    if not oSkill:
        return None
    if 'ClientEffectID' not in oSkill.m_Collect:
        return None
    if iEffectID not in oSkill.m_Collect['ClientEffectID']:
        return None
    oSkill.m_Collect['ClientEffectID'].remove(iEffectID)
    dPlayer = oGame.GetRealPlayers()
    cl_snetwar.GS2CDeleteEffect(oGame, oSkill.m_Base['Scene'], iEffectID, dPlayer)


def AddAreaPlayerState(oSkill, iAttShape, tPos, lstArgs, iStateSID, iTime):
    if iTime < 0:
        return None
    oGame = oSkill.m_Game
    oReason = oSkill.m_Base['RS'].ExtInfo({
        'ActNum': 0 })
    dData = {
        'AID': oSkill.m_Base['AID'],
        'RS': oReason,
        'arg': { },
        'pfid': oSkill.m_Base['pfid'],
        'PFLV': oSkill.m_Base['PFLV'] }
    if iTime:
        iTimeType = STATE_TIME_LIMIT
        iTime = Time2Frame(iTime)
    else:
        iTimeType = STATE_TIME_FOREVER
    iScene = oSkill.m_Base['Scene']
    lstShapeArgs = [
        tPos]
    lstShapeArgs.extend(lstArgs)
    lstHit = cl_math.GetAttackTargetList(oGame, iScene, iAttShape, lstShapeArgs, {
        'Mask': PXMASK_LIVEOBJ })
    for iVictim in lstHit:
        oVictim = oGame.GetObject(iVictim)
        if not oVictim or oVictim.m_FightType != WARRIOR_HERO:
            continue
        oState = cl_state.AddState(oVictim, iStateSID, iTimeType, iTime, dData)
        if oState:
            oState.Enable(oVictim)
    


def DeleteClientEffect(oSkill):
    oGame = oSkill.m_Game
    if 'ClientEffectID' in oSkill.m_Collect:
        dPlayer = oGame.GetRealPlayers()
        for iEffectID in oSkill.m_Collect['ClientEffectID']:
            cl_snetwar.GS2CDeleteEffect(oGame, oSkill.m_Base['Scene'], iEffectID, dPlayer)
        
        oSkill.m_Collect['ClientEffectID'] = []


def SetSkillCartoonCheckData(oSkill, dArg):
    if 'CartoonCheck' not in oSkill.m_Collect:
        oSkill.m_Collect['CartoonCheck'] = { }
    oSkill.m_Collect['CartoonCheck'].update(dArg)


def SendCurCartoonTriggerMsg(oSkill, dInfo = None, sSubMsgKey = ''):
    oSkill.SendCurCartoonTriggerMsg(dInfo = dInfo, sSubMsgKey = sSubMsgKey)


def SetMonsterAttackerPhase(oSkill, iPhase):
    oAttack = oSkill.m_Game.GetObject(oSkill.m_Base['AID'], PY_FLAG_DEAD)
    if oAttack and oAttack.m_FightType & (WARRIOR_MONSTER | WARRIOR_SERVANT):
        oAttack.SetPhase(iPhase)


def CustomPerformAction(oSkill, iPerform, sFuncName, *args):
    func = cl_perform.GetPerformModuleAttr(iPerform, sFuncName)
    if func:
        func(oSkill, *args)


def SetPerformElementType(oSkill, iPerform, iType):
    
    def ClearChange(oSkill):
        oPerform.m_ElementTypeObj.RemoveSetModify(sKey)

    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    if iType & DAM_MASK_ELEMENT:
        sKey = oSkill.m_Base['PFKey']
        oPerform = oAttack.GetPerformIfNoThenNew(iPerform)
        oPerform.m_ElementTypeObj.SetModify(sKey, iType)
        oSkill.AddEndFunc(ClearChange)


def ModifySkillCache(oSkill, sAttr, iVal):
    if sAttr not in oSkill.m_Cache:
        SkillLog.Error('skill%d err, no %s attrcache' % (oSkill.m_Base['pfid'], sAttr))
        return None
    oSkill.m_Cache[sAttr] = iVal


def ModifySkillCacheValue(oSkill, sAttr, iVal):
    ModifySkillCache(oSkill, sAttr, iVal)


def GetElementType(oSkill):
    iElementType = oSkill.m_CacheData.GetElementType()
    if iElementType not in (DAM_TYPE_CORRISION, DAM_TYPE_THUNDER, DAM_TYPE_FIRE):
        iElementType = DAM_TYPE_NORMAL
    return iElementType


def SetCircleSummonParam(oSkill, iPrefab, iRotateTime, iCnt, iAction, iUpTime):
    oGame = oSkill.m_Game
    iScene = oSkill.m_Base['Scene']
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return None
    lstSummon = oScene.GetObjectsByType('Summon')
    for iSummon in lstSummon:
        oSummon = oGame.GetObject(iSummon)
        if oSummon and oSummon.m_Prefab == iPrefab:
            oSummon.SetCircleParam(iRotateTime, iCnt, iAction, iUpTime)
    


def TriggerSceneSummonRotate(oSkill, iPrefab, iAngle):
    oGame = oSkill.m_Game
    iScene = oSkill.m_Base['Scene']
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return None
    lstSummon = oScene.GetObjectsByType('Summon')
    for iSummon in lstSummon:
        oSummon = oGame.GetObject(iSummon)
        if oSummon and oSummon.m_Prefab == iPrefab:
            oSummon.TriggerSummon({
                'Angle': iAngle })
    


def TriggerAssignedCircleSummon(oSkill, lstSummon, iCnt, iAction, iWaitTime, iUpTime):
    oGame = oSkill.m_Game
    iScene = oSkill.m_Base['Scene']
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return None
    lstChosen = ShufferList(oGame, lstSummon, iCnt)
    dCircle = { }
    for sPerfab in lstChosen:
        (iCirclePrefab, iStonePrefab) = sPerfab.split('-')
        lstStone = dCircle.setdefault(int(iCirclePrefab), [])
        lstStone.append(int(iStonePrefab))
    
    for iSummon in oScene.GetObjectsByType('Summon'):
        oSummon = oGame.GetObject(iSummon)
        if not oSummon:
            continue
        if oSummon.m_Prefab in dCircle:
            oSummon.SetCircleParam(iWaitTime, 0, iAction, iUpTime)
            oSummon.SetObstacle(dCircle[oSummon.m_Prefab])
            oSummon.TriggerSummon({ })
    


def SummonObstacleUsePerform(oSkill, iPrefab, iPerform):
    oGame = oSkill.m_Game
    iScene = oSkill.m_Base['Scene']
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return None
    lstSummon = oScene.GetObjectsByType('Summon')
    for iSummon in lstSummon:
        oSummon = oGame.GetObject(iSummon)
        if oSummon and oSummon.m_Prefab == iPrefab:
            oSummon.ObstacleUsePerform(iPerform)
    


def GetObstacleSelfExternalCenter(oSkill):
    iAttack = oSkill.m_Base['AID']
    oGame = oSkill.m_Game
    oAttack = oGame.GetObject(iAttack, PY_FLAG_DEAD)
    if not oAttack or not (oAttack.m_FightType & WARRIOR_OBSTACLE_SIMCTRL):
        return oSkill.m_Base['Start']
    vCenter = oGame.GetCenterPosition(iAttack)
    fHeight = oAttack.m_ModelData.GetModelHeight()
    vMoveDisp = oAttack.m_MoveDisp
    vPos = (vCenter[0], vCenter[1] + fHeight / 2 - vMoveDisp[1] / 2, vCenter[2])
    return vPos


def ChooseSectorList(oSkill, vStart, vCenterDir, iTotalAngle, iTotalCnt, iCnt):
    oGame = oSkill.m_Game
    dAllIndex = dict.fromkeys(range(iTotalCnt), 1)
    iChosen = 0
    dChosenIndex = { }
    for _ in range(iTotalCnt * 5):
        iIndex = ChooseKey(oGame, dAllIndex)
        dAllIndex.pop(iIndex)
        if not iIndex + 1 in dChosenIndex and iIndex - 1 in dChosenIndex:
            dChosenIndex[iIndex] = 1
            iChosen += 1
        if iChosen >= iCnt:
            break
    
    for _ in range(iCnt - iChosen):
        iIndex = ChooseKey(oGame, dAllIndex)
        dAllIndex.pop(iIndex)
        dChosenIndex[iIndex] = 1
    
    lstPos = []
    iIntervalAngle = iTotalAngle // iTotalCnt
    iHalfAngle = iTotalAngle // 2
    iHalfInterval = iIntervalAngle // 2
    for i in range(iTotalCnt):
        if i in dChosenIndex:
            iAngle = i * iIntervalAngle + iHalfInterval
            vTarget = cl_math.Vec3DestPosDirPlane(vStart, vCenterDir, 10, iHalfAngle - iAngle)
            lstPos.append(vTarget)
    
    return lstPos


def SetBarriarPos(oSkill, fDis, fMinDis):
    vEnd = oSkill.m_Base['vEnd']
    return vEnd


def GetAttackerCustomPos(oSkill, sKey):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    vPos = oAttack.Query(sKey)
    if not vPos:
        SkillLog.Error('skill%d not find custom pos %s' % (oSkill.m_Base['pfid'], sKey))
        return oAttack.GetPos()
    return vPos


def SetAttackerCustomPos(oSkill, sKey, vPos):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oAttack.Set(sKey, vPos)


def SetAttackerCustomIntData(oSkill, sKey, iValue):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oAttack.Set(sKey, iValue)


def ChooseValidCannonID(oSkill, iPerform):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return 0
    lstMonster = oAttack.Query('CannonList', [])
    if not lstMonster:
        return 0
    lstRandom = []
    oGame = oSkill.m_Game
    for iMonster in lstMonster:
        oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
        if not oMonster:
            continue
        if not oMonster.m_FightType == WARRIOR_BOSSCANNON:
            continue
        if oMonster.CheckCastingAndBackSwingByPF(iPerform):
            continue
        if oMonster.IsImmobilize():
            continue
        lstRandom.append(iMonster)
    
    if not lstRandom:
        return 0
    iLen = len(lstRandom)
    return lstRandom[oGame.Random(iLen)]


def GetCartoonEntityID(oSkill, sid):
    dCartoon = oSkill.GetCartoonBySID(sid)
    if not dCartoon:
        return 0
    if 'SummonID' not in dCartoon:
        return 0
    return dCartoon['SummonID']


def AdjustRangedPos(oSkill, vAttemptPos, fSize, fGap, iOffset):
    
    def ClearFunc(oSkill):
        dPos.pop(iPosKey, None)

    oGame = oSkill.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oSkill.m_Base['Scene'])
    sSceneKey = 'RangedPos%s' % oSkill.m_Base['pfid']
    iPosKey = oGame.NewNoSceneObjID()
    dPos = oScene.m_CustomData.setdefault(sSceneKey, { })
    lstOverlap = []
    for vPos in dPos.values():
        if cl_math.CheckDistance(vPos, vAttemptPos, fGap):
            lstOverlap.append(vPos)
    
    if lstOverlap:
        if len(lstOverlap) == 1 and not cl_math.IsPlaneEqual(vAttemptPos, lstOverlap[0]):
            vValidPos = cl_math.Vec3DisplacePos(lstOverlap[0], vAttemptPos, fGap)
        else:
            lstPos = []
            lstAll = CreateRectanglePosList(oSkill, vAttemptPos, (fSize, fSize, fSize), 9, fGap, iOffset)
            for vPos in lstAll:
                for vSummonPos in dPos.values():
                    if cl_math.CheckDistance(vPos, vSummonPos, fGap):
                        break
                
            
            if not lstPos:
                SkillLog.Debug('%s %s 选点失败' % (oSkill.m_Base['pfid'], vAttemptPos))
                return vAttemptPos
            idx = oGame.Random(len(lstPos))
            vValidPos = lstPos[idx]
    else:
        vValidPos = vAttemptPos
    dPos[iPosKey] = vValidPos
    oSkill.AddEndFunc(ClearFunc)
    return vValidPos


def AdjustTentaclePos(oSkill, lstAttemptPos, vDir, iBaseMonster, fRadius, fGap, iTotalAngle, iRandomNum, lastDirOnly = 0, heightOffset = 0):
    
    def EndFunc(oSkill):
        if 'SummonCreate' not in oSkill.m_Collect:
            return None
        oGame = oSkill.m_Game
        oScene = oGame.m_SceneMgr.GetScene(oSkill.m_Base['Scene'])
        if not oScene:
            return None
        dMonster = oScene.m_CustomData.setdefault('TentacleID', { })
        iCur = 0
        for iMonster in oSkill.m_Collect['SummonCreate']:
            if iMonster in dMonster:
                continue
            dMonster[iMonster] = (fRadius, lstNewUsed[iCur])
            iCur += 1
            if iCur >= len(lstNewUsed):
                break
        

    oGame = oSkill.m_Game
    iPerform = oSkill.m_Base['pfid']
    oScene = oGame.m_SceneMgr.GetScene(oSkill.m_Base['Scene'])
    vCenter = GetMapCenterPos(oSkill)
    fArc = 3.14 * fRadius
    iPosCnt = int(fArc // fGap) + 1
    fIntervalAngle = iTotalAngle / (iPosCnt - 1)
    dAllTentacle = oScene.m_CustomData.setdefault('TentaclePos', { })
    dUsedPos = dAllTentacle.setdefault(fRadius, { })
    vLast = None
    if lastDirOnly:
        vLast = oScene.m_CustomData.get('LastTentacle%s' % iPerform, None)
    iStart = 0
    iEnd = 180
    lstValid = []
    lstNewUsed = []
    for vPos in lstAttemptPos:
        fDis = cl_math.CalDistance(vPos, vCenter)
        iAngle = cl_math.CalAngle2D(vDir, cl_math.Vec3Minus(vPos, vCenter))
        if dUsedPos:
            lstUsedAngle = sorted(dUsedPos)
            iUsed = 0
            for iUsedAngle in lstUsedAngle:
                if iAngle <= iUsedAngle + fIntervalAngle and iAngle >= iUsedAngle - fIntervalAngle:
                    iUsed = 1
                    break
            
            if iUsed:
                iFound = 0
                iFinalAngle = iAngle
                lstDir = (1, -1)
                if vLast:
                    lstDir = (1 if vPos[0] < vLast[0] else -1,)
                for k in range(1, 180):
                    for iDir in lstDir:
                        i = iAngle + k * iDir
                        if i < iStart or i > iEnd:
                            continue
                        for iUsedAngle in lstUsedAngle:
                            if i <= iUsedAngle + fIntervalAngle and i >= iUsedAngle - fIntervalAngle:
                                break
                        else:
                            iFound = 1
                            iFinalAngle = i
                            break
                    
                    if iFound:
                        break
                
                iAngle = iFinalAngle
                vPos = cl_math.Vec3DestPosDirPlane(vCenter, vDir, fDis, iAngle)
        if heightOffset:
            vPos = (vPos[0], vPos[1] + heightOffset, vPos[2])
        dUsedPos[iAngle] = 1
        lstNewUsed.append(iAngle)
        lstValid.append(vPos)
        if lastDirOnly:
            vLast = vPos
            oScene.m_CustomData['LastTentacle%s' % iPerform] = vLast
    
    if not lstValid:
        lstValid = lstAttemptPos
    if iRandomNum > 0:
        iRandomNum = min(iRandomNum, len(lstValid))
        lstValid = ShufferList(oGame, lstValid, iRandomNum)
    if lstNewUsed:
        oSkill.AddEndFunc(EndFunc)
    return lstValid


def ChooseSlapTentaclePos(oSkill, fRadius, iMove):
    vTarget = CrtArgTargetGroundPos(oSkill)
    vAttack = CrtArgSelfPos(oSkill)
    vCenter = GetMapCenterPos(oSkill)
    vDir = cl_math.Vec3Minus(vAttack, vCenter)
    (x, z) = cl_math.GetFootPoint(vTarget[0], vTarget[2], vAttack[0], vAttack[2], vCenter[0], vCenter[2])
    fDis = cl_math.CalDistance((x, vAttack[1], z), vCenter)
    if z < vCenter[2]:
        fDis = -fDis
    fMoveDis = fRadius - fDis
    vEnd = cl_math.Vec3DisplaceDir(vTarget, vDir, fMoveDis)
    fTargetDis = cl_math.CalDistance(vTarget, vEnd)
    if iMove and fTargetDis > fRadius:
        vEnd = cl_math.Vec3DisplaceDir(vTarget, vDir, fRadius)
        fCenterDis = vEnd[2] - vCenter[2]
        if fCenterDis < 1 or abs(fCenterDis) < fRadius / 2:
            vEnd = (vEnd[0], vEnd[1], vCenter[2] + fRadius)
    return (vEnd[0], vCenter[1], vEnd[2])


def ChooseSweepTentaclePosNew(oSkill, vBase, vTarget, fRadius, fArea):
    vCenter = GetMapCenterPos(oSkill)
    vBase = (vBase[0], vCenter[1], vBase[2])
    vTarget = (vTarget[0], vCenter[1], vTarget[2])
    vEnd = cl_math.Vec3DisplacePos(vCenter, vTarget, fRadius)
    if not cl_math.CheckDistance(vBase, vEnd, fArea):
        vDir = cl_math.Vec3Minus(vBase, vCenter)
        iAngle = int(math.asin(fArea / fRadius) * 180 / math.pi)
        iClock = CalTargetClockWise(oSkill, vBase, vCenter)
        iAngle = iClock * iAngle
        vEnd = cl_math.Vec3DestPosDirPlane(vCenter, vDir, fRadius, iAngle)
    return [
        vEnd]


def ChooseSweepTentaclePos(oSkill, vDir, fRadius, iPosCnt, iTotalAngle, fDodgeDistance):
    lstPos = []
    if iPosCnt <= 0 or iTotalAngle <= 0 or iTotalAngle > 360:
        return lstPos
    oGame = oSkill.m_Game
    iIntervalAngle = iTotalAngle // (iPosCnt - 1)
    vCenter = GetMapCenterPos(oSkill)
    iAngle = 0
    for i in range(iPosCnt):
        vPos = cl_math.Vec3DestPosDirPlane(vCenter, vDir, fRadius, iAngle + iIntervalAngle * i)
        lstPos.append(vPos)
    
    oTarget = oGame.GetObject(oSkill.m_Base['VID'])
    if not oTarget:
        return []
    vTarget = oTarget.GetPos()
    lstValidPos = []
    dDis = { }
    for vPos in lstPos:
        fDistance = cl_math.CalDistance(vPos, vTarget)
        dDis[vPos] = fDistance
        if fRadius - fDodgeDistance * 2 < fDistance and fDistance < fRadius - fDodgeDistance:
            lstValidPos.append(vPos)
    
    if not lstValidPos:
        fMax = 0
        vDefault = None
        for vPos, fDis in dDis.items():
            if fDis < fRadius and fDis > fMax:
                fMax = fDis
                vDefault = vPos
        
        if vDefault:
            lstValidPos = [
                vDefault]
    if not lstValidPos:
        lstValidPos = lstPos
    return lstValidPos


def ChooseTentacleRoundPos(oSkill, fRadius, fArea, iPosCnt, fMinGap, fMaxGap, fMinRange, fMaxRange):
    oGame = oSkill.m_Game
    oAttack = oSkill.GetAttack()
    vAttack = oAttack.GetPos()
    vCenter = GetMapCenterPos(oSkill)
    iMinGapAngle = int(math.asin(fMinGap / fRadius) * 180 / math.pi)
    iMaxGapAngle = int(math.asin(fMaxGap / fRadius) * 180 / math.pi)
    iGapAngle = (iMaxGapAngle - iMinGapAngle) + 1
    iStartAngle = oGame.Random(iMinGapAngle)
    iStartAngle = -iStartAngle if oGame.Random(2) else iStartAngle
    vBaseDir = cl_math.Vec3Minus(vAttack, vCenter)
    fDis = fRadius + fMinRange + oGame.Random((fMaxRange - fMinRange) + 1)
    lstPos = [
        cl_math.Vec3DestPosDirPlane(vCenter, vBaseDir, fDis, iStartAngle)]
    dAngle = {
        -1: iStartAngle,
        1: iStartAngle }
    for i in range(iPosCnt - 1):
        iDir = 1 if i % 2 == 0 else -1
        iAngle = (iMinGapAngle + oGame.Random(iGapAngle)) * iDir
        iShiftAngle = dAngle[iDir] + iAngle
        fDis = fRadius + fMinRange + oGame.Random((fMaxRange - fMinRange) + 1)
        vPos = cl_math.Vec3DestPosDirPlane(vCenter, vBaseDir, fDis, iShiftAngle)
        lstPos.append(vPos)
        dAngle[iDir] = iShiftAngle
    
    lstPos = ShufferList(oGame, lstPos)
    return lstPos


def ChooseTentacleSequencePos(oSkill, vTarget, fRadius, iPosCnt, fGap):
    vCenter = GetMapCenterPos(oSkill)
    fBaseX = vTarget[0]
    fMinX = vCenter[0] - fRadius / 2
    fMaxX = vCenter[0] + fRadius / 2
    iDir = 1 if fBaseX > vCenter[0] else -1
    lstX = [
        fBaseX]
    dX = {
        -1: fBaseX,
        1: fBaseX }
    for _ in range(1, iPosCnt // 2):
        x = dX[iDir] + iDir * fGap
        if x < fMinX or x > fMaxX:
            iDir = -iDir
            x = dX[iDir] + iDir * fGap
        dX[iDir] = x
        lstX.append(x)
        iDir = -iDir
    
    fBaseX = (lstX[0] + lstX[1]) / 2
    lstX.append(fBaseX)
    dX = {
        -1: fBaseX,
        1: fBaseX }
    iDir = 1 if fBaseX > vCenter[0] else -1
    for _ in range(1, iPosCnt // 2):
        x = dX[iDir] + iDir * fGap
        if x < fMinX or x > fMaxX:
            iDir = -iDir
            x = dX[iDir] + iDir * fGap
        dX[iDir] = x
        lstX.append(x)
        iDir = -iDir
    
    lstPos = []
    for x in lstX:
        iAngle = int(math.acos(abs(x - vCenter[0]) / fRadius) * 180 / math.pi)
        z = fRadius * cl_math.SinAngle(iAngle)
        vPos = (x, vCenter[1], z)
        lstPos.append(vPos)
    
    return lstPos


def ChooseTentacleSummonPos(oSkill, vStart, iBaseSummon, fSize, iTryCnt, fGap, iOffset):
    oGame = oSkill.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oSkill.m_Base['Scene'])
    lstSummon = oScene.GetObjectsByType('Summon')
    lstSummonPos = []
    iUseGap = 0
    for iSummon in lstSummon:
        oSummon = oGame.GetObject(iSummon)
        if oSummon and oSummon.m_DataSID == iBaseSummon:
            vSummonPos = oSummon.GetPos()
            lstSummonPos.append(vSummonPos)
            if cl_math.CalDistance(vStart, vSummonPos) < fGap:
                iUseGap = 1
    
    if iUseGap:
        lstPos = []
        lstAll = CreateRectanglePosList(oSkill, vStart, (fSize, fSize, fSize), iTryCnt, fGap, iOffset)
        iScene = oSkill.m_Base['Scene']
        for vPos in lstAll:
            vPos = oGame.Scene_NavMeshRayCast(iScene, vStart, vPos)
            for vSummonPos in lstSummonPos:
                if cl_math.CheckDistance(vPos, vSummonPos, fGap):
                    break
            
        
        if not lstPos:
            SkillLog.Debug('%s %s %s小触手召唤物选点' % (oSkill.m_Base['pfid'], len(lstAll), len(lstSummonPos)))
            lstPos = [
                vStart]
            return lstPos
        idx = oGame.Random(len(lstPos))
        vEnd = lstPos[idx]
    else:
        vEnd = vStart
    vRet = oGame.Scene_RaycastSingle(oSkill.m_Base['Scene'], vEnd, cl_math.Vec3Add(vEnd, (0, -5, 0)), PXMASK_SKILLBLK)
    if vRet[0] != -1:
        vEnd = (vRet[1][0], vRet[1][1] + 0.1, vRet[1][2])
    return [
        vEnd]


def ClearTentacleSummon(oSkill, iBaseSummon, iCnt, iMarkState):
    oGame = oSkill.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oSkill.m_Base['Scene'])
    lstSummon = []
    for iSummon in oScene.GetObjectsByType('Summon'):
        oSummon = oGame.GetObject(iSummon, PY_FLAG_DEAD)
        if oSummon and oSummon.m_DataSID == iBaseSummon:
            lstSummon.append(iSummon)
    
    if len(lstSummon) < iCnt:
        return None
    iRemoveSummon = 0
    lstFree = []
    iMarkFrame = GAME_FRAME_INF
    for iSummon in lstSummon:
        oSummon = oGame.GetObject(iSummon)
        if not oSummon:
            continue
        oMarkState = oSummon.m_State.GetItemBySID(iMarkState)
        if oMarkState and oMarkState.m_CreateFrame < iMarkFrame and not (oSummon.m_CastingSkill):
            iMarkFrame = oMarkState.m_CreateFrame
            iRemoveSummon = iSummon
            continue
        if not oSummon.m_CastingSkill:
            lstFree.append(iSummon)
    
    if not iRemoveSummon:
        lstRandom = lstFree if lstFree else lstSummon
        idx = oGame.Random(len(lstRandom))
        iRemoveSummon = lstRandom[idx]
    oSummon = oGame.GetObject(iRemoveSummon)
    if not oSummon:
        return None
    oSummon.Remove('Skill')


def GetMapCenterPos(oSkill):
    oGame = oSkill.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oSkill.m_Base['Scene'])
    vCenter = oScene.m_CustomData.get('MapCenter', None)
    if not vCenter:
        oAttack = oSkill.GetAttack()
        vCenter = (32, 0, 4.7)
        vCenter = oGame.Scene_NavMeshRayCast(oAttack.m_Scene, vCenter, (vCenter[0], 0, vCenter[2]))
        if not (oAttack.m_LineIdx) and oScene.m_SID != 1030103:
            vCenter = oAttack.GetPos()
        oScene.m_CustomData['MapCenter'] = vCenter
    return vCenter


def CalTargetClockWise(oSkill, vStart, vEnd):
    oTarget = oSkill.m_Game.GetObject(oSkill.m_Base['VID'])
    if not oTarget:
        return 0
    vTarget = oTarget.GetPos()
    vDir = cl_math.Vec3Minus(vEnd, vStart)
    vCompareDir = cl_math.Vec3Minus(vTarget, vStart)
    iClockWise = 1 if cl_math.VectorCross2D(vDir, vCompareDir) < 0 else -1
    return iClockWise


def CreateRectanglePosList(oSkill, vCenter, vSize, iCount, fRadius, iOffset):
    fMaxX = vCenter[0] + vSize[0] * 0.5
    fMinX = vCenter[0] - vSize[0] * 0.5
    fMaxZ = vCenter[2] + vSize[2] * 0.5
    fMinZ = vCenter[2] - vSize[2] * 0.5
    fSize = fRadius * 2
    iGridXCnt = int((fMaxX - fMinX) // fSize)
    iGridZCnt = int((fMaxZ - fMinZ) // fSize)
    iGridCnt = iGridXCnt * iGridZCnt
    oGame = oSkill.m_Game
    lstPoint = []
    lstGrid = [ x for x in range(0, iGridCnt) ]
    lstGridFlag = [ [
1] * (iGridZCnt + 2) for _ in range(iGridXCnt + 2) ]
    iRemainGridCnt = iGridCnt
    lDirx = [
        1,
        1,
        -1,
        -1]
    lDirz = [
        1,
        -1,
        1,
        -1]
    if iRemainGridCnt < iCount:
        SendAlert('err', '技能%d创建矩形范围内随机圆个数不足,需求%d个,可创建%d个' % (oSkill.m_Base['pfid'], iCount, iGridCnt))
    lstFail = []
    lstChoose = []
    for _ in range(iGridCnt):
        if not iCount:
            break
        iFail = 0
        if not iRemainGridCnt:
            break
        iRand = lstGrid[oGame.Random(iRemainGridCnt)]
        lstGrid.remove(iRand)
        iRemainGridCnt -= 1
        iX = iRand // iGridZCnt + 1
        iZ = iRand % iGridZCnt + 1
        for idir in range(0, 4):
            iJugX = iX + lDirx[idir]
            iJugZ = iZ + lDirz[idir]
            if not lstGridFlag[iJugX][iZ] or lstGridFlag[iX][iJugZ]:
                if not lstGridFlag[iJugX][iJugZ]:
                    iFail = 1
                    break
        
        if iFail:
            lstFail.append([
                iX,
                iZ])
            continue
        lstGridFlag[iX][iZ] = 0
        lstChoose.append([
            iX,
            iZ])
        iCount -= 1
    
    if iCount:
        for iX, iZ in lstFail:
            lstChoose.append([
                iX,
                iZ])
            iCount -= 1
            if not iCount:
                break
        
    for iX, iZ in lstChoose:
        x = iX - 1
        z = iZ - 1
        vPos = (x * fSize + fMinX + fRadius, 0, z * fSize + fMinZ + fRadius)
        iMidOffset = iOffset * 0.5
        vOffet = (oGame.Random(iOffset * 100) * 0.01 - iMidOffset, vCenter[1], oGame.Random(iOffset * 100) * 0.01 - iMidOffset)
        vPos = cl_math.Vec3Add(vPos, vOffet)
        lstPoint.append(vPos)
    
    return lstPoint


def CreateAolongRectanglePosList(oSkill, iState, iCount, fRadius, iCheckHight, iSize):
    oGame = oSkill.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oSkill.m_Base['Scene'])
    lstAllPoint = []
    fSize = math.ceil(fRadius * 2)
    iGridCnt = iSize * iSize
    iAreaCnt = iSize // fSize
    iRemainGridCnt = iGridCnt
    lstGrid = [ x for x in range(0, iGridCnt) ]
    iAreaRandomCnt = iAreaCnt + 1
    oAttack = oSkill.GetAttack()
    vAttackPos = oAttack.GetPos()
    for iHero in oScene.GetHeros():
        oHero = oGame.GetObject(iHero)
        if not oHero or not oHero.m_State.GetItemBySID(iState):
            continue
        vHeroPos = oHero.GetPos()
        (iRet, vArrive) = oGame.Scene_GetSpace(oSkill.m_Base['Scene'], vHeroPos)
        if not iRet:
            continue
        if not oGame.Scene_IsDestPosAccessible(oSkill.m_Base['Scene'], vArrive, vAttackPos) or oGame.Scene_IsDestPosAccessible(oSkill.m_Base['Scene'], vAttackPos, vArrive):
            continue
        fMinX = vHeroPos[0] - iSize * 0.5
        fMinZ = vHeroPos[2] - iSize * 0.5
        lstHeroGrid = lstGrid
        iArea = oGame.Random(4)
        lstArea = []
        for iCnt in range(iAreaRandomCnt):
            if iArea == 0:
                x = iCnt * fSize
                z = oGame.Random(fSize)
            elif iArea == 1:
                x = iCnt * fSize
                z = fSize + oGame.Random(fSize)
            elif iArea == 2:
                z = iCnt * fSize
                x = oGame.Random(fSize)
            elif iArea == 3:
                z = iCnt * fSize
                x = fSize + oGame.Random(fSize)
            iPoint = z + x * iSize
            vPos = (x + fMinX, vHeroPos[1], z + fMinZ)
            lstCover = CoverArea(fSize, iSize, iPoint, iGridCnt)
            lstArea.extend(lstCover)
            vPointPos = GetActualPoint(oSkill, fRadius * 2, vPos, lstAllPoint, iCheckHight)
            if vPointPos:
                lstAllPoint.append(vPointPos)
        
        lstHeroGrid = [ i for i in lstHeroGrid if i not in lstArea ]
        iRemainGridCnt = len(lstHeroGrid)
        for _ in range(iCount - iAreaRandomCnt):
            iRand = lstHeroGrid[oGame.Random(iRemainGridCnt)]
            iX = iRand // iSize
            iZ = iRand % iSize
            list = CoverArea(fSize, iSize, iRand, iGridCnt)
            vPos = (iX + fMinX, vHeroPos[1], iZ + fMinZ)
            vPointPos = GetActualPoint(oSkill, fRadius * 2, vPos, lstAllPoint, iCheckHight)
            if vPointPos:
                lstAllPoint.append(vPointPos)
            lstHeroGrid = [ i for i in lstHeroGrid if i not in list ]
            iRemainGridCnt = len(lstHeroGrid)
            if not iRemainGridCnt:
                break
        
    
    return lstAllPoint


def CoverArea(iSize, iCnt, iPoint, iTolCnt):
    lstArea = []
    for x in range(int(iSize)):
        for z in range(int(iSize)):
            iPoint1 = iPoint + x * iCnt + z
            iPoint2 = iPoint - x * iCnt - z
            iPoint3 = iPoint + x * iCnt - z
            iPoint4 = (iPoint - x * iCnt) + z
            if iPoint1 >= 0 and iPoint1 < iTolCnt and iPoint1 not in lstArea:
                lstArea.append(iPoint1)
            if iPoint2 >= 0 and iPoint2 < iTolCnt and iPoint2 not in lstArea:
                lstArea.append(iPoint2)
            if iPoint3 >= 0 and iPoint3 < iTolCnt and iPoint3 not in lstArea:
                lstArea.append(iPoint3)
            if iPoint4 >= 0 and iPoint4 < iTolCnt and iPoint4 not in lstArea:
                lstArea.append(iPoint4)
        
    
    return lstArea


def CheckListPointDis(vPos, lstPos, fDis):
    for vPosChoose in lstPos:
        if cl_math.CheckDistance(vPosChoose, vPos, fDis):
            return 0
    
    return 1


def GetActualPoint(oSkill, fSize, vPos, lstAllPoint, iCheckHight):
    if not CheckListPointDis(vPos, lstAllPoint, fSize):
        return None
    vPos = cl_math.Vec3Add(vPos, (0, iCheckHight, 0))
    vRet = oSkill.m_Game.Scene_RaycastSingle(oSkill.m_Base['Scene'], vPos, cl_math.Vec3Add(vPos, (0, -iCheckHight * 2, 0)), PXMASK_SKILLBLK)
    if vRet[0] == -1:
        return None
    return vRet[1]


def CreateBoxPosList(oSkill, vCenter, vSize, iCount, fRadius, fOffset):
    oGame = oSkill.m_Game
    vMax = cl_math.Vec3Mad(vCenter, vSize, 0.5)
    vMin = cl_math.Vec3Mad(vCenter, vSize, -0.5)
    fSize = fRadius * 2 + fOffset
    iXCnt = int(vSize[0] / fSize)
    iYCnt = int(vSize[1] / fSize)
    iZCnt = int(vSize[2] / fSize)
    iPlaneCnt = iXCnt * iYCnt
    iGridCnt = iPlaneCnt * iZCnt
    iCount = min(iCount, iGridCnt)
    if not iGridCnt:
        return []
    lstGridFlag = [ i for i in range(iGridCnt) ]
    fGridX = (vMax[0] - vMin[0]) / iXCnt
    fGridY = (vMax[1] - vMin[1]) / iYCnt
    fGridZ = (vMax[2] - vMin[2]) / iZCnt
    lstPos = []
    lstGridFlag = ShufferList(oGame, lstGridFlag)
    for i in range(iCount):
        iFlag = lstGridFlag[i]
        (iX, iY, iZ) = DecodeFlag(iFlag, iPlaneCnt, iYCnt)
        fOffsetX = oGame.Random(int(fOffset * 100)) * 0.01 - fOffset * 0.5
        fOffsetY = oGame.Random(int(fOffset * 100)) * 0.01 - fOffset * 0.5
        fOffsetZ = oGame.Random(int(fOffset * 100)) * 0.01 - fOffset * 0.5
        fPosX = fGridX * (iX + 0.5) + fOffsetX + vMin[0]
        fPosY = fGridY * (iY + 0.5) + fOffsetY + vMin[1]
        fPosZ = fGridZ * (iZ + 0.5) + fOffsetZ + vMin[2]
        lstPos.append((fPosX, fPosY, fPosZ))
    
    return lstPos


def CreatePosOnCircle(oSkill, vCenter, fRadius, iNum):
    (x, y, z) = vCenter
    iAngle = 360 // iNum
    lstPos = []
    iCurAngle = 0
    for _ in range(iNum):
        x1 = x + fRadius * cl_math.CosAngle(iCurAngle)
        z1 = z + fRadius * cl_math.SinAngle(iCurAngle)
        lstPos.append((x1, y, z1))
        iCurAngle += iAngle
    
    return lstPos


def DecodeFlag(iFlag, iPlaneCnt, iCntY):
    iPlane = iFlag % iPlaneCnt
    iY = iFlag // iPlaneCnt
    iX = iPlane % iCntY
    iZ = iPlane // iCntY
    return (iX, iY, iZ)


def CreateBeaconSummon(oSkill, iSummon, vPos, iTime, iMaxCount = 1, iMaxTriggerCnt = 0, bOnly = False):
    oGame = oSkill.m_Game
    iAttack = oSkill.m_Base['AID']
    oAttack = oGame.GetObject(iAttack)
    if not oAttack:
        return None
    iVictim = oSkill.m_Update['CurVID'] if 'CurVID' in oSkill.m_Update else 0
    if iVictim:
        oVictim = oGame.GetObject(iVictim, PY_FLAG_DEAD)
        if not oVictim:
            return None
    iSrcWeapon = oSkill.m_Base['Weapon']
    iSrcPerform = oSkill.m_Base['pfid']
    lstSameSummon = []
    for iCurSummon in list(oAttack.m_SummonDict):
        oCurSummon = oGame.GetObject(iCurSummon)
        if not oCurSummon:
            continue
        if oCurSummon.m_FightType & WARRIOR_BEACON != WARRIOR_BEACON:
            continue
        if oCurSummon.m_SrcPerform != iSrcPerform or oCurSummon.m_SrcWeapon != iSrcWeapon:
            continue
        if bOnly and oCurSummon.m_AttachTarget == iVictim:
            oCurSummon.Remove('Repeat')
            continue
        lstSameSummon.append(oCurSummon)
    
    for _ in range((len(lstSameSummon) - iMaxCount) + 1):
        oRemoveSummon = lstSameSummon.pop(0)
        oRemoveSummon.Remove('OverMaxCount')
    
    dAddInfo = {
        'Shape': MODEL_TYPE_POINT,
        'Side': oSkill.m_Cache['Side'],
        'Origin': vPos,
        'Owner': iAttack,
        'Weapon': iSrcWeapon,
        'Victim': iVictim,
        'AttachPart': oSkill.m_Update['CurHitArea'] if 'CurHitArea' in oSkill.m_Update else 0,
        'SrcPerform': iSrcPerform,
        'MaxTriggerCnt': iMaxTriggerCnt }
    oSummon = oGame.m_ResMgr.CreateSummon(oSkill.m_Base['Scene'], iSummon, dAddInfo)
    if not oSummon:
        return None
    oSummon.SetLifeFrame(Time2Frame(iTime))


def TriggerVictimBeaconSummon(oSkill, iCnt):
    if 'CurVID' not in oSkill.m_Update:
        return None
    iVictim = oSkill.m_Update['CurVID']
    oGame = oSkill.m_Game
    iAttack = oSkill.m_Base['AID']
    oAttack = oGame.GetObject(iAttack)
    if not oAttack:
        return None
    iSrcWeapon = oSkill.m_Base['Weapon']
    for iCurSummon in list(oAttack.m_SummonDict):
        oCurSummon = oGame.GetObject(iCurSummon)
        if not oCurSummon:
            continue
        if oCurSummon.m_FightType & WARRIOR_BEACON != WARRIOR_BEACON:
            continue
        if oCurSummon.m_AttachTarget != iVictim:
            continue
        if oCurSummon.m_SrcWeapon != iSrcWeapon:
            continue
        oCurSummon.TriggerSummon({
            'TriggerCnt': iCnt })
    


def CheckVictimHasBeaconSunmon(oSkill, iVictim):
    if 'CurVID' not in oSkill.m_Update:
        return False
    oGame = oSkill.m_Game
    iAttack = oSkill.m_Base['AID']
    oAttack = oGame.GetObject(iAttack)
    if not oAttack:
        return False
    iSrcWeapon = oSkill.m_Base['Weapon']
    for iCurSummon in oAttack.m_SummonDict:
        oCurSummon = oGame.GetObject(iCurSummon)
        if not oCurSummon:
            continue
        if oCurSummon.m_FightType & WARRIOR_BEACON != WARRIOR_BEACON:
            continue
        if oCurSummon.m_AttachTarget != iVictim:
            continue
        if oCurSummon.m_SrcWeapon != iSrcWeapon:
            continue
        return True
    
    return False


def GetBeaconCount(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return 0
    iItem = oSkill.m_Base['Weapon']
    oWeapon = oAttack.m_WieldCon.GetItemByID(iItem)
    if not oWeapon:
        return 0
    iMax = oWeapon.m_ExtItemAttr['MaxBeacon'] if 'MaxBeacon' in oWeapon.m_ExtItemAttr else 0
    return min(iMax, oSkill.m_CacheData.m_BeaconCount)


def SummonAttachHitTarget(oSkill, iSummon, bClearAttach, iTarget, vFixOffset, parentName = None):
    oGame = oSkill.m_Game
    oSummon = oGame.GetObject(iSummon)
    if not oSummon:
        return None
    if oSummon.m_FightType != WARRIOR_MONSTERBEACON:
        return None
    if bClearAttach:
        oSummon.ClearAttachTarget()
    elif not iTarget and 'CurVID' in oSkill.m_Update:
        iTarget = oSkill.m_Update['CurVID']
    oSummon.SetAttachTarget(iTarget)


def SetShapeInfo(oSkill, bValid, vPos, iShape, lstArgs):
    if bValid:
        oSkill.m_Collect['ShapeInfo'] = (vPos, iShape, lstArgs)
    elif 'ShapeInfo' in oSkill.m_Collect:
        oSkill.m_Collect.pop('ShapeInfo')


def CheckPosInSkillRangeBySID(oSkill, vPos, iCheckSID):
    oSkillMgr = oSkill.m_Game.m_SkillMgr
    lstSkill = oSkillMgr.GetSkillBySID(iCheckSID)
    for oSkill in lstSkill:
        if 'ShapeInfo' in oSkill.m_Collect:
            (vOrigin, iShape, lstArgs) = oSkill.m_Collect['ShapeInfo']
            if iShape == ATT_SHAPE_SPHERE:
                fRadius = lstArgs[0]
                fDis = cl_math.CalDistance3D(vPos, vOrigin)
                if fDis <= fRadius:
                    return True
    
    return False


def CheckSkillRandomInRange(oSkill, iMin, iMax):
    iRand = oSkill.m_CacheData.m_Random
    if iMin <= iRand and iRand <= iMax:
        return True
    return False


def GetRandomInRange(oSkill, iMin, iMax):
    if iMax > iMin:
        iRand = oSkill.m_CacheData.m_Random
        iRangeLen = (iMax - iMin) + 1
        fCube = 100 / iRangeLen
        index = int(iRand / fCube)
        return iMin + index
    return iMin


def GetJumpAttackSkillVelocity(oSkill):
    fSpeed = oSkill.m_CacheData.m_SignSpeed
    return fSpeed


def GetWarriorModelRadius(oSkill, iFightType, iWarriorSID, sModelKey):
    oGame = oSkill.m_Game
    if iFightType == WARRIOR_MONSTER:
        clsMonsterData = oGame.GetWarData().GetMonsterData(iWarriorSID)
        if not clsMonsterData:
            SkillLog.Error('skill%d getwarriormodeldata err monster:%d' % (oSkill.m_Base['pfid'], iWarriorSID))
            return 0
        iShape = clsMonsterData.m_Shape
    elif iFightType == WARRIOR_SUMMON:
        clsSummonData = oGame.GetWarData().GetSummonData(iWarriorSID)
        if not clsSummonData:
            SkillLog.Error('skill%d getwarriormodeldata err summon: %d' % (oSkill.m_Base['pfid'], iWarriorSID))
            return 0
        iShape = clsSummonData.m_Shape
    else:
        SkillLog.Error('skill%d getwarriormodeldata err invalid fighttype:%d' % (oSkill.m_Base['pfid'], iFightType))
        return 0
    tModelData = cl_modeldefine.GetModelDefine(iShape, sModelKey)
    if not tModelData:
        return 0
    return tModelData[0]


def GetSummonPosByBoxSplit(oSkill, fSize, iNum, iSummonRadius, bCheckSpace, dNumPivot, dPosInfo, bBaseVictim, iAngle = 0):
    if iNum <= 0:
        return []
    fBoxSize = fSize / iNum
    if fBoxSize < iSummonRadius * 2:
        SkillLog.Error('skill%d setsummonpos err, boxsize %s to small, summon radius %s' % (oSkill.m_Base['pfid'], fBoxSize, iSummonRadius))
        return []
    oGame = oSkill.m_Game
    oTarget = oGame.GetObject(oSkill.m_Base['VID']) if bBaseVictim else oSkill.GetAttack()
    if not oTarget:
        return []
    lstSummonPos = []
    iScene = oTarget.m_Scene
    iModelRadius = oTarget.m_ModelRadius
    vAttackPos = oTarget.GetPos()
    if bBaseVictim:
        vAttackPos = cl_math.Vec3Add(vAttackPos, (0, 0.1, 0))
    (px, py, pz) = vAttackPos
    if dPosInfo and 'CenterY' in dPosInfo:
        py += oTarget.m_ModelHeight / 2
    iFloatY = 0
    if dPosInfo and 'FloatY' in dPosInfo:
        fFloatY = dPosInfo['FloatY']
        iFloatY = int(fFloatY * 100)
    iCenterIndex = (iNum - 1) / 2
    fOffsetTolerance = fBoxSize / 2 - iSummonRadius
    iMinDis = dPosInfo['MinDis'] if 'MinDis' in dPosInfo else 0
    iIgnoreTargetPos = dPosInfo['IgnoreTargetPos'] if 'IgnoreTargetPos' in dPosInfo else 0
    vFacing = oTarget.GetFacing()
    for iRow in range(iNum):
        x = px + (iRow - iCenterIndex) * fBoxSize
        for iCol in range(iNum):
            z = pz + (iCol - iCenterIndex) * fBoxSize
            if not iIgnoreTargetPos and abs(x - px) < iModelRadius + fBoxSize / 2 and abs(z - pz) < iModelRadius + fBoxSize / 2:
                continue
            vTmpPos = (x, py, z)
            if iFloatY > 0:
                yFloat = (oGame.Random(iFloatY * 2) - iFloatY) / 100
                vTmpPos = cl_math.Vec3Add(vTmpPos, (0, yFloat, 0))
            if iMinDis and cl_math.CheckDistance(vAttackPos, vTmpPos, iMinDis):
                continue
            if bCheckSpace:
                (iRet, vBoxPos) = oGame.Scene_GetSpace(iScene, vTmpPos)
                if not iRet:
                    continue
                if abs(vBoxPos[0] - x) > fOffsetTolerance or abs(vBoxPos[2] - z) > fOffsetTolerance:
                    continue
            vBoxPos = vTmpPos
            if not bBaseVictim:
                if bCheckSpace:
                    tRetPos = oGame.Scene_NavMeshRayCast(iScene, vAttackPos, vBoxPos)
                    if tRetPos != vBoxPos:
                        continue
                bAnyHit = oGame.Scene_RaycastAnyHit(iScene, vAttackPos, vBoxPos, PXMASK_BLOCK)
                if bAnyHit:
                    continue
                continue
            if iAngle and cl_math.CheckVector2Angle(vFacing, cl_math.Vec3Minus(vBoxPos, vAttackPos), iAngle):
                continue
            lstSummonPos.append(vBoxPos)
        
    
    iChooseNum = ChooseKey(oGame, dNumPivot)
    if not iChooseNum:
        return []
    iLen = len(lstSummonPos)
    iChooseNum = min(iChooseNum, iLen)
    iLeft = iLen
    for idx in range(iChooseNum):
        iRandIndex = oGame.Random(iLeft)
        lstSummonPos[iRandIndex] = lstSummonPos[iLeft - 1]
        lstSummonPos[iLeft - 1] = lstSummonPos[iRandIndex]
        iLeft -= 1
    
    lstChoosePos = lstSummonPos[-iChooseNum:]
    return lstChoosePos


def CreateRandomNumWarriorAtPointPos(oSkill, lstPos, iFightType, dWarriorSIDPivot, dInfo, tFace = None):
    from cl_resmgr.aitempparam import GetAIConfParam
    if not lstPos:
        return None
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oGame = oSkill.m_Game
    iScene = oAttack.m_Scene
    if not tFace:
        tFace = oAttack.GetFacing()
    tLine = oAttack.m_LineIdx
    iGrade = oAttack.m_AddGrade if 'SameGrade' in dInfo else 0
    if iFightType == WARRIOR_MONSTER:
        dAI = {
            'AIParamLv': PARAM_LEVEL_MEDIUM_HIGH,
            'AIMethod': MONSTERAI_TYPE_DEFAULT }
        dHateSearchAI = GetAIConfParam(MONSTERAI_TYPE_HATESEARCH, PARAM_LEVEL_MEDIUM_HIGH)
        dAI.update(dHateSearchAI)
        iFollowDie = 1 if 'FollowDie' in dInfo else 0
        iNoEnemyNotify = False if 'NoEnemyNotify' in dInfo else True
        iSuperLevel = oAttack.SuperLevel() if 'SameSuper' in dInfo else 0
        if iSuperLevel:
            (iPlusPF, iAfPF) = oAttack.Query('MonsterSuper', (0, 0))
        lstSummon = oSkill.m_Collect.setdefault('SummonCreate', [])
        lstMonsterNum = []
        if 'MonsterRate' in dInfo and dInfo['MonsterRate']:
            iAllNum = len(lstPos)
            for iSID, iRate in dInfo['MonsterRate'].items():
                iNum = iRate * iAllNum // 100
                if iNum > 0:
                    lstMonsterNum.append((iSID, iNum))
            
        for vPos in lstPos:
            if lstMonsterNum:
                (iWarriorSID, iNum) = lstMonsterNum[0]
                iNum -= 1
                if iNum:
                    lstMonsterNum[0] = (iWarriorSID, iNum)
                else:
                    lstMonsterNum.pop(0)
            iWarriorSID = ChooseKey(oGame, dWarriorSIDPivot)
            dInfo.update({
                'Owner': oAttack.m_ID,
                'NoEnemyNotify': iNoEnemyNotify })
            oMonster = oGame.m_ResMgr.CreateMonster(iScene, iWarriorSID, vPos, tFace, SIDE_TYPE_MONSTER, iGrade, dAI, tLine, dInfo)
            if oAttack.m_FightType & WARRIOR_MONSTER == WARRIOR_MONSTER:
                oAttack.m_MonsterSummon[oMonster.m_ID] = iWarriorSID
            if iFollowDie:
                oAttack.m_FollowDieObjs[oMonster.m_ID] = 1
            lstSummon.append(oMonster.m_ID)
            if 'MonsterAutoUsePerform' in dInfo:
                WarriorUsePerform(oSkill, oMonster.m_ID, dInfo['MonsterAutoUsePerform'], { }, False)
            if iSuperLevel:
                oMonster.MonsterSuper(iSuperLevel, iPlusPF, iAfPF)
        
    elif iFightType == WARRIOR_SUMMON:
        dAddInfo = {
            'Owner': oAttack.m_ID,
            'Side': oAttack.m_Side,
            'Grade': oAttack.m_Grade,
            'Origin': oAttack.GetPos(),
            'Facing': tFace,
            'SrcPerform': oSkill.m_Base['pfid'] }
        if 'Capsule' in dInfo:
            iWarriorSID = ChooseKey(oGame, dWarriorSIDPivot)
            clsSummonData = oGame.m_WarData.GetSummonData(iWarriorSID)
            tModelData = cl_modeldefine.GetModelDefine(clsSummonData.m_Shape, 'NavMesh')
            dShapeInfo = {
                'Shape': MODEL_TYPE_CAPSULE,
                'Angle': (0, 0, 0),
                'Scale': (1, 1, 1),
                'Center': (0, 0, 0),
                'Size': (tModelData[1], tModelData[0], 0) }
            dAddInfo.update(dShapeInfo)
        elif 'Radius' in dInfo:
            fRadius = dInfo['Radius']
            dShapeInfo = {
                'Shape': MODEL_TYPE_SPHERE,
                'Angle': (0, 0, 0),
                'Scale': (1, 1, 1),
                'Center': (0, 0, 0),
                'Size': (fRadius, fRadius, fRadius) }
            if 'ScaleX' in dInfo and 'ScaleY' in dInfo and 'ScaleZ' in dInfo:
                dShapeInfo['Scale'] = (dInfo['ScaleX'], dInfo['ScaleY'], dInfo['ScaleZ'])
            dAddInfo.update(dShapeInfo)
        elif 'Box' in dInfo:
            iWarriorSID = ChooseKey(oGame, dWarriorSIDPivot)
            clsSummonData = oGame.m_WarData.GetSummonData(iWarriorSID)
            vBox = cl_modeldefine.GetModelDefine(clsSummonData.m_Shape, 'Box')
            radiansy = cl_math.CalRotate2D(tFace)
            dShapeInfo = {
                'Angle': (0, radiansy, 0),
                'Center': (0, vBox[1] / 2, 0),
                'Scale': (1, 1, 1),
                'Shape': MODEL_TYPE_BOX,
                'Size': vBox }
            dAddInfo.update(dShapeInfo)
        lstSummonID = oSkill.m_Collect.setdefault('SummonCreate', [])
        for vPos in lstPos:
            iWarriorSID = ChooseKey(oGame, dWarriorSIDPivot)
            dAddInfo['Origin'] = vPos
            oSummon = oGame.m_ResMgr.CreateSummon(iScene, iWarriorSID, dAddInfo, tLine, iGrade)
            lstSummonID.append(oSummon.m_ID)
        


def GetSkillSummonCreate(oSkill):
    if 'SummonCreate' not in oSkill.m_Collect:
        return []
    return oSkill.m_Collect['SummonCreate']


def ClearSkillSummonCreateCollect(oSkill):
    oSkill.m_Collect['SummonCreate'] = []


def GetSceneObjPos(oSkill, objID):
    oGame = oSkill.m_Game
    oSceneObj = oGame.GetObject(objID)
    if not oSceneObj:
        return (0, 0, 0)
    return oSceneObj.GetPos()


def GetCartoonLoopID(oSkill, sid):
    dCartoon = oSkill.GetCartoonBySID(sid)
    if 'LoopID' not in dCartoon:
        return 0
    return dCartoon['LoopID']


def SetSummonLifeTime(oSkill, iSummon, iLifeTime):
    oSummon = oSkill.m_Game.GetObject(iSummon)
    if not oSummon or oSummon.m_FightType & WARRIOR_SUMMON != WARRIOR_SUMMON:
        return None
    oSummon.SetLifeFrame(Time2Frame(iLifeTime))


def GetMonsterSummonCnt(oSkill, iSummonSID):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oGame = oSkill.m_Game
    iNowCnt = 0
    for iSummonID in oAttack.m_MonsterSummon:
        oSummon = oGame.GetObject(iSummonID, PY_FLAG_DEAD)
        if oSummon and oSummon.m_SID == iSummonSID:
            iNowCnt += 1
    
    return iNowCnt


def AttackerUsePerform(oSkill, iPerform, dCustomData, iDelay = 0, iVictim = 0):
    
    def DelayAttackerUsePerform(dData):
        cl_war.UsePerform(oAttack, oPerform, dData)

    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oPerform = oAttack.GetPerform(iPerform)
    if not oPerform:
        return None
    dData = {
        'Custom': dCustomData,
        'VID': oSkill.m_Base['VID'] }
    if iVictim:
        oVictim = oSkill.m_Game.GetObject(iVictim, PY_FLAG_DEAD)
        if not oVictim:
            return None
        dData['VID'] = iVictim
    if not iDelay:
        DelayAttackerUsePerform(dData)
    else:
        oAttack.Call_Out(Functor(DelayAttackerUsePerform, dData), Time2Frame(iDelay), f'''DelayAttackerUsePerform{oSkill.m_SkillID}''')


def WarriorUsePerform(oSkill, iWarrior, iPerform, dCustomData, bInherit, iTargetVID = 0):
    oGame = oSkill.m_Game
    oWarrior = oGame.GetObject(iWarrior)
    if not oWarrior:
        return None
    oPerform = oWarrior.GetPerformIfNoThenNew(iPerform)
    if not oPerform:
        return None
    if bInherit:
        dCustomData['dCache'] = dict(oSkill.m_Cache)
    dData = {
        'Custom': dCustomData,
        'VID': iTargetVID if iTargetVID else oSkill.m_Base['VID'] }
    cl_war.UsePerform(oWarrior, oPerform, dData)


def ServantUsePerform(oSkill, iPerform, dCustomData):
    oGame = oSkill.m_Game
    oAttack = oSkill.GetAttack()
    if not oAttack or not (oAttack.m_FightType & WARRIOR_HERO):
        return None
    oScene = oGame.m_SceneMgr.GetScene(oAttack.m_Scene)
    if not oScene or oAttack.m_ID not in oScene.m_Heros:
        return None
    iServant = oAttack.m_Servant
    oServant = oGame.GetObject(iServant, PY_FLAG_DEAD)
    if not oServant or not (oServant.m_Agent):
        return None
    oAgent = oServant.m_Agent
    oAgent.SetData('HeroCtrlPF', {
        'pfid': iPerform,
        'Custom': dCustomData })
    oAgent.m_GameSpace.CallDelayUpdate(oAgent, 1)


def GetSkillCustomData(oSkill, sKey, defaultValue = 0):
    dCustom = oSkill.m_Custom
    if sKey not in dCustom:
        return defaultValue
    return dCustom[sKey]


def SetSkillCustomDataInt(oSkill, sKey, iVal):
    oSkill.m_Custom[sKey] = iVal


def SetSkillCustomDataV3List(oSkill, sKey, lstData):
    oSkill.m_Custom[sKey] = lstData


def ExtendSkillCustomDataV3List(oSkill, sKey, lstData):
    if sKey not in oSkill.m_Custom:
        oSkill.m_Custom[sKey] = []
    oSkill.m_Custom[sKey].extend(lstData)


def GetPlayRound(oSkill):
    oGame = oSkill.m_Game
    return oGame.m_WarMgr.m_Round


def GetPlayCycle(oSkill):
    oGame = oSkill.m_Game
    return oGame.m_WarMgr.m_Cycle


def GetGamePlayMode(oSkill):
    oWarMgr = oSkill.m_Game.m_WarMgr
    return GetPlayMode(oWarMgr.m_SID)


def CheckGamePlayMode(oSkill, iPlayMode):
    oWarMgr = oSkill.m_Game.m_WarMgr
    if iPlayMode == GetPlayMode(oWarMgr.m_SID):
        return True
    return False


def SetSkillCacheExtraTrajectory(oSkill, iExtraTrajectory):
    if oSkill.m_CheckType == CRT_CHECK_SERVER:
        oSkill.m_CacheData.SetExtraTrajectory(iExtraTrajectory)


def GetSkillCacheExtraTrajectory(oSkill):
    return oSkill.m_CacheData.GetExtraTrajectory()


def ServerSendSkillCache(oSkill, lstChoose):
    cl_perform.net.GS2CSkillThroughInfo(oSkill, {
        'Choose': lstChoose })


def GetSkillCacheData(oSkill, iIndex):
    return cl_perform.skillcache.GetSkillCacheByIndex(oSkill, iIndex)


def SetSkillCacheData(oSkill, iChooseIndex, objValue):
    cl_perform.skillcache.SetSkillCacheByIndex(oSkill, iChooseIndex, objValue)


def GetSkillCacheAttrName(iChooseIndex):
    return cl_perform.skillcache.GetSkillCacheAttrNameByIndex(iChooseIndex)


def AddItemToLstInt(oSkill, iValue):
    lstInt = cl_perform.skillcache.GetSkillCacheByIndex(oSkill, SKILLCACHE_LSTINT)
    if iValue in lstInt:
        return None
    lstInt.append(iValue)


def AddItemToLstPos(oSkill, vPos, bCheckSame = False):
    lstPos = cl_perform.skillcache.GetSkillCacheByIndex(oSkill, SKILLCACHE_LSTPOS)
    if bCheckSame and vPos in lstPos:
        return None
    lstPos.append(vPos)


def AddSkillCacheData(oSkill, iIndex):
    pass


def SetCartoonDependState(oSkill, sid, iState):
    dCartoon = oSkill.GetCartoonBySID(sid)
    dCartoon['DependState'] = iState


def SetAttackerForceDistance(oSkill, fDis):
    oAttack = oSkill.GetAttack()
    if oAttack:
        oAttack.m_ForceDistance = fDis


def ClearAttackerForceDistance(oSkill):
    oAttack = oSkill.GetAttack()
    if oAttack:
        oAttack.m_ForceDistance = 0


def SwitchAttackerPhyAble(oSkill, iEnable):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    if not oAttack.m_PhyModel:
        return None
    if iEnable:
        oAttack.m_PhyModel.SetCtrlFlag(CTRL_FLAG_FOR_ALL, 1)
    else:
        oAttack.m_PhyModel.SetCtrlFlag(CTRL_FLAG_FOR_ALL, 0)


def SwitchAttackerNavAble(oSkill, iEnable):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    if not oAttack.m_MoveCtrl:
        return None
    if iEnable:
        oAttack.UnForbid(cl_forbid.NAVSEEK_RULE, 'NavMove')
        oAttack.m_MoveCtrl.E_Enable()
    else:
        oAttack.Forbid(cl_forbid.NAVSEEK_RULE, 'NavMove')
        oAttack.m_MoveCtrl.E_Disable()


def SwitchTargetsPhyAble(oSkill, iEnable, lstTarget):
    oGame = oSkill.m_Game
    for iTarget in lstTarget:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget or not (oTarget.m_PhyModel):
            continue
        if iEnable:
            oTarget.m_PhyModel.SetCtrlFlag(CTRL_FLAG_FOR_ALL, 1)
            continue
        oTarget.m_PhyModel.SetCtrlFlag(CTRL_FLAG_FOR_ALL, 0)
    


def SwitchTargetsNavAble(oSkill, iEnable, lstTarget):
    oGame = oSkill.m_Game
    for iTarget in lstTarget:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget or not (oTarget.m_MoveCtrl):
            continue
        if iEnable:
            oTarget.UnForbid(cl_forbid.NAVSEEK_RULE, 'NavMove')
            oTarget.m_MoveCtrl.E_Enable()
            continue
        oTarget.Forbid(cl_forbid.NAVSEEK_RULE, 'NavMove')
        oTarget.m_MoveCtrl.E_Disable()
    


def DelStonePillar(oSkill, iBuild, iDelay = 8):
    oGame = oSkill.m_Game
    oVictim = oGame.GetObject(iBuild, PY_FLAG_DEAD)
    if not oVictim or oVictim.m_FightType != WARRIOR_STONEPILLAR:
        return None
    iFrame = Time2Frame(iDelay)
    if iFrame:
        oVictim.Call_Out(Functor(DelayDelStonePillar, oVictim), iFrame, 'DelayRemoveStone')
    else:
        oVictim.Remove('Skill')


def DelayDelStonePillar(oVictim):
    oVictim.Remove('Skill')


def CreateStonePillar(oSkill, objSID, action, origin, iModelType, lstArgs, iMaxFallPercent, iMaxRotate):
    oGame = oSkill.m_Game
    oAttack = oGame.GetObject(oSkill.m_Base['AID'], PY_FLAG_DEAD)
    if not oAttack:
        return None
    iFallPercent = oGame.Random(iMaxFallPercent % 100)
    iHeight = lstArgs[1] if iModelType == MODEL_TYPE_BOX else lstArgs[0]
    fFall = iHeight * (100 + iFallPercent) / 100
    (x, y, z) = origin
    vOrigin = [
        x,
        y - fFall,
        z]
    vDest = [
        x,
        (y - fFall) + iHeight,
        z]
    iRotate = oGame.Random(iMaxRotate % 360)
    dAddData = {
        'Angle': [
            0,
            iRotate,
            0],
        'Center': [
            0,
            iHeight * 0.5,
            0],
        'GlobalArea': 0,
        'NextArea': 0,
        'Origin': vOrigin,
        'Perfab': 0,
        'SID': objSID,
        'Scale': [
            1,
            1,
            1],
        'Source': 0,
        'Shape': iModelType,
        'Size': lstArgs,
        'Other': {
            'Action': {
                action: vDest } } }
    iScene = oSkill.m_Base['Scene']
    oBuild = oGame.m_ResMgr.CreateBuild(iScene, objSID, dAddData)
    if oBuild:
        oBuild.DoAction(action, { })


def PerformCreateBuild(oSkill, iObjSID, iModelType, vPos, fAngle, iDelayDieTime, dInfo):
    oGame = oSkill.m_Game
    oAttack = oGame.GetObject(oSkill.m_Base['AID'], PY_FLAG_DEAD)
    if not oAttack:
        return None
    iScene = oSkill.m_Base['Scene']
    oObstacle = oGame.m_WarData.GetBuildData(iObjSID)
    if not oObstacle:
        SendAlert('err', '技能%d 在战场%d创建%d建筑失败' % (oSkill.m_Base['pfid'], oGame.m_WarMgr.m_SID, iObjSID))
        return None
    if iModelType == MODEL_TYPE_BOX:
        lstArgs = cl_modeldefine.GetModelDefine(oObstacle.m_Shape, 'Box')
        fCenterHeight = lstArgs[1] * 0.5
    elif iModelType == MODEL_TYPE_CAPSULE:
        tModelData = cl_modeldefine.GetModelDefine(oObstacle.m_Shape, 'Physx')
        lstArgs = (tModelData[1], tModelData[0], 0)
        fCenterHeight = tModelData[1] * 0.5
    else:
        SendAlert('err', '技能%d 当前未支持创建%d类型建筑，请联系程序支持' % (oSkill.m_Base['pfid'], iModelType))
        return None
    if 'OffsetCenterHeight' in dInfo:
        fCenterHeight += dInfo['OffsetCenterHeight']
    dAddData = {
        'Owner': oAttack.m_ID,
        'Angle': [
            0,
            fAngle,
            0],
        'Center': [
            0,
            fCenterHeight,
            0],
        'Origin': vPos,
        'SID': iObjSID,
        'Scale': [
            1,
            1,
            1],
        'Shape': iModelType,
        'Size': lstArgs }
    oBuild = oGame.m_ResMgr.CreateBuild(iScene, iObjSID, dAddData)
    iFrame = Time2Frame(iDelayDieTime)
    if 'FollowDie' in dInfo:
        oAttack.m_FollowDieObjs[oBuild.m_ID] = 1
    if iFrame:
        oBuild.Call_Out(Functor(DelayDieBuild, oBuild), iFrame, 'DelayDieBuild')


def DelayDieBuild(oBuild):
    oReason = cl_object.reason.CStrReason('Skill', None, {
        'DamType': DAM_TYPE_PERFORM | DAM_USE_HP })
    oBuild.HPModifyDam(oBuild.m_ID, [
        [
            oBuild.HP(),
            oReason]])


def PerformCreateInkBead(oSkill, lstPos, fCheckDis):
    if not lstPos:
        return None
    oAttack = oSkill.GetAttack()
    if not oAttack or oAttack.m_SID != INKMASTER_HERO:
        return None
    oInkCon = oAttack.m_InkCon
    oInkCon.CreateInkBead(oSkill, lstPos, fCheckDis)


def CrtTargeFloorPos(oSkill, iTarget):
    oGame = oSkill.m_Game
    oTarget = oGame.GetObject(iTarget)
    if oTarget:
        return oTarget.GetGroundPos()
    return (0, 0, 0)


def CalTargetPosInRectangle(oSkill, vCenter, vSize):
    fMaxX = vCenter[0] + vSize[0] * 0.5
    fMaxZ = vCenter[2] + vSize[2] * 0.5
    fMinX = vCenter[0] - vSize[0] * 0.5
    fMinZ = vCenter[2] - vSize[2] * 0.5
    iVictim = oSkill.m_Base['VID']
    oVictim = oSkill.m_Game.GetObject(iVictim, PY_FLAG_DEAD)
    if oVictim:
        vEnd = oVictim.GetPos()
    else:
        vEnd = oSkill.m_Base['vEnd']
    fCurX = vEnd[0]
    fCurZ = vEnd[2]
    fCurX = max(fMinX, fCurX)
    fCurX = min(fMaxX, fCurX)
    fCurZ = max(fMinZ, fCurZ)
    fCurZ = min(fMaxZ, fCurZ)
    return (fCurX, vEnd[1], fCurZ)


def GetGamePlayerCnt(oSkill):
    oGame = oSkill.m_Game
    oWarMgr = oGame.m_WarMgr
    return oWarMgr.GetAllPlayerCnt()


def GetRoomPlayerCnt(oSkill):
    oGame = oSkill.m_Game
    oWarMgr = oGame.m_WarMgr
    return len(oWarMgr.GetRoomPlayer())


def SinAngle(oSkill, fAngle):
    return cl_math.SinAngle(fAngle)


def CosAngle(oSkill, fAngle):
    return cl_math.CosAngle(fAngle)


def ToInt(oSkill, value):
    return int(value)


def IntToString(oSkill, value):
    return str(value)


def StringToInt(oSkill, value):
    return int(value)


def ObjectBranchBySkillElementType(oSkill, oFire, oCorrision, oThunder, oOther):
    pass


def CheckReloadFullBullet(oSkill):
    return False


def HitPartGetProb(oSkill, fCenterNum, fWeaknessNum):
    return False


def EllipseRandomPoints(oSkill, vStartPos, vMuzzlePos, iCount, fA, fB, fOffectXAngle, fOffectYAngle, iIndex):
    pass


def CheckHasPlayerInRange(oSkill, fRange, iPyFlag = PY_FLAG_NONE):
    oGame = oSkill.m_Game
    iAttack = oSkill.m_Base['AID']
    oAttack = oGame.GetObject(iAttack)
    if not oAttack:
        return False
    lstLive = GetLiveHeroID(oSkill, False)
    if not lstLive:
        return False
    vAttackPos = oAttack.GetPos()
    for iHero in lstLive:
        oHero = oGame.GetObject(iHero, iPyFlag)
        if not oHero:
            continue
        vPos = oHero.GetPos()
        fDistance = cl_math.CalDistance3D(vAttackPos, vPos)
        if fDistance < fRange:
            return True
    
    return False


def GetFarTargetInRange(oSkill):
    oGame = oSkill.m_Game
    iAttack = oSkill.m_Base['AID']
    oAttack = oGame.GetObject(iAttack)
    if not oAttack:
        return 0
    lstLive = GetLiveHeroID(oSkill, True)
    if not lstLive:
        return 0
    dDis = oGame.Scene_GetTargetDisMap(oAttack.m_ID, list(lstLive))
    if not dDis:
        return 0
    lstVLST = sorted(dDis, key = dDis.get, reverse = True)
    return lstVLST[0]


def CrtPlayerOffsetPosInRange(oSkill, fRange, tOffset, iPyFlag = PY_FLAG_NONE):
    oGame = oSkill.m_Game
    iAttack = oSkill.m_Base['AID']
    oAttack = oGame.GetObject(iAttack)
    if not oAttack:
        return oSkill.m_Base['vEnd']
    lstLive = GetLiveHeroID(oSkill, True)
    if not lstLive:
        return oSkill.m_Base['vEnd']
    lstChoosePos = []
    vAttackPos = oAttack.GetPos()
    for iHero in lstLive:
        oHero = oGame.GetObject(iHero, iPyFlag)
        if not oHero:
            continue
        vPos = oHero.GetPos()
        fDistance = cl_math.CalDistance3D(vAttackPos, vPos)
        if fDistance < fRange:
            lstChoosePos.append(vPos)
    
    (fX, _, fZ) = tOffset
    iX = int(fX * 100)
    iZ = int(fZ * 100)
    fX = oGame.Random(iX) / 100 - fX * 0.5
    fZ = oGame.Random(iZ) / 100 - fZ * 0.5
    if not lstChoosePos:
        vEndPos = (vAttackPos[0] + fX, vAttackPos[1], vAttackPos[2] + fZ)
    else:
        idx = oGame.Random(len(lstChoosePos))
        vEndPos = (lstChoosePos[idx][0] + fX, lstChoosePos[idx][1], lstChoosePos[idx][2] + fZ)
    vRet = oGame.Scene_RaycastSingle(oSkill.m_Base['Scene'], vEndPos, cl_math.Vec3Add(vEndPos, (0, -5, 0)), PXMASK_BLOCK)
    if vRet[0] != -1:
        vEndPos = (vRet[1][0], vRet[1][1] + 0.1, vRet[1][2])
    return vEndPos


def CheckSummonIsDestroy(oSkill, lstSummon):
    oGame = oSkill.m_Game
    iScene = oSkill.m_Base['Scene']
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return False
    for iSummon in lstSummon:
        oSummon = oGame.GetObject(iSummon, PY_FLAG_DEAD)
        if oSummon:
            return False
    
    return True


def AssignSummonDie(oSkill, lstSummon, iTime):
    oGame = oSkill.m_Game
    iFrame = Time2Frame(iTime)
    for iSummon in lstSummon:
        oSummon = oGame.GetObject(iSummon, PY_FLAG_DEAD)
        if not oSummon:
            continue
        if iFrame:
            oSummon.Call_Out(Functor(DelayAssignSummonDie, oSummon), iFrame, 'DelayAssignSummonDie')
            continue
        DelayAssignSummonDie(oSummon)
    


def DelayAssignSummonDie(oSummon):
    oReason = cl_object.reason.CStrReason('SkillHaltDie', None, {
        'DamType': DAM_TYPE_SCENE | DAM_USE_HP })
    oSummon.HPModifyDam(0, [
        [
            oSummon.HP(),
            oReason]])


def AssignBuildDie(oSkill, iBuildSID):
    iScene = oSkill.m_Base['Scene']
    oGame = oSkill.m_Game
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return None
    lstBuild = oScene.GetObjectsByTypes([
        'Build',
        'Obstacle',
        'Trap',
        'GateControl'])
    for bid in lstBuild:
        oBuild = oGame.GetObject(bid)
        if oBuild and oBuild.m_SID == iBuildSID:
            oReason = cl_object.reason.CStrReason('Skill', None, {
                'DamType': DAM_TYPE_PERFORM | DAM_USE_HP })
            oBuild.HPModifyDam(oBuild.m_ID, [
                [
                    oBuild.HP(),
                    oReason]])
    


def DestroyAssignSummon(oSkill, lstSummon, iTime):
    oGame = oSkill.m_Game
    iScene = oSkill.m_Base['Scene']
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return None
    iFrame = Time2Frame(iTime)
    for iSummon in lstSummon:
        oSummon = oGame.GetObject(iSummon, PY_FLAG_DEAD)
        if not oSummon:
            continue
        if iFrame:
            oSummon.Call_Out(Functor(DelayDestroyAssignSummon, oSummon), iFrame, 'DelayRemoveSummon')
            continue
        oSummon.Remove('Skill')
    


def DelayDestroyAssignSummon(oSummon):
    oSummon.Remove('Skill')


def BindSummonFollowTarget(oSkill, lstSummon, bBind):
    oGame = oSkill.m_Game
    iAttack = oSkill.m_Base['AID']
    oAttack = oGame.GetObject(iAttack)
    if not oAttack:
        return None
    if not oAttack.m_AttachCtrl:
        oAttack.m_AttachCtrl = cl_attachctrl.CAttachCtrlTmp(oAttack)
    for iSummon in lstSummon:
        oSummon = oGame.GetObject(iSummon, PY_FLAG_DEAD)
        if not oSummon:
            continue
        if bBind:
            oAttack.m_AttachCtrl.AddAttach(iSummon)
            continue
        oAttack.m_AttachCtrl.DelAttach(iSummon)
    


def GetPosByRelativePosition(oSkill, lstPos, iCnt):
    if iCnt < 0:
        return []
    oAttack = oSkill.GetAttack()
    tBossPos = oAttack.GetPos()
    (iUnitx, _, iUnitz) = oAttack.GetFacing()
    vOrthogonal = (-iUnitz, 0, iUnitx)
    for iIndex, tPos in enumerate(lstPos):
        (x, y, z) = tPos
        tXpos = (iUnitx * x, y, iUnitz * x)
        vtempPos = cl_math.Vec3Add(tBossPos, tXpos)
        tZpos = (vOrthogonal[0] * z, y, vOrthogonal[2] * z)
        tRealPos = cl_math.Vec3Add(vtempPos, tZpos)
        lstPos[iIndex] = tRealPos
    
    return lstPos[0:iCnt]


def RandomTraceUnLockHero(oSkill, iSummon, lstLive, bTarget):
    oGame = oSkill.m_Game
    oSummon = oGame.GetObject(iSummon)
    if not oSummon:
        return None
    oBoss = oSkill.GetAttack()
    if not hasattr(oBoss, 'm_Track'):
        oBoss.m_Track = { }
    if bTarget and oSkill.m_Base['VID'] in lstLive:
        lstLive.remove(oSkill.m_Base['VID'])
    lstUnlcok = []
    for iLive in lstLive:
        iFlag = 1
        if iLive not in oBoss.m_Track:
            lstUnlcok.append(iLive)
            continue
        for iSum in oBoss.m_Track[iLive]:
            oSum = oGame.GetObject(iSum)
            if oSum:
                iFlag = 0
                break
        
        if iFlag:
            lstUnlcok.append(iLive)
    
    if len(lstUnlcok) == 0:
        iIndex = oGame.Random(len(lstLive))
        iVID = lstLive[iIndex]
    else:
        iIndex = oGame.Random(len(lstUnlcok))
        iVID = lstUnlcok[iIndex]
    if iVID not in oBoss.m_Track:
        oBoss.m_Track[iVID] = [
            iSummon]
    else:
        oBoss.m_Track[iVID].append(iSummon)
    oSummon.StartMove(iVID)
    oSummon.m_MoveCtrl.SetPathMode('WindSummon', PATHMODE_COLLISIONLESS)


def GetMonsterWinkPos(oSkill, fRadius1, fRadius2, iAngle1, iAngle2):
    if iAngle1 <= 0 or iAngle1 >= 180 or iAngle2 <= 0 or iAngle2 >= 180:
        SendAlert('err', '技能%d GetMonsterWinkPos角度范围:0<Angle<180' % oSkill.m_Base['pfid'])
    if iAngle1 > iAngle2:
        SendAlert('err', '技能%d GetMonsterWinkPos角度起始值大于结束值' % oSkill.m_Base['pfid'])
    if fRadius1 > fRadius2:
        SendAlert('err', '技能%d GetMonsterWinkPos半径范围初始值大于结束值' % oSkill.m_Base['pfid'])
    oGame = oSkill.m_Game
    oAttack = oSkill.GetAttack()
    for _ in range(10):
        vPos = oGame.Scene_RandomPointSectorInMesh(oAttack.m_Scene, oAttack.GetPos(), oAttack.GetFacing(), fRadius1, fRadius2, iAngle1, iAngle2)
        if vPos:
            break
    
    if not vPos:
        iAngle = oGame.Random(iAngle2 - iAngle1)
        fDis = oGame.Random(int(100 * (fRadius2 - fRadius1))) / 100 + fRadius1
        vDir = cl_math.RotateAroundVector(oAttack.GetFacing(), (0, 1, 0), iAngle1 + 180 + iAngle)
        if cl_math.CalDistance3D((0, 0, 0), vDir) == 0:
            vEnd = oAttack.GetPos()
        else:
            vEnd = cl_math.Vec3DisplaceDir(oAttack.GetPos(), vDir, fDis)
        fGroundDis = oGame.Scene_GroundDistance(oAttack.m_Scene, vEnd, 2, PXMASK_MOVEBLK | PXMASK_OBJECT, oAttack.m_ID)
        vPos = oGame.Scene_NavMeshRayCast(oAttack.m_Scene, oAttack.GetPos(), (vEnd[0], vEnd[1] - fGroundDis, vEnd[2]))
    return vPos


def RemovePointsWithinDistance(oSkill, lstPos, fDistance, iCnt):
    iLen = min(len(lstPos), iCnt)
    oAttack = oSkill.GetAttack()
    vAttackPos = oAttack.GetPos()
    lstSummonPos = []
    for vPos in lstPos:
        if cl_math.CalDistance3D(vPos, vAttackPos) > fDistance:
            lstSummonPos.append(vPos)
    
    return lstSummonPos[:iLen]


def StartAndEndAtSameHeight(oSkill, vStart, vEnd):
    vPos = (vEnd[0], vStart[1], vEnd[2])
    return vPos


def RayCastCartoonEnd(oSkill, sid):
    dCartoon = oSkill.GetCartoonBySID(sid)
    dCartoon['Pierce'] = 0


def SetCurCartoonCurPos(oSkill, sid, vPos):
    dCartoon = oSkill.GetCartoonBySID(sid)
    dCartoon['CurPos'] = vPos


def GetMonsterPhase(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return 0
    return oAttack.m_Phase


def GetSummonCnt(oSkill, iSID):
    oAttack = oSkill.GetAttack()
    oGame = oSkill.m_Game
    iScene = oAttack.m_Scene
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    lstSummon = oScene.GetObjectsByType('Summon')
    iCnt = 0
    for iSummon in lstSummon:
        oSummon = oGame.GetObject(iSummon)
        if oSummon and oSummon.m_DataSID == iSID:
            iCnt += 1
    
    return iCnt


def SetSkillServerCache(oSkill, key, var):
    oSkill.m_Collect[key] = var


def GetSkillServerCache(oSkill, key):
    if key not in oSkill.m_Collect:
        SkillLog.Error('skill%d err, no %s servercache' % (oSkill.m_Base['pfid'], key))
        return None
    return oSkill.m_Collect[key]


def CheckHasSkillCollect(oSkill, key):
    return key in oSkill.m_Collect


def ClearSkillServerCache(oSkill, key):
    oSkill.m_Collect.pop(key, None)


def RemovePointsBeyondDistance(oSkill, lstPos, fDistance, vCenter):
    lstSummonPos = []
    for vPos in lstPos:
        if cl_math.CalDistance3D(vPos, vCenter) < fDistance:
            lstSummonPos.append(vPos)
    
    return lstSummonPos


def RandomVector3(oSkill):
    oAttack = oSkill.GetAttack()
    vPos = oAttack.GetPos()
    return vPos


def CrtArgDestPosDirPoint(oSkill, vPos, vDir, fDis, iNum, iAngle, bOrder):
    lstPoint = []
    oGame = oSkill.m_Game
    if not oGame:
        return []
    for num in range(iNum):
        iNewAngle = int(iAngle * num)
        vEnd = cl_math.Vec3DestPosDirPlane(vPos, vDir, fDis, iNewAngle)
        lstPoint.append(vEnd)
    
    if not bOrder:
        lstPoint = ShufferList(oGame, lstPoint)
    return lstPoint


def GetSummonByDistance(oSkill, fRaduis, iSID):
    oAttack = oSkill.GetAttack()
    oGame = oSkill.m_Game
    iScene = oAttack.m_Scene
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    lstSummon = oScene.GetObjectsByType('Summon')
    lstSummonPos = []
    for iSummon in lstSummon:
        oSummon = oGame.GetObject(iSummon)
        if oSummon and oSummon.m_DataSID == iSID and cl_math.CalDistance3D(oAttack.GetPos(), oSummon.GetPos()) < fRaduis:
            lstSummonPos.append(iSummon)
    
    return lstSummonPos


def CountDistance(oSkill, vStart, vEnd):
    return cl_math.CalDistance(vStart, vEnd)


def CountDistance3D(oSkill, vStart, vEnd):
    return cl_math.CalDistance3D(vStart, vEnd)


def CheckVectorIsZero(oSkill, vPos):
    return cl_math.IsZero(vPos)


def GetPosByDistanceAndSummon(oSkill, fRaduis, lstSummon, lstPos):
    oGame = oSkill.m_Game
    lstSummonPos = []
    for iSummon in lstSummon:
        oSummon = oGame.GetObject(iSummon)
        if not oSummon:
            continue
        lstSummonPos.append(oSummon.GetPos())
    
    lstRes = []
    for vPos in lstPos:
        iFlag = 1
        for vSummonPos in lstSummonPos:
            if cl_math.CalDistance3D(vPos, vSummonPos) < fRaduis:
                iFlag = 0
                break
        
        if iFlag:
            lstRes.append(vPos)
    
    return lstRes


def SkillShowLockHitLstCount(oSkill):
    count = 0
    return count


def CrtArgMuzzleObject(oSkill, Name):
    pass


def GetNavMeshHero(oSkill, vCenter, bAlive):
    oGame = oSkill.m_Game
    oAttack = oSkill.GetAttack()
    lstLive = GetLiveHeroID(oSkill, bAlive)
    lstHero = []
    for iHero in lstLive:
        oHero = oGame.GetObject(iHero, PY_FLAG_EXCLUDEMONSTERHATE)
        if not oHero:
            continue
        (fTargetRadius, _) = cl_modeldefine.GetModelDefine(oHero.m_Shape, 'NavMesh')
        vHero = oHero.GetPos()
        vRet = oGame.Scene_NavMeshRayCast(oAttack.m_Scene, vCenter, (vHero[0], vCenter[1], vHero[2]))
        if cl_math.CalDistance(vRet, vHero) <= 2 * fTargetRadius:
            lstHero.append(iHero)
    
    return lstHero


def GetRandomNavMeshPlayer(oSkill, vCenter, bAlive):
    oGame = oSkill.m_Game
    oAttack = oSkill.GetAttack()
    lstLive = GetLiveHeroID(oSkill, bAlive)
    lstPlayer = []
    for iHero in lstLive:
        oHero = oGame.GetObject(iHero, PY_FLAG_EXCLUDEMONSTERHATE)
        if not oHero:
            continue
        vHero = oHero.GetPos()
        (fTargetRadius, _) = cl_modeldefine.GetModelDefine(oHero.m_Shape, 'NavMesh')
        vRet = oGame.Scene_NavMeshRayCast(oAttack.m_Scene, vCenter, (vHero[0], vCenter[1], vHero[2]))
        if cl_math.CalDistance(vRet, vHero) <= 2 * fTargetRadius:
            lstPlayer.append(iHero)
    
    if not lstPlayer:
        return 0
    iIndex = oSkill.m_Game.Random(len(lstPlayer))
    return lstPlayer[iIndex]


def SkillForbid(oSkill, iEnable, iRule):
    
    def ClearForbid(oSkill):
        oAttack = oSkill.GetAttack()
        if iWeapon:
            oForbidObj = oAttack.m_WieldCon.GetItemByID(iWeapon)
        else:
            oForbidObj = oAttack
        if not oForbidObj:
            return None
        oForbidObj.UnForbid(iRule, sKey)

    if not iRule:
        iPerform = oSkill.m_Base['pfid']
        iRule = cl_perform.GetPerformClassAttr(iPerform, 'm_ForbidRule')
    oAttack = oSkill.GetAttack()
    sKey = oSkill.m_Base['PFKey']
    iWeapon = oSkill.m_Base['Weapon']
    if not oAttack:
        return None
    if iWeapon:
        oForbidObj = oAttack.m_WieldCon.GetItemByID(iWeapon)
    else:
        oForbidObj = oAttack
    if not oForbidObj:
        return None
    if iEnable:
        oForbidObj.Forbid(iRule, sKey)
        oSkill.AddEndFunc(ClearForbid)
    else:
        oForbidObj.UnForbid(iRule, sKey)


def GetNowLayer(oSkill):
    oLevelCtrl = oSkill.m_Game.m_WarMgr.GetComponent('LevelCtrl')
    return oLevelCtrl.m_LayerNum


def ModifySkillHitArea(oSkill, iHitArea):
    oSkill.m_Update['CurHitArea'] = iHitArea


def ModifySkillHitPos(oSkill, vHitPos):
    oSkill.m_Update['CurHitPos'] = vHitPos


def SetCurVictim(oSkill, iTarget):
    oSkill.m_Update['CurVID'] = iTarget


def SetHitFlaw(oSkill, iFlaw, iBreakFlaw = 0):
    oSkill.m_Update['Flaw'] = [
        iFlaw]
    oSkill.m_Update['BreakFlaw'] = iBreakFlaw


def SetHitVictimAllFlaw(oSkill, iBreakFlaw):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    iVictim = oSkill.m_Update['CurVID']
    dFlaw = oAttack.m_FlawCon.GetFlaw(iVictim)
    if not dFlaw:
        return None
    oSkill.m_Update['Flaw'] = list(dFlaw)
    oSkill.m_Update['BreakFlaw'] = iBreakFlaw


def CheckHitPointArea(oSkill, iPointArea):
    iCurHitArea = oSkill.m_Update['CurHitArea'] if 'CurHitArea' in oSkill.m_Update else 0
    if iCurHitArea == iPointArea:
        return True
    return False


def GetAttackSummon(oSkill, iFightType):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oGame = oSkill.m_Game
    lstSummon = []
    for iSummonID in oAttack.m_SummonDict:
        oSummon = oGame.GetObject(iSummonID, PY_FLAG_DEAD)
        if not oSummon:
            continue
        if oSummon.m_FightType & iFightType == iFightType:
            lstSummon.append(iSummonID)
    
    return lstSummon


def CurVictimDeath(oSkill):
    iVictim = oSkill.m_Update['CurVID']
    oVictim = oSkill.m_Game.GetObject(iVictim, PY_FLAG_DEAD)
    if not oVictim:
        return None
    if not oVictim.QueryBitAttr('LogicKey') & FIGHT3_KEY_IGNELBEEXECUTED:
        oVictim.AddExecuteType(EXECUTETYPE_ACTIVEPF)


def CostAttackerEnergy(oSkill, iPredictFrame, fCost, fGain):
    iTarget = oSkill.m_Base['AID']
    oGame = oSkill.m_Game
    oHero = oGame.GetObject(iTarget, PY_FLAG_DEAD)
    if not oHero:
        return 0
    iCurEnergy = oHero.Energy()
    iMaxEnergy = oHero.QueryAttr('EnergyMax')
    iCost = int(iMaxEnergy * fCost) // 100
    iPredictCost = iPredictFrame * iCost
    iActualCost = 0
    if iPredictCost <= iCurEnergy:
        oHero.EnergyModify(-iPredictCost, oSkill = oSkill)
        iActualCost = iPredictCost
    else:
        oHero.EnergyModify(-iCurEnergy, oSkill = oSkill)
        iActualCost = iCurEnergy
    return int((iActualCost / iMaxEnergy) * 10000 * fGain)


def StopAttackEnergyRecover(oSkill, sFlag, iRestartTime):
    iTarget = oSkill.m_Base['AID']
    oGame = oSkill.m_Game
    oAttack = oGame.GetObject(iTarget)
    if not oAttack:
        return None
    sNewFlag = '%s-%s' % (oSkill.m_Base['PFKey'], sFlag)
    if iRestartTime <= 0:
        oAttack.StopEnergyRecover(sNewFlag)
        return None
    iRestartFrame = Time2Frame(iRestartTime)
    oAttack.StopEnergyRecover(sNewFlag, iRestartFrame)


def StartAttackEnergyRecover(oSkill, sFlag):
    iTarget = oSkill.m_Base['AID']
    oGame = oSkill.m_Game
    oAttack = oGame.GetObject(iTarget)
    if not oAttack:
        return None
    sNewFlag = '%s-%s' % (oSkill.m_Base['PFKey'], sFlag)
    oAttack.StartEnergyRecover(sNewFlag)


def GetAttackEnergy(oSkill):
    iTarget = oSkill.m_Base['AID']
    oGame = oSkill.m_Game
    oAttack = oGame.GetObject(iTarget)
    if not oAttack:
        return 0
    return oAttack.Energy()


def CalWaitTimeByRange(iCurVal, iMinVal, iMaxVal, iMinTime, iMaxtime):
    iTime = 0
    if iCurVal <= iMinVal:
        iTime = iMaxtime
    elif iCurVal >= iMaxVal:
        iTime = iMinTime
    else:
        iY = iMaxtime - iMinTime
        iX = iMaxVal - iMinVal
        iTime = iMaxtime - int((iY / iX) * (iCurVal - iMinVal))
    return iTime


def GetContinueCount(oSkill):
    iCount = 0
    return iCount


def RandomFloat(iMin, iMax):
    iRes = 0
    return iRes


def SetCurLockTargetID(oSkill, iIndex):
    iTarget = 0
    return iTarget


def GetSummonOwnerAttr(oSkill, sAttr):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return 0
    iTarget = oAttack.m_Owner
    oTarget = oAttack.m_Game.GetObject(iTarget)
    if oTarget:
        return cl_newformula.GetWarriorAttr(sAttr, oTarget)
    return 0


def GetSummonOwnerTalentLevel(oSkill, iTalent):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return 0
    iTarget = oAttack.m_Owner
    oTarget = oAttack.m_Game.GetObject(iTarget)
    if not oTarget:
        return 0
    oTalent = oTarget.m_TalentCon.GetPerform(iTalent)
    if oTalent:
        return oTalent.m_Level
    return 0


def GetThunderPos(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return []
    lstThunderCernterPos = oAttack.Query('ThunderCernterPos', [])
    return lstThunderCernterPos


def GetCustomPos(oSkill):
    return GetPosInCustomData(oSkill)


def GetPosInCustomData(oSkill):
    if 'vStart' in oSkill.m_Custom:
        return oSkill.m_Custom['vStart']
    oAttack = oSkill.GetAttack()
    return oAttack.GetPos()


def CalWaitTimeByTotaltime(iCurVal, iMinVal, iMinTotal, iMaxTotal, iAddTime):
    iTotalTime = iMinTotal
    iNum = iCurVal - iMinVal
    if iNum > 0:
        iTotalTime += iNum * iAddTime
    if iTotalTime > iMaxTotal:
        iTotalTime = iMaxTotal
    iTime = round(iTotalTime / iCurVal)
    return iTime


def SwitchHeroPerform(oSkill, iOldPerformSID, iNewPerformSID, iType):
    oAttack = oSkill.GetAttack()
    oPerformCon = oAttack.m_Perform
    oCurPerform = oPerformCon.GetPerform(iOldPerformSID)
    oCurPerform.Disable(oAttack)
    oNewPerform = oPerformCon.GetPerform(iNewPerformSID)
    oNewPerform.Enable(oAttack)


def SwitchServantOwnerPerform(oSkill, iPerform):
    oServant = oSkill.GetAttack()
    if not oServant.m_FightType & WARRIOR_SERVANT:
        return None
    oHero = oServant.GetOwner()
    if not oHero:
        return None
    oHero.SwitchPerform('Career', iPerform)


def IsHeroCtrl(oSkill):
    return 1


def CheckSummonBelongToCtrl(oSkill):
    return 1


def CheckHasBenediction(oSkill, iBenediction):
    oAttack = oSkill.GetAttack()
    oBenediction = oAttack.m_BenedictionCon.GetPerform(iBenediction)
    if oBenediction and oBenediction.m_Enable:
        return True
    return False


def CheckPointSkillIsEnable(oSkill, iPerform):
    oAttack = oSkill.GetAttack()
    oPerformCon = oAttack.m_Perform
    if oPerformCon.IsEnabled(iPerform):
        return True
    return False


def CheckVictimInStruckCD(oSkill):
    if 'CurVID' in oSkill.m_Update:
        iTarget = oSkill.m_Update['CurVID']
    else:
        iTarget = oSkill.m_Base['VID']
    oGame = oSkill.m_Game
    oAttack = oGame.GetObject(iTarget, PY_FLAG_DEAD)
    if not oAttack:
        return False
    iCurFrame = oGame.GetFrameNum()
    if iCurFrame < oAttack.Query('StruckCDFrame'):
        return True
    return False


def GetCameraDirPos(oSkill, fDistance):
    oAttack = oSkill.GetAttack()
    vPos = oAttack.GetPos()
    vStart = (vPos[0], vPos[1] + oSkill.m_Base['ModelHeight'] * 0.85, vPos[2])
    vEnd = cl_math.Vec3DisplaceDir(vStart, oAttack.GetFacing(), fDistance)
    return vEnd


def CalCameraDir(oSkill, bHorizontal = True):
    if 'vDir' in oSkill.m_Custom:
        vDir = oSkill.m_Custom['vDir']
    else:
        vDir = CrtArgSelfFace(oSkill)
    return vDir


def GetAttackerNearSpace(oSkill, vOffset):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return []
    iScene = oAttack.m_Scene
    oGame = oAttack.m_Game
    (_, vPos) = oGame.Scene_GetSpace(iScene, cl_math.Vec3Add(oAttack.GetPos(), vOffset))
    return vPos


def MoveToPos(oSkill, vPos):
    oAttack = oSkill.GetAttack()
    if oAttack and oAttack.m_MoveCtrl:
        oAttack.m_MoveCtrl.SeekPath(oAttack, vPos)


def StopMove(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oAgent = oAttack.m_Agent
    if not oAgent:
        return None
    oAgent.Stop()


def BuildRandomList(oSkill, dInfo):
    lstSID = []
    for iSID, iNum in dInfo.items():
        for _ in range(iNum):
            lstSID.append(iSID)
        
    
    return ShufferList(oSkill.m_Game, lstSID)


def PopSkillListCache(oSkill, sKey):
    if sKey not in oSkill.m_Collect:
        SkillLog.Error('skill%d err, no %s servercache' % (oSkill.m_Base['pfid'], sKey))
        return 0
    lstNum = oSkill.m_Collect[sKey]
    iResult = lstNum.pop() if lstNum else None
    return iResult


def GetSkillCacheList(oSkill, sKey):
    if sKey not in oSkill.m_Collect:
        SkillLog.Error('skill%d err, no %s servercache' % (oSkill.m_Base['pfid'], sKey))
        return None
    return oSkill.m_Collect[sKey]


def RandomPointSectorInMesh(oSkill, fRadius1, fRadius2, iAngle1, iAngle2):
    if iAngle1 <= 0 or iAngle1 >= 180 or iAngle2 <= 0 or iAngle2 >= 180:
        SendAlert('err', '技能%d RandomPointSectorInMesh角度范围:0<Angle<180' % oSkill.m_Base['pfid'])
    if iAngle1 > iAngle2:
        SendAlert('err', '技能%d RandomPointSectorInMesh角度起始值大于结束值' % oSkill.m_Base['pfid'])
    if fRadius1 > fRadius2:
        SendAlert('err', '技能%d RandomPointSectorInMesh半径范围初始值大于结束值' % oSkill.m_Base['pfid'])
    oAttack = oSkill.GetAttack()
    oGame = oSkill.m_Game
    vPos = oAttack.GetGroundPos()
    for _ in range(10):
        vTarget = oGame.Scene_RandomPointSectorInMesh(oAttack.m_Scene, vPos, oAttack.GetFacing(), fRadius1, fRadius2, iAngle1, iAngle2)
        if vTarget:
            break
    else:
        iLevel = 0
        sName = ''
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        if oAttack.m_LineIdx:
            oLine = oLevelCtrl.GetLineNode(oAttack.m_LineIdx)
            iLevel = oLine.m_LevelNode.m_Level
            sName = oLine.m_Name
        SkillLog.Info('技能%d RandomPointSectorInMesh 关卡:%s 路线 %s 的 %s 附近取不到点。' % (oSkill.m_Base['pfid'], iLevel, sName, vPos))
        return vPos
    return vTarget


def RandomPointSectorInMeshList(oSkill, vStart, vDir, fRadius1, fRadius2, iAngle1, iAngle2, iMaxNum):
    oGame = oSkill.m_Game
    iScene = oSkill.m_Base['Scene']
    lstPos = []
    iTryTimes = 10
    iSuccess = 0
    for _ in range(iMaxNum * iTryTimes):
        vTarget = oGame.Scene_RandomPointSectorInMesh(iScene, vStart, vDir, fRadius1, fRadius2, iAngle1, iAngle2)
        if not vTarget:
            continue
        lstPos.append(vTarget)
        iSuccess += 1
        if iSuccess >= iMaxNum:
            break
    
    return lstPos


def GetPointInCircle(oSkill, vCenter, fRadius):
    return cl_math.GetPointInCircle(oSkill.m_Game, vCenter, fRadius)


def ChooseAreaSummonPos(oSkill):
    oAttack = oSkill.GetAttack()
    oAgent = oAttack.m_Agent
    if not oAgent or not (oAttack.m_LineIdx):
        return oAttack.GetPos()
    oGame = oAttack.m_Game
    lstRangedGroup = oAgent.GetConfig('RangedAreaGroup')
    lstSummonGroup = oAgent.GetConfig('SummonAreaGroup')
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    if len(lstRangedGroup) > 1 or len(lstSummonGroup) > 1:
        SendAlert('err', '%d 抽取区域移动对应的召唤点,当前仅支持单组。' % oAttack.m_SID)
        return oAttack.GetPos()
    oLine = oLevelCtrl.GetLineNode(oAttack.m_LineIdx)
    iLevel = oLine.m_LevelNode.m_Level
    dSummonPos = oLevelCtrl.m_LevelConfData.GetLineConfig(iLevel, oLine.m_Name, 'summonarea')
    lstPos = []
    iCurArea = oAgent.GetData('ChosenArea', -1)
    vAttackPos = oAttack.GetPos()
    if iCurArea == -1:
        dAllArea = oLevelCtrl.m_LevelConfData.GetLineConfig(iLevel, oLine.m_Name, 'monsterarea')
        for idx, dArea in enumerate(dAllArea.values()):
            if dArea['group'] in lstRangedGroup and cl_math.CheckDistance3D(dArea['center'], vAttackPos, 1):
                iCurArea = idx
                break
        else:
            return oAttack.GetPos()
    if lstSummonGroup:
        for idx, dArea in enumerate(dSummonPos.values()):
            if dArea['group'] in lstSummonGroup or 'num' in dArea or dArea['num'] == iCurArea:
                lstPos.append(dArea['center'])
                continue
            if iCurArea == idx:
                lstPos.append(dArea['center'])
        
    if not lstPos:
        SendAlert('err', '组号%s,编号%d的区域移动点,无对应召唤点' % (lstRangedGroup, iCurArea))
    iPos = oGame.Random(len(lstPos))
    return lstPos[iPos]


def GetPosByPointDistance(oSkill, fDistance):
    oAttack = oSkill.GetAttack()
    vEnd = cl_math.Vec3DisplaceDir(oAttack.GetPos(), oAttack.GetFacing(), fDistance)
    return vEnd


def RandomNumberList(oSkill, iMax, iSize):
    return GetRandomCard(oSkill.m_Game, iSize, iMax)


def CheckNumberinList(oSkill, iNumber, lstNumber):
    if iNumber in lstNumber:
        return True
    return False


def GetMonsterNumberByScene(oSkill, iSID):
    oGame = oSkill.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oSkill.m_Base['Scene'])
    lstMonster = oScene.GetObjectsByType('Monster')
    iRes = 0
    for iMonster in lstMonster:
        oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
        if oMonster and oMonster.m_DataSID == iSID:
            iRes += 1
    
    return iRes


def GetNextSkillSID(oSkill):
    oAttack = oSkill.GetAttack()
    oAgent = oAttack.m_Agent
    if not oAgent:
        return 0
    dPFGroup = oAgent.GetData('CurPFGroup')
    iUsedCnt = oAgent.GetData('PFUsed', 0)
    iTotalCnt = len(dPFGroup)
    if iUsedCnt == 0 and iUsedCnt + 1 >= iTotalCnt:
        return 0
    return dPFGroup[iUsedCnt + 1][0]


def GetDistanceByAttackerAndTarget(oSkill):
    oAttack = oSkill.GetAttack()
    iTarget = oSkill.m_Update['CurVID']
    oTarget = oAttack.m_Game.GetObject(iTarget)
    if not oTarget:
        return 0
    return cl_math.CalDistance3D(oAttack.GetPos(), oTarget.GetPos())


def DemonKingRoamingSiteSelection(oSkill, iPerform, dInfo):
    oAttack = oSkill.GetAttack()
    oGame = oSkill.m_Game
    if iPerform == 0:
        if oGame.m_WarMgr.Query('TestMonster', 0) != oAttack.m_ID:
            SendAlert('err', '%d 妖王漫游选点没有获取到下一个技能' % oSkill.m_Base['pfid'])
        return oAttack.GetPos()
    clsPerform = cl_perform.GetPerformModule(iPerform)
    oTarget = oAttack.m_Game.GetObject(oSkill.m_Base['VID'])
    if not oTarget:
        return oAttack.GetPos()
    if clsPerform.m_SkillShotType in (CLOSE_DISTANCE, MIDDLE_DISTANCE):
        iAngle = dInfo['angle1']
        fDis = dInfo['distance1']
        if clsPerform.m_SkillShotType == MIDDLE_DISTANCE:
            iAngle = dInfo['angle2']
            fDis = dInfo['distance2']
        return oAttack.m_MoveCtrl.E_GetFleeDestPos(oTarget.GetPos(), 1, fDis, -iAngle, iAngle, 10, 10)
    if clsPerform.m_SkillShotType == FAR_DISTANCE:
        iRandius = oGame.Random(dInfo['randius2'] - dInfo['randius1']) + dInfo['randius1']
        iAngle1 = dInfo['winkangle1']
        iAngle2 = dInfo['winkangle2']
        if oGame.Random(2):
            iAngle1 = -iAngle2
            iAngle2 = -iAngle1
        return oAttack.m_MoveCtrl.E_GetFleeDestPos(oTarget.GetPos(), 0, iRandius, iAngle1, iAngle2, 10, 10)


def CreateWarriorList(oSkill, dWeight, dStrength, iExpectStrength):
    oGame = oSkill.m_Game
    iStrength = 0
    lstSID = []
    for idx in range(100):
        iSID = ChooseKey(oGame, dWeight)
        lstSID.append(iSID)
        iStrength += dStrength[iSID]
        if iStrength >= iExpectStrength:
            break
    
    return lstSID


def DemonKingCondensedSiteSelection(oSkill, iProtegeSID, lstPos):
    oAttack = oSkill.GetAttack()
    oAgent = oAttack.m_Agent
    if not oAgent:
        return oAttack.GetPos()
    oGame = oSkill.m_Game
    iCondensedProtege = oAgent.GetData('CondensedProtege', 0)
    oScene = oGame.m_SceneMgr.GetScene(oSkill.m_Base['Scene'])
    lstProtege = oScene.GetObjectsByType('Protege')
    if iCondensedProtege and iCondensedProtege in lstProtege:
        lstProtege.remove(iCondensedProtege)
    lstRes = []
    for iProtege in lstProtege:
        oProtege = oGame.GetObject(iProtege, PY_FLAG_DEAD)
        if oProtege and oProtege.m_SID == iProtegeSID:
            lstRes.append(iProtege)
    
    if not lstRes:
        oCondensedState = oAttack.m_State.GetItemBySID(7994)
        if oCondensedState:
            oAttack.m_State.RemoveItem(oCondensedState.m_ID)
        SendAlert('err', '%s 妖王凝气选点异常 %s %s' % (oGame.m_ID, oSkill.m_Base['RS'], lstProtege))
        return oAttack.GetPos()
    iIndex = oSkill.m_Game.Random(len(lstRes))
    iTarget = lstRes[iIndex]
    oAgent.SetData('CondensedProtege', iTarget)
    oProtege = oGame.GetObject(iTarget)
    fMinDis = 268435455
    vRes = oAttack.GetPos()
    for vPos in lstPos:
        fDis = cl_math.CalDistance(oProtege.GetPos(), vPos)
        if fDis < fMinDis:
            fMinDis = fDis
            vRes = vPos
    
    return vRes


def GetPosByAttackerAndPointDistance(oSkill, fDistance):
    oAttack = oSkill.GetAttack()
    oTarget = oAttack.m_Game.GetObject(oSkill.m_Base['VID'])
    if not oTarget:
        return oAttack.GetPos()
    vDir = cl_math.Vec3Minus(oAttack.GetPos(), oTarget.GetPos())
    return cl_math.Vec3DisplaceDir(oTarget.GetPos(), vDir, fDistance)


def GetAttackSID(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return 0
    return oAttack.m_SID


def GetlstPosSortByDistanceFromTargetPos(oSkill, lstPos, vTargetPos, bDesc):
    if bDesc:
        lstPos.sort(key = functools.cmp_to_key((lambda v1, v2: cl_math.CalDistance(vTargetPos, v2) - cl_math.CalDistance(vTargetPos, v1))))
    else:
        lstPos.sort(key = functools.cmp_to_key((lambda v1, v2: cl_math.CalDistance(vTargetPos, v1) - cl_math.CalDistance(vTargetPos, v2))))
    return lstPos


def GetMonsterSummonPosList(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack or oAttack.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
        return []
    lstPos = []
    for iSummon in oAttack.m_MonsterSummon:
        oSummon = oSkill.m_Game.GetObject(iSummon)
        if not oSummon:
            continue
        lstPos.append(oSummon.GetPos())
    
    return lstPos


def ClearMonsterSummon(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack or oAttack.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
        return None
    for iSummon in oAttack.m_MonsterSummon:
        if iSummon in oAttack.m_FollowDieObjs:
            oAttack.m_FollowDieObjs.pop(iSummon)
        oSummon = oSkill.m_Game.GetObject(iSummon)
        if not oSummon:
            continue
        oSummon.DieClearEffect()
        oSummon.Remove('Skill')
    
    oAttack.m_MonsterSummon = { }


def SetAsAttackerSameAttrRatio(oSkill, lstMonster, iType):
    
    def GetFuncAttr(oWarrior, sAttr):
        if sAttr == 'HP':
            iAttr = oWarrior.HP()
        elif sAttr == 'Armor':
            iAttr = oWarrior.Armor()
        elif sAttr == 'Shield':
            iAttr = oWarrior.Shield()
        else:
            iAttr = 0
        return iAttr

    dType = {
        DAM_USE_SHIELD: 'Shield',
        DAM_USE_ARMOR: 'Armor',
        DAM_USE_HP: 'HP' }
    dAttr2Ratio = { }
    if iType == DAM_USE_ALL:
        for sAttr in dType.values():
            dAttr2Ratio[sAttr] = 0
        
    else:
        sAttr = dType.get(iType, '')
        if not sAttr:
            SendAlert('err', '技能%d SetAsAttackerSameAttrRatio没有该属性%s' % (oSkill.m_Base['pfid'], iType))
            return None
        dAttr2Ratio[sAttr] = 0
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    for sAttr in dAttr2Ratio:
        iMax = oAttack.QueryAttr('%sMax' % sAttr)
        iAttr = GetFuncAttr(oAttack, sAttr)
        fRatio = iAttr / iMax if iMax > 0 else 0
        dAttr2Ratio[sAttr] = fRatio
    
    for iSummon in lstMonster:
        oSummon = oSkill.m_Game.GetObject(iSummon)
        if not oSummon:
            continue
        for sAttr, fRatio in dAttr2Ratio.items():
            iAttr = GetFuncAttr(oSummon, sAttr)
            oReason = cl_object.reason.CStrReason('设置等比例%s' % sAttr)
            oSummon.HPDirectModify(sAttr, oSummon.m_ID, -int(iAttr * (1 - fRatio)), oReason)
        
    


def ChooseMonsterMirrorPos(oSkill, dWeight, dRange, iNum):
    lstPos = []
    iTryTimes = 10
    oGame = oSkill.m_Game
    iResult = ChooseKey(oSkill.m_Game, dWeight)
    lstRange = dRange[iResult]
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    vAttackPos = oAttack.GetPos()
    vAttackDir = oAttack.GetFacing()
    if iResult == 1:
        fRange = lstRange[0]
        for _ in range(iNum):
            for _ in range(iTryTimes):
                vPos = oGame.Scene_RandomPointSectorInMesh(oAttack.m_Scene, vAttackPos, vAttackDir, 1, fRange, 1, 179)
                if not vPos:
                    continue
                lstPos.append(vPos)
            
        
    elif iResult == 2:
        fRange1Min = lstRange[0]
        fRange1Max = lstRange[1]
        fRange2 = lstRange[2]
        for _ in range(iTryTimes):
            vPos = oGame.Scene_RandomPointSectorInMesh(oAttack.m_Scene, vAttackPos, vAttackDir, fRange1Min, fRange1Max, 1, 179)
            if not vPos:
                continue
            lstPos.append(vPos)
        
        if not lstPos:
            lstPos.append(vAttackPos)
        for _ in range(iTryTimes):
            vPos1 = oGame.Scene_RandomPointSectorInMesh(oAttack.m_Scene, lstPos[0], vAttackDir, fRange2, fRange2 + 0.5, 1, 179)
            if not vPos1:
                continue
            lstPos.append(vPos1)
        
        if iNum > 2:
            for _ in range(iNum - 2):
                vNewDir = cl_math.Vec3Minus(lstPos[-1], lstPos[0])
                for _ in range(iTryTimes):
                    vPos2 = oGame.Scene_RandomPointSectorInMesh(oAttack.m_Scene, lstPos[0], vNewDir, fRange2, fRange2 + 0.5, 60, 179)
                    if not vPos2:
                        continue
                    lstPos.append(vPos2)
                
            
    if len(lstPos) < iNum:
        for _ in range(iTryTimes):
            vPos3 = oGame.Scene_RandomPointSectorInMesh(oAttack.m_Scene, vAttackPos, vAttackDir, 15, 30, 1, 179)
            if not vPos3:
                continue
            SkillLog.Debug('%s failmirrorpos add %s' % (oSkill.m_Base['pfid'], vPos3))
            lstPos.append(vPos3)
            if len(lstPos) >= iNum:
                break
        
    if len(lstPos) < iNum:
        SkillLog.Debug('%s failchoose %s %s' % (oSkill.m_Base['pfid'], vAttackPos, lstPos))
        iLength = len(lstPos)
        for _ in range(iNum - iLength):
            lstPos.append(vAttackPos)
        
    return ShufferList(oSkill.m_Game, lstPos)


def SystemObj2UnityObj(oSkill, object):
    pass


def CheckIsAllBulletRecycled(oSkill):
    return False


def MonsterRecallRider(oSkill):
    
    def ResetBaseAttr(oTarget, sAttr):
        if iRound not in clsData.m_BaseAttrInfo:
            return None
        if sAttr not in clsData.m_BaseAttrInfo[iRound]:
            return None
        iVal = clsData.m_BaseAttrInfo[iRound][sAttr]
        iVal = cl_formula.GetFormulaResultByLV(oTarget, iVal, iGrade)
        oTarget.SetAttr(sAttr, iVal, BASEATTR_REFRESH)

    oGame = oSkill.m_Game
    iTarget = oSkill.m_Base['AID']
    oAttack = oGame.GetObject(iTarget, PY_FLAG_DEAD)
    if not oAttack:
        return None
    if oAttack.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
        return None
    if not oAttack.m_Part:
        return None
    oGame = oAttack.m_Game
    oReason = oSkill.m_Base['RS']
    oPart = oAttack.m_Game.GetObject(oAttack.m_Part)
    iDataSID = oAttack.m_SID
    clsData = oGame.m_WarData.GetMonsterData(iDataSID)
    iRound = oGame.m_WarMgr.m_Round
    iGrade = oAttack.m_Grade
    for sAttr, iType in cl_formula.g_PartTransAttr.items():
        if iType == cl_formula.OTHER_TRANS:
            if sAttr == 'HP':
                dReason = {
                    'Type': TYPE_RELIFE_PASSIVE }
                dRelifeInfo = {
                    'HP': oAttack.HP(),
                    'Shield': 0,
                    'Armor': 0 }
                oPart.Relife(dReason, dRelifeInfo)
                ResetBaseAttr(oAttack, 'HPMax')
                oAttack.HPDirectModify('HP', oAttack.m_ID, oAttack.QueryAttr('HPMax'), oReason)
            elif sAttr == 'MoveSpeed':
                oAgent = oAttack.m_Agent
                if oAgent:
                    oAgent.SetActionSMPatrol(oAgent)
                    ResetBaseAttr(oPart, 'MoveSpeed')
                    ResetBaseAttr(oAttack, 'MoveSpeed')
                    continue
                continue
        if iType == cl_formula.ATTR_TRANS:
            Attr = getattr(oAttack, sAttr)
            if not Attr:
                continue
            setattr(oPart, sAttr, Attr)
            Attr = getattr(clsData, sAttr)
            if not Attr:
                continue
            setattr(oAttack, sAttr, Attr)
            continue
        if iType == cl_formula.QUERY_TRANS:
            ResetBaseAttr(oPart, sAttr)
            ResetBaseAttr(oAttack, sAttr)
    
    oAttack.SetPhase(1)


def ChangeFlyingMuzzleTarget(oSkill, sid, iTargetID):
    dCartoon = oSkill.GetCartoonBySID(sid)
    dNet = {
        'LockTarget': [
            iTargetID] }
    oSkill.Send(dCartoon['ID'], dNet)
    oSkill.NetSkillTrigger()


def CheckSightCentrePosDis(oSkill, vStart, iDis):
    oAttack = oSkill.GetAttack()
    vPos = oAttack.GetPos()
    vPos = (vPos[0], vPos[1] + oSkill.m_Base['ModelHeight'] * 0.85, vPos[2])
    if not cl_math.CheckDistance3D(vPos, vStart, iDis):
        oSkill.LogCheckErr('startfail %s %s' % (vPos, vStart))
        return None
    bAnyHit = oSkill.m_Game.Scene_RaycastAnyHit(oSkill.m_Base['Scene'], vPos, vStart, PXMASK_SKILLBLK)
    if bAnyHit:
        oSkill.LogCheckErr('startfail %s %s' % (vPos, vStart))
        return None


def CheckIsHover(oSkill, sid):
    dCartoon = oSkill.GetCartoonBySID(sid)
    if 'FlyOverDis' in dCartoon:
        return True
    return False


def ChangePosListToCloseGround(oSkill, lstPos):
    oGame = oSkill.m_Game
    lstRes = []
    for vPos in lstPos:
        vPos = oGame.Scene_NavMeshRayCast(oSkill.m_Base['Scene'], (vPos[0], vPos[1] + 0.5, vPos[2]), (vPos[0], vPos[1] - 5, vPos[2]))
        lstRes.append(vPos)
    
    return lstRes


def HaltTargetAllCasting(oSkill, lstTarget):
    oGame = oSkill.m_Game
    for iTarget in lstTarget:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        cl_action.HaltAllCasting(oTarget, 'Skill%s' % oSkill.m_Base['pfid'])
    


def GetIntLstSubscript(oSkill, lstInfo, index):
    return lstInfo[index]


def GetVct3LstSubscript(oSkill, lstInfo, index):
    return lstInfo[index]


def CheckPopupHook(oSkill, dArgs):
    if 'CurVID' not in oSkill.m_Update:
        return 0
    oGame = oSkill.m_Game
    iVictim = oSkill.m_Update['CurVID']
    oVictim = oGame.GetObject(iVictim, PY_FLAG_DEAD)
    oAttack = oSkill.GetAttack()
    if not oVictim:
        return 0
    if oVictim.m_SID == 213:
        iState = dArgs['State']
        if oVictim.m_State.GetItemBySID(iState):
            iCosAngle = dArgs['CosAngle']
            if not cl_math.CheckVector2Angle(cl_math.Vec3Minus(oAttack.GetPos(), oVictim.GetPos()), oVictim.GetFacing(), iCosAngle):
                return 1
    return 0


def GetListByShuffleAndNumber(oSkill, lstPos, iNumber):
    oGame = oSkill.m_Game
    return ShufferList(oGame, lstPos, iNumber)


def GetSkillHitArea(oSkill):
    return oSkill.m_Update['CurHitArea']


def GetHitTimesAtpointTarget(oSkill, iTarget):
    dHitInfo = oSkill.m_Collect['HitTimesInfo'] if 'HitTimesInfo' in oSkill.m_Collect else { }
    if iTarget in dHitInfo:
        return dHitInfo[iTarget]
    return 0


def RemoveTargetsAllStateByType(oSkill, lstTarget, iType):
    oGame = oSkill.m_Game
    for iTarget in lstTarget:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        oStateCon = oTarget.m_State
        for oState in oStateCon.Values():
            if oState.m_Type == iType:
                oStateCon.RemoveItem(oState.m_ID)
        
    


def GetBulletCurPos(oSkill, iSID):
    return GetCurrentBulletPosition(oSkill, iSID)


def GetCurrentBulletPosition(oSkill, iSID):
    return (0, 0, 0)


def GetCurBulletFinalPos(oSkill, iSID):
    return (0, 0, 0)


def ModifyMonsterNavMesh(oSkill, iShape):
    oGame = oSkill.m_Game
    iAttack = oSkill.m_Base['AID']
    oAttack = oGame.GetObject(iAttack)
    if not oAttack or not (oAttack.m_FightType & WARRIOR_MONSTER):
        return None
    if not iShape or not cl_modeldefine.IsValidModelShape(iShape):
        WarobjLog.Alert('%s ModifyMonsterNavMesh shape err %s' % (oSkill.m_Base['pfid'], iShape))
        return None
    oAttack.m_Shape = iShape
    oAttack.GS2CPropChange('Shape')
    oAttack.m_MoveCtrl.InitParams(oAttack)


def SetRigidbodySimulation(oSkill, iWarrior, bOpen):
    oGame = oSkill.m_Game
    oWarrior = oGame.GetObject(iWarrior)
    if oWarrior and oWarrior.m_PhyModel:
        oWarrior.m_PhyModel.rigidbody.E_SetEnableSimulation(int(bOpen))


def SetRigidbodyKinematic(oSkill, iWarrior, bOpen):
    oGame = oSkill.m_Game
    oWarrior = oGame.GetObject(iWarrior)
    if oWarrior and oWarrior.m_PhyModel:
        oWarrior.m_PhyModel.rigidbody.E_SetKinematic(int(bOpen))


def GetKeyItemPos(oSkill, iSID):
    oGame = oSkill.m_Game
    iScene = oSkill.m_Base['Scene']
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return None
    lstDrop = oScene.GetObjectsByType('Drop')
    for iDrop in lstDrop:
        oDrop = oGame.GetObject(iDrop)
        if oDrop.m_FightType == NWARRIOR_DROP_KEYITEM and oDrop.m_DropInfo[0].m_SID == iSID:
            vPos = oDrop.GetPos()
            break
    else:
        oAttack = oSkill.GetAttack()
        vPos = oAttack.GetPos()
    return vPos


def GetPosWithinCircle(oSkill, iRadius, iNum, bBaseVictim):
    oGame = oSkill.m_Game
    oTarget = oGame.GetObject(oSkill.m_Base['VID']) if bBaseVictim else oSkill.GetAttack()
    if not oTarget:
        if bBaseVictim:
            oAttack = oSkill.GetAttack()
            vPos = oAttack.GetPos() if oAttack else oSkill.m_Base['vStart']
        else:
            vPos = oSkill.m_Base['vStart']
        return [ vPos for i in range(iNum) ]
    vTargetPos = oTarget.GetPos()
    if bBaseVictim:
        vTargetPos = cl_math.Vec3Add(vTargetPos, (0, 0.1, 0))
    (px, py, pz) = vTargetPos
    (fx, _, fz) = oTarget.GetFacing() if oTarget.GetFacing() else (0, 0, -100)
    lstRes = []
    iRadius = int(iRadius)
    for _ in range(iNum):
        iDis = oGame.Random(iRadius + 1)
        iAngle = oGame.Random(360)
        (tx, tz) = cl_math.Vec2DestPosDir((px, pz), (fx, fz), iDis, iAngle)
        vTar = (tx, py, tz)
        lstRes.append(vTar)
    
    return lstRes


def GetTargetPhase(oSkill, iTarget):
    oTarget = oSkill.m_Game.GetObject(iTarget, PY_FLAG_DEAD)
    if not oTarget:
        return 0
    return oTarget.m_Phase


def CreateViscoelastic(oSkill, iSID):
    pass


def IsCurSkillTrigger(oSkill, sid):
    if 'Trigger' in oSkill.m_Update:
        return True
    return False


def CheckVictimSameLastVictim(oSkill, sid):
    iHitPart = oSkill.m_Update['CurHitArea'] if 'CurHitArea' in oSkill.m_Update else 0
    if iHitPart == MONSTER_PART_SHIELD:
        return False
    dCartoon = oSkill.GetCartoonBySID(sid)
    iVictim = oSkill.m_Update['CurVID']
    iLastVictim = dCartoon['LastVID'] if 'LastVID' in dCartoon else 0
    if not iLastVictim or iLastVictim != iVictim:
        dCartoon['LastVID'] = iVictim
        return False
    return True


def CrtArgMuzzleTransform(oSkill, Name):
    pass


def SetAttackStateStatistics(oSkill, iStateSID, sAttr, iValue):
    oAttack = oSkill.GetAttack()
    oState = oAttack.m_State.GetItemBySID(iStateSID)
    if oState:
        oState.m_Data[sAttr] = iValue


def SetCastingRayShootEnd(oSkill):
    pass


def CrtArgGetTransPos(oSkill, trans):
    return (0, 0, 0)


def GetSkillEffectByKey(oSkill, Idx):
    pass


def GetHeroTrans(oSkill):
    pass


def FloatToIntFloor(oSkill, value):
    return int(value)


def GetCustomPid(oSkill):
    return oSkill.m_Base['AID']


def AddWeaponPFBullet(oSkill, iAdd):
    oAttack = oSkill.GetAttack()
    oPerform = oAttack.GetPerform(oSkill.m_Base['pfid'], oSkill.m_Base['Weapon'])
    if oPerform:
        oPerform.AddPFBullet(iAdd)


def ChooseBoxGemSummonPos(oSkill, iNum):
    oAttack = oSkill.GetAttack()
    if not oAttack.m_LineIdx:
        return []
    oGame = oAttack.m_Game
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    oLine = oLevelCtrl.GetLineNode(oAttack.m_LineIdx)
    iLevel = oLine.m_LevelNode.m_Level
    dSummonAreaConfig = oLevelCtrl.m_LevelConfData.GetLineConfig(iLevel, oLine.m_Name, 'summonarea')
    if not dSummonAreaConfig:
        SendAlert('err', f'''{iLevel} {oLine.m_Name} 路线未配置召唤点''')
        return []
    lstSummonPos = [ dArea['center'] for dArea in dSummonAreaConfig.values() ]
    iLen = len(lstSummonPos)
    if iLen <= iNum:
        return lstSummonPos
    iLeft = iLen
    for _ in range(iNum):
        iRandIndex = oGame.Random(iLeft)
        lstSummonPos[iRandIndex] = lstSummonPos[iLeft - 1]
        lstSummonPos[iLeft - 1] = lstSummonPos[iRandIndex]
        iLeft -= 1
    
    return lstSummonPos[-iNum:]


def IsSkillWeaponType(oSkill, iType):
    if 'ItemType' not in oSkill.m_Cache:
        return False
    return oSkill.m_Cache['ItemType'] == iType


def SetDirectHitInfo(oSkill, iTarget):
    oGame = oSkill.m_Game
    oTarget = oGame.GetObject(iTarget)
    if not oTarget:
        oSkill.m_Update['CurVID'] = 0
        return None
    if not cl_math.CheckTargetType(oGame, oTarget, oSkill.m_Base['AID'], oSkill.m_Cache['Side'], OBJ_ENEMY):
        iTarget = 0
    oSkill.m_Update['CurVID'] = iTarget
    lstVictim = oSkill.m_Update['LastVLST'] if 'LastVLST' in oSkill.m_Update else []
    if iTarget not in lstVictim:
        lstVictim.append(iTarget)
    lstPos = oSkill.m_Collect['CartoonPos'] if 'CartoonPos' in oSkill.m_Collect else []
    vPos = oTarget.GetPos()
    vPos = (vPos[0], vPos[1] + oTarget.m_ModelHeight * 0.85, vPos[2])
    lstPos.append((vPos, vPos))
    oSkill.m_Collect['CartoonPos'] = lstPos
    oSkill.m_Collect['DirectHitCurPos'] = vPos
    oSkill.m_Update['LastVLST'] = lstVictim


def CreateMonsterAtPos(oSkill, iMonterSID, vPos, iPhase, bFollowSkill, sMark, bLineGoal = False, bFollowDie = False):
    
    def ClearSkillMonster(iMonsterID, oSkill):
        oClrearMonster = oGame.GetObject(iMonsterID)
        if oClrearMonster:
            oClrearMonster.DieClearEffect()
            oClrearMonster.Remove('SkillOver')

    
    def OnMonsterDie(oDieMonster, dMsgInfo):
        oLevelNode.UnlockRoom(iRoomPos, sKey)

    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oAgent = oAttack.m_Agent
    dConfig = oAgent.m_Config
    oGame = oSkill.m_Game
    iScene = oAttack.m_Scene
    tFace = oAttack.GetFacing()
    tLine = oAttack.m_LineIdx
    dConfig.pop('PFAI', 0)
    oMonster = oGame.m_ResMgr.CreateMonster(iScene, iMonterSID, vPos, tFace, SIDE_TYPE_MONSTER, 0, dConfig, tLine, {
        'Owner': oAttack.m_ID })
    if not oMonster or oMonster.IsDead():
        return None
    iMonster = oMonster.m_ID
    lstSummon = oSkill.m_Collect.setdefault('SummonCreate', [])
    lstSummon.append(iMonster)
    dMark = oAttack.Query(sMark, { })
    if sMark in dMark:
        lstMark = dMark[sMark]
        lstMark.append(iMonster)
    else:
        lstMark = [
            iMonster]
    oAttack.Set(sMark, {
        sMark: lstMark })
    if iPhase:
        oMonster.SetPhase(iPhase)
    if bFollowSkill:
        oSkill.AddEndFunc(Functor(ClearSkillMonster, iMonster))
    if bFollowDie:
        oAttack.m_FollowDieObjs[iMonster] = 1
    if bLineGoal and tLine:
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        (iLevel, iRoomPos, _) = tLine
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        if oLevelNode:
            sKey = '%s-%s-%s' % (oSkill.m_Base['PFKey'], iMonterSID, iMonster)
            oLevelNode.LockRoom(iRoomPos, sKey)
            cl_msgcenter.AddFunction(oMonster, cl_msgcenter.MSG_WAR_DIE, OnMonsterDie, sKey, iOnce = 0)


def GetCartoonHitTarget(oSkill, sid):
    dCartoon = oSkill.GetCartoonBySID(sid)
    if 'AllTarget' not in dCartoon:
        oSkill.LogCheckErr('crt:%d no AllTarget' % sid)
        return []
    return dCartoon['AllTarget']


def CheckOnlySkill(oSkill):
    iAttack = oSkill.m_Base['AID']
    iWeapon = oSkill.m_Base['Weapon']
    iActNum = oSkill.m_Base['ActNum']
    oSkillMgr = oSkill.m_Game.m_SkillMgr
    lstSkill = oSkillMgr.GetSkillBySID(oSkill.m_Base['pfid'])
    for oCurSkill in lstSkill:
        if oCurSkill.m_Base['AID'] == iAttack or oCurSkill.m_Base['ActNum'] == iActNum:
            continue
        if oCurSkill.m_Base['Weapon'] == iWeapon:
            return False
    
    return True


def CheckIsHalt(oSkill):
    return False


def CalLockDistance(oSkill, iDistance):
    return 0


def SpecialChoose(oSkill, res1, res2, res3, res4):
    return 0


def CrtArgToCameraRotation(oSkill, vTrans):
    return (0, 0, 0)


def CheckCurLevel(oSkill, iLevel):
    iScene = oSkill.m_Base['Scene']
    oScene = oSkill.m_Game.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return False
    if oScene.m_Level == iLevel:
        return True
    return False


def CheckCurLevelType(oSkill, iLevelType):
    iScene = oSkill.m_Base['Scene']
    oScene = oSkill.m_Game.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return False
    oLevelCtrl = oSkill.m_Game.m_WarMgr.GetComponent('LevelCtrl')
    oLevelNode = oLevelCtrl.GetLevelNode(oScene.m_Level)
    if oLevelNode:
        return oLevelNode.m_LevelType == iLevelType
    return False


def GetTargetCenterPos(oSkill, iTarget):
    oTarget = oSkill.m_Game.GetObject(iTarget)
    if oTarget:
        vPos = oTarget.GetPos()
        vPos = (vPos[0], vPos[1] + oTarget.m_ModelHeight / 2, vPos[2])
    else:
        vPos = (0, 0, 0)
    return vPos


def GetSkillCustomArg(oSkill, sKey):
    return 0


def GetTargetListSortByDisInRange(oSkill, iTargetType, fRange, iIgnoreBlock, iNum, iSight, fAttackHeightRatio, fTargetHeightRatio, iSort, iNoPetrochemical):
    if fRange <= 0 or iNum <= 0:
        return []
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return []
    lstTarget = []
    oGame = oSkill.m_Game
    if iTargetType & WARRIOR_MONSTER:
        iPxMask = PXMASK_MONSTER
    else:
        iPxMask = PXMASK_LIVEOBJ
    dMask = {
        'Mask': iPxMask }
    if iIgnoreBlock:
        dMask['BlockMask'] = 0
    vAttack = oAttack.GetCenter()
    lstArgs = [
        vAttack,
        fRange]
    iScene = oSkill.m_Base['Scene']
    lstVLST = cl_math.GetAttackTargetList(oGame, iScene, ATT_SHAPE_SPHERE, lstArgs, dMask)
    if not lstVLST:
        return lstTarget
    if iSort:
        dDis = oGame.Scene_GetTargetDisMap(oAttack.m_ID, list(lstVLST))
        lstVLST = sorted(dDis, key = dDis.get)
    if iSight:
        vStart = (vAttack[0], vAttack[1] + oAttack.m_ModelHeight * fAttackHeightRatio, vAttack[2])
    for iTarget in lstVLST:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget or iTargetType & oTarget.m_FightType != iTargetType:
            continue
        if iNoPetrochemical and oTarget.m_FightType & WARRIOR_MONSTER and oTarget.IsPetrochemical():
            continue
        if iSight:
            vTarget = oTarget.GetPos()
            vEnd = (vTarget[0], vTarget[1] + oTarget.m_ModelHeight * fTargetHeightRatio, vTarget[2])
            bAnyHit = oGame.Scene_RaycastAnyHit(iScene, vStart, vEnd, PXMASK_SIGHTBLK)
            if bAnyHit:
                continue
            continue
        lstTarget.append(iTarget)
        iNum -= 1
        if iNum <= 0:
            break
    
    return lstTarget


def SetSkillVictimByLoopIndex(oSkill, lstTarget, iIndex):
    if not lstTarget:
        return None
    iLen = len(lstTarget)
    iTarget = lstTarget[iIndex % iLen]
    oSkill.m_Base['VID'] = iTarget


def GetNearestMonsterInRange(oSkill, fRange, iFiltleHistory, iIgnoreBlock, iSight, fAttackHeightRatio, fTargetHeightRatio, iUseVictim = 0, iExcludeState = 0, iExcludeStateCountMin = 0, iExcludeStateFromAttack = 0):
    if fRange <= 0:
        return 0
    if iUseVictim:
        if 'CurVID' in oSkill.m_Update:
            iVictim = oSkill.m_Update['CurVID']
        else:
            iVictim = oSkill.m_Base['VID']
        oCenterTarget = oSkill.m_Game.GetObject(iVictim)
    else:
        oCenterTarget = oSkill.GetAttack()
    if not oCenterTarget:
        return 0
    oGame = oSkill.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oCenterTarget.m_Scene)
    if not oScene:
        return 0
    dMask = {
        'Mask': PXMASK_MONSTER }
    if iIgnoreBlock:
        dMask['BlockMask'] = 0
    if iUseVictim:
        dMask['PassID'] = oCenterTarget.m_ID
    vCenter = oCenterTarget.GetPos()
    lstArgs = [
        vCenter,
        fRange]
    iScene = oSkill.m_Base['Scene']
    lstVLST = cl_math.GetAttackTargetList(oGame, iScene, ATT_SHAPE_SPHERE, lstArgs, dMask)
    if not lstVLST:
        return 0
    dDis = oGame.Scene_GetTargetDisMap(oCenterTarget.m_ID, list(lstVLST))
    lstSortDis = sorted(dDis.items(), key = (lambda item: item[1]))
    if iSight:
        vStart = (vCenter[0], vCenter[1] + oCenterTarget.m_ModelHeight * fAttackHeightRatio, vCenter[2])
    dHistory = oSkill.m_Collect.setdefault('HistoryTarget', { }) if iFiltleHistory else { }
    lstIgnore = []
    for iTarget, _ in lstSortDis:
        if iFiltleHistory and iTarget in dHistory:
            lstIgnore.append(iTarget)
            continue
        oTarget = oGame.GetObject(iTarget, PY_FLAG_SERVANTTARGET)
        if not oTarget:
            continue
        if iExcludeState:
            lstExcludeState = oTarget.m_State.GetItems(iExcludeState)
            bExclude = False
            for oExcludeState in lstExcludeState:
                if iExcludeStateFromAttack and oExcludeState.m_Attacker != oSkill.m_Base['AID']:
                    continue
                if not not iExcludeStateCountMin:
                    if oExcludeState.GetCount() >= iExcludeStateCountMin:
                        bExclude = True
                        break
            
            if bExclude:
                continue
            continue
        if iSight:
            vTarget = oTarget.GetPos()
            vEnd = (vTarget[0], vTarget[1] + oTarget.m_ModelHeight * fTargetHeightRatio, vTarget[2])
            bAnyHit = oGame.Scene_RaycastAnyHit(iScene, vStart, vEnd, PXMASK_SIGHTBLK)
            if bAnyHit:
                continue
            continue
        if iFiltleHistory:
            dHistory[iTarget] = 1
        return iTarget
    
    if lstIgnore:
        dNewHistory = { }
        oSkill.m_Collect['HistoryTarget'] = dNewHistory
        for iTarget in lstIgnore:
            oTarget = oGame.GetObject(iTarget, PY_FLAG_SERVANTTARGET)
            if not oTarget:
                continue
            if iSight:
                vTarget = oTarget.GetPos()
                vEnd = (vTarget[0], vTarget[1] + oTarget.m_ModelHeight * fTargetHeightRatio, vTarget[2])
                bAnyHit = oGame.Scene_RaycastAnyHit(iScene, vStart, vEnd, PXMASK_SIGHTBLK)
                if bAnyHit:
                    continue
                continue
            dNewHistory[iTarget] = 1
            return iTarget
        
    return 0


def CheckWeaponByUnHoldType(oSkill, iType):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return 0
    lstItem = oAttack.m_WieldCon.GetWeapons(iFlag = -1)
    if not lstItem:
        return 0
    for oItem in lstItem:
        if CheckWeaponType2(oItem, iType):
            return 1
    
    return 0


def IsMainWeaponInDouble(oSkill):
    return False


def ListHasWeaponType(oSkill, iType, lstType):
    if iType in lstType:
        return 1
    return 0


def GetLuohouWeakerID(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return 0
    iWeakerID = oAttack.Query('Luohou_Weaker', 0)
    return iWeakerID


def GetHeroInSightArgs(oSkill, iAngle, fDis, bBlock, iExcludeTarget, vMuzzlepos):
    oGame = oSkill.m_Game
    iScene = oSkill.m_Base['Scene']
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    oAttack = oSkill.GetAttack()
    lstHero = []
    if not oScene or not oAttack:
        return lstHero
    vAttack = oAttack.GetPos()
    vFace = oAttack.GetFacing()
    for iHero in oScene.GetHeros():
        oHero = oGame.GetObject(iHero, PY_FLAG_DEAD)
        if not oHero:
            continue
        if oHero.m_ID == iExcludeTarget:
            continue
        vTarget = oHero.GetPos()
        if not cl_math.CheckDistance3D(vAttack, vTarget, fDis):
            continue
        disp = cl_math.Vec3Minus(vTarget, vAttack)
        if cl_math.CheckVector2Angle(disp, vFace, iAngle):
            continue
        if bBlock:
            vTarget = (vTarget[0], vTarget[1] + oHero.m_ModelHeight * 0.93, vTarget[2])
            bAnyHit = oGame.Scene_RaycastAnyHit(iScene, vMuzzlepos, vTarget, PXMASK_SIGHTBLK)
            if bAnyHit:
                continue
            continue
        lstHero.append(iHero)
    
    return lstHero


def GetSceneObstacleNumberBySID(oSkill, iSID):
    oGame = oSkill.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oSkill.m_Base['Scene'])
    if not oScene:
        return 0
    lstObstacle = oScene.GetObjectsByType('Obstacle')
    iCnt = 0
    for iObstacle in lstObstacle:
        oObstacle = oGame.GetObject(iObstacle, PY_FLAG_DEAD)
        if oObstacle and oObstacle.m_SID == iSID:
            iCnt += 1
    
    return iCnt


def CheckVictimBeExecuted(oSkill, iVictim):
    oGame = oSkill.m_Game
    oVictim = oGame.GetObject(iVictim, PY_FLAG_DEAD)
    if not oVictim:
        return False
    if not oVictim.m_FightType & WARRIOR_MONSTER:
        return False
    if oVictim.IsWudi() and oVictim.m_FightType & WARRIOR_BOSS == WARRIOR_BOSS:
        return False
    oAttack = oSkill.GetAttack()
    if oAttack.m_SID != EXECUTOR_HERO:
        return False
    return oAttack.m_FlawCon.CheckMonsterBeExecuted(oVictim)


def KillCurVictim(oSkill, iClearRelife):
    if 'CurVID' not in oSkill.m_Update:
        return None
    KillTarget(oSkill, oSkill.m_Update['CurVID'], iClearRelife)


def KillTarget(oSkill, iTarget, iClearRelife):
    oGame = oSkill.m_Game
    oVictim = oGame.GetObject(iTarget, PY_FLAG_DEAD)
    if not oVictim:
        return None
    if not oVictim.m_FightType & WARRIOR_MONSTER:
        return None
    if oVictim.IsWudi() and oVictim.m_FightType & WARRIOR_BOSS == WARRIOR_BOSS:
        return None
    if iClearRelife:
        oVictim.Set('RelifeInfo', { })
    iAttack = oSkill.m_Base['AID']
    oReason = oSkill.m_Base['RS']
    oAttack = oSkill.GetAttack()
    sReason = oReason.GetStrReason()
    oVictim.SetDiePriority(DIE_PRIORITY_KILL, sReason)
    iActNum = oReason.Query('ActNum', 0)
    WarobjLog.Debug('%s %s pfkill %s reason %s' % (oGame.m_ID, oAttack.m_PlayerID, oVictim.m_SID, oReason.GetStrReason()))
    dMsgInfo = {
        'Skill': oSkill,
        'VID': iTarget,
        'CurVID': iTarget,
        'PredictChange': [
            oVictim.Shield(),
            oVictim.Armor(),
            oVictim.HP()] }
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_PFNODEKILLED_BEFORE, oVictim, dMsgInfo)
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_PFNODEKILL, oAttack, dMsgInfo)
    (iShield, iArmor, iHP) = dMsgInfo['PredictChange']
    if iShield:
        oVictim.HPDirectModify('Shield', iAttack, -iShield, oReason)
    if iArmor:
        oVictim.HPDirectModify('Armor', iAttack, -iArmor, oReason)
    if iHP:
        oVictim.HPDirectModify('HP', iAttack, -iHP, oReason)
    oVictim.ClearDiePriority(sReason)
    iBreakShield = 1 if iShield else 0
    cl_snetwar.GS2CWStatusHP(oVictim, oSkill, oAttack.m_PlayerID, iAttack, iActNum, 99999900, DAM_TYPE_TRUE, 0, iBreakShield, 0, 1, KILL_DAMAGE)


def GetTargetFlawCount(oSkill, iTarget):
    oAttack = oSkill.GetAttack()
    if oAttack.m_SID != EXECUTOR_HERO:
        return None
    dFlaw = oAttack.m_FlawCon.GetFlaw(iTarget)
    if dFlaw:
        return len(dFlaw)
    return 0


def GetTargetFlaw(oSkill, iTarget, bIncludeWeakness):
    oAttack = oSkill.GetAttack()
    if oAttack.m_SID != EXECUTOR_HERO:
        return None
    dFlaw = oAttack.m_FlawCon.GetFlaw(iTarget)
    if not dFlaw:
        return []
    if bIncludeWeakness:
        return list(dFlaw)
    lstFlaw = []
    for iFlaw, dInfo in dFlaw.items():
        if dInfo[FLAW_ISWEAKNESS]:
            continue
        lstFlaw.append(iFlaw)
    
    return lstFlaw


def GetCurKillLineDamage(oSkill):
    if 'CurVID' not in oSkill.m_Update:
        return 0
    oGame = oSkill.m_Game
    iVictim = oSkill.m_Update['CurVID']
    oVictim = oGame.GetObject(iVictim, PY_FLAG_DEAD)
    if not oVictim:
        return 0
    oAttack = oSkill.GetAttack()
    if oAttack.m_SID != EXECUTOR_HERO:
        return 0
    iKillLine = oAttack.m_FlawCon.GetKillLine(oVictim)
    iKillLineDamage = (oVictim.QueryAttr('HPMax') + oVictim.QueryAttr('ShieldMax') + oVictim.QueryAttr('ArmorMax')) * iKillLine // 10000
    return iKillLineDamage


def GetVictimHPShieldArmor(oSkill):
    if 'CurVID' not in oSkill.m_Update:
        return 0
    oGame = oSkill.m_Game
    iVictim = oSkill.m_Update['CurVID']
    oVictim = oGame.GetObject(iVictim, PY_FLAG_DEAD)
    if not oVictim:
        return 0
    return oVictim.HP() + oVictim.Shield() + oVictim.Armor()


def GetVictimHPShieldArmorMax(oSkill):
    if 'CurVID' not in oSkill.m_Update:
        return 0
    oGame = oSkill.m_Game
    iVictim = oSkill.m_Update['CurVID']
    oVictim = oGame.GetObject(iVictim, PY_FLAG_DEAD)
    if not oVictim:
        return 0
    return oVictim.QueryAttr('HPMax') + oVictim.QueryAttr('ShieldMax') + oVictim.QueryAttr('ArmorMax')


def EndDelayAttackUsePerform(oSkill, iPerform, dCustomData, iDelay, iVictim, bIgnoreoTargetDie):
    
    def UsePerform(oAttack):
        if oAttack.IsDead():
            return None
        if iVictim:
            oGame = oAttack.m_Game
            if bIgnoreoTargetDie:
                oTarget = oGame.GetObject(iVictim)
            else:
                oTarget = oGame.GetObject(iVictim, PY_FLAG_DEAD)
            if not oTarget:
                return None
            vTargetPos = oTarget.GetPos()
            vTargetPos = (vTargetPos[0], vTargetPos[1] + oTarget.m_ModelHeight / 2, vTargetPos[2])
            dData['vStart'] = vTargetPos
            dData['VID'] = iVictim
        pfobj = oAttack.GetPerform(iPerform)
        if not pfobj:
            return None
        cl_war.UsePerform(oAttack, pfobj, dData)

    
    def EndFunc(oSkill):
        oAttack = oSkill.GetAttack()
        if not oAttack:
            return None
        if iDelay:
            iFrame = Time2Frame(iDelay)
            oAttack.Call_Out(Functor(UsePerform, oAttack), iFrame, f'''EndDelayAttackeUsePerform{oSkill.m_SkillID}''')
            return None
        UsePerform(oAttack)

    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    if not oAttack.GetPerform(iPerform):
        oAttack.AddPerform(iPerform, 1)
    pfobj = oAttack.GetPerform(iPerform)
    if not pfobj:
        return None
    if iVictim:
        oVictim = oSkill.m_Game.GetObject(iVictim)
        if not oVictim:
            return None
    dData = {
        'Custom': dCustomData }
    oSkill.AddEndFunc(EndFunc)


def GetSpecificPerformArgValue(oSkill, iPerform, sAttr, iDefault = 0):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return iDefault
    oPerform = oAttack.GetPerform(iPerform)
    if not oPerform:
        return iDefault
    return oPerform.GetArgValue(sAttr, iDefault)


def GetPointTargetModelHeight(oSkill, iTarget):
    oGame = oSkill.m_Game
    oTarget = oGame.GetObject(iTarget)
    if not oTarget:
        return 0
    return oTarget.m_ModelHeight


def GetLockTargetID(oSkill, iDefault = 0):
    dCustom = oSkill.m_Custom
    if 'LockTarget' in dCustom and dCustom['LockTarget']:
        return dCustom['LockTarget'][0]
    return iDefault


def TargetSetStateTime(oSkill, iTarget, iStateSID, iTime):
    oTarget = oSkill.m_Game.GetObject(iTarget)
    if not oTarget:
        return None
    oState = oTarget.m_State.GetItemBySID(iStateSID)
    if not oState:
        return None
    oState.SetTime(oTarget, Time2Frame(iTime), 0)


def CheckMonsterType(oSkill, iFightType, iMonster):
    oVictim = oSkill.m_Game.GetObject(iMonster)
    if not oVictim:
        return 0
    if 255 & iFightType:
        if oVictim.m_FightType == iFightType:
            return 1
        return 0
    if oVictim.m_FightType & iFightType == iFightType:
        return 1
    return 0


def TargetGetStateRemainTime(oSkill, iTarget, iStateSID):
    oTarget = oSkill.m_Game.GetObject(iTarget)
    if not oTarget:
        return 0
    oState = oTarget.m_State.GetItemBySID(iStateSID)
    if oState:
        return Frame2Time(oState.GetRemainTime())
    return 0


def GetDeviceAttr(oSkill, sAttr):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return 0
    oDevice = oAttack.GetDevice()
    if oDevice:
        return oDevice.QueryAttr(sAttr)
    return 0


def UpdateDictSkillCustomData(oSkill, sDictKey, iKey, iValue):
    dCustom = oSkill.m_Custom
    if sDictKey not in dCustom:
        dCustom[sDictKey] = { }
    dCustom[sDictKey][iKey] = iValue


def GetDictValueFromSkillCustomData(oSkill, sDictKey, iCheckKey, iDefault = 0):
    dCustom = oSkill.m_Custom
    if sDictKey not in dCustom or iCheckKey not in dCustom[sDictKey]:
        return iDefault
    return dCustom[sDictKey][iCheckKey]


def GetNowFrame(oSkill):
    return oSkill.m_Game.GetFrameNum()


def ArrangeDevice(oSkill, vPos, vFace, dInfo, iAttach):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    if iAttach:
        iVictim = oSkill.m_Update['CurVID'] if 'CurVID' in oSkill.m_Update else 0
        if iVictim:
            oVictim = oSkill.m_Game.GetObject(iVictim, PY_FLAG_DEAD)
            if oVictim:
                dInfo['Victim'] = iVictim
                dInfo['AttachPart'] = oSkill.m_Update['CurHitArea'] if 'CurHitArea' in oSkill.m_Update else 0
    oAttack.m_DeviceMgr.DeployDevice(oAttack.m_Scene, vPos, vFace, dInfo)


def RecycleDevice(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oAttack.m_DeviceMgr.RecycleDevice()


def ModifyDeviceEnergy(oSkill, iChange):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oAttack.DeviceEnergyModify(iChange)


def EnableDevicePerform(oSkill, iPerform):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oDevice = oAttack.GetDevice()
    if not oDevice:
        return None
    oPerform = oDevice.GetPerform(iPerform)
    if not oPerform:
        return None
    oPerform.Enable(oDevice)


def DisableDevicePerform(oSkill, iPerform):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oDevice = oAttack.GetDevice()
    if not oDevice:
        return None
    oPerform = oDevice.GetPerform(iPerform)
    if not oPerform:
        return None
    oPerform.Disable(oDevice)


def CheckDeciveStatus(oSkill, iDeployed, iActive):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return False
    return oAttack.CheckDeciveStatus(iDeployed, iActive)


def SetDeciveAcitveStatus(oSkill, iActive):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oAttack.m_DeviceMgr.SetDeciveActiveStatus(iActive)


def DisableWeaponPerform(oSkill, iPerform):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    iItem = oSkill.m_Base['Weapon']
    oWeapon = oAttack.m_WieldCon.GetItemByID(iItem)
    if not oWeapon:
        return None
    oPerformCom = oWeapon.GetComponent('Perform')
    if not oPerformCom:
        return None
    oPerform = oPerformCom.GetPerform(iPerform)
    if not oPerform:
        return None
    oPerform.Disable(oAttack)


def EnableWeaponPerform(oSkill, iPerform):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    iItem = oSkill.m_Base['Weapon']
    oWeapon = oAttack.m_WieldCon.GetItemByID(iItem)
    if not oWeapon:
        return None
    oPerformCom = oWeapon.GetComponent('Perform')
    if not oPerformCom:
        return None
    oPerform = oPerformCom.GetPerform(iPerform)
    if not oPerform:
        return None
    oPerform.Enable(oAttack)


def SetDeviceMovePos(oSkill, vPos):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oDevice = oAttack.GetDevice()
    if not oDevice or not (oDevice.m_Scene) or not (oDevice.m_Agent):
        return None
    if not oDevice.DeployStatus():
        return None
    oGame = oSkill.m_Game
    iScene = oDevice.m_Scene
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return None
    if not oScene.IsInSceneBound(vPos):
        return None
    fGroundDis = oGame.Scene_GroundDistance(iScene, (vPos[0], vPos[1] + 0.2, vPos[2]), 10, PXMASK_GROUNDBLK, oAttack.m_ID)
    vPos = (vPos[0], vPos[1] + 0.2 - fGroundDis, vPos[2])
    oAgent = oDevice.m_Agent
    oAgent.SetData('ArrivePos', vPos)
    oAgent.SetData('TransferPos', vPos)
    oAgent.m_GameSpace.CallDelayUpdate(oAgent, 1)


def SwitchDeviceFollowMoveStatus(oSkill, iStatus):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oDevice = oAttack.GetDevice()
    if not oDevice or not (oDevice.m_Agent):
        return None
    oDevice.SwitchFollowMoveStatus(iStatus)


def EndDeviceUsePerform(oSkill, iPerform, dCustomData):
    
    def EndFunc(oSkill):
        pfobj = oDecive.GetPerform(iPerform)
        if not pfobj:
            return None
        cl_war.UsePerform(oDecive, pfobj, {
            'Custom': dCustomData })

    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oDecive = oAttack.GetDevice()
    if not oDecive:
        return None
    oSkill.AddEndFunc(EndFunc)


def GetCartoonLockTargets(oSkill, sid):
    dCartoon = oSkill.GetCartoonBySID(sid)
    if 'LockTarget' in dCartoon:
        return dCartoon['LockTarget']
    return []


def GetCartoonDict(oSkill, sid):
    dCartoon = oSkill.GetCartoonBySID(sid)
    if 'Dict' in dCartoon:
        return dCartoon['Dict']
    return { }


def GetChargeCartoonTime(oSkill, sid):
    dCartoon = oSkill.GetCartoonBySID(sid)
    if 'MaxFrame' in dCartoon and 'Time' in dCartoon:
        iMaxChargeTime = Frame2Time(dCartoon['MaxFrame'])
        iChargeTime = dCartoon['Time']
        if iChargeTime > iMaxChargeTime:
            iChargeTime = iMaxChargeTime
        return iChargeTime
    return 0


def GetDictionaryKeys(oSkill, dData):
    return list(dData.keys())


def GetDictionaryValue(oSkill, dData, iKey):
    return dData[iKey]


def GetSmashTimes(oSkill):
    if 'ExtraTimes' in oSkill.m_Custom:
        return oSkill.m_Cache['DamInterval'] + oSkill.m_Custom['ExtraTimes']
    return oSkill.m_Cache['DamInterval']


def CreatePhyModel(oSkill, sFlag, iModelType, iPhyType, iLayer, lstHalfExt, vOffset):
    if iPhyType not in (PAMOD_TYPE_DYNA,):
        return None
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    if iModelType == MODEL_TYPE_BOX:
        dParam = {
            'Shape': MODEL_TYPE_BOX,
            'HalfExt': (lstHalfExt[0], lstHalfExt[1], lstHalfExt[2]),
            'Center': vOffset }
    else:
        SendAlert('err', '技能%d 不存在模型形状 %d' % (oSkill.m_Base['pfid'], iModelType))
        return None
    oModel = cl_engphyobj.CreatePhyModel(oAttack, iPhyType, iLayer, dParam)
    if oModel:
        oAttack.Set(sFlag, oModel)


def RemovePhyModel(oSkill, sFlag):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oModel = oAttack.Query(sFlag)
    if not oModel:
        return None
    oModel.E_Unstall()
    oAttack.Delete(sFlag)


def SetPosAtPerformAttacked(oSkill, vPos):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oAttack.Set('PerformAttackedPos', vPos)


def RemoveAttackedPos(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oAttack.Delete('PerformAttackedPos')


def GetArgDataCache(skill, sKey, iDefault = 0):
    dCache = skill.m_Cache
    if 'ArgData' not in dCache:
        return iDefault
    dArgDataCache = dCache['ArgData']
    if sKey in dArgDataCache:
        return dArgDataCache[sKey]
    return iDefault


def GetGroundPos(oSkill, vPos):
    fGroundDis = oSkill.m_Game.Scene_GroundDistance(oSkill.m_Base['Scene'], (vPos[0], vPos[1] + 0.2, vPos[2]), 25, PXMASK_GROUNDBLK)
    return (vPos[0], vPos[1] + 0.2 - fGroundDis, vPos[2])


def GetSkillCrtBuff(oSkill):
    dCartoon = oSkill.GetCurCartoon()
    return oSkill.GetCartoonBuffList(dCartoon['ID'])


def CrtArgConversionPos(oSkill, vPos):
    return vPos


def AssignWarriorDie(oSkill, iWarrior):
    oWarrior = oSkill.m_Game.GetObject(iWarrior, PY_FLAG_DEAD)
    if not oWarrior:
        return None
    oReason = cl_object.reason.CStrReason('AssignDie', None, {
        'DamType': DAM_TYPE_PERFORM | DAM_USE_HP,
        'ActNum': oSkill.m_Base['ActNum'] })
    oWarrior.Set('RelifeInfo', { })
    oWarrior.HPDirectModify('HP', oSkill.m_Base['AID'], -(oWarrior.m_HP), oReason)


def Power(oSkill, a, b):
    return a ** b


def CheckVictimCreatedBySkill(oSkill, dCartoon, dArgs):
    if 'VID' in dArgs and 'SummonCreate' in oSkill.m_Collect and dArgs['VID'] in oSkill.m_Collect['SummonCreate']:
        return 1
    return 0


def GetFuncCheckVictimCreatedBySkill(oSkill):
    return CheckVictimCreatedBySkill


def ChoosePosByTargetFacingAndArgs(oSkill, iTarget, fMinRadius, fMaxRadius, iMinAngle, iMaxAngle, iCalNavRadius = 0):
    vBase = oSkill.m_Base['vStart']
    oGame = oSkill.m_Game
    oTarget = oGame.GetObject(iTarget)
    if not oTarget:
        return vBase
    iScene = oTarget.m_Scene
    vPos = oTarget.GetPos()
    vFace = oTarget.GetFacing()
    if iCalNavRadius:
        oAttack = oSkill.GetAttack()
        fAddRadius = 0
        if oAttack and oAttack.m_MoveCtrl:
            fAddRadius += oAttack.m_MoveCtrl.m_NavRadius
        if oTarget.m_MoveCtrl:
            fTargetRadius = oTarget.m_MoveCtrl.m_NavRadius
        else:
            (fTargetRadius, _) = cl_modeldefine.GetModelDefine(oTarget.m_Shape, 'NavMesh')
        fAddRadius += fTargetRadius
        fMinRadius += fAddRadius
        fMaxRadius += fAddRadius
    for _ in range(5):
        vTarget = oGame.Scene_RandomPointSectorInMesh(iScene, vPos, vFace, fMinRadius, fMaxRadius, iMinAngle, iMaxAngle)
        if vTarget:
            return vTarget
    
    return vBase


def ChooseHateCrowdPos(oSkill, fRadius, iMinCnt):
    oAttack = oSkill.GetAttack()
    oAgent = oAttack.m_Agent
    dHate = oAgent.GetData('HateData', { })
    oGame = oAgent.m_Game
    dQArgs = {
        'Mask': PXMASK_MONSTER,
        'BlockMask': 0 }
    iMaxCnt = 0
    tChooseTarget = []
    for iMonster in dHate:
        oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
        if oMonster:
            lstTarget = oGame.Scene_GetSphereObjects(oAttack.m_Scene, oMonster.GetPos(), fRadius, PXMASK_MONSTER, dQArgs)
            iLen = len(lstTarget)
            if iLen >= iMinCnt:
                tChooseTarget = lstTarget
                break
            if iLen > iMaxCnt:
                iMaxCnt = iLen
                tChooseTarget = lstTarget
    
    if not tChooseTarget:
        return oSkill.m_Base['vEnd']
    vMonster = [
        0,
        0,
        0]
    iCnt = 0
    for iMonster in tChooseTarget:
        oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
        if oMonster:
            vMonster = cl_math.Vec3Add(vMonster, oMonster.GetPos())
            iCnt += 1
    
    if iCnt <= 0:
        return oSkill.m_Base['vEnd']
    vPos = cl_math.Vec3MulF(vMonster, 1 / iCnt)
    (bRet, vPos) = oGame.Scene_GetAccessibleDestPos(oAttack.m_Scene, oAttack.GetPos(), vPos)
    if not bRet:
        return oSkill.m_Base['vEnd']
    return vPos


def CheckPosIsNavMeshArrive(oSkill, vStartPos, vDir, iDis, iCheckPlane, iOffset):
    if not vStartPos or iDis < iOffset:
        return 0
    oGame = oSkill.m_Game
    CalDistanceFunc = cl_math.CalDistance3D
    if iCheckPlane:
        vDir = (vDir[0], 0, vDir[2])
        CalDistanceFunc = cl_math.CalDistance
    vCheckEndPos = cl_math.Vec3HorizonDisplaceDir(vStartPos, vDir, iDis)
    vPos = oGame.Scene_NavMeshRayCast(oSkill.m_Base['Scene'], vStartPos, vCheckEndPos)
    if vStartPos != vPos:
        iDis -= iOffset
        iRealDis = CalDistanceFunc(vStartPos, vPos)
        if iRealDis >= iDis:
            return 1
    return 0


def GetTargetNearestSpace(oSkill, iTarget, bCalTargetRadius, fExtraDis):
    oGame = oSkill.m_Game
    oTarget = oGame.GetObject(iTarget)
    vBase = oSkill.m_Base['vStart']
    if not oTarget:
        return vBase
    oAttack = oSkill.GetAttack()
    vAttack = oAttack.GetPos()
    vTarget = oTarget.GetPos()
    if bCalTargetRadius and not cl_math.IsEqual(vTarget, vAttack):
        (fEnemyRadius, _) = cl_modeldefine.GetModelDefine(oTarget.m_Shape, 'NavMesh')
        fEnemyRadius += fExtraDis
        vTarget = cl_math.Vec3DisplacePos(vTarget, vAttack, fEnemyRadius)
    (bRet, vPos) = oGame.Scene_GetAccessibleDestPos(oAttack.m_Scene, vAttack, vTarget)
    if not bRet:
        return vBase
    return vPos


def Clamp(oSkill, iCurrent, iMin, iMax):
    if iCurrent < iMin:
        return iMin
    if iCurrent > iMax:
        return iMax
    return iCurrent


def SetSkillScanInfo(oSkill, dInfo):
    oSkill.m_Collect['ScanInfo'] = dInfo
    oSkill.m_Collect['ScanNum'] = len(dInfo)


def SendUseCareerPFMsg(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_USE_CAREERPF, oAttack, {
        'Skill': oSkill })


def SendUseThrowPFMsg(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_USE_THROWPF, oAttack, {
        'Skill': oSkill })


def SendParasiticTriggerMsg(oSkill, iParasiticCount):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    dMsgInfo = {
        'VID': oSkill.m_Base['VID'],
        'ParasiticCount': iParasiticCount }
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_PARASITIC, oAttack, dMsgInfo, iSub = TRIGGER_PARASITIC)


def SendOwnerUseCareerPFMsg(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oOwner = oAttack.GetOwner()
    if not oOwner:
        return None
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_USE_CAREERPF, oOwner, {
        'Skill': oSkill })


def SendOwnerUseThrowPFMsg(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oOwner = oAttack.GetOwner()
    if not oOwner:
        return None
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_USE_THROWPF, oOwner, {
        'Skill': oSkill })


def SendPetPerformTriggerMsg(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_TRIGGERPETPERFORM, oAttack, {
        'Skill': oSkill })


def SendTriggerBurstMsg(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_TRIGGERBURST, oAttack, {
        'Skill': oSkill })


def SendInteraceHitTargetMsg(oSkill, iTriggerID, dInfo = None):
    if not iTriggerID:
        return None
    oGame = oSkill.m_Game
    oTrigger = oGame.GetObject(iTriggerID, PY_FLAG_DEAD)
    if not oTrigger:
        return None
    if dInfo is None:
        dInfo = { }
    iCurVID = oSkill.m_Update['CurVID'] if 'CurVID' in oSkill.m_Update else 0
    dInfo.update({
        'Skill': oSkill,
        'CurVID': iCurVID })
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_INTERACT_PERFORM_HIT_TARGET, oTrigger, dInfo)


def SetExtraModelDistance(oSkill, fDistance):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oAttack.SetExtraModelDistance(fDistance)


def SetForceNoDestFlag(oSkill, bForceNoDest):
    
    def EndFunc(oSkill):
        oAttack = oSkill.GetAttack()
        if oAttack:
            oAttack.Delete('ForceNoDest')

    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    if bForceNoDest:
        oAttack.Set('ForceNoDest', 1)
        oSkill.AddEndFunc(EndFunc)
    else:
        oAttack.Delete('ForceNoDest')


def SetModelHeight(oSkill, fHeight, bWithPF):
    
    def EndFunc(oSkill):
        oAttack = oSkill.GetAttack()
        if oAttack and oAttack.m_ModelData:
            oAttack.m_ModelHeight = oAttack.m_ModelData.GetModelHeight()

    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oAttack.m_ModelHeight = fHeight
    if bWithPF:
        oSkill.AddEndFunc(EndFunc)


def GetCurCartoonEntitySID(oSkill):
    dCartoon = oSkill.GetCurCartoon()
    if not dCartoon:
        return 0
    if 'SummonSID' not in dCartoon:
        return 0
    return dCartoon['SummonSID']


def GetPosIncisedCircle(oSkill, iNum, iMinRadius, iMaxRadius):
    oGame = oSkill.m_Game
    oAttack = oSkill.GetAttack()
    if not oAttack:
        vPos = oSkill.m_Base['vStart']
        fFacingx = 0
        fFacingz = 0
    else:
        vPos = oAttack.GetPos()
        (fFacingx, _, fFacingz) = oAttack.GetFacing()
    (fPosx, fPosy, fPosz) = vPos
    lstRes = []
    iAngleLimit = 360 // iNum
    for iCount in range(iNum):
        iDis = oGame.Random((iMaxRadius - iMinRadius) + 1) + iMinRadius
        iAngle = iCount * iAngleLimit + oGame.Random(iAngleLimit)
        (fResx, fResz) = cl_math.Vec2DestPosDir((fPosx, fPosz), (fFacingx, fFacingz), iDis, iAngle)
        vRes = (fResx, fPosy, fResz)
        lstRes.append(vRes)
    
    return lstRes


def GetTransDamFactor(oSkill):
    if 'TransDamFactor' in oSkill.m_Custom:
        return oSkill.m_Custom['TransDamFactor']
    return { }


def ApplyStateTransDamFactor(oSkill, iStateSID):
    oAttack = oSkill.GetAttack()
    oState = oAttack.m_State.GetItemBySID(iStateSID)
    if not oState:
        return None
    dTransFactor = oState.GetArgValue('TransDamFactor')
    if not dTransFactor:
        return None
    dFactor = oSkill.m_Collect['DamFactor'] if 'DamFactor' in oSkill.m_Collect else { }
    dFactor.update(dTransFactor)
    oSkill.m_Collect['DamFactor'] = dFactor
    dSelfTransFactor = oSkill.m_Custom['TransDamFactor'] if 'TransDamFactor' in oSkill.m_Custom else { }
    dSelfTransFactor.update(dTransFactor)
    oSkill.m_Custom['TransDamFactor'] = dSelfTransFactor


def ApplyPFTransDamFactor(oSkill):
    iParentActNum = cl_perform.skillcache.GetSkillCacheByIndex(oSkill, SKILLCACHE_PARENTACTNUM)
    if not iParentActNum:
        return None
    oAttack = oSkill.GetAttack()
    sKey = 'PFTransFactor'
    dPerformInfo = oAttack.Query(sKey, { })
    if iParentActNum not in dPerformInfo:
        return None
    dTransFactor = dPerformInfo[iParentActNum]
    dFactor = oSkill.m_Collect['DamFactor'] if 'DamFactor' in oSkill.m_Collect else { }
    dFactor.update(dTransFactor)
    oSkill.m_Collect['DamFactor'] = dFactor
    dSelfTransFactor = oSkill.m_Custom['TransDamFactor'] if 'TransDamFactor' in oSkill.m_Custom else { }
    dSelfTransFactor.update(dTransFactor)
    oSkill.m_Custom['TransDamFactor'] = dSelfTransFactor


def CachePFTransDamFactor(oSkill, iTime):
    
    def ClearFunc(oAttack, iActNum):
        dPerformInfo = oAttack.Query(sKey, { })
        if iActNum in dPerformInfo:
            dPerformInfo.pop(iActNum)
            oAttack.Set(sKey, dPerformInfo)

    dTransFactor = oSkill.m_Custom['TransDamFactor'] if 'TransDamFactor' in oSkill.m_Custom else { }
    if not dTransFactor:
        return None
    oAttack = oSkill.GetAttack()
    iActNum = oSkill.m_Base['ActNum']
    sKey = 'PFTransFactor'
    dPerformInfo = oAttack.Query(sKey, { })
    dPerformInfo[iActNum] = dTransFactor
    oAttack.Set(sKey, dPerformInfo)
    oAttack.Call_Out(Functor(ClearFunc, oAttack, iActNum), Time2Frame(iTime), 'ClearTransDamFactor')


def ApplyCountTransDamFactor(oSkill, sKey):
    oAttack = oSkill.GetAttack()
    dCountTransFactor = oAttack.Query('CountTransFactor', { })
    if sKey not in dCountTransFactor:
        return None
    lstTransFactor = dCountTransFactor[sKey]
    if not lstTransFactor:
        return None
    (dTransFactor, iCount) = lstTransFactor[0]
    iCount -= 1
    if iCount <= 0:
        lstTransFactor.pop(0)
    else:
        lstTransFactor[0] = (dTransFactor, iCount)
    dFactor = oSkill.m_Collect['DamFactor'] if 'DamFactor' in oSkill.m_Collect else { }
    dFactor.update(dTransFactor)
    oSkill.m_Collect['DamFactor'] = dFactor
    dSelfTransFactor = oSkill.m_Custom['TransDamFactor'] if 'TransDamFactor' in oSkill.m_Custom else { }
    dSelfTransFactor.update(dTransFactor)
    oSkill.m_Custom['TransDamFactor'] = dSelfTransFactor


def CacheCountTransDamFactor(oSkill, sKey, iCount):
    dTransFactor = oSkill.m_Custom['TransDamFactor'] if 'TransDamFactor' in oSkill.m_Custom else { }
    if not dTransFactor:
        return None
    oAttack = oSkill.GetAttack()
    dCountTransFactor = oAttack.Query('CountTransFactor', { })
    if sKey not in dCountTransFactor:
        dCountTransFactor[sKey] = [
            (dTransFactor, iCount)]
    else:
        dCountTransFactor[sKey].append((dTransFactor, iCount))
    oAttack.Set('CountTransFactor', dCountTransFactor)


def GetAttackerWeaponPerformAttr(oSkill, iPerform, sAttr):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return 0
    iItem = oSkill.m_Base['Weapon']
    oPerform = oAttack.GetPerform(iPerform, iItem)
    if oPerform and sAttr in oPerform.m_Attr:
        return oPerform.CalAttr(sAttr)
    return 0


def CheckHookPullBack(oSkill):
    oGame = oSkill.m_Game
    iTarget = oSkill.m_Update['CurVID']
    oVictim = oGame.GetObject(iTarget, PY_FLAG_DEAD)
    if not oVictim:
        return False
    if not oVictim.m_FightType & WARRIOR_MONSTER:
        return False
    if not oVictim.m_MoveCtrl:
        return False
    return True


def GetPointOnAimPlane(oSkill, vStartPos, vCenterPos, vEndPos):
    return vEndPos


def CreateMonsterHinder(oSkill, iBuildSID, vPos, lstNumPos, dParam):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oGame = oSkill.m_Game
    clsSummonData = oGame.m_WarData.GetBuildData(iBuildSID)
    tModelData = cl_modeldefine.GetModelDefine(clsSummonData.m_Shape, 'Box')
    iRotate = oGame.Random(360)
    dAddData = {
        'Angle': [
            0,
            iRotate,
            0],
        'Center': [
            0,
            tModelData[1] * 0.5,
            0],
        'Origin': (vPos[0], vPos[1], vPos[2]),
        'GlobalArea': 0,
        'SID': iBuildSID,
        'Scale': [
            1,
            1,
            1],
        'Shape': MODEL_TYPE_BOX,
        'Size': tModelData,
        'Owner': oAttack.m_ID }
    iScene = oSkill.m_Base['Scene']
    oBuild = oGame.m_ResMgr.CreateBuild(iScene, iBuildSID, dAddData)
    oAttack.m_FollowDieObjs[oBuild.m_ID] = 1
    oBuild.CreateSonHinderByNum(lstNumPos, vPos, iRotate)
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return None
    dMonsterHinder = oScene.m_SceneData.SetDefault('MonsterHinder', { })
    dMonsterHinder[oBuild.m_ID] = oAttack.m_ID


def GetMonsterHinderNum(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return 0
    oGame = oSkill.m_Game
    iScene = oSkill.m_Base['Scene']
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return 0
    dMonsterHinder = oScene.m_SceneData.Query('MonsterHinder', { })
    return len(dMonsterHinder)


def CheckClientCtrl(oSkill):
    return oSkill.m_CheckType == CRT_CHECK_CLIENT


def GetRangeTargetByPointTarget(oSkill, iTarget, fRange, bIgnoreBlock, iNum, bSort = False, bChooseHero = False, bFillinList = True):
    oGame = oSkill.m_Game
    oTarget = oGame.GetObject(iTarget)
    if not oTarget:
        return []
    vCenter = oTarget.GetPos()
    lstArgs = [
        vCenter,
        fRange]
    iScene = oSkill.m_Base['Scene']
    if bChooseHero:
        dMask = {
            'Mask': PXMASK_PLAYER }
    else:
        dMask = {
            'Mask': PXMASK_MONSTER }
    if bIgnoreBlock:
        dMask['BlockMask'] = 0
    setVLST = cl_math.GetAttackTargetList(oGame, iScene, ATT_SHAPE_SPHERE, lstArgs, dMask)
    if not setVLST:
        return []
    lstVLST = list(setVLST)
    if bSort:
        dVLST = oGame.Scene_GetTargetDisMap(iTarget, lstVLST)
        lstSort = sorted(dVLST.items(), key = (lambda x: x[1]))
        lstVLST = [ x[0] for x in lstSort ]
    if iNum:
        iLen = len(lstVLST)
        if iNum <= iLen:
            return lstVLST[:iNum]
        if bFillinList:
            lstTarget = lstVLST[:]
            for _ in range(iNum - iLen):
                lstTarget.append(lstVLST[oGame.Random(iLen)])
            
            return lstTarget
    return lstVLST


def RefreshStepPerformNextPos(oSkill, vCurPos, vLastPos, fLimitDis, fDisOffset, iPosLiveTime = 0):
    if not vCurPos or not vLastPos or not fLimitDis or vCurPos == vLastPos:
        return (0, 0, 0)
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return (0, 0, 0)
    vRecordLastPos = oAttack.Query('RefreshStepLastPos', 0)
    if vRecordLastPos:
        vLastPos = vRecordLastPos
        oAttack.Delete('RefreshStepLastPos')
    if cl_math.CheckDistance(vLastPos, vCurPos, fLimitDis):
        return (0, 0, 0)
    oWarMgr = oAttack.m_Game.m_WarMgr
    oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
    oScene = oAttack.m_Game.m_SceneMgr.GetScene(oAttack.m_Scene)
    oLevelNode = oLevelCtrl.GetLevelNode(oScene.m_Level)
    iPerform = oSkill.m_Base['pfid'] if 'pfid' in oSkill.m_Base else 0
    if not oLevelNode:
        SendAlert('err', '技能%s 获取关卡节点失败 %s' % (iPerform, oScene.m_Level))
        return (0, 0, 0)
    sKey = 'RefreshStepPerformPos-%s-%s' % (oAttack.m_ID, iPerform)
    dPerformPos = oLevelNode.m_CustomData.get(sKey, { })
    vPerformPos = cl_math.Vec3MulF(cl_math.Vec3Add(vCurPos, vLastPos), 0.5)
    iGameFrame = oAttack.m_Game.GetFrameNum()
    dTempPerformPos = CopyDict(dPerformPos)
    fLimitDis -= fDisOffset
    for iFrame, vLastPerformPos in dPerformPos.items():
        if iFrame <= iGameFrame:
            dTempPerformPos.pop(iFrame)
            continue
        if cl_math.CheckDistance(vLastPerformPos, vPerformPos, fLimitDis):
            oAttack.Set('RefreshStepLastPos', vLastPerformPos)
            oLevelNode.m_CustomData[sKey] = dTempPerformPos
            return (0, 0, 0)
    
    iGameFrame += Time2Frame(iPosLiveTime)
    dTempPerformPos[iGameFrame] = vPerformPos
    oLevelNode.m_CustomData[sKey] = dTempPerformPos
    return vPerformPos


def UseExtraThrowPerform(oSkill, dCustomData, iDelay, iVictim):
    return None


def UsePassiveThrowPerform(oAttack, iVictim, iPerform, iActNum, dData):
    if oAttack.IsDead():
        return None
    if iVictim:
        dData['VID'] = iVictim
    pfobj = oAttack.GetPerform(iPerform)
    if not pfobj:
        return None
    if EXTRA_THROW_PERFORM[oAttack.m_SID][1]:
        dArgs = {
            'ThrowMsg': 1,
            'Target': iVictim,
            'FirstActNum': iActNum }
        pfobj.AddCanUseCount()
        cl_snetwar.GS2CNotifyStartSkill(oAttack.m_Game, oAttack.m_PlayerID, iPerform, pfobj.m_ID, 0, dArgs)
        return None
    cl_war.UsePerform(oAttack, pfobj, dData)


def GetTargetPointStateNum(oSkill, iTarget, lstState):
    oTarget = oSkill.m_Game.GetObject(iTarget)
    iNum = 0
    if not oTarget:
        return iNum
    for iState in lstState:
        if oTarget.m_State.GetItemBySID(iState):
            iNum += 1
    
    return iNum


def CrtArgHitStaticPos(oSkill):
    pass


def CrtArgTpsTransform(oSkill, sName):
    pass


def GetOneListFromRandonList(oSkill, lstList):
    if not lstList:
        return []
    iLen = len(lstList)
    oGame = oSkill.m_Game
    return lstList[oGame.Random(iLen)]


def CalMoveControlDir(oSkill, hasZero = False):
    if 'Dir' in oSkill.m_Custom:
        return cl_math.Vec3Normalize(oSkill.m_Custom['Dir'])
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return (0, 0, 0)
    if not oAttack.IsStop() and oAttack.m_MoveCtrl:
        vPathDire = oAttack.m_MoveCtrl.E_GetPathDir()
        return cl_math.Vec3Normalize(vPathDire)
    return oAttack.GetFacing()


def GetWeaponFlagTargetByKey(oSkill, sKey):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return []
    iItem = oSkill.m_Base['Weapon']
    oWeapon = oAttack.m_WieldCon.GetItemByID(iItem)
    if not oWeapon:
        return []
    dRemainTarget = { }
    iScene = oSkill.m_Base['Scene']
    dFlagTarget = oWeapon.QueryTmp(sKey, { })
    oGame = oSkill.m_Game
    lstFlagTarget = list(dFlagTarget)
    for iTarget in dFlagTarget:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            lstFlagTarget.remove(iTarget)
            continue
        if oTarget.m_Scene != iScene:
            lstFlagTarget.remove(iTarget)
            dRemainTarget[iTarget] = 1
    
    oSkill.m_Collect['RemainTarget'] = dRemainTarget
    return lstFlagTarget


def ClearWeaponFlagTarget(oSkill, sKey):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    iItem = oSkill.m_Base['Weapon']
    oWeapon = oAttack.m_WieldCon.GetItemByID(iItem)
    if not oWeapon:
        return None
    dRemainTarget = oSkill.m_Collect['RemainTarget'] if 'RemainTarget' in oSkill.m_Collect else { }
    if dRemainTarget:
        oWeapon.SetTmp(sKey, dRemainTarget)
    else:
        oWeapon.RemoveTmp(sKey)


def RemoveTargetSourceWeaponState(oSkill, iTarget, iStateSID):
    oGame = oSkill.m_Game
    oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
    if not oTarget:
        return None
    iItem = oSkill.m_Base['Weapon']
    lstStateObj = oTarget.m_State.GetItems(iStateSID)
    oStateCon = oTarget.m_State
    for oState in lstStateObj:
        oReason = oState.m_Reason
        iStateItem = oReason.Query('Item', 0)
        if iStateItem and iStateItem == iItem:
            oStateCon.RemoveItem(oState.m_ID)
    


def TrapThumpVictim(oSkill, iVictim):
    oVictim = oSkill.m_Game.GetObject(iVictim, PY_FLAG_DEAD)
    if not oVictim:
        return None
    oVictim.GetTrapThumped()


def GetAttackerFacing(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return (0, 0, 0)
    return oAttack.GetFacing()


def GetWeaponData(oSkill, sKey):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return 0
    iItem = oSkill.m_Base['Weapon']
    oWeapon = oAttack.m_WieldCon.GetItemByID(iItem)
    if not oWeapon:
        return 0
    return oWeapon.Query(sKey, 0)


def GetTornadoDashPos(oSkill, vCenter, fAngle, iExcludeFlag):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return oSkill.m_Base['vEnd']
    oGame = oSkill.m_Game
    iScene = oSkill.m_Base['Scene']
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return oSkill.m_Base['vEnd']
    vAttack = oAttack.GetPos()
    vCenterDir = cl_math.Vec3Minus(vCenter, vAttack)
    lstPos = []
    lstHero = []
    for iHero in oScene.GetHeros():
        oHero = oGame.GetObject(iHero, iExcludeFlag)
        if not oHero:
            continue
        lstHero.append(oHero)
        vTarget = oHero.GetPos()
        disp = cl_math.Vec3Minus(vTarget, vAttack)
        if cl_math.CheckVector2Angle(disp, vCenterDir, fAngle):
            continue
        lstPos.append(vTarget)
    
    if lstPos:
        iIndex = oSkill.m_Game.Random(len(lstPos))
        return lstPos[iIndex]
    if not lstHero:
        return oSkill.m_Base['vEnd']
    iIndex = oSkill.m_Game.Random(len(lstHero))
    oHero = lstHero[iIndex]
    vDir = cl_math.Vec3Minus(oHero.GetPos(), vAttack)
    fShiftAngle = fAngle if cl_math.VectorCross2D(vCenterDir, vDir) > 0 else -fAngle
    return cl_math.Vec3DestPosDir(vAttack, vCenterDir, 5, fShiftAngle)


def GetWatchPerformStart(oSkill):
    vPos = oSkill.m_Base['vStart']
    vStart = (vPos[0], vPos[1] + oSkill.m_Base['ModelHeight'] * 0.85, vPos[2])
    return vStart


def GetValueFromDict(oSkill, iKey, dArgs, iDefault):
    if iKey in dArgs:
        return dArgs[iKey]
    return iDefault


def GetThunderWandThunderPos(oSkill, vPos, vDir, iNum, fStartAngle, fStartDis, fChangeAngle, fChangeDis):
    if iNum <= 0 or not vPos or not vDir:
        return []
    lstPos = []
    fDis = fStartDis
    fAngle = fStartAngle
    for _ in range(iNum):
        vThunderPos = cl_math.Vec3DestPosDirPlane(vPos, vDir, fDis, fAngle)
        (iRet, vThunderPos) = oSkill.m_Game.Scene_GetSpace(oSkill.m_Base['Scene'], vThunderPos)
        if iRet:
            lstPos.append(vThunderPos)
        fDis += fChangeDis
        fAngle += fChangeAngle
    
    return lstPos


def HatchVictimGardenerSeed(oSkill):
    iAttack = oSkill.m_Base['AID']
    oAttack = oSkill.m_Game.GetObject(iAttack)
    if not oAttack or oAttack.m_SID != GARDENER_HERO:
        return None
    if 'CurVID' in oSkill.m_Update:
        iTarget = oSkill.m_Update['CurVID']
    else:
        iTarget = oSkill.m_Base['VID']
    oTarget = oSkill.m_Game.GetObject(iTarget)
    if not oTarget:
        return None
    if oTarget.m_FightType & WARRIOR_SUMMON_SEED != WARRIOR_SUMMON_SEED:
        return None
    oPlant = oAttack.m_GardenerCon.HatchSeed(iTarget, oSkill.m_Base['PFKey'])
    if not oPlant:
        return None
    CollectPlantInfo(oSkill, oPlant.m_ID, PLANT_PHASE_NORMAL)


def CreatePlantByPos(oSkill, vPos, fShiftDis, vShiftDir, iCheckPos = 0, iPlantPhase = PLANT_PHASE_NORMAL, iUseState = 0):
    oAttack = oSkill.GetAttack()
    if not oAttack or oAttack.m_SID != GARDENER_HERO:
        return None
    if fShiftDis:
        vTarget = cl_math.Vec3DisplaceDir(vPos, vShiftDir, fShiftDis)
        vTarget = oSkill.m_Game.Scene_NavMeshRayCast(oAttack.m_Scene, vPos, vTarget)
    else:
        vTarget = vPos
    oPlant = oAttack.m_GardenerCon.CreatePlant(vTarget, iPlantPhase, iCheckPos, oSkill.m_Base['PFKey'])
    if not oPlant:
        return None
    if iUseState and 'BuffInfo' in oSkill.m_Custom:
        oPlant.AddTransferState(oSkill.m_Custom['BuffInfo'])
    CollectPlantInfo(oSkill, oPlant.m_ID, iPlantPhase)


def CollectPlantInfo(oSkill, iPlant, iPlantPhase):
    dCustom = oSkill.m_Custom
    if 'HitPlant' not in dCustom:
        dCustom['HitPlant'] = { }
    if 'CreatePlant' not in dCustom:
        dCustom['CreatePlant'] = { }
    dCustom['HitPlant'][iPlant] = iPlantPhase
    dCustom['CreatePlant'][iPlant] = iPlantPhase


def CreateSeedByPos(oSkill, vTargetPos, iCheckPos, iNum):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oAttack.m_GardenerCon.CreateSeed(vTargetPos, oSkill.m_Base['PFKey'], iCheckPos, iNum)


def RemoveNearesSeedByPos(oSkill, vPos, iRecord):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    if oAttack.m_SID == GARDENER_HERO:
        oGardenerCon = oAttack.m_GardenerCon
    elif oAttack.m_FightType & WARRIOR_PLANT == WARRIOR_PLANT:
        oOwner = oAttack.GetOwner()
        if not oOwner or oOwner.m_SID != GARDENER_HERO:
            return None
        oGardenerCon = oOwner.m_GardenerCon
    else:
        return None
    oSeed = oGardenerCon.GetNearestSeed(vPos)
    if not oSeed:
        return None
    vPos = oAttack.GetPos()
    oGardenerCon.RemoveSeed(oSeed.m_ID, oSkill.m_Base['PFKey'])
    if iRecord:
        oSkill.m_Custom['RemovebSeedPos'] = vPos


def AddParasiticState(oSkill, iTarget, iAddCount = 0):
    oAttack = oSkill.GetAttack()
    if not oAttack or oAttack.m_SID != GARDENER_HERO:
        return None
    oAttack.m_GardenerCon.AddParasiticState(iTarget, oSkill.m_Base['PFKey'], iAddCount)


def ParasiticDamage(oSkill, iTarget, iMul, dTransDamFactor, iAddCount = 0):
    oAttack = oSkill.GetAttack()
    if not oAttack or oAttack.m_SID != GARDENER_HERO:
        return None
    oAttack.m_GardenerCon.CauseParasiticDam(iTarget, iMul, iAddCount, dTransDamFactor = dTransDamFactor)


def CreateSummonBarrier(oSkill, vCenter, vScale, iHPMax):
    oAttack = oSkill.GetAttack()
    if not oAttack or oAttack.m_SID != GARDENER_HERO:
        return None
    oAttack.m_GardenerCon.CreateSummonBarrier(vCenter, vScale, iHPMax)


def UpdateFieldSeedInfo(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack or oAttack.m_SID != GARDENER_HERO:
        return None
    if 'CurVID' in oSkill.m_Update:
        iTarget = oSkill.m_Update['CurVID']
    else:
        iTarget = oSkill.m_Base['VID']
    oTarget = oSkill.m_Game.GetObject(iTarget)
    if not oTarget:
        return None
    oAttack.m_GardenerCon.UpdateFieldSeedInfo(oTarget.m_ID)


def ClearFieldSeedInfo(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack or oAttack.m_SID != GARDENER_HERO:
        return None
    oAttack.m_GardenerCon.ClearFieldSeedInfo()


def GetThrowBoomRadiusByShape(oSkill, iShape, fDefault):
    fRadius = GetGardenerAimThrowRadius(iShape)
    if fRadius:
        return fRadius
    return fDefault


def SetThrowElementTypeByShape(oSkill, iShape):
    iElement = GetGardenerAimThrowElementType(iShape)
    if iElement:
        oSkill.m_Cache['ElementType'] = iElement


def GetThrowCreateMonsterSID(oSkill, iShape):
    oGame = oSkill.m_Game
    return GetGardenerAimThrowCreateMonsterInfo(iShape, oGame.m_WarMgr.m_SID)


def CreateGardenerArea(oSkill, iShape, vStart, vScale):
    oAttack = oSkill.GetAttack()
    if not oAttack or oAttack.m_SID != GARDENER_HERO:
        return None
    oAttack.m_GardenerCon.CreateArea(iShape, vStart, vScale)


def GetWarriorLockEnemy(oSkill, iWarrior):
    oTarget = oSkill.m_Game.GetObject(iWarrior)
    if not oTarget:
        return 0
    if not oTarget.m_Agent:
        return 0
    oLockEnemy = oTarget.m_Agent.GetLockEnemy()
    if not oLockEnemy:
        return 0
    return oLockEnemy.m_ID


def AttackerAddPerformCanUseCount(oSkill, iPerform, iCount):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oPerform = oAttack.GetPerform(iPerform)
    if not oPerform:
        return None
    oPerform.AddCanUseCount(iCount)


def GetAttackerCustomData(oSkill, sAttr, iDefault = 0):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return iDefault
    return oAttack.Query(sAttr, iDefault)


def GetVictimCustomData(oSkill, sAttr, iDefault = 0):
    if 'CurVID' not in oSkill.m_Update:
        return iDefault
    iCurVictim = oSkill.m_Update['CurVID']
    oGame = oSkill.m_Game
    oVictim = oGame.GetObject(iCurVictim)
    if not oVictim:
        return iDefault
    return oVictim.Query(sAttr, iDefault)


def CheckHasPerfrom(oSkill, iPerform):
    oAttack = oSkill.GetAttack()
    oPerformCon = oAttack.m_Perform
    return iPerform in oPerformCon.m_Perform


def GetLegalAOWUThrowTriggerNum(oSkill, iTriggerTime):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return iTriggerTime
    iPerform = oSkill.m_Base['pfid']
    oPerform = oAttack.GetPerform(iPerform)
    if not oPerform:
        return iTriggerTime
    oTriggerTimesAttr = oPerform.GetAttr('TriggerTimes')
    if not oTriggerTimesAttr:
        return iTriggerTime
    iBullet = oPerform.CalAttr('BulletSID')
    iThorwMax = oAttack.m_BulletCon.GetMaxBullet(iBullet)
    tLimit = oTriggerTimesAttr.m_AttrLimit
    iServerTriggerTime = oPerform.CalAttr('TriggerTimes')
    if not iTriggerTime - iServerTriggerTime >= iThorwMax:
        if tLimit or tLimit[0] >= iTriggerTime or tLimit[1] < iTriggerTime:
            OtherLog.Debug('%s %s IllegalThrowTriggerNum %s %s %s' % (oSkill.m_Game.m_ID, oAttack.m_PlayerID, iTriggerTime, iServerTriggerTime, iThorwMax))
            return iServerTriggerTime
    return iTriggerTime


def GetSkillItemAttrBase(oSkill, sAttr):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return 0
    iItem = oSkill.m_Base['Weapon']
    oWeapon = oAttack.m_WieldCon.GetItemByID(iItem)
    if not oWeapon:
        return 0
    oAttr = oWeapon.GetItemAttr(sAttr)
    if not oAttr:
        return 0
    return oAttr.m_BaseValue


def CheckHasBullet(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return 0
    if 'ItemID' not in oSkill.m_Cache:
        return 0
    iWeaponID = oSkill.m_Cache['ItemID']
    oWeapon = oAttack.m_WieldCon.GetItemByID(iWeaponID)
    if not oWeapon:
        return 0
    oBulletCom = oWeapon.GetComponent('Bullet')
    if not oBulletCom:
        return 0
    iNowBullet = oBulletCom.Bullet()
    if iNowBullet <= 0:
        return 0
    return 1


def GetExtraChargeTime(oSkill, iSID):
    dCartoon = oSkill.GetCartoonBySID(iSID)
    if 'ExcessiveStartFrame' in dCartoon and 'ExcessiveOverFrame' in dCartoon:
        return Frame2Time(dCartoon['ExcessiveOverFrame'] - dCartoon['ExcessiveStartFrame'])
    return 0


def AttackAddWarGold(oSkill, iWarCash):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    if not oAttack or not (oAttack.m_FightType & WARRIOR_HERO):
        return None
    oAttack.AddCash(iWarCash, oSkill.m_Base['pfid'])


def CostPointSkillPFBullet(oSkill, iPerform, iCost):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oPerform = oAttack.GetPerform(iPerform)
    if not oPerform:
        return None
    oPerform.CostPFBullet(iCost)


def GetDiceAttackTimes(oSkill, iDice):
    oAttack = oSkill.GetAttack()
    if oAttack:
        oDiceCon = oAttack.m_DiceCon
        oDice = oDiceCon.GetDiceByID(iDice)
        if oDice:
            return oDice.GetDiceAttackTimes()
    return 0


def GetDiceAbilityQuality(oSkill, iDice):
    oAttack = oSkill.GetAttack()
    if oAttack:
        oDiceCon = oAttack.m_DiceCon
        oDice = oDiceCon.GetDiceByID(iDice)
        if oDice:
            return oDice.GetDiceAbilityQuality()
    return 0


def LionAddLockStateToTarget(oSkill, iTarget, iStateTime, iEnhance, dArgs):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    dRSInfo = {
        'ActNum': oSkill.m_Base['ActNum'] }
    TargetAddLionLockState(oAttack, iTarget, iStateTime, iEnhance, 'pf-%d' % oSkill.m_Base['pfid'], dArgs, dRSInfo)


def LionThrowPfSearchEnemy(oSkill, fRadius, vCenterPos, iNum, iCheckCanSee, iCheckFly, iCheckLockStateFromSelf, dExcludeEnemy, iIgnWudi = 0):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    return LionLockStateSearchEnemy(oAttack, fRadius, vCenterPos, iNum, iCheckCanSee, iCheckFly, iCheckLockStateFromSelf, dExcludeEnemy, iIgnWudi)


def GetScaleByOriginSize(fOriginR, fTargetR):
    if not fOriginR:
        return (1, 1, 1)
    fMul = fTargetR / fOriginR
    vScale = (fMul, fMul, fMul)
    return vScale


def GetSkillBaseAttr(oSkill, sAttr):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return 0
    iPerform = oSkill.m_Base['pfid']
    oPerform = oAttack.GetPerform(iPerform)
    if not oPerform:
        return 0
    oAttr = oPerform.GetAttr(sAttr)
    if not oAttr:
        return 0
    return oAttr.GetBaseAttr()


def GetSkillRunTimes(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return 0
    iPerform = oSkill.m_Base['pfid']
    oPerform = oAttack.GetPerform(iPerform)
    if not oPerform:
        return 0
    return oPerform.GetArgValue('SkillCount')


def SetWeaponDamageMergeTimes(oSkill, iTimes):
    dCurCartoon = oSkill.GetCurCartoon()
    if dCurCartoon:
        dCurCartoon['CopyTimes'] = iTimes


def GetProbabilityThroughTimes(oSkill, iProbability, iTimes):
    iCount = 0
    oGame = oSkill.m_Game
    for _ in range(iTimes):
        if oGame.Random(100) < iProbability:
            iCount += 1
    
    return iCount


def GetTargetShape(oSkill, iTarget):
    oGame = oSkill.m_Game
    oTarget = oGame.GetObject(iTarget)
    if not oTarget:
        return 0
    return oTarget.m_Shape


def SkillMarkTarget(oSkill, sMark, iTarget, iClearWhenEnd):
    
    def ClearSkillMarkTarget(oSkill):
        oGame = oSkill.m_Game
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            return None
        lstMarkWarrior = oTarget.Query(sMark, [])
        if iAttack in lstMarkWarrior:
            lstMarkWarrior.remove(iAttack)

    oGame = oSkill.m_Game
    oTarget = oGame.GetObject(iTarget)
    if not oTarget:
        return None
    lstMarkWarrior = oTarget.SetDefault(sMark, [])
    iAttack = oSkill.m_Base['AID']
    if iAttack not in lstMarkWarrior:
        lstMarkWarrior.append(iAttack)
    if iClearWhenEnd:
        oSkill.AddEndFunc(ClearSkillMarkTarget)


def SetSceneDataInt(oSkill, sKey, iVal):
    iScene = oSkill.m_Base['Scene']
    pfid = oSkill.m_Base['pfid']
    if not isinstance(iVal, int):
        SkillLog.Error(f'''iScene = {iScene}, pfid = {pfid} sKey = {sKey} iVal = {iVal} 设置场景数据有误''')
    oGame = oSkill.m_Game
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    oScene.m_SceneData.Set(sKey, iVal)


def GetSceneDataInt(oSkill, sKey, iDefault):
    oGame = oSkill.m_Game
    iScene = oSkill.m_Base['Scene']
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    iVal = oScene.m_SceneData.Query(sKey, iDefault)
    if not isinstance(iVal, int):
        pfid = oSkill.m_Base['pfid']
        SkillLog.Error(f'''iScene = {iScene}, pfid = {pfid} sKey = {sKey} iVal = {iVal} 获取场景数据有误''')
        return 0
    return iVal


def IntToFloat(oSkill, iVal):
    return iVal


def GetTargetRandomAccessiblePos(oSkill, iAttack, iTarget, vDir, iExtraRandomNum, fRadius1, fRadius2, iAngle1, iAngle2, vDefaultPos):
    oGame = oSkill.m_Game
    vStart = oSkill.m_Base['vStart']
    if cl_math.IsZero(vDefaultPos):
        vDefaultPos = vStart
    oTarget = oGame.GetObject(iTarget)
    oAttack = oGame.GetObject(iAttack)
    if not oTarget or not oAttack:
        return vDefaultPos
    vTargetPos = oTarget.GetPos()
    vAttack = oAttack.GetPos()
    iScene = oSkill.m_Base['Scene']
    for _ in range(1 + iExtraRandomNum):
        vPos = oGame.Scene_RandomPointSectorInMesh(iScene, vTargetPos, vDir, fRadius1, fRadius2, iAngle1, iAngle2)
        if not vPos:
            continue
        if oGame.Scene_IsDestPosAccessible(iScene, vAttack, vPos):
            return vPos
    
    return vDefaultPos


def GetOffsetPos(vStart, vEnd, fOffsetDis):
    vPos = cl_math.Vec3Minus(vEnd, vStart)
    vPos = cl_math.Vec3Normalize(vPos)
    return cl_math.Vec3Mad(vStart, vPos, fOffsetDis)


def GetEndHorizonDisplacePos(vStart, vEnd, fMoveDis):
    vDest = cl_math.Vec3HorizonDisplacePos(vStart, vEnd, fMoveDis)
    return (vDest[0], vEnd[1], vDest[2])


def Get3DisplacePos(vStart, vEnd, fMoveDis):
    return cl_math.Vec3DisplacePos(vStart, vEnd, fMoveDis)


def GetHoverObjPos(oSkill, iState, iVal):
    return GetMuzzlePos(oSkill)


def GetStateIdBySid(oSkill, iTarget, iState):
    oTarget = oSkill.m_Game.GetObject(iTarget, PY_FLAG_DEAD)
    if not oTarget:
        return 0
    oState = oTarget.m_State.GetItemBySID(iState)
    return oState.m_ID


def GetAttSpeedRatio(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return 0
    iItem = oSkill.m_Base['Weapon']
    oWeapon = oAttack.m_WieldCon.GetItemByID(iItem)
    if not oWeapon:
        return 0
    oAttr = oWeapon.GetItemAttr('AttSpeed')
    if not oAttr:
        return 0
    iBaseAttSpeed = oAttr.GetBaseAttr()
    if iBaseAttSpeed <= 0:
        return 0
    return oAttr.GetValue(oWeapon) / iBaseAttSpeed


def GetClosestLockTarget(oSkill, iNum, lstArgs):
    return []


def S8ThirdActiveAddState(oSkill, iTarget, iStateSID, dArgs):
    
    def StateEndFunc(oTarget, oLifeCycle):
        oGame = oTarget.m_Game
        oAttack = oGame.GetObject(iAttack)
        if not oAttack:
            return None
        oS8Con = oAttack.m_S8Con
        if not oS8Con:
            return None
        oItem = oS8Con.GetItemByID(iItem)
        if not oItem:
            return None
        oState = oLifeCycle.GetObject()
        if not oState:
            return None
        oItem.KeepStateEnd(oState)

    dSkillCache = oSkill.m_Cache
    if 'AddStateTime' not in dSkillCache or dSkillCache['AddStateTime'] <= 0:
        SendAlert('err', 'S8第三技能%s主动添加持续状态失败%s' % (oSkill, dSkillCache))
        return None
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oS8Con = oAttack.m_S8Con
    if not oS8Con:
        return None
    iItem = oSkill.m_Base['RS'].Query('Item', 0)
    oItem = oS8Con.GetItemByID(iItem)
    if not oItem:
        return None
    iAttack = oAttack.m_ID
    iStateTime = dSkillCache['AddStateTime']
    oState = TargetAddState(oSkill, iStateSID, iStateTime, 0, dArgs, iTarget)
    if oState:
        oItem.KeepStateStart(oState)
        oLifeCycle = oState.m_LifeCycle
        if oLifeCycle:
            oLifeCycle.AddUniqueDisableFunc('S8ThirdActiveAddState', StateEndFunc, iCover = 0)


def ChangeS8ThirdItemEnergy(oSkill, iChange):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oS8Con = oAttack.m_S8Con
    if not oS8Con:
        return None
    iItem = oSkill.m_Base['RS'].Query('Item', 0)
    oItem = oS8Con.GetItemByID(iItem)
    if not oItem:
        return None
    oItem.ChangeEnergy(iChange)


def GetS8ThirdItemEnergy(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return 0
    oS8Con = oAttack.m_S8Con
    if not oS8Con:
        return 0
    iItem = oSkill.m_Base['RS'].Query('Item', 0)
    oItem = oS8Con.GetItemByID(iItem)
    if not oItem:
        return 0
    return oItem.m_Energy


def GetSubductionPosList(oSkill):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return []
    oAgent = oAttack.m_Agent
    if not oAgent:
        return []
    return oAgent.GetData('LstSubductionPos', [])

