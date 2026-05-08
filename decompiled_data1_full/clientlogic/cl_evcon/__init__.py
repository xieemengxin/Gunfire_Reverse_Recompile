# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_evcon/__init__.pyc
# RelativePath: clientlogic/cl_evcon/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_evcon.evc_item import *
from cl_evcon.evc_state import *
from cl_evcon.evc_passive import *
from cl_evcon.evc_achieve import *
from cl_evcon.evc_season import *
from cl_evcon.evc_task import *
from cl_evact import CheckWeaponType2, GetCommonEventKey
from cl_commondefines.cd_illus import *
from cl_commondefines import PF_TYPE_BENEDICTION, PF_TYPE_SHOOT, PF_TYPE_CONSHOOT, PF_TYPE_CHARGE, DAM_TYPE_WEAKNESS, MAIN_FIRECNT, WARRIOR_HERO, WARRIOR_MONSTER, DEBUG_STATUS_NOCOSTBULLET, INTERACT_STATUS_PEND, WARRIOR_SUMMON, DAM_MASK_PART, DAM_TYPE_SHIELD, LEVEL_TYPE_HIDE, INSCRIPTION_TYPE_EXCLUSIVE, PART_TYPE, NWARRIOR_DROP_BULLET, DAM_USE_ALL, CRT_TYPE_DIRECTPOS, PF_TYPE_SUITACTIVE, PF_TYPE_MONSTERACT, GAMBLER_HERO, SKILLCACHE_LSTINT, SKILLCACHE_LSTINTSPECIAL, LEVEL_STATUS_GOAL, SKILLCACHE_PARENTACTNUM, NWARRIOR_DROP_TRIGGER, TALENT_GRADE_REDUCE, TALENT_GRADE_ADD, TALENT_GRADE_IGNORE_NOTHING, TALENT_GRADE_IGNORE_ALL, TALENT_GRADE_IGNORE_NEWLEVEL, TALENT_GRADE_IGNORE_OLDLEVEL, MONSTER_PART_FLAW
from cl_commondefines import SOURCE_REASON_MODE_MONSTERRELIC, WARRIOR_PET, WARRIOR_DEVICE_BARRIER, WARRIOR_DEVICE, INKMASTER_HERO, TOXIC_FOG, NWARRIOR_DROP_EQUIP, EXECUTOR_HERO, WARRIOR_PET_MINI, WARRIOR_PET_MINICLONE, g_PositiveElement, HP_TYPE_SHIELD, HP_TYPE_ARMOR, HP_TYPE_NORMAL, DAM_TYPE_NORMAL, DIE_PRIORITY_TYPE_DIE, DIE_PRIORITY_TYPE_NO_DIE, DEFEND_TREND_SHIELD, NWARRIOR_DROP, SUITTAG_EXPORT, SUITEXPORT_PFSPECIALTAG, RELIC_TO_TEMPRELIC, NWARRIOR_NPC_ALL_GOLDENCUP, VIRTUAL_ITEM_WAND, VIRTUAL_ITEM_WANDCOMP, WAND_COMP_TYPE_ACTION, WAND_COMP_TYPE_CONDITION, HULK_NORMAL_PUNCH_PF, PF_TYPE_CAREERPF, WARRIOR_BOSS, LION_MONSTER_LOCK_STATE, GARDENER_HERO, IGNORESTATE_EFF_FLAG, LION_MONSTER_ENHANCELOCK_STATE
from cl_pxlayer import PXMASK_BARRIER, PXMASK_GROUNDBLK
from cl_abnormalconf import g_AllAbnormalStateSID, g_AllEleAbnormalState
from cl_only import PY_FLAG_DEAD, Time2Frame, Frame2Time
from cl_only import SendAlert
from cl_newformula import GetWarriorAttr
from cl_object.reason import CPerformReason
from cl_container.inkcon import INKPERFORM
from cl_container.petcon import FUSE_MAIN_POS
from cl_platformdata import GetSeasonSuitCls, GetActiveSourceSuitMap, GetSummonClassify, GetSeasonSuitTag, GetCommonActiveTag, GetSpItemBanBenedicList, GetDiceSpecialTypeList, GetS7CrystalType, GetClientActiveTag
from cl_cscommondef.cs_perform import SKILLCACHE_INT
import cl_item.defines as itemdef
import cl_item.load as itemload
import cl_modeldefine
import cl_perform
import cl_item
import cl_hero
import cl_state

def CheckIsHit(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if 'CurHitArea' not in oSkill.m_Update:
        return 0
    return 1


def CheckHitBody(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'MainDam' in dMsgInfo:
        lstDam = dMsgInfo['MainDam']
        for _, oReason in lstDam:
            iDamType = oReason.Query('DamType')
            if iDamType & DAM_TYPE_WEAKNESS != DAM_TYPE_WEAKNESS:
                return 1
        
    elif 'RS' in dMsgInfo:
        oReason = dMsgInfo['RS']
        iDamType = oReason.Query('DamType')
        if iDamType & DAM_TYPE_WEAKNESS != DAM_TYPE_WEAKNESS:
            return 1
    return 0


def CheckHitWeakness(oListener, oEventCB, iFlow = 0):
    iResult = 0
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'MainDam' in dMsgInfo:
        lstDam = dMsgInfo['MainDam']
        for _, oReason in lstDam:
            iDamType = oReason.Query('DamType')
            if iDamType & DAM_TYPE_WEAKNESS == DAM_TYPE_WEAKNESS:
                iResult = 1
        
    elif 'RS' in dMsgInfo:
        oReason = dMsgInfo['RS']
        iDamType = oReason.Query('DamType')
        if iDamType & DAM_TYPE_WEAKNESS == DAM_TYPE_WEAKNESS:
            iResult = 1
    if not iResult and iFlow and 'RS' in dMsgInfo:
        iFromDamType = dMsgInfo['RS'].Query('FromDamType')
        if iFromDamType & DAM_TYPE_WEAKNESS == DAM_TYPE_WEAKNESS:
            iResult = 1
    return iResult


def CheckBackHit(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    oGame = oListener.m_Game
    if 'CurVID' in dMsgInfo:
        iVictim = dMsgInfo['CurVID']
    elif 'VID' in dMsgInfo:
        iVictim = dMsgInfo['VID']
    else:
        return 0
    oVictim = oGame.GetObject(iVictim)
    if not oVictim:
        return 0
    return cl_formula.CheckPerformBackHit(oVictim, oSkill)


def CheckHitPart(oListener, oEventCB, iCheckHitPart):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if 'CurHitArea' not in oSkill.m_Update:
        return 0
    iHitArea = oSkill.m_Update['CurHitArea']
    return iHitArea == iCheckHitPart


def CheckTargetDist(oListener, oEventCB, fDist, iCheckModelRadius = 0, iObjectType = 0):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    oGame = oListener.m_Game
    iTarget = lstTar[0]
    oTarget = oGame.GetObject(iTarget)
    if not oTarget:
        return 0
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    fDist = cl_formula.GetResultByData(oListener, fDist, dEventInfo, dMsgInfo)
    if oTarget.m_ForceDistance:
        return oTarget.m_ForceDistance <= fDist
    tTargetPos = oTarget.GetPos()
    if iObjectType:
        iOwner = oListener.GetOwnObjectID(iObjectType)
        oOwner = oGame.GetObject(iOwner)
        if not oOwner:
            return 0
    oOwner = oListener
    tOwnerPos = oOwner.GetPos()
    fCheckRadius = 0
    if iCheckModelRadius:
        tModelArgs = cl_modeldefine.GetModelDefine(oTarget.m_Shape, 'Physx')
        fCheckRadius = tModelArgs[0]
    return cl_math.CheckDistance3D(tOwnerPos, tTargetPos, fDist + fCheckRadius)


def CheckHitVictimCnt(oListener, oEventCB, iCnt):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if 'LastVLST' not in oSkill.m_Update:
        return 0
    iCur = len(oSkill.m_Update['LastVLST'])
    if iCnt == iCur:
        return 1
    return 0


def CheckVictimEPFPosDist(oListener, oEventCB, fDis):
    dTrans = oEventCB.GetCBTransInfo()
    if 'EPFPos' not in dTrans:
        SendAlert('err', '回调检查受击者至事件动画点距离 未设置动画点目标')
        return 0
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'CurVID' in dMsgInfo:
        iVictim = dMsgInfo['CurVID']
    elif 'VID' in dMsgInfo:
        iVictim = dMsgInfo['VID']
    else:
        return 0
    oGame = oListener.m_Game
    oVictim = oGame.GetObject(iVictim)
    if not oVictim:
        return 0
    return cl_math.CheckDistance(oVictim.GetPos(), dTrans['EPFPos'], fDis)


def CheckInjuredByTarget(oListener, oEventCB):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    oGame = oListener.m_Game
    for iTarget in lstTar:
        oTarget = oGame.GetObject(iTarget)
        if oTarget:
            dInjured = oTarget.Query('Injured', { })
            if oListener.m_ID in dInjured:
                return 1
    
    return 0


def CheckDeadlyPredictDam(oListener, oEventCB, iObjectType = 0):
    iDiePriorityType = oListener.DiePriorityType()
    if iDiePriorityType == DIE_PRIORITY_TYPE_DIE:
        return 1
    if iDiePriorityType == DIE_PRIORITY_TYPE_NO_DIE:
        return 0
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'PredictChange' not in dMsgInfo:
        return 0
    lstPredictChange = dMsgInfo['PredictChange']
    (_, _, iHPChange) = lstPredictChange
    if iObjectType:
        oWarrior = oListener.GetOwnObject(iObjectType)
        if not oWarrior:
            return 0
    oWarrior = oListener
    if 'PreCureHp' in dMsgInfo:
        (iCalHp, _sKey) = dMsgInfo['PreCureHp']
    else:
        iCalHp = oWarrior.HP()
    if iHPChange >= iCalHp:
        return 1
    return 0


def CheckBreakShieldPredictDam(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'PredictChange' not in dMsgInfo:
        return 0
    lstPredictChange = dMsgInfo['PredictChange']
    (iShieldChange, _, _) = lstPredictChange
    if iShieldChange and iShieldChange >= oListener.Shield():
        return 1
    return 0


def CheckBreakArmorPredictDam(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'PredictChange' not in dMsgInfo:
        return 0
    lstPredictChange = dMsgInfo['PredictChange']
    (_, iArmor, _) = lstPredictChange
    if iArmor and iArmor >= oListener.Armor():
        return 1
    return 0


def CheckMonsterType(oListener, oEventCB):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget.Query('MonsterSuper'):
        return 0
    return 1


def CheckFromPointPerform(oListener, oEventCB, iPointPerform, iDirect = 0, iFlow = 0):
    iResult = 0
    iPerform = 0
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        iPerform = oSkill.m_Base['pfid']
    elif 'pfid' in dMsgInfo:
        iPerform = dMsgInfo['pfid']
    elif iDirect and 'RS' in dMsgInfo:
        oReason = dMsgInfo['RS']
        if oReason.m_Type == reason.REASON_TYPE_PERFORM:
            iPerform = oReason.m_Perform
    if iPerform == iPointPerform:
        iResult = 1
    elif iFlow and 'AID' in dMsgInfo and 'RS' in dMsgInfo:
        iAttack = dMsgInfo['AID']
        oGame = oListener.m_Game
        oReason = dMsgInfo['RS']
        oFromSkill = oGame.m_SkillMgr.GetSkill(iAttack, oReason.Query('FromActNum', 0))
        if oFromSkill and oFromSkill.m_Base['pfid'] == iPointPerform:
            iResult = 1
    return iResult


def CheckInPointPerform(oListener, oEventCB, dPerform, iDirect = 0, iFlow = 0):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    return CheckInPointPerformByMsgInfo(oListener, dPerform, dMsgInfo, iDirect, iFlow)


def CheckInPointPerformByMsgInfo(oListener, dPerform, dMsgInfo, iDirect, iFlow):
    iResult = 0
    iPerform = 0
    if 'Skill' in dMsgInfo:
        iPerform = dMsgInfo['Skill'].m_Base['pfid']
    elif 'pfid' in dMsgInfo:
        iPerform = dMsgInfo['pfid']
    elif iDirect and 'RS' in dMsgInfo:
        oReason = dMsgInfo['RS']
        if oReason.m_Type == reason.REASON_TYPE_PERFORM:
            iPerform = oReason.m_Perform
    if iPerform in dPerform:
        iResult = 1
    elif iFlow and 'AID' in dMsgInfo and 'RS' in dMsgInfo:
        oGame = oListener.m_Game
        oFromSkill = oGame.m_SkillMgr.GetSkill(dMsgInfo['AID'], dMsgInfo['RS'].Query('FromActNum', 0))
        if oFromSkill and oFromSkill.m_Base['pfid'] in dPerform:
            iResult = 1
    return iResult


def CheckFromWeapon(oListener, oEventCB, iFlowWeapon = 0):
    iResult = 0
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        if oSkill.m_Base['Weapon']:
            iResult = 1
    if not iResult and iFlowWeapon and 'AID' in dMsgInfo and 'RS' in dMsgInfo:
        iAttack = dMsgInfo['AID']
        oReason = dMsgInfo['RS']
        oFromSkill = oListener.m_Game.m_SkillMgr.GetSkill(iAttack, oReason.Query('FromActNum', 0))
        if oFromSkill and oFromSkill.m_Base['Weapon']:
            iResult = 1
    return iResult


def CheckFromPFReason(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'RS' not in dMsgInfo:
        return 0
    oReason = dMsgInfo['RS']
    if oReason.m_Type == reason.REASON_TYPE_PERFORM:
        return 1
    return 0


def CheckPerformType(oListener, oEventCB, iPerformType, iFlow = 0):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'pfid' in dMsgInfo:
        iPerform = dMsgInfo['pfid']
        clsPerform = cl_perform.GetPerformModule(iPerform)
        if not clsPerform:
            return 0
        iType = clsPerform.m_PFType
    elif 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        iType = oSkill.m_Base['PFType']
    elif iFlow and 'AID' in dMsgInfo and 'RS' in dMsgInfo:
        oFromSkill = oListener.m_Game.m_SkillMgr.GetSkill(dMsgInfo['AID'], dMsgInfo['RS'].Query('FromActNum', 0))
        if not oFromSkill:
            return 0
        iType = oFromSkill.m_Base['PFType']
    else:
        return 0
    if iType != iPerformType:
        return 0
    return 1


def CheckMainPerform(oListener, oEventCB, iFlow = 0):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'pfid' in dMsgInfo:
        iPerform = dMsgInfo['pfid']
        clsPerform = cl_perform.GetPerformModule(iPerform)
        if not clsPerform:
            return 0
        iType = clsPerform.m_PFType
    elif 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        iType = oSkill.m_Base['PFType']
        iPerform = oSkill.m_Base['pfid']
    elif iFlow and 'AID' in dMsgInfo and 'RS' in dMsgInfo:
        oFromSkill = oListener.m_Game.m_SkillMgr.GetSkill(dMsgInfo['AID'], dMsgInfo['RS'].Query('FromActNum', 0))
        if not oFromSkill:
            return 0
        iType = oFromSkill.m_Base['PFType']
        iPerform = oFromSkill.m_Base['pfid']
    else:
        return 0
    if iType == PF_TYPE_CAREERPF:
        return 1
    if iPerform in cl_hero.load.GetHero2SpecialCareer().get(oListener.m_SID, []):
        return 1
    return 0


def CheckEleDamType(oListener, oEventCB, iDamType, iExt = 0):
    iElementType = GetEleDamType(oListener, oEventCB)
    if iDamType & iElementType:
        return 1
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if iExt and 'MainDam' in dMsgInfo:
        lstMainDam = dMsgInfo['MainDam']
        for _, oReason in lstMainDam:
            lstExt = oReason.Query('ExtEleAbnormal', [])
            for dExt in lstExt:
                iElementType = dExt['DamType'] & DAM_MASK_ELEMENT
                if iDamType & iElementType:
                    return 1
            
        
    return 0


def GetEleDamType(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iElementType = 0
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        if 'ElementType' in oSkill.m_Cache:
            iElementType = oSkill.m_Cache['ElementType']
    if not iElementType and 'RS' in dMsgInfo:
        oReason = dMsgInfo['RS']
        iElementType = oReason.Query('DamType', 0)
        iElementType = iElementType & DAM_MASK_ELEMENT
    return iElementType


def CheckSrcDamType(oListener, oEventCB, iCheckType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'RS' not in dMsgInfo:
        return 0
    if dMsgInfo['RS'].Query('DamType', 0) & iCheckType == iCheckType:
        return 1
    return 0


def CheckFromMinorPerform(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    iPerform = dMsgInfo['Skill'].m_Base['pfid']
    clsPerform = cl_perform.GetPerformModule(iPerform)
    if clsPerform.m_IsMinor:
        return 1
    return 0


def CheckDirectDamage(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'RS' not in dMsgInfo:
        return 0
    oReason = dMsgInfo['RS']
    if oReason.Query('CopyWeapon'):
        return 0
    return 1


def CheckHasState(oListener, oEventCB, iState):
    if oListener.m_State.GetItemBySID(iState):
        return 1
    return 0


def CheckStateSameItemSource(oListener, oEventCB, iStateSID):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'RS' in dMsgInfo:
        iItem = dMsgInfo['RS'].Query('Item', 0)
    elif 'ItemID' in dMsgInfo:
        iItem = dMsgInfo['ItemID']
    elif 'Skill' in dMsgInfo:
        iItem = dMsgInfo['Skill'].m_Base['Weapon']
    else:
        return 0
    for oState in oListener.m_State.GetItems(iStateSID):
        if oState.m_Item == iItem:
            return 1
    
    return 0


def CheckTargetAddState(oListener, oEventCB, iState):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if dMsgInfo['StateSID'] == iState:
        return 1
    return 0


def CheckTargetHasState(oListener, oEventCB, iState, iFromSameItem = 0, iFromSelf = 0, iFromMsgItem = 0, iFromMsgAID = 0):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return 0
    lstState = oTarget.m_State.GetItems(iState)
    if not lstState:
        return 0
    if iFromSelf or iFromMsgAID or iFromSameItem or iFromMsgItem:
        dMsgInfo = oEventCB.GetCBMsgInfo()
        iAttack = 0
        if iFromSelf:
            iAttack = oListener.m_ID
        elif iFromMsgAID:
            if 'AID' in dMsgInfo:
                iAttack = dMsgInfo['AID']
            elif 'Skill' in dMsgInfo:
                iAttack = dMsgInfo['Skill'].m_Base['AID']
        iTarItem = 0
        if iFromSameItem:
            dEventInfo = oEventCB.GetCBEventInfo()
            iTarItem = dEventInfo['ItemID']
        elif iFromMsgItem:
            iTarItem = dMsgInfo['RS'].Query('Item')
        for oState in lstState:
            if iAttack and oState.m_Attacker != iAttack:
                continue
            if iTarItem and oState.m_Item != iTarItem:
                continue
        else:
            return 0
    return 1


def CheckTargetHasStateByAttacker(oListener, oEventCB, iState, iAttack):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return False
    lstTar = dTrans['TargetList']
    if not lstTar:
        return False
    oTarget = oListener.m_Game.GetObject(lstTar[0])
    if not oTarget:
        return False
    if iAttack:
        dMsgInfo = oEventCB.GetCBMsgInfo()
        dEventInfo = oEventCB.GetCBEventInfo()
        iAttack = cl_formula.GetResultByData(oListener, iAttack, dEventInfo, dMsgInfo)
    else:
        iAttack = oListener.m_ID
    return oTarget.m_State.CheckHasStateFrom(iState, iAttack = iAttack, iItem = 0)


def GetTargetStateCount(oListener, oEventCB, iState, iFromSelf = 0, iFromSameItem = 0):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return 0
    if iFromSelf or iFromSameItem:
        dEventInfo = oEventCB.GetCBEventInfo()
        lstState = oTarget.m_State.GetItems(iState)
        for oState in lstState:
            if iFromSelf and oState.m_Attacker != oListener.m_ID:
                continue
            if iFromSameItem and dEventInfo['ItemID'] != oState.m_Item:
                continue
            return oState.GetCount()
        
        return 0
    oState = oTarget.m_State.GetItemBySID(iState)
    if not oState:
        return 0
    return oState.GetCount()


def CheckHasStateFromSelf(oListener, oEventCB, iState):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oGame = oListener.m_Game
    oTarget = oGame.GetObject(iTarget)
    if not oTarget:
        return 0
    oState = oTarget.m_State.GetItemBySource(iState, oListener.m_ID)
    if oState:
        return 1
    return 0


def GetTargetStateNum(oListener, oEventCB, iStateSID, iSameItem):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    if iSameItem:
        iItem = dEventInfo['ItemID']
        if not iItem:
            oReason = dEventInfo['RS']
            iItem = oReason.Query('Item', 0)
        if not iItem:
            return 0
    iItem = 0
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oGame = oListener.m_Game
    oTarget = oGame.GetObject(iTarget)
    if not oTarget:
        return 0
    iCnt = 0
    lstState = oTarget.m_State.GetItems(iStateSID)
    for oTarState in lstState:
        if iItem and oTarState.m_Reason.Query('Item', 0) != iItem:
            continue
        iCnt += 1
    
    return iCnt


def CheckVictimFightType(oListener, oEventCB, iFightType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'CurVID' in dMsgInfo:
        iVictim = dMsgInfo['CurVID']
    elif 'VID' in dMsgInfo:
        iVictim = dMsgInfo['VID']
    else:
        return 0
    oGame = oListener.m_Game
    oVictim = oGame.GetObject(iVictim)
    if not oVictim:
        return 0
    if 255 & iFightType:
        if oVictim.m_FightType == iFightType:
            return 1
        return 0
    if oVictim.m_FightType & iFightType == iFightType:
        return 1
    return 0


def CheckFightType(oListener, oEventCB, iFightType):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oGame = oListener.m_Game
    oTarget = oGame.GetObject(iTarget)
    if not oTarget:
        return 0
    if 255 & iFightType:
        if oTarget.m_FightType == iFightType:
            return 1
        return 0
    if oTarget.m_FightType & iFightType == iFightType:
        return 1
    return 0


def CheckFightTypeInRange(oListener, oEventCB, dFightType):
    sKey = oEventCB.m_Key
    if not dFightType:
        SendAlert('err', '%s需要指定战斗类型范围' % sKey)
        return 0
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % sKey)
        return 0
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oGame = oListener.m_Game
    oTarget = oGame.GetObject(iTarget)
    if not oTarget:
        return 0
    for iFightType in dFightType:
        if 255 & iFightType or oTarget.m_FightType == iFightType:
            return 1
        if oTarget.m_FightType & iFightType == iFightType:
            return 1
    
    return 0


def CheackTargetFightTypeIsRealit(oListener, oEventCB):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oGame = oListener.m_Game
    oTarget = oGame.GetObject(iTarget)
    if not oTarget:
        return 0
    if oTarget.m_FightType in PART_TYPE:
        return 0
    return 1


def CheckTargetIsSelfSummon(oListener, oEventCB, iFightType):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return False
    lstTar = dTrans['TargetList']
    if not lstTar:
        return False
    oGame = oListener.m_Game
    for iTarget in lstTar:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        if oTarget.m_FightType & iFightType == iFightType and oTarget.m_Owner == oListener.m_ID:
            return True
    
    return False


def CheckTargetIsSelfOwner(oListener, oEventCB):
    iOwner = oListener.m_Owner
    if not iOwner:
        return False
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return False
    lstTar = dTrans['TargetList']
    if not lstTar:
        return False
    return lstTar[0] == iOwner


def CheckTargetIsSummon(oListener, oEventCB):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return False
    lstTar = dTrans['TargetList']
    if not lstTar:
        return False
    oGame = oListener.m_Game
    oTarget = oGame.GetObject(lstTar[0])
    if not oTarget:
        return False
    if (oTarget.m_FightType & WARRIOR_SUMMON or oTarget.m_Owner) and oTarget.m_FightType & WARRIOR_MONSTER:
        return True
    return False


def CheckTargetSideType(oListener, oEventCB, iTargetType):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oGame = oListener.m_Game
    oTarget = oGame.GetObject(iTarget)
    if not oTarget:
        return 0
    iAttack = oListener.m_ID
    iSide = oListener.m_Side
    return cl_math.CheckTargetType(oGame, oTarget, iAttack, iSide, iTargetType)


def CheckTargetMoveStatus(oListener, oEventCB, iStatus):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oGame = oListener.m_Game
    oTarget = oGame.GetObject(iTarget)
    if not oTarget or not (oTarget.m_MoveCtrl):
        return 0
    return oTarget.m_MoveCtrl.m_CurStatus == iStatus


def CheckTargetInSelfFace(oListener, oEventCB, iCosAngle):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oGame = oListener.m_Game
    oTarget = oGame.GetObject(iTarget)
    if not oTarget:
        return 0
    vListen = oListener.GetPos()
    vFace = oListener.GetFacing()
    vTarget = oTarget.GetPos()
    if cl_math.CheckVector2Angle(cl_math.Vec3Minus(vTarget, vListen), vFace, iCosAngle):
        return 0
    return 1


def CheckSourceInSelfFace(oListener, oEventCB, iCosAngle, dSkill, dOffsetSkill):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oGame = oListener.m_Game
    vTarget = None
    iPerform = 0
    bDirect = False
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        iPerform = oSkill.m_Base['pfid']
        dCartoon = oSkill.GetCurCartoon()
        if 'CrtType' in dCartoon and dCartoon['CrtType'] == CRT_TYPE_DIRECTPOS:
            bDirect = True
        if iPerform not in dSkill and bDirect:
            vTarget = dCartoon['Start']
        elif 'RS' in dMsgInfo:
            oReason = dMsgInfo['RS']
            if isinstance(oReason, CPerformReason):
                iPerform = oReason.m_Perform
    if not None:
        iTarget = 0
        if 'AID' in dMsgInfo:
            iTarget = dMsgInfo['AID']
        elif 'Skill' in dMsgInfo:
            iTarget = dMsgInfo['Skill'].m_Base['AID']
        else:
            return 0
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            return 0
        vTarget = oTarget.GetPos()
    if iPerform and not bDirect and iPerform in dOffsetSkill:
        fDis = dOffsetSkill[iPerform]
        vTarget = cl_math.Vec3DisplaceDir(vTarget, oListener.GetFacing(), fDis)
    if cl_math.CheckVector2Angle(cl_math.Vec3Minus(vTarget, oListener.GetPos()), oListener.GetFacing(), iCosAngle):
        return 0
    return 1


def CheckTargetPointBaseMonster(oListener, oEventCB, iMonsterSID):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s回调检查目标为指定基础怪物 事件未获取目标' % oEventCB.m_Key)
        return 0
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oGame = oListener.m_Game
    oTarget = oGame.GetObject(iTarget)
    if oTarget and oTarget.m_FightType & WARRIOR_MONSTER == WARRIOR_MONSTER:
        pass
    return oTarget.m_DataSID == iMonsterSID


def CheckTargetPointBaseMonsters(oListener, oEventCB, dMonsterSID):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s回调检查目标为指定基础怪物组 事件未获取目标' % oEventCB.m_Key)
        return 0
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oGame = oListener.m_Game
    oTarget = oGame.GetObject(iTarget)
    if oTarget and oTarget.m_FightType & WARRIOR_MONSTER == WARRIOR_MONSTER:
        pass
    return oTarget.m_DataSID in dMonsterSID


def CheckTargetPointBaseSummon(oListener, oEventCB, iBaseSummonSID):
    dSID = {
        iBaseSummonSID: 1 }
    return CheckTargetPointBaseSummons(oListener, oEventCB, dSID)


def CheckTargetPointBaseSummons(oListener, oEventCB, dBaseSummonSID):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTarget = dTrans['TargetList']
    if not lstTarget:
        return 0
    iTarget = lstTarget[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget or oTarget.m_FightType & WARRIOR_SUMMON != WARRIOR_SUMMON or oTarget.m_DataSID not in dBaseSummonSID:
        return 0
    return 1


def CheckMonsterPFAttackType(oListener, oEventCB, iAttackType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'pfid' in dMsgInfo:
        iPerform = dMsgInfo['pfid']
    elif 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        iPerform = oSkill.m_Base['pfid']
    else:
        return 0
    clsPerform = cl_perform.GetPerformModule(iPerform)
    if not clsPerform or clsPerform.m_PFType != PF_TYPE_MONSTERACT:
        return 0
    iType = clsPerform.m_AttackType
    if iType != iAttackType:
        return 0
    return 1


def CheckTargetHasAfPF(oListener, oEventCB, iAfPF):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return 0
    tSuperInfo = oTarget.Query('MonsterSuper', None)
    if tSuperInfo:
        (_, iAf) = tSuperInfo
        return iAfPF == iAf
    return 0


def CheckTargetInSkillCollect(oListener, oEventCB, sKey):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s回调检查事件目标被技能统计 事件未获取目标' % oEventCB.m_Key)
        return 0
    oSkill = dMsgInfo['Skill']
    dTarget = oSkill.m_Collect.get(sKey, { })
    for iTarget in dTrans['TargetList']:
        if iTarget not in dTarget:
            return 0
    
    return 1


def CheckTargetInTheScene(oListener, oEventCB):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTarget = dTrans['TargetList']
    if not lstTarget:
        return 0
    iTarget = lstTarget[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return 0
    return oListener.m_Scene == oTarget.m_Scene


def GetVictimHPRatio(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'CurVID' in dMsgInfo:
        iVictim = dMsgInfo['CurVID']
    elif 'VID' in dMsgInfo:
        iVictim = dMsgInfo['VID']
    else:
        return 0
    oGame = oListener.m_Game
    oVictim = oGame.GetObject(iVictim, PY_FLAG_DEAD)
    if not oVictim:
        return 0
    iTrueVictim = oVictim.Query('TentacleOwner', 0)
    oVictim = oGame.GetObject(iTrueVictim) if iTrueVictim else oVictim
    return oVictim.m_HP * 100 // oVictim.QueryAttr('HPMax')


def GetVictimTotalHPRatio(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'CurVID' in dMsgInfo:
        iVictim = dMsgInfo['CurVID']
    elif 'VID' in dMsgInfo:
        iVictim = dMsgInfo['VID']
    else:
        return 0
    oGame = oListener.m_Game
    oVictim = oGame.GetObject(iVictim, PY_FLAG_DEAD)
    if not oVictim:
        return 0
    return (oVictim.HP() + oVictim.Shield() + oVictim.Armor()) * 100 // (oVictim.QueryAttr('HPMax') + oVictim.QueryAttr('ShieldMax') + oVictim.QueryAttr('ArmorMax'))


def GetListenerHPRatio(oListener, oEventCB):
    return oListener.m_HP * 100 // oListener.QueryAttr('HPMax')


def GetShieldRatio(oListener, oEventCB):
    iShieldMax = oListener.ShieldMax()
    if not iShieldMax:
        return 0
    iShield = oListener.Shield()
    return iShield * 100 // iShieldMax


def GetTargetTotalAllHP(oListener, oEventCB):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return 0
    return oTarget.HP() + oTarget.Shield() + oTarget.Armor()


def GetEventWeaponBulletCnt(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ItemID' not in dMsgInfo:
        return 0
    iWeapon = dMsgInfo['ItemID']
    oWeapon = oListener.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return 0
    oBulletCom = oWeapon.GetComponent('Bullet')
    if not oBulletCom:
        return 0
    return oBulletCom.Bullet()


def GetEventWeaponGrade(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ItemID' not in dMsgInfo:
        return 0
    iWeapon = dMsgInfo['ItemID']
    oWeapon = oListener.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return 0
    return oWeapon.m_Grade


def GetEventWeaponInscriptionNum(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ItemID' not in dMsgInfo:
        return 0
    iWeapon = dMsgInfo['ItemID']
    oWeapon = oListener.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return 0
    oInscriptionCom = oWeapon.GetComponent('Inscription')
    if oInscriptionCom:
        return oInscriptionCom.GetInscriptionNum()
    return 0


def GetWeaponExclusiveInscriptionNum(oListener, oEventCB, iInscriptionType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ItemID' in dMsgInfo:
        iWeapon = dMsgInfo['ItemID']
        oWeapon = oListener.m_WieldCon.GetItemByID(iWeapon)
    elif 'RecycleDropType' in dMsgInfo:
        iRecycleDrop = dMsgInfo['RecycleDropType']
        if iRecycleDrop != NWARRIOR_DROP_EQUIP:
            return 0
        oDrop = oListener.m_Game.GetObject(dMsgInfo['RecycleDrop'])
        oWeapon = oDrop.m_DropInfo[0]
    else:
        return 0
    if not oWeapon:
        return 0
    oInscriptionCom = oWeapon.GetComponent('Inscription')
    if not oInscriptionCom:
        return 0
    iExclusiveNum = oInscriptionCom.m_Type2Num.get(iInscriptionType, 0)
    return iExclusiveNum


def GetDropWeaponExclusiveInscriptionNum(oListener, oEventCB, iInscriptionType = 0):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Weapon' not in dMsgInfo:
        return 0
    if not dMsgInfo['Weapon']:
        return 0
    oInscriptionCom = dMsgInfo['Weapon'].GetComponent('Inscription')
    if not oInscriptionCom:
        return 0
    if not iInscriptionType:
        return oInscriptionCom.GetInscriptionNum()
    return oInscriptionCom.m_Type2Num.get(iInscriptionType, 0)


def CheckWeaponHasInscription(oListener, oEventCB, iSID):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        if 'Inscription' in oSkill.m_Cache and iSID in oSkill.m_Cache['Inscription']:
            return 1
    if 'ItemID' in dMsgInfo:
        iWeapon = dMsgInfo['ItemID']
        oWeapon = oListener.m_WieldCon.GetItemByID(iWeapon)
        if oWeapon:
            oPerformCom = oWeapon.GetComponent('Perform')
            if oPerformCom and oPerformCom.GetPerform(iSID):
                return 1
    return 0


def PassiveCBSetAndReturnWeaponAttrTimes(oListener, oEventCB, sAttr, iTime):
    dEventInfo = oEventCB.GetCBEventInfo()
    iItemID = dEventInfo['ItemID']
    oWeapon = oListener.m_WieldCon.GetItemByID(iItemID)
    if not oWeapon:
        return 0
    lstHappend = oWeapon.Query(sAttr, [])
    iNowFrame = oListener.m_Game.GetFrameNum()
    iSpaFrame = Time2Frame(iTime)
    lstHappend.append(iNowFrame)
    for iFTime in lstHappend[:]:
        if iNowFrame - iFTime <= iSpaFrame:
            break
        lstHappend.pop(0)
    
    oWeapon.Set(sAttr, lstHappend)
    return len(lstHappend)


def CheckWeaponBulletCnt(oListener, oEventCB, iCnt):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    dEventInfo = oEventCB.GetCBEventInfo()
    iCnt = cl_formula.GetResultByData(oListener, iCnt, dEventInfo, dMsgInfo)
    if 'CurBullet' not in oSkill.m_Collect:
        return 0
    iPreBullet = oSkill.m_Collect['CurBullet']
    return iPreBullet == iCnt


def CheckCartridgeEmpty(oListener, oEventCB):
    if oListener.Query('DebugStatus', 0) & DEBUG_STATUS_NOCOSTBULLET == DEBUG_STATUS_NOCOSTBULLET:
        return 0
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    dCollect = oSkill.m_Collect
    if not dCollect:
        return 0
    if 'NoBulletUse' in dCollect:
        return 0
    if 'CurBullet' not in dCollect:
        return 0
    iPreBullet = dCollect['CurBullet']
    iUseBullet = dCollect['BulletUse']
    iUseBullet += (dCollect['ExtBulletUse'] if 'ExtBulletUse' in dCollect else 0)
    if iUseBullet >= iPreBullet:
        return 1
    return 0


def CheckWeaponType(oListener, oEventCB, iType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if 'ItemType' not in oSkill.m_Cache:
        return 0
    if oSkill.m_Cache['ItemType'] == iType:
        return 1
    return 0


def CheckWeaponTypeByHoldType(oListener, oEventCB, iHoldType, iType):
    lstItem = oListener.m_WieldCon.GetWeapons(iHoldType)
    if not lstItem:
        return 0
    for oItem in lstItem:
        if CheckWeaponType2(oItem, iType):
            return 1
    
    return 0


def CheckEventWeaponType(oListener, oEventCB, iType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iWeapon = 0
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        if 'ItemType' in oSkill.m_Cache:
            iWeaponType = oSkill.m_Cache['ItemType']
            if 15 & iType:
                if iWeaponType == iType:
                    return 1
                return 0
            if iWeaponType & iType == iType:
                return 1
            return 0
        iWeapon = oSkill.m_Cache['ItemID'] if 'ItemID' in oSkill.m_Cache else 0
    elif 'ItemID' in dMsgInfo:
        iWeapon = dMsgInfo['ItemID']
    elif 'ReplaceID' in dMsgInfo:
        iWeapon = dMsgInfo['ReplaceID']
    if not iWeapon:
        return 0
    oWeapon = oListener.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return 0
    return CheckWeaponType2(oWeapon, iType)


def CheckEventWeaponTypeInPointType(oListener, oEventCB, dType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iWeapon = 0
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        iWeapon = oSkill.m_Cache['ItemID'] if 'ItemID' in oSkill.m_Cache else 0
    elif 'ItemID' in dMsgInfo:
        iWeapon = dMsgInfo['ItemID']
    elif 'ReplaceID' in dMsgInfo:
        iWeapon = dMsgInfo['ReplaceID']
    if not iWeapon:
        return 0
    oWeapon = oListener.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return 0
    for iType in dType:
        if CheckWeaponType2(oWeapon, iType):
            return 1
    
    return 0


def CheckEventWeaponClassifyTag(oListener, oEventCB, iClassifyTag):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iWeapon = 0
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        iWeapon = oSkill.m_Cache['ItemID'] if 'ItemID' in oSkill.m_Cache else 0
    elif 'ItemID' in dMsgInfo:
        iWeapon = dMsgInfo['ItemID']
    if not iWeapon:
        return False
    oWeapon = oListener.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return False
    if iClassifyTag in oWeapon.m_ClassifyTag:
        return True
    return False


def CheckEventWeaponBulletType(oListener, oEventCB, iType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iWeapon = 0
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        iWeapon = oSkill.m_Cache['ItemID'] if 'ItemID' in oSkill.m_Cache else 0
    elif 'ItemID' in dMsgInfo:
        iWeapon = dMsgInfo['ItemID']
    if not iWeapon:
        return 0
    oWeapon = oListener.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return 0
    oBulletCom = oWeapon.GetComponent('Bullet')
    if oBulletCom.BulletType() != iType:
        return 0
    return 1


def CheckWeaponBulletTypeByHoldType(oListener, oEventCB, iHoldType, iBulletType):
    oItem = oListener.m_WieldCon.GetCurWeapon(iHoldType)
    if not oItem:
        return 0
    oBulletCom = oItem.GetComponent('Bullet')
    if not oBulletCom:
        return 0
    return oBulletCom.m_BulletType == iBulletType


def CheckWeaponElementTypeByHoldType(oListener, oEventCB, iHoldType, iElementType):
    oItem = oListener.m_WieldCon.GetCurWeapon(iHoldType)
    if not oItem:
        return 0
    iItemElementType = oItem.m_ElementType
    if iItemElementType & iElementType == iElementType:
        return 1
    return 0


def CheckOwnerWeaponElementTypeByHoldType(oListener, oEventCB, iHoldType, iElementType):
    oOwner = oListener.GetOwner()
    if not oOwner:
        return 0
    return CheckWeaponElementTypeByHoldType(oOwner, oEventCB, iHoldType, iElementType)


def EventCBCheckAttorneyWeaponElement(oListener, oEventCB, iElementType):
    lstWeapon = oListener.m_WieldCon.GetAllItemByType(itemdef.EQUIP_TYPE_MAINWEAPON)
    oAttorneyWeapon = None
    for oWeapon in lstWeapon:
        if not oWeapon or oWeapon.GetComponent('Hold').HoldPos() == itemdef.MAIN_HOLD:
            continue
        oAttorneyWeapon = oWeapon
    
    if not oAttorneyWeapon:
        return 0
    iItemElementType = oAttorneyWeapon.m_ElementType
    return iItemElementType & iElementType == iElementType


def CheckWeaponElementType(oListener, oEventCB, iItemType, iHoldType, iReverse, iElementType):
    lstWeapon = oListener.m_WieldCon.GetAllItemByType(iItemType)
    for oWeapon in lstWeapon:
        if not oWeapon:
            continue
        if iReverse or oWeapon.GetComponent('Hold').HoldPos() == iHoldType:
            continue
        if not oWeapon.GetComponent('Hold').HoldPos() == iHoldType:
            continue
        iItemElementType = oWeapon.m_ElementType
        if iItemElementType & iElementType == iElementType:
            return 1
    
    return 0


def GetMainHoldWeaponPos(oListener, oEventCB):
    return oListener.m_WieldCon.GetCurWeaponPos()


def CheckShootStatus(oListener, oEventCB):
    oStatusMgr = oListener.m_ShootStatusMgr
    if oStatusMgr.m_SnipeStatus == SNIPE_STATUS_OPEN:
        return 1
    return 0


def GetFireCnt(oListener, oEventCB, iType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if iType == MAIN_FIRECNT:
        sKey = 'TempFireCnt'
        sMaxKey = 'RepeatCnt'
    else:
        sKey = 'MinorTempFireCnt'
        sMaxKey = 'MinorRepeatCnt'
    if sKey not in oSkill.m_Cache or sMaxKey not in oSkill.m_Cache:
        return 0
    return oSkill.m_Cache[sKey] % oSkill.m_Cache[sMaxKey]


def GetFireOver(oListener, oEventCB, iType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if iType == MAIN_FIRECNT:
        sKey = 'TempFireCnt'
        sMaxKey = 'RepeatCnt'
    else:
        sKey = 'MinorTempFireCnt'
        sMaxKey = 'MinorRepeatCnt'
    if sKey not in oSkill.m_Cache or sMaxKey not in oSkill.m_Cache:
        return 0
    iRlt = oSkill.m_Cache[sKey] % oSkill.m_Cache[sMaxKey]
    if iRlt == oSkill.m_Cache[sMaxKey] - 1:
        return 1
    return 0


def GetTargetBagBulletAmount(oListener, oEventCB, iType):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    oHero = oListener.m_Game.GetObject(dTrans['TargetList'][0], PY_FLAG_DEAD)
    if not oHero:
        return 0
    iBagBullet = oHero.m_BulletCon.Bullet(iType)
    return iBagBullet


def CheckSelfAllBagBulletRatio(oListener, oEventCB, iRatio):
    iAllBagBullet = 0
    iAllBagBulletMax = 0
    for iType in itemload.GetAllWeaponBulletType():
        iAllBagBullet += oListener.m_BulletCon.Bullet(iType)
        iAllBagBulletMax += oListener.m_BulletCon.GetMaxBullet(iType)
    
    if iAllBagBullet >= iAllBagBulletMax * iRatio / 100:
        return 1
    return 0


def GetBulletUseByType(oListener, oEventCB, iType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    dCollect = oSkill.m_Collect
    if 'OtherBulletUse' in dCollect and iType in dCollect['OtherBulletUse']:
        return dCollect['OtherBulletUse'][iType]
    iWeapon = oSkill.m_Cache['ItemID'] if 'ItemID' in oSkill.m_Cache else 0
    if not iWeapon and 'ItemID' in dMsgInfo:
        iWeapon = dMsgInfo['ItemID']
    oWeapon = oListener.m_WieldCon.GetItemByID(iWeapon)
    iCurWeaponBulletType = oWeapon.GetComponent('Bullet').BulletType()
    if 'BulletUse' not in dCollect:
        return 0
    if iCurWeaponBulletType == iType:
        iExtShootBulletUse = dCollect['ExtShootBulletUse'] if 'ExtShootBulletUse' in dCollect else 0
        return dCollect['BulletUse'] + iExtShootBulletUse
    return 0


def CheckPickType(oListener, oEventCB, iType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Item' in dMsgInfo and 'Type' in dMsgInfo and dMsgInfo['Type'] == iType:
        return 1
    return 0


def CheckMiniGameSource(oListener, oEventCB, iSource):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Source' not in dMsgInfo:
        return 0
    iMsgSource = dMsgInfo['Source']
    if iMsgSource == iSource:
        return 1
    return 0


def CheckMiniGameType(oListener, oEventCB, iType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'MiniGameType' not in dMsgInfo:
        return 0
    iMiniGameType = dMsgInfo['MiniGameType']
    if iMiniGameType == iType:
        return 1
    return 0


def CheckTriggerDrop(oListener, oEventCB, iPerform):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'DropType' not in dMsgInfo or 'TriggerItem' not in dMsgInfo:
        return 0
    iType = dMsgInfo['DropType']
    if iType and iType == NWARRIOR_DROP_TRIGGER:
        lstDropInfo = dMsgInfo['TriggerItem']
        for dDropInfo in lstDropInfo:
            if iPerform in dDropInfo:
                return 1
        
    return 0


def CheckTriggerPick(oListener, oEventCB, iPerform):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Item' in dMsgInfo and 'Type' in dMsgInfo and dMsgInfo['Type'] == NWARRIOR_DROP_TRIGGER and iPerform in dMsgInfo['Item']:
        return 1
    return 0


def GetSingleDamageNum(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'TotalDam' not in dMsgInfo:
        return 0
    iEffectDamage = sum(dMsgInfo['TotalDam'])
    if 'ExcessChange' not in dMsgInfo:
        return iEffectDamage // 100
    iExcessDamage = 0
    for iDam, _ in dMsgInfo['ExcessChange']:
        iExcessDamage += iDam
    
    iTotalDamage = iEffectDamage + iExcessDamage
    if iTotalDamage % 100:
        iTotalDamage = (iTotalDamage - iTotalDamage % 100) + 100
    return iTotalDamage


def CheckRandom(oListener, oEventCB, iRange, iProb):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iRange = cl_formula.GetResultByData(oListener, iRange, dEventInfo, dMsgInfo)
    iProb = cl_formula.GetResultByData(oListener, iProb, dEventInfo, dMsgInfo)
    return oListener.m_Game.Random(iRange) + 1 <= iProb


def CheckTalent(oListener, oEventCB, iTalentID):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iTalentID = cl_formula.GetResultByData(oListener, iTalentID, dEventInfo, dMsgInfo)
    oTalent = oListener.m_TalentCon.GetPerform(iTalentID)
    if oTalent:
        return 1
    return 0


def CheckTalentLevel(oListener, oEventCB, iTalentID):
    if not oListener.m_TalentCon:
        return 0
    oTalent = oListener.m_TalentCon.GetPerform(iTalentID)
    if oTalent:
        return oTalent.m_Level
    return 0


def GetRelicNumByQuality(oListener, oEventCB, iQuality):
    iCnt = 0
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iAddingRelic = dMsgInfo.get('NewRelic', 0)
    if iAddingRelic:
        iAddingRelicQuality = cl_perform.GetPerformClassAttr(iAddingRelic, 'm_Quality')
        if not iQuality or iAddingRelicQuality == iQuality:
            iCnt += 1
    for oRelic in oListener.m_RelicCon.GetAllPerform():
        if iQuality and oRelic.m_Quality != iQuality:
            continue
        iCnt += 1
    
    return iCnt


def CheckBulletChange(oListener, oEventCB, iBulletChange, iLevel):
    for oPerform in oListener.m_BulletChangeCon.m_Perform.values():
        if iBulletChange == oPerform.m_SID and iLevel == oPerform.Level() and oPerform.m_Enable == 1:
            return True
    
    return False


def GetMainWeaponNum(oListener, oEventCB):
    return len(oListener.m_WieldCon.GetAllItemByType(itemdef.EQUIP_TYPE_MAINWEAPON))


def GetFormula(oListener, oEventCB, tFormu):
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iVal = cl_formula.GetResultByData(oListener, tFormu, dEventInfo, dMsgInfo)
    return iVal


def GetFormulaWithTarget(oListener, oEventCB, tFormu):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    if not dTrans['TargetList']:
        return 0
    iTarget = dTrans['TargetList'][0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return 0
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iVal = cl_formula.GetResultByData(oTarget, tFormu, dEventInfo, dMsgInfo)
    return iVal


def GetThisTargetNum(oListener, oEventCB):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    return len(dTrans['TargetList'])


def GetPerformAttr(oListener, oEventCB, sAttr):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oSkill = dMsgInfo['Skill']
    iPerform = oSkill.m_Base['pfid']
    oPerform = oListener.GetPerform(iPerform)
    if not oPerform:
        return 0
    return oPerform.CalAttr(sAttr)


def GetSkillCacheValue(oListener, oEventCB, sKey):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if sKey not in oSkill.m_Cache:
        return 0
    return oSkill.m_Cache[sKey]


def GetWeaponCrazyEff(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'CrazyEff' not in dMsgInfo:
        return 0
    return dMsgInfo['CrazyEff']


def CheckBulletFull(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    lstWeapon = oListener.m_WieldCon.GetWeapons(itemdef.MAIN_HOLD)
    for oWeapon in lstWeapon:
        oBulletCom = oWeapon.GetComponent('Bullet')
        if oBulletCom.Bullet() == oBulletCom.QueryAttr('MaxBullet'):
            return 1
    
    if 'ItemID' not in dMsgInfo:
        return 0
    iWeapon = dMsgInfo['ItemID']
    oWeapon = oListener.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return 0
    oBulletCom = oWeapon.GetComponent('Bullet')
    if not oBulletCom:
        return 0
    if oBulletCom.Bullet() != oBulletCom.QueryAttr('MaxBullet'):
        return 0
    return 1


def CheckBulletRatio(oListener, oEventCB, iRatio):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    lstWeapon = oListener.m_WieldCon.GetWeapons(itemdef.MAIN_HOLD)
    dEventInfo = oEventCB.GetCBEventInfo()
    iRatio = cl_formula.GetResultByData(oListener, iRatio, dEventInfo, dMsgInfo)
    for oWeapon in lstWeapon:
        oBulletCom = oWeapon.GetComponent('Bullet')
        if oBulletCom.Bullet() >= oBulletCom.QueryAttr('MaxBullet') * iRatio / 100:
            return 1
    
    iWeapon = dMsgInfo['ItemID'] if 'ItemID' in dMsgInfo else 0
    oWeapon = oListener.m_WieldCon.GetItemByID(iWeapon)
    if oWeapon:
        oBulletCom = oWeapon.GetComponent('Bullet')
        if oBulletCom and oBulletCom.Bullet() >= oBulletCom.QueryAttr('MaxBullet') * iRatio / 100:
            return 1
    return 0


def CheckSkillCollectInfo(oListener, oEventCB, sAttr, iAddExtInfo = 0):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    if iAddExtInfo:
        sAttr = '%s%s' % (oEventCB.m_Key, sAttr)
    oSkill = dMsgInfo['Skill']
    if sAttr in oSkill.m_Collect:
        return oSkill.m_Collect[sAttr]
    return 0


def CheckFromSkillCollectInfo(oListener, oEventCB, sAttr):
    iValue = 0
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'AID' in dMsgInfo and 'RS' in dMsgInfo:
        iAttack = dMsgInfo['AID']
        oGame = oListener.m_Game
        oReason = dMsgInfo['RS']
        oFromSkill = oGame.m_SkillMgr.GetSkill(iAttack, oReason.Query('FromActNum', 0))
        if oFromSkill:
            iValue = oFromSkill.m_Collect.get(sAttr, 0)
    return iValue


def CheckStateStatistics(oListener, oEventCB, iStateSID, sAttr):
    oStateCon = oListener.m_State
    oState = oStateCon.GetItemBySID(iStateSID)
    if not oState:
        return 0
    if sAttr in oState.m_Data:
        return oState.m_Data[sAttr]
    return 0


def EventCBCheckTargetStateStatistics(oListener, oEventCB, iStateSID, sAttr, iFromSelf, iFromSameItem):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    if not dTrans['TargetList']:
        return 0
    iTarget = dTrans['TargetList'][0]
    oTarget = oListener.m_Game.GetObject(iTarget, PY_FLAG_DEAD)
    if not oTarget:
        return 0
    iAttack = oListener.m_ID if iFromSelf else 0
    if iFromSameItem:
        dEventInfo = oEventCB.GetCBEventInfo()
        iItem = dEventInfo['ItemID']
    else:
        iItem = 0
    oState = oTarget.m_State.GetStateBySource(iStateSID, iAttack, iItem)
    if not oState or sAttr not in oState.m_Data:
        return 0
    return oState.m_Data[sAttr]


def CheckSkillHitCartoon(oListener, oEventCB, iAddExtInfo = 0):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    dCurCartoon = oSkill.GetCurCartoon()
    if not dCurCartoon:
        return 0
    sAttr = 'HitCartoon'
    if iAddExtInfo:
        sAttr = '%s%s' % (oEventCB.m_Key, sAttr)
    dHitCollect = oSkill.m_Collect[sAttr] if sAttr in oSkill.m_Collect else { }
    if not dHitCollect:
        return 0
    sKey = oEventCB.Key()
    dHitCartoon = dHitCollect[sKey] if sKey in dHitCollect else { }
    if dCurCartoon['ID'] in dHitCartoon:
        return 1
    return 0


def CheckBulletHit(oListener, oEventCB):
    return CheckBulletHitCount(oListener, oEventCB) > 0


def CheckBulletHitCount(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iHitCartoon = 0
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        dHitCollect = oSkill.m_Collect['HitCartoon'] if 'HitCartoon' in oSkill.m_Collect else { }
        if not dHitCollect:
            return 0
        sKey = oEventCB.Key()
        dHitCartoon = dHitCollect[sKey] if sKey in dHitCollect else { }
        iHitCartoon = len(dHitCartoon)
    return iHitCartoon


def CheckParentSkillHitInfo(oListener, oEventCB, iTime):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    iParentActNum = cl_perform.skillcache.GetSkillCacheByIndex(oSkill, SKILLCACHE_PARENTACTNUM)
    if not iParentActNum:
        return 0
    dNewHitInfo = { }
    sKey = oEventCB.m_Key + 'ParentHitInfo'
    dParentHitInfo = oListener.Query(sKey, { })
    iCurFrame = oListener.m_Game.GetFrameNum()
    for iActNum in dParentHitInfo:
        if dParentHitInfo[iActNum] >= iCurFrame:
            dNewHitInfo[iActNum] = dParentHitInfo[iActNum]
    
    oListener.Set(sKey, dNewHitInfo)
    if iParentActNum in dNewHitInfo:
        return 0
    dNewHitInfo[iParentActNum] = iCurFrame + Time2Frame(iTime)
    return 1


def CheckMoveStatus(oListener, oEventCB, iStatus):
    if oListener.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
        return 0
    oMoveCtrl = oListener.m_MoveCtrl
    if not oMoveCtrl:
        return 0
    return oMoveCtrl.m_CurStatus == iStatus


def CheckLastMoveStatus(oListener, oEventCB, iStatus):
    if oListener.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
        return 0
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iOldStatus = dMsgInfo['LastMoveStatus']
    return iOldStatus == iStatus


def CheckTriggerLuckyHit(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'RS' in dMsgInfo:
        oReason = dMsgInfo['RS']
        iLucky = oReason.Query('LuckyHitEff', 1)
        if iLucky > 1:
            return 1
    if 'LuckyHitEff' not in dMsgInfo:
        return 0
    iLuckyHitEff = dMsgInfo['LuckyHitEff']
    if iLuckyHitEff > 1:
        return iLuckyHitEff
    return 0


def GetTriggerLuckyHit(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'RS' in dMsgInfo:
        oReason = dMsgInfo['RS']
        iLucky = oReason.Query('LuckyHitEff', 1)
        if iLucky > 1:
            return iLucky
    if 'LuckyHitEff' not in dMsgInfo:
        return 0
    iLuckyHitEff = dMsgInfo['LuckyHitEff']
    if iLuckyHitEff > 1:
        return iLuckyHitEff
    return 0


def CheckBreakShieldOrArmor(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'IsDam' not in dMsgInfo or not dMsgInfo['IsDam']:
        return 0
    if 'CurVID' in dMsgInfo:
        iTarget = dMsgInfo['CurVID']
        oTarget = oListener.m_Game.GetObject(iTarget)
        if not oTarget:
            return 0
        lstChange = dMsgInfo.get('TotalDam', [])
        if not lstChange:
            return 0
        (iShieldChange, iArmorChange, _) = lstChange
        if iShieldChange and oTarget.Shield() < 1:
            return 1
        if iArmorChange and oTarget.Armor() < 1:
            return 1
    return 0


def CheckEnterNewSecne(oListener, oEventCB):
    if oListener.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
        return 0
    return oListener.ValidEnterNewScene(oListener.m_Scene)


def CheckLayerAndLevel(oListener, oEventCB, iTargetLayer, iTargetLevel):
    oWarMgr = oListener.m_Game.m_WarMgr
    oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
    if not oLevelCtrl:
        return 0
    if oWarMgr.GetBaseLayer(oLevelCtrl.m_LayerNum) == iTargetLayer and oLevelCtrl.m_LevelNum == iTargetLevel:
        return 1
    return 0


def CheckLevelType(oListener, oEventCB, iLevelType):
    oGame = oListener.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oListener.m_Scene)
    if oScene:
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.GetLevelNode(oScene.m_Level)
        if oLevelNode:
            return iLevelType == oLevelNode.m_LevelType
    return 0


def CheckEventLevelType(oListener, oEventCB, iLevelType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'LevelType' in dMsgInfo:
        if dMsgInfo['LevelType'] == iLevelType:
            return 1
        return 0
    if 'Level' in dMsgInfo:
        iLevel = dMsgInfo['Level']
    elif 'LineIdx' in dMsgInfo and dMsgInfo['LineIdx']:
        iLevel = dMsgInfo['LineIdx'][0]
    elif 'LevelNode' in dMsgInfo:
        if dMsgInfo['LevelNode'].m_LevelType == iLevelType:
            return 1
        return 0
    return 0


def CheckEventHideType(oListener, oEventCB, iHideType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Level' in dMsgInfo:
        iLevel = dMsgInfo['Level']
    elif 'LineIdx' in dMsgInfo and dMsgInfo['LineIdx']:
        iLevel = dMsgInfo['LineIdx'][0]
    else:
        return 0
    oGame = oListener.m_Game
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
    if not oLevelNode or oLevelNode.m_LevelType != LEVEL_TYPE_HIDE:
        return 0
    if iLevel not in oLevelCtrl.m_HideLevelLib:
        return 0
    if iHideType != oLevelCtrl.m_HideLevelLib[iLevel]:
        return 0
    return 1


def CheckTransferType(oListener, oEventCB, iTransferDir):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'TransferDir' not in dMsgInfo:
        return 0
    if iTransferDir == dMsgInfo['TransferDir']:
        return 1
    return 0


def CheckLevelGameType(oListener, oEventCB, iType):
    oGame = oListener.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oListener.m_Scene)
    if oScene:
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.GetLevelNode(oScene.m_Level)
        if oLevelNode and oLevelNode.m_GameType == iType:
            return 1
    return 0


def CheckFinalLevel(oListener, oEventCB):
    oLevelCtrl = oListener.m_Game.m_WarMgr.GetComponent('LevelCtrl')
    if not oLevelCtrl or not oLevelCtrl.CheckFinishWar():
        return 0
    return 1


def CheckRelifeType(oListener, oEventCB, iType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'RS' not in dMsgInfo:
        return 0
    oReason = dMsgInfo['RS']
    iRelifeType = oReason.Query('Type', 0)
    if iType == iRelifeType:
        return 1
    return 0


def CheckSceneNPCInteracted(oListener, oEventCB, iNPCType):
    oGame = oListener.m_Game
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Hero' in dMsgInfo and oListener.m_ID != dMsgInfo['Hero']:
        return None
    if 'NPC' in dMsgInfo:
        oNpc = oGame.GetObject(dMsgInfo['NPC'])
        iScene = oNpc.m_Scene if oNpc else 0
    else:
        iScene = oListener.m_Scene
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return 0
    pid = oListener.m_PlayerID
    lstNPC = oScene.GetObjectsByType('NPC')
    for iNPCID in lstNPC:
        oTarget = oGame.GetObject(iNPCID)
        if oTarget and oTarget.m_FightType == iNPCType and oTarget.m_PlayerInteractStatus[pid] == INTERACT_STATUS_PEND:
            return 0
    
    return 1


def CheckNPCType(oListener, oEventCB, iNPCType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if oListener.m_FightType & WARRIOR_HERO and 'Hero' in dMsgInfo and oListener.m_ID != dMsgInfo['Hero']:
        return 0
    if 'NPC' in dMsgInfo:
        iNPCID = dMsgInfo['NPC']
    elif 'NpcID' in dMsgInfo:
        iNPCID = dMsgInfo['NpcID']
    elif 'ShopNpc' in dMsgInfo:
        iNPCID = dMsgInfo['ShopNpc']
    else:
        return 0
    oTarget = oListener.m_Game.GetObject(iNPCID)
    if oTarget and oTarget.m_FightType == iNPCType:
        return 1
    return 0


def CheckNPCSID(oListener, oEventCB, iNPCSID):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'NpcID' not in dMsgInfo:
        return 0
    iNPCSID = iNPCSID % 10000
    iNPCID = dMsgInfo['NpcID']
    oTarget = oListener.m_Game.GetObject(iNPCID)
    if oTarget and oTarget.m_SID == iNPCSID:
        return 1
    return 0


def GetTargetNum(oListener, oEventCB):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTrans['TargetList']
    return len(lstTar)


def CheckFixedTimeDamCnt(oListener, oEventCB, iPerformType, iTime, iDamCnt, bExclude):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if oSkill.m_Base['PFType'] != iPerformType:
        return 0
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    sKey = oLifeCycle.Key()
    oGame = oListener.m_Game
    iFrame = Time2Frame(iTime)
    iCurFrame = oGame.GetFrameNum()
    if sKey in oSkill.m_Collect:
        dFixedDam = oSkill.m_Collect[sKey]
    else:
        dFixedDam = { }
    if not bExclude:
        if iCurFrame in dFixedDam:
            dFixedDam[iCurFrame] += 1
        else:
            dFixedDam[iCurFrame] = 1
    iCnt = 0
    dDam = { }
    for i in range(iFrame):
        if iCurFrame - i in dFixedDam:
            iCnt += dFixedDam[iCurFrame - i]
            dDam[iCurFrame - i] = dFixedDam[iCurFrame - i]
    
    oSkill.m_Collect[sKey] = dDam
    iDamCnt = cl_formula.GetResultByData(oListener, iDamCnt, dEventInfo, dMsgInfo)
    if iCnt >= iDamCnt:
        return 1
    return 0


def GetRecentDis(oListener, oEventCB, sBaseKey):
    sKey = f'''RecentDis{sBaseKey}'''
    return oListener.Query(sKey, 99999)


def GetLiveMonsterPer(oListener, oEventCB):
    oGame = oListener.m_Game
    iScene = oListener.m_Scene
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return 10000
    iLevel = oScene.m_Level
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
    if not oLevelNode:
        return 10000
    lstLine = oLevelNode.m_RoomList[oLevelNode.m_CurRoomPos]
    iLive = 0
    iDie = 0
    iWait = 0
    for oLine in lstLine:
        dSummary = oLine.m_MonsterCtrl.GetMonsterSummary()
        iLive += dSummary['Live']
        iDie += dSummary['Die']
        for iCnt in dSummary['Wait'].values():
            iWait += iCnt
        
    
    iTotal = iLive + iDie + iWait
    if iTotal <= 0:
        return 10000
    return 10000 - int((iDie / iTotal) * 10000)


def GetRefreshMonsterTimeInterval(oListener, oEventCB):
    sKey = oEventCB.m_Key + 'MonsterTime'
    if oListener.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
        return 0
    iCurFrame = oListener.m_Game.GetFrameNum()
    iInterval = Frame2Time(iCurFrame - oListener.Query(sKey, 0))
    return iInterval


def GetSceneMonsterCnt(oListener, oEventCB, iOnlyLife):
    oGame = oListener.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oListener.m_Scene)
    lstMonster = oScene.GetObjectsByType('Monster')
    if iOnlyLife:
        iCnt = 0
        for iMonster in lstMonster:
            oMonster = oGame.GetObject(iMonster)
            if oMonster and not oMonster.IsDead():
                iCnt += 1
        
        return iCnt
    return len(lstMonster)


def GetRoomPlayerCnt(oListener, oEventCB):
    return oListener.m_Game.m_WarMgr.GetAllPlayerCnt()


def GetTargetMonsterRelicNumByQuality(oListener, oEventCB, iQuality):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTrans['TargetList']
    iTarget = lstTar[0]
    oTarget = oListener.m_Game.GetObject(iTarget, PY_FLAG_DEAD)
    if not oTarget or not (oTarget.m_FightType & WARRIOR_MONSTER):
        return 0
    oMonsterRelicElement = oTarget.m_Game.m_WarMgr.GetComponent('MonsterRelicElement')
    if not iQuality:
        return oMonsterRelicElement.GetMonsterRelicNum(oTarget)
    return oMonsterRelicElement.GetMonsterRelicNumByQuality(oTarget, iQuality)


def CheckDamageDropCash(oListener, oEventCB):
    sKey = oEventCB.m_Key + 'DropTime'
    if not oListener.Query(sKey):
        return False
    return oListener.m_Game.GetFrameNum() == oListener.Query(sKey)


def CheckCureSource(oListener, oEventCB, iStateSID):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'TrueChange' not in dMsgInfo:
        return 0
    lstTrueChange = dMsgInfo['TrueChange']
    for _iVal, oReason in lstTrueChange:
        iSource = oReason.Query('SourceState')
        if iSource and iSource == iStateSID:
            return 1
    
    return 0


def CheckRelifeTimesKey(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Key' not in dMsgInfo:
        return 0
    sKey = dMsgInfo['Key']
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    if sKey == oLifeCycle.GetStableKey():
        return 1
    return 0


def CheckShieldOrArmor(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'CurVID' not in dMsgInfo:
        return 0
    iTarget = dMsgInfo['CurVID']
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return 0
    if oTarget.Shield() > 0 or oTarget.Armor() > 0:
        return 1
    return 0


def CheckHasLogicKey(oListener, oEventCB, iLogicKey):
    if not hasattr(oListener, 'QueryBitAttr'):
        return 0
    return oListener.QueryBitAttr('LogicKey') & iLogicKey


def GetMonsterSuperLevel(oListener, oEventCB):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    iMaxSuperLevel = 0
    for iTarget in dTransInfo['TargetList']:
        oTarget = oListener.m_Game.GetObject(iTarget)
        if not oTarget or not (oTarget.m_FightType & WARRIOR_MONSTER):
            continue
        iMaxSuperLevel = max(iMaxSuperLevel, oTarget.SuperLevel())
    
    return iMaxSuperLevel


def CheckPerformCodeTime(oListener, oEventCB, iPerform):
    oPerformcon = oListener.m_Perform
    iCover = oPerformcon.HasCover(iPerform)
    iColdTimeFrame = oPerformcon.GetTotalColdTime(iPerform)
    if not iColdTimeFrame or iCover > 0:
        return 0
    return 1


def CheckAttackInShield(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'RS' not in dMsgInfo:
        return 0
    oReason = dMsgInfo['RS']
    if oReason.Query('DamType') & DAM_MASK_PART == DAM_TYPE_SHIELD:
        return 1
    return 0


def CheckDamFromSelf(oListener, oEventCB, iOrigin = 0):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'AID' not in dMsgInfo:
        return False
    if iOrigin:
        if 'OriginAID' not in dMsgInfo:
            SendAlert('err', '%s监听的消息没有【伤害原始来源】信息，请检查' % oEventCB.m_Key)
            return False
        iCheckAID = dMsgInfo['OriginAID']
    else:
        iCheckAID = dMsgInfo['AID']
    if iCheckAID == oListener.m_ID:
        return True
    return False


def CheckDamFromPetSelf(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'OriginalAID' in dMsgInfo:
        iAID = dMsgInfo['OriginalAID']
    elif 'AID' not in dMsgInfo:
        return False
    iAID = dMsgInfo['AID']
    if iAID == oListener.m_ID:
        return True
    return False


def CheckDamFromPet(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'OriginalAID' in dMsgInfo:
        iAID = dMsgInfo['OriginalAID']
    elif 'AID' not in dMsgInfo:
        return False
    iAID = dMsgInfo['AID']
    oAttacker = oListener.m_Game.GetObject(iAID)
    if oAttacker and oAttacker.m_FightType & WARRIOR_PET:
        return True
    return False


def CheckDamFromTarget(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return False
    if 'AID' not in dMsgInfo:
        return False
    iTarget = dTransInfo['TargetList'][0]
    if dMsgInfo['AID'] == iTarget:
        return True
    return False


def CheckExplosive(oEventCB):
    iPerform = 0
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' in dMsgInfo:
        iPerform = dMsgInfo['Skill'].m_Base['pfid']
    elif 'pfid' in dMsgInfo:
        iPerform = dMsgInfo['pfid']
    clsPerform = cl_perform.GetPerformModule(iPerform)
    if not clsPerform:
        return 0
    dBaseArgData = clsPerform.m_BaseArgData
    iExplosive = dBaseArgData['Explosive'] if 'Explosive' in dBaseArgData else 0
    return iExplosive


def CheckDamIsExplosion(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if CheckExplosive(oEventCB):
        return True
    if 'RS' not in dMsgInfo:
        return False
    oReason = dMsgInfo['RS']
    if oReason.Query('Explosion') and oReason.Query('ActNum'):
        return True
    return False


def CBCheckCastingSkill(oListener, oEventCB, iPerform):
    if oListener.CheckCastingAndBackSwingByPF(iPerform):
        return 1
    return 0


def CheckPerformUnCrtByOwner(oListener, oEventCB):
    iPerform = 0
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' in dMsgInfo:
        iPerform = dMsgInfo['Skill'].m_Base['pfid']
    elif 'pfid' in dMsgInfo:
        iPerform = dMsgInfo['pfid']
    clsPerform = cl_perform.GetPerformModule(iPerform)
    if not clsPerform:
        return 0
    return clsPerform.m_UnCrtByOwnerSign


def CheckHasItem(oListener, oEventCB, iItem):
    if oListener.m_ItemCon.GetItemBySID(iItem):
        return 1
    return 0


def CheckConformKillMethod(oListener, oEventCB, iKillMethod):
    oHero = oListener
    oGame = oHero.m_Game
    if iKillMethod & KILL_INFO_ABNORMAL:
        dMsgInfo = oEventCB.GetCBMsgInfo()
        oMonster = oGame.GetObject(dMsgInfo['VID'])
        lstState = oMonster.m_State.Values()
        iCurAbnormal = 0
        for oState in lstState:
            if oState.m_SID in g_AllAbnormalStateSID:
                iCurAbnormal |= g_AllEleAbnormalState[oState.m_SID]
        
        if not iCurAbnormal & iKillMethod:
            return False
    if iKillMethod & KILL_INFO_DAM_TYPE:
        bExplosion = CheckDamIsExplosion(oHero, oEventCB)
        if iKillMethod == KILL_INFO_DAM_NOT_EXPLOSION and bExplosion:
            return False
        if iKillMethod == KILL_INFO_DAM_EXPLOSION and not bExplosion:
            return False
    if iKillMethod & DAM_MASK_ELEMENT:
        iCurDamType3 = GetEleDamType(oHero, oEventCB)
        if not iKillMethod & iCurDamType3:
            return False
    if iKillMethod & KILL_INFO_DAM3_TYPE:
        bWeakness = CheckHitWeakness(oHero, oEventCB)
        if iKillMethod == KILL_INFO_DAM3_NOT_WEAKNESS and bWeakness:
            return False
        if iKillMethod == KILL_INFO_DAM3_WEAKNESS and not bWeakness:
            return False
    SendAlert('err', '【回调检查符合击杀方式】设置了一个未被处理的常量 %s，请检查。' % iKillMethod)
    return False


def CountByKillInfo(dKillInfo, iKillMethod):
    if not dKillInfo:
        return 0
    dKillMonsterInfo = dKillInfo['dKillMonsterInfo']
    iRoundLimit = dKillInfo['RoundLimit']
    iTargetValue = dKillInfo['TargetValue']
    iCountResult = 0
    for iRound, dKillMonsterInfo2 in dKillMonsterInfo.items():
        if iRound < iRoundLimit:
            continue
        for iCurKillMethod, iKillValue in dKillMonsterInfo2.items():
            if iCurKillMethod & iKillMethod:
                iCountResult += iKillValue
                if iCountResult >= iTargetValue:
                    return iCountResult
        
    
    return iCountResult


def CheckDoubleEleDamEffect(oListener, oEventCB):
    return oListener.Query('DoubleDebuff', 0)


def CheckMonsterPhase(oListener, oEventCB, iPhase):
    if oListener.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
        return None
    if oListener.Phase() != iPhase:
        return 0
    return 1


def CheckCareerTrigger(oListener, oEventCB, dPfid):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    if 'pfid' not in dMsgInfo['Skill'].m_Custom:
        return 0
    if dMsgInfo['Skill'].m_Custom['pfid'] not in dPfid.values():
        return 0
    return 1


def CheckStateAddByIs(oListener, oEventCB, iCheckOwner = 0):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'AID' not in dMsgInfo:
        return 0
    iStateID = dEventInfo['StateID']
    oState = oListener.m_State.GetItem(iStateID)
    if not oState:
        return 0
    if oState.m_Attacker != dMsgInfo['AID']:
        if iCheckOwner:
            oAttack = oListener.m_Game.GetObject(dMsgInfo['AID'])
            if not oAttack or not (oAttack.m_Owner) or oAttack.m_Owner != oState.m_Attacker:
                return 0
        return 0
    return 1


def CheckStateFromFightType(oListener, oEventCB, iFightType):
    dEventInfo = oEventCB.GetCBEventInfo()
    oAttacker = oListener.m_Game.GetObject(dEventInfo['AID'])
    if 255 & iFightType:
        if oAttacker.m_FightType == iFightType:
            return 1
        return 0
    if oAttacker.m_FightType & iFightType == iFightType:
        return 1
    return 0


def CheckSkillCanUseTimes(oListener, oEventCB, iPerform):
    oPerform = oListener.m_Perform.GetPerform(iPerform)
    iBulletSID = oPerform.CalAttr('BulletSID')
    if not iBulletSID:
        return 0
    return oListener.m_BulletCon.m_Bullet[iBulletSID]


def GetSummonAttr(oListener, oEventCB, sAttr):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'summonId' not in dMsgInfo:
        SendAlert('err', '%s事件回调未设置召唤物Id' % oEventCB.m_Key)
        return 0
    oSummon = oListener.m_Game.GetObject(dMsgInfo['summonId'])
    if not oSummon:
        return 0
    return GetWarriorAttr(sAttr, oSummon)


def CheckSummonFightType(oListener, oEventCB, iFightType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'summonId' not in dMsgInfo:
        SendAlert('err', '%s事件回调未设置召唤物Id' % oEventCB.m_Key)
        return 0
    oSummon = oListener.m_Game.GetObject(dMsgInfo['summonId'])
    if not oSummon:
        return 0
    if oSummon.m_FightType & iFightType == iFightType:
        return 1
    return 0


def CheckTargetIsSelf(oListener, oEventCB):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    return iTarget == oListener.m_ID


def CheckAttackIsVictim(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'AID' not in dMsgInfo:
        return False
    if 'CurVID' in dMsgInfo:
        iVictim = dMsgInfo['CurVID']
    elif 'VID' in dMsgInfo:
        iVictim = dMsgInfo['VID']
    else:
        return False
    return dMsgInfo['AID'] == iVictim


def CheckCurrentPFAI(oListener, oEventCB, iTargetGroup):
    if not oListener.m_Agent:
        return 0
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if not oSkill.m_Custom.get('FromAI', False):
        return 0
    iGroup = oListener.m_Agent.m_PFAI.m_CurGroup
    return iGroup == iTargetGroup


def CheckCostBulletType(oListener, oEventCB, iBulletType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'SID' not in dMsgInfo:
        return False
    return dMsgInfo['SID'] == iBulletType


def CheckPickBulletType(oListener, oEventCB, iBulletType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Type' not in dMsgInfo or dMsgInfo['Type'] != NWARRIOR_DROP_BULLET:
        return 0
    if 'Item' not in dMsgInfo:
        return 0
    if iBulletType not in dMsgInfo['Item']:
        return 0
    return 1


def CheckTotalCureSource(oListener, oEventCB, iStateSID, iUseType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'MainCure' not in dMsgInfo:
        return 0
    lstChange = dMsgInfo['MainCure']
    if 'FlowCure' in dMsgInfo and dMsgInfo['FlowCure']:
        lstChange += dMsgInfo['FlowCure']
    for _iVal, oReason in lstChange:
        iSource = oReason.Query('SourceState')
        iDamType = oReason.Query('DamType')
        if iSource and iSource == iStateSID and iDamType & DAM_USE_ALL == iUseType:
            return 1
    
    return 0


def CheckTargetHasMark(oListener, oEventCB, sMark, iFromSelf):
    dTransInfo = oEventCB.GetCBTransInfo()
    oGame = oListener.m_Game
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    sKey = oEventCB.m_Key
    sPreFix = sKey.split('-', 1)[0]
    sFinalMark = '%s-%s' % (sPreFix, sMark)
    for iTarget in dTransInfo['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        lstMaskTarget = oTarget.Query(sFinalMark, [])
        if iFromSelf or lstMaskTarget:
            return 1
        for iMaskTarget in lstMaskTarget:
            if iMaskTarget == oListener.m_ID:
                return 1
        
    
    return 0


def GetPFBulletCount(oListener, oEventCB, iPerform):
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'ItemID' in dEventInfo:
        iWeapon = dEventInfo['ItemID']
    elif 'RS' in dEventInfo:
        iWeapon = dEventInfo['RS'].Query('Item')
    else:
        iWeapon = 0
    oPerform = oListener.GetPerform(iPerform, iWeapon)
    if oPerform and oPerform.m_PFType in (PF_TYPE_SHOOT, PF_TYPE_CONSHOOT, PF_TYPE_CHARGE):
        return oPerform.CurPFBullet()
    return 0


def GetEventWeaponPerformPFBulletCount(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ItemID' not in dMsgInfo:
        return 0
    iWeapon = dMsgInfo['ItemID']
    oWeapon = oListener.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return 0
    oPerform = oWeapon.GetPFBulletPerform()
    if oPerform:
        return oPerform.CurPFBullet()
    return 0


def GetEventWeaponPerformMaxPFBullet(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ItemID' not in dMsgInfo:
        if 'Skill' not in dMsgInfo:
            return 0
        if not dMsgInfo['Skill']:
            return 0
        oSkill = dMsgInfo['Skill']
        if 'ItemID' not in oSkill.m_Cache:
            return 0
        iWeapon = oSkill.m_Cache['ItemID']
    else:
        iWeapon = dMsgInfo['ItemID']
    oWeapon = oListener.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return 0
    oPerform = oWeapon.GetPFBulletPerform()
    if not oPerform:
        return 0
    return oPerform.MaxPFBullet()


def CheckRelicType(oListener, oEventCB, iType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'iPerform' in dMsgInfo:
        iRelic = dMsgInfo['iPerform']
    elif 'Relic' in dMsgInfo:
        iRelic = dMsgInfo['Relic']
    else:
        return 0
    iRelicType = cl_perform.GetPerformClassAttr(iRelic, 'm_RelicType')
    if iRelicType == iType:
        return 1
    return 0


def CheckRelicQuality(oListener, oEventCB, iQuality):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'iPerform' in dMsgInfo:
        iRelic = dMsgInfo['iPerform']
    elif 'Relic' in dMsgInfo:
        iRelic = dMsgInfo['Relic']
    else:
        return 0
    iRelicQuality = cl_perform.GetPerformClassAttr(iRelic, 'm_Quality')
    if iRelicQuality == iQuality:
        return 1
    return 0


def CheckMonsterIsPetrochemical(oListener, oEventCB):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTrans['TargetList']
    iTarget = lstTar[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return 0
    if oTarget.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER or not oTarget.IsPetrochemical():
        return 0
    return 1


def CheckReason(oListener, oEventCB, sReason, iCheckSplit = 0):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'RS' in dMsgInfo and dMsgInfo['RS']:
        sCheckReason = dMsgInfo['RS'].GetStrReason()
    elif 'Reason' in dMsgInfo:
        sCheckReason = dMsgInfo['Reason']
    else:
        return 0
    if iCheckSplit:
        sCheckReason = sCheckReason.split('-')[iCheckSplit - 1]
    if sReason == sCheckReason:
        return 1
    return 0


def CheckDropReason(oListener, oEventCB, iReason):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'DropReason' not in dMsgInfo:
        return 0
    if dMsgInfo['DropReason'] == iReason:
        return 1
    return 0


def CheckPointRelic(oListener, oEventCB, iPointRelic):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iRelicSID = 0
    if 'NewRelic' in dMsgInfo:
        iRelicSID = dMsgInfo['NewRelic']
    elif 'iPerform' in dMsgInfo:
        iRelicSID = dMsgInfo['iPerform']
    elif 'Relic' in dMsgInfo:
        iRelicSID = dMsgInfo['Relic']
    if iPointRelic == iRelicSID:
        return 1
    return 0


def CheckInPointRelic(oListener, oEventCB, dPointRelic):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iRelicSID = 0
    if 'NewRelic' in dMsgInfo:
        iRelicSID = dMsgInfo['NewRelic']
    elif 'iPerform' in dMsgInfo:
        iRelicSID = dMsgInfo['iPerform']
    elif 'Relic' in dMsgInfo:
        iRelicSID = dMsgInfo['Relic']
    if iRelicSID in dPointRelic:
        return 1
    return 0


def CheckInPointWand(oListener, oEventCB, dPointWand):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'WandSID' in dMsgInfo and dMsgInfo['WandSID'] in dPointWand:
        return 1
    return 0


def CheckWeaponNoDoubleHold(oListener, oEventCB):
    lstAdd = oListener.m_WieldCon.GetWeapons(itemdef.MAIN_HOLD)
    for oWeapon in lstAdd:
        if not oWeapon:
            return 0
        if oWeapon.m_CanDoubleHold == 0:
            return 1
    
    return 0


def CheckIsReduceBulletUse(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if 'NoBulletUse' in oSkill.m_Collect and oSkill.m_Collect['NoBulletUse']:
        return 1
    return 0


def CheckIsFinalLevel(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    return dMsgInfo['PassAll']


def CheckSettleType(oListener, oEventCB, iType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'SettleType' not in dMsgInfo:
        return False
    return dMsgInfo['SettleType'] == iType


def CheckWarPlayMode(oTarget, oEventCB, iCheckMode):
    return oTarget.m_Game.m_WarMgr.m_PlayMode == iCheckMode


def CheckTargetIsPointClasses(oListener, oEventCB, iType):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oGame = oListener.m_Game
    oTarget = oGame.GetObject(iTarget)
    if not oTarget:
        return 0
    if iType in oTarget.m_ClassifyList:
        return 1
    return 0


def CheckThrowBullet(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    iPerform = oSkill.m_Base['pfid']
    oPerform = oListener.m_Perform.GetPerform(iPerform)
    iBulletSID = oPerform.CalAttr('BulletSID')
    if iBulletSID == 0:
        return 0
    return 1


def CheckTriggerPerfromPfid(oListener, oEventCB, dPfid):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    if 'TriggerPerfrom' not in dMsgInfo['Skill'].m_Custom:
        return 0
    if dMsgInfo['Skill'].m_Custom['TriggerPerfrom'] not in dPfid.values():
        return 0
    return 1


def CheckIsPointButton(oListener, oEventCB, iClientButton):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'lstClientKey' not in dMsgInfo:
        return 0
    iKey = 0
    for iButton in dMsgInfo['lstClientKey']:
        iKey |= iButton
    
    if iKey == iClientButton:
        return 1
    return 0


def EventCBGetTargetStateRemainingTime(oListener, oEventCB, iState, iFromSelf):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return 0
    if not iFromSelf:
        oState = oTarget.m_State.GetItemBySID(iState)
        if not oState:
            return 0
        return Frame2Time(oState.GetRemainTime())
    lstState = oTarget.m_State.GetItems(iState)
    for oState in lstState:
        if oState.m_Attacker != oListener.m_ID:
            continue
        return Frame2Time(oState.GetRemainTime())
    
    return 0


def EventCBCheckFromPointState(oListener, oEventCB, iState):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iSourceState = 0
    if 'RS' in dMsgInfo:
        iSourceState = dMsgInfo['RS'].Query('SourceState', 0)
    if not iSourceState and 'StateSID' in dMsgInfo:
        iSourceState = dMsgInfo['StateSID']
    if iSourceState == iState:
        return 1
    return 0


def EventCBCheckInPointState(oListener, oEventCB, dState):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iState = dMsgInfo['StateSID'] if 'StateSID' in dMsgInfo else 0
    if not iState:
        SendAlert('err', '%s事件回调没有状态信息,请检查监听消息是否正确' % oEventCB.m_Key)
        return 0
    if iState in dState:
        return 1
    return 0


def EventCBCheekFormPointBehavior(oListener, oEventCB, iBehavior):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if dMsgInfo['Behavior'] == iBehavior:
        return 1
    return 0


def EventCBGetStateExistTime(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    return dMsgInfo.get('Time', 0)


def EventCBCheekDualReplaceWeapon(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Halt' in dMsgInfo:
        return 0
    return dMsgInfo['CanDoubleHold']


def CheckSummonSameWeaponSource(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'CurVID' not in dMsgInfo:
        return False
    iCurVID = dMsgInfo['CurVID']
    oVictim = oListener.m_Game.GetObject(iCurVID)
    if not oVictim or oVictim.m_FightType & WARRIOR_SUMMON != WARRIOR_SUMMON:
        return False
    iSrcWeapon = oVictim.m_SrcWeapon
    if not iSrcWeapon:
        return False
    if 'Skill' in dMsgInfo:
        iWeapon = dMsgInfo['Skill'].m_Base['Weapon']
    else:
        return False
    return iSrcWeapon == iWeapon


def CheckTargetSkillHitInfo(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return False
    oSkill = dMsgInfo['Skill']
    if 'lstAllVID' not in oSkill.m_Collect:
        return False
    if 'CurVID' not in dMsgInfo:
        return False
    lstAll = oSkill.m_Collect['lstAllVID']
    iCurVID = dMsgInfo['CurVID']
    if iCurVID in lstAll:
        return True
    return False


def EventCBCheckSkillRandomInRange(oListener, oEventCB, iMin, iMax):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return False
    oSkill = dMsgInfo['Skill']
    iRandom = oSkill.m_CacheData.m_Random
    if iMin <= iRandom and iRandom <= iMax:
        return True
    return False


def EventCBGetSkillCacheBallisticType(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oSkill = dMsgInfo['Skill']
    return oSkill.m_CacheData.GetBallisticType()


def EventCBCheckOpenSnipe(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oSkill = dMsgInfo['Skill']
    return oSkill.m_CacheData.IsOpenSnipe()


def EventCBCheckPerformMode(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oSkill = dMsgInfo['Skill']
    return oSkill.m_CacheData.GetPerformMode()


def EventCBCheckSkillCache(oListener, oEventCB, iIndex):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    return cl_perform.skillcache.GetSkillCacheByIndex(oSkill, iIndex)


def EventCBGetCurCrtData(oListener, oEventCB, sKey):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    dCartoon = oSkill.GetCurCartoon()
    if sKey not in dCartoon:
        return 0
    return dCartoon[sKey]


def EventCBGetCurCrtHitNum(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    dCartoon = oSkill.GetCurCartoon()
    if 'AllVLST' in dCartoon:
        return len(dCartoon['AllVLST'])
    if 'AllTarget' in dCartoon:
        return len(dCartoon['AllTarget'])
    return 0


def EventCBGetLeftGoodsNumAfterShopBuy(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iShopNpc = dMsgInfo['ShopNpc']
    oShopNpc = oListener.m_Game.GetObject(iShopNpc)
    dGoods = oShopNpc.m_GoodsData[oListener.m_ID]
    iLeft = 0
    for iPos, oGoods in dGoods.items():
        if oListener.m_BuyMgr.IsHidden(iPos, oGoods):
            continue
        if oGoods.m_HasBuy >= oGoods.m_CanBuy:
            continue
        iLeft += 1
    
    return iLeft


def CheckFromCareerPerform(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iPerform = 0
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        iPerform = oSkill.m_Base['pfid']
    elif 'pfid' in dMsgInfo:
        iPerform = dMsgInfo['pfid']
    oCareerPF = oListener.GetCareerPerform()
    iCareerPF = oCareerPF.m_SID
    if iPerform == iCareerPF:
        return True
    return False


def CheckFromThrowPerform(oListener, oEventCB, iAllThrow = 0):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iPerform = 0
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        iPerform = oSkill.m_Base['pfid']
    elif 'pfid' in dMsgInfo:
        iPerform = dMsgInfo['pfid']
    if not iAllThrow:
        oThrowPerform = oListener.GetThrowPerform()
        if oThrowPerform and iPerform == oThrowPerform.m_SID:
            return True
        return False
    dHero2HeroThrow = cl_hero.load.GetHero2HeroThrow()
    if oListener.m_SID not in dHero2HeroThrow:
        return False
    if iPerform not in dHero2HeroThrow[oListener.m_SID]:
        return False
    return True


def EventCBGetHitVictimCnt(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    iCur = 0
    if 'LastVLST' in oSkill.m_Update:
        iCur = len(oSkill.m_Update['LastVLST'])
    return iCur


def EventCBCheckChangeEnergyReason(oListener, oEventCB, iChangeReason):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Reason' not in dMsgInfo:
        return 0
    iReason = dMsgInfo['Reason']
    if iReason == iChangeReason:
        return 1
    return 0


def EventCBCheckTargetCDByMark(oListener, oEventCB, sMark, iUseOwner = 0):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    oGame = oListener.m_Game
    sKey = sMark + 'CDMark'
    iTarget = lstTar[0]
    oTarget = oGame.GetObject(iTarget)
    if not oTarget:
        return 0
    dMarkCDInfo = oTarget.Query(sKey, [])
    if not dMarkCDInfo:
        return 0
    (iRecordFrame, iFrame) = (0, 0)
    if iUseOwner and oListener.m_Owner:
        iRecodeID = oListener.m_Owner
    else:
        iRecodeID = oListener.m_ID
    if iRecodeID in dMarkCDInfo:
        (iRecordFrame, iFrame) = dMarkCDInfo[iRecodeID]
    iNowFrame = oListener.m_Game.GetFrameNum()
    if iRecordFrame + iFrame > iNowFrame:
        return 1
    return 0


def EventCBCheckTargetNoSourceCDByMark(oListener, oEventCB, sMark):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    oGame = oListener.m_Game
    sKey = sMark + 'NoSourceCDMark'
    iTarget = lstTar[0]
    oTarget = oGame.GetObject(iTarget)
    if not oTarget:
        return 0
    iTimeoutFrame = oTarget.Query(sKey, 0)
    if iTimeoutFrame == 0:
        return 0
    iNowFrame = oListener.m_Game.GetFrameNum()
    if iTimeoutFrame > iNowFrame:
        return 1
    return 0


def EventCBCheckPlayerInteractStatus(oListener, oEvent, iStatus):
    dMsgInfo = oEvent.GetCBMsgInfo()
    if 'InteractStatus' not in dMsgInfo:
        return False
    if iStatus == dMsgInfo['InteractStatus']:
        return True
    return False


def EventCBCheckGoodsIsPointItem(oListener, oEventCB, iType, iSID):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Type' not in dMsgInfo or 'SID' not in dMsgInfo:
        return False
    if iType != dMsgInfo['Type']:
        return False
    if iSID and iSID != dMsgInfo['SID']:
        return False
    return True


def EventCBCheckTriggerOwner(oListener, oEventCB):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    oGame = oListener.m_Game
    iTarget = lstTar[0]
    oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
    if not oTarget:
        return 0
    iOwner = oTarget.m_Owner
    if not iOwner:
        return 0
    oOwner = oGame.GetObject(iOwner, PY_FLAG_DEAD)
    if not oOwner:
        return 0
    return 1


def EventCBCheckTargetRealDead(oListener, oEventCB):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return 0
    return oTarget.IsRealDied()


def EventCBCheckUnLockNewSuit(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'SuitID' not in dMsgInfo:
        return False
    iSuit = dMsgInfo['SuitID']
    dUnlockSuit = oListener.Query('UnlockSuit', { })
    if iSuit not in dUnlockSuit:
        return True
    return False


def CheckEventWeaponHoldType(oListener, oEventCB, iType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iHoldType = 0
    if 'HoldType' in dMsgInfo:
        iHoldType = dMsgInfo['HoldType']
    elif 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        if 'HoldType' in oSkill.m_Cache:
            iHoldType = oSkill.m_Cache['HoldType']
        elif 'ActNum' in dMsgInfo:
            iActNum = dMsgInfo['ActNum']
            oSkill = oListener.m_Game.m_SkillMgr.GetSkill(oListener.m_ID, iActNum)
            if oSkill and 'HoldType' in oSkill.m_Cache:
                iHoldType = oSkill.m_Cache['HoldType']
            elif 'ItemID' in dMsgInfo:
                oWeapon = oListener.m_WieldCon.GetItemByID(dMsgInfo['ItemID'])
                if oWeapon:
                    iHoldType = oWeapon.GetComponent('Hold').HoldPos()
    if None == iType:
        return 1
    return 0


def CheckCBCheckShopType(oListener, oEventCB, dType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ShopNpc' not in dMsgInfo or 'Type' not in dMsgInfo:
        return 0
    iType = dMsgInfo['Type']
    if iType in dType:
        return 1
    return 0


def CheckEventRecycleDropType(oListener, oEventCB, iType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'RecycleDropType' not in dMsgInfo:
        return 0
    iRecycleDrop = dMsgInfo['RecycleDropType']
    if iRecycleDrop == iType:
        return 1
    return 0


def CheckDamageIsSourceWeapon(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if 'ItemID' not in oSkill.m_Cache:
        return 0
    dEventInfo = oEventCB.GetCBEventInfo()
    return dEventInfo['ItemID'] == oSkill.m_Cache['ItemID']


def GetComb(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iComb = 0
    if 'Comb' in dMsgInfo and dMsgInfo['Comb']:
        iComb = dMsgInfo['Comb']
    elif oListener.m_SID == GAMBLER_HERO:
        iComb = oListener.m_GamblerCon.GetComb()
    return iComb


def EventCBCheckQuality(oListener, oEventCB, iQuality):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iEventQuality = 0
    if 'Quality' in dMsgInfo:
        iEventQuality = dMsgInfo['Quality']
    elif 'Skill' in dMsgInfo:
        iEventQuality = dMsgInfo['Skill'].m_Collect['Quality']
    if iEventQuality == iQuality:
        return 1
    return 0


def EventCBCheckReenter(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'reenter' in dMsgInfo:
        return dMsgInfo['reenter']
    return 0


def CheckIsShareDamage(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'RS' not in dMsgInfo:
        return 0
    if dMsgInfo['RS'].Query('DamShare'):
        return 1
    return 0


def CheckTalentChooseAll(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ChooseAll' not in dMsgInfo:
        return 0
    if 'NpcID' not in dMsgInfo:
        return 0
    iNpcID = dMsgInfo['NpcID']
    sKey = GetCommonEventKey(oEventCB.GetCBEventInfo())
    iOldNpcID = oListener.Query('%sNpcID' % sKey, 0)
    if iNpcID == iOldNpcID:
        return 0
    oListener.Set('%sNpcID' % sKey, iNpcID)
    return 1


def CheckPlayerLinkStatus(oListener, oEventCB, iStatus, iIncludeSelf = 0):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'LinkStatus' not in dMsgInfo or 'Hero' not in dMsgInfo:
        return 0
    if iStatus == dMsgInfo['LinkStatus']:
        if not iIncludeSelf and dMsgInfo['Hero'] == oListener.m_ID:
            return 0
        return 1
    return 0


def EventCBSetDefaultSavedData(oListener, oEventCB, sFlag, iDefault, iUseFormula):
    sKey = 'save.' + sFlag
    iValue = oListener.QuerySavedData(sKey, None)
    if iValue is None:
        if iUseFormula:
            iDefault = cl_formula.GetResultByData(oListener, iDefault, { }, oEventCB.GetCBMsgInfo())
        oListener.SetSavedData(sKey, iDefault)
        return iDefault
    return iValue


def EventCBCheckAtiveExplosion(oListener, oEventCB):
    if not oListener.m_FightType & WARRIOR_HERO:
        return 0
    iServant = oListener.m_Servant
    if not iServant:
        return 0
    oServant = oListener.m_Game.GetObject(iServant)
    if oServant and oServant.Query('CanExplosion'):
        return 1
    return 0


def EventCBCheckWeaponTypeInCache(oListener, oEventCB, iType, iIndex):
    if iIndex not in [
        SKILLCACHE_LSTINT,
        SKILLCACHE_LSTINTSPECIAL]:
        return 0
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    lstCache = cl_perform.skillcache.GetSkillCacheByIndex(oSkill, iIndex)
    if not lstCache:
        return 0
    if iType not in lstCache:
        return 0
    return 1


def EventCBGetCareerPerformUsable(oListener, oEventCB):
    if not oListener.m_FightType & WARRIOR_HERO:
        return 0
    iPerform = oListener.GetCareerPerformID()
    if not iPerform:
        return 0
    oPerformcon = oListener.m_Perform
    return oPerformcon.GetCover(iPerform)


def EventCBGetSpawnGroup(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Group' not in dMsgInfo:
        return 0
    return dMsgInfo['Group']


def EventCBGetMonsterGroupLiveCount(oListener, oEventCB, iGroup):
    oGame = oListener.m_Game
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    oLineNode = oLevelCtrl.GetLineNode(oListener.m_LineIdx)
    if not oLineNode:
        return 0
    oMonsterCtrl = oLineNode.m_MonsterCtrl
    if iGroup not in oMonsterCtrl.m_GroupInfo:
        return 0
    dGroup = oMonsterCtrl.m_GroupInfo[iGroup]
    return len(dGroup['Live'])


def EventCBCheckSwitchWeaponType(oListener, oEventCB, iType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ItemType' not in dMsgInfo:
        return 0
    if dMsgInfo['ItemType'] != iType:
        return 0
    return 1


def EventCBCheckTaskStatus(oListener, oEventCB, iStatus):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Status' not in dMsgInfo:
        return 0
    if dMsgInfo['Status'] == iStatus:
        return 1
    return 0


def EventCBCheckOrderTaskRunning(oListener, oEventCB, dTask):
    if not dTask:
        SendAlert('err', '%s事件回调未设置指定任务列表' % oEventCB.m_Key)
        return None
    tTaskSID = tuple(dTask.keys())
    iCnt = oListener.m_TaskCon.GetRunningTaskCntBySID(tTaskSID)
    if iCnt > 0:
        return 1
    return 0


def EventCBCheckLevelGoal(oListener, oEventCB):
    oGame = oListener.m_Game
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    oScene = oGame.m_SceneMgr.GetScene(oListener.m_Scene)
    if oScene:
        oLevelNode = oLevelCtrl.GetLevelNode(oScene.m_Level)
        if oLevelNode and oLevelNode.m_Status == LEVEL_STATUS_GOAL:
            return 1
    return 0


def EventCBCheckIsMonsterGroup(oListener, oEventCB, dMonster):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTransInfo['TargetList']
    if not lstTar:
        return 0
    oMonster = oListener.m_Game.GetObject(lstTar[0], PY_FLAG_DEAD)
    if not oMonster:
        return 0
    if oMonster.m_SID not in dMonster:
        return 0
    return 1


def EventCBCheckItemMode(oListener, oEventCB, iMode):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Mode' not in dMsgInfo or 'Status' not in dMsgInfo or dMsgInfo['Mode'] != iMode:
        return 0
    return dMsgInfo['Status']


def EventCBCheckWeaponModeByHoldType(oListener, oEventCB, iHoldType, iMode):
    lstItem = oListener.m_WieldCon.GetWeapons(iHoldType)
    if not lstItem:
        return 0
    iStatus = 0
    for oItem in lstItem:
        iStatus = oItem.GetModeStatus(iMode)
        if iStatus:
            break
    
    return iStatus


def EventCBCheckTalentGrade(oListener, oEventCB, iChangeTrend, iOldLevel, iNewLevel, iSituation):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Level' not in dMsgInfo or 'CurLevel' not in dMsgInfo:
        return False
    iCurLevel = dMsgInfo['CurLevel']
    iLevel = dMsgInfo['Level']
    if iLevel == iCurLevel:
        return False
    if iChangeTrend == TALENT_GRADE_ADD or iLevel < iCurLevel:
        return False
    if iChangeTrend == TALENT_GRADE_REDUCE and iLevel > iCurLevel:
        return False
    if iSituation == TALENT_GRADE_IGNORE_ALL:
        return True
    if iSituation == TALENT_GRADE_IGNORE_OLDLEVEL or iLevel == iNewLevel:
        return True
    if iSituation == TALENT_GRADE_IGNORE_NEWLEVEL or iCurLevel == iOldLevel:
        return True
    if iSituation == TALENT_GRADE_IGNORE_NOTHING and iCurLevel == iOldLevel and iLevel == iNewLevel:
        return True
    return False


def EventCBCheckCommonTalent(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'iPerform' not in dMsgInfo:
        return False
    oWarMgr = oListener.m_Game.m_WarMgr
    oTalentFusionElement = oWarMgr.GetComponent('TalentFusionElement')
    if not oTalentFusionElement:
        return False
    return oTalentFusionElement.CheckIsCommonTalent(oListener, dMsgInfo['iPerform'])


def EventCBCheckRelicFromMonsterRelicElement(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'NewRelic' not in dMsgInfo or 'SourceReason' not in dMsgInfo:
        return False
    dElementReason = dMsgInfo['SourceReason']
    if 'Mode' not in dElementReason:
        return False
    oWarMgr = oListener.m_Game.m_WarMgr
    oMonsterRelicElement = oWarMgr.GetComponent('MonsterRelicElement')
    if not oMonsterRelicElement:
        return False
    iMode = dElementReason['Mode']
    return iMode == SOURCE_REASON_MODE_MONSTERRELIC


def EventCBCheckGoodsTypeInReward(oListener, oEventCB, iGoodsType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'GoodsMenu' not in dMsgInfo:
        return False
    dGoodsMenu = dMsgInfo['GoodsMenu']
    if not dGoodsMenu:
        return False
    for _, oGood in dGoodsMenu.items():
        if oGood.m_GoodsType == iGoodsType:
            return True
    
    return False


def EventCBCheckGoodsType(oListener, oEventCB, iGoodsType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Type' not in dMsgInfo:
        return False
    return dMsgInfo['Type'] == iGoodsType


def EventCBCheckBreakFlaw(oListener, oEventCB, iPreCal = 0):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'BreakFlaw' in dMsgInfo:
        return dMsgInfo['BreakFlaw']
    if iPreCal and oListener.m_SID == EXECUTOR_HERO:
        return oListener.m_FlawCon.CheckPreBreakFlaw(dMsgInfo)
    return 0


def EventCBGetRecordQueueCnt(oListener, oEventCB):
    sKey = '%sRecordQueue' % oEventCB.m_Key
    dRecordQueue = oListener.Query(sKey, { })
    iCurFrame = oListener.m_Game.GetFrameNum()
    iCnt = 0
    bChange = False
    dQueue = { }
    for iKey, iLastFrame in dRecordQueue.items():
        if iLastFrame and iLastFrame < iCurFrame:
            bChange = True
            continue
        dQueue[iKey] = iLastFrame
        iCnt += 1
    
    if bChange:
        oListener.Set(sKey, dQueue)
    return iCnt


def CheckDropOwner(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'VID' not in dMsgInfo:
        return False
    iAttachID = dMsgInfo['VID']
    oDrop = oListener.m_Game.GetObject(iAttachID)
    if not oDrop or not (oDrop.m_FightType & NWARRIOR_DROP):
        return False
    return oDrop.m_Owner == oListener.m_ID


def EventCBGetTargetCustomData(oListener, oEventCB, sKey):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTransInfo['TargetList']
    if not lstTar:
        return 0
    oGame = oListener.m_Game
    oTarget = oGame.GetObject(lstTar[0])
    if not oTarget:
        return 0
    return oTarget.Query(sKey)


def EventCBAddVictimHitCount(oListener, oEventCB, iAdd):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTransInfo['TargetList']
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if not lstTar or 'Skill' not in dMsgInfo or not dMsgInfo['Skill']:
        return 0
    oGame = oListener.m_Game
    oTarget = oGame.GetObject(lstTar[0])
    if not oTarget:
        return 0
    oSkill = dMsgInfo['Skill']
    sFlag = '%d-%dhitcount' % (oSkill.m_Base['AID'], oSkill.m_Base['pfid'])
    iCount = oTarget.Query(sFlag, 0)
    oTarget.Set(sFlag, iCount + iAdd)
    return iCount


def EventCBGetTargetAbnormalStateNum(oListener, oEventCB):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    iTarget = dTransInfo['TargetList'][0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return 0
    iResult = 0
    for iState in g_AllAbnormalStateSID:
        if not oTarget.m_State.GetItemBySID(iState):
            continue
        iResult += 1
    
    return iResult


def EventCBCheckItemRefreshAttribute(oListener, oEventCB, sAttr):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'RefreshAttribute' not in dMsgInfo:
        return False
    return dMsgInfo['RefreshAttribute'] == sAttr


def EventCBGetTargetCustomDataRemainTime(oListener, oEventCB, sKey, iAppendListener = 0):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTransInfo['TargetList']
    if not lstTar:
        return 0
    oGame = oListener.m_Game
    oTarget = oGame.GetObject(lstTar[0])
    if not oTarget:
        return 0
    if iAppendListener:
        sKey = '%s-%d' % (sKey, oListener.m_ID)
    dCustomData = oTarget.Query(sKey, { })
    if not dCustomData:
        return 0
    iCurFrame = oGame.GetFrameNum()
    iRemainTime = 0
    for iLastFrame in dCustomData.values():
        iRemainFrame = iLastFrame - iCurFrame
        if iRemainFrame > 0:
            iRemainTime = Frame2Time(iRemainFrame)
    
    return iRemainTime


def EventCBGetVictimHitNumberInCollect(oListener, oEventCB, iSuffix):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return -1
    oSkill = dMsgInfo['Skill']
    iTarget = 0
    if 'CurVID' in dMsgInfo:
        iTarget = dMsgInfo['CurVID']
    elif 'VID' in dMsgInfo:
        iTarget = dMsgInfo['VID']
    else:
        iTarget = oSkill.m_Base['VID']
        if not iTarget and 'CurVID' in oSkill.m_Update:
            iTarget = oSkill.m_Update['CurVID']
    if not iTarget:
        return -1
    sSuffix = oEventCB.m_Key if iSuffix else ''
    dHitInfo = oSkill.GetHitTarget(sSuffix)
    if iTarget in dHitInfo:
        return dHitInfo[iTarget]
    return 0


def EventCBGetTargetHitNumberInCollect(oListener, oEventCB, iSuffix):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return -1
    oSkill = dMsgInfo['Skill']
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return -1
    lstTar = dTrans['TargetList']
    if not lstTar:
        return -1
    iTarget = lstTar[0]
    sSuffix = oEventCB.m_Key if iSuffix else ''
    dHitInfo = oSkill.GetHitTarget(sSuffix)
    if iTarget in dHitInfo:
        return dHitInfo[iTarget]
    return -1


def EventCBGetSkillCustomInfo(oListener, oEventCB, sAttr):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if sAttr not in oSkill.m_Custom:
        return 0
    return oSkill.m_Custom[sAttr]


def CheckKeyInReason(oListener, oEventCB, sKey):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Reason' in dMsgInfo and sKey in dMsgInfo['Reason']:
        return 1
    return 0


def EventCBCheckFullRelicTalent(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    return dMsgInfo['FullPF']


def EventCBCheckAddImmobilize(oListener, oEventCB):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oGame = oListener.m_Game
    oTarget = oGame.GetObject(iTarget)
    if not oTarget:
        return 0
    return oTarget.IsImmobilize()


def EventCBCheckChangeSuitNum(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    return dMsgInfo.get('Change', False)


def EventCBCheckDamageHasTag(oListener, oEventCB, sTag):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'RS' not in dMsgInfo:
        return 0
    oReason = dMsgInfo['RS']
    dInfo = oReason.Query('OtherInfo', { })
    if dInfo and sTag in dInfo:
        return 1
    return 0


def CheckEventWeapon(oListener, oEventCB, dWeapon):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iItem = 0
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        iItem = oSkill.m_Base['Weapon'] if 'Weapon' in oSkill.m_Base else 0
    elif 'ItemID' in dMsgInfo:
        iItem = dMsgInfo['ItemID']
    elif 'ReplaceID' in dMsgInfo:
        iItem = dMsgInfo['ReplaceID']
    if not iItem:
        return 0
    oWeapon = oListener.m_WieldCon.GetItemByID(iItem)
    if not oWeapon:
        return 0
    return oWeapon.m_SID in dWeapon


def EventCBGetRelicLevel(oListener, oEventCB, iCBCheckChange = 0):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if iCBCheckChange and 'RelicDropLevel' in dMsgInfo:
        iLevel = dMsgInfo['RelicDropLevel']
    elif 'Level' in dMsgInfo:
        pass
    
    iLevel = 0
    return iLevel


def EventCBGetTargetFlawCount(oListener, oEventCB):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    dFlaw = oListener.m_FlawCon.GetFlaw(iTarget)
    if not dFlaw:
        return 0
    return len(dFlaw)


def EventCBGetTargetFlawMaxCount(oListener, oEventCB):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return 0
    return oListener.m_FlawCon.GetFlawMaxCount(oTarget)


def EventCBCheckHitFlaw(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo or 'AID' not in dMsgInfo or 'CurVID' not in dMsgInfo:
        return False
    oSkill = dMsgInfo['Skill']
    if 'CurHitArea' not in oSkill.m_Update or oSkill.m_Update['CurHitArea'] != MONSTER_PART_FLAW:
        return False
    oAttack = oListener.m_Game.GetObject(dMsgInfo['AID'])
    if not oAttack or oAttack.m_SID != EXECUTOR_HERO:
        return False
    if oAttack.m_FlawCon.GetSkillHitFlaw(oSkill, dMsgInfo['CurVID']):
        return True
    return False


def EventCBCheckChooseAll(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ChooseAll' not in dMsgInfo:
        return 0
    return dMsgInfo['ChooseAll']


def EventCBCheckAmuletPerform(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if 'Amulet' in oSkill.m_Cache:
        return 1
    iWeapon = oSkill.m_Base['Weapon']
    oWeapon = oListener.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return 0
    return oWeapon.CheckWeaponType2(itemdef.EQUIP_TYPE_AMULET)


def EventCBCheckFromWeaponPFBulletPerform(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if not oSkill.m_Base['Weapon']:
        return 0
    iWeapon = oSkill.m_Base['Weapon']
    oWeapon = oListener.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return 0
    oPFBulletPerform = oWeapon.GetPFBulletPerform()
    if not oPFBulletPerform or oSkill.m_Base['pfid'] != oPFBulletPerform.m_SID:
        return 0
    return 1


def EventCBCheckSmithExtraCost(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'NpcID' not in dMsgInfo:
        return 0
    iNPCID = dMsgInfo['NpcID']
    oTarget = oListener.m_Game.GetObject(iNPCID)
    if not oTarget:
        return 0
    iEnable = oListener.Query('WeaponExtraUpgradeCostEnable', 0)
    if not iEnable:
        return 0
    dCost = oListener.Query('WeaponExtraUpgradeCost', { })
    if oTarget.m_ID in dCost:
        return 1
    return 0


def EventCBCheckTalent(oListener, oEventCB, iTalent):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'iPerform' not in dMsgInfo:
        return False
    return dMsgInfo['iPerform'] == iTalent


def EventCBCheckVictimForSelf(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'CurVID' in dMsgInfo:
        iVictim = dMsgInfo['CurVID']
    elif 'VID' in dMsgInfo:
        iVictim = dMsgInfo['VID']
    else:
        return False
    return iVictim == oListener.m_ID


def EventCBCheckDamageBuffByBarrier(oListener, oEventCB, iFromSelf):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return False
    oSkill = dMsgInfo['Skill']
    if 'PassCrtBuff' in oSkill.m_Custom:
        lstBuff = oSkill.m_Custom['PassCrtBuff']
        if iFromSelf:
            iBarrier = oListener.GetDeviceID()
            if iBarrier in lstBuff:
                return True
        for iBuffSourceID in lstBuff:
            oBuff = oSkill.m_Game.GetObject(iBuffSourceID)
            if not oBuff:
                continue
            if oBuff.m_FightType == WARRIOR_DEVICE_BARRIER:
                return True
        
    if 'PFBuff' not in oSkill.m_Update:
        return False
    if 'CurVID' in dMsgInfo:
        iVictim = dMsgInfo['CurVID']
    elif 'VID' in dMsgInfo:
        iVictim = dMsgInfo['VID']
    else:
        return False
    dBuff = oSkill.m_Update['PFBuff']
    if iVictim not in dBuff:
        return False
    lstBuff = dBuff[iVictim]
    if iFromSelf:
        iBarrier = oListener.GetDeviceID()
        return iBarrier in lstBuff
    for iBuffSourceID in lstBuff:
        oBuff = oSkill.m_Game.GetObject(iBuffSourceID)
        if not oBuff:
            continue
        if oBuff.m_FightType == WARRIOR_DEVICE_BARRIER:
            return True
    
    return False


def CheckWeaponHasMinorPeform(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        if 'MinorPerform' not in oSkill.m_Cache:
            return False
        iMinorPerform = oSkill.m_Cache['MinorPerform']
        if iMinorPerform:
            return True
    if 'EquipSID' in dMsgInfo:
        iWeapon = dMsgInfo['EquipSID']
        clsWeapon = cl_item.GetItemCls(iWeapon)
        if not clsWeapon:
            return False
        dPerform = clsWeapon.m_ComponentAttr['Perform']
        if 'MinorPerform' in dPerform and dPerform['MinorPerform']:
            return True
    return False


def CheckDeviceCompType(oListener, oEventCB, iType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'DeviceCompType' in dMsgInfo:
        return dMsgInfo['DeviceCompType'] == iType
    return False


def CheckDeviceCompHasExcludeComp(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ExcludeComp' not in dMsgInfo:
        return False
    if not dMsgInfo['ExcludeComp']:
        return False
    return True


def GetDeviceCompEnbleType(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Enable' in dMsgInfo:
        return dMsgInfo['Enable']
    return -1


def CheckSelfDeviceInRaycastRange(oListener, oEventCB, iRange):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Cartoon' not in dMsgInfo:
        return False
    dCartoon = dMsgInfo['Cartoon']
    vDir = dCartoon['Dir']
    vStart = dCartoon['MuzzlePos']
    vEnd = cl_math.Vec3DisplaceDir(vStart, vDir, iRange)
    lstVictim = oListener.m_Game.Scene_RaycastMultiple(oListener.m_Scene, vStart, vEnd, PXMASK_BARRIER)
    if not lstVictim:
        return False
    oDevice = oListener.GetDevice()
    iDeviceID = oDevice.m_ID
    for iVictim, dHit in lstVictim:
        if not iVictim == iDeviceID:
            if iVictim in oDevice.m_SummonDict:
                return True
    
    return False


def EventCBCheckDealTotalDamFromDevice(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    return 'DeviceSourceID' in dMsgInfo


def EventCBCheckToxicState(oListener, oEventCB):
    if oListener.m_FightType & WARRIOR_DEVICE:
        oDevice = oListener
    elif oListener.m_FightType & WARRIOR_HERO:
        oDevice = oListener.GetDevice()
    else:
        return False
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'CurVID' in dMsgInfo:
        iTarget = dMsgInfo['CurVID']
    elif 'VID' in dMsgInfo:
        iTarget = dMsgInfo['VID']
    elif 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        iTarget = oSkill.m_Base['VID']
        if not iTarget and 'CurVID' in oSkill.m_Update:
            iTarget = oSkill.m_Update['CurVID']
        else:
            SendAlert('err', '%s回调检查受击者拥有来源自身装置毒气状态未获取到受击者' % oEventCB.m_Key)
            return False
    iDevice = oDevice.m_ID
    oPerfrom = oDevice.GetPerform(TOXIC_FOG)
    if not oPerfrom:
        return False
    iToxicState = oPerfrom.GetArgValue('ToxicStateSID')
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return False
    oToxicState = oTarget.m_State.GetItemBySource(iToxicState, iDevice)
    if oToxicState:
        return True
    return False


def EventCBCheckTriggerSameWeapon(oListener, oEventCB):
    dEventInfo = oEventCB.GetCBEventInfo()
    iPFItem = 0
    if 'ItemID' in dEventInfo:
        iPFItem = dEventInfo['ItemID']
    elif 'RS' in dEventInfo:
        oReason = dEventInfo['RS']
        iPFItem = oReason.Query('Item', 0)
    if not iPFItem:
        return 0
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if 'TriggerWeaponID' not in oSkill.m_Collect:
        return 0
    if oSkill.m_Collect['TriggerWeaponID'] != iPFItem:
        return 0
    return 1


def CheckTargetInInkArea(oListener, oEventCB):
    if oListener.m_SID != INKMASTER_HERO:
        return 0
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    oInkCon = oListener.m_InkCon
    return oInkCon.CheckTargetInInkArea(lstTar[0])


def EventCBCheckDamSign(oListener, oEventCB, sSign):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dDamSign = { }
    if 'Skill' in dMsgInfo and 'DamSign' in dMsgInfo['Skill'].m_Collect:
        dDamSign = dMsgInfo['Skill'].m_Collect['DamSign']
    if not dDamSign and 'RS' in dMsgInfo:
        oReason = dMsgInfo['RS']
        dDamSign = oReason.Query('DamSign', { })
    return sSign in dDamSign


def EventCBCheckDamageBuffBySummonFormPointPerform(oListener, oEventCB, iPointPerform):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return False
    oSkill = dMsgInfo['Skill']
    if 'PFBuff' not in oSkill.m_Update:
        return False
    if 'CurVID' in dMsgInfo:
        iVictim = dMsgInfo['CurVID']
    elif 'VID' in dMsgInfo:
        iVictim = dMsgInfo['VID']
    else:
        return False
    dBuff = oSkill.m_Update['PFBuff']
    if iVictim not in dBuff:
        return False
    lstBuff = dBuff[iVictim]
    for iBuffSourceID in lstBuff:
        oBuff = oSkill.m_Game.GetObject(iBuffSourceID)
        if not oBuff:
            continue
        if oBuff.m_FightType & WARRIOR_SUMMON != WARRIOR_SUMMON:
            continue
        if oBuff.m_SrcPerform == iPointPerform:
            return True
    
    return False


def EventCBCheckMoveDis(oListener, oEventCB, sBaseKey, iObjectType):
    oWarrior = oListener.GetOwnObject(iObjectType)
    if not oWarrior:
        SendAlert('err', '%s 回调检查移动距离变化 没找到对象' % oEventCB.m_Key)
        return False
    sKey = 'MoveDis%s' % sBaseKey
    tLast = oWarrior.Query(sKey, None)
    if not tLast:
        return True
    (vLast, _) = tLast
    if not cl_math.IsEqual(vLast, oWarrior.GetPos()):
        return True
    return False


def EventCBCheckAutoRecycle(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'AutoRecycle' in dMsgInfo:
        return 1
    return 0


def EventCBCheckFirstGetRelic(oListener, oEventCB):
    iPlayerID = oListener.m_PlayerID
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'OwnerInfo' in dMsgInfo and iPlayerID in dMsgInfo['OwnerInfo']:
        return 0
    return 1


def EventCBCheckTargetHasElementState(oListener, oEventCB, dStateSID, bHasAll = False):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return False
    lstTar = dTrans['TargetList']
    if not lstTar:
        return False
    iTarget = lstTar[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return False
    for iStateSID in dStateSID:
        bHasState = oTarget.m_State.HasState(iStateSID)
        if not bHasAll or bHasState:
            return False
        if bHasState:
            return True
    
    if bHasAll:
        return True
    return False


def EventCBCheckLoading(oListener, oEventCB):
    if oListener.Query('Loading', 0):
        return 1
    return 0


def EventCBCheckTargetBeExecuted(oListener, oEventCB):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return False
    lstTar = dTrans['TargetList']
    if not lstTar:
        return False
    iTarget = lstTar[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return False
    return oListener.m_FlawCon.CheckMonsterBeExecuted(oTarget)


def EventCBCheckVirtualArea(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'VirtualArea' not in dMsgInfo or not dMsgInfo['VirtualArea']:
        return 0
    return 1


def EventCBCheckModifyInkValue(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Modify' not in dMsgInfo:
        return 0
    return dMsgInfo['Modify']


def EventCBCheckSelfSameLevel(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Level' in dMsgInfo:
        iLevel = dMsgInfo['Level']
    elif 'LineIdx' in dMsgInfo and dMsgInfo['LineIdx']:
        iLevel = dMsgInfo['LineIdx'][0]
    else:
        return 0
    tLineIdx = oListener.m_LineIdx
    if tLineIdx or iLevel != tLineIdx[0]:
        return 0
    oScene = oListener.m_Game.m_SceneMgr.GetScene(oListener.m_Scene)
    if not oScene:
        return 0
    if iLevel != oScene.m_Level:
        return 0
    return 1


def EventCBCheckTargetIsDevil(oListener, oEventCB):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return False
    lstTar = dTrans['TargetList']
    if not lstTar:
        return False
    iTarget = lstTar[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if oTarget and oTarget.Query('Demon'):
        return True
    return False


def EventCBCheckPerformIsPetPerformType(oListener, oEventCB, dType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if 'PFSubType' not in oSkill.m_Cache:
        return 0
    if oSkill.m_Cache['PFSubType'] not in dType:
        return 0
    return 1


def GetTargetWarCash(oListener, oEventCB):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return 0
    if oTarget.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
        return 0
    return oTarget.Cash()


def EventCBCheckTargetIsLive(oListener, oEventCB):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    oGame = oListener.m_Game
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
    if not oTarget:
        return 0
    return 1


def EventCBCheckAssistKill(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iNowFrame = oListener.m_Game.GetFrameNum()
    oTarget = oListener.m_Game.GetObject(dMsgInfo['VID'])
    if not oTarget:
        return 0
    iLastFrame = oTarget.Query('Injured%d' % oListener.m_ID)
    if not iLastFrame or iLastFrame + oTarget.m_AssistKillFrame < iNowFrame:
        return 0
    return 1


def EventCBCheckInPointExecute(oListener, oEventCB, dExecuteType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ExecutType' not in dMsgInfo:
        return 0
    iType = dMsgInfo['ExecutType']
    iResult = 0
    for iExecuteType in dExecuteType:
        if iExecuteType & iType:
            iResult = 1
            break
    
    return iResult


def EventCBCheckTargetPetAbilityNumByQualityType(oListener, oEventCB, dQualityType):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    oTargetPet = oListener.m_Game.GetObject(lstTar[0])
    if not oTargetPet:
        return 0
    return oTargetPet.m_AbilityCon.GetAbilityNumByQualityType(dQualityType)


def EventCBGetConquerSpendTime(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    return dMsgInfo['SpendTime']


def EventCBCheckWeaponElementType(oListener, oEventCB, sExcludeReason, iHoldType, iElementType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if sExcludeReason in dMsgInfo['Reason']:
        return 0
    if dMsgInfo['HoldType'] != iHoldType:
        return 0
    if iElementType and not (iElementType & dMsgInfo['ElementType']):
        return 0
    return 1


def EventCBGetVictimScanCount(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if 'ScanInfo' not in oSkill.m_Collect:
        return 0
    if 'CurVID' in dMsgInfo:
        iVictim = dMsgInfo['CurVID']
    elif 'VID' in dMsgInfo:
        iVictim = dMsgInfo['VID']
    else:
        return 0
    dScanInfo = oSkill.m_Collect['ScanInfo']
    if iVictim not in dScanInfo:
        return 0
    return dScanInfo[iVictim]


def CheckTargetPetPointBaseMonster(oListener, oEventCB, iMonsterSID):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s回调检查目标妖灵为指定基础怪物 事件未获取目标' % oEventCB.m_Key)
        return 0
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oGame = oListener.m_Game
    oTarget = oGame.GetObject(iTarget)
    if not oTarget or not (oTarget.m_FightType & WARRIOR_PET):
        return 0
    return oTarget.m_MonsterDataSID == iMonsterSID


def CheckPerformIsInkPerform(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if oSkill.m_Base['pfid'] not in INKPERFORM:
        return 0
    return 1


def CheckHandlePetSameType(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oMainPet = oListener.m_PetCon.GetPetByID(dMsgInfo['MainPet'])
    if not oMainPet:
        return 0
    oDeputyPet = oListener.m_PetCon.GetPetByID(dMsgInfo['DeputyPet'])
    if not oDeputyPet:
        return 0
    if oMainPet.m_PetType != oDeputyPet.m_PetType:
        return 0
    return 1


def CheckHandlePetChosenNewPet(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if dMsgInfo['ChosenPos'] != FUSE_MAIN_POS:
        return 1
    return 0


def CheckEventPlayerIsLiveFirst(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oWarMgr = oListener.m_Game.m_WarMgr
    lstPlayer = oWarMgr.GetLivePlayer(iCalAI = 0)
    if not lstPlayer:
        return 0
    if dMsgInfo['Player'] != lstPlayer[0]:
        return 0
    return 1


def GetWeaponPerformPFBulletCountByHoldType(oListener, oEventCB, iHoldType):
    oItem = oListener.m_WieldCon.GetCurWeapon(iHoldType)
    if oItem:
        oPerform = oItem.GetPFBulletPerform()
        if oPerform:
            return oPerform.CurPFBullet()
    return 0


def GetWeaponPerformMaxPFBulletByHoldType(oListener, oEventCB, iHoldType):
    oItem = oListener.m_WieldCon.GetCurWeapon(iHoldType)
    if oItem:
        oPerform = oItem.GetPFBulletPerform()
        if oPerform:
            return oPerform.MaxPFBullet()
    return 0


def CBGetPFArgs(oListener, oEventCB, iPerform, sArgs):
    pfobj = oListener.GetPerform(iPerform)
    if not pfobj:
        return 0
    return pfobj.GetArgValue(sArgs)


def CBCheckFromBenediction(oWarrior, oEventCB, iPerform):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Bene' in dMsgInfo and dMsgInfo['Bene'] == iPerform:
        return 1
    return 0


def CheckInPointBene(oListener, oEventCB, dPointBene):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Bene' in dMsgInfo and dMsgInfo['Bene'] in dPointBene:
        return 1
    return 0


def EventCBGetMsgInfo(oListener, oEventCB, sKey):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if sKey in dMsgInfo:
        return dMsgInfo[sKey]
    return 0


def EventCBCheckSameScene(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'oScene' in dMsgInfo and dMsgInfo['oScene']:
        return dMsgInfo['oScene'].m_ID == oListener.m_Scene
    return 0


def EventCBCheckTargetIsAIHero(oListener, oEventCB):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oWarMgr = oListener.m_Game.m_WarMgr
    return oWarMgr.IsAIHero(iTarget)


def EventCBCheckTargetHasAllAbnormalState(oListener, oEventCB):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTransInfo['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return 0
    for iState in g_AllAbnormalStateSID:
        if not oTarget.m_State.GetItemBySID(iState):
            return 0
    
    return 1


def EventCBCheckWeaponBulletType(oListener, oEventCB, iBulletType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Weapon' not in dMsgInfo:
        return 0
    if not dMsgInfo['Weapon']:
        return 0
    oWeapon = dMsgInfo['Weapon']
    oBulletCom = oWeapon.GetComponent('Bullet')
    if not oBulletCom:
        return 0
    return oBulletCom.m_BulletType == iBulletType


def EventCBCheckTargetIsMainPet(oListener, oEventCB):
    if oListener.m_FightType == WARRIOR_PET_MINI:
        iMainPet = oListener.m_ID
    elif oListener.m_FightType == WARRIOR_PET_MINICLONE:
        iMainPet = oListener.m_OwnerPet
    else:
        return False
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return False
    lstTar = dTrans['TargetList']
    if not lstTar:
        return False
    return lstTar[0] == iMainPet


def EventCBCheckElementRestraint(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'CurVID' in dMsgInfo:
        iVictim = dMsgInfo['CurVID']
    elif 'VID' in dMsgInfo:
        iVictim = dMsgInfo['VID']
    else:
        return 0
    oVictim = oListener.m_Game.GetObject(iVictim, PY_FLAG_DEAD)
    if not oVictim:
        return 0
    if oVictim.Shield():
        iHPType = HP_TYPE_SHIELD
    elif oVictim.Armor():
        iHPType = HP_TYPE_ARMOR
    else:
        iHPType = HP_TYPE_NORMAL
    iRestraintElement = g_PositiveElement[iHPType]
    iMustElementRestraint = 1 if oListener.m_MustElementRestrainted else 0
    if 'MainDam' in dMsgInfo:
        lstDam = dMsgInfo['MainDam']
        for _, oReason in lstDam:
            if CheckElementRestraint(oReason, iRestraintElement, iMustElementRestraint):
                return 1
        
    elif 'RS' in dMsgInfo and CheckElementRestraint(dMsgInfo['RS'], iRestraintElement, iMustElementRestraint):
        return 1
    return 0


def CheckElementRestraint(oReason, iRestraintElement, iMustElementRestraint):
    lstDamType = []
    if oReason.Query('MustElementRestraint', 0):
        iMustElementRestraint = 1
    lstDamType.append(oReason.Query('DamType', 0))
    lstDamType.extend(oReason.Query('ExtraFactorElement', []))
    for iDamType in lstDamType:
        if iMustElementRestraint and not (iDamType & DAM_TYPE_NORMAL):
            return 1
        if iDamType & iRestraintElement:
            return 1
    
    return 0


def EventCBCheckEventSeasonSuitHasCoreRelic(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'SeasonSuit' not in dMsgInfo:
        return False
    iSuit = dMsgInfo['SeasonSuit']
    clsSuit = GetSeasonSuitCls(iSuit)
    if not clsSuit:
        return False
    iCoreRelic = clsSuit.m_CoreRelic
    if not iCoreRelic:
        return False
    return True


def EventCBCheckFirstActSeasonSuit(oListener, oEventCB, sBaseKey):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'SeasonSuit' not in dMsgInfo:
        return False
    iSuit = dMsgInfo['SeasonSuit']
    sKey = 'FirstActSuit-%s' % sBaseKey
    dFirstActSuit = oListener.QuerySavedData(sKey, { })
    if iSuit in dFirstActSuit:
        return False
    dFirstActSuit[iSuit] = 1
    oListener.SetSavedData(sKey, dFirstActSuit)
    return True


def EventCBCheckSeasonSuitHasSuitActive(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'SeasonSuit' not in dMsgInfo:
        return False
    lstSourceSuit = GetActiveSourceSuitMap().values()
    if dMsgInfo['SeasonSuit'] not in lstSourceSuit:
        return False
    return True


def EventCBCheckEventFromSubTask(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'TaskID' not in dMsgInfo:
        return 0
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oTask = oLifeCycle.GetObject()
    if oTask.m_SubTask and oTask.m_SubTask and oTask.m_SubTask.m_ID == dMsgInfo['TaskID']:
        return 1
    return 0


def EventCBCheckTargetSuit(oListener, oEventCB, iSuit):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Result' not in dMsgInfo:
        return 0
    lstResult = dMsgInfo['Result']
    if not lstResult or iSuit != lstResult[0]:
        return 0
    return 1


def EventCBPerformDamType(oListener, oEventCB, iObjectType, iDamType, iIgnoreSelf):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'DamType' not in dMsgInfo:
        return 0
    if not iIgnoreSelf:
        if iDamType == dMsgInfo['DamType']:
            return 1
        return 0
    if 'Perform' not in dMsgInfo:
        return 0
    iPerform = dMsgInfo['Perform']
    oTarget = oListener.GetOwnObject(iObjectType)
    if not oTarget:
        return 0
    oPerform = oTarget.GetPerform(iPerform)
    if not oPerform:
        return 0
    oElement = oPerform.m_ElementTypeObj
    iExcludeDamType = oElement.GetExcludeValue(oEventCB.Key())
    if iExcludeDamType != iDamType:
        return 0
    return 1


def EventCBCheckWeaponElementTypeExcludeSelf(oListener, oEventCB, iElementType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Weapon' not in dMsgInfo:
        return 0
    iWeapon = dMsgInfo['Weapon']
    oWeapon = oListener.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return 0
    if not iElementType & oWeapon.m_ElementTypeObj.GetExcludeValue(oEventCB.Key()):
        return 0
    return 1


def EventCBCheckSuitActiveSourceHasTag(oListener, oEventCB, iTag):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    iPerform = oSkill.m_Base['pfid']
    if iTag == SUITTAG_EXPORT:
        dPerformSpecialTag = oListener.Query('PerformSpecialTag', { })
        if dPerformSpecialTag and SUITEXPORT_PFSPECIALTAG in dPerformSpecialTag and iPerform in dPerformSpecialTag[SUITEXPORT_PFSPECIALTAG]:
            return 1
    iPerformType = oSkill.m_Base['PFType']
    if iPerformType != PF_TYPE_SUITACTIVE:
        return 0
    dActiveSourceSuitMap = GetActiveSourceSuitMap()
    iSuit = dActiveSourceSuitMap[iPerform]
    if iTag in GetSeasonSuitTag(iSuit):
        return 1
    return 0


def EventCBCheckTargetDefendTrend(oListener, oEventCB, iDefTrend):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTarget = dTrans['TargetList']
    iTarget = lstTarget[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if oTarget.m_DefendTrend == iDefTrend:
        return 1
    return 0


def EventCBCheckTargetBeneSource(oListener, oEventCB, iSource):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Bene' not in dMsgInfo:
        return 0
    oPerform = oListener.GetPerform(dMsgInfo['Bene'])
    if not oPerform or oPerform.m_PFType != PF_TYPE_BENEDICTION:
        return 0
    return oPerform.m_SourceType == iSource


def EventCBCheckSuitReduceSource(oTarget, oEventCB, iCheckSuit):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if iCheckSuit in dMsgInfo['Result']:
        return 1
    return 0


def EventCBCheckKillSummonClassify(oTarget, oEventCB, dSummon):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'VID' not in dMsgInfo:
        return 0
    oVictim = oTarget.m_Game.GetObject(dMsgInfo['VID'])
    if not oVictim or not (oVictim.m_FightType & WARRIOR_SUMMON):
        return 0
    lstClassify = GetSummonClassify(oVictim.m_SID)
    for iClassify in dSummon:
        if iClassify in lstClassify:
            return 1
    
    return 0


def EventCBCheckPerformSpecialTag(oListener, oEventCB, iTag):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'AID' not in dMsgInfo or dMsgInfo['AID'] != oListener.m_ID:
        return 0
    if 'Skill' not in dMsgInfo:
        return 0
    dPerformSpecialTag = oListener.Query('PerformSpecialTag', { })
    if not dPerformSpecialTag:
        return 0
    oSkill = dMsgInfo['Skill']
    if iTag not in dPerformSpecialTag:
        return 0
    if oSkill.m_Base['pfid'] not in dPerformSpecialTag[iTag]:
        return 0
    return 1


def EventCBGetSkillDamFactorFormItem(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if 'DamFactor' not in oSkill.m_Collect:
        return 0
    dFactor = oSkill.m_Collect['DamFactor']
    dEventInfo = oEventCB.GetCBEventInfo()
    sKey = dEventInfo['PFKey']
    if sKey not in dFactor:
        return 0
    return dFactor[sKey]


def EventCBCheckSuitHasTag(oListener, oEventCB, iTag):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Suit' not in dMsgInfo:
        return 0
    iSuit = dMsgInfo['Suit']
    if iTag not in GetSeasonSuitTag(iSuit):
        return 0
    return 1


def EventCBCheckRelicLotteryRewardLevel(oListener, oEventCB, iRewardLevel):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'PreReward' not in dMsgInfo:
        return 0
    if dMsgInfo['PreReward'] == iRewardLevel:
        return 1
    return 0


def EventCBCheckSeasonCoreSuitReachMaxGrade(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'SeasonSuit' not in dMsgInfo:
        return False
    iSuit = dMsgInfo['SeasonSuit']
    oSeasonSuit = oListener.m_Game.m_WarMgr.GetSeasonSuitElement()
    if not oSeasonSuit:
        return False
    return oSeasonSuit.CheckCoreSuitReachMaxGrade(oListener.m_ID, iSuit)


def EventCheckHandleDisableSuit(oListener, oEventCB, iSeasonSuit):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'HandleRelic' not in dMsgInfo:
        return 0
    oSuitElement = oListener.m_Game.m_WarMgr.GetSeasonSuitElement()
    if not oSuitElement:
        return 0
    dGradeInfo = oSuitElement.GetSuitRelicGradeInfo(iSeasonSuit)
    if not dGradeInfo:
        return 0
    iMinGrade = min(dGradeInfo)
    lstHandleRelic = dMsgInfo['HandleRelic']
    iConditionNum = oSuitElement.GetSuitConditionNum(oListener.m_ID, iSeasonSuit)
    dRelic = oSuitElement.GetSuitRelicCondition(iSeasonSuit)
    iMinEnableNum = dGradeInfo[iMinGrade]
    iRemoveClearNum = 0
    for iRelic, iHandleType in lstHandleRelic:
        if iHandleType != RELIC_TO_TEMPRELIC:
            continue
        if iRelic in dRelic:
            iRemoveClearNum += 1
        if iConditionNum - iRemoveClearNum < iMinEnableNum:
            return 1
    
    return 0


def EventCBGetSeasonSuitOptData(oListener, oEventCB, iIndex):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Result' not in dMsgInfo:
        return 0
    lstResult = dMsgInfo['Result']
    if len(lstResult) <= iIndex:
        return 0
    return lstResult[iIndex]


def CheckMiniGameFromSelf(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'MiniGameSource' not in dMsgInfo:
        return 0
    if dMsgInfo['MiniGameSource'] == oEventCB.Key():
        return 1
    return 0


def EventCBCheckInputRelicLotteryQuality(oListener, oEventCB, iQuality):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Quality' not in dMsgInfo:
        return 0
    if dMsgInfo['Quality'] == iQuality:
        return 1
    return 0


def CheckSuitChosenHistoryWeapon(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Result' not in dMsgInfo:
        return 0
    lstResult = dMsgInfo['Result']
    for iWeaponID in lstResult:
        oWeapon = oListener.GetWeaponByID(iWeaponID)
        if oWeapon and oWeapon.Query('HistoryInjectAnimaWeapon', 0):
            return 1
    
    return 0


def EventCheckStateStatisticsData(oListener, oEventCB, iStateSID, sDictKey, iCheckKey):
    oStateCon = oListener.m_State
    oState = oStateCon.GetItemBySID(iStateSID)
    if not oState:
        return 0
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iCheckKey = cl_formula.GetResultByData(oListener, iCheckKey, dEventInfo, dMsgInfo)
    dCheckDict = oState.GetArgValue(sDictKey, None)
    if not dCheckDict:
        return 0
    if iCheckKey not in dCheckDict:
        return 0
    return 1


def EventCheckTargetSpecialKey(oListener, oEventCB, iKey):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTarget = dTrans['TargetList']
    iTarget = lstTarget[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return 0
    if oTarget.QueryBitAttr('SpecialKey') & iKey:
        return 1
    return 0


def EventCheckRelicIsGoldBoxSuper(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'iPerform' not in dMsgInfo:
        return 0
    lstRelic = oListener.QuerySavedData('SeasonSuit_NowRelic', [])
    if not lstRelic:
        return 0
    iRelic = lstRelic[0]
    if iRelic == dMsgInfo['iPerform']:
        return 1
    return 0


def EventCBCheckPerfromInActivePerformTag(oListener, oEventCB, iTag):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    iPerform = oSkill.m_Base['pfid']
    dCommonActiveTag = GetCommonActiveTag()
    dClientActiveTag = GetClientActiveTag()
    for dActiveTag in (dCommonActiveTag, dClientActiveTag):
        if iTag in dActiveTag:
            dTagPerform = dActiveTag[iTag]
            if iPerform in dTagPerform:
                return 1
    
    return 0


def CheckTargetHasAfPFType(oListener, oEventCB, iType):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return 0
    tSuperInfo = oTarget.Query('MonsterSuper', None)
    if not tSuperInfo:
        return 0
    (_, iAf) = tSuperInfo
    clsAf = cl_perform.GetPerformModule(iAf)
    if not clsAf or clsAf.m_MonsterAfType != iType:
        return 0
    return 1


def CheckNPCIsGoldenCup(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'NPC' in dMsgInfo:
        iNPCID = dMsgInfo['NPC']
    elif 'NpcID' in dMsgInfo:
        iNPCID = dMsgInfo['NpcID']
    elif 'ShopNpc' in dMsgInfo:
        iNPCID = dMsgInfo['ShopNpc']
    else:
        return 0
    oNpc = oListener.m_Game.GetObject(iNPCID)
    if oNpc and oNpc.m_FightType in NWARRIOR_NPC_ALL_GOLDENCUP:
        return 1
    return 0


def EventCBCheckSeedOrPlantPos(oListener, oEventCB, iSetTargetPos, iCheckID = 0):
    oGame = oListener.m_Game
    dEventInfo = oEventCB.GetCBEventInfo()
    iCheckID = cl_formula.GetResultByData(oListener, iCheckID, dEventInfo)
    if iCheckID:
        oListener = oGame.GetObject(iCheckID)
    if oListener.m_SID != GARDENER_HERO:
        return 0
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.GetStableKey(oEventCB.GetCBEventInfo()))
        return 0
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oTarget = oGame.GetObject(iTarget)
    if not oTarget:
        return 0
    oGardenerCon = oListener.m_GardenerCon
    oScene = oGame.m_SceneMgr.GetScene(oListener.m_Scene)
    if not oScene:
        return 0
    iLevel = oScene.m_Level
    if oTarget.m_FightType & WARRIOR_BOSS == WARRIOR_BOSS and oGardenerCon.CheckUseBossLevelCreatePos(iLevel):
        (ret, vPos) = oGardenerCon.GetBossLevelAutoCreatePos(iLevel)
        if ret:
            if iSetTargetPos:
                dTrans['TargetPos'] = vPos
            return 1
        return 0
    vPos = oGardenerCon.GetPosInGround(oTarget.GetPos())
    if not vPos:
        return 0
    if iSetTargetPos:
        dTrans['TargetPos'] = vPos
    return 1


def CheckMoveStatusList(oListener, oEventCB, dStatus):
    if not oListener.m_FightType & WARRIOR_HERO:
        return 0
    oMoveCtrl = oListener.m_MoveCtrl
    if not oMoveCtrl:
        return 0
    return oMoveCtrl.m_CurStatus in dStatus


def EventCBCheckItemQuality(oListener, oEventCB, iQuality, iItemType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if iItemType == VIRTUAL_ITEM_WAND:
        if 'Wand' not in dMsgInfo:
            return 0
        oWand = oListener.m_WandCon.GetWandByID(dMsgInfo['Wand'])
        if not oWand:
            return 0
        if iQuality != oWand.GetWandQuality():
            return 0
    if iItemType == VIRTUAL_ITEM_WANDCOMP:
        if 'Quality' not in dMsgInfo:
            return 0
        if iQuality != dMsgInfo['Quality']:
            return 0
    return 1


def EventCBCheckChallengeStatus(oListener, oEventCB, iCheckStatus):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Status' not in dMsgInfo:
        return 0
    iStatus = dMsgInfo['Status']
    if iCheckStatus != iStatus:
        return 0
    return 1


def EventCBCheckInteractReHit(oListener, oEventCB, sKey):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'OriginID' not in dMsgInfo or 'TriggerFrame' not in dMsgInfo:
        return 0
    iOriginID = dMsgInfo['OriginID']
    iTriggerFrame = dMsgInfo['TriggerFrame']
    tHitFlag = (iOriginID, iTriggerFrame)
    lstHitFlag = oListener.Query(sKey, [])
    if tHitFlag not in lstHitFlag:
        return 0
    return 1


def EventCBCheckWandAllPointCompPointQuality(oListener, oEventCB, iQuality, iCompType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Wand' not in dMsgInfo:
        return 0
    oWand = oListener.m_WandCon.GetWandByID(dMsgInfo['Wand'])
    if not oWand:
        return 0
    (iMaxConditionNum, iMaxActionNum) = oWand.GetWandGroveNum()
    if iCompType == WAND_COMP_TYPE_ACTION:
        iMaxNum = iMaxActionNum
    elif iCompType == WAND_COMP_TYPE_CONDITION:
        iMaxNum = iMaxConditionNum
    else:
        SendAlert('err', f'''法杖模块类型配置有误：{iCompType}''')
        return 0
    dComp = oWand.GetWandCompByType(iCompType)
    if len(dComp) < iMaxNum:
        return 0
    for oComp in dComp.values():
        if oComp.GetLifeCycleLevel() != iQuality:
            return 0
    
    return 1


def EventCBCheckDamFromTargetFightType(oListener, oEventCB, iFightType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'OriginalAID' in dMsgInfo:
        iAID = dMsgInfo['OriginalAID']
    elif 'AID' not in dMsgInfo:
        return 0
    iAID = dMsgInfo['AID']
    oAttacker = oListener.m_Game.GetObject(iAID)
    if not oAttacker:
        return 0
    iAttackerFightType = oAttacker.m_FightType
    if 255 & iFightType:
        if iAttackerFightType == iFightType:
            return 1
        return 0
    if iAttackerFightType & iFightType == iFightType:
        return 1
    return 0


def EventCBCheckDamFromFightTypeInRange(oListener, oEventCB, dFightType, iFromSelf):
    if not dFightType:
        SendAlert('err', '%s需要指定战斗类型范围' % oEventCB.m_Key)
        return 0
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'OriginalAID' in dMsgInfo:
        iAID = dMsgInfo['OriginalAID']
    elif 'AID' not in dMsgInfo:
        return 0
    iAID = dMsgInfo['AID']
    oAttacker = oListener.m_Game.GetObject(iAID)
    if not oAttacker:
        return 0
    if iFromSelf and oAttacker.m_Owner != oListener.m_ID:
        return 0
    iAttackerFightType = oAttacker.m_FightType
    for iFightType in dFightType:
        if 255 & iFightType or iAttackerFightType == iFightType:
            return 1
        if iAttackerFightType & iFightType == iFightType:
            return 1
    
    return 0


def EventCBCheckMinorPfTag(oListener, oEventCB, iTag):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' in dMsgInfo:
        iPerform = dMsgInfo['Skill'].m_Base['pfid']
    else:
        iPerform = dMsgInfo.get('pfid', 0)
    if not iPerform:
        return 0
    clsPerform = cl_perform.GetPerformModule(iPerform)
    if not clsPerform or not (clsPerform.m_IsMinor):
        return 0
    if iTag in clsPerform.m_ClassifyTag:
        return 1
    return 0


def EventCBCheckItemType(oListener, oEventCB, iType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ItemType' not in dMsgInfo:
        return 0
    iItemType = dMsgInfo['ItemType']
    if iItemType & iType == iType:
        return 1
    return 0


def EventCBGetLimitedTimeInfo(oListener, oEventCB, iKey, iTime):
    oLifeCycle = oEventCB.GetCBLifeCycle()
    oLifeCycleOwner = oLifeCycle.GetObject()
    if not oLifeCycleOwner:
        return 0
    dLimitedTimeInfo = oLifeCycleOwner.GetArgValue('LimitedTimeInfo', { })
    if not dLimitedTimeInfo:
        return 0
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iKey = cl_formula.GetResultByData(oListener, iKey, dEventInfo, dMsgInfo)
    if iKey not in dLimitedTimeInfo:
        return 0
    dInfo = dLimitedTimeInfo[iKey]
    iTime = cl_formula.GetResultByData(oListener, iTime, dEventInfo, dMsgInfo)
    iLimitFrame = oListener.m_Game.GetFrameNum() - Time2Frame(iTime)
    iAllRecordVal = 0
    for iRecordFrame, iRecordVal in dict(dInfo).items():
        if iRecordFrame >= iLimitFrame:
            iAllRecordVal += iRecordVal
            continue
        dInfo.pop(iRecordFrame)
    
    return iAllRecordVal


def EventCBGetTransInfo(oListener, oEventCB, sKey, iDefault = 0):
    dTransInfo = oEventCB.GetCBTransInfo()
    if sKey not in dTransInfo:
        return iDefault
    return dTransInfo[sKey]


def EventCBGetHulkNormalPunchIdx(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    iPerform = oSkill.m_Base['pfid']
    if iPerform != HULK_NORMAL_PUNCH_PF:
        return 0
    return cl_perform.skillcache.GetSkillCacheByIndex(oSkill, SKILLCACHE_INT) % 4 + 1


def EventCBGetDicePoints(oListener, oEventCB):
    oDiceCon = oListener.m_DiceCon
    if not oDiceCon:
        return 0
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Dice' not in dMsgInfo:
        return 0
    iDice = dMsgInfo['Dice']
    oDice = oDiceCon.GetDiceByID(iDice)
    if not oDice:
        return 0
    return oDice.m_RollPoint


def EventCBCheckDicePointInDict(oListener, oEventCB, dPoints):
    oDiceCon = oListener.m_DiceCon
    if not oDiceCon:
        return 0
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Dice' not in dMsgInfo:
        return 0
    iDice = dMsgInfo['Dice']
    oDice = oDiceCon.GetDiceByID(iDice)
    if not oDice:
        return 0
    if oDice.m_RollPoint in dPoints:
        return 1
    return 0


def EventCBSpItemBanBeneDic(oListener, oEventCB, iBanBeneDicSID):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'RS' not in dMsgInfo:
        return True
    if 'UsedSpi' not in dMsgInfo:
        return False
    lstUsedSpi = dMsgInfo['UsedSpi']
    lstBanBeneList = GetSpItemBanBenedicList()
    for iSpItem in lstUsedSpi:
        if iSpItem in lstBanBeneList and iBanBeneDicSID in lstBanBeneList[iSpItem]:
            return True
    
    return False


def EventCBCheckSpecialItemUsed(oListener, oEventCB, iSpecialItemSID):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'UsedSpi' not in dMsgInfo:
        return False
    lstUsedSpi = dMsgInfo['UsedSpi']
    if iSpecialItemSID in lstUsedSpi:
        return True
    return False


def EventCBCheckInPointSpecialItem(oListener, oEventCB, dSpecialItem):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'SpecialItemSID' not in dMsgInfo:
        return 0
    iSpecialSID = dMsgInfo['SpecialItemSID']
    if iSpecialSID in dSpecialItem:
        return 1
    return 0


def EventCBGetDiceQuality(oListener, oEventCB):
    oDiceCon = oListener.m_DiceCon
    if not oDiceCon:
        return 0
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Dice' not in dMsgInfo:
        return 0
    iDice = dMsgInfo['Dice']
    oDice = oDiceCon.GetDiceByID(iDice)
    if not oDice:
        return 0
    return oDice.m_Quality


def EventCBGetAssembledDifferentDiceNumByCondition(oListener, oEventCB, iQuality):
    oDiceCon = oListener.m_DiceCon
    if not oDiceCon:
        return 0
    dAssembledDice = oDiceCon.GetAssembleDice()
    if not dAssembledDice:
        return 0
    iResultNum = 0
    lstUsed = []
    for iDice in dAssembledDice.values():
        oDice = oDiceCon.GetDiceByID(iDice)
        if not oDice:
            continue
        if oDice.m_SID not in lstUsed and oDice.m_Quality == iQuality:
            lstUsed.append(oDice.m_SID)
            iResultNum += 1
    
    return iResultNum


def EventCBGetTargetCareerPFBullet(oListener, oEventCB, iPerform):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return 0
    oPerform = oTarget.GetPerform(iPerform)
    if oPerform and oPerform.m_PFType == PF_TYPE_CAREERPF:
        return oPerform.CurPFBullet()
    return 0


def EventCBCheckAffectedByLion(oListener, oEventCB, iEnhance, iUseTarget, iFromSelf = 0):
    if iUseTarget:
        dTrans = oEventCB.GetCBTransInfo()
        if 'TargetList' not in dTrans:
            SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
            return 0
        lstTarget = dTrans['TargetList']
        if not lstTarget:
            return 0
        oTarget = oListener.m_Game.GetObject(lstTarget[0])
        if not oTarget:
            return 0
    oTarget = oListener
    iAttack = oListener.m_ID if iFromSelf else 0
    if iEnhance or oTarget.m_State.GetStateBySource(LION_MONSTER_ENHANCELOCK_STATE, iAttack, 0):
        return 1
    if oTarget.m_State.GetStateBySource(LION_MONSTER_LOCK_STATE, iAttack, 0) or oTarget.m_State.GetStateBySource(LION_MONSTER_ENHANCELOCK_STATE, iAttack, 0):
        return 1
    return 0


def EventCBCheckHitDomainBarrier(oListener, oEventCB):
    if oListener.m_SID != GARDENER_HERO:
        return 0
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Summon' not in dMsgInfo:
        return 0
    if not oListener.m_GardenerCon.CheckIsDomainBarrierSummon(dMsgInfo['Summon']):
        return 0
    return 1


def EventCBCheckStateEffType(oListener, oEventCB, iEffType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    clsState = cl_state.GetStateClass(dMsgInfo['StateSID'])
    if clsState and clsState.m_EffType & iEffType == clsState.m_EffType:
        return 1
    return 0


def EventCBCheckKeyInIgnoreSTEff(oListener, oEventCB, iEffectType, sKey = ''):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oVictim = oListener.m_Game.GetObject(dMsgInfo['VID'])
    if not oVictim:
        return 0
    iSourceEffType = dMsgInfo['EffType']
    if iSourceEffType & iEffectType != iSourceEffType:
        return 0
    dKeyInfo = oVictim.GetBitAttrKeyInfo('IgnoreSTEff', iEffectType | IGNORESTATE_EFF_FLAG)
    if sKey:
        for sIgnoreKey in dKeyInfo:
            if sKey in sIgnoreKey:
                return 1
        
        return 0
    return oEventCB.m_Key in dKeyInfo


def EventCBCheckStateType(oListener, oEventCB, iType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    clsState = cl_state.GetStateClass(dMsgInfo['StateSID'])
    if clsState and clsState.m_Type == iType:
        return 1
    return 0


def EventCBGetTargetWithSelfHeightDifference(oListener, oEventCB):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return float('nan')
    lstTar = dTrans['TargetList']
    if not lstTar:
        return float('nan')
    iTarget = lstTar[0]
    oTarget = oListener.m_Game.GetObject(iTarget, PY_FLAG_DEAD)
    if not oTarget:
        return float('nan')
    if oListener.m_Scene != oTarget.m_Scene:
        return float('nan')
    vTargetCenterPos = oTarget.GetCenter()
    vPos = oListener.GetPos()
    return vTargetCenterPos[1] - vPos[1]


def EventCBGetDiceAbilityQuality(oListener, oEventCB):
    oDiceCon = oListener.m_DiceCon
    if not oDiceCon:
        return 0
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'AbilityQuality' in dMsgInfo:
        return dMsgInfo['AbilityQuality']
    if 'Dice' not in dMsgInfo:
        return 0
    iDice = dMsgInfo['Dice']
    oDice = oDiceCon.GetDiceByID(iDice)
    if not oDice:
        return 0
    return oDice.GetDiceAbilityQuality()


def EventCBGetDiceSource(oListener, oEventCB):
    oDiceCon = oListener.m_DiceCon
    if not oDiceCon:
        return 0
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Dice' not in dMsgInfo:
        return 0
    iDice = dMsgInfo['Dice']
    oDice = oDiceCon.GetDiceByID(iDice)
    if not oDice:
        return 0
    return oDice.m_Source


def EventCBCheckSpecialItemType(oListener, oEventCB, iType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'SpecialItemSID' not in dMsgInfo:
        return 0
    iSpecialItemSID = dMsgInfo['SpecialItemSID']
    lstItem = GetDiceSpecialTypeList(iType)
    if iSpecialItemSID not in lstItem:
        return 0
    return 1


def EventCBGetTargetStateMaxCount(oListener, oEventCB, iState, iFromSelf = 0, iFromSameItem = 0):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return 0
    if iFromSelf or iFromSameItem:
        dEventInfo = oEventCB.GetCBEventInfo()
        lstState = oTarget.m_State.GetItems(iState)
        for oState in lstState:
            if iFromSelf and oState.m_Attacker != oListener.m_ID:
                continue
            if iFromSameItem and dEventInfo['ItemID'] != oState.m_Item:
                continue
            return oState.m_MaxCount
        
        return 0
    oState = oTarget.m_State.GetItemBySID(iState)
    if not oState:
        return 0
    return oState.m_MaxCount


def EventCBCheckInfoInDict(oListener, oEventCB, sKey, dData):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if sKey not in dMsgInfo:
        return 0
    iValue = dMsgInfo[sKey]
    if iValue not in dData:
        return 0
    return 1


def EventCBGetEquipS7ModuleNum(oListener, oEventCB, iS7ModuleSID, iTag, iCheckFullPoint, iCheckHasExtraPoint = 0, iCheckEnhanceTimes = 0, iCheckEquip = 0):
    oBackpackCon = oListener.m_BackpackCon
    if not oBackpackCon:
        return 0
    return oBackpackCon.GetEquipModuleInfo(iS7ModuleSID, iTag, iCheckFullPoint, iCheckHasExtraPoint = iCheckHasExtraPoint, iCheckEnhanceTimes = iCheckEnhanceTimes, iCheckEquip = iCheckEquip, iGetNum = 1)


def EventCBGetEquipS7ModulePoint(oListener, oEventCB, dCheckModuleTag, iCheckExcludeOverflow):
    oBackpackCon = oListener.m_BackpackCon
    if not oBackpackCon:
        return 0
    return oBackpackCon.GetAllEquipModulePoint(dCheckModuleTag, iCheckExcludeOverflow)


def EventCBCheckTargetGroundDistance(oListener, oEventCB, fCheckDistance):
    if fCheckDistance <= 0:
        SendAlert('err', '%s回调检查目标对地距离参数异常，请检查配置' % oEventCB.m_Key)
        return 0
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return 0
    if not oTarget.m_Scene:
        return 0
    vPos = oTarget.GetPos()
    fGroundDis = oTarget.m_Game.Scene_GroundDistance(oTarget.m_Scene, (vPos[0], vPos[1] + 1.8, vPos[2]), oTarget.m_GroundMaxDis, PXMASK_GROUNDBLK, oTarget.m_ID) - 1.8
    if fCheckDistance > fGroundDis:
        return 0
    return 1


def EventCBCheckTargetCurWeaponInWeapon(oListener, oEventCB, dWeapon):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    if not dTrans['TargetList']:
        return 0
    iTarget = dTrans['TargetList'][0]
    oTarget = oListener.m_Game.GetObject(iTarget, PY_FLAG_DEAD)
    if not oTarget:
        return 0
    oWeapon = oTarget.m_WieldCon.GetCurWeapon(itemdef.MAIN_HOLD)
    if not oWeapon:
        return 0
    return oWeapon.m_SID in dWeapon


def EventCBCheckTargetFormSelfByType(oListener, oEventCB, iObjectType):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return False
    lstTar = dTransInfo['TargetList']
    if not lstTar:
        return False
    iTarget = lstTar[0]
    iOwnerObject = oListener.GetOwnObjectID(iObjectType)
    if not iOwnerObject:
        return False
    return iOwnerObject == iTarget


def EventCBGetTargetStateReasonData(oListener, oEventCB, iStateSID, sKey, iFromSelf):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTransInfo['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return 0
    iAttack = oListener.m_ID if iFromSelf else 0
    oState = oTarget.m_State.GetStateBySource(iStateSID, iAttack, 0)
    if not oState:
        return 0
    oReason = oState.Reason()
    if not oReason:
        return 0
    return oReason.Query(sKey, 0)


def EventCBCrystalType(oListener, oEventCB, iType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'CrystalSID' not in dMsgInfo:
        return 0
    iCrystalSID = dMsgInfo['CrystalSID']
    iCrystalType = GetS7CrystalType(iCrystalSID)
    if iCrystalType != iType:
        return 0
    return 1


def EventCBCrystalPoint(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'S7Item' not in dMsgInfo:
        return 0
    oBackpackCon = oListener.m_BackpackCon
    oCrystal = oBackpackCon.GetCrystal(dMsgInfo['S7Item'])
    if not oCrystal:
        return 0
    return oCrystal.GetNowTotalPoint()


def CheckRescueTag(oListener, oEventCB, iType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'RS' not in dMsgInfo:
        return 0
    oReason = dMsgInfo['RS']
    iRescueTag = oReason.Query('Tag', 0)
    if iType == iRescueTag:
        return 1
    return 0


def EventCBCheckOwnerIsSelf(oListener, oEventCB):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTransInfo['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return 0
    return oTarget.m_Owner == oListener.m_ID

