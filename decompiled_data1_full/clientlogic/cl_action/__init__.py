# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_action/__init__.pyc
# RelativePath: clientlogic/cl_action/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

import cl_object.reason
import cl_snetwar
import cl_formula
import cl_msgcenter
import cl_engphyobj
import cl_pxlayer
import cl_newformula
import cl_reward
import cl_forbid
import cl_item.defines as itemdef
import cl_war
import cl_math
import cl_state
import cl_modeldefine
import cl_notify
import cl_betree.pfai
import cl_drop
import cl_abnormalconf
import cl_item.load as itemload
import cl_modeldata
import cl_platformdata
import cl_hero.load
import cl_extraattr
from cl_action.ac_pfative import *
from cl_action.ac_state import *
from cl_action.ac_common import *
from cl_action.ac_item import *
from cl_action.ac_passive import *
from cl_action.ac_achieve import *
from cl_action.ac_task import *
from cl_action.ac_suit import *
from cl_action.ac_wand import *
from cl_action.ac_dicespecialitem import *
from cl_evact import CheckWeaponType2
from cl_behavior.defines import BT_SUCCESS
from cl_commondefines import WARRIOR_OBSTACLE_CTRLGATE, WARRIOR_OBSTACLE_VICCTRL, STATUS_PATROL, FIGHT3_KEY_IGNOREIMMOBILIZE, SIDE_TYPE_VERTIGO, FIGHT_KEY_WUDI, DAM_USE_HP, DAM_TYPE_TRUE, DAM_TYPE_SCENE, NWARRIOR_DROP_CASH, NWARRIOR_DROP_GSCASH, VIRTUAL_ITEM_DROP, WAND_SUBTYPE_COPY
from cl_commondefines import MONSTER_TYPE_MASK, WEAPON_MINOR_PERFORM, WEAPON_MAIN_PERFORM, PAMOD_TYPE_DYNA, ITEMPERFORM_ENABLE_BOTH, WARRIOR_ELIPART, WARRIOR_NORPART, BOSS_DONOT_COUNT, WARRIOR_BOSS, WARRIOR_DEVICE_BARRIER
from cl_commondefines import STATUS_RUN, STATUS_SPRINT, HALTACT_OPENSNIPE, HALTACT_MOVE, FACE_STATUS_TARGET, FACE_STATUS_PATH, PF_TYPE_THROW, PF_TYPE_ATIVE, PF_TYPE_REWARD, PF_TYPE_PASSIVE, RELIC_TYPE_NORMAL, NWARRIOR_DROP_PETEGG, ACTION_SPEED_CD, GAMBLER_HERO, GARDENER_HERO
from cl_commondefines import RELIC_TYPE_CURSE, STATE_EFF_SUBSPD, SETTLE_LOSEWAR, DISABLE_TYPE_MSG, DISABLE_TYPE_SNAPMSG, SETTLE_OVER_FAIL, CTRLWARRIOR_MASK, GAMBLER_REPLACE_DEFAULT, VIRTUAL_ITEM_TALENTWEIGHT, VIRTUAL_ITEM_RELIC, PF_TYPE_RELIC, STATE_TIME_LIMIT
from cl_commondefines import MODEL_TYPE_CAPSULE, DISABLE_TYPE_WARMSG, PF_TYPE_CAREERPF, RESEND_PLAYERONREADY, RESEND_REENTER, RESEND_PLAYERMAPLOADOK, STATE_COUNT_MAX, STATE_COUNT_MIN, VIRTUAL_ITEM_TALENT, FLAW_UNBALANCE_STARTFRAME, RELIC_LIFECYCLE_TEMPLEVEL, STATE_THROWCD_CHANGED
from cl_commondefines import WARRIOR_HERO, NWARRIOR_DROP_RELIC, FORBID_AUTO_FILLBULLET, SEASONTASK_EXTINFO_TYPE_BENE, EXECUTOR_HERO, RELIC_TYPE_CURSE, WARRIOR_DEVICE, BASEATTR_REFRESH, INKMASTER_HERO, WARRIOR_PET, WARRIOR_PET_MINI, FIGHT3_KEY_IGNOREUNBALANCE, NWARRIOR_DROP_RELIC_MYSTERY
from cl_commondefines import FLAW_COLDTIME, FLAW_KILLLINE, FLAW_EFFECTTIME, FLAW_HITTIMES, FLAW_SIZE, FLAW_MAXCOUNT, FLAW_LOCKMAXCOUNT, FLAW_UNBALANCE_PROB, FLAW_UNBALANCE_EFFECTTIME, FLAW_UNBALANCE_IMMOBILIZETIME, FLAW_UNBALANCE_COLDTIME, FLAW_UNBALANCE_KILLLINE, FLAW_MAXKILLLINE, STATUS_JUMP
from cl_commondefines import DEFEND_TREND_SHIELD, DEFEND_TREND_ARMOR, DAM_TYPE_NORMAL, NPC_CB_VALUELIST, NPC_CB_VALUE, TYPE_PASSIVE_TIME_CYCLE, ALL_PERFORMCDRATE_TYPE, PF_SHIFT, VIRTUAL_ITEM_WAND, VIRTUAL_ITEM_WANDCOMP, LEVEL_TYPE_HIDE, CAREERPF_TEMPUSETIMES_STATE
from cl_commondefines import IGNORESTATE_EFF_FLAG, REMOVE_RELIC_ACTIVE, PLANT_PHASE_NORMAL, SEALED_TALENT, DROP_BULLETPICK_IGNOREMAX
from cl_cscommondef import MAIN_HOLD, DEPUTY_HOLD, ITEM_ALL_TYPE, ITEM_BUFF_TYPE, ITEM_DEBUFF_TYPE, GOALPOS_TYPE_PASSBOXNPC, WARRIOR_PET_MINICLONE, SUIT_ELEMENT, SUIT_HANDLE_ELEMENT, SUIT_HANDLE_INTENSIFY, SUIT_HANDLE_BANRELIC, SHOP_ITEM_CHANGE_REASON_BENEDICTION, PF_TYPE_ATTACK
from cl_item.defines import QUALITY_TYPE_LOW, QUALITY_TYPE_NORMAL, QUALITY_TYPE_CURSE
from cl_only import ShufferList, Time2Frame, ChooseKey, Functor, SendAlert, Frame2Time, DeepCopy, DEAD_FLAG_DIED, PY_FLAG_DIED, CTRL_FLAG_FOR_DEAD, PY_FLAG_EXCLUDEHATE, PY_FLAG_DEAD, GAME_FRAME, CTRL_FLAG_FOR_ALL, WFunctor, WeakProxy, ChooseMulKeys
from cl_propdata import BASIC_PROP_NAME
from cl_container.statecon import GS2CStateRefreshExtraInfo
from cl_object.logging import CgLog, WarobjLog, SeasonsuitLog
from cl_container.flawcon import MonsterForbidSpawnFlaw, MonsterResumeSpawnFlaw
from cl_container.inkcon import INKPERFORM
from cl_object.reason import REASON_TYPE_PERFORM
from cl_container.flawcon import NewTargetFlowSID
from cl_commondecorator import ChooseRewardEnd
from cl_seasonplay.season7 import GetCrystalPerformCls
from cl_betree.mobject import SWITCH_TREE_VERTIGO, SWITCH_TREE_SNEER, SWITCH_TREE_MONSTERCHANGE

def CommmonEventCBFunc(oEventCB, iGroup, dEvent, oTarget, dMsgInfo):
    oEventCB.CBFuncAction(oTarget, iGroup, dEvent, dMsgInfo)


def CommonListenMsgCallBack(oTarget, oLifeCycle, iMsg, iSub, iGroup, iOnce, iPriority):
    if not oLifeCycle.GetObject():
        return None
    dEvent = oLifeCycle.AttrCache()
    dEvent['LifeCycle'] = oLifeCycle
    sKey = oLifeCycle.Key()
    func = Functor(CommmonEventCBFunc, oLifeCycle.GetObject().m_EventCB, iGroup, dEvent)
    cl_msgcenter.AddFunction(oTarget, iMsg, func, sKey, iSub, iOnce, iPriority)
    oLifeCycle.AddDisableType(DISABLE_TYPE_MSG, iMsg, sKey, iSub)


def CommonListenServantMsgCallBack(oTarget, oLifeCycle, iMsg, iSub, iGroup):
    
    def ClearFunc(oTarget, oLifeCycle):
        cl_msgcenter.DoneAttention(oTarget, iServant, iMsg, sKey, iSub)

    if not (oTarget.m_FightType & WARRIOR_HERO) or not (oTarget.m_Servant):
        return None
    if not oLifeCycle.GetObject():
        return None
    iServant = oTarget.m_Servant
    dEvent = oLifeCycle.AttrCache()
    dEvent['LifeCycle'] = oLifeCycle
    sKey = oLifeCycle.Key()
    func = Functor(CommonAttentionCBFunc, oLifeCycle.GetObject().m_EventCB, iGroup, dEvent)
    cl_msgcenter.AddAttentionFunc(oTarget, iServant, iMsg, func, sKey, iSub)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonListenDeviceMsgCallBack(oTarget, oLifeCycle, iMsg, iSub, iGroup):
    
    def ClearFunc(oTarget, oLifeCycle):
        cl_msgcenter.DoneAttention(oTarget, iDevice, iMsg, sKey, iSub)

    if not oTarget.m_FightType & WARRIOR_HERO:
        return None
    if not oLifeCycle.GetObject():
        return None
    dEvent = oLifeCycle.AttrCache()
    dEvent['LifeCycle'] = oLifeCycle
    sKey = oLifeCycle.Key()
    iDevice = oTarget.GetDeviceID()
    if not iDevice:
        return None
    func = Functor(CommonAttentionCBFunc, oLifeCycle.GetObject().m_EventCB, iGroup, dEvent)
    cl_msgcenter.AddAttentionFunc(oTarget, iDevice, iMsg, func, sKey, iSub)
    sUniqueKey = 'ListenDeviceMsg-%s-%s' % (iMsg, iSub)
    oLifeCycle.AddUniqueDisableFunc(sUniqueKey, ClearFunc, iCover = 0)


def CommonListenCurPetMsgCallBack(oTarget, oLifeCycle, iMsg, iSub, iGroup):
    
    def ClearFunc(oTarget, oLifeCycle):
        cl_msgcenter.DoneAttention(oTarget, iCurPet, iMsg, sKey, iSub)

    if not oTarget.m_FightType & WARRIOR_HERO:
        return None
    if not oLifeCycle.GetObject():
        return None
    iCurPet = oTarget.m_PetCon.m_CurPet
    if not iCurPet:
        return None
    dEvent = oLifeCycle.AttrCache()
    dEvent['LifeCycle'] = oLifeCycle
    sKey = oLifeCycle.Key()
    func = Functor(CommonAttentionCBFunc, oLifeCycle.GetObject().m_EventCB, iGroup, dEvent)
    cl_msgcenter.AddAttentionFunc(oTarget, iCurPet, iMsg, func, sKey, iSub)
    sUniqueKey = 'ListenPetMsg-%s-%s' % (iMsg, iSub)
    oLifeCycle.AddUniqueDisableFunc(sUniqueKey, ClearFunc, iCover = 1)


def CommonListenOwnerMsgCallBack(oTarget, oLifeCycle, iMsg, iSub, iGroup):
    
    def ClearFunc(oTarget, oLifeCycle):
        cl_msgcenter.DoneAttention(oTarget, iOwner, iMsg, sKey, iSub)

    if not oLifeCycle.GetObject():
        return None
    dEvent = oLifeCycle.AttrCache()
    dEvent['LifeCycle'] = oLifeCycle
    sKey = oLifeCycle.Key()
    iOwner = oTarget.m_Owner
    if not iOwner:
        return None
    func = Functor(CommonAttentionCBFunc, oLifeCycle.GetObject().m_EventCB, iGroup, dEvent)
    cl_msgcenter.AddAttentionFunc(oTarget, iOwner, iMsg, func, sKey, iSub)
    sUniqueKey = 'ListenOwnerMsg-%s-%s' % (iMsg, iSub)
    oLifeCycle.AddUniqueDisableFunc(sUniqueKey, ClearFunc, iCover = 0)


def CommonListenGlobalMsgCallBack(oTarget, oLifeCycle, iMsg, iSub, iGroup):
    
    def ClearFunc(oTarget, oLifeCycle):
        oGame.DoneGlobalAttention(oTarget.m_ID, iMsg, sKey, iSub)

    if not oLifeCycle.GetObject():
        return None
    dEvent = oLifeCycle.AttrCache()
    dEvent['LifeCycle'] = oLifeCycle
    oGame = oTarget.m_Game
    sKey = oLifeCycle.Key()
    func = Functor(CommonAttentionCBFunc, oLifeCycle.GetObject().m_EventCB, iGroup, dEvent)
    oGame.AddGlobalAttention(oTarget.m_ID, iMsg, func, sKey, iSub)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonDoneGlobalMsg(oTarget, oLifeCycle, iMsg, iSub):
    oGame = oTarget.m_Game
    sKey = oLifeCycle.Key()
    oGame.DoneGlobalAttention(oTarget.m_ID, iMsg, sKey, iSub)


def CommonWeaponMsgCallBack(oTarget, oLifeCycle, iMsg, iGroup, iWeaponType, bListenSource):
    
    def ClearFunc(oTarget, oLifeCycle):
        for oWeapon in lstWeapon:
            oWeapon.DoneAttention(iMsg, sKey)
            oWeapon.DoneAttention(itemdef.MSG_ITEM_REMOVE, sKey)
        

    
    def ClearFuncWhenPopCon(oWeapon, oTarget):
        oWeapon.DoneAttention(iMsg, sKey)
        oWeapon.DoneAttention(itemdef.MSG_ITEM_REMOVE, sKey)

    sKey = oLifeCycle.Key()
    oLifeCycleOwner = oLifeCycle.GetObject()
    if bListenSource:
        oWeapon = oLifeCycleOwner.GetMyItem()
        if not oWeapon:
            SendAlert('err', '%s通用监听来源武器未获取到武器' % sKey)
            return None
        lstWeapon = [
            oWeapon]
    else:
        oWieldCon = oTarget.m_WieldCon
        if not oWieldCon:
            return None
        lstWeapon = oWieldCon.GetAllItemByType(iWeaponType)
    dEvent = oLifeCycle.AttrCache()
    dEvent['LifeCycle'] = oLifeCycle
    func = Functor(CommmonEventCBFunc, oLifeCycleOwner.m_EventCB, iGroup, dEvent)
    for oWeapon in lstWeapon:
        oWeapon.AddAttention(itemdef.MSG_ITEM_REMOVE, ClearFuncWhenPopCon, sKey)
        oWeapon.AddAttention(iMsg, func, sKey)
    
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonDoneWeaponMsg(oTarget, oLifeCycle, iMsg, iWeaponType, bListenSource):
    sKey = oLifeCycle.Key()
    oLifeCycleOwner = oLifeCycle.GetObject()
    if bListenSource:
        oWeapon = oLifeCycleOwner.GetMyItem()
        if not oWeapon:
            SendAlert('err', '%s通用监听来源武器未获取到武器' % sKey)
            return None
        lstWeapon = [
            oWeapon]
    else:
        oWieldCon = oTarget.m_WieldCon
        if not oWieldCon:
            return None
        lstWeapon = oWieldCon.GetAllItemByType(iWeaponType)
    for oWeapon in lstWeapon:
        oWeapon.DoneAttention(iMsg, sKey)
        oWeapon.DoneAttention(itemdef.MSG_ITEM_REMOVE, sKey)
    


def CommonListenHoldWeaponMsg(oTarget, oLifeCycle, iFlag, iMsg, iGroup):
    
    def ClearFunc(oTarget, oLifeCycle):
        oOwner = oTarget.GetOwner()
        if not oOwner:
            return None
        oWeapon = oOwner.m_WieldCon.GetCurWeapon(iFlag)
        if not oWeapon:
            return None
        oWeapon.DoneAttention(iMsg, sKey)
        oWeapon.DoneAttention(itemdef.MSG_ITEM_UNHOLD, sKey)

    
    def WeaponUnhold(oWeapon, oTarget):
        oWeapon.DoneAttention(iMsg, sKey)
        oWeapon.DoneAttention(itemdef.MSG_ITEM_UNHOLD, sKey)

    
    def EventCBFunc(oEventCB, iGroup, dEvent, oOwner, dMsgInfo):
        oEventCB.CBFuncAction(oTarget, iGroup, dEvent, dMsgInfo)

    if iFlag not in (MAIN_HOLD, DEPUTY_HOLD):
        return None
    oWeapon = oTarget.m_WieldCon.GetCurWeapon(iFlag)
    if not oWeapon:
        return None
    sKey = oLifeCycle.Key()
    oLifeCycleOwner = oLifeCycle.GetObject()
    dEvent = oLifeCycle.AttrCache()
    dEvent['LifeCycle'] = oLifeCycle
    func = Functor(EventCBFunc, oLifeCycleOwner.m_EventCB, iGroup, dEvent)
    oWeapon.AddAttention(iMsg, func, sKey)
    oWeapon.AddAttention(itemdef.MSG_ITEM_UNHOLD, WeaponUnhold, sKey)
    sUniqueKey = 'OwnerHoldWeaponMsg-%s' % iMsg
    oLifeCycle.AddUniqueDisableFunc(sUniqueKey, ClearFunc, iCover = 0)


def CommonListenCareerPerformCD(oTarget, oLifeCycle, iGroup):
    
    def ClearFunc(oTarget, oLifeCycle):
        sKey = oLifeCycle.Key()
        oTarget.Remove_Call_Out(sKey)
        cl_msgcenter.DoneEvent(oTarget, cl_msgcenter.MSG_WAR_MODIFYPERFORMCD, oLifeCycle.Key(), 0)
        cl_msgcenter.DoneEvent(oTarget, cl_msgcenter.MSG_WAR_ADDPERFORMCD, oLifeCycle.Key(), 0)

    oPerform = oTarget.GetCareerPerform()
    if not oPerform:
        return None
    sKey = oLifeCycle.Key()
    timeFunc = Functor(CDTimeChangeCallBack, oLifeCycle, iGroup)
    noCDFunc = Functor(NoCDUseCallBack, oLifeCycle, iGroup)
    iDelay = oTarget.m_Perform.GetCurCoverRemainTime(oPerform.m_SID)
    if iDelay:
        func = Functor(FillCDEventCBFunc, oTarget, oLifeCycle, iGroup, oPerform.m_SID)
        oTarget.Call_Out(func, iDelay, sKey)
    cl_msgcenter.AddFunction(oTarget, cl_msgcenter.MSG_WAR_MODIFYPERFORMCD, timeFunc, oLifeCycle.Key(), 0, 0, 0)
    cl_msgcenter.AddFunction(oTarget, cl_msgcenter.MSG_WAR_ADDPERFORMCD, noCDFunc, oLifeCycle.Key(), 0, 0, -1)
    oLifeCycle.AddDisableFunc(ClearFunc)


def FillCDEventCBFunc(oTarget, oLifeCycle, iGroup, iPerform):
    dEvent = oLifeCycle.AttrCache()
    dEvent['LifeCycle'] = oLifeCycle
    oLifeCycle.GetObject().m_EventCB.CBFuncAction(oTarget, iGroup, dEvent, { })
    oPerformcon = oTarget.m_Perform
    if oPerformcon.GetTotalColdTime(iPerform):
        (iDelay, _) = oPerformcon.GetPerformCDAndMaxCover(iPerform)
        func = Functor(FillCDEventCBFunc, oTarget, oLifeCycle, iGroup, iPerform)
        sKey = oLifeCycle.Key()
        oTarget.Call_Out(func, iDelay, sKey)


def CDTimeChangeCallBack(oLifeCycle, iGroup, oTarget, dMsgInfo):
    oPerform = oTarget.GetCareerPerform()
    if not oPerform:
        return None
    sKey = oLifeCycle.Key()
    oTarget.Remove_Call_Out(sKey)
    iDelay = oTarget.m_Perform.GetCurCoverRemainTime(oPerform.m_SID)
    if 'IsDel' in dMsgInfo and dMsgInfo['IsDel']:
        FillCDEventCBFunc(oTarget, oLifeCycle, iGroup, dMsgInfo['pfid'])
    elif iDelay:
        func = Functor(FillCDEventCBFunc, oTarget, oLifeCycle, iGroup, dMsgInfo['pfid'])
        oTarget.Call_Out(func, iDelay, sKey)


def NoCDUseCallBack(oLifeCycle, iGroup, oTarget, dMsgInfo):
    iTime = dMsgInfo['iTime']
    if iTime == 0:
        FillCDEventCBFunc(oTarget, oLifeCycle, iGroup, dMsgInfo['pfid'])


def CommonDoneEvent(oTarget, oLifeCycle, iMsg, iSub):
    sKey = oLifeCycle.Key()
    cl_msgcenter.DoneEvent(oTarget, iMsg, sKey, iSub)


def CommonDoneServantAttention(oTarget, oLifeCycle, iMsg, iSub):
    if not (oTarget.m_FightType & WARRIOR_HERO) or not (oTarget.m_Servant):
        return None
    if not oLifeCycle.GetObject():
        return None
    iServant = oTarget.m_Servant
    sKey = oLifeCycle.Key()
    cl_msgcenter.DoneAttention(oTarget, iServant, iMsg, sKey, iSub)


def CommonDoneDeviceEvent(oTarget, oLifeCycle, iMsg, iSub):
    if not oTarget.m_FightType & WARRIOR_HERO:
        return None
    if not oLifeCycle.GetObject():
        return None
    iDevice = oTarget.GetDeviceID()
    sKey = oLifeCycle.Key()
    cl_msgcenter.DoneAttention(oTarget, iDevice, iMsg, sKey, iSub)


def CommonDoneCurPetEvent(oTarget, oLifeCycle, iMsg, iSub):
    if not oTarget.m_FightType & WARRIOR_HERO:
        return None
    if not oLifeCycle.GetObject():
        return None
    iCurPet = oTarget.m_PetCon.m_CurPet
    if not iCurPet:
        return None
    sKey = oLifeCycle.Key()
    cl_msgcenter.DoneAttention(oTarget, iCurPet, iMsg, sKey, iSub)


def CommonDoneOwnerEvent(oTarget, oLifeCycle, iMsg, iSub):
    if not oLifeCycle.GetObject():
        return None
    iOwner = oTarget.m_Owner
    sKey = oLifeCycle.Key()
    cl_msgcenter.DoneAttention(oTarget, iOwner, iMsg, sKey, iSub)


def CommonListenSnapshotMsg(oTarget, oLifeCycle, iMsg, iSub, iGroup, iOnce, iPriority):
    if not oLifeCycle.m_Enable:
        return None
    dEvent = oLifeCycle.AttrCache()
    dEvent['LifeCycle'] = oLifeCycle
    func = Functor(CommmonEventCBFunc, oLifeCycle.GetObject().m_EventCB, iGroup, dEvent)
    sKey = oLifeCycle.Key()
    iMsgKey = cl_msgcenter.GetMsgKey(iMsg, iSub)
    iWeapon = 0
    if 'PFKey' in dEvent:
        pfobj = oLifeCycle.GetObject()
        oItem = pfobj.GetMyItem()
        if oItem and oItem.Type() & itemdef.EQUIP_MASK_WEAPON:
            oPerformCom = oItem.GetComponent('Perform')
            if not oPerformCom:
                return None
            iWeapon = oItem.m_ID
            oPerformCom.AddTransEvent(iMsgKey, func, sKey, iOnce, iPriority)
    if not iWeapon:
        oTarget.SetTransEvt(iMsg, iMsgKey, func, iOnce, iPriority, sKey)
    oLifeCycle.AddDisableType(DISABLE_TYPE_SNAPMSG, iMsgKey, iWeapon)


def CommonDoneSnapshotMsg(oTarget, oLifeCycle, iMsg, iSub):
    iMsgKey = cl_msgcenter.GetMsgKey(iMsg, iSub)
    sKey = oLifeCycle.Key()
    iWeapon = 0
    if 'PF' in sKey:
        pfobj = oLifeCycle.GetObject()
        if not pfobj:
            return None
        oWeapon = pfobj.GetMyItem()
        if oWeapon and oWeapon.Type() & itemdef.EQUIP_MASK_WEAPON:
            iWeapon = oWeapon.m_ID
            oPerformCom = oWeapon.GetComponent('Perform')
            oPerformCom.RemoveTransEvent(iMsgKey, sKey)
    if not iWeapon and iMsgKey in oTarget.m_TransEvt:
        dPriority = oTarget.m_TransEvt[iMsgKey]
        for dKeys in dPriority.values():
            if sKey in dKeys:
                dKeys.pop(sKey)
                break
        


def CommonListenHPThreshold(oTarget, oLifeCycle, iThreshold, iDirect, iGroup):
    
    def ClearHPThreshold(oTarget, oLifeCycle):
        oTarget.ClearHPThreshold(iThreshold, iDirect, sKey)

    dEvent = oLifeCycle.AttrCache()
    dEvent['LifeCycle'] = oLifeCycle
    iThreshold = cl_formula.GetResultByData(oTarget, iThreshold, dEvent)
    sKey = oLifeCycle.Key()
    func = Functor(CommmonEventCBFunc, oLifeCycle.GetObject().m_EventCB, iGroup, dEvent)
    oTarget.AddHPThreshold(iThreshold, iDirect, sKey, func)
    oLifeCycle.AddDisableFunc(ClearHPThreshold)


def CommonDoneListenHPThreshold(oTarget, oLifeCycle, iThreshold, iDirect):
    sKey = oLifeCycle.Key()
    dEvent = oLifeCycle.AttrCache()
    dEvent['LifeCycle'] = oLifeCycle
    iThreshold = cl_formula.GetResultByData(oTarget, iThreshold, dEvent)
    oTarget.ClearHPThreshold(iThreshold, iDirect, sKey)


def CommonListenMsgCallBackByAttr(oTarget, oLifeCycle, sAttr, iSub, iGroup, iOnce, iPriority):
    
    def ClearAttrEvent(oTarget, oLifeCycle):
        oTarget.DelRefreshAttr(sAttr)
        cl_msgcenter.DoneEvent(oTarget, cl_msgcenter.MSG_WAR_ATTR_CHANGE, oLifeCycle.Key(), iSub)

    iSub = BASIC_PROP_NAME[sAttr][0]
    dEvent = oLifeCycle.AttrCache()
    dEvent['LifeCycle'] = oLifeCycle
    oTarget.AddRefreshAttr(sAttr)
    func = Functor(CommmonEventCBFunc, oLifeCycle.GetObject().m_EventCB, iGroup, dEvent)
    cl_msgcenter.AddFunction(oTarget, cl_msgcenter.MSG_WAR_ATTR_CHANGE, func, oLifeCycle.Key(), iSub, iOnce, iPriority)
    oLifeCycle.AddDisableFunc(ClearAttrEvent)


def CommonDoneListenMsgCallBackByAttr(oTarget, oLifeCycle, sAttr):
    iSub = BASIC_PROP_NAME[sAttr][0]
    oTarget.DelRefreshAttr(sAttr)
    cl_msgcenter.DoneEvent(oTarget, cl_msgcenter.MSG_WAR_ATTR_CHANGE, oLifeCycle.Key(), iSub)


def CommonListenOwnerMsgCallBackByAttr(oTarget, oLifeCycle, sAttr, iGroup):
    
    def ClearAttrEvent(oTarget, oLifeCycle):
        oOwner = oTarget.GetOwner()
        if not oOwner:
            return None
        oOwner.DelRefreshAttr(sAttr)
        cl_msgcenter.DoneAttention(oTarget, iOwner, iMsg, sKey, iSub)

    oOwner = oTarget.GetOwner()
    if not oOwner:
        return None
    dEvent = oLifeCycle.AttrCache()
    dEvent['LifeCycle'] = oLifeCycle
    iOwner = oOwner.m_ID
    iMsg = cl_msgcenter.MSG_WAR_ATTR_CHANGE
    iSub = BASIC_PROP_NAME[sAttr][0]
    sKey = oLifeCycle.Key()
    oOwner.AddRefreshAttr(sAttr)
    func = Functor(CommonAttentionCBFunc, oLifeCycle.GetObject().m_EventCB, iGroup, dEvent)
    cl_msgcenter.AddAttentionFunc(oTarget, iOwner, iMsg, func, sKey, iSub)
    sUniqueKey = 'ListenOwnerMsg-%s-%s' % (iMsg, sAttr)
    oLifeCycle.AddUniqueDisableFunc(sUniqueKey, ClearAttrEvent, iCover = 0)


def CommmonWarEventCBFunc(oEventCB, iGroup, dEvent, oListener, oTarget, dMsgInfo):
    oEventCB.CBFuncAction(oListener, iGroup, dEvent, dMsgInfo)


def CommonListenWarMgrMsgCallBack(oTarget, oLifeCycle, iMsg, iSub, iGroup):
    iWarMgr = oTarget.m_Game.m_WarMgr.m_ID
    sKey = oLifeCycle.Key()
    dEvent = oLifeCycle.AttrCache()
    dEvent['LifeCycle'] = oLifeCycle
    func = Functor(CommmonWarEventCBFunc, oLifeCycle.GetObject().m_EventCB, iGroup, dEvent)
    cl_msgcenter.AddAttentionFunc(oTarget, iWarMgr, iMsg, func, sKey, iSub)
    oLifeCycle.AddDisableType(DISABLE_TYPE_WARMSG, iWarMgr, iMsg, sKey, iSub)


def CommonDoneWarMgrEvent(oTarget, oLifeCycle, iMsg, iSub):
    if not oLifeCycle.GetObject():
        return None
    iWarMgr = oTarget.m_Game.m_WarMgr.m_ID
    sKey = oLifeCycle.Key()
    cl_msgcenter.DoneAttention(oTarget, iWarMgr, iMsg, sKey, iSub)


def CommonListenLevelCtrlMsgCallBack(oTarget, oLifeCycle, iMsg, iSub, iGroup):
    iLevelCtrl = oTarget.m_Game.m_WarMgr.GetComponent('LevelCtrl').m_ID
    sKey = oLifeCycle.Key()
    dEvent = oLifeCycle.AttrCache()
    dEvent['LifeCycle'] = oLifeCycle
    func = Functor(CommmonWarEventCBFunc, oLifeCycle.GetObject().m_EventCB, iGroup, dEvent)
    cl_msgcenter.AddAttentionFunc(oTarget, iLevelCtrl, iMsg, func, sKey, iSub)
    oLifeCycle.AddDisableType(DISABLE_TYPE_WARMSG, iLevelCtrl, iMsg, sKey, iSub)


def CommonAttentionCBFunc(oEventCB, iGroup, dEvent, oListener, oTarget, dMsgInfo):
    oEventCB.CBFuncAction(oListener, iGroup, dEvent, dMsgInfo)


def CommonListenAllHeroMsgCallBack(oTarget, oLifeCycle, iMsg, iSub, iGroup, iExcSelf = 0):
    
    def ClearEvent(oOwner, oLifeCycle):
        for iHero in lstHero:
            cl_msgcenter.DoneAttention(oTarget, iHero, iMsg, sKey, iSub)
        

    if not oLifeCycle.GetObject():
        return None
    dEvent = oLifeCycle.AttrCache()
    dEvent['LifeCycle'] = oLifeCycle
    sKey = oLifeCycle.Key()
    func = Functor(CommonAttentionCBFunc, oLifeCycle.GetObject().m_EventCB, iGroup, dEvent)
    oGame = oTarget.m_Game
    lstHero = oGame.m_WarMgr.GetRoomHero()
    for iHero in lstHero:
        if iExcSelf and iHero == oTarget.m_ID:
            continue
        oHero = oGame.GetObject(iHero)
        if not oHero:
            continue
        cl_msgcenter.AddAttentionFunc(oTarget, iHero, iMsg, func, sKey, iSub)
    
    oLifeCycle.AddDisableFunc(ClearEvent)


def CommonClearListenAllHeroMsgCallBack(oTarget, oLifeCycle, iMsg, iSub):
    if not oLifeCycle.GetObject():
        return None
    sKey = oLifeCycle.Key()
    oGame = oTarget.m_Game
    lstHero = oGame.m_WarMgr.GetRoomHero()
    for iHero in lstHero:
        cl_msgcenter.DoneAttention(oTarget, iHero, iMsg, sKey, iSub)
    


def CommonListenInkValueThreshold(oTarget, oLifeCycle, iThreshold, iDirect, iGroup, iUnique):
    
    def ClearInkValueThreshold(oTarget, oLifeCycle):
        oInkCon = oTarget.m_InkCon
        oInkCon.ClearInkValueThreshold(iThreshold, iDirect, sKey)

    if oTarget.m_SID != INKMASTER_HERO:
        return None
    dEvent = oLifeCycle.AttrCache()
    iThreshold = cl_formula.GetResultByData(oTarget, iThreshold, dEvent)
    dEvent['LifeCycle'] = oLifeCycle
    sKey = oLifeCycle.Key()
    func = Functor(CommmonEventCBFunc, oLifeCycle.GetObject().m_EventCB, iGroup, dEvent)
    oInkCon = oTarget.m_InkCon
    oInkCon.AddInkValueThreshold(iThreshold, iDirect, sKey, func, iUnique)
    oLifeCycle.AddDisableFunc(ClearInkValueThreshold)


def CommonListenCareerPFReachMaxCover(oTarget, oLifeCycle, iGroup):
    
    def ClearReachMaxCoverFunc(oTarget, oLifeCycle):
        oPerformcon = oTarget.m_Perform
        oPerformcon.ClearReachMaxCoverFunc(iCareerPF, sKey)

    if not oTarget.m_FightType & WARRIOR_HERO:
        return None
    iCareerPF = oTarget.GetCareerPerformID()
    dEvent = oLifeCycle.AttrCache()
    dEvent['LifeCycle'] = oLifeCycle
    sKey = oLifeCycle.Key()
    func = Functor(CommmonEventCBFunc, oLifeCycle.GetObject().m_EventCB, iGroup, dEvent)
    oPerformcon = oTarget.m_Perform
    oPerformcon.AddReachMaxCoverFunc(iCareerPF, sKey, func)
    oLifeCycle.AddDisableFunc(ClearReachMaxCoverFunc)


def CommonListenAssembleDiceSumThreshold(oTarget, oLifeCycle, iThreshold, iDirect, iGroup, iUnique):
    
    def ClearFunc(oTarget, oLifeCycle):
        oDiceCon = oTarget.m_DiceCon
        if not oDiceCon:
            return None
        oDiceCon.ClearAssembleDiceSumThreshold(iThreshold, iDirect, sKey)

    oDiceCon = oTarget.m_DiceCon
    if not oDiceCon:
        return None
    dEvent = oLifeCycle.AttrCache()
    iThreshold = cl_formula.GetResultByData(oTarget, iThreshold, dEvent)
    dEvent['LifeCycle'] = oLifeCycle
    sKey = oLifeCycle.Key()
    func = Functor(CommmonEventCBFunc, oLifeCycle.GetObject().m_EventCB, iGroup, dEvent)
    oDiceCon.AddAssembleDiceSumThreshold(iThreshold, iDirect, sKey, func, iUnique)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonSetEventMaxCBCycle(oTarget, oLifeCycle, iCount):
    oEventCB = oLifeCycle.GetObject().m_EventCB
    oEventCB.SetMaxCBCycle(iCount)


def CommonDirectEventCBFunc(oTarget, oLifeCycle, iGroup, iUseEventReason = 0, iSelfAsAttack = 0):
    dEvent = oLifeCycle.AttrCache()
    dEvent['LifeCycle'] = oLifeCycle
    dMsgInfo = { }
    if iUseEventReason and 'RS' in dEvent:
        dMsgInfo['RS'] = dEvent['RS']
    if iSelfAsAttack:
        dMsgInfo['AID'] = oTarget.m_ID
    oLifeCycle.GetObject().m_EventCB.CBFuncAction(oTarget, iGroup, dEvent, dMsgInfo)


def CommonChangeAttr(oTarget, oLifeCycle, sAttr, iMul, iAdd, iPreExclude = 0):
    dData = {
        'LifeCycle': oLifeCycle }
    if iMul:
        iMul = cl_formula.GetResultByData(oTarget, iMul, dData)
    if iAdd:
        iAdd = cl_formula.GetResultByData(oTarget, iAdd, dData)
        iAdd = cl_object.AttrUnitConversion(sAttr, iAdd)
    sKey = oLifeCycle.Key()
    oLifeCycle.m_Apply[sAttr] = 1
    oTarget.AttrChange(sAttr, iMul, iAdd, sKey, iPreExclude = iPreExclude)


def CommonChangeAttrFixedAddition(oTarget, oLifeCycle, sAttr, iValue):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.AttrClearFixedAddition(sAttr, sKey)

    sKey = oLifeCycle.Key()
    dData = {
        'LifeCycle': oLifeCycle }
    iValue = cl_formula.GetResultByData(oTarget, iValue, dData)
    oTarget.AttrChangeFixedAddition(sAttr, sKey, iValue)
    oLifeCycle.AddUniqueDisableFunc(sKey, ClearFunc, iCover = 0)


def CommonChangeBaseDamRatio(oTarget, oLifeCycle, iMul, iAdd, iMask, iCloseRemove = 1):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.ClearBaseDamRatioByKey(sKey)

    sKey = oLifeCycle.Key()
    dData = {
        'LifeCycle': oLifeCycle }
    iAdd = cl_formula.GetResultByData(oTarget, iAdd, dData)
    iMul = cl_formula.GetResultByData(oTarget, iMul, dData)
    if iAdd or iMul:
        oTarget.ChangeBaseDamRatio(sKey, iAdd, iMul, iMask)
        if iCloseRemove:
            oLifeCycle.AddUniqueDisableFunc('CommonChangeBaseDamRatio', ClearFunc, iCover = 0)
        else:
            oTarget.ClearBaseDamRatioByKey(sKey)


def CommonChangeServantAttr(oTarget, oLifeCycle, sAttr, iMul, iAdd, iCalUserOwner = 0):
    
    def ClearChangeServantAttr(oTarget, oLifeCycle):
        oServant.AttrClear(sAttr, sKey)

    if not oTarget.m_FightType & WARRIOR_HERO:
        return None
    oServant = oTarget.m_Game.GetObject(oTarget.m_Servant)
    if not oServant:
        return None
    dData = {
        'LifeCycle': oLifeCycle }
    oCalTarget = oTarget if iCalUserOwner else oServant
    if iMul:
        iMul = cl_formula.GetResultByData(oCalTarget, iMul, dData)
    if iAdd:
        iAdd = cl_formula.GetResultByData(oCalTarget, iAdd, dData)
    sKey = oLifeCycle.Key()
    if iMul or iAdd:
        if not oServant.HasAttr(sAttr):
            oServant.SetAttr(sAttr, 0, BASEATTR_REFRESH)
        oServant.AttrChange(sAttr, iMul, iAdd, sKey)
        sUniqueKey = 'ChangeServantAttr-%s' % sAttr
        oLifeCycle.AddUniqueDisableFunc(sUniqueKey, ClearChangeServantAttr, iCover = 0)
    else:
        oServant.AttrClear(sAttr, sKey)


def CommonChangeDeviceAttr(oTarget, oLifeCycle, sAttr, iMul, iAdd, iCalUserOwner = 0):
    
    def ClearChangeDeviceAttr(oTarget, oLifeCycle):
        oDevice.AttrClear(sAttr, sKey)

    if not oTarget.m_FightType & WARRIOR_HERO:
        return None
    oDevice = oTarget.GetDevice()
    if not oDevice:
        return None
    dData = {
        'LifeCycle': oLifeCycle }
    oCalTarget = oTarget if iCalUserOwner else oDevice
    if iMul:
        iMul = cl_formula.GetResultByData(oCalTarget, iMul, dData)
    if iAdd:
        iAdd = cl_formula.GetResultByData(oCalTarget, iAdd, dData)
    sKey = oLifeCycle.Key()
    if iMul or iAdd:
        if not oDevice.HasAttr(sAttr):
            oDevice.SetAttr(sAttr, 0, BASEATTR_REFRESH)
        oDevice.AttrChange(sAttr, iMul, iAdd, sKey)
        sUniqueKey = 'ChangeDeviceAttr-%s' % sAttr
        oLifeCycle.AddUniqueDisableFunc(sUniqueKey, ClearChangeDeviceAttr, iCover = 0)
    else:
        oDevice.AttrClear(sAttr, sKey)


def CommonChangeDeviceBaseDamRatio(oTarget, oLifeCycle, iMul, iAdd, iMask, iCalUserOwner = 0):
    
    def ClearChangeDeviceBaseDamRatio(oTarget, oLifeCycle):
        oDevice = oTarget.GetDevice()
        oDevice.ClearBaseDamRatioByKey(sKey)

    if not oTarget.m_FightType & WARRIOR_HERO:
        return None
    oDevice = oTarget.GetDevice()
    if not oDevice:
        return None
    sKey = 'ChangeDeviceBaseDam-%s' % oLifeCycle.Key()
    dData = {
        'LifeCycle': oLifeCycle }
    oCalTarget = oTarget if iCalUserOwner else oDevice
    iAdd = cl_formula.GetResultByData(oCalTarget, iAdd, dData)
    iMul = cl_formula.GetResultByData(oCalTarget, iMul, dData)
    if iMul or iAdd:
        oDevice.ChangeBaseDamRatio(sKey, iAdd, iMul, iMask)
        oLifeCycle.AddUniqueDisableFunc(sKey, ClearChangeDeviceBaseDamRatio, iCover = 0)
    else:
        ClearChangeDeviceBaseDamRatio(oTarget, oLifeCycle)


def CommonChangeOwnerAttr(oTarget, oLifeCycle, sAttr, iMul, iAdd):
    
    def ClearChangeOwnerAttr(oTarget, oLifeCycle):
        oOwner = oTarget.GetOwner()
        if not oOwner or oOwner.m_ReleaseFlag:
            return None
        oOwner.AttrClear(sAttr, sKey)

    oOwner = oTarget.GetOwner()
    if not oOwner or oOwner.m_ReleaseFlag:
        return None
    dData = {
        'LifeCycle': oLifeCycle }
    if iMul:
        iMul = cl_formula.GetResultByData(oTarget, iMul, dData)
    if iAdd:
        iAdd = cl_formula.GetResultByData(oTarget, iAdd, dData)
    sKey = oLifeCycle.Key()
    if iMul or iAdd:
        if not oOwner.HasAttr(sAttr):
            oOwner.SetAttr(sAttr, 0, BASEATTR_REFRESH)
        oOwner.AttrChange(sAttr, iMul, iAdd, sKey)
        sUniqueKey = 'ChangeOwnerAttr-%s' % sAttr
        oLifeCycle.AddUniqueDisableFunc(sUniqueKey, ClearChangeOwnerAttr, iCover = 0)
    else:
        oOwner.AttrClear(sAttr, sKey)


def CommonChangeOwnerBaseDamRatio(oTarget, oLifeCycle, iMul, iAdd, iMask):
    
    def ClearFunc(oTarget, oLifeCycle):
        oOwner = oTarget.GetOwner()
        if not oOwner or oOwner.m_ReleaseFlag:
            return None
        sKey = oLifeCycle.Key()
        oOwner.ClearBaseDamRatioByKey(sKey)

    oOwner = oTarget.GetOwner()
    if not oOwner:
        return None
    sKey = 'ChangeOwnerDam-%s' % oLifeCycle.Key()
    dData = {
        'LifeCycle': oLifeCycle }
    iAdd = cl_formula.GetResultByData(oOwner, iAdd, dData)
    iMul = cl_formula.GetResultByData(oOwner, iMul, dData)
    if iAdd or iMul:
        oOwner.ChangeBaseDamRatio(sKey, iAdd, iMul, iMask)
        oLifeCycle.AddUniqueDisableFunc(sKey, ClearFunc, iCover = 0)
    else:
        oOwner.ClearBaseDamRatioByKey(sKey)


def CommonForceSetAttr(oTarget, oLifeCycle, sAttr, iValue):
    dData = {
        'LifeCycle': oLifeCycle }
    if iValue:
        iValue = cl_formula.GetResultByData(oTarget, iValue, dData)
        iValue = cl_object.AttrUnitConversion(sAttr, iValue)
    sKey = oLifeCycle.Key()
    oLifeCycle.m_Apply[sAttr] = 1
    oTarget.AttrForceSet(sAttr, iValue, sKey)


def CommonClearForceAttr(oTarget, oLifeCycle, sAttr):
    oTarget.AttrForceClear(sAttr, oLifeCycle.Key())


def CommonChageMulAttr(oTarget, oLifeCycle, sAttr, iMul):
    iMul = cl_formula.GetResultByData(oTarget, iMul, {
        'LifeCycle': oLifeCycle })
    sKey = oLifeCycle.Key()
    oLifeCycle.m_Apply[sAttr] = 1
    oAttr = oTarget.GetAttr(sAttr)
    oAttr.AddMulFactor(oTarget, iMul, sKey)


def CommonChangeWeaponAttr(oTarget, oLifeCycle, sAttr, iAdd, iMul, iFlag):
    lstAdd = oTarget.m_WieldCon.GetWeapons(iFlag)
    sKey = oLifeCycle.Key()
    dData = {
        'LifeCycle': oLifeCycle }
    if iMul:
        iMul = cl_formula.GetResultByData(oTarget, iMul, dData)
    if iAdd:
        iAdd = cl_formula.GetResultByData(oTarget, iAdd, dData)
        iAdd = cl_object.AttrUnitConversion(sAttr, iAdd)
    for oWeapon in lstAdd:
        if iMul or iAdd:
            oWeapon.AttrChange(sAttr, iMul, iAdd, sKey, iRemoveClear = 1)
            oLifeCycle.m_ItemApply[(oWeapon.m_ID, sAttr)] = 1
            continue
        if (oWeapon.m_ID, sAttr) in oLifeCycle.m_ItemApply:
            oLifeCycle.m_ItemApply.pop((oWeapon.m_ID, sAttr))
        oWeapon.AttrClear(sAttr, sKey)
    


def CommonChangeTargetWeaponAttr(oTarget, oLifeCycle, sAttr, iAdd, iMul, dExcludeType, dClassifyTag):
    lstItem = oTarget.m_WieldCon.GetAllItem()
    lstAdd = list(lstItem)
    if dClassifyTag:
        for oItem in lstItem:
            if not set(dClassifyTag) & set(oItem.m_ClassifyTag):
                lstAdd.remove(oItem)
        
    else:
        for iType in dExcludeType:
            for oItem in lstItem:
                if CheckWeaponType2(oItem, iType):
                    lstAdd.remove(oItem)
            
        
    if not lstAdd:
        return None
    sKey = oLifeCycle.Key()
    dData = {
        'LifeCycle': oLifeCycle }
    iMul = cl_formula.GetResultByData(oTarget, iMul, dData)
    iAdd = cl_formula.GetResultByData(oTarget, iAdd, dData)
    for oWeapon in lstAdd:
        if iMul or iAdd:
            oWeapon.AttrChange(sAttr, iMul, iAdd, sKey, iRemoveClear = 1)
            oLifeCycle.m_ItemApply[(oWeapon.m_ID, sAttr)] = 1
            continue
        if (oWeapon.m_ID, sAttr) in oLifeCycle.m_ItemApply:
            oLifeCycle.m_ItemApply.pop((oWeapon.m_ID, sAttr))
        oWeapon.AttrClear(sAttr, sKey)
    


def CommonSetWeaponForceAttr(oTarget, oLifeCycle, sAttr, iValue, iFlag, iLimitTag = 0, iPriority = 0):
    
    def ClearForceSetWeaponAttr(oTarget, oLifeCycle):
        sKey = oLifeCycle.Key()
        for iWeapon in lstClear:
            oWeapon = oTarget.m_WieldCon.GetItemByID(iWeapon)
            if not oWeapon:
                continue
            oWeapon.ItemAttrForceClear(sAttr, sKey)
        

    lstAdd = oTarget.m_WieldCon.GetWeapons(iFlag, iLimitTag)
    if not lstAdd:
        return None
    sKey = oLifeCycle.Key()
    iValue = cl_formula.GetResultByData(oTarget, iValue, {
        'LifeCycle': oLifeCycle })
    iValue = cl_object.AttrUnitConversion(sAttr, iValue)
    for oWeapon in lstAdd:
        oWeapon.ItemAttrForceSet(sAttr, iValue, sKey, iRemoveClear = 1, iPriority = iPriority)
    
    if lstAdd:
        lstClear = [ oWeapon.m_ID for oWeapon in lstAdd ]
        oLifeCycle.AddDisableFunc(ClearForceSetWeaponAttr)


def CommonIgnoreAttrChangeFromWeapon(oTarget, oLifeCycle, sSource, sAttr, iEffect):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.ClearBitAttr(sIgnoreAttrChange, sEffectKey, iEffect)
        lstAttrResult = GetCurHoldWeaponAttr(oTarget, oLifeCycle, sSource, sAttr)
        for iAdd, iMul, sKey in lstAttrResult:
            if NeedModifyAttr(iEffect, iAdd, iMul):
                oTarget.AttrChange(sAttr, iMul, iAdd, sKey)
        

    dSuppose = {
        'Source': [
            'Hold'],
        'Attr': [
            'MoveSpeed'] }
    if sSource not in dSuppose['Source'] or sAttr not in dSuppose['Attr']:
        SendAlert('err', '目前【武器持有状态】只支持“手持”, 【角色属性】只支持“移动速度”。')
        return None
    sIgnoreAttrChange = 'Ignore_{}_{}'.format(sSource, sAttr)
    sEffectKey = oLifeCycle.Key()
    oTarget.AddBitAttr(sIgnoreAttrChange, sEffectKey, iEffect)
    oLifeCycle.AddDisableFunc(ClearFunc)
    lstWeaponAttr = GetCurHoldWeaponAttr(oTarget, oLifeCycle, sSource, sAttr)
    for iAdd, iMul, sKey in lstWeaponAttr:
        if NeedModifyAttr(iEffect, iAdd, iMul):
            oTarget.AttrClear(sAttr, sKey)
    


def GetCurHoldWeaponAttr(oTarget, oLifeCycle, sSource, sAttr):
    dData = {
        'LifeCycle': oLifeCycle }
    lstWeaponAttr = []
    lstCurWeapon = oTarget.m_WieldCon.GetHoldWeapon()
    for tWeaponData in lstCurWeapon:
        tAttrData = tWeaponData[0].m_ComponentAttr[sSource]['WarriorAttr'][sAttr]
        (iAdd, iMul) = tAttrData
        iAdd = cl_formula.GetResultByData(oTarget, iAdd, dData)
        iAdd = cl_object.AttrUnitConversion(sAttr, iAdd)
        iMul = cl_formula.GetResultByData(oTarget, iMul, dData)
        sKey = tWeaponData[0].Key()
        lstWeaponAttr.append([
            iAdd,
            iMul,
            sKey])
    
    return lstWeaponAttr


def NeedModifyAttr(iEffect, iAdd, iMul):
    if iEffect == ITEM_BUFF_TYPE or iAdd > 0 or iMul > 0 or iEffect == ITEM_DEBUFF_TYPE:
        if iAdd < 0 or iMul < 0:
            return True
    return False


def CommonSetCurWeaponAttrChangeRatio(oTarget, oLifeCycle, sAttr, iRatio, iEffect):
    
    def ClearFunc(oTarget, oLifeCycle):
        oWeapon = oTarget.m_WieldCon.GetItemByID(iWeapon)
        if not oWeapon:
            return None
        (iMul, iAdd) = oAttr.GetKeyFactorInfo(sKey)
        if not iMul and not iAdd:
            return None
        oTarget.AttrChange(sAttr, iMul * 10000 // iRatio, iAdd * 10000 // iRatio, sKey)

    oAttr = oTarget.m_PrivateAttr[sAttr]
    if not oAttr:
        return None
    oWeapon = oTarget.m_WieldCon.GetCurWeapon()
    if not oWeapon:
        return None
    sKey = oWeapon.m_Key
    (iMul, iAdd) = oAttr.GetKeyFactorInfo(sKey)
    if not iMul and not iAdd:
        return None
    if not iEffect == ITEM_ALL_TYPE:
        if iEffect == ITEM_BUFF_TYPE or iAdd > 0 or iMul > 0 or iEffect == ITEM_DEBUFF_TYPE:
            if iAdd < 0 or iMul < 0:
                iRatio = cl_formula.GetResultByData(oTarget, iRatio, {
                    'LifeCycle': oLifeCycle })
                if iRatio <= 0:
                    return None
                iWeapon = oWeapon.m_ID
                oTarget.AttrChange(sAttr, iMul * iRatio // 10000, iAdd * iRatio // 10000, sKey)
                oLifeCycle.AddDisableFunc(ClearFunc)


def CommonChangeCareerPerformAttr(oTarget, oLifeCycle, sAttr, iMul, iAdd, iAllCareer = 0):
    if iAllCareer:
        dHero2AllCareer = cl_hero.load.GetHero2HeroCareer()
        for iCareer in dHero2AllCareer[oTarget.m_SID]:
            ChangePerformAttr(oTarget, oLifeCycle, sAttr, iMul, iAdd, iCareer)
        
    else:
        ChangePerformAttr(oTarget, oLifeCycle, sAttr, iMul, iAdd, oTarget.GetCareerPerformID())


def ChangePerformAttr(oTarget, oLifeCycle, sAttr, iMul, iAdd, iPerform):
    oChangePerform = oTarget.GetPerform(iPerform)
    if not oChangePerform:
        return None
    sKey = oLifeCycle.Key()
    dData = {
        'LifeCycle': oLifeCycle }
    if iMul:
        iMul = cl_formula.GetResultByData(oTarget, iMul, dData)
    if iAdd:
        iAdd = cl_formula.GetResultByData(oTarget, iAdd, dData)
        iAdd = cl_object.AttrUnitConversion(sAttr, iAdd)
    oChangePerform.AttrChange(sAttr, sKey, iMul, iAdd)
    oLifeCycle.m_PerformApply[(oChangePerform.m_Item, oChangePerform.m_SID, sAttr)] = 1


def CommonChangeThrowPerformAttr(oTarget, oLifeCycle, sAttr, iMul, iAdd, iAllThrow = 0):
    if iAllThrow:
        dHero2HeroThrow = cl_hero.load.GetHero2HeroThrow()
        for iThrow in dHero2HeroThrow[oTarget.m_SID]:
            ChangePerformAttr(oTarget, oLifeCycle, sAttr, iMul, iAdd, iThrow)
        
    else:
        ChangePerformAttr(oTarget, oLifeCycle, sAttr, iMul, iAdd, oTarget.GetThrowPerformID())


def CommonSetThrowPerformAttr(oTarget, oLifeCycle, sAttr, iValue, iAllThrow = 0):
    sKey = oLifeCycle.Key()
    dData = {
        'LifeCycle': oLifeCycle }
    iValue = cl_formula.GetResultByData(oTarget, iValue, dData)
    if iAllThrow:
        dHero2HeroThrow = cl_hero.load.GetHero2HeroThrow()
        for iThrow in dHero2HeroThrow[oTarget.m_SID]:
            oChangePerform = oTarget.GetPerform(iThrow)
            if not oChangePerform:
                return None
            oChangePerform.AttrForceSet(sAttr, iValue, sKey)
            oLifeCycle.m_PerformApply[(oChangePerform.m_Item, oChangePerform.m_SID, sAttr)] = 1
        
    else:
        oChangePerform = oTarget.GetThrowPerform()
        if not oChangePerform:
            return None
        oChangePerform.AttrForceSet(sAttr, iValue, sKey)
        oLifeCycle.m_PerformApply[(oChangePerform.m_Item, oChangePerform.m_SID, sAttr)] = 1


def CommonChangeThrowPerformColdTime(oTarget, oLifeCycle, iMul, iAdd):
    
    def ReduceStateCount(oWarrior, oLifeCycle):
        oState = oWarrior.m_State.GetItemBySID(STATE_THROWCD_CHANGED)
        if oState:
            oState.AddCount(oWarrior, -1, 0)

    sAttr = 'ColdTime'
    lstAllThrow = cl_hero.load.GetHero2HeroThrow().get(oTarget.m_SID, [])
    oState = oTarget.m_State.GetItemBySID(STATE_THROWCD_CHANGED)
    bNew = False
    if not oState:
        dArgs = {
            'AID': oTarget.m_ID,
            'RS': cl_object.reason.CStrReason(oLifeCycle.Key()) }
        oState = cl_state.AddState(oTarget, STATE_THROWCD_CHANGED, STATE_TIME_FOREVER, 0, dArgs)
        if not oState:
            SendAlert('err', f'''{oTarget}尝试修正投掷技能冷却时间失败''')
            return None
        oState.Enable(oTarget)
        bNew = True
    for iThrow in lstAllThrow:
        oChangePerform = oTarget.GetPerform(iThrow)
        if not oChangePerform:
            continue
        if bNew:
            dArgs = oState.SetArgValueDefault('ThrowColdTime', { })
            dArgs[iThrow] = oChangePerform.m_BaseAttrData['ColdTime']
        ChangePerformAttr(oTarget, oLifeCycle, sAttr, iMul, iAdd, iThrow)
    
    oState.AddCount(oTarget, 1, 0)
    oLifeCycle.AddDisableFunc(ReduceStateCount)


def CommonChangePerformAttr(oTarget, oLifeCycle, iPerform, sAttr, iRatio, iAdd):
    dData = {
        'LifeCycle': oLifeCycle }
    iPerform = cl_formula.GetResultByData(oTarget, iPerform, dData)
    oChangePerform = oTarget.GetPerform(iPerform)
    if not oChangePerform:
        return None
    sKey = oLifeCycle.Key()
    if iAdd:
        iAdd = cl_formula.GetResultByData(oTarget, iAdd, dData)
        iAdd = cl_object.AttrUnitConversion(sAttr, iAdd)
    if iRatio:
        iRatio = cl_formula.GetResultByData(oTarget, iRatio, dData)
    oChangePerform.AttrChange(sAttr, sKey, iRatio, iAdd)
    oLifeCycle.m_PerformApply[(oChangePerform.m_Item, iPerform, sAttr)] = 1


def CommonSetPerformForceAttr(oTarget, oLifeCycle, iPerform, sAttr, iValue):
    oPerform = oTarget.GetPerform(iPerform)
    if not oPerform:
        return None
    dData = {
        'LifeCycle': oLifeCycle }
    if iValue:
        iValue = cl_formula.GetResultByData(oTarget, iValue, dData)
    sKey = oLifeCycle.Key()
    oLifeCycle.m_PerformApply[(oPerform.m_Item, iPerform, sAttr)] = 1
    oPerform.AttrForceSet(sAttr, iValue, sKey)


def CommonClearPerformForceAttr(oTarget, oLifeCycle, iPerform, sAttr):
    oPerform = oTarget.GetPerform(iPerform)
    if not oPerform:
        return None
    sKey = oLifeCycle.Key()
    oPerform.AttrForceClear(sAttr, sKey)


def CommonChangeInkPerformAttr(oTarget, oLifeCycle, sAttr, iRatio, iAdd):
    if oTarget.m_SID != INKMASTER_HERO:
        return None
    sKey = oLifeCycle.Key()
    dData = {
        'LifeCycle': oLifeCycle }
    if iAdd:
        iAdd = cl_formula.GetResultByData(oTarget, iAdd, dData)
        iAdd = cl_object.AttrUnitConversion(sAttr, iAdd)
    if iRatio:
        iRatio = cl_formula.GetResultByData(oTarget, iRatio, dData)
    for iPerform in INKPERFORM:
        oChangePerform = oTarget.GetPerform(iPerform)
        if not oChangePerform:
            continue
        oChangePerform.AttrChange(sAttr, sKey, iRatio, iAdd)
        oLifeCycle.m_PerformApply[(oChangePerform.m_Item, iPerform, sAttr)] = 1
    


def CommonSetPerformAttr(oTarget, oLifeCycle, iPerform, sAttr, iVal):
    dData = {
        'LifeCycle': oLifeCycle }
    iPerform = cl_formula.GetResultByData(oTarget, iPerform, dData)
    oPerform = oTarget.GetPerform(iPerform)
    if not oPerform:
        return None
    iVal = cl_formula.GetResultByData(oTarget, iVal, dData)
    sKey = oLifeCycle.Key()
    if sAttr not in oPerform.m_Attr:
        oPerform.SetAttr(sAttr, 0, 1)
        oPerform.AttrChange(sAttr, sKey, 0, iVal)
    else:
        oAttr = oPerform.GetAttr(sAttr)
        iCurVal = oAttr.GetExcludeValue([
            sKey])
        iAdd = iVal - iCurVal
        oPerform.AttrChange(sAttr, sKey, 0, iAdd)
    oLifeCycle.m_PerformApply[(oPerform.m_Item, iPerform, sAttr)] = 1


def CommonSetSourceWeaponPerformAttr(oTarget, oLifeCycle, iPerform, sAttr, iVal):
    oWeapon = oLifeCycle.GetOwnerSourceWeapon()
    if not oWeapon:
        return None
    oPerform = GetItemPerform(oWeapon, iPerform)
    if not oPerform:
        return None
    sKey = oLifeCycle.Key()
    iVal = cl_formula.GetResultByData(oTarget, iVal, {
        'LifeCycle': oLifeCycle })
    if sAttr not in oPerform.m_Attr:
        oPerform.SetAttr(sAttr, 0, BASEATTR_REFRESH)
        oPerform.AttrChange(sAttr, sKey, 0, iVal)
    else:
        oPerform.AttrClear(sAttr, sKey)
        iCurVal = oPerform.CalAttr(sAttr)
        iAdd = iVal - iCurVal
        oPerform.AttrChange(sAttr, sKey, 0, iAdd)
    oLifeCycle.m_PerformApply[(oPerform.m_Item, iPerform, sAttr)] = 1


def CommonChangeMonsterPerformGroupAttr(oTarget, oLifeCycle, dPerform, sAttr, iRatio, iAdd):
    sKey = oLifeCycle.Key()
    dData = {
        'LifeCycle': oLifeCycle }
    if iRatio:
        iRatio = cl_formula.GetResultByData(oTarget, iRatio, dData)
    if iAdd:
        iAdd = cl_formula.GetResultByData(oTarget, iAdd, dData)
    for iPerform in dPerform:
        oChangePerform = oTarget.GetPerform(iPerform)
        if not oChangePerform:
            continue
        oChangePerform.AttrChange(sAttr, sKey, iRatio, iAdd)
        oLifeCycle.m_PerformApply[(oChangePerform.m_Item, iPerform, sAttr)] = 1
    


def CommonChangeAllAtivePerformAttr(oTarget, oLifeCycle, sAttr, iRatio, iAdd):
    lstPerform = oTarget.m_Perform.GetPerformSIDByType(PF_TYPE_ATIVE)
    if not lstPerform:
        return None
    sKey = oLifeCycle.Key()
    dData = {
        'LifeCycle': oLifeCycle }
    if iAdd:
        iAdd = cl_formula.GetResultByData(oTarget, iAdd, dData)
        iAdd = cl_object.AttrUnitConversion(sAttr, iAdd)
    if iRatio:
        iRatio = cl_formula.GetResultByData(oTarget, iRatio, dData)
    for iPerform in lstPerform:
        oPerform = oTarget.GetPerform(iPerform)
        oPerform.AttrChange(sAttr, sKey, iRatio, iAdd)
        oLifeCycle.m_PerformApply[(oPerform.m_Item, iPerform, sAttr)] = 1
    


def CommonChangeTargetTypePerformAttr(oTarget, oLifeCycle, iType, sAttr, iMul, iAdd):
    lstPerform = oTarget.GetPerformSIDByType(iType)
    dData = {
        'LifeCycle': oLifeCycle }
    iAdd = cl_formula.GetResultByData(oTarget, iAdd, dData)
    iMul = cl_formula.GetResultByData(oTarget, iMul, dData)
    sKey = oLifeCycle.Key()
    for iPerform in lstPerform:
        oPerform = oTarget.GetPerform(iPerform)
        if not oPerform:
            continue
        oPerform.AttrChange(sAttr, sKey, iMul, iAdd)
        oLifeCycle.m_PerformApply[(oPerform.m_Item, oPerform.m_SID, sAttr)] = 1
    


def CommonChangePerformDamType(oTarget, oLifeCycle, iPerform, iDamType):
    
    def ClearChangePerformDamType(oTarget, oLifeCycle):
        oChangePerform = oTarget.GetPerform(iPerform)
        if not oChangePerform:
            return None
        sKey = oLifeCycle.Key()
        oChangePerform.m_ElementTypeObj.RemoveSetModify(sKey)

    sKey = oLifeCycle.Key()
    oChangePerform = oTarget.GetPerform(iPerform)
    if not oChangePerform:
        return None
    iDamType = cl_formula.GetResultByData(oTarget, iDamType, {
        'LifeCycle': oLifeCycle })
    oChangePerform.m_ElementTypeObj.SetModify(sKey, iDamType)
    oLifeCycle.AddDisableFunc(ClearChangePerformDamType)


def CommonGetPerformAttr(oTarget, oLifeCycle, iPerform, sAttr):
    oPerform = oTarget.GetPerform(iPerform)
    if not oPerform:
        return 0
    return oPerform.CalAttr(sAttr)


def CommonGetAttPerformAttr(oTarget, oLifeCycle, sAttr):
    oPerform = oTarget.GetPerform(oTarget.m_AttPerform)
    if not oPerform:
        return 0
    return oPerform.CalAttr(sAttr)


def CommonChangeMaxBullet(oTarget, oLifeCycle, iBullet, iMul, iAdd):
    
    def ClearChangeMaxBullet(oTarget, oLifeCycle):
        iBulletNum = oTarget.m_BulletCon.Bullet(iBullet)
        oTarget.m_BulletCon.RemoveBulletMul(iBullet, sKey)
        oLifeCycleOwner = oLifeCycle.GetObject()
        if oLifeCycleOwner and oLifeCycleOwner.GetArgValue('ChangeLeveling', 0) and iBulletNum > oTarget.m_BulletCon.Bullet(iBullet):
            dBulletCache = oLifeCycleOwner.SetArgValueDefault('BulletCache', { })
            dBulletCache[iBullet] = iBulletNum

    sKey = oLifeCycle.Key()
    dData = {
        'LifeCycle': oLifeCycle }
    iAdd = cl_formula.GetResultByData(oTarget, iAdd, dData)
    iMul = cl_formula.GetResultByData(oTarget, iMul, dData)
    oTarget.m_BulletCon.AddInBulletMul(iBullet, iMul, iAdd, sKey)
    oLifeCycleOwner = oLifeCycle.GetObject()
    if oLifeCycleOwner and oLifeCycleOwner.GetArgValue('ChangeLeveling', 0):
        dBulletCache = oLifeCycleOwner.GetArgValue('BulletCache', { })
        if iBullet in dBulletCache:
            iBulletNum = dBulletCache.pop(iBullet)
            if not dBulletCache:
                oLifeCycleOwner.DelArgValue('BulletCache')
            oTarget.m_BulletCon.SetBullet(iBullet, iBulletNum, iSync = 1)
    oLifeCycle.AddDisableFunc(ClearChangeMaxBullet)


def CommonModifyBullet(oTarget, oLifeCycle, iBulletType, iDeductBullet, iSendMsg):
    sKey = oLifeCycle.Key()
    dData = {
        'LifeCycle': oLifeCycle }
    iDeductBullet = cl_formula.GetResultByData(oTarget, iDeductBullet, dData)
    if not iDeductBullet:
        return None
    oTarget.m_BulletCon.BulletModify(iBulletType, iDeductBullet, sKey, iSendMsg)


def CommonTranslateElementDamType(oTarget, oLifeCycle, iDamType):
    
    def ClearTranslateElementDamType(oTarget, oLifeCycle):
        sKey = oLifeCycle.Key()
        oTarget.m_ElementTypeObj.RemoveSetModify(sKey)

    sKey = oLifeCycle.Key()
    oTarget.m_ElementTypeObj.SetModify(sKey, iDamType)
    oLifeCycle.AddDisableFunc(ClearTranslateElementDamType)


def CommonChangeBaseReceiveDamageRatio(oTarget, oLifeCycle, iAdd, iMul):
    
    def ClearFun(oTarget, oLifeCycle):
        oTarget.ClearBaseRecvDamRatioByKey(sKey)

    dData = {
        'LifeCycle': oLifeCycle }
    if iAdd:
        iAdd = cl_formula.GetResultByData(oTarget, iAdd, dData)
    if iMul:
        iMul = cl_formula.GetResultByData(oTarget, iMul, dData)
    sKey = oLifeCycle.Key()
    if iAdd or iMul:
        oTarget.ChangeBaseRecvDamRatio(sKey, iAdd, iMul)
    else:
        oTarget.ClearBaseRecvDamRatioByKey(sKey)
    oLifeCycle.AddUniqueDisableFunc(sKey, ClearFun, iCover = 0)


def CommonChangeDefValue(oTarget, oLifeCycle, iValue, iDamUseType):
    dEventData = oLifeCycle.AttrCache()
    oReason = dEventData['RS'] if 'RS' in dEventData else cl_object.reason.CStrReason(oLifeCycle.Key())
    oReason = oReason.ExtInfo({
        'DamType': DAM_TYPE_TRUE | iDamUseType,
        'ShowTips': 0 })
    dEventData['LifeCycle'] = oLifeCycle
    iFormulaValue = cl_formula.GetResultByData(oTarget, iValue, dEventData)
    iTarget = oTarget.m_ID
    if iFormulaValue < 0:
        lstChange = [
            (-iFormulaValue, oReason)]
        oTarget.HPModifyDam(iTarget, lstChange)
    elif iFormulaValue > 0:
        lstChange = [
            (iFormulaValue, oReason)]
        oTarget.HPModifyCure(iTarget, lstChange)


def CommonUsePerform(oTarget, oLifeCycle, iPerform, dArgs):
    pfobj = oTarget.GetPerform(iPerform)
    if not pfobj:
        return None
    dData = {
        'LifeCycle': oLifeCycle }
    dRet = cl_formula.CalArgsFormula(oTarget, dArgs, dData)
    dPerform = {
        'Custom': dRet }
    cl_war.UsePerform(oTarget, pfobj, dPerform)


def CommonThumpMonsterOwner(oTarget, oLifeCycle, iProp, iTime, iClient):
    if oTarget.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
        return None
    dData = { }
    if iTime:
        dData['ThumpFrame'] = Time2Frame(iTime)
    oTarget.GetThumped(dData, iProp, iClient)


def CommonDualWield(oTarget, oLifeCycle):
    
    def OverDualWield(oTarget, oLifeCycle):
        oTarget.CloseDualWield()

    if not oTarget.ValidOpenDualWield():
        return None
    oTarget.OpenDualWield()
    oLifeCycle.AddDisableFunc(OverDualWield)


def CommonForbid(oTarget, oLifeCycle, iRule):
    
    def ClearForbid(oTarget, oLifeCycle):
        oTarget.UnForbid(iRule, sKey)

    sKey = oLifeCycle.Key()
    oTarget.Forbid(iRule, sKey)
    oLifeCycle.AddDisableFunc(ClearForbid)


def CommonUnForbid(oTarget, oLifeCycle, iRule):
    sKey = oLifeCycle.Key()
    oTarget.UnForbid(iRule, sKey)


def CommonHalt(oTarget, oLifeCycle, dActPassRule, dPerformPassRule):
    if HALTACT_MOVE not in dActPassRule:
        oTarget.Stop()
    if HALTACT_OPENSNIPE not in dActPassRule and oTarget.m_FightType & WARRIOR_HERO:
        oTarget.SwitchSnipe(0)
    for iActNum, dCasting in oTarget.GetAllCasting():
        if dCasting['pfid'] in dPerformPassRule:
            continue
        HaltCasting(oTarget, iActNum, oLifeCycle.Key() + str(dCasting['pfid']))
    


def CommonHaltPointPerform(oTarget, oLifeCycle, iPerform):
    for iActNum, dCasting in oTarget.GetAllCasting():
        if dCasting['pfid'] == iPerform:
            HaltCasting(oTarget, iActNum, oLifeCycle.Key())
    


def CommonRemovePerform(oTarget, oLifeCycle, iPerform):
    oPerformCon = oTarget.m_Perform
    if oPerformCon.GetPerform(iPerform):
        oPerformCon.RemovePerform(oTarget, iPerform)


def CommonAddLogicKey(oTarget, oLifeCycle, iKey):
    
    def ClearBitAttr(oTarget, oLifeCycle):
        oTarget.ClearBitAttr('LogicKey', sKey, iKey)

    sKey = oLifeCycle.Key()
    oTarget.AddBitAttr('LogicKey', sKey, iKey)
    oLifeCycle.AddDisableFunc(ClearBitAttr)


def CommonRemoveLogicKey(oTarget, oLifeCycle, iKey):
    sKey = oLifeCycle.Key()
    oTarget.ClearBitAttr('LogicKey', sKey, iKey)


def CommonAddSpecialKey(oTarget, oLifeCycle, iKey, iIngoreExclude = 0):
    
    def ClearSpecialKey(oWarrior, oLifeCycle):
        oTarget = oWarrior.m_Game.GetObject(iTarget)
        if not oTarget:
            return None
        oTarget.ClearBitAttr('SpecialKey', sKey, iKey)
        if iKey == FIGHT_KEY_WUDI and not (oTarget.QueryBitAttr('SpecialKey') & FIGHT_KEY_WUDI):
            oTarget.m_Game.SetPyFlag(oTarget.m_ID, PY_FLAG_EXCLUDEHATE, 0)

    iTarget = oTarget.m_ID
    sKey = oLifeCycle.Key()
    oTarget.AddBitAttr('SpecialKey', sKey, iKey)
    if iKey == FIGHT_KEY_WUDI and not iIngoreExclude:
        oTarget.m_Game.SetPyFlag(oTarget.m_ID, PY_FLAG_EXCLUDEHATE, 1)
    oLifeCycle.AddDisableFunc(ClearSpecialKey)


def CommonRemoveSpecialKey(oTarget, oLifeCycle, iKey):
    sKey = oLifeCycle.Key()
    oTarget.ClearBitAttr('SpecialKey', sKey, iKey)
    if iKey == FIGHT_KEY_WUDI and not (oTarget.QueryBitAttr('SpecialKey') & FIGHT_KEY_WUDI):
        oTarget.m_Game.SetPyFlag(oTarget.m_ID, PY_FLAG_EXCLUDEHATE, 0)


def CommonIgnoreStateEffectAdd(oTarget, oLifeCycle, iEffectType, iAddIgnoreStateEffFlag = 0):
    
    def ClearBitApply(oTarget, oLifeCycle):
        oTarget.ClearBitAttr(sAttr, sKey, iEffectType)

    sKey = oLifeCycle.Key()
    sAttr = 'IgnoreSTEff'
    if iAddIgnoreStateEffFlag:
        iEffectType |= IGNORESTATE_EFF_FLAG
    oTarget.AddBitAttr(sAttr, sKey, iEffectType)
    oLifeCycle.AddDisableFunc(ClearBitApply)


def CommonRemoveAllStateByType(oTarget, oLifeCycle, iType):
    oStateCon = oTarget.m_State
    for oState in oStateCon.Values():
        if oState.m_Type == iType:
            oStateCon.RemoveItem(oState.m_ID)
    


def CommonIgnoreStateTypeAdd(oTarget, oLifeCycle, iType, iTime):
    
    def ClearBitApply(oTarget, oLifeCycle):
        oTarget.ClearMaxAttr(sAttr, sKey)

    sKey = oLifeCycle.Key()
    sAttr = 'IgnoreST%d' % iType
    oTarget.AddMaxAttr(sAttr, sKey, 1, Time2Frame(iTime))
    oLifeCycle.AddDisableFunc(ClearBitApply)


def CommonForbidAutoFillBullet(oTarget, oLifeCycle, iLimitTag):
    
    def ClearForbid(oTarget, oLifeCycle):
        dAutoFillLimitTag = oTarget.Query('AutoFillLimitTag', { })
        if iLimitTag in dAutoFillLimitTag:
            lstKey = dAutoFillLimitTag.get(iLimitTag, [])
            if sKey in lstKey:
                lstKey.remove(sKey)
                if lstKey:
                    dAutoFillLimitTag[iLimitTag] = lstKey
                else:
                    dAutoFillLimitTag.pop(iLimitTag)
                oTarget.Set('AutoFillLimitTag', dAutoFillLimitTag)
        oTarget.UnForbid(cl_forbid.AUTO_FILLBULLET_RULE, sKey)
        if oTarget.IsForbid(FORBID_AUTO_FILLBULLET):
            return None
        lstWeapon = oTarget.m_WieldCon.GetAllItemByType(itemdef.EQUIP_TYPE_MAINWEAPON)
        for oWeapon in lstWeapon:
            if iLimitTag not in oWeapon.m_ClassifyTag:
                continue
            oBulletCom = oWeapon.GetComponent('Bullet')
            if not oBulletCom:
                continue
            oStatusMgr = oBulletCom.m_FillBulletStatusMgr
            if not oStatusMgr:
                continue
            oStatusMgr.Enable(oWeapon, oTarget)
        

    sKey = oLifeCycle.Key()
    oTarget.Forbid(cl_forbid.AUTO_FILLBULLET_RULE, sKey)
    dAutoFillLimitTag = oTarget.Query('AutoFillLimitTag', { })
    lstKey = dAutoFillLimitTag.get(iLimitTag, [])
    if sKey not in lstKey:
        lstKey.append(sKey)
        dAutoFillLimitTag[iLimitTag] = lstKey
        oTarget.Set('AutoFillLimitTag', dAutoFillLimitTag)
    lstWeapon = oTarget.m_WieldCon.GetAllItemByType(itemdef.EQUIP_TYPE_MAINWEAPON)
    for oWeapon in lstWeapon:
        if iLimitTag not in oWeapon.m_ClassifyTag:
            continue
        oBulletCom = oWeapon.GetComponent('Bullet')
        if not oBulletCom:
            continue
        oStatusMgr = oBulletCom.m_FillBulletStatusMgr
        if not oStatusMgr:
            continue
        oStatusMgr.Exit(oWeapon, oTarget)
    
    oLifeCycle.AddDisableFunc(ClearForbid)


def CommonForbidWeaponAutoFillBullet(oTarget, oLifeCycle, iWeapon):
    
    def ClearForbid(oTarget, oLifeCycle):
        dAutoFillLimitWeapon = oTarget.Query('AutoFillLimitWeapon', { })
        lstKey = dAutoFillLimitWeapon.get(iWeapon, [])
        if sKey in lstKey:
            lstKey.remove(sKey)
            if lstKey:
                dAutoFillLimitWeapon[iWeapon] = lstKey
            else:
                dAutoFillLimitWeapon.pop(iWeapon)
                lstWeapon = oTarget.m_WieldCon.GetAllItemByType(itemdef.EQUIP_TYPE_MAINWEAPON)
                for oWeapon in lstWeapon:
                    if iWeapon != oWeapon.m_SID:
                        continue
                    oBulletCom = oWeapon.GetComponent('Bullet')
                    if not oBulletCom:
                        continue
                    if oBulletCom.Bullet():
                        continue
                    oStatusMgr = oBulletCom.m_FillBulletStatusMgr
                    if not oStatusMgr or not oStatusMgr.IsNormal():
                        continue
                    oStatusMgr.Normal(oWeapon, oTarget)
                
            oTarget.Set('AutoFillLimitWeapon', dAutoFillLimitWeapon)

    sKey = oLifeCycle.Key()
    dAutoFillLimitWeapon = oTarget.Query('AutoFillLimitWeapon', { })
    lstKey = dAutoFillLimitWeapon.get(iWeapon, [])
    if sKey not in lstKey:
        lstKey.append(sKey)
        dAutoFillLimitWeapon[iWeapon] = lstKey
        oTarget.Set('AutoFillLimitWeapon', dAutoFillLimitWeapon)
    oLifeCycle.AddDisableFunc(ClearForbid)


def CommonTriggerClientBehavior(oTarget, oLifeCycle, iBehavior, iResend, iItemID = 0, iOnlySendSelf = 0):
    
    def EndTriggerClientBehavior(oTarget, oLifeCycle):
        oGame.DoneGlobalAttention(oTarget.m_ID, iMsg, sKey)

    if iItemID is None:
        iItemID = 0
    else:
        iItemID = cl_formula.GetResultByData(oTarget, iItemID, {
            'LifeCycle': oLifeCycle })
    oGame = oTarget.m_Game
    if iOnlySendSelf:
        lstPlayer = [
            oTarget.m_PlayerID]
    else:
        lstPlayer = oGame.m_WarMgr.GetRoomPlayer()
    cl_snetwar.GS2CTriggerBehavior(oGame, oTarget.m_ID, iBehavior, lstPlayer, iStop = 0, iItemID = iItemID)
    iMsg = 0
    if iResend in (RESEND_PLAYERONREADY, RESEND_REENTER):
        iMsg = cl_msgcenter.MSG_WAR_PLAYERONREADY
    elif iResend == RESEND_PLAYERMAPLOADOK:
        iMsg = cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK
    if iMsg:
        sKey = '%s-%s' % (oLifeCycle.Key(), iBehavior)
        oGame.AddGlobalAttention(oTarget.m_ID, iMsg, Functor(ResendBehavior, iBehavior, iResend, iItemID), sKey)
        oLifeCycle.AddDisableFunc(EndTriggerClientBehavior)


def CommonRemoveClientBehavior(oTarget, oLifeCycle, iBehavior):
    oGame = oTarget.m_Game
    lstPlayer = oGame.m_WarMgr.GetRoomPlayer()
    cl_snetwar.GS2CTriggerBehavior(oGame, oTarget.m_ID, iBehavior, lstPlayer, iStop = 1)


def ResendBehavior(iBehavior, iResend, iItemID, oListener, oSender, dInfo):
    if iResend == RESEND_REENTER and dInfo['reenter'] != 1:
        return None
    cl_snetwar.GS2CTriggerBehavior(oListener.m_Game, oListener.m_ID, iBehavior, [
        oSender.m_PlayerID], iItemID = iItemID)


def CommonTriggerWeaponPerformBehavior(oTarget, oLifeCycle, iPerformType, iBehavior, iStop, iResend):
    
    def EndTriggerClientBehavior(oTarget, oLifeCycle):
        oGame.DoneGlobalAttention(oTarget.m_ID, cl_msgcenter.MSG_WAR_PLAYERONREADY, sKey)

    oGame = oTarget.m_Game
    oWeapon = oLifeCycle.GetOwnerSourceWeapon()
    if not oWeapon:
        return None
    oPerformCom = oWeapon.GetComponent('Perform')
    if not oPerformCom:
        return None
    dSend = { }
    lstPlayer = oGame.m_WarMgr.GetRoomPlayer()
    if iPerformType == WEAPON_MAIN_PERFORM:
        for iPerform, _, _, _ in oPerformCom.m_AllAttPerform.values():
            if not iPerform or iPerform in dSend:
                continue
            dSend[iPerform] = 1
        
    elif iPerformType == WEAPON_MINOR_PERFORM:
        iPerform = oPerformCom.m_MinorPeform
        if iPerform:
            dSend[iPerform] = 1
    for iPerform in dSend:
        oPerform = oPerformCom.GetPerform(iPerform)
        dSend[iPerform] = oPerform.m_ID
        cl_snetwar.GS2CTriggerBehavior(oGame, oTarget.m_ID, iBehavior, lstPlayer, iStop, oPerform.m_ID)
    
    if dSend and iResend:
        sKey = '%s-%s' % (oLifeCycle.Key(), iBehavior)
        oGame.AddGlobalAttention(oTarget.m_ID, cl_msgcenter.MSG_WAR_PLAYERONREADY, Functor(ResendItemBehavior, iBehavior, iStop, dSend), sKey)
        oLifeCycle.AddDisableFunc(EndTriggerClientBehavior)


def ResendItemBehavior(iBehavior, iStop, dItem, oListener, oSender, dInfo):
    for iItemID in dItem.values():
        cl_snetwar.GS2CTriggerBehavior(oListener.m_Game, oListener.m_ID, iBehavior, [
            oSender.m_PlayerID], iStop, iItemID)
    


def CommonRemoveState(oTarget, oLifeCycle, iState):
    cl_state.RemoveState(oTarget, iState)


def CommonRefreshStateExtraInfo(oTarget, oLifeCycle, dInfo, iStateSID):
    oGame = oTarget.m_Game
    if not oGame:
        return None
    oState = oTarget.m_State.GetItemBySID(iStateSID)
    if not oState:
        return None
    dRet = cl_formula.CalArgsFormula(oTarget, dInfo, {
        'LifeCycle': oLifeCycle })
    oState.SetArgValue('StateExtraInfo', dRet)
    if not oTarget.m_PlayerID:
        oScene = oGame.m_SceneMgr.GetScene(oTarget.m_Scene)
        dPlayer = dict(oScene.GetPlayers()) if oScene else { }
    else:
        dPlayer = {
            oTarget.m_PlayerID: 1 }
    GS2CStateRefreshExtraInfo(oTarget, oState, dRet, dPlayer)


def CommonRemoveOwnerState(oTarget, oLifeCycle, iStateSID, bJudgeSameItem):
    if bJudgeSameItem:
        dEvent = oLifeCycle.AttrCache()
        iItem = 0
        if 'ItemID' in dEvent:
            iItem = dEvent['ItemID']
        elif 'RS' in dEvent:
            iItem = dEvent['RS'].Query('Item')
    lstState = oTarget.m_State.GetItems(iStateSID)
    for oState in lstState:
        if not oState:
            continue
        if bJudgeSameItem:
            oReason = oState.m_Reason
            iStateItem = oReason.Query('Item', 0)
            if iStateItem and iStateItem == iItem:
                oTarget.m_State.RemoveItem(oState.m_ID)
                continue
        oTarget.m_State.RemoveItem(oState.m_ID)
    


def CommonPerformMonsterVertigo(oTarget, oLifeCycle, sDefaultTree, dTree = None):
    
    def ClearStatePerformMonsterVertigo(oTarget, oLifeCycle):
        oTarget.SetSide(iSide)
        oAgent = oTarget.m_Agent
        if not oAgent:
            return None
        oAgent.RemoveSwitchCurrentBT(SWITCH_TREE_VERTIGO, sKey)

    if not oTarget.m_FightType & MONSTER_TYPE_MASK:
        return None
    oAgent = oTarget.m_Agent
    if not oAgent:
        return None
    sTree = dTree[oTarget.m_DataSID] if dTree and oTarget.m_DataSID in dTree else sDefaultTree
    sKey = oLifeCycle.Key()
    if oAgent.AddSwitchCurrentBT(SWITCH_TREE_VERTIGO, sTree, sKey):
        iSide = oTarget.m_Side
        oTarget.SetSide(SIDE_TYPE_VERTIGO)
        oLifeCycle.AddDisableFunc(ClearStatePerformMonsterVertigo)


def CommonHeroSwitchPerform(oTarget, oLifeCycle, sType, iPerform):
    if not oTarget.m_FightType & WARRIOR_HERO:
        return None
    oTarget.SwitchPerform(sType, iPerform)


def CommonSneerMonster(oTarget, oLifeCycle, sDefaultTree, dTree):
    
    def ClearSneer(oTarget, oLifeCycle):
        dSneerInner = oTarget.Query('Sneer', { })
        dSneerInner.pop(sKey, None)
        oTarget.Set('Sneer', dSneerInner)
        oState = oLifeCycle.GetObject()
        if not oState:
            return None
        oAttack = oTarget.m_Game.GetObject(oState.m_Attacker, PY_FLAG_DEAD)
        if oAttack and oAttack.m_Agent:
            oAttack.m_Agent.RemoveForceHateTarget(iTarget)
        oAgent = oTarget.m_Agent
        if not oAgent:
            return None
        oAgent.RemoveSwitchCurrentBT(SWITCH_TREE_SNEER, sKey)
        oAgent.ClearHateVal()
        oAgent.HateTargetByID(oState.m_Attacker)

    if not oTarget.m_FightType & WARRIOR_MONSTER:
        return None
    iTarget = oTarget.m_ID
    oAgent = oTarget.m_Agent
    if not oAgent:
        return None
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    oAttack = oTarget.m_Game.GetObject(oState.m_Attacker, PY_FLAG_DEAD)
    if not oAttack:
        return None
    sTree = dTree[oTarget.m_DataSID] if dTree and oTarget.m_DataSID in dTree else sDefaultTree
    sKey = oLifeCycle.Key()
    sCDKey = 'SneerCDMark'
    iNowFrame = oTarget.m_Game.GetFrameNum()
    oTarget.Set(sCDKey, iNowFrame)
    dSneer = oTarget.Query('Sneer', { })
    dSneer[sKey] = 1
    oTarget.Set('Sneer', dSneer)
    if oAgent.AddSwitchCurrentBT(SWITCH_TREE_SNEER, sTree, sKey):
        oAgent.SetLockEnemy(oAttack.m_ID)
        if oAttack.m_Agent:
            oAttack.m_Agent.AddForceHateTarget(iTarget)
        oLifeCycle.AddDisableFunc(ClearSneer)


def CommonRemoveSameSourceState(oTarget, oLifeCycle, iRemoveState, iSourceState):
    oStateCon = oTarget.m_State
    oSourceState = None
    iCount = 0
    for oState in oStateCon.Values():
        if oState.m_SID == iSourceState:
            oSourceState = oState
            iCount += 1
    
    if iCount > 1:
        SendAlert('err', '目前【来源状态】只支持一个, 当前存在多个 %s 状态。' % iSourceState)
        return None
    if not oSourceState:
        return None
    oSourceStateReason = oSourceState.m_Reason
    if not hasattr(oSourceStateReason, 'm_Perform'):
        return None
    for oState in oStateCon.Values():
        oReason = oState.m_Reason
        if not hasattr(oReason, 'm_Perform'):
            continue
        if oState.m_SID == iRemoveState and oReason.m_Perform == oSourceStateReason.m_Perform:
            oStateCon.RemoveItem(oState.m_ID)
    


def ImmunitySubSpdState(oTarget, oLifeCycle):
    
    def EnableSubSpdState(oTarget, oLifeCycle):
        oTarget.ClearBitAttr(sAttr, oLifeCycle.Key(), STATE_EFF_SUBSPD)
        for oState in oTarget.m_State.Values():
            if oState.m_EffType == STATE_EFF_SUBSPD:
                oState.Enable(oTarget)
        

    oStateCon = oTarget.m_State
    for oState in oStateCon.Values():
        if oState.m_EffType == STATE_EFF_SUBSPD:
            oState.Disable(oTarget, 1)
    
    sKey = oLifeCycle.Key()
    sAttr = 'ForbidEnableSTEff'
    oTarget.AddBitAttr('ForbidEnableSTEff', sKey, STATE_EFF_SUBSPD)
    oLifeCycle.AddDisableFunc(EnableSubSpdState)


def ImmunitySubSpdStateByMonster(oTarget, oLifeCycle):
    
    def EnableSubSpdState(oTarget, oLifeCycle):
        oTarget.ClearBitAttr(sAttr, oLifeCycle.Key(), STATE_EFF_SUBSPD)
        for oState in oTarget.m_State.Values():
            oReason = oState.Reason()
            if oState.m_EffType == STATE_EFF_SUBSPD and oReason and oReason.m_Type == REASON_TYPE_PERFORM:
                iFightType = oReason.m_FightType
                if iFightType and iFightType & WARRIOR_MONSTER:
                    oState.Enable(oTarget)
        

    oStateCon = oTarget.m_State
    for oState in oStateCon.Values():
        oReason = oState.Reason()
        if oState.m_EffType == STATE_EFF_SUBSPD and oReason and oReason.m_Type == REASON_TYPE_PERFORM:
            iFightType = oReason.m_FightType
            if iFightType and iFightType & WARRIOR_MONSTER:
                oState.Disable(oTarget, 1)
    
    sKey = oLifeCycle.Key()
    sAttr = 'ForbidEnableSTEffByMonster'
    oTarget.AddBitAttr('ForbidEnableSTEffByMonster', sKey, STATE_EFF_SUBSPD)
    oLifeCycle.AddDisableFunc(EnableSubSpdState)


def CommonAddStateCount(oTarget, oLifeCycle, iStateSID, iVal, iCountTime = 0):
    oState = oTarget.m_State.GetItemBySID(iStateSID)
    if oState:
        iVal = cl_formula.GetResultByData(oTarget, iVal, {
            'LifeCycle': oLifeCycle })
        if iCountTime:
            iCountTime = cl_formula.GetResultByData(oTarget, iCountTime, {
                'LifeCycle': oLifeCycle })
            oState.AddCount(oTarget, iVal, Time2Frame(iCountTime))
        else:
            oState.AddCount(oTarget, iVal)


def CommonSetStateCount(oTarget, oLifeCycle, iStateSID, iVal, iFromSameItem = 0):
    if iFromSameItem:
        dEvent = oLifeCycle.AttrCache()
        if 'ItemID' in dEvent:
            iItem = dEvent['ItemID']
        elif 'RS' in dEvent:
            iItem = dEvent['RS'].Query('Item')
        else:
            return None
        lstState = oTarget.m_State.GetItems(iStateSID)
        iVal = cl_formula.GetResultByData(oTarget, iVal, {
            'LifeCycle': oLifeCycle })
        for oState in lstState:
            if iItem != oState.m_Item:
                continue
            oState.SetCount(oTarget, iVal)
        
    else:
        oState = oTarget.m_State.GetItemBySID(iStateSID)
        if oState:
            iVal = cl_formula.GetResultByData(oTarget, iVal, {
                'LifeCycle': oLifeCycle })
            oState.SetCount(oTarget, iVal)


def CommonSetRelifeAttr(oTarget, oLifeCycle, iType, iTime, iTimes, iPriority, dHatchRatio = None, iOnlyRelife = 0, iMaxTimes = 0):
    
    def ClearSetRelifeAttr(oTarget, oLifeCycle):
        if iOnlyRelife:
            oTarget.Delete('SpecificRelife')
        oTarget.ClearRelifeInfo(iType, sKey)

    sKey = oLifeCycle.GetStableKey()
    if iOnlyRelife:
        sSpecificRelife = oTarget.Query('SpecificRelife')
        if sSpecificRelife and sSpecificRelife != sKey:
            SendAlert('err', '%s多来源设置设置唯一复活%s' % (sKey, sSpecificRelife))
            return None
        oTarget.Set('SpecificRelife', sKey)
    iTimes = cl_formula.GetResultByData(oTarget, iTimes, {
        'LifeCycle': oLifeCycle })
    oLifeCycle.AlreadyDoDisableFunc(oTarget, ClearSetRelifeAttr.__name__)
    oTarget.AddRelifeInfo(iType, sKey, iTime, iTimes, iPriority, iMaxTimes = iMaxTimes)
    if oTarget.m_FightType & WARRIOR_MONSTER:
        iOwnerSID = oLifeCycle.GetObject().m_SID
        oTarget.AddHatchRatio(iOwnerSID, iType, sKey, dHatchRatio)
    oLifeCycle.AddDisableFunc(ClearSetRelifeAttr)


def CommonAddHeroBuyRule(oTarget, oLifeCycle, iRule, iValue):
    
    def ClearAddHeroBuyRule(oTarget, oLifeCycle):
        oTarget.m_BuyMgr.RemoveRule(iRule, sKey)

    sKey = oLifeCycle.Key()
    iValue = cl_formula.GetResultByData(oTarget, iValue, {
        'LifeCycle': oLifeCycle })
    oTarget.m_BuyMgr.AddRule(iRule, sKey, iValue)
    oLifeCycle.AddDisableFunc(ClearAddHeroBuyRule)


def CommonAddExtraPickUpRule(oTarget, oLifeCycle, iRule):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.RemoveExtraPickUpRule(iRule)

    if not oTarget.m_FightType & WARRIOR_HERO:
        return None
    oTarget.AddExtraPickUpRule(iRule)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonSetMonsterAgentConfig(oTarget, oLifeCycle, sKey, iValue):
    
    def ClearMonsterAgentConfig(oTarget, oLifeCycle):
        if not oTarget.m_Agent:
            return None
        oTarget.m_Agent.m_Config[sKey] = iOldValue

    if oTarget.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
        return None
    if not oTarget.m_Agent:
        return None
    if sKey not in oTarget.m_Agent.m_Config:
        return None
    iOldValue = oTarget.m_Agent.m_Config[sKey]
    oTarget.m_Agent.m_Config[sKey] = iValue
    oLifeCycle.AddDisableFunc(ClearMonsterAgentConfig)


def CommonReplaceMonsterAIPF(oTarget, oLifeCycle, iOldPF, iNewPF, iInheritCondition = 0):
    if not oTarget.m_FightType & WARRIOR_MONSTER:
        return None
    if not oTarget.m_Agent:
        return None
    oPFAI = oTarget.m_Agent.m_PFAI
    dPFGroup = oPFAI.m_PFGroup
    if not dPFGroup:
        return None
    dPFGroup = DeepCopy(dPFGroup)
    for iGroup in dPFGroup:
        for lstInfo in dPFGroup[iGroup].values():
            if lstInfo[0] == iOldPF:
                lstInfo[0] = iNewPF
        
    
    oPFAI.m_PFGroup = dPFGroup
    if iInheritCondition or iOldPF in oPFAI.m_CheckPFCanUse:
        dNewCondiction = dict(oPFAI.m_CheckPFCanUse)
        oCondition = dNewCondiction.pop(iOldPF)
        dNewCondiction[iNewPF] = oCondition
        oPFAI.m_CheckPFCanUse = dNewCondiction
    elif iNewPF in oPFAI.m_CheckPFCanUse:
        dNewCondiction = dict(oPFAI.m_CheckPFCanUse)
        dNewCondiction.pop(iNewPF)
        oPFAI.m_CheckPFCanUse = dNewCondiction


def CommonSetPFAIGroupWeightByType(oTarget, oLifeCycle, iType, iPerform, iValue):
    if not oTarget.m_FightType & WARRIOR_MONSTER:
        return None
    if not oTarget.m_Agent:
        return None
    oPFAI = oTarget.m_Agent.m_PFAI
    if not oPFAI:
        return None
    lstGroupOfPF = oPFAI.m_GroupOfPF.get(iPerform, [])
    if not lstGroupOfPF:
        sKey = oLifeCycle.Key()
        SendAlert('err', '%s 怪物:%s 技能AI:%s 不存在技能组技能%s' % (sKey, oTarget.m_SID, oPFAI.m_SID, iPerform))
        return None
    dChoosePFInfo = oPFAI.m_ChoosePFInfo
    if dChoosePFInfo:
        ChangePFAIGroupWeight(oPFAI, dChoosePFInfo, iType, lstGroupOfPF, iValue)


def CommonDirectSetPFAIGroupWeight(oTarget, oLifeCycle, iType, dPfGroup):
    if not oTarget.m_FightType & WARRIOR_MONSTER:
        return None
    if not oTarget.m_Agent:
        return None
    oPFAI = oTarget.m_Agent.m_PFAI
    if not oPFAI:
        return None
    sKey = oLifeCycle.Key()
    for iPfGroupSID, iWeight in dPfGroup.items():
        if iPfGroupSID not in oPFAI.m_PFGroup:
            SendAlert('err', '%s 怪物:%s 技能AI:%s 不存在技能组%s' % (sKey, oTarget.m_SID, oPFAI.m_SID, iPfGroupSID))
        dChoosePFInfo = oPFAI.m_ChoosePFInfo
        if dChoosePFInfo:
            ChangePFAIGroupWeight(oPFAI, dChoosePFInfo, iType, [
                iPfGroupSID], iWeight)
    


def ChangePFAIGroupWeight(oPFAI, dInfo, iType, lstGroupOfPF, iValue):
    dNewInfo = { }
    dNewChoosePFInfo = { }
    dNewChoosePFInfo.update(dInfo)
    for tRestrict, tInfo in dNewChoosePFInfo[iType].items():
        lstInfo = []
        for dAction in tInfo:
            dNewAction = { }
            dNewPFInfo = { }
            dNewAction.update(dAction)
            dAllPFInfo = dNewAction.get('choose')
            dNewPFInfo.update(dAllPFInfo)
            for iPFGroup in lstGroupOfPF:
                if iPFGroup in dNewPFInfo:
                    dNewPFInfo[iPFGroup] = iValue
            
            dNewAction['choose'] = dNewPFInfo
            lstInfo.append(dNewAction)
        
        dNewInfo[tRestrict] = lstInfo
    
    dNewChoosePFInfo[iType] = dNewInfo
    oPFAI.m_ChoosePFInfo = dNewChoosePFInfo


def CommonSetPFAIGroupWeightByPhase(oTarget, oLifeCycle, iTargetType, iTargetPhase, iPerformGroup, iValue):
    if not oTarget.m_FightType & WARRIOR_MONSTER:
        return None
    if not oTarget.m_Agent:
        return None
    oPFAI = oTarget.m_Agent.m_PFAI
    if not oPFAI:
        return None
    dChoosePFInfo = oPFAI.m_ChoosePFInfo
    if iTargetType not in dChoosePFInfo:
        return None
    if iPerformGroup not in oPFAI.m_PFGroup:
        sKey = oLifeCycle.Key()
        SendAlert('err', '%s 怪物:%s 技能AI:%s 不存在技能组%s' % (sKey, oTarget.m_SID, oPFAI.m_SID, iPerformGroup))
        return None
    dNewInfo = { }
    dNewChoosePFInfo = { }
    dNewChoosePFInfo.update(dChoosePFInfo)
    for tRestrict, tInfo in dChoosePFInfo[iTargetType].items():
        lstInfo = []
        (_, _, _, _, _, _, iPhase) = tRestrict
        for dAction in tInfo:
            dNewAction = { }
            dNewPFInfo = { }
            dNewAction.update(dAction)
            dAllPFInfo = dNewAction.get('choose')
            dNewPFInfo.update(dAllPFInfo)
            if iPhase == iTargetPhase:
                dNewPFInfo[iPerformGroup] = iValue
            dNewAction['choose'] = dNewPFInfo
            lstInfo.append(dNewAction)
        
        dNewInfo[tRestrict] = lstInfo
    
    dNewChoosePFInfo[iTargetType] = dNewInfo
    oPFAI.m_ChoosePFInfo = dNewChoosePFInfo


def CommonSetMonsterAIPFGroupCnt(oTarget, oLifeCycle, iGroup, iPF, iCntLower, iCntUpper):
    if not oTarget.m_FightType & WARRIOR_MONSTER:
        return None
    if not oTarget.m_Agent:
        return None
    oPFAI = oTarget.m_Agent.m_PFAI
    dPFGroup = oPFAI.m_PFGroup
    if not dPFGroup or iGroup not in dPFGroup:
        return None
    dPFGroup = DeepCopy(dPFGroup)
    dPFGroupItem = dPFGroup[iGroup]
    for lstInfo in dPFGroupItem.values():
        if lstInfo[0] == iPF:
            lstInfo[1] = iCntLower
            lstInfo[2] = iCntUpper
    
    oPFAI.m_PFGroup = dPFGroup


def CommonSetMonsterAIPFGroupDelay(oTarget, oLifeCycle, iPerform, iMul):
    if not oTarget.m_FightType & WARRIOR_MONSTER:
        return None
    if not oTarget.m_Agent:
        return None
    oPFAI = oTarget.m_Agent.m_PFAI
    lstGroupOfPF = oPFAI.m_GroupOfPF.get(iPerform, [])
    if not lstGroupOfPF:
        sKey = oLifeCycle.Key()
        SendAlert('err', '%s 怪物:%s 技能AI:%s 不存在技能组技能%s' % (sKey, oTarget.m_SID, oPFAI.m_SID, iPerform))
        return None
    dPFGroup = oPFAI.m_PFGroup
    dPFGroup = DeepCopy(dPFGroup)
    for iGroup in lstGroupOfPF:
        for lstInfo in dPFGroup[iGroup].values():
            if lstInfo[0] == iPerform:
                lstInfo[3] = lstInfo[3] * iMul // 100
        
    
    oPFAI.m_PFGroup = dPFGroup


def CommonSetMonsterAccuracyFactor(oTarget, oLifeCycle, iValue):
    if not oTarget.m_FightType & WARRIOR_MONSTER:
        return None
    oTarget.m_AccuracyFactor = iValue


def CommonSetMonsterMissingDisTypeByRound(oTarget, oLifeCycle, dRoundInfo):
    if not oTarget.m_FightType & WARRIOR_MONSTER:
        return None
    dBaseData = oTarget.m_MissingDisType
    oTarget.m_MissingDisType = { }
    oTarget.m_MissingDisType.update(dBaseData)
    for iRound, iType in dRoundInfo.items():
        oTarget.m_MissingDisType[iRound] = iType
    


def CommonSetFillMinBullet(oTarget, oLifeCycle, iMinBullet):
    if not oTarget.m_FightType & WARRIOR_MONSTER:
        return None
    if not oTarget.m_Agent:
        return None
    oPFAI = oTarget.m_Agent.m_PFAI
    if not oPFAI:
        return None
    tFillBulletData = oPFAI.m_FillBulletData
    if tFillBulletData:
        (iPerform, _, fRatio) = tFillBulletData
        oPFAI.m_FillBulletData = (iPerform, iMinBullet, fRatio)


def CommonSetMonsterDodgeCD(oTarget, oLifeCycle, iNewCD):
    if not oTarget.m_FightType & WARRIOR_MONSTER:
        return None
    if not oTarget.m_Agent:
        return None
    dConfig = oTarget.m_Agent.GetData('Dodge')
    if dConfig:
        dConfig['CD'] = Time2Frame(iNewCD)


def ConmonReplaceMonsterPFAI(oTarget, oLifeCycle, iPFAI):
    if not (oTarget.m_FightType & WARRIOR_MONSTER) or not (oTarget.m_Agent):
        return None
    oNewPFAI = cl_betree.pfai.NewPFAI(iPFAI, oTarget)
    if not oNewPFAI:
        return None
    oAgent = oTarget.m_Agent
    if oAgent.m_PFAI:
        oAgent.m_PFAI.Release()
    oAgent.m_PFAI = oNewPFAI


def CommonSummonObstacleUsePerform(oTarget, oLifeCycle, iPrefab, iPerform):
    oGame = oTarget.m_Game
    iScene = oTarget.m_Scene
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return None
    lstSummon = oScene.GetObjectsByType('Summon')
    for iSummon in lstSummon:
        oSummon = oGame.GetObject(iSummon)
        if oSummon and oSummon.m_Prefab == iPrefab:
            oSummon.ObstacleUsePerform(iPerform)
    


def CommonSummonUsePerform(oTarget, oLifeCycle, iSID, iPerform):
    oGame = oTarget.m_Game
    iScene = oTarget.m_Scene
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return None
    lstSummon = oScene.GetObjectsByType('Summon')
    for iSummon in lstSummon:
        oSummon = oGame.GetObject(iSummon)
        if (not oSummon or iSID) and oSummon.m_SID != iSID:
            continue
        oPerform = oSummon.GetPerformIfNoThenNew(iPerform)
        if not oPerform:
            continue
        cl_war.UsePerform(oSummon, oPerform, { })
    


def CommonSetSummonLifeTime(oTarget, oLifeCycle, iTime):
    if not oTarget.m_FightType & WARRIOR_SUMMON:
        sKey = oLifeCycle.Key()
        SendAlert('err', '%s拥有者非召唤物' % sKey)
        return None
    oTarget.SetLifeFrame(Time2Frame(iTime))


def CommonOwnSummonDie(oTarget, oLifeCycle, iSID):
    oGame = oTarget.m_Game
    iScene = oTarget.m_Scene
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return None
    iOwner = oTarget.m_ID
    lstSummon = oScene.GetObjectsByType('Summon')
    oReason = cl_object.reason.CStrReason(oLifeCycle.Key(), None, {
        'DamType': DAM_TYPE_SCENE | DAM_USE_HP })
    for iSummon in lstSummon:
        oSummon = oGame.GetObject(iSummon)
        if not oSummon or oSummon.m_Owner != iOwner:
            continue
        if iSID and oSummon.m_SID != iSID:
            continue
        oSummon.HPModifyDam(iOwner, [
            [
                oSummon.HP(),
                oReason]])
    


def CommonSelfDie(oTarget, oLifeCycle):
    sKey = oLifeCycle.Key()
    oReason = cl_object.reason.CStrReason(sKey, None, {
        'DamType': DAM_TYPE_SCENE | DAM_USE_HP })
    oTarget.Set('RelifeInfo', { })
    oTarget.SetDiePriority(DIE_PRIORITY_KILL, sKey)
    oTarget.HPDirectModify('HP', 0, -(oTarget.m_HP), oReason)
    oTarget.ClearDiePriority(sKey)


def CommonAssignMonsterDie(oTarget, oLifeCycle, dSID):
    oGame = oTarget.m_Game
    iScene = oTarget.m_Scene
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return None
    iOwner = oTarget.m_ID
    lstTarget = oScene.GetObjectsByType('Monster')
    oReason = cl_object.reason.CStrReason(oLifeCycle.Key(), None, {
        'DamType': DAM_TYPE_SCENE | DAM_USE_HP })
    for iMonster in lstTarget:
        oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
        if not oMonster:
            continue
        if oMonster.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER or oMonster.m_SID not in dSID:
            continue
        oMonster.HPModifyDam(iOwner, [
            [
                oMonster.HP(),
                oReason]])
    


def CommonRemoveSelf(oTarget, oLifeCycle):
    if oTarget.IsDead():
        return None
    oTarget.m_Dead = DEAD_FLAG_DIED
    oTarget.ResetByDie()
    oGame = oTarget.m_Game
    oGame.SetPyFlag(oTarget.m_ID, PY_FLAG_DIED, 1)
    if oTarget.m_FightType & CTRLWARRIOR_MASK and oTarget.m_PhyModel:
        oTarget.m_PhyModel.SetCtrlFlag(CTRL_FLAG_FOR_DEAD, 0)
    oTarget.DieClearEffect()
    oTarget.LeaveScene(0)
    oTarget.RemoveFromScene()
    oTarget.m_RemoveDelay = 1
    oTarget.DieRemove()


def CommonSubPointPerformColdTime(oTarget, oLifeCycle, iPerform, iTime, iPercent):
    iColdTimeFrame = oTarget.m_Perform.GetTotalColdTime(iPerform)
    if not iColdTimeFrame:
        return None
    dData = {
        'LifeCycle': oLifeCycle }
    iTime = cl_formula.GetResultByData(oTarget, iTime, dData)
    iFrame = Time2Frame(iTime)
    iPercent = cl_formula.GetResultByData(oTarget, iPercent, dData)
    if iPercent > 0:
        iMaxColdTimeFrame = oTarget.m_Perform.GetMaxColdTime(iPerform)
        iFrame += iMaxColdTimeFrame * iPercent // 100
    oTarget.m_Perform.ModifyColdTime(iPerform, -iFrame)


def CommonSubCareerPerformColdTime(oTarget, oLifeCycle, iTime, iPercent):
    pfobj = oTarget.GetCareerPerform()
    if not pfobj:
        return None
    iPerform = pfobj.m_SID
    iColdTimeFrame = oTarget.m_Perform.GetTotalColdTime(iPerform)
    if not iColdTimeFrame:
        return None
    dData = {
        'LifeCycle': oLifeCycle }
    iTime = cl_formula.GetResultByData(oTarget, iTime, dData)
    iFrame = Time2Frame(iTime)
    if iPercent:
        iPercent = cl_formula.GetResultByData(oTarget, iPercent, dData)
        iMaxColdTimeFrame = oTarget.m_Perform.GetMaxColdTime(iPerform)
        iFrame += iMaxColdTimeFrame * iPercent // 100
    oTarget.m_Perform.ModifyColdTime(iPerform, -iFrame)


def CommonFullPerformColdTime(oTarget, oLifeCycle, iPerform):
    if oTarget.Query('DebugStatus', 0) & DEBUG_STATUS_NOPFCD == DEBUG_STATUS_NOPFCD:
        return 0
    oPerform = oTarget.m_Perform.GetPerform(iPerform)
    if not oPerform:
        return None
    iPerformCDFrame = oPerform.GetCDTime(oTarget)
    iColdTimeFrame = oTarget.m_Perform.GetNowCoverRemainTime(iPerform)
    oTarget.m_Perform.AddColdTime(iPerform, iPerformCDFrame - iColdTimeFrame)


def CommonAddBagBullet(oTarget, oLifeCycle, iBullet, iAmount, iClientBehavior):
    sKey = oLifeCycle.Key()
    dData = {
        'LifeCycle': oLifeCycle }
    iBullet = cl_formula.GetResultByData(oTarget, iBullet, dData)
    iAmount = cl_formula.GetResultByData(oTarget, iAmount, dData)
    if iAmount < 0:
        iHasBullet = oTarget.m_BulletCon.Bullet(iBullet)
        if iHasBullet + iAmount < 0:
            iAmount = 0 - iHasBullet
    oTarget.m_BulletCon.BulletModify(iBullet, iAmount, sKey)
    if iClientBehavior:
        cl_snetwar.GS2CTriggerBehavior(oTarget.m_Game, oTarget.m_ID, iClientBehavior, [
            oTarget.m_PlayerID], 0)


def CommonRandomDeductWeaponBagBullet(oTarget, oLifeCycle, iAmount, iClientBehavior, bExcludeMainHold = 0):
    dHoldType = { }
    if bExcludeMainHold:
        lstWeapon = oTarget.m_WieldCon.GetHoldWeapon()
        for oWeapon, _ in lstWeapon:
            if oWeapon.m_Type == itemdef.EQUIP_TYPE_FUNDAMENTALWEAPON:
                continue
            oBulletCom = oWeapon.GetComponent('Bullet')
            if not oBulletCom:
                continue
            dHoldType[oBulletCom.m_BulletType] = 1
        
    dBulletType = { }
    for iType in itemload.GetAllWeaponBulletType():
        if iType in dHoldType:
            continue
        if oTarget.m_BulletCon.Bullet(iType) > 0:
            dBulletType[iType] = 1
    
    if not dBulletType:
        return None
    iBullet = ChooseKey(oTarget.m_Game, dBulletType)
    CommonAddBagBullet(oTarget, oLifeCycle, iBullet, -iAmount, iClientBehavior)


def CommonDeductWeaponBagBulletByWeight(oTarget, oLifeCycle, iAmount, dWeight, iClientBehavior, bExcludeMainHold):
    if not iAmount:
        return None
    dConsumed = { }
    dTypeNum = { }
    if bExcludeMainHold:
        oWeapon = oTarget.m_WieldCon.GetCurWeapon()
        if oWeapon:
            oBulletCom = oWeapon.GetComponent('Bullet')
            if oBulletCom and oWeapon.m_Type != itemdef.EQUIP_TYPE_FUNDAMENTALWEAPON and oBulletCom.m_BulletType in dWeight:
                dWeight.pop(oBulletCom.m_BulletType)
    for iType in list(dWeight.keys()):
        if dWeight[iType] == 0 or oTarget.m_BulletCon.Bullet(iType) == 0:
            dWeight.pop(iType)
            continue
        dTypeNum[iType] = oTarget.m_BulletCon.Bullet(iType)
    
    if not dWeight:
        return None
    for _ in range(iAmount):
        iChosen = ChooseKey(oTarget.m_Game, dWeight)
        if iChosen in dConsumed:
            dConsumed[iChosen] += 1
        else:
            dConsumed[iChosen] = 1
        if dTypeNum[iChosen] - dConsumed[iChosen] <= 0:
            dWeight.pop(iChosen)
            if not dWeight:
                break
    
    for iBullet, iCost in dConsumed.items():
        CommonAddBagBullet(oTarget, oLifeCycle, iBullet, -iCost, iClientBehavior)
    


def CommonRandomAddWeaponBagBullet(oTarget, oLifeCycle, iAmount, iClientBehavior):
    dBulletType = { }
    for iType in itemload.GetAllWeaponBulletType():
        if oTarget.m_BulletCon.Bullet(iType) < oTarget.m_BulletCon.GetMaxBullet(iType):
            dBulletType[iType] = 1
    
    if not dBulletType:
        return None
    iBullet = ChooseKey(oTarget.m_Game, dBulletType)
    CommonAddBagBullet(oTarget, oLifeCycle, iBullet, iAmount, iClientBehavior)


def CommonAddThrowBagBullet(oTarget, oLifeCycle, iAmount, iClientBehavior):
    oPerform = oTarget.GetThrowPerform()
    if not oPerform:
        return None
    iBullet = oPerform.CalAttr('BulletSID')
    CommonAddBagBullet(oTarget, oLifeCycle, iBullet, iAmount, iClientBehavior)


def CommonSetImmobilize(oTarget, oLifeCycle):
    
    def ClearImmobilize(oTarget, oLifeCycle):
        oTarget.ClearImmobilize(sKey, iAID)
        dImmobilizeInner = oTarget.Query('Immobilize', { })
        dImmobilizeInner.pop(sKey, None)
        oTarget.Set('Immobilize', dImmobilizeInner)

    if oTarget.m_Scene == 0:
        return None
    if not oTarget.m_FightType & WARRIOR_MONSTER:
        return None
    if oTarget.CheckLogicKey(FIGHT3_KEY_IGNOREIMMOBILIZE):
        return None
    oState = oLifeCycle.GetObject()
    iAID = oState.m_StateInfo['AID']
    oState.m_Data['ImmobilizeFrame'] = oTarget.m_Game.GetFrameNum()
    oLifeCycle.AddDisableFunc(ClearImmobilize)
    sKey = oLifeCycle.Key()
    oTarget.SetImmobilize(sKey, iAID)
    sCDKey = 'ImmobilizeCDMark'
    iNowFrame = oTarget.m_Game.GetFrameNum()
    oTarget.Set(sCDKey, iNowFrame)
    dImmobilize = oTarget.Query('Immobilize', { })
    dImmobilize[sKey] = 1
    oTarget.Set('Immobilize', dImmobilize)


def CommonWalkToGround(oTarget, oLifeCycle):
    iScene = oTarget.m_Scene
    if not iScene:
        return None
    if oTarget.m_MoveCtrl.m_CurStatus == STATUS_JUMP:
        tTargetPos = oTarget.m_MoveCtrl.m_JumpStart
    else:
        tTargetPos = oTarget.GetGroundPos()
    sKey = oLifeCycle.Key()
    tPos = oTarget.GetPos()
    oTarget.WalkTo(tTargetPos, sKey)
    WarobjLog.Debug('game:%d, commonwalkto, %s, %s, %s' % (oTarget.m_Game.m_ID, tPos, tTargetPos, sKey))


def CommonReduceActionSpeed(oTarget, oLifeCycle, iValue, iRecoverTime, iRecoverValue, iToughEffect = 0):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.ClearActionSpeedEffect(sKey)

    if not oTarget.m_FightType & WARRIOR_MONSTER:
        return None
    iCurFrame = oTarget.m_Game.GetFrameNum()
    if oTarget.Query('ActionSpeedCD', 0) > iCurFrame:
        return None
    oTarget.Set('ActionSpeedCD', iCurFrame + ACTION_SPEED_CD)
    sKey = oLifeCycle.Key()
    iValue = cl_formula.GetResultByData(oTarget, iValue, {
        'LifeCycle': oLifeCycle })
    if iToughEffect:
        iValue = iValue * (100 - oTarget.QueryAttr('Toughness')) // 100
    iRecoverTime = cl_formula.GetResultByData(oTarget, iRecoverTime, {
        'LifeCycle': oLifeCycle })
    iRecoverFrame = Time2Frame(iRecoverTime)
    oTarget.ReduceActionSpeed(sKey, iValue, iRecoverFrame, iRecoverValue)
    oLifeCycle.AddDisableFunc(ClearFunc)
    oState = oLifeCycle.GetObject()
    oAttack = oTarget.m_Game.GetObject(oState.m_StateInfo['AID'])
    if oAttack:
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CAUSE_REDUCEACTIONSPEED, oAttack, {
            'StateSID': oState.m_SID,
            'ActionSpeed': iValue })


def CommonUnbalance(oTarget, oLifeCycle):
    
    def ClearUnbalance(oTarget, oLifeCycle):
        oTarget.ClearUnbalance(iAID)

    if not oTarget.m_FightType & WARRIOR_MONSTER:
        return None
    if oTarget.CheckLogicKey(FIGHT3_KEY_IGNOREIMMOBILIZE) or oTarget.CheckLogicKey(FIGHT3_KEY_IGNOREUNBALANCE):
        return None
    oState = oLifeCycle.GetObject()
    iAID = oState.m_StateInfo['AID']
    oTarget.Unbalance(iAID)
    oLifeCycle.AddDisableFunc(ClearUnbalance)


def CommonSendMessage(oTarget, oLifeCycle, iMsg, iSubMsg, dInfo = None):
    if dInfo:
        dInfo = cl_formula.CalArgsFormula(oTarget, dInfo, {
            'LifeCycle': oLifeCycle })
    else:
        dInfo = { }
    cl_msgcenter.SendMsg(iMsg, oTarget, dInfo, iSub = iSubMsg)


def CommonTriggerGateCtrl(oTarget, oLifeCycle, iAction, iDelay):
    
    def DelayDoAction(oGame, iObstacleID, iAction):
        oObstacle = oGame.GetObject(iObstacleID)
        if not oObstacle:
            return None
        oObstacle.DoAction(iAction, { })

    iFightType = oTarget.m_FightType
    if iFightType not in (WARRIOR_OBSTACLE_CTRLGATE, WARRIOR_OBSTACLE_VICCTRL):
        return None
    oGame = oTarget.m_Game
    iTime = cl_formula.GetResultByData(oTarget, iDelay, {
        'LifeCycle': oLifeCycle })
    if not iTime:
        oTarget.DoAction(iAction, { })
    else:
        oTarget.Call_Out(Functor(DelayDoAction, oGame, oTarget.m_ID, iAction), Time2Frame(iTime), 'DelayTriggerGateCtrl')


def CommonAddWarCash(oTarget, oLifeCycle, iCash):
    iCash = cl_formula.GetResultByData(oTarget, iCash, {
        'LifeCycle': oLifeCycle })
    oTarget.AddCash(iCash, oLifeCycle.Key())


def CommonSetSkillCheckArgs(oTarget, oLifeCycle, fRadius, fHeight):
    
    def ClearSkillCheckArgs(oTarget, oLifeCycle):
        oTarget.ClearSkillCheckArgs()

    if fRadius and fHeight:
        oTarget.SetSkillCheckArgs(fRadius, fHeight)
        oLifeCycle.AddDisableFunc(ClearSkillCheckArgs)


def CommonAddSkillCheckExtraArgs(oTarget, oLifeCycle, fRadius, fHeight):
    
    def ClearSkillCheckExtraArgs(oTarget, oLifeCycle):
        oTarget.ClearSkillCheckExtraArgs(oLifeCycle.Key())

    oTarget.AddSkillCheckExtraArgs(oLifeCycle.Key(), fRadius, fHeight)
    oLifeCycle.AddDisableFunc(ClearSkillCheckExtraArgs)


def CommonGetSkillCheckArgs(oTarget, oLifeCycle, iIndex):
    return oTarget.SkillCheckArgs[iIndex]


def CommonSetBulletPickModule(oTarget, oLifeCycle, iModule):
    
    def ClearBulletPickModule(oTarget, oLifeCycle):
        oBulletCon.m_DropModule -= iModule

    oBulletCon = oTarget.m_BulletCon
    oBulletCon.m_DropModule += iModule
    oLifeCycle.AddDisableFunc(ClearBulletPickModule)


def CommonPauseMonsterOwnerAgent(oTarget, oLifeCycle):
    
    def ClearPauseMonsterOwnerAgent(oTarget, oLifeCycle):
        if oTarget.m_Agent:
            oTarget.m_Agent.ResumeAgent(sKey)

    if not (oTarget.m_FightType & WARRIOR_MONSTER) and not (oTarget.m_FightType & WARRIOR_SERVANT):
        return None
    if not oTarget.m_Agent:
        return None
    sKey = oLifeCycle.Key()
    oTarget.m_Agent.PauseAgent(sKey)
    oLifeCycle.AddDisableFunc(ClearPauseMonsterOwnerAgent)


def CommonPauseOwnObjAgent(oTarget, oLifeCycle, iObjectType):
    
    def ClearPauseOwnObjAgent(oTarget, oLifeCycle):
        oWarrior = oGame.GetObject(iWarrior)
        if not oWarrior:
            return None
        oAgent = oWarrior.m_Agent
        if oAgent:
            oAgent.ResumeAgent(sKey)

    sKey = oLifeCycle.Key()
    iWarrior = oTarget.GetOwnObjectID(iObjectType)
    oGame = oTarget.m_Game
    oWarrior = oGame.GetObject(iWarrior)
    if not oWarrior:
        return None
    oAgent = oWarrior.m_Agent
    if not oAgent:
        return None
    oAgent.PauseAgent(sKey)
    oLifeCycle.AddDisableFunc(ClearPauseOwnObjAgent)


def CommonPausePlayerStateCounter(oTarget, oLifeCycle, iPauseTime, iState):
    
    def ResumeDyingState(oTarget, oLifeCycle):
        oTarget.Remove_Call_Out('PauseDying%s' % oTarget.m_ID)
        for iHero in lstHero:
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            oState = oHero.m_State.GetItemBySID(iState)
            if not oState:
                continue
            oState.StartCount(oHero)
        

    oLifeCycle.AddDisableFunc(ResumeDyingState)
    oGame = oTarget.m_Game
    lstHero = oGame.m_WarMgr.GetRoomHero()
    iPauseTime = cl_formula.GetResultByData(oTarget, iPauseTime, {
        'LifeCycle': oLifeCycle })
    oTarget.Call_Out(Functor(ResumeDyingState, oTarget, oLifeCycle), Time2Frame(iPauseTime), 'PauseDying%s' % oTarget.m_ID)
    for iHero in lstHero:
        oHero = oGame.GetObject(iHero)
        if not oHero:
            continue
        oState = oHero.m_State.GetItemBySID(iState)
        if not oState:
            continue
        oState.StopCount(oHero)
    


def CommonSetOwnerWeaponExtraInscriptionCost(oTarget, oLifeCycle, iCost):
    oTarget.Set('WeaponExtraInscriptionCost', iCost)


def CommonSetOwnerWeaponExtraEtchingCost(oTarget, oLifeCycle, dCost):
    
    def ClearFun(oTarget, oLifeCycle):
        oTarget.Delete('WeaponExtraEtchingCost')

    oTarget.Set('WeaponExtraEtchingCost', dCost)
    oLifeCycle.AddDisableFunc(ClearFun)


def CommonForceSetOwnerWeaponUpgradeCost(oTarget, oLifeCycle, iCost):
    
    def ClearForceSetOwnerWeaponUpgradeCost(oTarget, oLifeCycle):
        oTarget.Delete('ForceSetWeaponUpgradeCost')

    iCost = cl_formula.GetResultByData(oTarget, iCost, {
        'LifeCycle': oLifeCycle })
    oTarget.Set('ForceSetWeaponUpgradeCost', iCost)
    oLifeCycle.AddDisableFunc(ClearForceSetOwnerWeaponUpgradeCost)


def CommonForceSetOwnerWeaponUpgradeLevel(oTarget, oLifeCycle, iLevel):
    
    def ClearForceSetOwnerWeaponUpgradeLevel(oTarget, oLifeCycle):
        oTarget.Delete('ForceSetWeaponUpgradeLevel')

    iLevel = cl_formula.GetResultByData(oTarget, iLevel, {
        'LifeCycle': oLifeCycle })
    oTarget.Set('ForceSetWeaponUpgradeLevel', iLevel)
    oLifeCycle.AddDisableFunc(ClearForceSetOwnerWeaponUpgradeLevel)


def CommonForceSetOwnerWeaponUpgradeGenCash(oTarget, oLifeCycle):
    
    def ClearForceSetOwnerWeaponUpgradeGenCash(oTarget, oLifeCycle):
        oTarget.Delete('PriceReverse')

    oTarget.Set('PriceReverse', 1)
    oLifeCycle.AddDisableFunc(ClearForceSetOwnerWeaponUpgradeGenCash)


def CommonForceSetOwnerWeaponUpgradeUnlimit(oTarget, oLifeCycle, iUnlimit):
    
    def ClearForceSetOwnerWeaponUpgradeUnlimit(oTarget, oLifeCycle):
        oTarget.Delete('ForceSetWeaponUpgradeUnlimit')

    oTarget.Set('ForceSetWeaponUpgradeUnlimit', iUnlimit)
    oLifeCycle.AddDisableFunc(ClearForceSetOwnerWeaponUpgradeUnlimit)


def CommonEnablePerform(oTarget, oLifeCycle, iPerform):
    
    def ClearFunc(oTarget, oLifeCycle):
        oClearPerform = oTarget.GetPerform(iPerform)
        if not oClearPerform:
            return None
        oClearPerform.Disable(oTarget)

    oPerform = oTarget.GetPerformIfNoThenNew(iPerform)
    if not oPerform:
        return None
    oPerform.Enable(oTarget)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonDisablePF(oTarget, oLifeCycle, iPerform, iClear = 0):
    
    def ClearFunc(oTarget, oLifeCycle):
        oClearPerform = oTarget.GetPerform(iPerform)
        if oClearPerform:
            oClearPerform.Enable(oTarget, iNotify = 1)

    oPerform = oTarget.GetPerform(iPerform)
    if oPerform:
        oPerform.Disable(oTarget, iNotify = 1)
        if iClear:
            oLifeCycle.AddDisableFunc(ClearFunc)


def CommonRecordMoveDis(oTarget, oLifeCycle, sBaseKey):
    sKey = 'MoveDis%s' % sBaseKey
    vNow = oTarget.GetPos()
    tLast = oTarget.Query(sKey, None)
    if tLast:
        (vLast, fLastDis) = tLast
        fNewDis = cl_math.CalDistance(vLast, vNow) + fLastDis
    else:
        fNewDis = 0
    oTarget.Set(sKey, (vNow, fNewDis))


def CommonChangeMoveDis(oTarget, oLifeCycle, sBaseKey, iVal):
    sKey = 'MoveDis%s' % sBaseKey
    tLast = oTarget.Query(sKey, None)
    if tLast:
        (_, fDis) = tLast
        iVal = cl_formula.GetResultByData(oTarget, iVal, {
            'LifeCycle': oLifeCycle })
        fDis = fDis + iVal
        if fDis < 0:
            fDis = 0
        oTarget.Set(sKey, (oTarget.GetPos(), fDis))


def CommonAttentionOwnerRoomGoalCallBack(oTarget, oLifeCycle, iGroup):
    
    def ClearAttention(oTarget, oLifeCycle):
        cl_msgcenter.DoneAttention(oTarget, oLevelCtrl.m_ID, iMsg, sKey)

    
    def RoomGoalCallBack(oTarget, oLevelCtrl, dMsgInfo):
        iLevel = dMsgInfo['Level']
        iRoom = dMsgInfo['Room']
        (iTargetLevel, iTargetRoom, _) = oTarget.m_LineIdx
        if iLevel != iTargetLevel or iRoom != iTargetRoom:
            return None
        dEvent = oLifeCycle.AttrCache()
        dEvent['LifeCycle'] = oLifeCycle
        oEventCB = oLifeCycle.GetObject().m_EventCB
        oEventCB.CBFuncAction(oTarget, iGroup, dEvent, dMsgInfo)

    if not oTarget.m_LineIdx:
        return None
    iMsg = cl_msgcenter.MSG_LEVEL_ROOMGOAL
    oWarMgr = oTarget.m_Game.GetWarMgr()
    oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
    sKey = 'CommonAttentionOwnerRoomGoalCallBack_%d' % oTarget.m_ID
    cl_msgcenter.AddAttentionFunc(oTarget, oLevelCtrl.m_ID, iMsg, RoomGoalCallBack, sKey)
    oLifeCycle.AddDisableFunc(ClearAttention)


def CommonSetPhase(oTarget, oLifeCycle, iPhase):
    if oTarget.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
        return None
    iPhase = cl_formula.GetResultByData(oTarget, iPhase, {
        'LifeCycle': oLifeCycle })
    oTarget.SetPhase(iPhase)


def CommonAddPerform(oTarget, oLifeCycle, iPerform):
    
    def ClearFunc(oTarget, oLifeCycle):
        oPerform = oTarget.GetPerform(iPerform)
        if not oPerform:
            return None
        dSourceInfo = oPerform.GetArgValue('SourceInfo', { })
        if sKey in dSourceInfo:
            dSourceInfo.pop(sKey)
        if not dSourceInfo:
            oPerform.DelArgValue('SourceInfo')
            oTarget.RemovePerform(iPerform)

    oPerform = oTarget.AddPerform(iPerform, 1)
    dSourceInfo = oPerform.SetArgValueDefault('SourceInfo', { })
    sKey = oLifeCycle.Key()
    dSourceInfo[sKey] = 1
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonAddRelic(oTarget, oLifeCycle, iRelic, iLevel, iIgnoreLock, iOwnedDrop):
    setUnlock = oTarget.Query('Illus')['Relic']
    sKey = oLifeCycle.Key()
    if iRelic not in setUnlock and not iIgnoreLock:
        SendAlert('err', f'''{sKey} 通用添加遗物 添加了未解锁遗物 {iRelic} ，请检查''')
        return None
    oRelicCon = oTarget.m_RelicCon
    oRelic = oRelicCon.GetPerform(iRelic)
    if oRelic:
        if not iOwnedDrop:
            return None
        dStaticInfo = {
            'DropLevel': iLevel,
            'DropSource': oRelicCon.m_PlayerID }
        cl_drop.DropPerform(oTarget, iRelic, dStaticInfo, True)
    else:
        dReward = {
            'item': VIRTUAL_ITEM_RELIC,
            'info': {
                'sid': iRelic,
                'level': iLevel } }
        cl_reward.RewardItem(oTarget.m_Game, oTarget, [
            dReward], sKey)


def CommonSetForceMoveStatus(oTarget, oLifeCycle, iStatus):
    
    def ClearFunc(oTarget, oLifeCycle):
        oAgent = oTarget.m_Agent
        iCacheStatus = oTarget.Query('CacheMoveStatus')
        if not oAgent or not iCacheStatus:
            return None
        oTarget.Set('ForceMoveStatus', 0)
        oTarget.Set('CacheMoveStatus', 0)
        if iCacheStatus == STATUS_PATROL:
            oAgent.SetActionSMPatrol(oAgent)
        elif iCacheStatus == STATUS_RUN:
            oAgent.SetActionSMRun(oAgent)
        elif iCacheStatus == STATUS_SPRINT:
            oAgent.SetActionSMSprint(oAgent)

    oAgent = oTarget.m_Agent
    if oAgent:
        if iStatus == STATUS_PATROL:
            oAgent.SetActionSMPatrol(oAgent)
        elif iStatus == STATUS_RUN:
            oAgent.SetActionSMRun(oAgent)
        elif iStatus == STATUS_SPRINT:
            oAgent.SetActionSMSprint(oAgent)
        else:
            return None
        oTarget.Set('ForceMoveStatus', 1)
        oLifeCycle.AddDisableFunc(ClearFunc)


def CommonSetForceFaceStatus(oTarget, oLifeCycle, iStatus, iKeep):
    
    def ClearFunc(oTarget, oLifeCycle):
        oAgent = oTarget.m_Agent
        if not oAgent:
            return None
        oAgent.SetData('ForceFaceStatus', 0)
        oAgent.ResumeFaceStatus()

    oAgent = oTarget.m_Agent
    if not (oTarget.m_FaceCtrl) or not oAgent:
        return None
    iForceStatus = None
    if iStatus == FACE_STATUS_PATH:
        iForceStatus = oAgent.FacePath(oAgent)
    elif iStatus == FACE_STATUS_TARGET:
        iForceStatus = oAgent.FaceLockEnemy(iKeep, oAgent)
    else:
        return None
    if iForceStatus == BT_SUCCESS:
        oAgent.SetData('ForceFaceStatus', 1)
        oLifeCycle.AddDisableFunc(ClearFunc)


def CommonPause(oTarget, oLifeCycle, iPauseTime, iDelayTime = 0):
    oTarget.m_Game.m_WarKeep.CallOutCommonGamePause(iPauseTime, iDelayTime)


def HaltAllSkill(oTarget, oLifeCycle, dIgnoreSkill):
    
    def DelayHaltAllSkill():
        if not oGame:
            return None
        skillMgr = oGame.m_SkillMgr
        for oSkill in list(skillMgr.m_Using.values()):
            if not oSkill.m_Base:
                continue
            if oSkill.m_Base['pfid'] in IgnoreSkillList:
                continue
            oSkill.Halt()
        

    IgnoreSkillList = list(dIgnoreSkill)
    oGame = oTarget.m_Game
    sKey = oLifeCycle.Key()
    oGame.m_Timer.Call_Out(DelayHaltAllSkill, 1, sKey)


def StopDyingState(oTarget, oLifeCycle, iStopTime, iDelayTime):
    oWarMgr = oTarget.m_Game.m_WarMgr
    oWarMgr.OnPlayingCG(iStopTime, iDelayTime)


def AddAchieveStat(oListener, oLifeCycle, iAchieveID, iAdd):
    oAchievement = oListener.m_Achievement
    iAdd = cl_formula.GetResultByData(oListener, iAdd, {
        'LifeCycle': oLifeCycle })
    if oAchievement:
        oAchievement.AddStat(iAchieveID, iAdd)


def AddSeasonTaskValue(oListener, oEventCB, iSeasonTask, iAdd):
    oListener.m_SeasonTaskMgr.AddTaskValue(iSeasonTask, iAdd)


def CommonChangeThrowPerformUse(oWarrior, oLifeCycle, iNewUse, iPointPf = 0):
    
    def ClearChangeThrowPerformUse(oWarrior, oLifeCycle):
        oPerformCon = oWarrior.m_Perform
        for iPerform in lstPerformSID:
            oPerform = oPerformCon.GetPerform(iPerform)
            if not oPerform:
                continue
            oPerform.ClearBulletUseByKey(sKey)
        

    oPerformCon = oWarrior.m_Perform
    lstPerform = oPerformCon.GetAllPerform()
    lstPerformSID = []
    sKey = oLifeCycle.Key()
    for oPerform in lstPerform:
        if (oPerform.m_PFType == PF_TYPE_THROW or iPointPf) and oPerform.m_SID != iPointPf:
            continue
        iBulletSID = oPerform.CalAttr('BulletSID')
        if not iBulletSID:
            continue
        oPerform.SetBulletUseByKey(iNewUse, sKey)
        lstPerformSID.append(oPerform.m_SID)
    
    oLifeCycle.AddDisableFunc(ClearChangeThrowPerformUse)


def CommonClearChangeThrowPerformUse(oWarrior, oLifeCycle):
    oPerformCon = oWarrior.m_Perform
    lstPerform = oPerformCon.GetAllPerform()
    sKey = oLifeCycle.Key()
    for oPerform in lstPerform:
        if oPerform.m_PFType == PF_TYPE_THROW:
            iBulletSID = oPerform.CalAttr('BulletSID')
            if not iBulletSID:
                continue
            oPerform.ClearBulletUseByKey(sKey)
    


def CommonChangeThrowPerformExtraUse(oWarrior, oLifeCycle, iExtra, iPointPf = 0):
    
    def ClearChangeThrowPerformExtraUse(oWarrior, oLifeCycle):
        oPerformCon = oWarrior.m_Perform
        for iPerform in lstPerformSID:
            oPerform = oPerformCon.GetPerform(iPerform)
            if not oPerform:
                continue
            oPerform.ClearBulletExtraUseByKey(sKey)
        

    oPerformCon = oWarrior.m_Perform
    lstPerform = oPerformCon.GetAllPerform()
    lstPerformSID = []
    sKey = oLifeCycle.Key()
    for oPerform in lstPerform:
        if (oPerform.m_PFType == PF_TYPE_THROW or iPointPf) and oPerform.m_SID != iPointPf:
            continue
        iBulletSID = oPerform.CalAttr('BulletSID')
        if not iBulletSID:
            continue
        oPerform.SetBulletExtraUseByKey(iExtra, sKey)
        lstPerformSID.append(oPerform.m_SID)
    
    oLifeCycle.AddDisableFunc(ClearChangeThrowPerformExtraUse)


def CommonClearChangeThrowPerformExtraUse(oWarrior, oLifeCycle):
    oPerformCon = oWarrior.m_Perform
    lstPerform = oPerformCon.GetAllPerform()
    sKey = oLifeCycle.Key()
    for oPerform in lstPerform:
        if oPerform.m_PFType == PF_TYPE_THROW:
            iBulletSID = oPerform.CalAttr('BulletSID')
            if not iBulletSID:
                continue
            oPerform.ClearBulletExtraUseByKey(sKey)
    


def SwitchTargetNavAble(oWarrior, oLifeCycle, iEnable):
    if not oWarrior.m_MoveCtrl:
        return None
    if iEnable:
        oWarrior.UnForbid(cl_forbid.NAVSEEK_RULE, 'CommonNavMove')
        oWarrior.m_MoveCtrl.E_Enable()
    else:
        oWarrior.Forbid(cl_forbid.NAVSEEK_RULE, 'CommonNavMove')
        oWarrior.m_MoveCtrl.E_Disable()


def SwitchTargetPathMode(oWarrior, oLifeCycle, iPathMode):
    
    def ClearFunc(oWarrior, oLifeCycle):
        if oWarrior.m_MoveCtrl:
            oWarrior.m_MoveCtrl.ClearPathMode(sKey)

    if not oWarrior.m_MoveCtrl:
        return None
    sKey = oLifeCycle.Key()
    oWarrior.m_MoveCtrl.SetPathMode(sKey, iPathMode)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonModifyPhyModel(oWarrior, oLifeCycle, iFlag, iRadius):
    
    def ClearFunc(oWarrior, oLifeCycle):
        oModel = oWarrior.Query(sKey)
        if oModel:
            oModel.E_Unstall()
        oWarrior.Delete(sKey)

    sKey = f'''{oLifeCycle.Key()}_PhyModel'''
    if iFlag == 0:
        oWarrior.Delete(sKey)
    else:
        dParam = oWarrior.m_ModelData.GetServerData()
        if 'Radius' in dParam:
            dParam['Radius'] *= 0.9
        if 'Height' in dParam:
            dParam['Height'] *= 0.9
        dParam['layer'] = cl_pxlayer.PXLATER_PETROCHEMICAL_OUTER
        oModel = cl_engphyobj.CreatePhyModel(oWarrior, PAMOD_TYPE_DYNA, dParam['layer'], dParam)
        oWarrior.Set(sKey, oModel)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonAddSelfPhyModel(oTarget, oLifeCycle, iModelType, iPhyType, iLayer, dArgs):
    if iModelType == MODEL_TYPE_BOX:
        dParam = {
            'Shape': MODEL_TYPE_BOX,
            'HalfExt': (dArgs['HalfExtX'], dArgs['HalfExtY'], dArgs['HalfExtZ']),
            'Center': (dArgs['CenterX'], dArgs['CenterY'], dArgs['CenterZ']) }
    else:
        SendAlert('err', f'''{oLifeCycle.Key()} 增加了不存在的物理模型,请检查''')
        return None
    cl_engphyobj.CreatePhyModel(oTarget, iPhyType, iLayer, dParam)


def CommonSetExtraModelDistance(oTarget, oLifeCycle, fDistance):
    oTarget.SetExtraModelDistance(fDistance)


def CommonSetHeightOffset(oTarget, oLifeCycle, iValue):
    oTarget.SetHeightOffset(iValue)


def CommonAddCustomData(oWarrior, oLifeCycle, sData, dData):
    if not dData:
        return None
    oWarMgr = oWarrior.m_Game.m_WarMgr
    dCustomData = oWarMgr.Query(sData, { })
    dCustomData.update(dData)
    oWarMgr.Set(sData, dCustomData)


def CommonSetCustomData(oTarget, oLifeCycle, sKey, iVal):
    iVal = cl_formula.GetResultByData(oTarget, iVal, {
        'LifeCycle': oLifeCycle })
    oTarget.Set(sKey, iVal)


def CommonSetMaxCustomData(oTarget, oLifeCycle, sKey, iVal):
    
    def ClearFunc(oWarrior, _oLifeCycle):
        dAllVal = oWarrior.Query(sMaxKey, { })
        dAllVal.pop(sSourceKey, 0)
        if dAllVal:
            oWarrior.Set(sKey, max(dAllVal.values()))
        else:
            oWarrior.Delete(sKey)

    iVal = cl_formula.GetResultByData(oTarget, iVal, {
        'LifeCycle': oLifeCycle })
    sMaxKey = 'Max%s' % sKey
    sSourceKey = oLifeCycle.m_Key
    dAllVal = oTarget.SetDefault(sMaxKey, { })
    dAllVal[sSourceKey] = iVal
    oTarget.Set(sKey, max(dAllVal.values()))
    oLifeCycle.AddUniqueDisableFunc(sSourceKey, ClearFunc, iCover = 0)


def CommonChangeEnergy(oTarget, oLifeCycle, iVal, iReason = 0):
    if not oLifeCycle.GetObject():
        return None
    iVal = cl_formula.GetResultByData(oTarget, iVal, {
        'LifeCycle': oLifeCycle })
    if oTarget.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
        return None
    oTarget.EnergyModify(iVal, iReason)


def CommonGetSummonAttr(oTarget, oLifeCycle, iFightType, sAttr):
    dSummon = oTarget.m_SummonDict
    if not dSummon:
        return 0
    for iSummon in dSummon:
        oSummon = oTarget.m_Game.GetObject(iSummon, PY_FLAG_DEAD)
        if not oSummon:
            continue
        if oSummon.m_FightType & iFightType == iFightType:
            return cl_newformula.GetWarriorAttr(sAttr, oSummon)
    
    return 0


def CommonGetTalentLevel(oTarget, oLifeCycle, iTalent):
    oTalent = oTarget.m_TalentCon.GetPerform(iTalent)
    if oTalent:
        return oTalent.m_Level
    return 0


def CommonSwitchPerform(oTarget, oLifeCycle, iPerform):
    oPerform = oTarget.GetPerform(iPerform)
    if oPerform:
        oTarget.m_Perform.GS2CPerformAdd(oPerform)
        return None
    oTarget.AddPerform(iPerform, 1)


def CommonSyncPointSkillUse(oTarget, oLifeCycle, iPerform):
    oPerformCon = oTarget.m_Perform
    lstPerform = oPerformCon.GetAllPerform()
    for oPerform in lstPerform:
        if oPerform.m_SID == iPerform:
            iBulletSID = oPerform.CalAttr('BulletSID')
            if not iBulletSID:
                continue
            oPerform.GS2CPerformPropChange('BulletUse', oPerform.m_CurBulletUse)
    


def GetDualPerformAndMergeCurPFBullet(oTarget, oLifeCycle, iPerform):
    oItemCon = oTarget.m_WieldCon
    lstItem = oItemCon.GetHoldWeapon()
    if len(lstItem) != 2:
        SendAlert('err', '%s 当前并非双持阶段' % oLifeCycle.Key())
        return ([], 0)
    iCurValue = 0
    lstPerform = []
    for tItem in lstItem:
        (oItem, _) = tItem
        oPerform = GetItemPerform(oItem, iPerform)
        if not oPerform:
            continue
        iCurValue += oPerform.m_CurPFBullet
        lstPerform.append(oPerform)
    
    return (lstPerform, iCurValue)


def CommonMergeDualPerformCurPFBullet(oTarget, oLifeCycle, iPerform):
    (lstPerform, iCurValue) = GetDualPerformAndMergeCurPFBullet(oTarget, oLifeCycle, iPerform)
    for oPerform in lstPerform:
        oPerform.m_CurPFBullet = iCurValue
        oPerform.RefreshCurPFBullet()
    


def CommonDivideDualPerformCurPFBullet(oTarget, oLifeCycle, iPerform):
    (lstPerform, iCurValue) = GetDualPerformAndMergeCurPFBullet(oTarget, oLifeCycle, iPerform)
    for oPerform in lstPerform:
        oPerform.m_CurPFBullet = iCurValue // 4
        oPerform.RefreshCurPFBullet()
    


def CommonShareDualPerformCurPFBullet(oTarget, oLifeCycle, iPerform):
    (lstPerform, iCurValue) = GetDualPerformAndMergeCurPFBullet(oTarget, oLifeCycle, iPerform)
    iShareCount = math.ceil(iCurValue / 2)
    for oPerform in lstPerform:
        oPerform.m_CurPFBullet = iShareCount
        oPerform.RefreshCurPFBullet()
    


def CommonShareMainPerformPFBullet(oTarget, oLifeCycle, iPerform):
    oItemCon = oTarget.m_WieldCon
    lstItem = oItemCon.GetHoldWeapon()
    if len(lstItem) != 2:
        SendAlert('err', '%s 当前并非双持阶段' % oLifeCycle.Key())
        return None
    oMainPerform = None
    oDeputyPerform = None
    iSumMaxPFBullet = 0
    fPFBulletRatio = 0
    for tItem in lstItem:
        (oItem, iHoldPos) = tItem
        oPerform = GetItemPerform(oItem, iPerform)
        if not oPerform:
            continue
        iMaxPFBullet = oPerform.MaxPFBullet()
        iSumMaxPFBullet += iMaxPFBullet
        if iHoldPos == MAIN_HOLD:
            oMainPerform = oPerform
            fPFBulletRatio = oPerform.m_CurPFBullet / iMaxPFBullet
            continue
        if iHoldPos == DEPUTY_HOLD:
            oDeputyPerform = oPerform
    
    if not oMainPerform or not oDeputyPerform:
        SendAlert('err', '%s 双持武器技能获取异常' % oLifeCycle.Key())
        return None
    if oMainPerform.GetArgValue('ShareMainPFBullet') or oDeputyPerform.GetArgValue('ShareMainPFBullet'):
        return None
    oMainPerform.SetArgValue('ShareMainPFBullet', True)
    oDeputyPerform.SetArgValue('ShareMainPFBullet', True)
    oDeputyPerform.AddPFBullet = WFunctor(oMainPerform.AddPFBullet)
    oDeputyPerform.CostPFBullet = WFunctor(oMainPerform.CostPFBullet)
    oDeputyPerform.CurPFBullet = WFunctor(oMainPerform.CurPFBullet)
    oRefreshCurPFBulletFunc = Functor(RefreshShareCurPFBullet, WeakProxy(oMainPerform), WeakProxy(oDeputyPerform))
    oDeputyPerform.RefreshCurPFBullet = oRefreshCurPFBulletFunc
    oMainPerform.RefreshCurPFBullet = oRefreshCurPFBulletFunc
    oShareMaxPFBullet = Functor(ShareMaxPFBullet, iSumMaxPFBullet)
    oMainPerform.MaxPFBullet = oShareMaxPFBullet
    oDeputyPerform.MaxPFBullet = oShareMaxPFBullet
    oMainPerform.RefreshAttr = Functor(RefreshShareMaxPFBullet, WeakProxy(oMainPerform), WeakProxy(oDeputyPerform), WFunctor(oMainPerform.RefreshAttr), iSumMaxPFBullet)
    oDeputyPerform.RefreshAttr = Functor(RefreshShareMaxPFBullet, WeakProxy(oDeputyPerform), WeakProxy(oMainPerform), WFunctor(oDeputyPerform.RefreshAttr), iSumMaxPFBullet)
    iCurPFBullet = int(iSumMaxPFBullet * fPFBulletRatio)
    oMainPerform.m_CurPFBullet = iCurPFBullet
    oMainPerform.GS2CPerformPropChange('MaxPFBullet', iSumMaxPFBullet)
    oDeputyPerform.GS2CPerformPropChange('MaxPFBullet', iSumMaxPFBullet)
    oMainPerform.GS2CPerformPropChange('CurPFBullet', iCurPFBullet)
    oDeputyPerform.GS2CPerformPropChange('CurPFBullet', iCurPFBullet)


def ShareMaxPFBullet(iSumMaxPFBullet):
    return iSumMaxPFBullet


def RefreshShareCurPFBullet(oMainPerform, oDeputyPerform):
    
    try:
        iCurPFBullet = oMainPerform.CurPFBullet()
        oMainPerform.GS2CPerformPropChange('CurPFBullet', iCurPFBullet)
        oDeputyPerform.GS2CPerformPropChange('CurPFBullet', iCurPFBullet)
    except:
        SendAlert('err', '共享主手武器专属子弹数清理异常')



def RefreshShareMaxPFBullet(oOwnPerform, oOtherPerform, oOriginalRefreshFunc, iSumMaxPFBullet, sAttr, iValue):
    
    try:
        if sAttr == 'MaxPFBullet':
            oOwnPerform.GS2CPerformPropChange('MaxPFBullet', iSumMaxPFBullet)
            oOtherPerform.GS2CPerformPropChange('MaxPFBullet', iSumMaxPFBullet)
        else:
            oOriginalRefreshFunc(sAttr, iValue)
    except:
        SendAlert('err', '共享主手武器专属子弹数清理异常')



def CommonDisableShareMainPerformPFBullet(oTarget, oLifeCycle, iPerform):
    oItemCon = oTarget.m_WieldCon
    lstItem = oItemCon.GetHoldWeapon()
    if len(lstItem) != 2:
        SendAlert('err', '%s 当前并非双持阶段' % oLifeCycle.Key())
        return None
    oMainPerform = None
    oDeputyPerform = None
    iCurValue = 0
    for tItem in lstItem:
        (oItem, iHoldPos) = tItem
        oPerform = GetItemPerform(oItem, iPerform)
        if not oPerform:
            continue
        if iHoldPos == MAIN_HOLD:
            oMainPerform = oPerform
            iCurValue = oPerform.m_CurPFBullet
            continue
        if iHoldPos == DEPUTY_HOLD:
            oDeputyPerform = oPerform
    
    if not oMainPerform or not oDeputyPerform:
        SendAlert('err', '%s 双持武器技能获取异常' % oLifeCycle.Key())
        return None
    if not oMainPerform.GetArgValue('ShareMainPFBullet') or not oDeputyPerform.GetArgValue('ShareMainPFBullet'):
        return None
    oMainPerform.DelArgValue('ShareMainPFBullet')
    oDeputyPerform.DelArgValue('ShareMainPFBullet')
    del oDeputyPerform.AddPFBullet
    del oDeputyPerform.CostPFBullet
    del oDeputyPerform.MaxPFBullet
    del oDeputyPerform.CurPFBullet
    del oDeputyPerform.RefreshCurPFBullet
    del oDeputyPerform.RefreshAttr
    del oMainPerform.RefreshCurPFBullet
    del oMainPerform.MaxPFBullet
    del oMainPerform.RefreshAttr
    iValue = math.ceil(iCurValue / 2)
    iMaxPFBullet = oMainPerform.MaxPFBullet()
    oMainPerform.m_CurPFBullet = iValue if iValue < iMaxPFBullet else iMaxPFBullet
    iMaxPFBullet = oDeputyPerform.MaxPFBullet()
    oDeputyPerform.m_CurPFBullet = iValue if iValue < iMaxPFBullet else iMaxPFBullet
    oMainPerform.GS2CPerformPropChange('MaxPFBullet')
    oDeputyPerform.GS2CPerformPropChange('MaxPFBullet')
    oMainPerform.GS2CPerformPropChange('CurPFBullet')
    oDeputyPerform.GS2CPerformPropChange('CurPFBullet')


def GetItemPerform(oItem, iPerform):
    oPerformCom = oItem.GetComponent('Perform')
    if not oPerformCom:
        return None
    return oPerformCom.GetPerform(iPerform)


def CommonGetWeaponBulletType(oTarget, oLifeCycle):
    oCurWeapon = oTarget.m_WieldCon.GetCurWeapon()
    if not oCurWeapon:
        return 0
    if oCurWeapon.IsInitWeapon():
        return 0
    oBulletCom = oCurWeapon.GetComponent('Bullet')
    if not oBulletCom:
        return 0
    return oBulletCom.BulletType()


def CommonSetDyingSecond(oTarget, oLifeCycle, iSecond):
    iSecond = cl_formula.GetResultByData(oTarget, iSecond, {
        'LifeCycle': oLifeCycle })
    oTarget.InitDyingSecond(iSecond)


def CommonAddDyingSecond(oTarget, oLifeCycle, iAdd, iMul):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.RecoverTempDyingSecond(sKey)

    iAdd = cl_formula.GetResultByData(oTarget, iAdd, {
        'LifeCycle': oLifeCycle })
    iMul = cl_formula.GetResultByData(oTarget, iMul, {
        'LifeCycle': oLifeCycle })
    sKey = oLifeCycle.Key()
    oTarget.AddTempDyingSecond(sKey, iAdd, iMul, sKey)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonSetDeadPunishmentTimes(oTarget, oLifeCycle, iTimes):
    iTimes = cl_formula.GetResultByData(oTarget, iTimes, {
        'LifeCycle': oLifeCycle })
    iOldTimes = oTarget.GetDeadPunishmentTimes()
    oTarget.AddDeadPunishmentTimes(iTimes - iOldTimes, sReason = oLifeCycle.Key())


def CommonAddDeadPunishmentTimes(oTarget, oLifeCycle, iTimes):
    if not iTimes:
        return None
    iTimes = cl_formula.GetResultByData(oTarget, iTimes, {
        'LifeCycle': oLifeCycle })
    oTarget.AddDeadPunishmentTimes(iTimes, sReason = oLifeCycle.Key())


def CommonAddRecycleDropReward(oTarget, oLifeCycle, iType, iPrice, iCloseRemove = 1):
    
    def ClearFunc(oTarget, oLifeCycle):
        dPrice = oTarget.Query('RecycleDropPrice', { })
        if iType in dPrice:
            dPrice.pop(iType)
            if iType == NWARRIOR_DROP_RELIC:
                if NWARRIOR_DROP_RELIC_MYSTERY in dPrice:
                    dPrice.pop(NWARRIOR_DROP_RELIC_MYSTERY)
                oTarget.m_RelicCon.RefreshAllRelicItemInfo()

    dPrice = oTarget.SetDefault('RecycleDropPrice', { })
    sAddReason = oLifeCycle.Key()
    if iType in dPrice:
        sOldReason = dPrice[iType][1]
        if sOldReason != sAddReason:
            SendAlert('err', '通用设置掉落回收奖励%s覆盖%s，请检查' % (sAddReason, sOldReason))
    dPrice[iType] = (iPrice, sAddReason)
    if iType == NWARRIOR_DROP_RELIC:
        dPrice[NWARRIOR_DROP_RELIC_MYSTERY] = (iPrice, sAddReason)
        oTarget.m_RelicCon.RefreshAllRelicItemInfo()
    oRecycleDropElement = oTarget.m_Game.m_WarMgr.GetComponent('RecycleDropElement')
    if oRecycleDropElement:
        oRecycleDropElement.RefreshRecycleDropInfo(oTarget)
    if iCloseRemove:
        oLifeCycle.AddDisableFunc(ClearFunc)


def CommonSetSavedData(oTarget, oLifeCycle, sFlag, iVal):
    if iVal:
        iVal = cl_formula.GetResultByData(oTarget, iVal, {
            'LifeCycle': oLifeCycle }, { })
    oTarget.SetSavedData('save.' + sFlag, iVal)


def CommonAddSavedData(oTarget, oLifeCycle, sFlag, iVal):
    if iVal:
        iVal = cl_formula.GetResultByData(oTarget, iVal, {
            'LifeCycle': oLifeCycle }, { })
    oTarget.AddSavedData('save.' + sFlag, iVal)


def CommonAddChangeEvent(oTarget, oLifeCycle, dInfo):
    
    def ClearFunc(oTarget, oLifeCycle):
        oWarMgr.Set('BenedictionChallenge', { })

    oGame = oTarget.m_Game
    oWarMgr = oGame.GetWarMgr()
    dResult = { }
    for iLayer, dChallenge in dInfo.items():
        dLayerChallenge = { }
        for iChallenge in dChallenge:
            dLayerChallenge[iChallenge % 10000] = 1
        
        dResult[iLayer] = dLayerChallenge
    
    oWarMgr.Set('BenedictionChallenge', dResult)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonSetDieRemoveDelay(oTarget, oLifeCycle, iTime):
    oTarget.m_RemoveDelay = Time2Frame(iTime)


def CommonSetTalentChooseTimes(oTarget, oLifeCycle, iTimes, iCost = 0):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.Set('TalentChooseRefresh', 0)
        if iCost:
            oTarget.Set('GoldNpcRefreshCost', 0)

    if oTarget.Query('TalentChooseRefresh'):
        SendAlert('err', '已设置金爵刷新信息，请检查%s' % oLifeCycle.Key())
        return None
    oTarget.Set('TalentChooseRefresh', iTimes)
    if iCost:
        oTarget.Set('GoldNpcRefreshCost', iCost)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonAddTalentChooseTempTimes(oTarget, oLifeCycle, iAdd):
    iOldTimes = oTarget.QuerySavedData('TalentChooseRefreshTemp', 0)
    oTarget.SetSavedData('TalentChooseRefreshTemp', iOldTimes + iAdd)


def CommonSetTalentChooseAllTimes(oTarget, oLifeCycle, iTimes):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.Set('TalentChooseAll', 0)

    oTarget.Set('TalentChooseAll', iTimes)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonSetLimitRelicNum(oTarget, oLifeCycle, iNum):
    
    def ClearFunc(oTarget, oLifeCycle):
        oRelicCon = oTarget.m_RelicCon
        oRelicCon.SetMaxRelicNum(0, None, 1)

    oRelicCon = oTarget.m_RelicCon
    oRelicCon.SetMaxRelicNum(iNum, Functor(LimitRelicNumBeforeAddRelic), 1)
    lstAll = oRelicCon.GetAllRelicSIDByType(RELIC_TYPE_NORMAL)
    dCanRemove = { }
    for iPerform in lstAll:
        oPerform = oRelicCon.GetPerform(iPerform)
        if oPerform.ValidRemove():
            dCanRemove[oPerform.m_SID] = 1
    
    iAllNum = len(lstAll)
    if iAllNum > iNum:
        iDropNum = iAllNum - iNum
        dAll = dict.fromkeys(lstAll, 1)
        oGame = oRelicCon.m_Game
        for _ in range(iDropNum):
            if dCanRemove:
                iRemoveRelic = ChooseKey(oGame, dCanRemove)
                oRelicCon.RemoveRelicByDrop(iRemoveRelic, REMOVE_RELIC_ACTIVE, iAlert = 1, iShare = 0)
                dCanRemove.pop(iRemoveRelic)
                dAll.pop(iRemoveRelic)
                continue
            iRemoveRelic = ChooseKey(oGame, dAll)
            oRelicCon.RemoveRelic(iRemoveRelic, 'benedictionRelicTopLimit', 1)
            dAll.pop(iRemoveRelic)
        
    oLifeCycle.AddDisableFunc(ClearFunc)


def LimitRelicNumBeforeAddRelic(oRelicCon, iNewRelic, iLevel):
    clsPerform = cl_perform.GetPerformModule(iNewRelic)
    if not clsPerform or clsPerform.m_PFType != PF_TYPE_RELIC:
        return False
    if clsPerform.m_RelicType == RELIC_TYPE_CURSE:
        return False
    iMax = oRelicCon.MaxRelicNum()
    lstAll = oRelicCon.GetAllRelicSIDByType(RELIC_TYPE_NORMAL)
    if len(lstAll) < iMax:
        return False
    dStaticInfo = {
        'DropLevel': iLevel,
        'DropSource': oRelicCon.m_PlayerID }
    oTarget = oRelicCon.m_Game.GetObject(oRelicCon.m_Owner)
    if not oTarget:
        return False
    cl_drop.DropPerform(oTarget, iNewRelic, dStaticInfo, True, 1)
    return True


def CommonClearSmithNoCashCost(oTarget, oLifeCycle):
    oTarget.Set('SmithNoCashCost', 0)


def CommonSetSmithNoCashCost(oTarget, oLifeCycle):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.Set('SmithNoCashCost', 0)

    oTarget.Set('SmithNoCashCost', 1)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonSetWeightDropGoods(oTarget, oLifeCycle, iMiniGame, dWeight, iSourse, iOnlyRewardAttack, iRepeatReward, iLevel = 1, iAddMiniGameSource = 0):
    oGame = oTarget.m_Game
    iTimes = ChooseKey(oGame, dWeight)
    dReward = { }
    dReward[iMiniGame] = (10000, iTimes)
    dExtInfo = {
        'CheckGoldenCup': 1,
        'OnlyRewardAttack': iOnlyRewardAttack,
        'Abandoner': oTarget.m_ID,
        'RepeatReward': iRepeatReward,
        'Source': iSourse,
        'Level': iLevel }
    if iAddMiniGameSource:
        dExtInfo['MiniGameSource'] = oLifeCycle.Key()
    cl_reward.RewardItemByMiniGame(oTarget, oTarget.m_ID, dReward, 'CommonSetWeightDropGoods%d' % oTarget.m_ID, iSourse, dExtInfo)


def CommonDropDemon(oTarget, oLifeCycle, iMiniGame, dWeight, iSource, iOnlyRewardAttack, iRepeatReward, fOffsetDis, fInvalidRange, iLevel = 1):
    oGame = oTarget.m_Game
    iTimes = ChooseKey(oGame, dWeight)
    dReward = {
        iMiniGame: (10000, iTimes) }
    dExtInfo = {
        'OnlyRewardAttack': iOnlyRewardAttack,
        'Abandoner': oTarget.m_ID,
        'RepeatReward': iRepeatReward,
        'Source': iSource,
        'DropLevel': iLevel,
        'CalOffset': 0,
        'CheckGoldenCup': 1,
        'CanReward': 0,
        'AutoReward': 0 }
    if fOffsetDis:
        vStartPos = oTarget.GetAttackPos()
        vFace = oTarget.GetFacing()
        vDir = (vFace[0], 0, vFace[2])
        iScene = oTarget.m_Scene
        vEndPos = cl_math.Vec3DisplaceDir(vStartPos, vDir, fOffsetDis)
        tRet = oGame.Scene_RaycastSingle(iScene, vStartPos, vEndPos, PXMASK_MOVEBLK)
        if tRet[0] != -1:
            vNeDir = (-vDir[0], 0, -vDir[2])
            fModelRadius = cl_modeldefine.GetModelDefine(5540, 'Physx')[0]
            vDropPos = cl_math.Vec3DisplaceDir(tRet[1], vNeDir, fModelRadius)
        else:
            vDropPos = vEndPos
        if fInvalidRange and cl_math.CalDistance(vStartPos, vDropPos) <= fInvalidRange:
            vDropPos = oTarget.m_Pos
            oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
            if oLevelCtrl:
                oScene = oGame.m_SceneMgr.GetScene(iScene)
                if oScene:
                    iLevel = oScene.m_Level
                    oMiniMap = oLevelCtrl.m_LevelMiniMap.GetMiniMap(iLevel)
                    oGoal = oMiniMap.GetCurLevelGoal(oTarget.m_PlayerID)
                    if oGoal:
                        if oGoal.m_Type == GOALPOS_TYPE_PASSBOXNPC:
                            vGoalStartPos = oGoal.m_Pos
                            vGoalEndPos = cl_math.Vec3DisplaceDir(vGoalStartPos, oGoal.m_Facing, 2)
                            vDropPos = vGoalEndPos
                        else:
                            vDropPos = oGoal.m_Pos
        oTarget.Set('FixDropPos', vDropPos)
    dMGInfo = cl_reward.RewardItemByMiniGame(oTarget, oTarget.m_ID, dReward, 'CommonDropDemon-%s%d' % (oLifeCycle.Key(), oTarget.m_ID), iSource, dExtInfo)
    cl_reward.CreateDemon(oGame, oTarget.m_ID, dMGInfo)
    if fOffsetDis:
        oTarget.Delete('FixDropPos')


def CommonRandomTalentMiniGameRewardTalent(oTarget, oLifeCycle, iMiniGame, iSourse):
    dReward = {
        iMiniGame: (10000, 1) }
    dExtInfo = {
        'OnlyRewardAttack': 1,
        'Abandoner': oTarget.m_ID,
        'Source': iSourse }
    cl_reward.RewardItemByMiniGame(oTarget, oTarget.m_ID, dReward, 'CommonMiniGameRewardTalent-%s%d' % (oLifeCycle.Key(), oTarget.m_ID), iSourse, dExtInfo)


def CommonDirectRewardTalent(oTarget, oLifeCycle, iTalent):
    iTalent = cl_formula.GetResultByData(oTarget, iTalent, {
        'LifeCycle': oLifeCycle })
    oTalent = oTarget.m_TalentCon.GetPerform(iTalent)
    if oTalent and oTalent.m_Level == oTalent.m_MaxLevel:
        return None
    dReward = {
        'item': VIRTUAL_ITEM_TALENT,
        'info': {
            'sid': iTalent,
            'amount': 1 } }
    cl_reward.RewardItem(oTarget.m_Game, oTarget, [
        dReward], '%sRewardTalent' % oLifeCycle.Key(), None)


def CommonSetPerformArgs(oTarget, oLifeCycle, iPerform, sArg, iVal, iDisableClear = 1):
    
    def ClearFunc(oTarget, oLifeCycle):
        oPerform = oTarget.GetPerform(iPerform)
        if not oPerform:
            return None
        oPerform.AddArgValue(sArg, -iModify)

    oPerform = oTarget.GetPerform(iPerform)
    if not oPerform:
        return None
    if iDisableClear is None:
        iDisableClear = 1
    dData = {
        'LifeCycle': oLifeCycle }
    iVal = cl_formula.GetResultByData(oTarget, iVal, dData)
    iOldValue = oPerform.GetArgValue(sArg)
    iModify = iVal - iOldValue
    oPerform.SetArgValue(sArg, iVal)
    if iDisableClear:
        oLifeCycle.AddDisableFunc(ClearFunc)


def CommonAddPerformArgsValue(oTarget, oLifeCycle, iPerform, sArg, iAdd, iDisableClear = 0):
    
    def ClearFunc(oTarget, oLifeCycle):
        oPerform = oTarget.GetPerform(iPerform)
        if not oPerform:
            return None
        oPerform.AddArgValue(sArg, -iAdd)

    oPerform = oTarget.GetPerform(iPerform)
    if not oPerform:
        return None
    dData = {
        'LifeCycle': oLifeCycle }
    iAdd = cl_formula.GetResultByData(oTarget, iAdd, dData)
    oPerform.AddArgValue(sArg, iAdd)
    if iDisableClear:
        oLifeCycle.AddDisableFunc(ClearFunc)


def CommonAddClientActivePrformUseCount(oTarget, oLifeCycle, iPerform, iAdd):
    oPerform = oTarget.GetPerform(iPerform)
    if not oPerform:
        return None
    dData = {
        'LifeCycle': oLifeCycle }
    iAdd = cl_formula.GetResultByData(oTarget, iAdd, dData)
    oPerform.AddCanUseCount(iAdd)


def CommonAddClientActivePrformUseCountMax(oTarget, oLifeCycle, iPerform, iAdd):
    
    def ClearFunc(oTarget, oLifeCycle):
        oClearPerform = oTarget.GetPerform(iPerform)
        if not oClearPerform:
            return None
        oClearPerform.AddCanUseCountMax(-iAdd)

    oPerform = oTarget.GetPerform(iPerform)
    if not oPerform:
        return None
    dData = {
        'LifeCycle': oLifeCycle }
    iAdd = cl_formula.GetResultByData(oTarget, iAdd, dData)
    oPerform.AddCanUseCountMax(iAdd)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonShieldRecover(oTarget, oLifeCycle):
    oTarget.StartShieldRecover('Halt')


def CommonSetRecastInscription(oTarget, oLifeCycle, iTimes, iNoCost):
    
    def ClearFunc(oListener, oLifeCycle):
        oTarget.Set('RecastInscription', 0)
        oTarget.Set('RecastInscriptionNoCost', 0)

    oTarget.Set('RecastInscription', iTimes)
    oTarget.Set('RecastInscriptionNoCost', iNoCost)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonSetIgnoreSkillsToNoMaxHateTarget(oTarget, oLifeCycle, sIgnoreSkill):
    lstIgnoreSkill = sIgnoreSkill.rstrip('|').split('|')
    lstIgnoreSkill = [ int(sSkill) for sSkill in lstIgnoreSkill ]
    oAgent = oTarget.m_Agent
    if not oAgent:
        return None
    oAgent.SetData('IgnoreSkills', lstIgnoreSkill)


def CommonSetServantRescueConfig(oTarget, oLifeCycle, iColdTime, iOnlyOwner):
    if not (oTarget.m_FightType & WARRIOR_HERO) or not (oTarget.m_Servant):
        return None
    oServant = oTarget.m_Game.GetObject(oTarget.m_Servant)
    if not oServant:
        return None
    oServant.Set('RescueConfig', {
        'RescueCDFrame': Time2Frame(iColdTime),
        'OnlyOwner': iOnlyOwner })
    oTarget.Set('SingleRescue', 1)


def CommonChangeSubAttackMsgType(oTarget, oLifeCycle, iType):
    oTarget.m_SubAttackMsg = iType


def CommonNextFrameUpdateAI(oTarget, oLifeCycle):
    oAgent = oTarget.m_Agent
    if oAgent:
        oAgent.m_GameSpace.CallDelayUpdate(oAgent, 1)


def CommonRandomAddStateAndSetStateCount(oTarget, oLifeCycle, sState, iCount):
    lstRes = []
    lstState = sState.rstrip('|').split('|')
    lstState = [ int(iState) for iState in lstState ]
    for iState in lstState:
        if not oTarget.m_State.GetItemBySID(iState):
            lstRes.append(iState)
    
    if not lstRes:
        return None
    iIndex = oTarget.m_Game.Random(len(lstRes))
    iState = lstRes[iIndex]
    oReason = cl_object.reason.CStrReason(oLifeCycle.Key())
    oState = cl_state.AddState(oTarget, iState, STATE_TIME_FOREVER, 0, {
        'AID': oTarget.m_ID,
        'RS': oReason })
    if oState:
        oState.Enable(oTarget)
    oState.AddCount(oTarget, iCount)


def CommonPerformAddColdTime(oTarget, oLifeCycle, iPerform):
    pfobj = oTarget.GetPerform(iPerform)
    if not pfobj:
        return None
    oTarget.m_Perform.AddColdTime(iPerform, pfobj.GetCDTime(oTarget))


def CommonPerformSetColdTime(oTarget, oLifeCycle, iPerform, iCDTime):
    iCDTime = cl_formula.GetResultByData(oTarget, iCDTime, {
        'LifeCycle': oLifeCycle })
    iColdFrame = Time2Frame(iCDTime)
    if iColdFrame <= 0:
        return None
    oPerform = oTarget.GetPerform(iPerform)
    if not oPerform:
        return None
    oPerform.SetCDTime(oTarget, iColdFrame)


def CommonPerformPauseColdTime(oTarget, oLifeCycle, iPerform):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.m_Perform.ReStartColdDown(iPerform)

    pfobj = oTarget.GetPerform(iPerform)
    if not pfobj:
        return None
    oTarget.m_Perform.PauseColdDown(iPerform)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonSceneEventAddState(oTarget, oLifeCycle, iEvent, iState, iStateTime, iLeaveRemoveState, iFightType, iSelfOnly = 1):
    
    def SceneEnterFunc(oListener, dMsgInfo):
        iTriggerObj = dMsgInfo['VID']
        if iSelfOnly and iTriggerObj != oListener.m_ID:
            return None
        obj = oListener.m_Game.GetObject(iTriggerObj)
        if not obj or obj.m_FightType & iFightType != iFightType:
            return None
        oState = cl_state.AddState(obj, iState, iStateTimeType, Time2Frame(iStateTime), dStateArgs)
        if oState:
            lstStateID = dAllState.setdefault(iTriggerObj, [])
            lstStateID.append(oState.m_ID)
            oState.Enable(obj)

    
    def SceneLeaveFunc(oListener, dMsgInfo):
        if not iLeaveRemoveState:
            return None
        iTriggerObj = dMsgInfo['VID']
        if iSelfOnly and iTriggerObj != oListener.m_ID:
            return None
        obj = oListener.m_Game.GetObject(iTriggerObj)
        if not obj or obj.m_FightType & iFightType != iFightType:
            return None
        lstStateID = dAllState.get(iTriggerObj, [])
        if lstStateID:
            for iStateID in lstStateID:
                obj.m_State.RemoveItem(iStateID)
            
            dAllState.pop(iTriggerObj, None)
        else:
            obj.m_State.RemoveAllItemBySID(iState)

    
    def ClearFunc(oListener, oLifeCycle):
        oScene.UnBindSceneEvent(iEvent, sKey)
        for iObj, lstStateID in dAllState.items():
            obj = oListener.m_Game.GetObject(iObj)
            if not obj:
                continue
            for iStateID in lstStateID:
                obj.m_State.RemoveItem(iStateID)
            
        

    oGame = oTarget.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oTarget.m_Scene)
    if not oScene:
        return None
    dAllState = { }
    sKey = oLifeCycle.Key()
    oReason = cl_object.reason.CStrReason(sKey)
    iStateTimeType = STATE_TIME_LIMIT if iStateTime else STATE_TIME_FOREVER
    dStateArgs = {
        'AID': oTarget.m_ID,
        'RS': oReason }
    oScene.BindSceneEvent(oTarget, iEvent, SceneEnterFunc, SceneLeaveFunc, sKey)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonDelayGameOver(oTarget, oLifeCycle, iType, iTime):
    
    def DelayGameOver(oGame):
        iOverType = oGame.m_WarMgr.Query('OverType', 0)
        if iOverType == SETTLE_OVER_FAIL:
            oGame.m_WarMgr.OnFinishLevel(SETTLE_LOSEWAR)
            oGame.m_WarMgr.OnLoseWar()

    oGame = oTarget.m_Game
    if iType == SETTLE_LOSEWAR:
        oGame.m_WarMgr.UniqueSet('OverType', SETTLE_OVER_FAIL)
    iFrame = Time2Frame(iTime)
    if not iFrame:
        DelayGameOver(oGame)
    else:
        oGame.m_Timer.Call_Out(Functor(DelayGameOver, oGame, iType), iFrame, 'DelayGameOver')


def CommonGetAssistKill(oTarget, oLifeCycle, iFightType):
    oWarMgr = oTarget.m_Game.GetWarMgr()
    oReport = oWarMgr.GetComponent('Warreport')
    iAssistCnt = 0
    if not oReport:
        return iAssistCnt
    if iFightType & WARRIOR_ELITE == WARRIOR_ELITE:
        iAssistCnt += oReport.m_WarReportData.GetPlayerWarStatisticsByAttr(oTarget.m_PlayerID, 'AssistKillElite')
    if iFightType & WARRIOR_BOSS == WARRIOR_BOSS:
        iAssistCnt += oReport.m_WarReportData.GetPlayerWarStatisticsByAttr(oTarget.m_PlayerID, 'AssistKillBoss')
    return iAssistCnt


def CommonSwitchMonsterAtt(oTarget, oLifeCycle, iPerform):
    
    def SwitchPerform(oTarget, oLifeCycle):
        oTarget.m_AttPerform = iCurAttPerform

    if oTarget.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
        return None
    iCurAttPerform = oTarget.m_AttPerform
    oPerform = oTarget.AddPerform(iPerform, 1)
    if not oPerform:
        return None
    oTarget.m_AttPerform = iPerform
    oLifeCycle.AddDisableFunc(SwitchPerform)


def CommonSuperMonster(oTarget, oLifeCycle, dMonsterAf, dAttrPlus):
    if oTarget.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
        return None
    oGame = oTarget.m_Game
    iAf = ChooseKey(oGame, dMonsterAf)
    iPlus = ChooseKey(oGame, dAttrPlus)
    if not iAf or not iPlus:
        SendAlert('err', '怪物%d强化有误，af:%s plus:%s' % (oTarget.m_SID, iAf, iPlus))
        return None
    oWarMgr = oTarget.m_Game.GetWarMgr()
    oMonsterSuper = oWarMgr.GetComponent('MonsterSuper')
    oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
    iSuperLevel = 0
    if oMonsterSuper:
        oLevelNode = oLevelCtrl.m_CurNode
        iSuperLevel = oMonsterSuper.GetMonsterSuperLevel(oLevelNode.m_LevelType)
    else:
        iSuperLevel = oLevelCtrl.m_LayerNum
    oTarget.MonsterSuper(iSuperLevel, iPlus, iAf)


def CommonKillAllMonster(oTarget, oLifeCycle):
    if not oTarget.m_Scene:
        return None
    oReason = cl_object.reason.CStrReason('通用行为', None, {
        'DamType': DAM_TYPE_SCENE | DAM_TYPE_TRUE | DAM_USE_HP })
    oGame = oTarget.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oTarget.m_Scene)
    for iMonster in oScene.GetObjectsByType('Monster'):
        oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
        if oMonster and oMonster.m_FightType & WARRIOR_BOSS != WARRIOR_BOSS and oMonster.m_FightType not in BOSS_DONOT_COUNT and oMonster.m_FightType != WARRIOR_NORPART and oMonster.m_FightType != WARRIOR_ELIPART:
            oMonster.HPModifyDam(oTarget.m_ID, [
                [
                    oMonster.HP(),
                    oReason]])
            if oMonster.m_Part and not oMonster.IsDead():
                oMonster.HPModifyDam(oTarget.m_ID, [
                    [
                        oMonster.HP(),
                        oReason]])
    


def CommonCreateBuildOnSelfPos(oTarget, oLifeCycle, iBuild):
    oGame = oTarget.m_Game
    clsSummonData = oGame.m_WarData.GetBuildData(iBuild)
    tModelData = cl_modeldefine.GetModelDefine(clsSummonData.m_Shape, 'Physx')
    tFace = oTarget.GetFacing()
    fAngle = cl_math.CalAngle2D(tFace, (0, 0, 1))
    dAddData = {
        'Shape': MODEL_TYPE_CAPSULE,
        'Angle': (0, fAngle, 0),
        'Scale': (1, 1, 1),
        'Center': (0, 0, 0),
        'Size': (tModelData[1], tModelData[0], 0),
        'Origin': oTarget.GetPos() }
    iScene = oTarget.m_Scene
    oGame.m_ResMgr.CreateBuild(iScene, iBuild, dAddData)


def CommonRemoveBeExecuted(oTarget, oLifeCycle):
    oTarget.Set('BeExecuted', 0)


def CommonTriggerCG(oGame, iBehavior, iCanSkip):
    oWarMgr = oGame.m_WarMgr
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMGR_CG_START, oWarMgr, {
        'Behavior': iBehavior })
    CgLog.Debug('%d cgstart %d %d' % (oGame.m_ID, iBehavior, iCanSkip))
    lstHero = oWarMgr.GetRoomHero()
    for iHero in lstHero:
        oHero = oGame.GetObject(iHero)
        if not oHero:
            continue
        dDoneType = oHero.SetDefault('CheckTips', { })
        lstDoneBehavior = dDoneType.setdefault(CHECKTYPE_CLIENTBEHAVIOR, [])
        if iBehavior not in dDoneType[CHECKTYPE_CLIENTBEHAVIOR]:
            lstDoneBehavior.append(iBehavior)
            if oWarMgr.IsSingleGame():
                iCanSkip = 0
        cl_snetwar.GS2CTriggerCG(oGame, oHero.m_PlayerID, iHero, iBehavior, iCanSkip)
    


def CommonSendStateStartMessage(oTarget, oLifeCycle, iSendToSelf, iSendToAttack):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    iStateSID = oState.m_SID
    iAttack = oState.m_StateInfo['AID']
    if iSendToSelf:
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CUSTOMSTATE_START, oTarget, {
            'StateSID': iStateSID,
            'AID': iAttack,
            'RemainTime': Frame2Time(oState.GetRemainTime()),
            'RS': oState.m_Reason })
    if iSendToAttack:
        oGame = oTarget.m_Game
        oAttack = oGame.GetObject(iAttack)
        if oAttack:
            iFrame = oGame.GetFrameNum() - oState.m_CreateFrame
            iTime = Frame2Time(iFrame)
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CUSTOMSTATE_START, oAttack, {
                'StateSID': iStateSID,
                'Time': iTime,
                'RemainTime': Frame2Time(oState.GetRemainTime()),
                'VID': oTarget.m_ID,
                'Count': oState.GetCount(),
                'RS': oState.m_Reason })


def CommonSendStateMessage(oTarget, oLifeCycle, bSendMsgToSelf = False, dExtraInfo = None):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    iStateSID = oState.m_SID
    if dExtraInfo:
        dInfo = cl_formula.CalArgsFormula(oTarget, dExtraInfo, {
            'LifeCycle': oLifeCycle })
    else:
        dInfo = { }
    if bSendMsgToSelf:
        dInfo.update({
            'StateSID': iStateSID,
            'VID': oTarget.m_ID })
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, oTarget, dInfo)
    else:
        oGame = oTarget.m_Game
        oAttack = oGame.GetObject(oState.m_StateInfo['AID'])
        if not oAttack:
            return None
        iFrame = oGame.GetFrameNum() - oState.m_CreateFrame
        iTime = Frame2Time(iFrame)
        dInfo.update({
            'StateSID': iStateSID,
            'Time': iTime,
            'RemainTime': Frame2Time(oState.GetRemainTime()),
            'VID': oTarget.m_ID,
            'Count': oState.GetCount() })
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, oAttack, dInfo)


def CommonSendReduceSpeedMessage(oTarget, oLifeCycle):
    if oTarget.GetReducingSpeedNum() > 1:
        return None
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_REDUCESPEEDED, oTarget, { })


def CommonSendReduceSpeedEndMessage(oTarget, oLifeCycle):
    if oTarget.IsReducingSpeed():
        return None
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_REDUCESPEEDEDEND, oTarget, { })


def CommonAddWeaponUpgradeCnt(oTarget, oLifeCycle, iCnt):
    
    def ClearFunc(oTarget, oLifeCycle):
        iOld = oTarget.Query('AdditionalWeaponUpgrade', 0)
        oTarget.Set('AdditionalWeaponUpgrade', iOld - iCnt)

    iCnt = cl_formula.GetResultByData(oTarget, iCnt, {
        'LifeCycle': oLifeCycle })
    iOld = oTarget.Query('AdditionalWeaponUpgrade', 0)
    oTarget.Set('AdditionalWeaponUpgrade', iOld + iCnt)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonEnableSealedInscription(oTarget, oLifeCycle, iLevel):
    lstWeapon = oTarget.m_WieldCon.GetAllItemByMask(itemdef.EQUIP_MASK_WEAPON)
    if not lstWeapon:
        return None
    oTarget.Set('SealedInscriptionEnable', 1)
    for oWeapon in lstWeapon:
        oInscriptionCom = oWeapon.GetComponent('Inscription')
        if not oInscriptionCom:
            continue
        oInscriptionCom.EnableSealedInscription(iLevel)
    


def CommonDisableSealedInscription(oTarget, oLifeCycle, iLevel):
    lstWeapon = oTarget.m_WieldCon.GetAllItemByMask(itemdef.EQUIP_MASK_WEAPON)
    if not lstWeapon:
        return None
    oTarget.Set('SealedInscriptionEnable', 0)
    for oWeapon in lstWeapon:
        oInscriptionCom = oWeapon.GetComponent('Inscription')
        if not oInscriptionCom:
            continue
        oInscriptionCom.DisableSealedInscription(iLevel)
    


def CommmonDisableRewardPassive(oTarget, oLifeCycle, iPerform):
    
    def ClearFunc(oTarget, oLifeCycle):
        oClearPerform = oTarget.GetPerform(iPerform)
        if oClearPerform:
            oClearPerform.Enable(oTarget, iNotify = 1)

    oPerform = oTarget.GetPerform(iPerform)
    if oPerform and oPerform.m_PFType == PF_TYPE_REWARD:
        oPerform.Disable(oTarget, iNotify = 1)
        oLifeCycle.AddDisableFunc(ClearFunc)


def CommonReduceTalentLevel(oTarget, oLifeCycle, iTalent):
    oGame = oTarget.m_Game
    oTalentCon = oTarget.m_TalentCon
    if iTalent == 0:
        lstTalent = oTalentCon.GetAllTalentSID(iExcludeRareTalent = 1)
        if not lstTalent:
            return None
        iTalent = lstTalent[oGame.Random(len(lstTalent))]
    oTalentCon.DeGradeTalent(iTalent, 1, oLifeCycle.Key())


def CommonRandomReduceTalentLevel(oTarget, oLifeCycle, iPriorityType):
    oGame = oTarget.m_Game
    oTalentCon = oTarget.m_TalentCon
    lstTalent = oTalentCon.GetTalentListByPriority(iPriorityType, iExcludeOneLevel = 1)
    if not lstTalent:
        lstTalent = oTalentCon.GetTalentListByPriority(iPriorityType)
        if not lstTalent:
            return None
    iTalent = lstTalent[oGame.Random(len(lstTalent))]
    oTalentCon.DeGradeTalent(iTalent, 1, oLifeCycle.Key())


def CommonAddTalentLevel(oTarget, oLifeCycle, iTalent, iPriorityType, iLevel = 1):
    oGame = oTarget.m_Game
    oTalentCon = oTarget.m_TalentCon
    iTalent = cl_formula.GetResultByData(oTarget, iTalent, {
        'LifeCycle': oLifeCycle })
    if iTalent == 0:
        lstTalent = oTalentCon.GetTalentListByPriority(iPriorityType, iExcludeMaxLevel = 1, iExcludeBan = 1)
        if not lstTalent:
            AllTalentSet = set(oTalentCon.GetAllValidTalent(iUseLib = 0, iExcludeCurTalent = 0))
            CurTalentSet = set(oTalentCon.GetAllTalentSID())
            AddTalentSet = AllTalentSet - CurTalentSet
            if not AddTalentSet:
                return None
            lstRandomTalent = list(AddTalentSet)
            iTalent = lstRandomTalent[oGame.Random(len(lstRandomTalent))]
        else:
            iTalent = lstTalent[oGame.Random(len(lstTalent))]
    if iTalent in oTalentCon.m_Perform:
        oTalentCon.UpgradeTalent(iTalent, iLevel, oLifeCycle.Key())
    else:
        oTalentCon.AddTalent(iTalent, iLevel, oLifeCycle.Key())


def CommonRemoveAllTalent(oTarget, oLifeCycle):
    oTalentCon = oTarget.m_TalentCon
    oTalentCon.RemoveAllTalent(oLifeCycle.Key())


def CommonStateStatistics(oTarget, oLifeCycle, iStateSID, iValue, sAttr):
    oStateCon = oTarget.m_State
    oState = oStateCon.GetItemBySID(iStateSID)
    if not oState:
        return None
    iValue = cl_formula.GetResultByData(oTarget, iValue, {
        'LifeCycle': oLifeCycle })
    oState.m_Data[sAttr] = iValue


def CommonGetStateMaxArgsDict(oTarget, oLifeCycle, iStateSID, sArgs, iFromSelf, iFromSameItem):
    iAttack = oTarget.m_ID if iFromSelf else 0
    if iFromSameItem:
        dEventInfo = oLifeCycle.AttrCache()
        iItem = dEventInfo['ItemID']
    else:
        iItem = 0
    oState = oTarget.m_State.GetStateBySource(iStateSID, iAttack, iItem)
    if not oState:
        return 0
    dArgs = oState.GetArgValue(sArgs, { })
    if not dArgs:
        return 0
    return max(dArgs.values())


def CommonGetStateArgsDictSum(oTarget, oLifeCycle, iStateSID, sArgs, iFromSelf, iFromSameItem):
    iAttack = oTarget.m_ID if iFromSelf else 0
    if iFromSameItem:
        dEventInfo = oLifeCycle.AttrCache()
        iItem = dEventInfo['ItemID']
    else:
        iItem = 0
    oState = oTarget.m_State.GetStateBySource(iStateSID, iAttack, iItem)
    if not oState:
        return 0
    dArgs = oState.GetArgValue(sArgs, { })
    if not dArgs:
        return 0
    return sum(dArgs.values())


def CommonUpdateStateArgsDict(oTarget, oLifeCycle, iStateSID, sArgs, iValue, iFromSelf, iFromSameItem):
    iAttack = oTarget.m_ID if iFromSelf else 0
    if iFromSameItem:
        dEventInfo = oLifeCycle.AttrCache()
        iItem = dEventInfo['ItemID']
    else:
        iItem = 0
    oState = oTarget.m_State.GetStateBySource(iStateSID, iAttack, iItem)
    if not oState:
        return None
    iValue = cl_formula.GetResultByData(oTarget, iValue, {
        'LifeCycle': oLifeCycle })
    dArgs = oState.SetArgValueDefault(sArgs, { })
    dArgs[oLifeCycle.Key()] = iValue


def CommonRemoveStateArgsDict(oTarget, oLifeCycle, iStateSID, sArgs, iFromSelf, iFromSameItem):
    iAttack = oTarget.m_ID if iFromSelf else 0
    if iFromSameItem:
        dEventInfo = oLifeCycle.AttrCache()
        iItem = dEventInfo['ItemID']
    else:
        iItem = 0
    oState = oTarget.m_State.GetStateBySource(iStateSID, iAttack, iItem)
    if not oState:
        return None
    dArgs = oState.SetArgValueDefault(sArgs, { })
    dArgs.pop(oLifeCycle.Key(), None)


def CommonSetShopNpcRefresh(oTarget, oLifeCycle, tFristValue, iMul):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.Set('ShopNpcRefreshInfo', { })

    dShopNpcRefreshInfo = { }
    pfobj = oLifeCycle.GetObject()
    iLevel = pfobj.m_Level
    sKey = oLifeCycle.GetStableKey()
    sKey = '%s-%d' % (sKey, iLevel)
    dInfo = {
        'FristValue': tFristValue,
        'Mul': iMul,
        'Key': sKey }
    dShopNpcRefreshInfo = dInfo
    oTarget.Set('ShopNpcRefreshInfo', dShopNpcRefreshInfo)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonSetEventNpcInteract(oTarget, oLifeCycle, iExtra = 0):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.Set('NpcInteractChooseNoLimit', 0)
        if iExtra:
            oTarget.Set('NpcInteractExtraChoose', 0)

    oTarget.Set('NpcInteractChooseNoLimit', 1)
    if iExtra:
        oTarget.Set('NpcInteractExtraChoose', 1)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonSetAllRelicUnRemove(oTarget, oLifeCycle):
    
    def ClearFunc(oTarget, oLifeCycle):
        sKey = 'ChangeAll%s' % oLifeCycle.Key()
        dRelic = oTarget.Query(sKey, [])
        oTarget.Set(sKey, [])
        oRelicCon = oTarget.m_RelicCon
        oRelicCon.DelRelicTempRemove(dRelic)

    oRelicCon = oTarget.m_RelicCon
    dRelic = oRelicCon.SetAllRelicTempUnRemove()
    sKey = 'ChangeAll%s' % oLifeCycle.Key()
    oTarget.Set(sKey, dRelic)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonAddBossLevelCnt(oTarget, oLifeCycle, iType, iAdd):
    
    def ClearFunc(oWarrior, oLifeCycle):
        sKey = oLifeCycle.Key()
        oWarMgr = oWarrior.m_Game.m_WarMgr
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        dBossChoose = oLevelCtrl.m_LayerChoose.m_LayerBossChoose
        if sKey in dBossChoose:
            dBossChoose.pop(sKey)

    oWarMgr = oTarget.m_Game.m_WarMgr
    oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
    sKey = oLifeCycle.Key()
    oLevelCtrl.m_LayerChoose.SetBossLevelCnt(sKey, iType, iAdd)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonModifyWeaponDamageType(oTarget, oLifeCycle, iHoldType, iType, sExtInfo = ''):
    
    def ClearFunc(oTarget, oLifeCycle):
        oItem.m_ElementTypeObj.RemoveSetModify(sKey)

    oItem = oTarget.m_WieldCon.GetCurWeapon(iHoldType)
    if not oItem:
        return None
    sKey = oLifeCycle.Key()
    if sExtInfo:
        sKey = f'''{sKey}-{sExtInfo}'''
    iType = cl_formula.GetResultByData(oTarget, iType, {
        'LifeCycle': oLifeCycle })
    oItem.m_ElementTypeObj.SetModify(sKey, iType)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonChangePassiveCycleExecCBFuncTime(oTarget, oLifeCycle, iPerform, iMul, iAddTime):
    
    def ClearFunc(oTarget, oLifeCycle):
        oClearPerform = oTarget.GetPerform(iPerform)
        if not oClearPerform:
            return None
        oClearPerform.ClearCycleTimeChange(sKey, oTarget)

    oPerform = oTarget.GetPerform(iPerform)
    if not oPerform or oPerform.m_PFType & PF_TYPE_PASSIVE != PF_TYPE_PASSIVE:
        return None
    iMul = cl_formula.GetResultByData(oTarget, iMul, {
        'LifeCycle': oLifeCycle })
    iAddTime = cl_formula.GetResultByData(oTarget, iAddTime, {
        'LifeCycle': oLifeCycle })
    sKey = oLifeCycle.Key()
    iAdd = Time2Frame(iAddTime)
    if oPerform.AddCycleTimeChange(oTarget, iMul, iAdd, sKey):
        oLifeCycle.AddDisableFunc(ClearFunc)


def CommonSendStateCountChangeMessage(oTarget, oLifeCycle):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    oGame = oTarget.m_Game
    oAttack = oGame.GetObject(oState.m_StateInfo['AID'])
    if not oAttack:
        return None
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CUSTOMSTATECOUNTCHANGE, oAttack, {
        'StateSID': oState.m_SID,
        'Count': oState.GetCount() })


def CommonChangeWeaponExtGrade(oTarget, oLifeCycle, iGroup, iGrade, iFlag, iAll = 0):
    
    def ClearExtGrade(oTarget, oLifeCycle):
        for iWeapon in lstClear:
            oWeapon = oTarget.m_WieldCon.GetItemByID(iWeapon)
            if not oWeapon:
                continue
            oWeapon.ClearExtGrade(sKey)
        

    if iAll:
        lstAdd = oTarget.m_WieldCon.GetAllItem()
    else:
        lstAdd = oTarget.m_WieldCon.GetWeapons(iFlag)
    iGrade = cl_formula.GetResultByData(oTarget, iGrade, {
        'LifeCycle': oLifeCycle })
    sKey = oLifeCycle.Key()
    lstClear = []
    for oWeapon in lstAdd:
        if not oWeapon.CheckHasExtGrade(sKey):
            lstClear.append(oWeapon.m_ID)
        oWeapon.AddExtGrade(sKey, iGroup, iGrade)
    
    if lstClear:
        oLifeCycle.AddDisableFunc(ClearExtGrade)


def CommonChangeStateAttr(oTarget, oLifeCycle, iStateSID, iCount, iType, iChangeOwn = 0):
    
    def ClearFunc(oTarget, oLifeCycle):
        oClearState = oLifeCycle.GetObject() if iChangeOwn else oTarget.m_State.GetItem(iChangeStateID)
        if not oClearState:
            return None
        if iType == STATE_COUNT_MAX:
            oClearState.SetMaxCount(oTarget, oClearState.m_MaxCount - iFormulaCount)
        elif iType == STATE_COUNT_MIN:
            oClearState.SetMinCount(oTarget, oClearState.m_MinCount - iFormulaCount)

    if iChangeOwn:
        oState = oLifeCycle.GetObject()
    else:
        oState = oTarget.m_State.GetItemBySID(iStateSID)
    if not oState:
        return None
    iChangeStateID = oState.m_ID
    iFormulaCount = cl_formula.GetResultByData(oTarget, iCount, {
        'LifeCycle': oLifeCycle })
    if iType == STATE_COUNT_MAX:
        oState.SetMaxCount(oTarget, iFormulaCount + oState.m_MaxCount)
    elif iType == STATE_COUNT_MIN:
        oState.SetMinCount(oTarget, iFormulaCount + oState.m_MinCount)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonCreateServant(oTarget, oLifeCycle, iServantSID, fRadius1, fRadius2, fAngle1, fAngle2):
    if not (oTarget.m_FightType & WARRIOR_HERO) or oTarget.m_Servant:
        return None
    oGame = oTarget.m_Game
    dAddData = {
        'Owner': oTarget.m_ID }
    oServant = oGame.m_ResMgr.CreateServant(oTarget.m_Scene, iServantSID, dAddData)
    if oServant:
        oTarget.m_Servant = oServant.m_ID
        oServant.m_Agent.PauseAgent('LeaveScene')


def CommonRelifeServant(oTarget, oLifeCycle):
    if not oTarget.m_FightType & WARRIOR_HERO:
        return None
    oServant = oTarget.m_Game.GetObject(oTarget.m_Servant)
    if not oServant or not oServant.IsDead():
        return None
    dReason = {
        'Type': TYPE_RELIFE_PASSIVE }
    oServant.Relife(dReason)


def CommonModifyGrooveNum(oTarget, oLifeCycle, iModify):
    
    def ClearModify(oTarget, oLifeCycle):
        oTarget.m_GamblerCon.ModifyGrooveNum(-iModify)

    if not oTarget.m_GamblerCon:
        return None
    oTarget.m_GamblerCon.ModifyGrooveNum(iModify)
    oLifeCycle.AddDisableFunc(ClearModify)


def CommonAppendQuality(oTarget, oLifeCycle, iAssignQuality, iChooseType, iFundamental, iNum, iReplaceRule = 0, iNoRefresh = 0):
    if oTarget.m_SID != GAMBLER_HERO:
        return None
    if iNoRefresh:
        oTarget.m_GamblerCon.TryAppendQualityNoRefresh(iAssignQuality, iChooseType, iFundamental, iNum, iReplaceRule)
    else:
        oTarget.m_GamblerCon.TryAppendQuality(iAssignQuality, iChooseType, iFundamental, iNum, iReplaceRule)


def CommonClearAllGroove(oTarget, oLifeCycle, iFlag = 0):
    if oTarget.m_SID != GAMBLER_HERO:
        return None
    oTarget.m_GamblerCon.ClearAllQuality(0, iFlag, oLifeCycle.Key())


def CommonRandomClearGroove(oTarget, oLifeCycle, iAssignQuality, bUseMinQuality):
    if bUseMinQuality:
        iAssignQuality = oTarget.m_GamblerCon.GetMinQuality()
    oTarget.m_GamblerCon.RandomClearGroove(iAssignQuality)


def CommonClearLastGroove(oTarget, oLifeCycle):
    oTarget.m_GamblerCon.ClearLastGroove()


def CommonSetReplaceRule(oTarget, oLifeCycle, iRule):
    
    def ResetReplaceRule(oTarget, oLifeCycle):
        oTarget.m_GamblerCon.ResetReplaceRule()

    if oTarget.m_GamblerCon.m_ReplceRule != GAMBLER_REPLACE_DEFAULT:
        sKey = oLifeCycle.Key()
        SendAlert('err', f'''{sKey} setrule err, exist {oTarget.m_GamblerCon.m_ReplceRule}''')
        return None
    oTarget.m_GamblerCon.SetReplaceRule(iRule)
    oLifeCycle.AddDisableFunc(ResetReplaceRule)


def CommonModifyTalentWeight(oTarget, oLifeCycle, iTargetLevel, iModify):
    
    def ClearEvent(oTarget, oLifeCycle):
        cl_msgcenter.DoneEvent(oTarget, cl_msgcenter.MSG_WAR_ADDTALENT, oLifeCycle.Key())
        ClearTalentWeight(oTarget, iTargetLevel, sStableKey)

    sStableKey = oLifeCycle.GetStableKey()
    cl_msgcenter.AddFunction(oTarget, cl_msgcenter.MSG_WAR_ADDTALENT, Functor(CBModifyTalentWeight, iTargetLevel, iModify, sStableKey), oLifeCycle.Key(), iOnce = 0)
    oLifeCycle.AddDisableFunc(ClearEvent)


def CBModifyTalentWeight(iTargetLevel, iModify, sStableKey, oTarget, dInfo):
    iResult = 0
    if dInfo['Level'] == iTargetLevel - 1:
        iResult = iModify
    iTalent = dInfo['iPerform']
    lstReward = [
        {
            'item': VIRTUAL_ITEM_TALENTWEIGHT,
            'info': {
                'talent': iTalent,
                'modify': iResult } }]
    cl_reward.RewardItem(oTarget.m_Game, oTarget, lstReward, sStableKey, { })


def ClearTalentWeight(oTarget, iTargetLevel, sStableKey):
    lstReward = []
    for iTalent, iLevel in oTarget.m_TalentCon.GetAllTalentLevel().items():
        if iLevel == iTargetLevel - 1:
            lstReward.append({
                'item': VIRTUAL_ITEM_TALENTWEIGHT,
                'info': {
                    'talent': iTalent,
                    'modify': 0 } })
    
    if lstReward:
        cl_reward.RewardItem(oTarget.m_Game, oTarget, lstReward, sStableKey, { })


def CommonChangeRollRelicCnt(oTarget, oLifeCycle, iCnt):
    iCnt = cl_formula.GetResultByData(oTarget, iCnt, {
        'LifeCycle': oLifeCycle })
    iOld = oTarget.GetRollRelicCnt()
    oTarget.SetRollRelicCnt(iOld + iCnt)


def CommonShareWeaponInscription(oTarget, oLifeCycle):
    
    def ClearShareInscription(oTarget, oLifeCycle):
        pfobj = oLifeCycle.GetObject()
        oWeapon = pfobj.GetMyItem()
        oInscriptionCom = oWeapon.GetComponent('Inscription')
        oInscriptionCom.RemoveShareInscription()

    pfobj = oLifeCycle.GetObject()
    if pfobj.m_PFType != PF_TYPE_INSCRIPTION or pfobj.m_InscriptionType != INSCRIPTION_TYPE_GEMINI:
        return None
    oWeapon = pfobj.GetMyItem()
    if not oWeapon or not (oWeapon.Type() & itemdef.EQUIP_MASK_WEAPON):
        return None
    oInscriptionCom = oWeapon.GetComponent('Inscription')
    oOtherInscriptionCom = oInscriptionCom.GetAnotherWeaponInscriptionCom()
    if not oOtherInscriptionCom:
        return None
    lstInscription = oOtherInscriptionCom.m_Inscription
    lstHas = oInscriptionCom.m_Inscription
    for iSID in lstInscription:
        clsPerform = cl_perform.GetPerformModule(iSID)
        if clsPerform.m_InscriptionType == INSCRIPTION_TYPE_GEMINI:
            continue
        if not clsPerform.CheckValidItem(oWeapon, lstHas):
            continue
        oInscriptionCom.AddShareInscription(iSID)
    
    oLifeCycle.AddDisableFunc(ClearShareInscription)


def CommonEnableInscriptionPerform(oTarget, oLifeCycle):
    
    def ClearPerform(oTarget, oLifeCycle):
        pfobj = oLifeCycle.GetObject()
        oWeapon = pfobj.GetMyItem()
        if not oWeapon:
            return None
        oComPerform = oWeapon.GetComponent('Perform')
        oComPerform.m_Perform.RemovePerform(oTarget, iInscriptionPerform)

    pfobj = oLifeCycle.GetObject()
    oWeapon = pfobj.GetMyItem()
    if not oWeapon:
        return None
    dPerformAttr = oWeapon.m_ComponentAttr['Perform']
    iInscriptionPerform = dPerformAttr['InscriptionPerform'] if 'InscriptionPerform' in dPerformAttr else 0
    if not iInscriptionPerform:
        return None
    oPerformCom = oWeapon.GetComponent('Perform')
    oPerform = oPerformCom.AddPerform(iInscriptionPerform, 1)
    if oPerform:
        oPerform.m_ItemEnableType = ITEMPERFORM_ENABLE_BOTH
        oLifeCycle.AddDisableFunc(ClearPerform)


def CommonSendNotify(oTarget, oLifeCycle, bToSelf, iChat, dReplaceInfo):
    if not iChat:
        sKey = oLifeCycle.Key()
        SendAlert('err', '%s对白编号未指定，请对照通用对白表中对白编号填写' % sKey)
        return None
    oGame = oTarget.m_Game
    if bToSelf:
        if not oTarget.m_FightType & WARRIOR_HERO:
            sKey = oLifeCycle.Key()
            SendAlert('err', '%s目标类型为%s，非玩家无法进行提示' % (sKey, oTarget.m_Type))
            return None
        dPlayers = {
            oTarget.m_PlayerID: 1 }
    else:
        oScene = oGame.m_SceneMgr.GetScene(oTarget.m_Scene)
        if not oScene:
            return None
        dPlayers = oScene.GetPlayers()
    if dReplaceInfo:
        for key, value in dReplaceInfo.items():
            dReplaceInfo[key] = str(value)
        
    cl_notify.SendCommonNotify(oGame, dPlayers, iChat, dReplaceInfo)


def CommonSetServantBronPosInfo(oTarget, oLifeCycle, fMinRadius, fMaxRadius, iMinAngle, iMaxAngle):
    oTarget.Set('BronPosInfo', (fMinRadius, fMaxRadius, iMinAngle, iMaxAngle))


def CommonChangeQualityProb(oTarget, oLifeCycle, iQuality, iProb):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.m_GamblerCon.AddQualityProb(iQuality, -iProb)

    iProb = cl_formula.GetResultByData(oTarget, iProb, {
        'LifeCycle': oLifeCycle })
    oTarget.m_GamblerCon.AddQualityProb(iQuality, iProb)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonFullQuality(oTarget, oLifeCycle):
    if not oTarget.m_GamblerCon:
        return None
    oTarget.m_GamblerCon.FullQuality()


def CommonReplaceChildNode(oTarget, oLifeCycle, sPre, sAfter):
    
    def ClearFunc(oTarget, oLifeCycle):
        oNodeTask.m_TempBTPath = ''

    oAgent = oTarget.m_Agent
    if not oAgent:
        return None
    oFsm = oAgent.m_Fsm.m_Node
    oNodeTask = None
    for iNodeID, oBeTreeState in oFsm.m_Children.items():
        if oBeTreeState.m_Name == sPre:
            oNodeTask = oAgent.m_Fsm.GetChildTaskById(iNodeID)
            break
    
    if not oNodeTask:
        return None
    oNodeTask.m_TempBTPath = sAfter
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonReplaceOwnObjChildNode(oTarget, oLifeCycle, sPre, sAfter, iObjectType, iReplaceNow):
    
    def ClearFunc(oTarget, oLifeCycle):
        oWarrior = oTarget.m_Game.GetObject(oTarget.GetOwnObjectID(iObjectType))
        if not oWarrior:
            return None
        oAgent = oWarrior.m_Agent
        if not oAgent:
            return None
        oNodeTask = oAgent.m_Fsm.GetChildTaskById(iNodeID)
        if not oNodeTask:
            return None
        oNodeTask.m_TempBTPath = ''
        if iReplaceNow and oNodeTask == oAgent.m_Fsm.m_CurrentTask:
            HaltAllCasting(oTarget, sKey)
            oWarrior.Stop()
            oAgent.BTSetCurrent(sPre)

    oWarrior = oTarget.m_Game.GetObject(oTarget.GetOwnObjectID(iObjectType))
    if not oWarrior:
        return None
    oAgent = oWarrior.m_Agent
    if not oAgent:
        return None
    oFsm = oAgent.m_Fsm.m_Node
    oNodeTask = None
    for iNodeID, oBeTreeState in oFsm.m_Children.items():
        if oBeTreeState.m_Name == sPre:
            oNodeTask = oAgent.m_Fsm.GetChildTaskById(iNodeID)
            break
    
    if not oNodeTask:
        return None
    oNodeTask.m_TempBTPath = sAfter
    sKey = oLifeCycle.Key()
    if iReplaceNow and oNodeTask == oAgent.m_Fsm.m_CurrentTask:
        HaltAllCasting(oTarget, sKey)
        oWarrior.Stop()
        oAgent.BTSetCurrent(sAfter)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonReplaceOwnObjHateMethod(oTarget, oLifeCycle, iObjectType, iHateMethod):
    
    def ClearFunc(oTarget, oLifeCycle):
        lstHateMethod = oAgent.GetData('HateMethodList', [])
        if tKey in lstHateMethod:
            lstHateMethod.remove(tKey)
            if not lstHateMethod:
                return None
            (_, iNewHateMethod) = lstHateMethod[-1]
            oAgent.SetData('HateMethod', iNewHateMethod)

    oWarrior = oTarget.m_Game.GetObject(oTarget.GetOwnObjectID(iObjectType))
    if not oWarrior:
        return None
    oAgent = oWarrior.m_Agent
    if not oAgent:
        return None
    sKey = oLifeCycle.Key()
    tKey = (sKey, iHateMethod)
    lstHateMethod = oAgent.GetData('HateMethodList', [])
    if tKey in lstHateMethod:
        lstHateMethod.remove(tKey)
    lstHateMethod.append(tKey)
    oAgent.SetData('HateMethod', iHateMethod)
    oAgent.SetData('HateMethodList', lstHateMethod)
    oLifeCycle.AddUniqueDisableFunc('%s-%s' % (sKey, iHateMethod), ClearFunc, iCover = 0)


def CommonSetPyFlag(oTarget, oLifeCycle, iFlag, iValue):
    oGame = oTarget.m_Game
    oGame.SetPyFlag(oTarget.m_ID, iFlag, iValue)


def CommonChangeUpgradeRelicCnt(oTarget, oLifeCycle, iCnt):
    iCnt = cl_formula.GetResultByData(oTarget, iCnt, {
        'LifeCycle': oLifeCycle })
    iOld = oTarget.GetUpgradeRelicCnt()
    oTarget.SetUpgradeRelicCnt(iOld + iCnt)
    oTarget.m_GamblerCon.RefreshUpgradeRelic()


def CommonModifyChoosePFArgs(oTarget, oLifeCycle, dArgs):
    
    def ClearFunc(oTarget, oLifeCycle):
        oAgent = oTarget.m_Agent
        if not oAgent:
            return None
        oAgent.SetData('ChoosePF', { })

    oAgent = oTarget.m_Agent
    if not oAgent:
        return None
    dChoosePF = { }
    for sDistance, dPerform in dArgs.items():
        lstDistance = sDistance.split('-')
        lstDistance = [ int(sDis) for sDis in lstDistance ]
        dChoosePF[tuple(lstDistance)] = dPerform
    
    oAgent.SetData('ChoosePF', dChoosePF)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonModifyDamResistance(oTarget, oLifeCycle, iValue, iDamSrc, iElementType, iShow):
    
    def ClearFunc(oTarget, oLifeCycle):
        if not oTarget.m_Resistance:
            return None
        oTarget.m_Resistance.ClearValue(oTarget, sKey)

    sKey = oLifeCycle.m_Key
    if not oTarget.m_Resistance:
        oTarget.m_Resistance = cl_extraattr.CResistance('Resistance', 0, iSync = 0)
    oResistance = oTarget.m_Resistance
    iValue = cl_formula.GetResultByData(oTarget, iValue, {
        'LifeCycle': oLifeCycle })
    if sKey not in oResistance.m_Apply:
        oLifeCycle.AddUniqueDisableFunc('Resistance', ClearFunc, iCover = 0)
    oResistance.ModifyResistance(oTarget, iValue, iDamSrc, iElementType, iShow, sKey)


def CommonChangeMaxRelicRollNum(oTarget, oLifeCycle, iCnt):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.AddMaxRelicRollNum(-iCnt)

    iCnt = cl_formula.GetResultByData(oTarget, iCnt, {
        'LifeCycle': oLifeCycle })
    oTarget.AddMaxRelicRollNum(iCnt)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonChangeBurstCount(oTarget, oLifeCycle, iCnt):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.AddBurstCount(-iCnt)

    iCnt = cl_formula.GetResultByData(oTarget, iCnt, {
        'LifeCycle': oLifeCycle })
    oTarget.AddBurstCount(iCnt)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonChangeSourceWeaponSpecialAttr(oTarget, oLifeCycle, sAttr, iAdd):
    
    def ClearSpecialAttr(oTarget, oLifeCycle):
        oWeapon = oTarget.m_WieldCon.GetItemByID(iWeapon)
        if not oWeapon:
            return None
        oWeapon.SpecialAttrClear(sAttr, sKey)

    oWeapon = oLifeCycle.GetOwnerSourceWeapon()
    if not oWeapon:
        return None
    sKey = oLifeCycle.Key()
    if iAdd:
        iWeapon = oWeapon.m_ID
        iAdd = cl_formula.GetResultByData(oTarget, iAdd, {
            'LifeCycle': oLifeCycle }, { }, {
            'Weapon': oWeapon })
        oLifeCycle.AddDisableFunc(ClearSpecialAttr)
        oWeapon.ChangeSpecialAttr(sAttr, iAdd, sKey)


def CommonClearSourceWeaponSpecialAttr(oTarget, oLifeCycle, sAttr):
    oWeapon = oLifeCycle.GetOwnerSourceWeapon()
    if not oWeapon:
        return None
    sKey = oLifeCycle.Key()
    oWeapon.SpecialAttrClear(sAttr, sKey)


def CommonSetSourceWeaponForceAttr(oTarget, oLifeCycle, sAttr, iValue, iPriority):
    oWeapon = oLifeCycle.GetOwnerSourceWeapon()
    if not oWeapon:
        return None
    sKey = oLifeCycle.Key()
    iWeapon = oWeapon.m_ID
    iValue = cl_formula.GetResultByData(oTarget, iValue, {
        'LifeCycle': oLifeCycle }, { }, {
        'Weapon': oWeapon })
    oLifeCycle.m_ItemApply[(iWeapon, sAttr)] = 1
    oWeapon.ItemAttrForceSet(sAttr, iValue, sKey, iRemoveClear = 1, iPriority = iPriority)


def CommonAddSourceWeaponSpecialAttrBase(oTarget, oLifeCycle, sAttr, iAdd):
    oWeapon = oLifeCycle.GetOwnerSourceWeapon()
    if not oWeapon:
        return None
    if iAdd:
        iAdd = cl_formula.GetResultByData(oTarget, iAdd, {
            'LifeCycle': oLifeCycle }, { }, {
            'Weapon': oWeapon })
        oWeapon.AddSpecialAttrBase(sAttr, iAdd)


def CommonAddSourceWeaponSpecialAttrMax(oTarget, oLifeCycle, sAttr, iAdd):
    
    def ClearFunc(oTarget, oLifeCycle):
        oWeapon = oLifeCycle.GetOwnerSourceWeapon()
        if not oWeapon:
            return None
        oWeapon.ChangeSpecialAttrMax(sAttr, -iAdd)

    oWeapon = oLifeCycle.GetOwnerSourceWeapon()
    if not oWeapon:
        return None
    if iAdd:
        iAdd = cl_formula.GetResultByData(oTarget, iAdd, {
            'LifeCycle': oLifeCycle }, { }, {
            'Weapon': oWeapon })
        oWeapon.ChangeSpecialAttrMax(sAttr, iAdd)
        oLifeCycle.AddDisableFunc(ClearFunc)


def CommonAddState(oTarget, oLifeCycle, iMainState, iState, dArgs, iCheckHasFollow = 1):
    oMainState = oTarget.m_State.GetItemBySID(iMainState)
    if not oMainState:
        return None
    if iCheckHasFollow and iState in oMainState.m_FollowState.values():
        return None
    dData = {
        'LifeCycle': oLifeCycle }
    dRet = cl_formula.CalArgsFormula(oTarget, dArgs, dData)
    oReason = cl_object.reason.CStrReason(oLifeCycle.Key())
    dArgs = {
        'AID': oTarget.m_ID,
        'RS': oReason,
        'arg': dRet }
    cl_state.AddFollowState(oTarget, oMainState, iState, STATE_TIME_FOREVER, 0, dArgs)


def CommonAddWeaknessFlawProb(oTarget, oLifeCycle, iProb):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.m_FlawCon.DisableWeaknessFlawProb(sKey)

    if oTarget.m_SID != EXECUTOR_HERO:
        return None
    iProb = cl_formula.GetResultByData(oTarget, iProb, {
        'LifeCycle': oLifeCycle })
    sKey = oLifeCycle.Key()
    oTarget.m_FlawCon.AddWeaknessFlawProb(sKey, iProb)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonAddFlawAddition(oTarget, oLifeCycle, sAttr, iAdd, iMul, iCover = 1):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.m_FlawCon.RemoveFlawAddition(sAttr, sKey)

    if oTarget.m_SID != EXECUTOR_HERO:
        return None
    iAdd = cl_formula.GetResultByData(oTarget, iAdd, {
        'LifeCycle': oLifeCycle })
    iMul = cl_formula.GetResultByData(oTarget, iMul, {
        'LifeCycle': oLifeCycle })
    sKey = 'FlawAddition-%s%s' % (oLifeCycle.Key(), sAttr)
    oTarget.m_FlawCon.AddFlawAddition(sAttr, sKey, iAdd, iMul, iCover)
    oLifeCycle.AddUniqueDisableFunc(sKey, ClearFunc, iCover = 0)


def CommonSetUnbalanceCDStart(oTarget, oLifeCycle):
    if not oTarget.m_FightType & WARRIOR_MONSTER:
        return None
    oTarget.Set(FLAW_UNBALANCE_STARTFRAME, oTarget.m_Game.GetFrameNum())


def CommonForbidSpawnFlaw(oTarget, oLifeCycle):
    
    def ClearFunc(oTarget, oLifeCycle):
        MonsterResumeSpawnFlaw(oTarget, sKey)

    if not oTarget.m_FightType & WARRIOR_MONSTER:
        return None
    sKey = oLifeCycle.Key()
    MonsterForbidSpawnFlaw(oTarget, sKey)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonReduceCurFlawCD(oTarget, oLifeCycle, iReduce, iMul):
    if oTarget.m_SID != EXECUTOR_HERO:
        return None
    iReduce = cl_formula.GetResultByData(oTarget, iReduce, {
        'LifeCycle': oLifeCycle })
    iMul = cl_formula.GetResultByData(oTarget, iMul, {
        'LifeCycle': oLifeCycle })
    iReduce = Time2Frame(iReduce)
    oTarget.m_FlawCon.ReduceAllCurFlawCD(iReduce, iMul)


def CommonDegradeHoldWeapon(oTarget, oLifeCycle, iGrade):
    oWeapon = oTarget.m_WieldCon.GetCurWeapon(MAIN_HOLD)
    if not oWeapon or oWeapon.m_Type == itemdef.EQUIP_TYPE_FUNDAMENTALWEAPON:
        lstWeapon = oTarget.m_WieldCon.GetAllItemByType(itemdef.EQUIP_TYPE_MAINWEAPON)
        if not lstWeapon:
            return None
        oWeapon = lstWeapon[0]
    iGrade = cl_formula.GetResultByData(oTarget, iGrade, {
        'LifeCycle': oLifeCycle })
    oWeapon.Degrade(iGrade)


def CommonChangeElementDam(oTarget, oLifeCycle, iDamType, dRule):
    
    def ClearFunc(oTarget, oLifeCycle):
        for iHPType, iRadio in dRule.items():
            oTarget.RemoveElementFactor(iDamType, iHPType, sKey)
        

    sKey = oLifeCycle.Key()
    for iHPType, iRadio in dRule.items():
        oTarget.AddElementFactor(iDamType, iHPType, iRadio, sKey)
    
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonChangePositiveElementFactor(oTarget, oLifeCycle, iAdd):
    
    def ClearFunc(oTarget, oLifeCycle):
        dPositiveElementFactor = oTarget.m_PositiveElementFactor
        if sKey in dPositiveElementFactor:
            dPositiveElementFactor.pop(sKey, 0)
            oTarget.m_PositiveElementFactorValue = sum(dPositiveElementFactor.values())

    dPositiveElementFactor = oTarget.m_PositiveElementFactor
    iAdd = cl_formula.GetResultByData(oTarget, iAdd, {
        'LifeCycle': oLifeCycle })
    sKey = oLifeCycle.Key()
    dPositiveElementFactor[sKey] = iAdd
    oTarget.m_PositiveElementFactorValue = sum(dPositiveElementFactor.values())
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonChangePositiveElementFactorByType(oTarget, oLifeCycle, iDamType, iAdd):
    
    def ClearFunc(oTarget, oLifeCycle):
        dElementFactor = oTarget.m_PositiveElementFactorByType
        if iDamType not in dElementFactor:
            return None
        dFactor = dElementFactor[iDamType]
        if sKey in dFactor:
            dFactor.pop(sKey, 0)
        if not dFactor:
            dElementFactor.pop(iDamType)
            if iDamType in oTarget.m_PositiveElementFactorValueByType:
                oTarget.m_PositiveElementFactorValueByType.pop(iDamType)
            else:
                oTarget.m_PositiveElementFactorValueByType[iDamType] = sum(dFactor.values())

    dElementFactor = oTarget.m_PositiveElementFactorByType
    iAdd = cl_formula.GetResultByData(oTarget, iAdd, {
        'LifeCycle': oLifeCycle })
    sKey = oLifeCycle.Key()
    dFactor = dElementFactor.setdefault(iDamType, { })
    dFactor[sKey] = iAdd
    oTarget.m_PositiveElementFactorValueByType[iDamType] = sum(dFactor.values())
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonSetImmuneElementRestraint(oTarget, oLifeCyle):
    
    def ClearFunc(oTarget, oLifeCyle):
        oTarget.RemoveImmuneElementRestraint(sKey)

    sKey = oLifeCyle.m_Key
    oTarget.AddImmuneElementRestraint(sKey)
    oLifeCyle.AddDisableFunc(ClearFunc)


def CommonStartSeasonTaskCounting(oListener, oLifeCyle, sFlagKey):
    sKey = oLifeCyle.m_Key
    sTimeCountingKey = sKey + sFlagKey
    if oListener.Query(sTimeCountingKey, -1) >= 0:
        return None
    oListener.Set(sTimeCountingKey, oListener.m_Game.GetFrameNum())


def CommonStatsSeasonTaskCountingToAddProgress(oListener, oLifeCyle, sFlagKey):
    sKey = oLifeCyle.m_Key
    sTimeCountingKey = sKey + sFlagKey
    iStartFrame = oListener.Query(sTimeCountingKey, -1)
    if iStartFrame < 0:
        return None
    iNowFrame = oListener.m_Game.GetFrameNum()
    iAdd = iNowFrame - iStartFrame
    iCur = oListener.QuerySavedData(sKey, 0)
    oListener.Set(sTimeCountingKey, iNowFrame)
    oListener.SetSavedData(sKey, iCur + iAdd)


def CommonResetSeasonTaskCounting(oListener, oLifeCyle, sFlagKey):
    sKey = oLifeCyle.m_Key
    sTimeCountingKey = sKey + sFlagKey
    oListener.Set(sTimeCountingKey, -1)


def CommonSetRelicUnFilterHasRatio(oTarget, oLifeCycle, iRatio, iCurseRatio):
    if not oTarget.m_FightType & WARRIOR_HERO:
        return None
    iRatio = cl_formula.GetResultByData(oTarget, iRatio, {
        'LifeCycle': oLifeCycle })
    oTarget.m_RelicCon.SetUnFilterHasRatio(iRatio, iCurseRatio)
    oTarget.m_RelicCon.SetRepeatFunc(OnRelicRepeatFunc)


def OnRelicRepeatFunc(oGame, iHero, iRelicSID, iLevel, sReason):
    if sReason == 'gm':
        return None
    oHero = oGame.GetObject(iHero)
    if oHero:
        dStaticInfo = {
            'DropLevel': iLevel,
            'DropSource': oHero.m_PlayerID }
        cl_drop.DropPerform(oHero, iRelicSID, dStaticInfo, bFly = True, iShare = 0)


def CommonGetRandomCustomValue(oListener, oLifeCycle, dRamdomInfo):
    oGame = oListener.m_Game
    return ChooseKey(oGame, dRamdomInfo)


def CommonHPModify(oTarget, oLifeCycle, sType, iValue, iCalExcess = 0):
    iMaxValue = oTarget.QueryAttr('%sMax' % sType)
    iValue = cl_formula.GetResultByData(oTarget, iValue, {
        'LifeCycle': oLifeCycle })
    if 0 <= iValue and not (iValue <= iMaxValue):
        SendAlert('err', '%s通用设置血盾甲(%s, %s)数值配置异常。' % (oLifeCycle.Key(), sType, iValue))
        return None
    iModifyValue = getattr(oTarget, sType)() - iValue
    oReason = cl_object.reason.CStrReason(oLifeCycle.Key())
    oTarget.HPDirectModify(sType, oTarget.m_ID, -iModifyValue, oReason, iCalExcess = iCalExcess)


def CommonUpgradeRelic(oTarget, oLifeCycle, iRelic, iNotify = 0):
    oRelicCon = oTarget.m_RelicCon
    oPerform = oLifeCycle.GetObject()
    iExcludeRelic = 0
    if oPerform.m_PFType == PF_TYPE_RELIC:
        iExcludeRelic = oPerform.m_SID
    if iRelic == 0:
        lstRelic = oRelicCon.GetAllRelicByType(RELIC_TYPE_NORMAL)
        lstUpgradeRelic = []
        for oRelic in lstRelic:
            if oRelic.m_Level < oRelic.m_MaxLevel:
                lstUpgradeRelic.append(oRelic.m_SID)
        
        if iExcludeRelic in lstUpgradeRelic:
            lstUpgradeRelic.remove(iExcludeRelic)
        if not lstUpgradeRelic:
            return None
        oGame = oTarget.m_Game
        iRelic = lstUpgradeRelic[oGame.Random(len(lstUpgradeRelic))]
    sReason = oLifeCycle.Key()
    oRelicCon.RemoveRelic(iRelic, sReason, iForce = 1)
    dReward = {
        'item': VIRTUAL_ITEM_RELIC,
        'info': {
            'sid': iRelic,
            'level': 2 } }
    cl_reward.RewardItem(oTarget.m_Game, oTarget, [
        dReward], sReason)
    if not iNotify:
        return None
    iRelicType = cl_perform.GetPerformClassAttr(iRelic, 'm_RelicType')
    if iRelicType == RELIC_TYPE_CURSE:
        return None
    iQuality = cl_perform.GetPerformClassAttr(iRelic, 'm_Quality')
    sName = cl_perform.GetPerformClassAttr(iRelic, 'm_Name')
    if iQuality == QUALITY_TYPE_LOW:
        iChat = 2378
    elif iQuality == QUALITY_TYPE_NORMAL:
        iChat = 2379
    else:
        iChat = 2380
    lstPlayer = [
        oTarget.m_PlayerID]
    cl_notify.SendCommonNotify(oTarget.m_Game, lstPlayer, iChat, {
        '$relicname': sName })


def CommonCreateNpc(oTarget, oLifeCycle, iNpcSID, iOnlySelfVisible, dExtInfo = None):
    iNpcSID = iNpcSID % 10000
    oGame = oTarget.m_Game
    tPos = oTarget.GetPos()
    tFace = oTarget.GetFacing()
    if dExtInfo and 'Scene' in dExtInfo:
        iScene = dExtInfo['Scene']
    else:
        iScene = oTarget.m_Scene
    tTargetPos = cl_math.Vec3DisplaceDir(tPos, tFace, 3)
    (bRet, tTargetPos) = oGame.Scene_GetSpace(iScene, tTargetPos)
    if not bRet:
        tTargetPos = tPos
    else:
        bRet = oGame.Scene_IsDestPosAccessible(iScene, tPos, tTargetPos)
        if not bRet:
            tTargetPos = tPos
    clsNpcData = oGame.m_WarData.GetNpcData(iNpcSID)
    tNpcFace = (-tFace[0], 0, -tFace[2])
    if not clsNpcData:
        SendAlert('err', '%s战场%d未配置NPC(%d)' % (oLifeCycle.Key(), oGame.m_WarMgr.m_SID, iNpcSID))
        return 0
    dParam = clsNpcData.GetNPCModeParam(clsNpcData.m_Shape, clsNpcData.m_FightType, tNpcFace, (1, 1, 1))
    oModelData = cl_modeldata.GetModel(dParam)
    lstHit = oGame.Scene_SweepMultiple(iScene, tTargetPos, oModelData.GetModelRadius(), (0, 1, 0), oModelData.GetModelHeight() + 5, PXMASK_OBJECT, {
        'PassID': oTarget.m_ID })
    if lstHit:
        tTargetPos = tPos
    dAddInfo = {
        'Pos': tTargetPos,
        'Facing': tNpcFace }
    if iOnlySelfVisible:
        dAddInfo['VisiblePlayer'] = {
            oTarget.m_PlayerID: 1 }
    if dExtInfo:
        dAddInfo.update(dExtInfo)
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    oLevelNode = oLevelCtrl.m_CurNode
    dMsgInfo = {
        'NPC': iNpcSID,
        'LevelNode': oLevelNode,
        'NPCInfo': dAddInfo,
        'Scene': iScene }
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_CREATENPC_PRE, oLevelNode.m_CtrlMgr, dMsgInfo)
    if not dMsgInfo['NPC']:
        return 0
    oNpc = oGame.m_ResMgr.CreateNpc(iScene, dMsgInfo['NPC'], dAddInfo)
    return oNpc.m_ID


def CommonRemoveNpc(oTarget, oLifeCycle, iNpc):
    oGame = oTarget.m_Game
    iNpc = cl_formula.GetResultByData(oTarget, iNpc, {
        'LifeCycle': oLifeCycle })
    oNpc = oGame.GetObject(iNpc)
    if not oNpc:
        return None
    oNpc.Remove(oLifeCycle.Key())


def CommonNpcSetShare(oTarget, oLifeCycle, iNpc, iShare):
    oGame = oTarget.m_Game
    iNpc = cl_formula.GetResultByData(oTarget, iNpc, {
        'LifeCycle': oLifeCycle })
    oNpc = oGame.GetObject(iNpc)
    if not oNpc:
        return None
    oNpc.SetShare(iShare)


def CommonGoldenCupNpcSetTimes(oTarget, oLifeCycle, iNpc, iTimes):
    oGame = oTarget.m_Game
    iNpc = cl_formula.GetResultByData(oTarget, iNpc, {
        'LifeCycle': oLifeCycle })
    iTimes = cl_formula.GetResultByData(oTarget, iTimes, {
        'LifeCycle': oLifeCycle })
    oNpc = oGame.GetObject(iNpc)
    if not oNpc:
        return None
    oNpc.SetTimes(iTimes)


def CommonGoldenCupNpcSetAutoRecycle(oTarget, oLifeCycle, iNpc, iAutoRecycle):
    oGame = oTarget.m_Game
    iNpc = cl_formula.GetResultByData(oTarget, iNpc, {
        'LifeCycle': oLifeCycle })
    oNpc = oGame.GetObject(iNpc)
    if not oNpc:
        return None
    oNpc.SetAutoRecycle(iAutoRecycle)


def CommonChangeRelicChooseAllCnt(oTarget, oLifeCycle, iChange):
    iChange = cl_formula.GetResultByData(oTarget, iChange, {
        'LifeCycle': oLifeCycle })
    iCnt = oTarget.GetRelicChooseAllCnt() + iChange
    oTarget.SetRelicChooseAllCnt(iCnt)


def CommonDisableWeaponPerform(oTarget, oLifeCycle, iPerform):
    
    def ClearFunc(oTarget, oLifeCycle):
        oWeapon = oTarget.m_WieldCon.GetItemByID(iWeapon)
        if not oWeapon:
            return None
        oPerform = GetItemPerform(oWeapon, iPerform)
        if not oPerform:
            return None
        oPerform.Enable(oTarget)

    oWeapon = oLifeCycle.GetOwnerSourceWeapon()
    if not oWeapon:
        return None
    oPerform = GetItemPerform(oWeapon, iPerform)
    if not oPerform:
        return None
    iWeapon = oWeapon.m_ID
    oPerform.Disable(oTarget)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonChangeDeviceEnergy(oTarget, oLifeCycle, iAdd, iMul):
    dData = {
        'LifeCycle': oLifeCycle }
    if oTarget.m_FightType & WARRIOR_HERO:
        oAttacker = oTarget
    elif oTarget.m_FightType & WARRIOR_DEVICE:
        oAttacker = oTarget.GetOwner()
    else:
        return None
    if iAdd:
        iAdd = cl_formula.GetResultByData(oTarget, iAdd, dData)
    if iMul:
        iMul = cl_formula.GetResultByData(oTarget, iMul, dData)
        iAdd += oAttacker.QueryAttr('MaxDeviceEnergy') * iMul // 10000
    oAttacker.DeviceEnergyModify(iAdd)


def CommonChangeDevicePerformAttr(oTarget, oLifeCycle, iPerform, sAttr, iAdd, iMul):
    
    def ClearFunc(oTarget, oLifeCycle):
        oDevice = oTarget.GetDevice()
        oPerform = oDevice.GetPerform(iPerform)
        if not oPerform:
            return None
        oPerform.AttrClear(sAttr, sKey, iRefresh = 1)

    if not oTarget.m_FightType & WARRIOR_HERO:
        return None
    oDevice = oTarget.GetDevice()
    if not oDevice:
        return None
    oPerform = oDevice.GetPerform(iPerform)
    if not oPerform:
        return None
    sKey = oLifeCycle.Key()
    dData = {
        'LifeCycle': oLifeCycle }
    if iAdd:
        iAdd = cl_formula.GetResultByData(oTarget, iAdd, dData)
    if iMul:
        iMul = cl_formula.GetResultByData(oTarget, iMul, dData)
    oPerform.AttrChange(sAttr, sKey, iMul, iAdd)
    sUniqueKey = 'ChangeDevicePerformAttr-%s-%s' % (iPerform, sAttr)
    oLifeCycle.AddUniqueDisableFunc(sUniqueKey, ClearFunc, iCover = 0)


def CommonOwnObjAddPerform(oTarget, oLifeCycle, iPerform, iObjectType):
    
    def ClearFunc(oTarget, oLifeCycle):
        oPerformCon = oWarrior.m_Perform
        oPerformCon.RemovePerform(oWarrior, iPerform)

    oWarrior = oTarget.GetOwnObject(iObjectType)
    if not oWarrior:
        return None
    oWarrior.AddPerform(iPerform, 1)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonAddDevicePerformArgsValue(oTarget, oLifeCycle, iPerform, sArg, iAdd, iDisableClear = 0):
    
    def ClearFunc(oTarget, oLifeCycle):
        oPerform = oDevice.GetPerform(iPerform)
        if not oPerform:
            return None
        oPerform.AddArgValue(sArg, -iAdd)

    oDevice = oTarget.GetDevice()
    if not oDevice:
        return None
    oPerform = oDevice.GetPerform(iPerform)
    if not oPerform:
        return None
    dData = {
        'LifeCycle': oLifeCycle }
    iAdd = cl_formula.GetResultByData(oDevice, iAdd, dData)
    oPerform.AddArgValue(sArg, iAdd)
    if iDisableClear:
        oLifeCycle.AddDisableFunc(ClearFunc)


def CommonDisableDevicePF(oTarget, oLifeCycle, iPerform):
    
    def ClearFunc(oTarget, oLifeCycle):
        oClearPerform = oTarget.GetPerform(iPerform)
        if oClearPerform:
            oClearPerform.Enable(oTarget, iNotify = 1)

    oPerform = oTarget.GetPerform(iPerform)
    if oPerform:
        oPerform.Disable(oTarget, iNotify = 1)
        oLifeCycle.AddDisableFunc(ClearFunc)


def CommonAddPlayerDevicePerform(oTarget, oLifeCycle, iPerform):
    
    def ClearFunc(oTarget, oLifeCycle):
        oPerformCon = oTarget.m_DevicePerformCon
        oPerformCon.RemovePerform(oTarget, iPerform)

    oPerformCon = oTarget.m_DevicePerformCon
    oPerformCon.AddPerform(oTarget, iPerform, 1, 1, 0)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonRecycleDevice(oTarget, oLifeCycle):
    if oTarget.m_FightType & WARRIOR_HERO:
        oDeviceOwner = oTarget
    elif oTarget.m_FightType & WARRIOR_DEVICE:
        oDeviceOwner = oTarget.GetOwner()
    else:
        SendAlert('err', '%s通用回收装置配置错误,行为使用者应该是英雄或者装置' % oLifeCycle.Key())
        return None
    oDeviceOwner.m_DeviceMgr.RecycleDevice()


def CommonSwitchMode(oTarget, oLifeCycle, iMode, iTimes, dExtraInfo = None, iNotAutoReset = 0):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.UpdateFuncMode(iMode, 0, { })

    if not oTarget.GetFuncModeTimes(iMode):
        if dExtraInfo:
            oTarget.UpdateFuncMode(iMode, iTimes, dExtraInfo)
        else:
            oTarget.UpdateFuncMode(iMode, iTimes, { })
        sUniqueKey = 'CommonSwitchMode-%s' % iMode
        if not iNotAutoReset:
            oLifeCycle.AddUniqueDisableFunc(sUniqueKey, ClearFunc, iCover = 0)


def CommonAddModeTimes(oTarget, oLifeCycle, iMode, iAdd):
    iAdd = cl_formula.GetResultByData(oTarget, iAdd, {
        'LifeCycle': oLifeCycle })
    if not iAdd:
        return None
    oTarget.AddFuncModeTimes(iMode, iAdd)


def CommonRefreshMode(oTarget, oLifeCycle, iMode, iTimes, dExtraInfo):
    if iMode not in oTarget.GetFuncMode():
        return None
    iTimes = cl_formula.GetResultByData(oTarget, iTimes, {
        'LifeCycle': oLifeCycle })
    oTarget.UpdateFuncMode(iMode, iTimes, dExtraInfo)


def CommonDeviceUsePF(oTarget, oLifeCycle, iPerform, dCustom):
    
    def ClearFunc(oTarget, oLifeCycle):
        oDevice = oTarget.GetDevice()
        if not oDevice:
            return None
        for iActNum, dCasting in oDevice.GetAllCasting():
            if dCasting['pfid'] == iPerform:
                HaltCasting(oDevice, iActNum, oLifeCycle.Key())
        

    oDevice = oTarget.GetDevice()
    if not oDevice:
        return None
    oPerform = oDevice.GetPerform(iPerform)
    if not oPerform:
        return None
    cl_war.UsePerform(oDevice, oPerform, {
        'Custom': dCustom })
    sUniqueKey = 'CommonDeviceUsePF-%s' % iPerform
    oLifeCycle.AddUniqueDisableFunc(sUniqueKey, ClearFunc, iCover = 0)


def CommonSetDeciveAcitveStatus(oTarget, oLifeCycle, iActive):
    oTarget.m_DeviceMgr.SetDeciveActiveStatus(iActive)


def CommonChangeBarrierDeviceEffect(oTarget, oLifeCycle, sAttr, iAdd, iMul):
    
    def ClearFunc(oTarget, oLifeCycle):
        oDevice = oTarget.GetDevice()
        if not oDevice:
            return None
        oDevice.AttrClear(sAttr, sKey)

    oDevice = oTarget.GetDevice()
    if not oDevice:
        return None
    sKey = oLifeCycle.Key()
    dData = {
        'LifeCycle': oLifeCycle }
    if iAdd:
        iAdd = cl_formula.GetResultByData(oTarget, iAdd, dData)
    if iMul:
        iMul = cl_formula.GetResultByData(oTarget, iMul, dData)
    oDevice.AttrChange(sAttr, iMul, iAdd, sKey)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonSetBarrierDeviceInitArgs(oTarget, oLifeCycle, dInfo):
    oTarget.SetBaseFactor(dInfo)


def CommonChooseChangeTalentLevel(oTarget, oLifeCycle):
    sReason = oLifeCycle.Key()
    oTarget.m_TalentCon.ChooseChangeTalentLevel(sReason)


def CommonBanEleAbnormalTrigger(oTarget, oLifeCycle):
    oTarget.m_EleAbnormal.Release()
    oTarget.m_EleAbnormal = cl_abnormalconf.GetNoAbnormalEleDam(oTarget)


def CommonChangeInkBeadNum(oTarget, oLifeCycle, iAdd):
    
    def ClearFunc(oTarget, oLifeCycle):
        oInkCon = oTarget.m_InkCon
        oInkCon.ModifyInkBeadNum(-iTrueModify)

    if oTarget.m_SID != INKMASTER_HERO:
        return None
    iAdd = cl_formula.GetResultByData(oTarget, iAdd, {
        'LifeCycle': oLifeCycle })
    oInkCon = oTarget.m_InkCon
    iTrueModify = oInkCon.ModifyInkBeadNum(iAdd)
    if iTrueModify:
        oLifeCycle.AddDisableFunc(ClearFunc)


def CommonModifyInkValue(oTarget, oLifeCycle, iAdd, sReason = '', dExtra = None):
    if iAdd and oTarget.m_SID == INKMASTER_HERO:
        if not sReason:
            sReason = oLifeCycle.Key()
        iAdd = cl_formula.GetResultByData(oTarget, iAdd, {
            'LifeCycle': oLifeCycle })
        oInkCon = oTarget.m_InkCon
        dExtra = { } if dExtra == None else dExtra
        oInkCon.ModifyInkValue(iAdd, sReason, dExtra)


def CommonSetLimitInkValue(oTarget, oLifeCycle, iLimit):
    if oTarget.m_SID != INKMASTER_HERO:
        return None
    oInkCon = oTarget.m_InkCon
    oInkCon.SetLimitInkValue(iLimit)


def CommonChangeMaxInkValue(oTarget, oLifeCycle, iAdd):
    
    def ClearFunc(oTarget, oLifeCycle):
        oInkCon = oTarget.m_InkCon
        oInkCon.ModifyMaxInkValue(-iTrueModify)

    if oTarget.m_SID != INKMASTER_HERO:
        return None
    iAdd = cl_formula.GetResultByData(oTarget, iAdd, {
        'LifeCycle': oLifeCycle })
    oInkCon = oTarget.m_InkCon
    iTrueModify = oInkCon.ModifyMaxInkValue(iAdd)
    if iTrueModify:
        oLifeCycle.AddDisableFunc(ClearFunc)


def CommonDisablePerformFromOwn(oTarget, oLifeCycle, iPerform, iObjectType):
    
    def ClearFunc(oTarget, oLifeCycle):
        oPerformOwn = oTarget.m_Game.GetObject(iPerformOwnID)
        if not oPerformOwn:
            return None
        oClearPerform = oPerformOwn.GetPerformIfNoThenNew(iPerform)
        if not oClearPerform:
            return None
        oClearPerform.Enable(oPerformOwn)

    iPerformOwnID = oTarget.GetOwnObjectID(iObjectType)
    oPerformOwn = oTarget.m_Game.GetObject(iPerformOwnID)
    if not oPerformOwn:
        return None
    oPerform = oPerformOwn.GetPerformIfNoThenNew(iPerform)
    if not oPerform:
        return None
    oPerform.Disable(oPerformOwn)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonChangeWeaponPerformAttr(oTarget, oLifeCycle, iPerform, sAttr, iAdd, iMul):
    oPerform = GetSourceWeaponPerform(oTarget, oLifeCycle, iPerform)
    if not oPerform:
        return None
    dData = {
        'LifeCycle': oLifeCycle }
    if iMul:
        iMul = cl_formula.GetResultByData(oTarget, iMul, dData)
    if iAdd:
        iAdd = cl_formula.GetResultByData(oTarget, iAdd, dData)
    sKey = oLifeCycle.Key()
    oPerform.AttrChange(sAttr, sKey, iMul, iAdd)
    oLifeCycle.m_PerformApply[(oPerform.m_Item, iPerform, sAttr)] = 1


def CommonSetWeaponPerformArgs(oTarget, oLifeCycle, iPerform, sArg, iVal):
    oPerform = GetSourceWeaponPerform(oTarget, oLifeCycle, iPerform)
    if not oPerform:
        return None
    dData = {
        'LifeCycle': oLifeCycle }
    iVal = cl_formula.GetResultByData(oTarget, iVal, dData)
    oPerform.SetArgValue(sArg, iVal)


def CommonChangeWeaponPerformArgs(oTarget, oLifeCycle, iPerform, sArg, iVal):
    oPerform = GetSourceWeaponPerform(oTarget, oLifeCycle, iPerform)
    if not oPerform:
        return None
    dData = {
        'LifeCycle': oLifeCycle }
    iVal = cl_formula.GetResultByData(oTarget, iVal, dData)
    oPerform.AddArgValue(sArg, iVal)


def CommonGetWeaponPerformArgs(oTarget, oLifeCycle, iPerform, sArg):
    oPerform = GetSourceWeaponPerform(oTarget, oLifeCycle, iPerform)
    if not oPerform:
        return 0
    return oPerform.GetArgValue(sArg)


def GetSourceWeaponPerform(oTarget, oLifeCycle, iPerform):
    oWeapon = oLifeCycle.GetOwnerSourceWeapon()
    if not oWeapon:
        return None
    oPerformCom = oWeapon.GetComponent('Perform')
    if not oPerformCom:
        return None
    return oPerformCom.GetPerform(iPerform)


def CommonCBGetTargetToxicStateCount(oListener, oLifeCycle, sKey):
    oDevice = oListener.GetDevice()
    return oDevice.Query(sKey)


def CommonAddSceneFightMonster(oTarget, oLifeCycle):
    
    def ClearFunc(oTarget, oLifeCycle):
        oScene.m_SceneData.RemoveFightMonster(oTarget.m_ID)

    oScene = oTarget.m_Game.m_SceneMgr.GetScene(oTarget.m_Scene)
    if not oScene:
        return None
    oScene.m_SceneData.AddFightMonster(oTarget.m_ID)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonTriggerStateRefreshBehavior(oTarget, oLifeCycle, iState, dArgs, iFromSameItem = 0, iFromSelf = 0):
    iAttack = oTarget.m_ID if iFromSelf else 0
    if iFromSameItem:
        dEventInfo = oLifeCycle.AttrCache()
        iItem = dEventInfo['ItemID']
    else:
        iItem = 0
    oState = oTarget.m_State.GetStateBySource(iState, iAttack, iItem)
    if not oState or not (oState.m_Enable):
        return None
    if 'arg' in oState.m_StateInfo:
        dStateInfoArgs = oState.m_StateInfo['arg']
        dStateInfoArgs.update(dArgs)
    else:
        oState.m_StateInfo.update({
            'arg': dArgs })
    oState.m_LifeCycle.CallFunc('Refresh', oTarget)


def CommonAddCareerPFBullet(oTarget, oLifeCycle, iPerform, iAdd):
    oPerform = oTarget.GetPerform(iPerform)
    if oPerform and oPerform.m_PFType == PF_TYPE_CAREERPF:
        iAddCount = cl_formula.GetResultByData(oTarget, iAdd, {
            'LifeCycle': oLifeCycle })
        if iAddCount:
            oPerform.AddPFBullet(iAddCount)


def CommonAddSourceWeaponPFBullet(oTarget, oLifeCycle, iPerform, iAdd):
    oWeapon = oLifeCycle.GetOwnerSourceWeapon()
    if not oWeapon:
        return None
    oPerform = GetItemPerform(oWeapon, iPerform)
    if not oPerform:
        return None
    if oPerform and oPerform.m_PFType in (PF_TYPE_SHOOT, PF_TYPE_CONSHOOT, PF_TYPE_CHARGE):
        iAddCount = cl_formula.GetResultByData(oTarget, iAdd, {
            'LifeCycle': oLifeCycle })
        if iAddCount:
            oPerform.AddPFBullet(iAddCount)


def CommonCostSourceWeaponPFBullet(oTarget, oLifeCycle, iPerform, iCost):
    oWeapon = oLifeCycle.GetOwnerSourceWeapon()
    if not oWeapon:
        return None
    oPerform = GetItemPerform(oWeapon, iPerform)
    if not oPerform:
        return None
    if oPerform and oPerform.m_PFType in (PF_TYPE_SHOOT, PF_TYPE_CONSHOOT, PF_TYPE_CHARGE):
        iCostCount = cl_formula.GetResultByData(oTarget, iCost, {
            'LifeCycle': oLifeCycle })
        if iCostCount:
            oPerform.CostPFBullet(iCostCount)


def CommonAddBarrierModelSize(oTarget, oLifeCycle, iWidthScale, iHeightScale):
    
    def ClearFunc(oTarget, oLifeCycle):
        oDevice = oTarget.GetDevice()
        if oDevice:
            (iCurWidthScale, iCurHeightScale, _) = oDevice.m_ModelScale
            iCurWidthScale -= iWidthScale
            iCurHeightScale -= iHeightScale
            oDevice.SetModelScale(iCurWidthScale, iCurHeightScale)

    oDevice = oTarget.GetDevice()
    if not oDevice or oDevice.m_FightType != WARRIOR_DEVICE_BARRIER:
        return None
    (iCurWidthScale, iCurHeightScale, _) = oDevice.m_ModelScale
    iCurWidthScale += iWidthScale
    iCurHeightScale += iHeightScale
    oDevice.SetModelScale(iCurWidthScale, iCurHeightScale)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonGetBarrierDeviceAttr(oTarget, oLifeCycle, sAttr):
    oDevice = oTarget.GetDevice()
    if not oDevice:
        return 0
    return oDevice.QueryAttr(sAttr)


def CommonAppendMaxProbQuality(oTarget, oLifeCycle, iChooseType, iFundamental, iNum, iReplaceRule):
    oGamblerCon = oTarget.m_GamblerCon
    iAssignQuality = oGamblerCon.GetQualityByMaxProb()
    oGamblerCon.TryAppendQuality(iAssignQuality, iChooseType, iFundamental, iNum, iReplaceRule)


def CommonSetDevicePerformIgnoreCostEnergy(oTarget, oLifeCycle, iPerform):
    
    def ClearFunc(oTarget, oLifeCycle):
        oDevice = oTarget.GetDevice()
        dIgnoreCost = oDevice.SetDefault('IgnoreCost', { })
        lstKey = dIgnoreCost.get(iPerform, [])
        if sKey in lstKey:
            lstKey.remove(sKey)
            if lstKey:
                dIgnoreCost[iPerform] = lstKey
            else:
                dIgnoreCost.pop(iPerform)

    if not oTarget.m_FightType & WARRIOR_HERO:
        return None
    oDevice = oTarget.GetDevice()
    if not oDevice:
        return None
    sKey = oLifeCycle.Key()
    dIgnoreCost = oDevice.SetDefault('IgnoreCost', { })
    lstKey = dIgnoreCost.get(iPerform, [])
    if sKey not in lstKey:
        lstKey.append(sKey)
        dIgnoreCost[iPerform] = lstKey
    sUniqueKey = 'DevicePerformIgnoreCost-%s' % iPerform
    oLifeCycle.AddUniqueDisableFunc(sUniqueKey, ClearFunc, iCover = 0)


def CommonGetCurInkAreaSquareByType(oTarget, oLifeCycle, iType):
    if oTarget.m_SID != INKMASTER_HERO:
        return 0
    oInkCon = oTarget.m_InkCon
    return oInkCon.GetCurInkAreaSquareByType(iType)


def CommonGetCurInkAreaSquareFromThrow(oTarget, oLifeCycle):
    if oTarget.m_SID != INKMASTER_HERO:
        return 0
    oInkCon = oTarget.m_InkCon
    return oInkCon.GetCurSquareFromThrow()


def CommonSetPerformAttrFromOwn(oTarget, oLifeCycle, iPerform, sAttr, iVal, iObjectType):
    
    def ClearFunc(oTarget, oLifeCycle):
        oDevice = oTarget.GetDevice()
        oPerform = oDevice.GetPerform(iPerform)
        if not oPerform:
            return None
        oPerform.AttrClear(sAttr, sKey, iRefresh = 1)

    oWarrior = oTarget.GetOwnObject(iObjectType)
    if not oWarrior:
        return None
    oPerform = oWarrior.GetPerform(iPerform)
    if not oPerform:
        return None
    sKey = oLifeCycle.Key()
    if sAttr not in oPerform.m_Attr:
        oPerform.SetAttr(sAttr, 0, 1)
        oPerform.AttrChange(sAttr, sKey, 0, iVal)
    else:
        oPerform.AttrClear(sAttr, sKey)
        iCurVal = oPerform.CalAttr(sAttr)
        iAdd = iVal - iCurVal
        oPerform.AttrChange(sAttr, sKey, 0, iAdd)
    sUniqueKey = 'CommonSetPerformAttrFromOwn-%s-%s' % (iPerform, sAttr)
    oLifeCycle.AddUniqueDisableFunc(sUniqueKey, ClearFunc, iCover = 0)


def CommonStopDeviceEnergyRecover(oTarget, oLifeCycle, iDisableClear, bClearStop):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.StartDeviceEnergyRecover(sKey)

    sKey = oLifeCycle.Key()
    if bClearStop:
        oTarget.StartDeviceEnergyRecover(sKey)
        return None
    oTarget.StopDeviceEnergyRecover(sKey)
    if iDisableClear:
        oLifeCycle.AddDisableFunc(ClearFunc)


def CommonSetNavMeshSize(oTarget, oLifeCycle, fRadius, fHeight):
    (fNavRadius, fNavHeight) = cl_modeldefine.GetModelDefine(oTarget.m_Shape, 'NavMesh')
    if fRadius:
        fNavRadius = fRadius
    if fHeight:
        fNavHeight = fHeight
    oMoveCtrl = oTarget.m_MoveCtrl
    if oMoveCtrl:
        oMoveCtrl.SetNavParams(oTarget, fNavRadius, fNavHeight)


def CommonSetPetAddHateArgs(oTarget, oLifeCycle, iAngle, fRange, fHalfHeight, fHateFactor):
    if not oTarget.m_FightType & WARRIOR_PET:
        return None
    oTarget.Set('AddHateArgs', (iAngle, fRange, fHalfHeight, fHateFactor))


def CommonClearSuperMonster(oTarget, oLifeCycle):
    if not oTarget.m_FightType & WARRIOR_MONSTER:
        return None
    oTarget.ClearMonsterSuper()


def SwitchOwnerPhyAble(oWarrior, oLifeCycle, iEnable):
    oPhyModel = oWarrior.m_PhyModel
    if not oPhyModel:
        return None
    oPhyModel.SetCtrlFlag(CTRL_FLAG_FOR_ALL, iEnable)


def CommonGetAllHPLossInfo(oTarget, oLifeCycle, iTime):
    oLifeCycleOwner = oLifeCycle.GetObject()
    dLossInfo = oLifeCycleOwner.GetArgValue('AllHPLossInfo', { })
    if not dLossInfo:
        return 0
    iTotalLoss = 0
    iNowFrame = oTarget.m_Game.GetFrameNum()
    iFrame = Time2Frame(iTime)
    iNeedFrame = iNowFrame - iFrame
    lstTotalLoss = [ iToatlDam for iHPLossFrame, iToatlDam in dLossInfo.items() if iHPLossFrame >= iNeedFrame ]
    iTotalLoss = sum(lstTotalLoss)
    return iTotalLoss


def CommonSetFightStatusFlag(oTarget, oLifeCycle):
    oTarget.Set('FightStatusFlag', 1)


def CommonSetPetRescueConfig(oTarget, oLifeCycle, iColdTime):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.Delete('RescueConfig')
        oHero = oTarget.GetOwner()
        if oHero:
            oHero.Delete('SingleRescue')
        oDieElement = oTarget.m_Game.m_WarMgr.GetComponent('PVEDieElement')
        if oDieElement:
            oDieElement.CloseRescue(oLifeCycle.Key())

    if not oTarget.m_FightType & WARRIOR_PET:
        return None
    oTarget.Set('RescueConfig', {
        'RescueCDFrame': Time2Frame(iColdTime) })
    oHero = oTarget.GetOwner()
    if not oHero:
        return None
    oHero.Set('SingleRescue', 1)
    oDieElement = oTarget.m_Game.m_WarMgr.GetComponent('PVEDieElement')
    if oDieElement:
        oDieElement.OpenRescue(oLifeCycle.Key())
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonSetFlawData(oTarget, oLifeCycle, iUnbalanceProb, iColdTime, iFlawRange, iUnbalanceEffectTime, iUnbalanceImmobilizeTime, iKillLine, iUnbalanceKillLine, iEffectTime, iHitTimes, iMaxCount, iLockMaxCount, iSize, iUnbalanceColdTime, iWeaknessFlaw, iShareFlaw, iMaxKillLine):
    dData = {
        FLAW_MAXKILLLINE: iMaxKillLine,
        FLAW_UNBALANCE_COLDTIME: iUnbalanceColdTime,
        FLAW_SIZE: iSize,
        FLAW_LOCKMAXCOUNT: iLockMaxCount,
        FLAW_MAXCOUNT: iMaxCount,
        FLAW_HITTIMES: iHitTimes,
        FLAW_EFFECTTIME: iEffectTime,
        FLAW_UNBALANCE_KILLLINE: iUnbalanceKillLine,
        FLAW_KILLLINE: iKillLine,
        FLAW_UNBALANCE_IMMOBILIZETIME: iUnbalanceImmobilizeTime,
        FLAW_UNBALANCE_EFFECTTIME: iUnbalanceEffectTime,
        FLAW_COLDTIME: iColdTime,
        FLAW_UNBALANCE_PROB: iUnbalanceProb }
    oGame = oTarget.m_Game
    iFlawSID = NewTargetFlowSID(oTarget)
    for iHero in oGame.m_WarMgr.GetRoomHero(iCalAI = 0):
        oHero = oGame.GetObject(iHero)
        if not oHero or oHero.m_SID != EXECUTOR_HERO:
            continue
        oFlawCon = oHero.m_FlawCon
        oFlawCon.SetFlawData(iFlawSID, dData)
        oFlawCon.AddRangeFlaw(oTarget, iFlawSID, iFlawRange)
        oFlawCon.PrepareMonsterKillLine(oTarget)
        if iWeaknessFlaw:
            oFlawCon.AddWeaknessFlawMonster(iFlawSID)
        if iShareFlaw:
            oFlawCon.AddShareFlawMonster(iFlawSID)
    


def CommonChangeOwnerMaxBullet(oTarget, oLifeCycle, iBullet, iMul, iAdd):
    
    def ClearChangeMaxBullet(oTarget, oLifeCycle):
        oOwner = oTarget.GetOwner()
        if not oOwner:
            return None
        iBulletNum = oOwner.m_BulletCon.Bullet(iBullet)
        oOwner.m_BulletCon.RemoveBulletMul(iBullet, sKey)
        oLifeCycleOwner = oLifeCycle.GetObject()
        if oLifeCycleOwner and oLifeCycleOwner.GetArgValue('ChangeLeveling', 0) and iBulletNum > oOwner.m_BulletCon.Bullet(iBullet):
            dBulletCache = oLifeCycleOwner.SetArgValueDefault('BulletCache', { })
            dBulletCache[iBullet] = iBulletNum

    oOwner = oTarget.GetOwner()
    if not oOwner:
        return None
    sKey = oLifeCycle.Key()
    dData = {
        'LifeCycle': oLifeCycle }
    iAdd = cl_formula.GetResultByData(oTarget, iAdd, dData)
    iMul = cl_formula.GetResultByData(oTarget, iMul, dData)
    oOwner.m_BulletCon.AddInBulletMul(iBullet, iMul, iAdd, sKey)
    oLifeCycleOwner = oLifeCycle.GetObject()
    if oLifeCycleOwner and oLifeCycleOwner.GetArgValue('ChangeLeveling', 0):
        dBulletCache = oLifeCycleOwner.GetArgValue('BulletCache', { })
        if iBullet in dBulletCache:
            iBulletNum = dBulletCache.pop(iBullet)
            if not dBulletCache:
                oLifeCycleOwner.DelArgValue('BulletCache')
            oOwner.m_BulletCon.SetBullet(iBullet, iBulletNum, iSync = 1)
    oLifeCycle.AddDisableFunc(ClearChangeMaxBullet)


def CommonRelifePet(oTarget, oLifeCycle):
    if not oTarget.IsDead():
        return None
    if not oTarget.m_FightType & WARRIOR_PET:
        return None
    dReason = {
        'Type': TYPE_RELIFE_PASSIVE }
    oTarget.Relife(dReason)


def CommonSetPetRelifeCheckRadius(oTarget, oLifeCycle, fRadius):
    if not oTarget.m_FightType & WARRIOR_PET:
        return None
    oTarget.SetRelifeCheckRadius(fRadius)


def CommonSubPetRandomPerformColdTime(oTarget, oLifeCycle, iNum, iTime):
    lstPerfrom = oTarget.GetEnableSpell()
    if not lstPerfrom:
        return None
    iTime = cl_formula.GetResultByData(oTarget, iTime, {
        'LifeCycle': oLifeCycle })
    iFrame = Time2Frame(iTime)
    for _ in range(iNum):
        lstPerfrom = ShufferList(oTarget.m_Game, lstPerfrom)
        for iPerform in lstPerfrom:
            oPerform = oTarget.GetPerform(iPerform)
            if not oPerform or not (oPerform.m_Enable):
                continue
            if not oPerform.InColdTime():
                continue
            oPerform.ModifyColdTime(oTarget, -iFrame)
        
    


def CommonSetPetAbilityInheritInfo(oTarget, oLifeCycle, iAbility, sKey, iValue):
    if oTarget.m_FightType & WARRIOR_HERO:
        oTarget = oTarget.m_PetCon.GetCurPet()
        if not oTarget:
            return None
    if not oTarget.m_FightType & WARRIOR_PET:
        return None
    iValue = cl_formula.GetResultByData(oTarget, iValue, {
        'LifeCycle': oLifeCycle })
    oTarget.m_AbilityCon.SetInheritableInfo(iAbility, sKey, iValue)


def CommonChangeOwnerObjectAttr(oTarget, oLifeCycle, iObjectType, sAttr, iMul, iAdd, iCalUserOwner):
    
    def ClearChangeOwnerObjectAttr(oTarget, oLifeCycle):
        oOwnerObject = oTarget.GetOwnObject(iObjectType)
        if not oOwnerObject:
            return None
        oOwnerObject.AttrClear(sAttr, sKey)

    oOwnerObject = oTarget.GetOwnObject(iObjectType)
    if not oOwnerObject:
        return None
    dData = {
        'LifeCycle': oLifeCycle }
    oCalTarget = oTarget if iCalUserOwner else oOwnerObject
    if iMul:
        iMul = cl_formula.GetResultByData(oCalTarget, iMul, dData)
    if iAdd:
        iAdd = cl_formula.GetResultByData(oCalTarget, iAdd, dData)
    sKey = oLifeCycle.Key()
    if iMul or iAdd:
        oOwnerObject.AttrChange(sAttr, iMul, iAdd, sKey)
        sUniqueKey = 'ChangeOwnerObjectAttr-%s-%s' % (iObjectType, sAttr)
        oLifeCycle.AddUniqueDisableFunc(sUniqueKey, ClearChangeOwnerObjectAttr, iCover = 0)
    else:
        oOwnerObject.AttrClear(sAttr, sKey)


def CommonSetPetEggDropRatio(oTarget, oLifeCycle, iRatio):
    
    def ClearFunc(oTarget, oLifeCycle):
        oConquerElement.RemovePetEggDropRatio(oTarget.m_ID)

    oConquerElement = oTarget.m_Game.m_WarMgr.GetComponent('ConquerElement')
    if not oConquerElement:
        return None
    oConquerElement.SetPetEggDropRatio(oTarget.m_ID, iRatio)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonForceSetOwnerPetGoodCash(oTarget, oLifeCycle, iCash):
    
    def ClearForceSetOwnerPetGoodCash(oTarget, oLifeCycle):
        oTarget.Delete('ForcePetGoodCash')

    iCash = cl_formula.GetResultByData(oTarget, iCash, {
        'LifeCycle': oLifeCycle })
    oTarget.Set('ForcePetGoodCash', iCash)
    oLifeCycle.AddDisableFunc(ClearForceSetOwnerPetGoodCash)


def CommonPickUpAllInkBead(oTarget, oLifeCycle):
    if oTarget.m_SID != INKMASTER_HERO:
        return None
    oInkCon = oTarget.m_InkCon
    oInkCon.PickUpAllInkBead()


def CommonOpenBossDropPetEgg(oTarget, oLifeCycle):
    
    def ClearFunc(oTarget, oLifeCycle):
        oConquerElement = oTarget.m_Game.m_WarMgr.GetComponent('ConquerElement')
        if not oConquerElement:
            return None
        oConquerElement.ClearBossDropEgg(iHeroID)

    if not oTarget.m_FightType & WARRIOR_HERO:
        SendAlert('err', '%s通用开启BOSS掉落妖灵蛋设置目标需要为英雄' % oLifeCycle.Key())
        return None
    oConquerElement = oTarget.m_Game.m_WarMgr.GetComponent('ConquerElement')
    if not oConquerElement:
        SendAlert('err', '%s未开启妖灵组件,无法设置开启BOSS掉落妖灵蛋' % oLifeCycle.Key())
        return None
    iHeroID = oTarget.m_ID
    oConquerElement.SetBossDropEgg(iHeroID)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonEnableMonsterAureole(oTarget, oLifeCycle, sKey, iAureole):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.m_Game.m_AureoleMgr.RemoveMonsterAureole(iTarger, sKey, sSourceKey)

    iTarger = oTarget.m_ID
    sSourceKey = oLifeCycle.Key()
    oTarget.m_Game.m_AureoleMgr.AddMonsterAureole(iTarger, sKey, iAureole, sSourceKey)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonAddSourceWeaponPFBulletByType(oTarget, oLifeCycle, iType, iAdd):
    oWeapon = oLifeCycle.GetOwnerSourceWeapon()
    if not oWeapon:
        return None
    iPerform = oWeapon.GetWeaponPerformByType(iType)
    oPerform = GetItemPerform(oWeapon, iPerform)
    if not oPerform:
        return None
    iAddCount = cl_formula.GetResultByData(oTarget, iAdd, {
        'LifeCycle': oLifeCycle }, { }, {
        'Perform': oPerform,
        'Weapon': oWeapon })
    if iAddCount:
        oPerform.AddPFBullet(iAddCount)


def CommonChangeSourceWeaponPerformAttrByType(oTarget, oLifeCycle, iType, sAttr, iAdd, iMul):
    oWeapon = oLifeCycle.GetOwnerSourceWeapon()
    if not oWeapon:
        return None
    iPerform = oWeapon.GetWeaponPerformByType(iType)
    oPerform = GetItemPerform(oWeapon, iPerform)
    if not oPerform:
        return None
    sKey = oLifeCycle.Key()
    dData = {
        'LifeCycle': oLifeCycle }
    iMul = cl_formula.GetResultByData(oTarget, iMul, dData)
    iAdd = cl_formula.GetResultByData(oTarget, iAdd, dData)
    if iMul or iAdd:
        oPerform.AttrChange(sAttr, sKey, iMul, iAdd)
        oLifeCycle.m_PerformApply[(oPerform.m_Item, iPerform, sAttr)] = 1
    else:
        oPerform.AttrClear(sAttr, sKey)


def CommonSetResetPetInfo(oTarget, oLifeCycle, iTimes, iCost):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.Delete('ResetPetTimes')
        oTarget.Delete('ResetPetCost')

    if oTarget.Query('ResetPetTimes', 0):
        SendAlert('err', '已设置合宠重置次数，请检查%s' % oLifeCycle.Key())
        return None
    iTimes = cl_formula.GetResultByData(oTarget, iTimes, {
        'LifeCycle': oLifeCycle })
    iCost = cl_formula.GetResultByData(oTarget, iCost, {
        'LifeCycle': oLifeCycle })
    oTarget.Set('ResetPetTimes', iTimes)
    oTarget.Set('ResetPetCost', iCost)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonAddPetShopRefreshTimes(oTarget, oLifeCycle, iTimes):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.Add('PetShopRefreshTimes', -iTimes)

    iTimes = cl_formula.GetResultByData(oTarget, iTimes, {
        'LifeCycle': oLifeCycle })
    oTarget.Add('PetShopRefreshTimes', iTimes)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonAddSeasonFunc(oTarget, oLifeCycle, iFuncType):
    
    def ClearFunc(oTarget, oLifeCycle):
        oSeasonComponent = oWarMgr.GetComponentBySeasonFunc(iFuncType)
        if not oSeasonComponent:
            return None
        oSeasonComponent.ClearSeasonFunc(oTarget.m_ID, iFuncType)

    oWarMgr = oTarget.m_Game.m_WarMgr
    oSeasonComponent = oWarMgr.GetComponentBySeasonFunc(iFuncType)
    if not oSeasonComponent:
        return None
    oSeasonComponent.AddSeasonFunc(oTarget.m_ID, iFuncType)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonSetPFRecoverWeaponPFBullet(oTarget, oLifeCycle, dPerform, iDefault):
    oLifeCycleOwner = oLifeCycle.GetObject()
    dPerform['Default'] = iDefault
    oLifeCycleOwner.SetArgValue('PFRecoverWeaponPFBullet', dPerform)


def CommonGetSteamedStuffedBunRecover(oTarget, oLifeCycle):
    iSteamedStuffedBun = 1604
    oPerform = oTarget.GetPerformIfNoThenNew(iSteamedStuffedBun)
    if not oPerform:
        return None
    cl_war.UsePerform(oTarget, oPerform, { })
    oTarget.RemovePerform(iSteamedStuffedBun)


def CommonTriggerPetSpellShow(oTarget, oLifeCycle):
    oLifeCycleOwner = oLifeCycle.GetObject()
    oOwner = oTarget.GetOwner()
    if not oOwner:
        return None
    iTarget = oTarget.m_ID if oTarget.m_FightType != WARRIOR_PET_MINICLONE else oTarget.m_OwnerPet
    oOwner.m_PetCon.GS2CPetSpellStart(iTarget, oLifeCycleOwner.m_SID)


def CommonSetMoveUsePerform(oTarget, oLifeCycle, iPerform):
    if oTarget.m_Agent:
        oTarget.m_Agent.SetData('MoveUsePerform', iPerform)


def CommonDropPetEggs(oTarget, oLifeCycle, fRadius, dData):
    sKey = oLifeCycle.Key()
    if not fRadius or fRadius < 0:
        SendAlert('err', '%s未设置生成半径' % sKey)
        return None
    if not dData:
        SendAlert('err', '%s未设置妖灵蛋类型、数量' % sKey)
        return None
    PET_EGG_MODEL_NUM = 5565
    oGame = oTarget.m_Game
    oWarMgr = oGame.m_WarMgr
    tModelData = cl_modeldefine.GetModelDefine(PET_EGG_MODEL_NUM, 'Physx')
    if not tModelData:
        SendAlert('err', '%s战场%d未找到模型数据(%d)' % (sKey, oWarMgr.m_SID, PET_EGG_MODEL_NUM))
        return 0
    oConquerElement = oWarMgr.GetComponent('ConquerElement')
    dEggType = oConquerElement.m_ConquerRewardEggSID
    vDir = oTarget.GetFacing()
    iScene = oTarget.m_Scene
    tPos = oTarget.GetPos()
    for iType, iNum in dData.items():
        if iType not in dEggType:
            SendAlert('err', '%s错误的妖灵蛋类型' % sKey)
            return None
        iSID = dEggType[iType]
        for _ in range(iNum):
            dDrop = {
                'Type': iType,
                'SID': iSID }
            tTargetPos = oGame.Scene_RandomPointSectorInMesh(iScene, tPos, vDir, 0, fRadius, 0, 90)
            iFlag = 0
            if tTargetPos:
                if oGame.Scene_IsDestPosAccessible(iScene, tPos, tTargetPos):
                    iFlag = 1
                else:
                    (bRet, tTargetPos) = oGame.Scene_GetSpace(iScene, tTargetPos)
                    if bRet:
                        iFlag = 1
            if iFlag:
                tTargetPos = (tTargetPos[0], tTargetPos[1] + 1.8, tTargetPos[2])
                fGroundDis = oGame.Scene_GroundDistance(iScene, tTargetPos, 5, PXMASK_GROUNDBLK)
                tTargetPos = (tTargetPos[0], tTargetPos[1] - fGroundDis, tTargetPos[2])
                lstHit = oGame.Scene_SweepMultiple(iScene, tTargetPos, tModelData[0], (0, 1, 0), tModelData[1] + 5, PXMASK_LIVEOBJ, {
                    'BlockMask': PXMASK_MOVEBLK,
                    'PassID': oTarget.m_ID })
                if lstHit:
                    tTargetPos = tPos
                else:
                    tTargetPos = tPos
            None.m_ResMgr.CreateDrop(oTarget.m_Scene, NWARRIOR_DROP_PETEGG, tTargetPos, [
                dDrop], { }, { }, oTarget.m_ID, iSplit = 1)
        
    


def CommonSetExtraReward(oTarget, oLifeCycle, iDropType, iDropNum, iDropValue):
    
    def ClearFunc(oTarget, oLifeCycle):
        oConquerElement = oTarget.m_Game.m_WarMgr.GetComponent('ConquerElement')
        if not oConquerElement:
            return None
        oConquerElement.ClearConquerExtraReward(oTarget.m_ID, sKey)

    sKey = oLifeCycle.Key()
    if iDropType not in [
        NWARRIOR_DROP_CASH,
        NWARRIOR_DROP_GSCASH]:
        SendAlert('err', '%s通用设置降服额外奖励暂时只支持铜币或者精魄掉落' % sKey)
        return None
    oConquerElement = oTarget.m_Game.m_WarMgr.GetComponent('ConquerElement')
    if not oConquerElement:
        SendAlert('err', '%s未开启降服组件, 无法设置额外奖励' % sKey)
        return None
    if not oTarget.m_FightType & WARRIOR_HERO:
        SendAlert('err', '%s通用设置降服额外奖励只能作用于英雄' % sKey)
        return None
    dCash = {
        'Cash': iDropValue }
    dReward = {
        'item': VIRTUAL_ITEM_DROP,
        'info': {
            'DropType': iDropType,
            'DropInfo': [
                dCash] } }
    lstReward = [ dReward for _ in range(iDropNum) ]
    oConquerElement.SetConquerExtraReward(oTarget.m_ID, sKey, lstReward)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonGetPetEggs(oTarget, oLifeCycle, dData):
    sKey = oLifeCycle.Key()
    if not dData:
        SendAlert('err', '%s未设置妖灵蛋类型、数量' % sKey)
        return None
    oGame = oTarget.m_Game
    oWarMgr = oGame.m_WarMgr
    oConquerElement = oWarMgr.GetComponent('ConquerElement')
    dEggType = oConquerElement.m_ConquerRewardEggSID
    oPetCon = oTarget.m_PetCon
    for iType, iNum in dData.items():
        if iType not in dEggType:
            SendAlert('err', '%s错误的妖灵蛋类型' % sKey)
            return None
        for _ in range(iNum):
            oPetCon.AddPetEgg(iType)
        
    


def CommonGetStateTransDamFactor(oTarget, oLifeCycle, iStateSID):
    oState = oTarget.m_State.GetItemBySID(iStateSID)
    if oState:
        return oState.GetArgValue('TransDamFactor', { })
    return { }


def CommonSetSceneAIData(oTarget, oLifeCycle, sKey, iValue):
    
    def ClearFunc(oTarget, oLifeCycle):
        oScene = oTarget.m_Game.m_SceneMgr.GetScene(oTarget.m_Scene)
        if not oScene:
            return None
        oScene.m_SceneData.Delete(sKey)

    oScene = oTarget.m_Game.m_SceneMgr.GetScene(oTarget.m_Scene)
    if not oScene:
        return None
    oScene.m_SceneData.Set(sKey, iValue)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonSetMiniCloneNum(oTarget, oLifeCycle, iNum):
    if oTarget.m_FightType != WARRIOR_PET_MINI:
        return None
    iNum = cl_formula.GetResultByData(oTarget, iNum, {
        'LifeCycle': oLifeCycle })
    oTarget.SetMaxClone(iNum)


def CommonChangeSourceWeaponPFBulletPerfomrAttr(oTarget, oLifeCycle, sAttr, iAdd, iMul):
    oWeapon = oLifeCycle.GetOwnerSourceWeapon()
    if not oWeapon:
        return None
    oPerform = oWeapon.GetPFBulletPerform()
    if not oPerform:
        return None
    dData = {
        'LifeCycle': oLifeCycle }
    if iMul:
        iMul = cl_formula.GetResultByData(oTarget, iMul, dData)
    if iAdd:
        iAdd = cl_formula.GetResultByData(oTarget, iAdd, dData)
    sKey = oLifeCycle.Key()
    oPerform.AttrChange(sAttr, sKey, iMul, iAdd)
    oLifeCycle.m_PerformApply[(oPerform.m_Item, oPerform.m_SID, sAttr)] = 1


def CommonFullBullet(oTarget, oLifeCycle, iWeaponType, iNotCostBullet = 0, iSend = 0, iSendAlert = 1):
    sKey = oLifeCycle.Key()
    lstWeapon = oTarget.m_WieldCon.GetWeapons(iWeaponType)
    if not lstWeapon:
        if iSendAlert:
            SendAlert('err', '%s未获取到指定条件武器' % sKey)
        return None
    for oWeapon in lstWeapon:
        oBulletCom = oWeapon.GetComponent('Bullet')
        if not oBulletCom:
            continue
        iMaxBullet = oBulletCom.MaxBullet()
        iNowBullet = oBulletCom.Bullet()
        if iNowBullet >= iMaxBullet:
            continue
        iCnt = iMaxBullet - iNowBullet
        if iNotCostBullet:
            oBulletCom.BulletModify(iCnt, iSendMsg = iSend)
            continue
        iBulletSID = oBulletCom.BulletType()
        iHasBullet = oTarget.m_BulletCon.Bullet(iBulletSID)
        if iCnt > iHasBullet:
            iCnt = iHasBullet
        iCnt = -oBulletCom.BulletModify(iCnt, iSendMsg = iSend)
        oTarget.m_BulletCon.BulletModify(iBulletSID, iCnt, 'fillbullet')
    


def CommonSetDiePriority(oTarget, oLifeCycle, iDiePriority):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.ClearDiePriority(oLifeCycle.Key())

    oTarget.SetDiePriority(iDiePriority, oLifeCycle.Key())
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonAddCustomIntData(oTarget, oLifeCycle, sKey, iVal, iNoAutoClear = 0):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.Add(sKey, -iVal)

    iVal = cl_formula.GetResultByData(oTarget, iVal, {
        'LifeCycle': oLifeCycle })
    oTarget.Add(sKey, iVal)
    if not iNoAutoClear:
        oLifeCycle.AddDisableFunc(ClearFunc)


def CommonGetSavedData(oTarget, oLifeCycle, sFlag):
    return oTarget.QuerySavedData('save.' + sFlag)


def CommonClearImmuneElementRestraint(oTarget, oLifeCyle):
    oTarget.RemoveImmuneElementRestraint(oLifeCyle.m_Key)


def CommonSetMustElementRestraint(oTarget, oLifeCyle):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.ClearMustElementRestraint(sKey)

    sKey = oLifeCyle.m_Key
    oTarget.SetMustElementRestraint(sKey)
    oLifeCyle.AddDisableFunc(ClearFunc)


def CommonClearMustElementRestraint(oTarget, oLifeCyle):
    oTarget.ClearMustElementRestraint(oLifeCyle.m_Key)


def CommonSendRemoveDeBuffStateMessage(oTarget, oLifeCycle):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    oStateCon = oTarget.m_State
    if oStateCon.IsFinalState(oState):
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_REMOVEDEBUFF, oTarget, { })


def CommonGetRelicByInfo(oTarget, oLifeCyle, dInfo, dLevel, dExclude):
    dNormal = { }
    dCurse = { }
    for iRelic in oTarget.m_RelicCon.GetAvailableRelic():
        if iRelic in dExclude:
            continue
        clsPerform = cl_perform.GetPerformModule(iRelic)
        if clsPerform.m_RelicType == RELIC_TYPE_NORMAL:
            dNormal[iRelic] = 1
            continue
        if clsPerform.m_RelicType == RELIC_TYPE_CURSE:
            dCurse[iRelic] = 1
    
    oGame = oTarget.m_Game
    lstRelic = ChooseMulKeys(oGame, dNormal, dInfo[RELIC_TYPE_NORMAL])
    lstCurse = ChooseMulKeys(oGame, dCurse, dInfo[RELIC_TYPE_CURSE])
    lstReward = []
    iLevel = dLevel[RELIC_TYPE_NORMAL] if RELIC_TYPE_NORMAL in dLevel else 1
    for iRelic in lstRelic:
        dReward = {
            'item': VIRTUAL_ITEM_RELIC,
            'info': {
                'sid': iRelic,
                'level': iLevel } }
        lstReward.append(dReward)
    
    iLevel = dLevel[RELIC_TYPE_CURSE] if RELIC_TYPE_CURSE in dLevel else 1
    for iRelic in lstCurse:
        dReward = {
            'item': VIRTUAL_ITEM_RELIC,
            'info': {
                'sid': iRelic,
                'level': iLevel } }
        lstReward.append(dReward)
    
    if lstReward:
        cl_reward.RewardItem(oGame, oTarget, lstReward, oLifeCyle.m_Key)


def CommonAddSourceWeaponPerform(oTarget, oLifeCycle, iPerform):
    
    def ClearFunc(oTarget, oLifeCycle):
        oWeapon = oLifeCycle.GetOwnerSourceWeapon()
        if not oWeapon:
            return None
        oWeaponPerformCon = oWeapon.GetComponent('Perform')
        if not oWeaponPerformCon:
            return None
        oWeaponPerformCon.m_Perform.RemovePerform(oTarget, iPerform)

    oWeapon = oLifeCycle.GetOwnerSourceWeapon()
    if not oWeapon:
        return None
    oWeaponPerformCon = oWeapon.GetComponent('Perform')
    if not oWeaponPerformCon:
        return None
    oWeaponPerformCon.AddPerform(iPerform, iLevel = 1)
    sUniqueKey = 'CommonAddSourceWeaponPerform-%s' % iPerform
    oLifeCycle.AddUniqueDisableFunc(sUniqueKey, ClearFunc, iCover = 0)


def CommonCreateClone(oTarget, oLifeCycle):
    if not (oTarget.m_EnterBattle) or oTarget.m_FightType != WARRIOR_PET_MINI:
        return None
    sKey = oLifeCycle.Key()
    oTarget.CreateClone(sReason = sKey)


def CommonClearPetBronPos(oTarget, oLifeCycle):
    if not oTarget.m_FightType & WARRIOR_PET:
        return None
    oTarget.Delete('PetBornPos')


def CommonCreateHeroSidePet(oTarget, oLifeCycle, iPetSID, iPutWay, dAddData, iNum = 1, iLimit = 0, dState = None, iNumSpillReplace = 0, iDelay = 0):
    
    def ClearFunc(oTarget, oLifeCycle):
        oHeroSidePetCon = oTarget.m_HeroSidePetCon
        lstPet = oHeroSidePetCon.GetHeroSidePetBySource(sKey)
        for iPet in lstPet:
            oHeroSidePetCon.RemoveHeroSidePet(iPet, sReason = sKey, iDieRemove = 0)
        

    if not iNum:
        return None
    import cl_pet
    oHeroSidePetCon = oTarget.m_HeroSidePetCon
    dData = {
        'LifeCycle': oLifeCycle }
    iPetSID = cl_formula.GetResultByData(oTarget, iPetSID, dData)
    iNum = cl_formula.GetResultByData(oTarget, iNum, dData)
    sKey = 'CreateHeroSidePet' + oLifeCycle.Key()
    if iLimit:
        oGame = oTarget.m_Game
        iScene = oTarget.m_Scene
        oScene = oGame.m_SceneMgr.GetScene(iScene)
        if not oScene:
            return None
        lstPet = oHeroSidePetCon.GetHeroSidePetBySource(sKey)
        iCurCnt = len(lstPet)
        iLimit = cl_formula.GetResultByData(oTarget, iLimit, dData)
        iSpillNum = iCurCnt + iNum - iLimit
        if iSpillNum > 0:
            if iNumSpillReplace:
                for iIdx in range(iSpillNum):
                    oHeroSidePetCon.RemoveHeroSidePet(lstPet[iIdx], sReason = sKey, iDieRemove = 0)
                
            else:
                iNum = iLimit - iCurCnt
                if not iNum:
                    return None
    oReason = cl_object.reason.CStrReason(sKey)
    dAddData = cl_formula.CalArgsFormula(oTarget, dAddData, dData)
    for _ in range(iNum):
        oPet = cl_pet.CreatePet(oTarget.m_Game, oTarget, iPetSID, iPutWay, dAddData)
        if not oPet:
            continue
        oHeroSidePetCon.AddHeroSidePet(oPet, sReason = sKey)
        for iState in dState:
            oState = cl_state.AddState(oPet, iState, STATE_TIME_FOREVER, 0, {
                'AID': oPet.m_ID,
                'RS': oReason })
            if oState:
                oState.Enable(oPet)
        
        if not iDelay:
            continue
        iDelayFrame = Time2Frame(iDelay)
        if iDelayFrame:
            func = Functor(TimeClearPet, oPet, sKey)
            oPet.Call_Out(func, Time2Frame(iDelay), sKey)
    
    oLifeCycle.AddUniqueDisableFunc(sKey, ClearFunc, iCover = 0)


def TimeClearPet(oPet, sKey):
    oPet.Remove_Call_Out(sKey)
    oOwner = oPet.GetOwner()
    if not oOwner:
        return None
    oOwner.m_HeroSidePetCon.RemoveHeroSidePet(oPet.m_ID, sReason = 'TimeClearPet', iDieRemove = 0)


def CommonSetSeasonSuitElement(oTarget, oLifeCycle, iElement):
    if iElement not in SUIT_ELEMENT:
        return None
    oTarget.SetSavedData('SeasonSuit_NowElement', iElement)
    cl_snetwar.GS2CSeasonSuitOptionInfo(SUIT_HANDLE_ELEMENT, [
        iElement], oTarget.m_Game, oTarget)


def CommonCutSeasonSuitElement(oTarget, oLifeCycle, iSuit):
    oSeasonSuitElement = oTarget.m_Game.m_WarMgr.GetSeasonSuitElement()
    if not oSeasonSuitElement:
        return 0
    oSeasonSuitElement.ChangeSuitElement(oTarget, iSuit)


def CommonUpdateStateCountEff(oTarget, oLifeCycle, iCountEff):
    sEffKey = 'StateCountEff'
    iCountEff = cl_formula.GetResultByData(oTarget, iCountEff, oLifeCycle.AttrCache())
    if iCountEff == 0:
        oTarget.Delete(sEffKey)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_UPDATE_STATECOUNTEFF, oTarget, { })
        return None
    iCurCountEff = oTarget.Query(sEffKey, 0)
    if iCurCountEff:
        SendAlert('err', '%s %s %s 重复设置状态计数加成系数' % (oTarget.m_Game.m_ID, oTarget.m_PlayerID, oLifeCycle.Key()))
        return None
    oTarget.Set(sEffKey, iCountEff)
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_UPDATE_STATECOUNTEFF, oTarget, { })


def CommonChooseForceDisableCurseRelic(oTarget, oLifeCycle, iCnt):
    oTarget.m_RelicCon.ChooseForceDisableCurseRelic(oTarget, iCnt, oLifeCycle.Key())


def CommonUnsetForceDisableCurseRelic(oTarget, oLifeCycle):
    oTarget.m_RelicCon.UnsetAllRelicForceDisable()


def CommonSetTotalHPExcludeOrderRelic(oTarget, oLifeCycle, dInfo):
    if not dInfo:
        return None
    lstKeys = []
    for iRelic, _ in dInfo.items():
        oRelic = oTarget.m_RelicCon.GetPerform(iRelic)
        if not oRelic or not (oRelic.m_LifeCycle):
            continue
        lstKeys.append(oRelic.m_LifeCycle.Key())
    
    iTotalHP = 0
    if oTarget.m_DefendTrend == DEFEND_TREND_SHIELD:
        lstMaxAtt = [
            'HPMax',
            'ShieldMax']
    elif oTarget.m_DefendTrend == DEFEND_TREND_ARMOR:
        lstMaxAtt = [
            'HPMax',
            'ArmorMax']
    else:
        lstMaxAtt = [
            'HPMax']
    for sAttr in lstMaxAtt:
        oAttr = oTarget.GetAttr(sAttr)
        iTotalHP += oAttr.GetExcludeValue(lstKeys)
    
    oTarget.Set('ExcludeRelicTotalHP', iTotalHP)
    return iTotalHP


def CommonBanTagerRelicToTempRelic(oTarget, oLifeCycle, dBanRelicInfo):
    lstBanRelic = list(dBanRelicInfo)
    oTarget.SetSavedData('SeasonSuit_BanRelic', dBanRelicInfo)
    cl_snetwar.GS2CSeasonSuitOptionInfo(SUIT_HANDLE_BANRELIC, lstBanRelic, oTarget.m_Game, oTarget)


def CommonSendSeasonSuitTempRelic(oTarget, oLifeCycle, iApply, iTempLevel, iMaxNum):
    lstRelic = oTarget.QuerySavedData('SeasonSuit_NowRelic', [])
    iNowNum = len(lstRelic)
    if iNowNum != iMaxNum:
        if iNowNum > iMaxNum:
            lstRelic = lstRelic[:iMaxNum]
        if iNowNum < iMaxNum:
            lstRelic = lstRelic + [
                0] * (iMaxNum - iNowNum)
    if iApply:
        oRelicCon = oTarget.m_RelicCon
        dInfo = {
            'TempLevel': iTempLevel }
        for iIndex, iRelic in enumerate(lstRelic[:]):
            oPerform = oRelicCon.GetPerform(iRelic)
            if not oPerform:
                lstRelic[iIndex] = 0
                continue
            oPerform.SetOtherLifeCycle(oTarget, RELIC_LIFECYCLE_TEMPLEVEL, dInfo)
            lstRelic[iIndex] = iRelic
        
    oTarget.SetSavedData('SeasonSuit_NowRelic', lstRelic)
    cl_snetwar.GS2CSeasonSuitOptionInfo(SUIT_HANDLE_INTENSIFY, lstRelic, oTarget.m_Game, oTarget)


def CommonClearSeasonSuitTempRelic(oTarget, oLifeCycle, iClaerInfo):
    lstRelic = oTarget.QuerySavedData('SeasonSuit_NowRelic', [])
    oRelicCon = oTarget.m_RelicCon
    for iRelic in lstRelic:
        oPerform = oRelicCon.GetPerform(iRelic)
        if not oPerform:
            continue
        oPerform.RemoveOtherLifeCycle(oTarget, RELIC_LIFECYCLE_TEMPLEVEL)
    
    if iClaerInfo:
        oTarget.SetSavedData('SeasonSuit_NowRelic', [])
    cl_snetwar.GS2CSeasonSuitOptionInfo(SUIT_HANDLE_INTENSIFY, [], oTarget.m_Game, oTarget)


def CommonGetOwnerAttrBaseValue(oTarget, oLifeCycle, sAttr):
    oAttr = oTarget.GetAttr(sAttr)
    if not oAttr:
        return 0
    return oAttr.GetBaseAttr()


def CommonAddMonsterModelSize(oTarget, oLifeCycle, iAddScale, iChangeClientMode):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.SetModelScale(100, iChangeClientMode)

    if not oTarget.m_FightType & WARRIOR_MONSTER:
        return None
    iAddScale = cl_formula.GetResultByData(oTarget, iAddScale, {
        'LifeCycle': oLifeCycle })
    iOldScale = oTarget.Query('Scale')
    oTarget.SetModelScale(iOldScale + iAddScale, iChangeClientMode)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonAddExcessAttr(oTarget, oLifeCycle, sAttr, iAdd, iCalMul, iHPModify = 1):
    iAdd = cl_formula.GetResultByData(oTarget, iAdd, {
        'LifeCycle': oLifeCycle })
    if iCalMul:
        oTarget.AddExcessAttr(sAttr, iAdd, iHPModify)
    else:
        oTarget.TrueModifyExcessAttr(sAttr, iAdd, iHPModify)


def CommonSimulationChooseQuality(oTarget, oLifeCycle):
    return ChooseKey(oTarget.m_Game, oTarget.m_GamblerCon.m_QualityProb)


def CommonAddSuitPerform(oTarget, oLifeCycle, iPerform):
    
    def ClearFunc(oTarget, oLifeCycle):
        oPerformCon = oTarget.m_Perform
        oPerformCon.RemovePerform(oTarget, iPerform)

    if oTarget.GetPerform(iPerform):
        return None
    oPerform = oTarget.AddPerform(iPerform, 1)
    if not oPerform:
        return None
    oLifeCycle.AddDisableFunc(ClearFunc)
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ADDSUITPERFORM, oTarget, {
        'Perform': iPerform })


def CommonSubTargetPerformColdTimeByType(oListener, oLifeCycle, iType, iTime, iPercent):
    lstPerform = oListener.GetPerformSIDByType(iType)
    oPerformCom = oListener.m_Perform
    iTime = cl_formula.GetResultByData(oListener, iTime, {
        'LifeCycle': oLifeCycle })
    iFrame = Time2Frame(iTime)
    for iPerform in lstPerform:
        oPerform = oListener.GetPerform(iPerform)
        if not oPerform:
            continue
        iColdTimeFrame = oPerformCom.GetTotalColdTime(iPerform)
        if not iColdTimeFrame:
            continue
        if iPercent > 0:
            iMaxColdTimeFrame = oPerformCom.GetMaxColdTime(iPerform)
            iFrame += iMaxColdTimeFrame * iPercent // 10000
        oPerformCom.ModifyColdTime(iPerform, -iFrame)
    


def CommonRecordTimeLimitInfo(oListener, oLifeCycle, sArg, iVal):
    oLifeCycleOwner = oLifeCycle.GetObject()
    if not oLifeCycleOwner:
        return None
    dTimeLimitInfo = oLifeCycleOwner.GetArgValue(sArg, { })
    iChange = cl_formula.GetResultByData(oListener, iVal, {
        'LifeCycle': oLifeCycle })
    iNowFrame = oListener.m_Game.GetFrameNum()
    if iNowFrame in dTimeLimitInfo:
        dTimeLimitInfo[iNowFrame] += iChange
    else:
        dTimeLimitInfo[iNowFrame] = iChange
    oLifeCycleOwner.SetArgValue(sArg, dTimeLimitInfo)


def CommonSetSeasonSuitArg(oListener, oLifeCycle, iSID, sArg, iVal, iSave):
    oSeasonSuit = oListener.m_Game.m_WarMgr.GetSeasonSuitElement()
    if not oSeasonSuit:
        return None
    if not oSeasonSuit.GetSuitOpenStatus(oListener, iSID):
        return None
    iVal = cl_formula.GetResultByData(oListener, iVal, {
        'LifeCycle': oLifeCycle })
    if iSave:
        oSeasonSuit.SetSavedSuitArg(oListener, iSID, sArg, iVal)
    else:
        oSeasonSuit.SetSuitArg(oListener, iSID, sArg, iVal)


def CommonGetSeasonSuitArg(oListener, oLifeCycle, iSID, sArg, iSave):
    oSeasonSuit = oListener.m_Game.m_WarMgr.GetSeasonSuitElement()
    if not oSeasonSuit:
        return 0
    if iSave:
        return oSeasonSuit.GetSavedSuitArg(oListener, iSID, sArg)
    return oSeasonSuit.GetSuitArg(oListener, iSID, sArg)


def CommonChangeSeasonSuitArg(oListener, oLifeCycle, iSID, sArg, iChange, iSave):
    oSeasonSuit = oListener.m_Game.m_WarMgr.GetSeasonSuitElement()
    if not oSeasonSuit:
        return None
    iChange = cl_formula.GetResultByData(oListener, iChange, {
        'LifeCycle': oLifeCycle })
    if iSave:
        iNowValues = oSeasonSuit.GetSavedSuitArg(oListener, iSID, sArg)
        oSeasonSuit.SetSavedSuitArg(oListener, iSID, sArg, iNowValues + iChange)
        return None
    iNowValues = oSeasonSuit.GetSuitArg(oListener, iSID, sArg)
    oSeasonSuit.SetSuitArg(oListener, iSID, sArg, iNowValues + iChange)


def CommonSetRelicDisable(oTarget, oLifeCycle, iSID):
    
    def ClearFunc(oTarget, oLifeCycle):
        oRelic = oTarget.m_RelicCon.GetPerform(iSID)
        if not oRelic:
            return None
        oRelic.ClearDisableSource(oLifeCycle.Key())
        oRelic.Enable(oTarget)

    oRelic = oTarget.m_RelicCon.GetPerform(iSID)
    if not oRelic:
        return None
    oRelic.SetDisableSource(oLifeCycle.Key())
    oRelic.Disable(oTarget)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonShowShopHiddenGoods(oTarget, oLifeCycle, iPos):
    oTarget.m_BuyMgr.ShowHiddenGoods(iPos)


def CommonUsePerformInFace(oWarrior, oLifeCycle, iPerform, iDis, dCustom):
    oPerform = oWarrior.GetPerform(iPerform)
    if not oPerform:
        return None
    dData = {
        'Custom': dCustom }
    if 'vEnd' in dCustom:
        SendAlert('err', '回调在自身面前使用技能重复定义vEnd' % oLifeCycle.m_StableKey)
    vFacting = oWarrior.GetFacing()
    vPos = oWarrior.GetPos()
    vPos = (vPos[0], vPos[1] + oWarrior.m_ModelHeight / 2, vPos[2])
    vEnd = cl_math.Vec3DisplaceDir(vPos, vFacting, iDis)
    dCustom['vEnd'] = vEnd
    cl_war.UsePerform(oWarrior, oPerform, dData)


def CommonAddFilterRelic(oTarget, oLifeCycle, iRelicSID):
    sKey = oLifeCycle.Key()
    oTarget.m_RelicCon.AddFilterRelic(iRelicSID, sKey)


def CommonAddBlankRelic(oTarget, oLifeCycle, iNum):
    oTarget.m_RelicCon.ChangeBlankRelicNum(iNum, oLifeCycle.Key())


def CommonGetMonsterStateNumInScene(oTarget, oLifeCycle, sCacheFlag, iCacheFlagTime, dState):
    oGame = oTarget.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oTarget.m_Scene)
    if not oScene:
        return 0
    iCurFrame = oGame.GetFrameNum()
    if sCacheFlag in oScene.m_CustomData:
        (iRecordFrame, iRecordCnt) = oScene.m_CustomData[sCacheFlag]
        iIntervalFrame = Time2Frame(iCacheFlagTime)
        if iCurFrame - iRecordFrame < iIntervalFrame:
            return iRecordCnt
    iCnt = 0
    for iMonster in oScene.GetObjectsByType('Monster'):
        oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
        if not oMonster:
            continue
        for iStateSID in dState:
            if oMonster.m_State.GetItemBySID(iStateSID):
                iCnt += 1
        
    
    oScene.m_CustomData[sCacheFlag] = (iCurFrame, iCnt)
    return iCnt


def CommonCreateBuildOnRangePlayPoint(oTarget, oLifeCycle, iBuildSID, iShape, iSide, sPointKey, iNum):
    
    def ClearFunc(oTarget, oLifeCycle):
        oReason = cl_object.reason.CStrReason(oLifeCycle.Key(), None, {
            'DamType': DAM_TYPE_TRUE | DAM_TYPE_SCENE | DAM_USE_HP })
        for iBuild in lstCreate:
            oBuild = oTarget.m_Game.GetObject(iBuild, PY_FLAG_DEAD)
            if oBuild:
                oBuild.HPModifyDam(0, [
                    [
                        oBuild.HP(),
                        oReason]])
        

    if not oTarget.m_LineIdx:
        return None
    oGame = oTarget.m_Game
    clsBuildData = oGame.m_WarData.GetBuildData(iBuildSID)
    if not clsBuildData:
        return None
    oScene = oGame.m_SceneMgr.GetScene(oTarget.m_Scene)
    if not oScene:
        return None
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    oLevelConfData = oLevelCtrl.m_LevelConfData
    oLine = oLevelCtrl.GetLineNode(oTarget.m_LineIdx)
    lstConfig = oLevelConfData.GetLineConfig(oLine.m_LevelNode.m_Level, oLine.m_Name, 'GamePlayPoint', sPointKey)
    if not lstConfig:
        SendAlert('err', '%s %s 未配置点位%s' % (oGame.m_ID, oTarget.m_LineIdx, sPointKey))
        return None
    lstCreate = []
    iLen = len(lstConfig)
    if iNum > iLen:
        SendAlert('err', '%s %s 点位%s数量%s<%s' % (oGame.m_ID, oTarget.m_LineIdx, sPointKey, iLen, iNum))
    elif iNum < iLen:
        lstConfig = ShufferList(oGame, lstConfig, iNum)
    iScene = oTarget.m_Scene
    tModelData = cl_modeldefine.GetModelDefine(clsBuildData.m_Shape, 'Physx')
    for dConfig in lstConfig:
        dAddData = {
            'Shape': iShape,
            'Angle': cl_math.Radians2Angle(cl_math.Dir2Radians(dConfig['Facing'])),
            'Scale': dConfig['Scale'],
            'Center': (0, 0, 0),
            'Size': (tModelData[1], tModelData[0], 0),
            'Origin': dConfig['Pos'],
            'Owner': oTarget.m_ID,
            'Side': iSide }
        oBuild = oGame.m_ResMgr.CreateBuild(iScene, iBuildSID, dAddData)
        lstCreate.append(oBuild.m_ID)
    
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonChangePerformDamTypeByPerformType(oTarget, oLifeCycle, iPerformType, iObjectType, iDamType, iOnlyChangeNorMal, iIgnoreSelfChange):
    
    def ClearChangePerformDamType(oTarget, oLifeCycle):
        sKey = oLifeCycle.Key()
        oWarrior = oTarget.m_Game.GetObject(iWarrior)
        if not oWarrior:
            return None
        lstPerform = oWarrior.GetPerformSIDByType(iPerformType)
        for iPerform in lstPerform:
            oPerform = oWarrior.GetPerform(iPerform)
            if not oPerform:
                continue
            oPerform.m_ElementTypeObj.RemoveSetModify(sKey)
        

    sKey = oLifeCycle.Key()
    iWarrior = oTarget.GetOwnObjectID(iObjectType)
    oWarrior = oTarget.m_Game.GetObject(iWarrior)
    if not oWarrior:
        return None
    lstPerform = oWarrior.GetPerformSIDByType(iPerformType)
    iDamType = cl_formula.GetResultByData(oTarget, iDamType, {
        'LifeCycle': oLifeCycle })
    for iPerform in lstPerform:
        oPerform = oWarrior.GetPerform(iPerform)
        if not oPerform:
            continue
        oElement = oPerform.m_ElementTypeObj
        iNowElement = oElement.GetExcludeValue(sKey) if iIgnoreSelfChange else oElement.GetValue()
        if iOnlyChangeNorMal and iNowElement != DAM_TYPE_NORMAL:
            continue
        oElement.SetModify(sKey, iDamType)
    
    sUniqueKey = 'ChangePerformDamType-%s-%s' % (iPerformType, iObjectType)
    oLifeCycle.AddUniqueDisableFunc(sUniqueKey, ClearChangePerformDamType, iCover = 0)


def CommonAddStateStatisticsKeyItemID(oTarget, oLifeCycle, iValue, iStateSID, sExtAttr, iFlag):
    lstAdd = oTarget.m_WieldCon.GetWeapons(iFlag)
    for oWeapon in lstAdd:
        sAttr = sExtAttr + str(oWeapon.m_ID)
        CommonAddStateStatistics(oTarget, oLifeCycle, iStateSID, iValue, sAttr)
    


def CommonAddStateStatistics(oTarget, oLifeCycle, iStateSID, iValue, sAttr):
    oStateCon = oTarget.m_State
    oState = oStateCon.GetItemBySID(iStateSID)
    if not oState:
        return None
    iValue = cl_formula.GetResultByData(oTarget, iValue, {
        'LifeCycle': oLifeCycle })
    if sAttr in oState.m_Data:
        oState.m_Data[sAttr] += iValue
    else:
        oState.m_Data[sAttr] = iValue


def CommonSetStateStatisticsKeyItemID(oTarget, oLifeCycle, iValue, iStateSID, sExtAttr, iFlag):
    lstAdd = oTarget.m_WieldCon.GetWeapons(iFlag)
    for oWeapon in lstAdd:
        sAttr = sExtAttr + str(oWeapon.m_ID)
        CommonStateStatistics(oTarget, oLifeCycle, iStateSID, iValue, sAttr)
    


def CommonGetStateStatisticsKeyItemID(oTarget, oLifeCycle, iStateSID, sExtAttr, iFlag, iPos):
    if iPos:
        oWeapon = oTarget.m_WieldCon.GetItemByPos(iPos)
        if not oWeapon:
            return 0
        sAttr = sExtAttr + str(oWeapon.m_ID)
        return CommonGetStateStatistics(oTarget, oLifeCycle, iStateSID, sAttr)
    lstAdd = oTarget.m_WieldCon.GetWeapons(iFlag)
    for oWeapon in lstAdd:
        sAttr = sExtAttr + str(oWeapon.m_ID)
        return CommonGetStateStatistics(oTarget, oLifeCycle, iStateSID, sAttr)
    
    return 0


def CommonGetStateStatistics(oTarget, oLifeCycle, iStateSID, sAttr):
    oStateCon = oTarget.m_State
    oState = oStateCon.GetItemBySID(iStateSID)
    if not oState:
        return 0
    if sAttr not in oState.m_Data:
        return 0
    return oState.m_Data[sAttr]


def CommonTriggerReduceSuitTakeEffectAmount(oTarget, oLifeCycle, dInfo):
    sKey = dInfo['Key']
    if oTarget.QuerySavedData(sKey, 0):
        return None
    if 'MapLoadOKCb' in dInfo:
        cbFun = Functor(OpenReduceSuitTakeEffectAmountUI, dInfo)
        oTarget.AddMapLoadOKCbFun(sKey, cbFun)
    OpenReduceSuitTakeEffectAmountUI(dInfo, oTarget, { })


def OpenReduceSuitTakeEffectAmountUI(dInfo, oWarrior, dMsgInfo):
    from cl_npc import net
    if oWarrior.QuerySavedData(dInfo['Key'], 0):
        return 1
    oSuitElement = oWarrior.m_Game.m_WarMgr.GetSeasonSuitElement()
    if not oSuitElement:
        return 1
    lstSuit = oSuitElement.GetAllCanConditionReduceSuit(oWarrior.m_ID)
    if not lstSuit:
        return 1
    net.GS2COpenReduceSuitTakeEffectAmountUI(oWarrior, lstSuit, dInfo['ChooseNum'], dInfo['UIType'])
    net.SetNpcUICallBackFunction(oWarrior, NPC_CB_VALUELIST, Functor(ReduceSuitTakeEffectAmount, dInfo))
    if 'CheckCondiReduce' in dInfo:
        net.SetNpcUICallBackFunction(oWarrior, NPC_CB_VALUE, CheckCondiReduce)
    return 0


def ReduceSuitTakeEffectAmount(dInfo, oWarrior, lstAnswer):
    if not lstAnswer:
        return None
    sKey = dInfo['Key']
    if 'MapLoadOKCb' in dInfo:
        oWarrior.RemoveMapLoadOKCbFun(sKey)
    if oWarrior.QuerySavedData(sKey, 0):
        return None
    oWarrior.SetSavedData(sKey, 1)
    oSuitElement = oWarrior.m_Game.m_WarMgr.GetSeasonSuitElement()
    if not oSuitElement:
        return None
    if 'FromSuit' in dInfo:
        iFromSuit = dInfo['FromSuit']
        iNum = oSuitElement.GetSuitConditionNum(oWarrior.m_ID, iFromSuit)
        if iNum < dInfo['CheckSuitNum']:
            return None
    iFromSuit = 0
    lstReduceSuit = []
    iGame = oWarrior.m_Game.m_ID
    iPlayer = oWarrior.m_PlayerID
    iReduceNum = dInfo['ReduceNum']
    iChooseNum = dInfo['ChooseNum']
    if len(lstAnswer) > iChooseNum:
        SeasonsuitLog.Alert('%d %d %s numerr %s' % (iGame, iPlayer, sKey, lstAnswer))
        lstAnswer = lstAnswer[:iChooseNum]
    for iSuit in lstAnswer:
        if iSuit in lstReduceSuit:
            SeasonsuitLog.Alert('%d %d %s repetition %s' % (iGame, iPlayer, sKey, lstAnswer))
            continue
        lstReduceSuit.append(iSuit)
        clsSuit = GetSeasonSuitCls(iSuit)
        if not clsSuit:
            SeasonsuitLog.Alert('%d %d %s nosuit %d' % (iGame, iPlayer, sKey, iSuit))
            continue
        if not oSuitElement.CheckCondiReduce(oWarrior.m_ID, iSuit):
            SeasonsuitLog.Alert('%d %d %s reduceerr %d' % (iGame, iPlayer, sKey, iSuit))
            continue
        oSuitElement.SuitCondiReduce(oWarrior, clsSuit, iReduceNum, sKey, iFromSuit)
    


def CheckCondiReduce(oWarrior, iSuit):
    from cl_npc import net
    oSuitElement = oWarrior.m_Game.m_WarMgr.GetSeasonSuitElement()
    if not oSuitElement or not oSuitElement.CheckCondiReduce(oWarrior.m_ID, iSuit):
        iResult = 0
    else:
        iResult = 1
    net.GS2CUpdateCheckReduceSuitResult(oWarrior, iSuit, iResult)


def CommonAddChangeHPDamTypeReason(oTarget, oLifeCycle, iPriority):
    
    def ClearFunc(oTarget, oLifeCycle):
        setReason = oTarget.Query('ChangeHPDamTypeReason', set({ }))
        if iPriority in setReason:
            setReason.remove(iPriority)

    setReason = oTarget.SetDefault('ChangeHPDamTypeReason', set({ }))
    setReason.add(iPriority)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonGetSuitConditionNum(oTarget, oLifeCycle, iSuit):
    oSuitElement = oTarget.m_Game.m_WarMgr.GetSeasonSuitElement()
    if not oSuitElement:
        return 0
    return oSuitElement.GetSuitConditionNum(oTarget.m_ID, iSuit)


def CommonSendSuitHandleInfo(oTarget, oLifeCycle, iHandleType, dInfo, lstResult = None):
    if not lstResult:
        dResult = cl_formula.CalArgsFormula(oTarget, dInfo, {
            'LifeCycle': oLifeCycle })
        lstResult = dResult.values()
    cl_snetwar.GS2CSeasonSuitOptionInfo(iHandleType, lstResult, oTarget.m_Game, oTarget)


def CommonSetPerformSpecialTag(oTarget, oLifeCycle, iTag, dPerform):
    
    def ClearFunc(oTarget, oLifeCycle):
        dPerformSpecialTag = oTarget.Query('PerformSpecialTag', { })
        if not dPerformSpecialTag:
            return None
        if iTag not in dPerformSpecialTag:
            return None
        dTagInfo = dPerformSpecialTag[iTag]
        for iPerform in dPerform:
            if iPerform not in dTagInfo:
                continue
            lstKey = dTagInfo[iPerform]
            if sKey not in lstKey:
                continue
            lstKey.remove(sKey)
            if not lstKey:
                dTagInfo.pop(iPerform)
        
        if dTagInfo:
            dPerformSpecialTag[iTag] = dTagInfo
            oTarget.Set('PerformSpecialTag', dPerformSpecialTag)
        else:
            dPerformSpecialTag.pop(iTag)
            if not dPerformSpecialTag:
                oTarget.Delete('PerformSpecialTag')

    dPerformSpecialTag = oTarget.SetDefault('PerformSpecialTag', { })
    if iTag not in dPerformSpecialTag:
        dPerformSpecialTag[iTag] = { }
    dTagInfo = dPerformSpecialTag[iTag]
    sKey = oLifeCycle.Key()
    for iPerform in dPerform:
        if iPerform not in dTagInfo:
            dTagInfo[iPerform] = []
        lstKey = dTagInfo[iPerform]
        if sKey in lstKey:
            continue
        lstKey.append(sKey)
    
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonRecordItemActiveTime(oTarget, oLifeCycle, sKey):
    oLifeCycleOwner = oLifeCycle.GetObject()
    if not oLifeCycleOwner:
        return None
    iCurFrame = oTarget.m_Game.GetFrameNum()
    (iLastFrame, _) = oLifeCycleOwner.GetArgValue(sKey, (0, 0))
    oLifeCycleOwner.SetArgValue(sKey, (iCurFrame, Frame2Time(iCurFrame - iLastFrame)))


def CommonGetItemActiveInterval(oTarget, oLifeCycle, sKey):
    oLifeCycleOwner = oLifeCycle.GetObject()
    if not oLifeCycleOwner:
        return 0
    (_, iInterval) = oLifeCycleOwner.GetArgValue(sKey, (0, 0))
    return iInterval


def CommonGetRecycleWeaponNum(oTarget, oLifeCycle):
    oSuitElement = oTarget.m_Game.m_WarMgr.GetSeasonSuitElement()
    if not oSuitElement:
        return 0
    return oSuitElement.GetRecycleWeaponNum(oTarget.m_PlayerID)


def CommonoDisableTalent(oTarget, oLifeCycle):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.m_TalentCon.SwitchDisableTalent(0, sKey)

    sKey = oLifeCycle.Key()
    oTarget.m_TalentCon.SwitchDisableTalent(1, sKey)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonSetMaxExcessAttr(oTarget, oLifeCycle, iMaxVal):
    iMaxVal = cl_formula.GetResultByData(oTarget, iMaxVal, {
        'LifeCycle': oLifeCycle })
    oTarget.SetMaxExcessAttr(iMaxVal)


def CommonSettleAccountsSeasonSuit(oTarget, oLifeCycle, iSuit):
    oSuitElement = oTarget.m_Game.m_WarMgr.GetSeasonSuitElement()
    if not oSuitElement:
        return 0
    oSuitElement.SettleAccountsSeasonSuit(oTarget, iSuit)


def CommonClearRecordInfoList(oTarget, oLifeCycle, sKey):
    oLifeCycleOwner = oLifeCycle.GetObject()
    if not oLifeCycleOwner:
        return None
    oLifeCycleOwner.DelArgValue(sKey)


def CommonGetRecordInfoList(oTarget, oLifeCycle, sKey):
    oLifeCycleOwner = oLifeCycle.GetObject()
    if not oLifeCycleOwner:
        return []
    return oLifeCycleOwner.GetArgValue(sKey, [])


def CommonTriggerSeasonSuitPerformShow(oTarget, oLifeCycle, iSID):
    oSuitElement = oTarget.m_Game.m_WarMgr.GetSeasonSuitElement()
    if not oSuitElement:
        return None
    if not oSuitElement.GetSuitOpenStatus(oTarget, iSID):
        SendAlert('err', f'''{oTarget.m_Game} pid:{oTarget.m_PlayerID} {oLifeCycle.Key()} 传入套装SID：{iSID}是否正确''')
        return None
    oSuitElement.GS2CSeasonSuitPerformStart(iSID, oTarget.m_PlayerID)


def CommonGetSuitConditionSpillNumByTag(oTarget, oLifeCycle, iTag):
    oSuitElement = oTarget.m_Game.m_WarMgr.GetSeasonSuitElement()
    if not oSuitElement:
        return 0
    lstSuit = cl_platformdata.GetSeasonSuitByTag(iTag)
    iSpillNum = 0
    for iSuit in lstSuit:
        iSpillNum += oSuitElement.GetSuitConditionSpillNum(oTarget.m_ID, iSuit)
    
    return iSpillNum


def CommonChangeAIBaseDamageFactor(oTarget, oLifeCycle, iMul):
    
    def ClearFunc(oTarget, oLifeCycle):
        dAIBaseDamageFactor = oTarget.Query('AIBaseDamageFactor', { })
        dAIBaseDamageFactor.pop(sKey, 0)

    sKey = oLifeCycle.Key()
    dAIBaseDamageFactor = oTarget.SetDefault('AIBaseDamageFactor', { })
    if iMul:
        iMul = cl_formula.GetResultByData(oTarget, iMul, {
            'LifeCycle': oLifeCycle })
    dAIBaseDamageFactor[sKey] = iMul
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonChangePerformCDRate(oTarget, oLifeCycle, iPerformType, iAdd, iMul = 0):
    
    def ClearFunc(oTarget, oLifeCycle):
        oPerformCDRate.ClearValue(oTarget, sKey)

    sKey = oLifeCycle.m_Key
    oPerformCDRate = oTarget.m_PerformCDRate
    iAdd = cl_formula.GetResultByData(oTarget, iAdd, {
        'LifeCycle': oLifeCycle })
    if not iMul:
        iMul = 0
    else:
        iMul = cl_formula.GetResultByData(oTarget, iMul, {
            'LifeCycle': oLifeCycle })
    if sKey not in oPerformCDRate.m_Apply:
        oLifeCycle.AddDisableFunc(ClearFunc)
    for iCDType in ALL_PERFORMCDRATE_TYPE:
        if iCDType & iPerformType:
            oPerformCDRate.ModifyPerformCDRate(oTarget, iCDType, iAdd, iMul, sKey)
    


def CommonAddNeedSubCDPerform(oTarget, oLifeCycle, iPerform):
    
    def ClearFunc(oTarget, oLifeCycle):
        dSubCDPerform = oTarget.Query('SubCDPerform', { })
        dSubCDPerform.pop(tKey, 0)

    dSubCDPerform = oTarget.SetDefault('SubCDPerform', { })
    tKey = (iPerform, 0)
    dSubCDPerform[tKey] = 1
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonAddSelfNeedSubCDPerform(oTarget, oLifeCycle):
    
    def ClearFunc(oTarget, oLifeCycle):
        dSubCDPerform = oTarget.Query('SubCDPerform', { })
        dSubCDPerform.pop(tKey, 0)

    dSubCDPerform = oTarget.SetDefault('SubCDPerform', { })
    oPerform = oLifeCycle.GetObject()
    iPerform = oPerform.m_SID
    iItem = oPerform.m_Item if oPerform else 0
    tKey = (iPerform, iItem)
    dSubCDPerform[tKey] = 1
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonAddNeedSubCDState(oTarget, oLifeCycle, iStateSID):
    
    def ClearFunc(oTarget, oLifeCycle):
        dSubCDState = oTarget.Query('SubCDState', { })
        dSubCDState.pop(iStateSID, 0)

    dSubCDState = oTarget.SetDefault('SubCDState', { })
    dSubCDState[iStateSID] = 1
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonAddNeedSubCDActivePerform(oTarget, oLifeCycle, iPerform):
    
    def ClearFunc(oTarget, oLifeCycle):
        dSubCDActivePerform = oTarget.Query('CDActivePerform', { })
        dSubCDActivePerform.pop(iPerform, 0)

    dSubCDActivePerform = oTarget.SetDefault('CDActivePerform', { })
    dSubCDActivePerform[iPerform] = 1
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonAddPerformCDTimer(oTarget, oLifeCycle, iTime, iJustUpdateTimer = 0):
    
    def ClearFunc(oTarget, oLifeCycle):
        dPerformCDTimer = oTarget.Query('PerformCDTimer', { })
        (iPopFrame, _) = dPerformCDTimer.pop(sKey, (0, 0))
        if not iPopFrame or not oTarget.Find_Call_Out(sFlag):
            return None
        bIsDelTimer = True
        for _, iTmpJustUpdate in dPerformCDTimer.values():
            if not iTmpJustUpdate:
                bIsDelTimer = False
                break
        
        if bIsDelTimer:
            oTarget.Remove_Call_Out(sFlag)
        else:
            iUpdateFrame = oTarget.Query('UpdatePfFrame', 0)
            if iPopFrame < iUpdateFrame or not iUpdateFrame:
                iUpdateFrame = min((tUpdateTimer[0] for tUpdateTimer in dPerformCDTimer.values()))
                oTarget.Set('UpdatePfFrame', iUpdateFrame)

    sKey = oLifeCycle.Key()
    iFrame = Time2Frame(iTime)
    sFlag = 'PerformCDTimerKey'
    if iFrame < 3:
        SendAlert('err', '技能冷却定时器定时间隔过低 %s %d' % (oLifeCycle.Key(), iTime))
        iFrame = 3
    dPerformCDTimer = oTarget.SetDefault('PerformCDTimer', { })
    dPerformCDTimer[sKey] = (iFrame, iJustUpdateTimer)
    if oTarget.Find_Call_Out(sFlag):
        iMinDelay = oTarget.Query('UpdatePfFrame', 0)
        if iFrame < iMinDelay or not iMinDelay:
            oTarget.Set('UpdatePfFrame', iFrame)
        elif not iJustUpdateTimer:
            iMinDelay = min((tUpdateTimer[0] for tUpdateTimer in dPerformCDTimer.values()))
            oTarget.Set('UpdatePfFrame', iMinDelay)
            func = Functor(UpdatePerformCD, oTarget, iMinDelay, sFlag)
            oTarget.Call_Out(func, iMinDelay, sFlag)
    None.AddDisableFunc(ClearFunc)


def UpdatePerformCD(oTarget, iFrame, sFlag):
    oPerformCDRate = oTarget.m_PerformCDRate
    (iCareerCDRate, iPassiveCDRate, iShiftCDRate) = oPerformCDRate.GetAllPerformCDRate()
    iUpdateFrame = oTarget.Query('UpdatePfFrame', 12)
    if iCareerCDRate <= 0 and iPassiveCDRate <= 0 and iShiftCDRate <= 0:
        func = Functor(UpdatePerformCD, oTarget, iUpdateFrame, sFlag)
        oTarget.Call_Out(func, iUpdateFrame, sFlag)
        return None
    iCareerVal = int(iFrame * (iCareerCDRate / 10000))
    iPassivetVal = int(iFrame * (iPassiveCDRate / 10000))
    iShiftVal = int(iFrame * (iShiftCDRate / 10000))
    if iShiftVal:
        ModifyPerformColdTime(oTarget, [
            PF_SHIFT], iShiftVal)
    if iCareerVal:
        dHero2AllCareer = cl_hero.load.GetHero2HeroCareer()
        ModifyPerformColdTime(oTarget, dHero2AllCareer[oTarget.m_SID], iCareerVal)
    if iPassivetVal:
        dSubCDActivePerform = oTarget.Query('CDActivePerform', { })
        ModifyPerformColdTime(oTarget, dSubCDActivePerform, iPassivetVal)
        ModifySubCDPerformColdTime(oTarget, iPassivetVal, dExcludeiPerform = { })
        oStateCon = oTarget.m_State
        dSubCDState = oTarget.Query('SubCDState', { })
        for iState in dSubCDState:
            oState = oStateCon.GetItemBySID(iState)
            if not oState:
                continue
            cl_state.AddTime(oState, oTarget, -iPassivetVal, 300 * GAME_FRAME)
        
    func = Functor(UpdatePerformCD, oTarget, iUpdateFrame, sFlag)
    oTarget.Call_Out(func, iUpdateFrame, sFlag)


def ModifyPerformColdTime(oTarget, lstPerform, iVal):
    oPerformCon = oTarget.m_Perform
    for iPerform in lstPerform:
        oPerform = oTarget.GetPerform(iPerform)
        if not oPerform:
            continue
        iColdTimeFrame = oPerformCon.GetTotalColdTime(iPerform)
        if not iColdTimeFrame:
            continue
        oPerformCon.ModifyColdTime(iPerform, -iVal)
    


def ModifySubCDPerformColdTime(oTarget, iVal, dExcludeiPerform, iDelayFrame = 1):
    oPerformCon = oTarget.m_Perform
    dSubCDPerform = oTarget.Query('SubCDPerform', { })
    iCurFrame = oTarget.m_Game.GetFrameNum()
    for iPerform, iItem in dSubCDPerform:
        if (iPerform, iItem) in dExcludeiPerform:
            continue
        oPerform = oTarget.GetPerform(iPerform, iItem)
        if not oPerform:
            continue
        if oPerformCon.GetTotalColdTime(iPerform):
            oPerform.ModifyColdTime(oTarget, -iVal)
        oPerform.ModifyLiteCD(-iVal)
        idx = oPerform.m_ID * 10 + TYPE_PASSIVE_TIME_CYCLE
        dIdx2Frame = oTarget.m_PFPassTimeUnit.m_Idx2Frame
        if idx not in dIdx2Frame:
            continue
        iCallFrame = dIdx2Frame[idx]
        dWaitFrame = oTarget.m_PFPassTimeUnit.m_WaitFrame
        if iCallFrame not in dWaitFrame:
            continue
        dFrameInfo = dWaitFrame[iCallFrame]
        if idx not in dFrameInfo:
            continue
        dPassInfo = dFrameInfo[idx]
        iEnableFrame = iCallFrame - iVal
        iEnableFrame = max(iEnableFrame, iCurFrame + iDelayFrame)
        oPerform.DelPassTime(oTarget, TYPE_PASSIVE_TIME_CYCLE)
        oTarget.AddPFPassTime(idx, iEnableFrame - iCurFrame, dPassInfo)
    


def CommonDict2List(oTarget, oLifeCycle, dInfo, iTransformKey, iTransformValue):
    lstResult = []
    for key, value in dInfo.items():
        if iTransformKey:
            lstResult.append(key)
        if iTransformValue:
            lstResult.append(value)
    
    return lstResult


def CommonAddRoomChallengeCollectDataFromMonster(oTarget, oLifeCycle, sKey, iAdd):
    oGame = oTarget.m_Game
    tLineIdx = oTarget.m_LineIdx
    if not tLineIdx:
        return None
    oCtrlMgr = oGame.m_WarMgr.GetComponent('LevelCtrl')
    oChallenge = oCtrlMgr.m_RoomChallenge.GetChallenge(tLineIdx)
    if not oChallenge:
        return None
    if sKey not in oChallenge.m_CollectData:
        oChallenge.m_CollectData[sKey] = iAdd
    else:
        oChallenge.m_CollectData[sKey] += iAdd


def CommonEnableSeasonSuitDamSummary(oTarget, oLifeCycle, iSuit, dPerform):
    
    def ClearFunc(oTarget, oLifeCycle):
        oElement = oTarget.m_Game.m_WarMgr.GetSeasonSuitElement()
        if not oElement:
            return None
        oElement.DisableSuitDamSummary(iHero, iSuit)

    oElement = oTarget.m_Game.m_WarMgr.GetSeasonSuitElement()
    if not oElement:
        return None
    oSuit = oLifeCycle.GetObject()
    if not oSuit:
        return None
    iHero = oTarget.m_ID
    oElement.EnableSuitDamSummary(iHero, iSuit, dPerform)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonOpenTempRelicPlayType(oTarget, oLifeCycle, iGamePlayerType):
    oRelicCon = oTarget.m_RelicCon
    oRelicCon.OpenTempRelicPlayType(iGamePlayerType)


def CommonClearTempRelicPlayType(oTarget, oLifeCycle, iGamePlayerType):
    oRelicCon = oTarget.m_RelicCon
    oRelicCon.ClearTempRelicPlayType(iGamePlayerType)


def CommonAddLotteryRelicBackProb(oTarget, oLifeCycle, iProb):
    
    def ClearFunc(oTarget, oLifeCycle):
        dRelicBackFactor = oTarget.Query('LotteryRelicBackFactor', { })
        if iPerformSID in dRelicBackFactor:
            dRelicBackFactor.pop(iPerformSID)
            oTarget.Set('LotteryRelicBackFactor', dRelicBackFactor)

    dRelicBackFactor = oTarget.Query('LotteryRelicBackFactor', { })
    iProb = cl_formula.GetResultByData(oTarget, iProb, {
        'LifeCycle': oLifeCycle })
    if iProb <= 0:
        SendAlert('err', '%s秘卷返还概率异常' % oLifeCycle.Key())
        return None
    oPerform = oLifeCycle.GetObject()
    if not oPerform:
        return None
    iPerformSID = oPerform.m_SID
    dRelicBackFactor[iPerformSID] = iProb
    oTarget.Set('LotteryRelicBackFactor', dRelicBackFactor)
    oLifeCycle.AddUniqueDisableFunc('ClearLotteryRelicBackProb', ClearFunc, iCover = 0)


def CalMoveDis(oTarget, oLifeCycle, sKey, iMoveLimit, iFrame, iGroup, iMultiple):
    if not oLifeCycle.m_Owner:
        return None
    oLifeCycleOwner = oLifeCycle.GetObject()
    vNow = oTarget.GetPos()
    tLast = oLifeCycleOwner.SetArgValueDefault(sKey, (vNow, 0))
    (vLast, fLastDis) = tLast
    fNewDis = cl_math.CalDistance(vLast, vNow) + fLastDis
    oLifeCycleOwner.SetArgValue(sKey, (vNow, fNewDis % iMoveLimit))
    if fNewDis >= iMoveLimit:
        oEventCB = oLifeCycle.GetObject().m_EventCB
        dEvent = oLifeCycle.AttrCache()
        dEvent['LifeCycle'] = oLifeCycle
        if iMultiple:
            for _ in range(int(fNewDis // iMoveLimit)):
                oEventCB.CBFuncAction(oTarget, iGroup, dEvent, { })
            
        else:
            oEventCB.CBFuncAction(oTarget, iGroup, dEvent, { })
    oTarget.Call_Out(Functor(CalMoveDis, oTarget, oLifeCycle, sKey, iMoveLimit, iFrame, iGroup, iMultiple), iFrame, sKey)


def CBEnterScene(oLifeCycle, sKey, oTarget, dInfo):
    oLifeCycleOwner = oLifeCycle.GetObject()
    tLast = oLifeCycleOwner.GetArgValue(sKey, None)
    if not tLast:
        return None
    (_, fLastDis) = tLast
    oLifeCycleOwner.SetArgValue(sKey, (oTarget.GetPos(), fLastDis))


def CommonStartCalMoveDis(oTarget, oLifeCycle, iMoveLimit, iTime, iGroup, iMultiple):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.Delete(sKey)
        oTarget.Remove_Call_Out(sKey)
        cl_msgcenter.DoneEvent(oTarget, cl_msgcenter.MSG_WAR_ENTERSCENE, sKey)

    sKey = 'MoveDis' + oLifeCycle.Key()
    oTarget.Remove_Call_Out(sKey)
    oLifeCycleOwner = oLifeCycle.GetObject()
    oLifeCycleOwner.SetArgValue(sKey, (oTarget.GetPos(), 0))
    iFrame = Time2Frame(iTime)
    iMoveLimit = cl_formula.GetResultByData(oTarget, iMoveLimit, {
        'LifeCycle': oLifeCycle })
    oTarget.Call_Out(Functor(CalMoveDis, oTarget, oLifeCycle, sKey, iMoveLimit, iFrame, iGroup, iMultiple), iFrame, sKey)
    cl_msgcenter.AddFunction(oTarget, cl_msgcenter.MSG_WAR_ENTERSCENE, Functor(CBEnterScene, oLifeCycle, sKey), sKey, iOnce = 0)
    oLifeCycle.AddUniqueDisableFunc(sKey, ClearFunc, 0)


def CommonGetRandomResult(oTarget, oLifeCycle, iLimit, iRatio, iCount):
    dData = {
        'LifeCycle': oLifeCycle }
    iCount = cl_formula.GetResultByData(oTarget, iCount, dData)
    if iCount <= 0:
        SendAlert('err', '%s随机次数小于0' % oLifeCycle.Key())
        return 0
    iLimit = cl_formula.GetResultByData(oTarget, iLimit, dData)
    iRatio = cl_formula.GetResultByData(oTarget, iRatio, dData)
    iResult = 0
    for _ in range(iCount):
        if oTarget.m_Game.Random(iLimit) < iRatio:
            iResult += 1
    
    return iResult


def CommonGetHistoryWeapon(oTarget, oLifeCycle):
    lstAllWeapon = []
    lstResult = []
    lstAllWeapon.extend(oTarget.m_WieldCon.GetAllItem())
    oWeaponStoreElement = oTarget.m_Game.m_WarMgr.GetComponent('WeaponStoreElement')
    if not oWeaponStoreElement:
        return lstResult
    lstAllWeapon.extend(oTarget.m_ExWeaponCon.GetAllItem())
    lstAllWeapon.extend(oTarget.m_WeaponStoreCon.GetAllItem())
    for oWeapon in lstAllWeapon:
        if oWeapon and oWeapon.Query('HistoryInjectAnimaWeapon', 0):
            lstResult.append(oWeapon.m_ID)
    
    return lstResult


def OnMonsterSuperBefore(oTarget, dMsgInfo):
    if 'PlusPFEnable' in dMsgInfo:
        dMsgInfo['PlusPFEnable'] = 0
    if 'AfPFEnable' in dMsgInfo:
        dMsgInfo['AfPFEnable'] = 0


def CommonDisableMonsterSuper(oTarget, oLifeCycle):
    
    def ClearFunc(oTarget, oLifeCycle):
        cl_msgcenter.DoneEvent(oTarget, cl_msgcenter.MSG_WAR_MONSTER_SUPER_BEFORE, sKey)
        dSourceInfo.pop(sLifeCycleKey)
        tSuperInfo = oTarget.Query('MonsterSuper')
        if not tSuperInfo or dSourceInfo:
            return None
        (iPlusPF, iAfPF) = tSuperInfo
        oTarget.EnablePerform(iPlusPF, iNotify)
        oTarget.EnablePerform(iAfPF, iNotify)
        iPart = oTarget.m_Part
        if iPart:
            oGame = oTarget.m_Game
            oPart = oGame.GetObject(iPart)
            if oPart:
                oPart.EnablePerform(iPlusPF, iNotify)
                oPart.EnablePerform(iAfPF, iNotify)

    if not oTarget.m_FightType & WARRIOR_MONSTER:
        SendAlert('err', '%s通用使怪物强化失效只能作用在怪物身上' % oLifeCycle.GetStableKey())
        return None
    sLifeCycleKey = oLifeCycle.Key()
    dSourceInfo = oTarget.SetDefault('DisableMonsterSuper', { })
    if sLifeCycleKey in dSourceInfo:
        return None
    dSourceInfo[sLifeCycleKey] = 1
    tSuperInfo = oTarget.Query('MonsterSuper')
    iNotify = 1
    if tSuperInfo:
        (iPlusPF, iAfPF) = tSuperInfo
        oTarget.DisablePerform(iPlusPF, iNotify)
        oTarget.DisablePerform(iAfPF, iNotify)
        iPart = oTarget.m_Part
        if iPart:
            oGame = oTarget.m_Game
            oPart = oGame.GetObject(oTarget.m_Part)
            if oPart:
                oPart.DisablePerform(iPlusPF, iNotify)
                oPart.DisablePerform(iAfPF, iNotify)
    sKey = 'CommonDisableMonsterSuper' + sLifeCycleKey
    cl_msgcenter.AddFunction(oTarget, cl_msgcenter.MSG_WAR_MONSTER_SUPER_BEFORE, OnMonsterSuperBefore, sKey, iOnce = 0)
    oLifeCycle.AddUniqueDisableFunc(sKey, ClearFunc, iCover = 0)


def CommonDisableMonsterRelic(oTarget, oLifeCycle):
    
    def ClearFunc(oTarget, oLifeCycle):
        dSourceInfo.pop(sLifeCycleKey)
        if dSourceInfo:
            return None
        for iRelicSID in lstMonsterRelic:
            oRelicPF = oTarget.GetPerform(iRelicSID)
            if not oRelicPF:
                continue
            if oRelicPF.m_Quality == QUALITY_TYPE_CURSE:
                continue
            oRelicPF.Enable(oTarget, iNotify)
        

    if not oTarget.m_FightType & WARRIOR_MONSTER:
        SendAlert('err', '%s通用使怪物遗物失效只能作用在怪物身上' % oLifeCycle.GetStableKey())
        return None
    oMonsterRelicElement = oTarget.m_Game.m_WarMgr.GetComponent('MonsterRelicElement')
    if not oMonsterRelicElement:
        return None
    sLifeCycleKey = oLifeCycle.Key()
    dSourceInfo = oTarget.SetDefault('DisableMonsterRelic', { })
    if sLifeCycleKey in dSourceInfo:
        return None
    dSourceInfo[sLifeCycleKey] = 1
    iNotify = 1
    lstMonsterRelic = oMonsterRelicElement.GetMonsterRelic(oTarget.m_ID)
    for iRelicSID in lstMonsterRelic:
        oRelicPF = oTarget.GetPerform(iRelicSID)
        if not oRelicPF:
            continue
        if oRelicPF.m_Quality == QUALITY_TYPE_CURSE:
            continue
        oRelicPF.Disable(oTarget, iNotify)
    
    sKey = 'CommonDisableMonsterRelic' + sLifeCycleKey
    oLifeCycle.AddUniqueDisableFunc(sKey, ClearFunc, iCover = 0)


def PassiveCBSetPFArgsDict(oTarget, oLifeCycle, iPerform, sArgs, dInfo):
    pfobj = oTarget.GetPerform(iPerform)
    if not pfobj:
        return None
    pfobj.SetArgValue(sArgs, dInfo)


def CommonSetWandMaxCount(oTarget, oLifeCycle, iCount):
    oLifeCycleOwner = oLifeCycle.GetObject()
    oWand = oTarget.m_WandCon.GetWandByID(oLifeCycleOwner.m_Item)
    if not oWand:
        return None
    dData = {
        'LifeCycle': oLifeCycle }
    iCount = cl_formula.GetResultByData(oTarget, iCount, dData)
    oWand.SetWandMaxCount(iCount)


def CommonWandEnterCD(oTarget, oLifeCycle, iTime = 0):
    oLifeCycleOwner = oLifeCycle.GetObject()
    oWand = oLifeCycleOwner.GetMyItem()
    if not oWand:
        return None
    iTime = cl_formula.GetResultByData(oTarget, iTime, {
        'LifeCycle': oLifeCycle })
    if iTime < 0:
        return None
    oWand.EnterCD(iCDTime = iTime)


def CommonWandForbidCasting(oTarget, oLifeCycle, iForbid = 0):
    oLifeCycleOwner = oLifeCycle.GetObject()
    oWand = oLifeCycleOwner.GetMyItem()
    if not oWand:
        return None
    oWand.SetWandForbidCasting(iForbid)


def CommonTriggerNextPosActionComp(oTarget, oLifeCycle, iTimes):
    oLifeCycleOwner = oLifeCycle.GetObject()
    oWand = oLifeCycleOwner.GetMyItem()
    if not oWand:
        return None
    iNextPos = oLifeCycleOwner.GetCurPos() + 1
    if not oWand.CheckCompPos(iNextPos):
        return None
    oComp = oWand.GetCompByPos(WAND_COMP_TYPE_ACTION, iNextPos)
    if not oComp.CanTriggerByNextPos():
        return None
    iTimes = cl_formula.GetResultByData(oTarget, iTimes, {
        'LifeCycle': oLifeCycle })
    for _ in range(iTimes):
        oWand.TriggerPointPosActionComp(iNextPos)
    


def CommonKillMonsterSummon(oTarget, oLifeCycle):
    if not oTarget or not (oTarget.m_FightType & WARRIOR_MONSTER):
        return None
    iAttack = oTarget.m_ID
    sKey = oLifeCycle.Key()
    for iSummon in oTarget.m_MonsterSummon:
        if iSummon in oTarget.m_FollowDieObjs:
            oTarget.m_FollowDieObjs.pop(iSummon)
        oSummon = oTarget.m_Game.GetObject(iSummon, PY_FLAG_DEAD)
        if not oSummon:
            continue
        oReason = cl_object.reason.CStrReason(sKey, None, {
            'DamType': DAM_TYPE_SCENE | DAM_TYPE_TRUE | DAM_USE_HP })
        oSummon.HPDirectModify('HP', iAttack, -oSummon.HP(), oReason)
        if oSummon.m_Part and not oSummon.IsDead():
            oSummon.HPDirectModify('HP', iAttack, -oSummon.HP(), oReason)
    
    oTarget.m_MonsterSummon = { }


def CommonRemoveSourceItemTmpData(oTarget, oLifeCycle, sKey):
    oLifeCycleOwner = oLifeCycle.GetObject()
    oItem = oLifeCycleOwner.GetMyItem()
    if not oItem:
        return None
    oItem.RemoveTmp(sKey)


def CommonSetSourceItemTmpData(oTarget, oLifeCycle, sKey, iValue):
    oLifeCycleOwner = oLifeCycle.GetObject()
    oItem = oLifeCycleOwner.GetMyItem()
    if not oItem:
        return None
    iValue = cl_formula.GetResultByData(oTarget, iValue, {
        'LifeCycle': oLifeCycle })
    oItem.SetTmp(sKey, iValue)


def CommonSetWeaponBullet(oTarget, oLifeCycle, iWeaponID, iNum, iSendMsg, iAddBag):
    dData = {
        'LifeCycle': oLifeCycle }
    iWeaponID = cl_formula.GetResultByData(oTarget, iWeaponID, dData)
    oWeapon = oTarget.m_WieldCon.GetItemByID(iWeaponID)
    if not oWeapon:
        return None
    oBulletCom = oWeapon.GetComponent('Bullet')
    if not oBulletCom:
        return None
    iNum = cl_formula.GetResultByData(oTarget, iNum, dData)
    iChange = iNum - oBulletCom.Bullet()
    oBulletCom.BulletModify(iChange, iSendMsg = iSendMsg)
    if iAddBag and iChange < 0:
        sKey = oLifeCycle.Key()
        iBulletType = oBulletCom.BulletType()
        oTarget.m_BulletCon.BulletModify(iBulletType, -iChange, sKey)


def CommonSetAllWandExtActionCompNum(oTarget, oLifeCycle, iNum, iNotyfiy):
    
    def ClearFunc(oTarget, oLifeCycle):
        if not oTarget.m_OnGame:
            return None
        for oWand in oTarget.m_WandCon.m_Wand.values():
            oWand.DelExtActionComp(sKey, iNotyfiy)
        

    sKey = oLifeCycle.Key()
    for oWand in oTarget.m_WandCon.m_Wand.values():
        oWand.SetExtActionComp(sKey, iNum, iNotyfiy)
    
    oLifeCycle.AddUniqueDisableFunc(sKey, ClearFunc, iCover = 0)


def CommonWandCompFinishCondition(oTarget, oLifeCycle):
    oLifeCycleOwner = oLifeCycle.GetObject()
    oCurWand = oTarget.m_WandCon.GetCurWand()
    iComp = oLifeCycleOwner.m_Item
    if not oCurWand or not iComp:
        return None
    oWandComp = None
    for oTmpComp in oCurWand.m_Comp[WAND_COMP_TYPE_CONDITION].values():
        if oTmpComp.m_ID == iComp:
            oWandComp = oTmpComp
            break
    
    if not oWandComp:
        return None
    oWandComp.FinishCondition()


def CommonTriggerWandComp(oTarget, oLifeCycle, iWandCompPos):
    dData = {
        'LifeCycle': oLifeCycle }
    iWandCompPos = cl_formula.GetResultByData(oTarget, iWandCompPos, dData)
    if iWandCompPos < 0:
        return None
    oLifeCycleOwner = oLifeCycle.GetObject()
    oWand = oLifeCycleOwner.GetMyItem()
    if not oWand:
        return None
    oWand.TriggerPointPosActionComp(iWandCompPos)


def CommonReplaceWandShopWandCompWeight(oTarget, oLifeCycle, dCompWeight):
    if not dCompWeight:
        return None
    oTarget.Set('ReplaceWandShopWandCompWeight', dCompWeight)


def CommonSetWandShopCompQuality(oTarget, oLifeCycle, dInfo):
    if not dInfo:
        SendAlert('err', '%s参数异常 ' % oLifeCycle.Key())
        return None
    dChangeWandShopWandComp = { }
    for iIndex, iQuality in dInfo.items():
        dChangeWandShopWandComp[iIndex] = (iQuality, SHOP_ITEM_CHANGE_REASON_BENEDICTION)
    
    oTarget.Set('ChangeWandShopWandComp', dChangeWandShopWandComp)


def CommonAddPlantAttrMul(oTarget, oLifeCycle, sKey, iMul):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.Add(sKey, -iMul)

    oTarget.Add(sKey, iMul)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonGetQualityWandItemNum(oTarget, oLifeCycle, iQuality, iItemType):
    iResult = 0
    if iItemType == VIRTUAL_ITEM_WAND:
        dAllWand = oTarget.m_WandCon.GetAllWand()
        for oWand in dAllWand.values():
            if iQuality == oWand.GetWandQuality():
                iResult += 1
        
    elif iItemType == VIRTUAL_ITEM_WANDCOMP:
        dAllBagComp = oTarget.m_WandCon.GetAllBagComp()
        for _, dCompInfo in dAllBagComp.items():
            if iQuality in dCompInfo:
                iResult += dCompInfo[iQuality]
        
    return iResult


def CommonClearAllSeed(oTarget, oLifeCycle):
    if oTarget.m_SID != GARDENER_HERO:
        return None
    oTarget.m_GardenerCon.ClearAllSeed(oLifeCycle.Key())


def CommonClearAllPlant(oTarget, oLifeCycle):
    if oTarget.m_SID != GARDENER_HERO:
        return None
    oTarget.m_GardenerCon.ClearAllPlant(oLifeCycle.Key())


def CommonClearDomainBarrierSummon(oTarget, oLifeCycle):
    if oTarget.m_SID != GARDENER_HERO:
        return None
    oTarget.m_GardenerCon.ClearDomainBarrierSummon(iDelayRemove = 1)


def CommonAddMonsterBanAF(oTarget, oLifeCycle, dBanAF):
    lstBanPF = list(oTarget.m_BanPF)
    for iBanAF in dBanAF:
        if iBanAF not in lstBanPF:
            lstBanPF.append(iBanAF)
    
    oTarget.m_BanPF = tuple(lstBanPF)


def CommonSetMonsterAttrPlus(oTarget, oLifeCycle, dAttrPlus):
    oTarget.m_AttrPlusPF = tuple(dAttrPlus)


def CommonAddWandShopNpcRefreshTimes(oTarget, oLifeCycle, iTimes):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.Add('WandShopRefreshTimes', -iTimes)

    oTarget.Add('WandShopRefreshTimes', iTimes)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonAddDiceShopNpcEnergy(oTarget, oLifeCycle, iDefaultEnergy, iBossEnergy):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.Add('DiceShopNpcDefaultEnergy', -iDefaultEnergy)
        oTarget.Add('DiceShopNpcBossEnergy', -iBossEnergy)

    oTarget.Add('DiceShopNpcDefaultEnergy', iDefaultEnergy)
    oTarget.Add('DiceShopNpcBossEnergy', iBossEnergy)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonAddDiceShopNpcSpecialItem(oTarget, oLifeCycle, iSpecialItemID):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.Set('DiceShopNpcExtraSpecialItemID', 0)

    oTarget.Add('DiceShopNpcExtraSpecialItemID', iSpecialItemID)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonAddWandShopGoodsNum(oTarget, oLifeCycle, iItemType, iNum):
    dExtraGoodsNum = oTarget.Query('AddWandShopGoodsExtraGoodsNum', { })
    if iItemType in dExtraGoodsNum:
        dExtraGoodsNum[iItemType] += iNum
    else:
        dExtraGoodsNum[iItemType] = iNum
    oTarget.Set('AddWandShopGoodsExtraGoodsNum', dExtraGoodsNum)


def CommonAddWeaponAttrIgnoreLink(oTarget, oLifeCycle, sAttr, iFlag, iLimitTag):
    
    def ClearFunc(oTarget, oLifeCycle):
        for iWeapon in lstClear:
            oWeapon = oTarget.m_WieldCon.GetItemByID(iWeapon)
            if not oWeapon:
                continue
            oAttr = oWeapon.GetItemAttr(sAttr)
            if oAttr:
                oAttr.RemoveIgnoreLink(oWeapon, sKey)
        

    lstAdd = oTarget.m_WieldCon.GetWeapons(iFlag, iLimitTag)
    if not lstAdd:
        return None
    sKey = oLifeCycle.Key()
    for oWeapon in lstAdd:
        oAttr = oWeapon.GetItemAttr(sAttr)
        if oAttr:
            oAttr.AddIgnoreLink(oWeapon, sKey)
        oWeapon.m_LifeCycle.AddDisableFunc(ClearFunc)
    
    if lstAdd:
        lstClear = [ oWeapon.m_ID for oWeapon in lstAdd ]
        oLifeCycle.AddDisableFunc(ClearFunc)


def CommonAddMonterHateInfo(oTarget, oLifeCycle, iFightType):
    oGame = oTarget.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oTarget.m_Scene)
    if not oScene:
        return None
    iTarget = oTarget.m_ID
    iCurFrame = oGame.GetFrameNum()
    for iMonster in oScene.GetObjectsByType('Monster'):
        oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
        if not oMonster or oMonster.m_FightType & iFightType != iFightType:
            continue
        oAgent = oMonster.m_Agent
        if not oAgent:
            continue
        dHateData = oAgent.GetData('HateData', { })
        oNowTarget = oAgent.GetLockEnemy()
        if iTarget not in dHateData:
            dHateData[iTarget] = {
                'Dam': { },
                'Hate': [
                    0,
                    iCurFrame],
                'Immutable': 0 }
        if oNowTarget and oNowTarget.m_ID in dHateData and dHateData[oNowTarget.m_ID]['Hate'][0] <= 0:
            oAgent.SetLockEnemy(iTarget)
        oAgent.SetData('HateData', dHateData)
    


def CommonGetAttrExcludeTargetWandComp(oTarget, oLifeCycle, sAttr, dExcludeWandComp):
    oLifeCycleOwner = oLifeCycle.GetObject()
    oWand = oLifeCycleOwner.GetMyItem()
    if not oWand:
        return 0
    oAttr = oWand.GetItemAttr(sAttr)
    if not oAttr:
        return 0
    dWandCompInfo = oWand.m_Comp[WAND_COMP_TYPE_ACTION]
    lstExcludeKey = [
        oLifeCycle.Key()]
    for oWandComp in dWandCompInfo.values():
        if oWandComp.m_SID in dExcludeWandComp:
            lstExcludeKey.append(oWandComp.m_Key)
    
    return oAttr.GetExcludeValue(lstExcludeKey)


def CommonSetWandExtraCallTimeProb(oTarget, oLifeCycle, iProb):
    
    def ClearFunc(oTarget, oLifeCycle):
        oLifeCycleOwner = oLifeCycle.GetObject()
        oWand = oTarget.m_WandCon.GetWandByID(oLifeCycleOwner.m_Item)
        if not oWand:
            return None
        oWand.ClearExtraCallTimeProb(sKey)

    oLifeCycleOwner = oLifeCycle.GetObject()
    oWand = oLifeCycleOwner.GetMyItem()
    if not oWand:
        return None
    sKey = oLifeCycle.Key()
    iProb = cl_formula.GetResultByData(oTarget, iProb, {
        'LifeCycle': oLifeCycle })
    oWand.AddExtraCallTimeProb(iProb, sKey)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonSetWandPassiveLevel(oTarget, oLifeCycle, iLevel):
    
    def ClearFunc(oTarget, oLifeCycle):
        for iPerform in tInitPerform:
            oPerform = oTarget.GetPerform(iPerform)
            if not oPerform:
                continue
            if oPerform.m_PFType != PF_TYPE_PASSIVE:
                continue
            oPerform.ClearTempLevelLifeCycle(oTarget)
        

    oLifeCycleOwner = oLifeCycle.GetObject()
    oWand = oLifeCycleOwner.GetMyItem()
    if not oWand:
        return None
    tInitPerform = oWand.m_InitPerform
    if not tInitPerform:
        return None
    for iPerform in tInitPerform:
        oPerform = oTarget.GetPerform(iPerform)
        if oPerform.m_PFType != PF_TYPE_PASSIVE:
            continue
        oPerform.SetTempLevelLifeCycle(oTarget, iLevel)
    
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonSetWandPosFunc(oTarget, oLifeCycle, iPos, iFunc, iValue):
    
    def ClearWandPosInvalidProb(oTarget, oLifeCycle):
        oLifeCycleOwner = oLifeCycle.GetObject()
        oWand = oTarget.m_WandCon.GetWandByID(oLifeCycleOwner.m_Item)
        if not oWand:
            return None
        oWand.ClearWandPosFunc(iPos, iFunc, sKey)

    oLifeCycleOwner = oLifeCycle.GetObject()
    oWand = oTarget.m_WandCon.GetWandByID(oLifeCycleOwner.m_Item)
    if not oWand:
        return None
    dData = {
        'LifeCycle': oLifeCycle }
    iPos = cl_formula.GetResultByData(oTarget, iPos, dData)
    if iPos < 0:
        return None
    sKey = oLifeCycle.Key()
    iValue = cl_formula.GetResultByData(oTarget, iValue, dData)
    oLifeCycle.AddDisableFunc(ClearWandPosInvalidProb)
    oWand.SetWandPosFunc(iPos, iFunc, sKey, iValue)


def CommonChangeWandConditionCount(oTarget, oLifeCycle, iChangeRatio, iClearConditionCount):
    
    def ClearFunc(oTarget, oLifeCycle):
        oLifeCycleOwner = oLifeCycle.GetObject()
        oWand = oLifeCycleOwner.GetMyItem()
        if not oWand:
            return None
        dComp = oWand.m_Comp[WAND_COMP_TYPE_CONDITION]
        for oConditionComp in dComp.values():
            dChangeFactor = oConditionComp.GetKeepValue('ChangeFinishCountFactor', { })
            if sKey in dChangeFactor:
                dChangeFactor.pop(sKey, None)
                oConditionComp.SetKeepValue('ChangeFinishCountFactor', dChangeFactor)
                oConditionComp.m_ChangeFinishConditionCountFactor = sum(dChangeFactor.values())
                iBaseFinshCount = oConditionComp.GetKeepValue('BaseFinshCount', 0)
                if iBaseFinshCount:
                    oConditionComp.SetFinishConditionCount(iBaseFinshCount)
        

    oLifeCycleOwner = oLifeCycle.GetObject()
    oWand = oLifeCycleOwner.GetMyItem()
    if not oWand:
        return None
    dComp = oWand.m_Comp[WAND_COMP_TYPE_CONDITION]
    iChangeRatio = cl_formula.GetResultByData(oTarget, iChangeRatio, {
        'LifeCycle': oLifeCycle })
    sKey = oLifeCycle.Key()
    for oConditionComp in dComp.values():
        dChangeFactor = oConditionComp.GetKeepValue('ChangeFinishCountFactor', { })
        dChangeFactor[sKey] = iChangeRatio
        oConditionComp.m_ChangeFinishConditionCountFactor = sum(dChangeFactor.values())
        oConditionComp.SetKeepValue('ChangeFinishCountFactor', dChangeFactor)
        iBaseFinishCount = oConditionComp.GetKeepValue('BaseFinshCount', 0)
        if not iBaseFinishCount:
            iBaseFinishCount = oConditionComp.m_FinishConditionCount
        if iClearConditionCount:
            oConditionComp.m_ConditionCount = 0
        oConditionComp.SetFinishConditionCount(iBaseFinishCount)
    
    oLifeCycle.AddUniqueDisableFunc('ClearFinishCountFactor', ClearFunc, iCover = 0)


def CommonGetRarityWandCompNum(oTarget, oLifeCycle, iCompType, dRarity):
    if iCompType not in (WAND_COMP_TYPE_CONDITION, WAND_COMP_TYPE_ACTION):
        return 0
    oWandCon = oTarget.m_WandCon
    if not oWandCon:
        return 0
    oWand = oWandCon.GetCurWand()
    if not oWand:
        return 0
    iNum = 0
    for _, oComp in oWand.m_Comp[iCompType].items():
        if oComp.m_Level in dRarity:
            iNum += 1
    
    return iNum


def CommonSetItemCustomLimit(oTarget, oLifeCycle, sAttr, iMin, iMax):
    
    def ClearFunc(oTarget, oLifeCycle):
        oLifeCycleOwner = oLifeCycle.GetObject()
        oItem = oLifeCycleOwner.GetMyItem()
        if not oItem:
            return None
        oAttr = oItem.GetAttr(sAttr)
        if not oAttr:
            return None
        oAttr.RemoveCustomLimit(oItem)

    oLifeCycleOwner = oLifeCycle.GetObject()
    oItem = oLifeCycleOwner.GetMyItem()
    if not oItem:
        return None
    oAttr = oItem.GetAttr(sAttr)
    if not oAttr:
        return None
    oAttr.SetCustomLimit(oItem, (iMin, iMax))
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonSetAttrCustomLimit(oTarget, oLifeCycle, sAttr, iMin, iMax):
    
    def ClearFunc(oTarget, oLifeCycle):
        oAttr = oTarget.GetAttr(sAttr)
        if not oAttr:
            return None
        oAttr.RemoveCustomLimit(oTarget)

    oAttr = oTarget.GetAttr(sAttr)
    if not oAttr:
        return None
    oAttr.SetCustomLimit(oTarget, (iMin, iMax))
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonChangeStateMaxCount(oTarget, oLifeCycle, iStateSID, iAdd, iMul, iFromSelf, iFromSameItem):
    
    def ClearFunc(oTarget, oLifeCycle):
        oState = oTarget.m_State.GetStateBySource(iStateSID, iAttack, iItem)
        if oState:
            iBaseCount = oState.GetArgValue('BaseStateCount', 0)
            dMaxCountFactor = oState.SetArgValueDefault('StateMaxCountFactor', { })
            dMaxCountFactor.pop(sKey, None)
            iAddition = 0
            lstMul = []
            for iAdd, iMul in dMaxCountFactor.values():
                iAddition += iAdd
                lstMul.append(iMul)
            
            iMaxCount = iBaseCount + iAddition
            for iMul in lstMul:
                iMaxCount = iMaxCount * (10000 + iMul) // 10000
            
            oLifeCycleOwner = oLifeCycle.GetObject()
            if oLifeCycleOwner and oLifeCycleOwner.GetArgValue('ChangeLeveling', 0):
                oState.SetArgValue('RecordCount', oState.GetCount())
            oState.SetMaxCount(oTarget, iMaxCount)

    iAttack = oTarget.m_ID if iFromSelf else 0
    if iFromSameItem:
        dEventInfo = oLifeCycle.AttrCache()
        iItem = dEventInfo['ItemID']
    else:
        iItem = 0
    oState = oTarget.m_State.GetStateBySource(iStateSID, iAttack, iItem)
    if not oState:
        return None
    sKey = oLifeCycle.Key()
    iBaseCount = oState.GetArgValue('BaseStateCount', 0)
    if not iBaseCount:
        clsState = cl_state.GetStateClass(iStateSID)
        iBaseCount = clsState.m_MaxCount
        oState.SetArgValue('BaseStateCount', iBaseCount)
    dMaxCountFactor = oState.SetArgValueDefault('StateMaxCountFactor', { })
    iAdd = cl_formula.GetResultByData(oTarget, iAdd, {
        'LifeCycle': oLifeCycle })
    iMul = cl_formula.GetResultByData(oTarget, iMul, {
        'LifeCycle': oLifeCycle })
    dMaxCountFactor[sKey] = (iAdd, iMul)
    iAddition = 0
    lstMul = []
    for iAdd, iMul in dMaxCountFactor.values():
        iAddition += iAdd
        lstMul.append(iMul)
    
    iMaxCount = iBaseCount + iAddition
    for iMul in lstMul:
        iMaxCount = iMaxCount * (10000 + iMul) // 10000
    
    oState.SetMaxCount(oTarget, iMaxCount)
    oLifeCycleOwner = oLifeCycle.GetObject()
    if oLifeCycleOwner and oLifeCycleOwner.GetArgValue('ChangeLeveling', 0):
        iRecordCount = oState.GetArgValue('RecordCount', 0)
        iNowCount = oState.GetCount()
        if iRecordCount and iRecordCount > iNowCount:
            oState.AddCount(oTarget, iRecordCount - iNowCount)
        oState.SetArgValue('RecordCount', 0)
    oLifeCycle.AddUniqueDisableFunc('ClearStateMaxCount', ClearFunc, iCover = 1)


def CommonSetWeaponRepeatInfo(oListener, oLifeCycle, iFlag, iLimitTag, iRepeatCnt, iRepeatCold):
    
    def ClearFunc(oTarget, oLifeCycle):
        for iWeapon in lstWeapon:
            oWeapon = oListener.m_WieldCon.GetItemByID(iWeapon)
            if not oWeapon:
                continue
            oWeapon.RemoveRepeatInfo(sKey)
        

    lstAdd = oListener.m_WieldCon.GetWeapons(iFlag, iLimitTag)
    if not lstAdd:
        return None
    dInfo = {
        'LifeCycle': oLifeCycle }
    iRepeatCnt = cl_formula.GetResultByData(oListener, iRepeatCnt, dInfo)
    iRepeatCold = cl_formula.GetResultByData(oListener, iRepeatCold, dInfo)
    sKey = oLifeCycle.Key()
    lstWeapon = { }
    for oWeapon in lstAdd:
        oWeapon.SetRepeatInfo(sKey, iRepeatCnt, iRepeatCold)
        lstWeapon[oWeapon.m_ID] = 1
    
    oLifeCycle.AddDisableFunc(ClearFunc)


def GetSourceWand(oListener, oLifeCycle):
    oLifeCycleOwner = oLifeCycle.GetObject()
    oWandcon = oListener.m_WandCon
    oWand = oWandcon.GetWandByID(oLifeCycleOwner.m_Item)
    return oWand


def CommonFillWandEmptyActionCompSlot(oListener, oLifeCycle, iCompSID, iLevel, iSubType, dBlock, iMaxNum):
    
    def ClearFunc(oListener, oLifeCycle):
        oWand = GetSourceWand(oListener, oLifeCycle)
        if not oWand:
            return None
        oWand.RemoveCompByInitFlag(WAND_COMP_TYPE_ACTION, sKey, bSyncSameWand = False)
        oListener.m_WandCon.RefreshWand(oWand)

    oWand = GetSourceWand(oListener, oLifeCycle)
    if not oWand:
        return None
    dInfo = {
        'LifeCycle': oLifeCycle }
    iCompSID = cl_formula.GetResultByData(oListener, iCompSID, dInfo)
    if not iCompSID or iCompSID in dBlock:
        return None
    iLevel = cl_formula.GetResultByData(oListener, iLevel, dInfo)
    if not iLevel:
        return None
    sKey = oLifeCycle.Key()
    iNum = oWand.GetSubCompNum(WAND_COMP_TYPE_ACTION, WAND_SUBTYPE_COPY, sKey)
    iMaxNum = cl_formula.GetResultByData(oListener, iMaxNum, dInfo)
    iNeedNum = iMaxNum - iNum
    if iNeedNum <= 0:
        return None
    iNewNum = 0
    (_, iActionGroveNum) = oWand.GetWandGroveNum()
    for iPos in range(iActionGroveNum):
        if oWand.GetCompByPos(WAND_COMP_TYPE_ACTION, iPos) or not oWand.ValidAddComp(WAND_COMP_TYPE_ACTION, iPos, iCompSID, iLevel, iSubType):
            continue
        oWand.AddComp(WAND_COMP_TYPE_ACTION, iPos, iCompSID, iLevel, sKey, bSyncSameWand = False, iSubType = iSubType)
        iNewNum += 1
        if iNewNum >= iNeedNum:
            break
    
    oLifeCycle.AddUniqueDisableFunc(sKey, ClearFunc, iCover = 0)
    oListener.m_WandCon.RefreshWand(oWand)


def ClearWandEmptyActionCompSlot(oListener, oLifeCycle):
    oWand = GetSourceWand(oListener, oLifeCycle)
    if not oWand:
        return None
    oWand.RemoveCompByInitFlag(WAND_COMP_TYPE_ACTION, oLifeCycle.Key(), bSyncSameWand = False)
    oListener.m_WandCon.RefreshWand(oWand)


def CommonSetMinTriggerAllCompNum(oListener, oLifeCycle, iNum):
    
    def ClearFunc(oListener, oLifeCycle):
        oWand = GetSourceWand(oListener, oLifeCycle)
        if not oWand:
            return None
        oWand.ClearMinTriggerAllCompNum(sKey)

    oWand = GetSourceWand(oListener, oLifeCycle)
    if not oWand:
        return None
    sKey = oLifeCycle.Key()
    iNum = cl_formula.GetResultByData(oListener, iNum, {
        'LifeCycle': oLifeCycle })
    oWand.SetMinTriggerAllCompNum(sKey, iNum)
    oLifeCycle.AddUniqueDisableFunc(sKey, ClearFunc, iCover = 0)


def CommonChangeWandAttr(oListener, oLifeCycle, sAttr, iMul, iAdd):
    
    def ClearFunc(oListener, oLifeCycle):
        oWand = GetSourceWand(oListener, oLifeCycle)
        if not oWand:
            return None
        oWand.AttrClear(sAttr, sKey)

    oWand = GetSourceWand(oListener, oLifeCycle)
    if not oWand:
        return None
    sKey = oLifeCycle.Key()
    dData = {
        'LifeCycle': oLifeCycle }
    iMul = cl_formula.GetResultByData(oListener, iMul, dData)
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dData)
    if iMul or iAdd:
        oWand.AttrChange(sAttr, iMul, iAdd, sKey)
        oLifeCycle.AddUniqueDisableFunc(sKey + sAttr, ClearFunc, iCover = 0)
    else:
        oWand.AttrClear(sAttr, sKey)


def CommonSetWandExtActionCompNum(oListener, oLifeCycle, iNum, iNotyfiy):
    
    def ClearFunc(oTarget, oLifeCycle):
        if not oTarget.m_OnGame:
            return None
        oWand = GetSourceWand(oListener, oLifeCycle)
        if not oWand:
            return None
        oWand.DelExtActionComp(sKey, iNotyfiy)

    oWand = GetSourceWand(oListener, oLifeCycle)
    if not oWand:
        return None
    sKey = oLifeCycle.Key()
    iNum = cl_formula.GetResultByData(oListener, iNum, {
        'LifeCycle': oLifeCycle })
    oWand.SetExtActionComp(sKey, iNum, iNotyfiy)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonMonsterLockRoom(oTarget, oLifeCycle):
    
    def ClearFunc(oTarget, oLifeCycle):
        oGame = oTarget.m_Game
        if not oGame or oGame.m_ReleaseFlag:
            return None
        oWarMgr = oTarget.m_Game.GetWarMgr()
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.GetLevelNode(tLineIdx[0])
        if oLevelNode:
            oLevelNode.UnlockRoom(iRoomPos, sKey)

    if not oTarget.m_FightType & WARRIOR_MONSTER:
        return None
    oWarMgr = oTarget.m_Game.GetWarMgr()
    oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
    tLineIdx = oTarget.m_LineIdx
    oLine = oLevelCtrl.GetLineNode(tLineIdx)
    if not oLine:
        return None
    oLevelNode = oLine.m_LevelNode
    iRoomPos = oLine.m_IndexInLevel
    if not oLevelNode or oLevelNode.m_LevelType == LEVEL_TYPE_HIDE or iRoomPos != oLevelNode.m_CurRoomPos or oLevelNode.CheckLevelPass():
        return None
    sKey = '%s-m%d-%d' % (oLifeCycle.Key(), oTarget.m_SID, oTarget.m_ID)
    oLevelNode.LockRoom(iRoomPos, sKey)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonAddCareerPfTempUseTimes(oTarget, oLifeCycle, iAdd, iPriority, iCanOverLayNum, iClear):
    
    def ClearFunc(oTarget, oLifeCycle):
        oState = oTarget.m_State.GetItemBySID(CAREERPF_TEMPUSETIMES_STATE)
        if not oState:
            return None
        dTempUseTimes = oState.SetArgValueDefault('CareerPfTempUseTimes', { })
        if sKey in dTempUseTimes:
            oState.AddCount(oTarget, -dTempUseTimes[sKey][1])
            dTempUseTimes.pop(sKey)

    sKey = oLifeCycle.Key()
    oState = oTarget.m_State.GetItemBySID(CAREERPF_TEMPUSETIMES_STATE)
    if not oState:
        oState = cl_state.AddState(oTarget, CAREERPF_TEMPUSETIMES_STATE, STATE_TIME_FOREVER, 0, {
            'AID': oTarget.m_ID,
            'RS': cl_object.reason.CStrReason(sKey) })
        if oState:
            oState.Enable(oTarget)
        else:
            return None
    dTempUseTimes = oState.SetArgValueDefault('CareerPfTempUseTimes', { })
    iAdd = cl_formula.GetResultByData(oTarget, iAdd, {
        'LifeCycle': oLifeCycle })
    if iAdd <= 0:
        return None
    iOldAdd = 0
    if sKey in dTempUseTimes:
        (iOldPriority, iOldAdd) = dTempUseTimes[sKey]
        if iOldPriority != iPriority:
            SendAlert('err', '%s设置职业技能临时使用次数消耗优先级前后不一致' % sKey)
    if iOldAdd >= iCanOverLayNum:
        return None
    iTrueAdd = min(iAdd, iCanOverLayNum - iOldAdd)
    dTempUseTimes[sKey] = (iPriority, iOldAdd + iTrueAdd)
    oState.AddCount(oTarget, iTrueAdd)
    if iClear:
        oLifeCycle.AddUniqueDisableFunc(sKey, ClearFunc, iCover = 0)


def CommonClearOnePlant(oTarget, oLifeCycle):
    if not oTarget.m_GardenerCon:
        return None
    oTarget.m_GardenerCon.ClearOnePlant(oLifeCycle.Key())


def CommonSetPlantCanTransferState(oTarget, oLifeCycle, dState):
    if oTarget.m_FightType & WARRIOR_PLANT != WARRIOR_PLANT:
        return None
    oTarget.SetCanTransferState(dState)


def CommonCopyAssembleEffect(oTarget, oLifeCycle, dExclude, iCopyNum, iLast):
    
    def ClearFunc(oTarget, oLifeCycle):
        oDiceCon = oTarget.m_DiceCon
        if not oDiceCon:
            return None
        oDiceAbility = oDiceCon.GetPerform(iAbilitySID, iItem)
        if not oDiceAbility:
            return None
        oDiceCon.DisableCopyDiceAbility(oDiceAbility.m_Item)

    if not iCopyNum:
        return None
    oDiceCon = oTarget.m_DiceCon
    if not oDiceCon:
        return None
    oLifeCycleOwner = oLifeCycle.GetObject()
    oDice = oLifeCycleOwner.GetMyItem()
    if not oDice:
        return None
    iAbilitySID = oDice.m_SID
    iItem = oDice.m_ID
    oDiceAbility = oDiceCon.GetPerform(iAbilitySID, iItem)
    if not oDiceAbility:
        return None
    oDiceCon.EnableCopyDiceAbility(oDiceAbility, dExclude, iCopyNum, iLast)
    sKey = oLifeCycle.Key()
    oLifeCycle.AddUniqueDisableFunc(sKey, ClearFunc, iCover = 0)


def CommonResetWandConditionComp(oTarget, oLifeCycle):
    oLifeCycleOwner = oLifeCycle.GetObject()
    oWand = oTarget.m_WandCon.GetWandByID(oLifeCycleOwner.m_Item)
    if not oWand:
        return None
    oWand.ResetConditionComp()
    oWand.WandCastingConditionsRefresh()


def CommonHatchTargetSeed(oTarget, oLifeCycle, iSeed, iPlantPhase = PLANT_PHASE_NORMAL):
    if oTarget.m_SID != GARDENER_HERO:
        return None
    iSeed = cl_formula.GetResultByData(oTarget, iSeed, {
        'LifeCycle': oLifeCycle })
    oTarget.m_GardenerCon.HatchSeed(iSeed, oLifeCycle.Key(), iPlantPhase)


def CommonChangeWeaponAttPerformAttr(oTarget, oLifeCycle, sAttr, iAdd, iMul, iFlag):
    lstWeapon = oTarget.m_WieldCon.GetWeapons(iFlag)
    sKey = oLifeCycle.Key()
    dData = {
        'LifeCycle': oLifeCycle }
    iMul = cl_formula.GetResultByData(oTarget, iMul, dData)
    iAdd = cl_formula.GetResultByData(oTarget, iAdd, dData)
    for oWeapon in lstWeapon:
        oPerformCom = oWeapon.GetComponent('Perform')
        if not oPerformCom:
            continue
        lstPerform = oPerformCom.GetPerformSIDByType(PF_TYPE_ATTACK)
        for iPerform in lstPerform:
            oPerform = oPerformCom.GetPerform(iPerform)
            if sAttr not in oPerform.m_Attr:
                continue
            oLifeCycle.m_PerformApply[(oPerform.m_Item, iPerform, sAttr)] = 1
            oPerform.AttrChange(sAttr, sKey, iMul, iAdd)
        
    


def CommonSetReceiveDebuff(oTarget, oLifeCycle, iAdd, iMul):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.m_EleAbnormal.ClearReceiveDebuff(sKey)

    dData = {
        'LifeCycle': oLifeCycle }
    iAdd = cl_formula.GetResultByData(oTarget, iAdd, dData)
    iMul = cl_formula.GetResultByData(oTarget, iMul, dData)
    sKey = oLifeCycle.Key()
    oTarget.m_EleAbnormal.SetReceiveDebuff(iAdd, iMul, sKey)
    oLifeCycle.AddUniqueDisableFunc('ClearReceiveDebuff', ClearFunc, iCover = 0)


def CommonChangeWeaponPFBulletPerfomrAttrByHold(oTarget, oLifeCycle, iHoldType, sAttr, iAdd, iMul):
    lstWeapon = oTarget.m_WieldCon.GetWeapons(iHoldType)
    if not lstWeapon:
        return None
    dData = {
        'LifeCycle': oLifeCycle }
    if iMul:
        iMul = cl_formula.GetResultByData(oTarget, iMul, dData)
    if iAdd:
        iAdd = cl_formula.GetResultByData(oTarget, iAdd, dData)
    for oWeapon in lstWeapon:
        oPerform = oWeapon.GetPFBulletPerform()
        if not oPerform or sAttr not in oPerform.m_Attr:
            continue
        sKey = oLifeCycle.Key()
        oPerform.AttrChange(sAttr, sKey, iMul, iAdd)
        oLifeCycle.m_PerformApply[(oPerform.m_Item, oPerform.m_SID, sAttr)] = 1
    


def CommonSetDiceAnchoringPoint(oTarget, oLifeCycle, iPoint):
    if not oTarget.m_DiceCon:
        return None
    iPoint = cl_formula.GetResultByData(oTarget, iPoint, {
        'LifeCycle': oLifeCycle })
    oTarget.m_DiceCon.SetAnchoringPoint(iPoint)


def CommonSetDiceAttackTimes(oTarget, oLifeCycle, iTimes):
    
    def ClearFunc(oTarget, oLifeCycle):
        oLifeCycleOwner = oLifeCycle.GetObject()
        oDice = oLifeCycleOwner.GetMyItem()
        if not oDice:
            return None
        oDice.ClearDiceAttackTimes()

    if not oTarget.m_DiceCon:
        return None
    iTimes = cl_formula.GetResultByData(oTarget, iTimes, {
        'LifeCycle': oLifeCycle })
    oLifeCycleOwner = oLifeCycle.GetObject()
    oDice = oLifeCycleOwner.GetMyItem()
    if not oDice:
        return None
    oDice.SetDiceAttackTimes(iTimes)
    oLifeCycle.AddUniqueDisableFunc('SetDiceAttackTimes', ClearFunc, iCover = 0)


def CommonSetShape(oTarget, oLifeCycle, iShape, iClear):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.m_Shape = iOldShape
        oTarget.GS2CPropChange('Shape')

    iOldShape = oTarget.m_Shape
    if iOldShape == iShape:
        return None
    oTarget.m_Shape = iShape
    oTarget.GS2CPropChange('Shape')
    if iClear:
        oLifeCycle.AddUniqueDisableFunc('CommonSetShape', ClearFunc, iCover = 0)


def CommonChangeSelfDefPathMode(oTarget, oLifeCycle, iPathMode):
    
    def ClearFunc(oTarget, oLifeCycle):
        if not oTarget.m_MoveCtrl:
            return None
        oTarget.m_MoveCtrl.m_DefPathMode = iDefPathMode

    if not oTarget.m_MoveCtrl:
        return None
    iDefPathMode = oTarget.m_MoveCtrl.m_DefPathMode
    oTarget.m_MoveCtrl.m_DefPathMode = iPathMode
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonRandomGetFieldSeed(oTarget, oLifeCycle):
    if oTarget.m_SID != GARDENER_HERO:
        return 0
    dFieldSeedInfo = oTarget.m_GardenerCon.GetFieldSeedInfo()
    if not dFieldSeedInfo:
        return 0
    return ChooseKey(oTarget.m_Game, dFieldSeedInfo)


def CommonSetSourceWeaponPFBulletPerfomrForceAttr(oTarget, oLifeCycle, sAttr, iValue):
    
    def ClearFunc(oTarget, oLifeCycle):
        oWeapon = oLifeCycle.GetObject()
        if not oWeapon:
            return None
        oPerform = oWeapon.GetPFBulletPerform()
        if not oPerform or sAttr not in oPerform.m_Attr:
            return None
        oPerform.AttrForceClear(sAttr, sKey)

    oWeapon = oLifeCycle.GetOwnerSourceWeapon()
    if not oWeapon:
        return None
    oPerform = oWeapon.GetPFBulletPerform()
    if not oPerform or sAttr not in oPerform.m_Attr:
        return None
    dData = {
        'LifeCycle': oLifeCycle }
    iValue = cl_formula.GetResultByData(oTarget, iValue, dData)
    sKey = oLifeCycle.Key()
    oLifeCycle.m_PerformApply[(oPerform.m_Item, oPerform.m_SID, sAttr)] = 1
    oPerform.AttrForceSet(sAttr, iValue, sKey)
    if oWeapon.m_LifeCycle:
        oWeapon.m_LifeCycle.AddUniqueDisableFunc('ClearPerformForceAttr-%s' % sKey, ClearFunc, iCover = 0)


def CommonClearSourceWeaponPFBulletPerfomrForceAttr(oTarget, oLifeCycle, sAttr):
    oWeapon = oLifeCycle.GetOwnerSourceWeapon()
    if not oWeapon:
        return None
    oPerform = oWeapon.GetPFBulletPerform()
    if not oPerform or sAttr not in oPerform.m_Attr:
        return None
    sKey = oLifeCycle.Key()
    oPerform.AttrForceClear(sAttr, sKey)


def CommonSwitchAttPerform(oTarget, oLifeCycle, iPerform):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.m_AttPerform = iCurAttPerform

    oPerform = oTarget.GetPerform(iPerform)
    if not oPerform:
        return None
    iCurAttPerform = oTarget.m_AttPerform
    oTarget.m_AttPerform = iPerform
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonChangeDiceEnergy(oTarget, oLifeCycle, iValue, sReason):
    if not oTarget.m_FightType & WARRIOR_HERO:
        return None
    if not oTarget.m_DiceCon:
        return None
    dData = {
        'LifeCycle': oLifeCycle }
    iValue = cl_formula.GetResultByData(oTarget, iValue, dData)
    oTarget.m_DiceCon.ChangeDiceEnergy(iValue, sReason)


def CommonPlantSetPhase(oTarget, oLifeCycle, iPhase):
    if oTarget.m_FightType & WARRIOR_PLANT != WARRIOR_PLANT:
        return None
    oHero = oTarget.GetOwner()
    if not oHero or oHero.m_SID != GARDENER_HERO:
        return None
    oHero.m_GardenerCon.SetPlantPhase(oTarget.m_ID, iPhase)


def CommonAddChargeEnergyRate(oTarget, oLifeCycle, iMul):
    
    def ClearAddChargeEnergyRate(oTarget, oLifeCycle):
        oDiceCon = oTarget.m_DiceCon
        if not oDiceCon:
            return None
        oDiceCon.AddChargeEnergyMul(-iMul)

    oDiceCon = oTarget.m_DiceCon
    if not oDiceCon:
        return None
    iMul = cl_formula.GetResultByData(oTarget, iMul, {
        'LifeCycle': oLifeCycle })
    oDiceCon.AddChargeEnergyMul(iMul)
    oLifeCycle.AddDisableFunc(ClearAddChargeEnergyRate)


def CommonAddWarSeasonSonTaskValueByCarrySpecialItem(oTarget, oLifeCycle, iTaskType, iItemType, iAdd, iAddType):
    oDiceCon = oTarget.m_DiceCon
    if not oDiceCon:
        return None
    dSpecialItemInfo = oDiceCon.GetSpecialItemInfo()
    if not dSpecialItemInfo:
        return None
    oSeasonTask = oLifeCycle.GetObject()
    if not oSeasonTask or iTaskType not in oSeasonTask.m_SubTaskInfo:
        return None
    lstItem = cl_platformdata.GetDiceSpecialTypeList(iItemType)
    oSeasonTaskMgr = oTarget.m_SeasonTaskMgr
    for iSpecialItem in dSpecialItemInfo.values():
        if iSpecialItem in lstItem or iSpecialItem not in oSeasonTask.m_SubTaskInfo[iTaskType]:
            continue
        oSeasonTaskMgr.AddTaskVauleBySubTask(oSeasonTask, iTaskType, iSpecialItem, iAdd, iAddType)
    


def CommonSetAgentInfo(oTarget, oLifeCycle, sKey, iValues):
    oAgent = oTarget.m_Agent
    if not oAgent:
        return None
    oAgent.SetData(sKey, iValues)


def CommonHaltDicePointPerform(oTarget, oLifeCycle, iPerform):
    oLifeCycleOwner = oLifeCycle.GetObject()
    if not oLifeCycleOwner:
        return None
    oDice = oLifeCycleOwner.GetMyItem()
    if not oDice:
        return None
    iDice = oDice.m_ID
    for iActNum, dCasting in oTarget.GetAllCasting():
        if dCasting['pfid'] == iPerform:
            oSkill = oTarget.m_Game.m_SkillMgr.GetSkill(oTarget.m_ID, iActNum)
            if not oSkill or iDice != oSkill.m_Custom.get('DiceID', 0):
                continue
            HaltCasting(oTarget, iActNum, oLifeCycle.Key())
    


def CommonAddWeaponPFBulletByHoldType(oTarget, oLifeCycle, iHoldType, iAdd, iPercent):
    if not oTarget.m_FightType & WARRIOR_HERO:
        return None
    lstWeapon = oTarget.m_WieldCon.GetWeapons(iHoldType)
    for oWeapon in lstWeapon:
        oPerform = oWeapon.GetPFBulletPerform()
        if oPerform:
            iAddCount = 0
            if iAdd:
                iAddCount += cl_formula.GetResultByData(oTarget, iAdd, {
                    'LifeCycle': oLifeCycle })
            if iPercent:
                iAddCount += oPerform.MaxPFBullet() * iPercent // 100
            oPerform.AddPFBullet(iAddCount)
    


def CommonChangeMaxAssemblyNum(oTarget, oLifeCycle, iVal):
    oDiceCon = oTarget.m_DiceCon
    if not oDiceCon:
        return None
    iVal = cl_formula.GetResultByData(oTarget, iVal, {
        'LifeCycle': oLifeCycle })
    oTarget.m_DiceCon.AddMaxAssemblyNum(iVal)


def CommonAddSpecItemTriggerEnergyRatio(oTarget, oLifeCycle, iMul):
    
    def ClearFunc(oTarget, oLifeCycle):
        oDiceCon = oTarget.m_DiceCon
        if not oDiceCon:
            return None
        oDiceCon.AddSpecItemTriggerEnergyRatio(-iMul)

    oDiceCon = oTarget.m_DiceCon
    if not oDiceCon:
        return None
    iMul = cl_formula.GetResultByData(oTarget, iMul, {
        'LifeCycle': oLifeCycle })
    oDiceCon.AddSpecItemTriggerEnergyRatio(iMul)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonMonsterSwitch(oTarget, oLifeCycle, iTargetSID, dIgnorePF = None, sTargetBetree = '', dExtraPF = None):
    
    def ClearMonsterSwitch(oTarget, oLifeCycle):
        clsOwnMonster = oTarget.m_Game.m_WarData.GetMonsterData(oTarget.m_SID)
        if not clsOwnMonster:
            return None
        oAgent = oTarget.m_Agent
        if not oAgent:
            return None
        oTarget.m_Shape = clsOwnMonster.m_Shape
        for iDisablePF in dEnablePF:
            oTarget.RemovePerform(iDisablePF)
        
        oTarget.m_AttPerform = clsOwnMonster.m_AttPerform
        oTarget.m_PerformList = clsOwnMonster.m_PerformList
        if bSwitchBeTree:
            oAgent.RemoveSwitchCurrentBT(SWITCH_TREE_MONSTERCHANGE, sKey)
        dOwnAIConfig = clsOwnMonster.m_AIConfig
        if tKey in dOwnAIConfig:
            dOwnConfig = dOwnAIConfig[tKey]
            ChangeTargetPFAI(oTarget, oAgent, dOwnConfig)
        oTarget.OnGoto()

    if not iTargetSID or not (oTarget.m_FightType & MONSTER_TYPE_MASK):
        return None
    oGame = oTarget.m_Game
    iScene = oTarget.m_Scene
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return None
    oAgent = oTarget.m_Agent
    if not oAgent:
        return None
    clsMonster = oGame.m_WarData.GetMonsterData(iTargetSID)
    if not clsMonster:
        return None
    oTarget.m_Shape = clsMonster.m_Shape
    dEnablePF = { }
    iTargetAttPerform = clsMonster.m_AttPerform
    oTargetAttPerform = oTarget.AddPerform(iTargetAttPerform, 1)
    if not oTargetAttPerform:
        return None
    dEnablePF[iTargetAttPerform] = 1
    oTarget.m_AttPerform = iTargetAttPerform
    oTarget.m_PerformList = clsMonster.m_PerformList
    for iPerform in oTarget.m_PerformList:
        if dIgnorePF and iPerform in dIgnorePF:
            continue
        oPerform = oTarget.AddPerform(iPerform, 1)
        if not oPerform:
            continue
        dEnablePF[iPerform] = 1
    
    for iExtraPF in dExtraPF:
        oExtraPerform = oTarget.AddPerform(iExtraPF, 1)
        if not oExtraPerform:
            continue
        dEnablePF[iExtraPF] = 1
    
    bSwitchBeTree = False
    if sTargetBetree:
        sKey = oLifeCycle.Key()
        if oAgent.AddSwitchCurrentBT(SWITCH_TREE_MONSTERCHANGE, sTargetBetree, sKey):
            bSwitchBeTree = True
    dTargetAIConfig = clsMonster.m_AIConfig
    oWarMgr = oGame.m_WarMgr
    iTeam = 0 if oWarMgr.IsSingleGame() else 1
    iRound = oWarMgr.m_Round
    tKey = (iTeam, iRound)
    if tKey in dTargetAIConfig:
        dTargetConfig = dTargetAIConfig[tKey]
        ChangeTargetPFAI(oTarget, oAgent, dTargetConfig)
    oTarget.OnGoto()
    oLifeCycle.AddDisableFunc(ClearMonsterSwitch)


def ChangeTargetPFAI(oTarget, oAgent, dConfig):
    if oAgent.m_PFAI:
        oAgent.m_PFAI.Release()
    oAgent.m_PFAI = cl_betree.pfai.NewPFAI(dConfig['PFAI'], oTarget)
    oAgent.m_Config.update(dConfig)


def CommonReplaceFundamentalLevelFormula(oTarget, oLifeCycle, iFormula):
    
    def ClearFunc(oTarget, oLifeCycle):
        oWeapon = oTarget.m_WieldCon.GetItemByID(iWeapon)
        if not oWeapon:
            return None
        oWeapon.RestoreGradeFormula(oTarget)

    oWeapon = oTarget.m_WieldCon.GetItemByType(itemdef.EQUIP_TYPE_FUNDAMENTALWEAPON)
    if not oWeapon:
        return None
    if oWeapon.QueryTmp('ReplaceLevelFormula'):
        SendAlert('err', '熔炉等级公式重复替换%s' % oLifeCycle.Key())
        return None
    oWeapon.ChangeGradeFormula(oTarget, iFormula)
    iWeapon = oWeapon.m_ID
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonAddFundamentalInscription(oTarget, oLifeCycle, dInscription, iInscriptionNum):
    
    def ClearFunc(oTarget, oLifeCycle):
        oWeapon = oTarget.m_WieldCon.GetItemByID(iWeapon)
        if not oWeapon:
            return None
        oInscriptionCom = oWeapon.GetComponent('Inscription')
        if not oInscriptionCom:
            return None
        for iSID in lstAddInscription:
            oInscriptionCom.RemoveInscription(iSID)
        
        oWeapon.GS2CItemPropChange('Inscription', oInscriptionCom.GetAllInscription())
        lstSealedInscription = oInscriptionCom.GetSealedInscription()
        if lstSealedInscription and lstSealedInscription != [
            0,
            0,
            0]:
            oWeapon.Set('TempSealedInscription', oInscriptionCom.GetSealedInscription())
            oTalent = oTarget.m_TalentCon.GetPerform(SEALED_TALENT)
            if oTalent and oTarget.Query('SealedInscriptionEnable', 0):
                oInscriptionCom.DisableSealedInscription(iNowSealedInscriptionLv)
        oWeapon.RemoveComponent('Inscription')

    oWeapon = oTarget.m_WieldCon.GetItemByType(itemdef.EQUIP_TYPE_FUNDAMENTALWEAPON)
    if not oWeapon:
        return None
    oInscriptionCom = oWeapon.GetComponent('Inscription')
    if not oInscriptionCom:
        oWeapon.SetTmp('NotInitInscription', 1)
        oInscriptionCom = oWeapon.AddComponent('Inscription', { })
        if not oInscriptionCom:
            return None
        lstTempSealedInscription = oWeapon.Query('TempSealedInscription', [])
        if lstTempSealedInscription and lstTempSealedInscription != [
            0,
            0,
            0]:
            oInscriptionCom.m_SealedInscription = lstTempSealedInscription
            oWeapon.GS2CItemPropChange('SealedInscription', lstTempSealedInscription)
        oTalent = oTarget.m_TalentCon.GetPerform(SEALED_TALENT)
        iNowSealedInscriptionLv = oTalent.m_Level if oTalent else 0
        if iNowSealedInscriptionLv:
            if oTarget.Query('SealedInscriptionEnable', 0):
                oInscriptionCom.EnableSealedInscription(iNowSealedInscriptionLv)
            else:
                oInscriptionCom.DisableSealedInscription(iNowSealedInscriptionLv)
    lstFundamentalInscription = list(oWeapon.Query('FundamentalInscription', []))
    iAddInscriptionNum = iInscriptionNum - len(lstFundamentalInscription)
    if iAddInscriptionNum > 0:
        lstInscription = list(set(dInscription) - set(oInscriptionCom.m_Inscription) - set(lstFundamentalInscription))
        if lstInscription:
            lstNewInscription = ShufferList(oTarget.m_Game, lstInscription, iAddInscriptionNum)
            lstFundamentalInscription.extend(lstNewInscription)
            oWeapon.Set('FundamentalInscription', lstFundamentalInscription)
        elif iAddInscriptionNum < 0:
            lstFundamentalInscription = lstFundamentalInscription[:iInscriptionNum]
    lstAddInscription = oTalent.m_Level(set(lstFundamentalInscription) - set(oInscriptionCom.m_Inscription))
    if not lstAddInscription:
        return None
    for iInscription in lstAddInscription:
        oInscriptionCom.AppendInscription(iInscription)
    
    oWeapon.GS2CItemPropChange('Inscription', oInscriptionCom.GetAllInscription())
    iWeapon = oWeapon.m_ID
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonListenMsgCallBackFromOwnByAttr(oTarget, oLifeCycle, sAttr, iGroup, iObjectType):
    
    def ClearFunc(oTarget, oLifeCycle):
        cl_msgcenter.DoneAttention(oTarget, oWarrior.m_ID, cl_msgcenter.MSG_WAR_ATTR_CHANGE, sKey, iSub)

    oWarrior = oTarget.GetOwnObject(iObjectType)
    if not oWarrior:
        return None
    iSub = BASIC_PROP_NAME[sAttr][0]
    dEvent = oLifeCycle.AttrCache()
    dEvent['LifeCycle'] = oLifeCycle
    sKey = oLifeCycle.Key()
    oWarrior.AddRefreshAttr(sAttr)
    func = Functor(CommonAttentionCBFunc, oLifeCycle.GetObject().m_EventCB, iGroup, dEvent)
    cl_msgcenter.AddAttentionFunc(oTarget, oWarrior.m_ID, cl_msgcenter.MSG_WAR_ATTR_CHANGE, func, sKey, iSub)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonAddSeasonShopNpcRefreshTimes(oTarget, oLifeCycle, iTimes, sRefreshKey):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.Add(sRefreshKey, -iTimes)

    if not sRefreshKey:
        sRefreshKey = 'SeasonShopRefreshTimes'
    oTarget.Add(sRefreshKey, iTimes)
    oLifeCycle.AddDisableFunc(ClearFunc)


def CommonChangePerformAttrFromOwn(oTarget, oLifeCycle, iPerform, sAttr, iAdd, iRatio, iObjectType, iAddPerformInKey = 0):
    
    def ClearFunc(oTarget, oLifeCycle):
        oWarrior = oTarget.GetOwnObject(iObjectType)
        if not oWarrior:
            return None
        oPerform = oWarrior.GetPerform(iPerform)
        if not oPerform:
            return None
        oPerform.AttrClear(sAttr, sKey, iRefresh = 1)

    oWarrior = oTarget.GetOwnObject(iObjectType)
    if not oWarrior:
        return None
    oPerform = oWarrior.GetPerform(iPerform)
    if not oPerform:
        return None
    sKey = oLifeCycle.Key()
    dData = {
        'LifeCycle': oLifeCycle }
    if iAdd:
        iAdd = cl_formula.GetResultByData(oTarget, iAdd, dData)
        iAdd = cl_object.AttrUnitConversion(sAttr, iAdd)
    if iRatio:
        iRatio = cl_formula.GetResultByData(oTarget, iRatio, dData)
    oPerform.AttrChange(sAttr, sKey, iRatio, iAdd)
    if iAddPerformInKey:
        sUniqueKey = 'ChangePerformAttrFromOwn-%s-%s-%s' % (sKey, sAttr, iPerform)
    else:
        sUniqueKey = 'ChangePerformAttrFromOwn-%s-%s' % (sKey, sAttr)
    oLifeCycle.AddUniqueDisableFunc(sUniqueKey, ClearFunc, iCover = 1)


def CommonRewardS7Crystal(oTarget, oLifeCycle, iBeneMark, dCrystal, iRewardTimes):
    if iRewardTimes <= 0:
        return None
    oBackpackCon = oTarget.m_BackpackCon
    if not oBackpackCon:
        return None
    oGame = oTarget.m_Game
    sKey = oLifeCycle.Key()
    for _ in range(iRewardTimes):
        iCrystal = ChooseKey(oGame, dCrystal)
        clsCrystalData = GetCrystalPerformCls(iCrystal)
        if not clsCrystalData:
            SendAlert('err', '%s %s %s未配置水晶数据%s %s' % (oGame.m_ID, oTarget.m_ID, sKey, iCrystal, dCrystal))
            continue
        iChoosePoint = ChooseKey(oGame, clsCrystalData.m_CanChoosePoint)
        dCrystalData = {
            'SID': iCrystal,
            'TP': iChoosePoint }
        dReward = {
            'info': dCrystalData }
        dExtInfo = { }
        if iBeneMark:
            dExtInfo['BeneMark'] = iBeneMark
        cl_reward.RewardS7Crystal(oGame, oTarget, dReward, sKey, dExtInfo)
    


def CommonAddCustomValueWithReason(oTarget, oLifeCycle, sKey, iVal):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.DelCustomFactor(sKey, sReason)

    iVal = cl_formula.GetResultByData(oTarget, iVal, {
        'LifeCycle': oLifeCycle })
    sReason = oLifeCycle.Key()
    oTarget.AddCustomValue(sKey, iVal, sReason)
    oLifeCycle.AddUniqueDisableFunc('EventCBAddCustomDataByFactor-%s' % sKey, ClearFunc, iCover = 0)


def CommonSetBulletPickIgnoreMax(oTarget, oLifeCycle, iBullet):
    
    def ClearFunc(oTarget, oLifeCycle):
        CommonClearBulletPickIgnoreMax(oTarget, oLifeCycle, iBullet)

    oTarget.m_BulletCon.m_DropModule |= DROP_BULLETPICK_IGNOREMAX
    dBulletPickIgnoreMax = oTarget.SetDefault('BulletPickIgnoreMax', { })
    dBulletPick = dBulletPickIgnoreMax.setdefault(iBullet, { })
    sKey = 'CommonSetBulletPickModule-%s' % oLifeCycle.Key()
    if sKey in dBulletPick:
        return None
    dBulletPick[sKey] = 1
    oLifeCycle.AddUniqueDisableFunc(sKey, ClearFunc, iCover = 0)


def CommonClearBulletPickIgnoreMax(oTarget, oLifeCycle, iBullet):
    dBulletPickIgnoreMax = oTarget.Query('BulletPickIgnoreMax', { })
    if iBullet not in dBulletPickIgnoreMax:
        return None
    dBulletPick = dBulletPickIgnoreMax[iBullet]
    sKey = 'CommonSetBulletPickModule-%s' % oLifeCycle.Key()
    dBulletPick.pop(sKey, 0)
    if not dBulletPick:
        dBulletPickIgnoreMax.pop(iBullet, 0)
        if not dBulletPickIgnoreMax:
            oTarget.m_BulletCon.m_DropModule &= ~DROP_BULLETPICK_IGNOREMAX

