# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warrior.pyc
# RelativePath: clientlogic/cl_warrior.pyc
# Source Generated with Decompyle++
# File: cl_warrior.pyc (Python 3.6)

from cl_only import Functor, GAME_FRAME, Time2Frame, PerSecond2PerFrame, GAME_FRAME_INF, Second2Frame, PY_FLAG_DIED, PY_FLAG_DYING, PY_FLAG_DEAD, CTRL_FLAG_FOR_DEAD, DEAD_FLAG_DIED, DEAD_FLAG_DYING, DEAD_FLAG_REAL, CTRL_FLAG_HERO_DYING, CTRL_FLAG_SIM, SendAlert
g_RelifePriority = g_RelifePriority
from cl_commondefines import PAMOD_TYPE_DYING, STATE_SECKILL, FIGHT3_KEY_IGNELBEEXECUTED, MONSTER_PART_SECKILL, STATE_UNDER_ATTACK, GetContainHitArea, FIGHT2_KEY_ALL, FIGHT2_KEY_OFFSET, ARMOR_RADIO_ADD, ARMOR_RADIO_SUB, MAX_STATE_TYPE, FIGHT_KEY_OFFSET, FIGHT_KEY_IMMOBILIZE, FIGHT3_KEY_IGNOREATT, DAM_TYPE_ELEMENT, DAM_MASK_ELEMENT, OBJ_VICTIM, OBJ_ATTACK, IMMUNITY_WUDI, IMMUNITY_PERFORM, IMMUNITY_SHOWCOVER, FIGHT_KEY_WUDI, DAM_TYPE_WEAKNESS, DAM_TYPE_HARDNESS, MONSTER_PART_WEAKNESS, STATE_WEAKER, MONSTER_PART_UNTAGGED, DEBUG_STATUS_NODIE, STATE_SHIELD_LIST, MONSTER_PART_SHIELD, GetGlobalHitPartToType, FORBID_SHIELDRECOVER, STATE_TIME_LIMIT, STATE_RELIFE, STATE_TIME_FOREVER, STATE_DYING, DAM_TYPE_SCENE, CTRLWARRIOR_MASK, PF_TYPE_PASSIVE, DAM_USE_HP, RADIO_SUB, RADIO_HP, WARRIOR_HERO, RADIO_ADD, DAM_TYPE_TRUE, DAM_TYPE_SHIELD, DAM_MASK_PART, g_Attr2HPType, FORBID_SHIELDCURE, DAM_USE_SHIELD, FORBID_BREAKSHIELDRECOVER, FIGHT_KEY_ALL, MIN_FIGHT_KEY, STATE_CLS_SPECIAL, STATE_CLS_ABNORMAL, STATE_CLS_HELP, g_ElementFactor, HPARMOR_RADIO_ADD, HPARMOR_RADIO_SUB, SHIELD_RADIO_ADD, SHIELD_RADIO_SUB, HP_RADIO_ADD, HP_RADIO_SUB, DAM_TYPE_NORMAL, DEFEND_TREND_NONE, ATTACKERSUBMSG_NORMAL, RADIO_MIX_HPARMOR, RADIO_ARMOR, RADIO_SHIELD, DAM_USE_ARMOR, ABNORMAL_DEFAULT, CLIENT_ACTION_NUM_MAX, SERVER_ACTION_NUM_MAX, FIGHT_KEY_IGNOREDAMAGE, WARRIOR_SERVANT, TYPE_RELIFE_ALL, RADIO_MIX_HPARMORSHIELD, HPARMORSHIELD_RADIO_SUB, HPARMORSHIELD_RADIO_ADD, WARRIOR_PET
from cl_commondefines import FIGHT3_KEY_IGNOREKNOCKBACK, FIGHT3_KEY_IGNORETHUMP, WUDI_START, WUDI_END, STATE_IDX_DEFAULT, STATE_IDX_DELAY, STATE_IDX_COUNT, STATE_IDX_LIMITCOUNT, OBJECT_OWNER, OBJECT_SELFOWNER, STATE_UNBALANCE, EXSHOWTIPS_ALL, DIE_PRIORITY_TYPE_NONE, DIE_PRIORITY_TYPE_DIE, DIE_PRIORITY_TYPE_NO_DIE, DIE_PRIORITY, EXECUTETYPE_PART_SECKILL, g_PositiveElement, STATE_SUBSPD_LIST, WARRIOR_BOSS, BASEATTR_CLIENT, BASEATTR_REFRESH, IGNORESTATE_EFF_FLAG
from cl_cscommondef import ITEM_BUFF_TYPE, ITEM_DEBUFF_TYPE, WARRIOR_DEVICE
from cl_object.reason import CPerformReason, CStrReason
g_CureTypeSequence = g_CureTypeSequence
from cl_formula import g_HpTypeIndex, g_DamTypeSequence
from itertools import chain
from cl_msgcenter.defines import MSG_WAR_ATTACK, MSG_WAR_PERFORM
from cl_object.logging import WarobjLog, SkillLog, OtherLog
from cl_propdata import BASIC_PROP_NAME
from cl_pxlayer import PXLAYER_PLAYER_DYING, PXMASK_GROUNDBLK
from cl_only import TraceLog
import functools
import types
import cl_world
import cl_object.baseattr
import cl_object.maxattr
import cl_object.sumattr
import cl_object.bitattr
import cl_object.timeunit
import cl_object.elementtype
import cl_object.logging
import cl_object.dielog
import cl_container.statecon
import cl_container.performcon
import cl_perform
import cl_perform.net
import cl_perform.cartoon.argcheck
import cl_snetwar
import cl_msgcenter
import cl_action
import cl_forbid
import cl_state
import cl_formula
import cl_war
import cl_abnormalconf
import cl_notify
import cl_modeldefine
import cl_only
import cl_netattr
import cl_engphyobj
import cllib.lib_flag
g_ThresholdDirect = {
    'HP': RADIO_HP,
    'Shield': RADIO_SHIELD,
    'Armor': RADIO_ARMOR,
    'HPArmor': RADIO_MIX_HPARMOR,
    'HPArmorShield': RADIO_MIX_HPARMORSHIELD }
g_MixThresholdInfo = {
    'HP': (('Armor', RADIO_MIX_HPARMOR, 'HPArmor'), ('ArmorShield', RADIO_MIX_HPARMORSHIELD, 'HPArmorShield')),
    'Armor': (('HP', RADIO_MIX_HPARMOR, 'HPArmor'), ('HPShield', RADIO_MIX_HPARMORSHIELD, 'HPArmorShield')),
    'Shield': (('HPArmor', RADIO_MIX_HPARMORSHIELD, 'HPArmorShield'),) }
g_ContainPartAttr = ('HP', 'HPMax', 'Shield', 'ShieldMax', 'Armor', 'ArmorMax')
SEND_ASSISTKILL_FIGHTTYPE = WARRIOR_HERO | WARRIOR_SERVANT | WARRIOR_DEVICE | WARRIOR_PET

class CWarrior(cl_world.CSceneObject):
    m_AttPerform = 0
    m_PerformList = ()
    m_Delete = 0
    m_RemoveDelay = 3 * GAME_FRAME
    m_ValidShowTips = 1
    m_SubAttackMsg = ATTACKERSUBMSG_NORMAL
    m_AssistKillFrame = Second2Frame(30)
    m_DefendTrend = DEFEND_TREND_NONE
    m_ForceDistance = 0
    m_Part = 0
    m_OwnerPlayerID = 0
    m_ActionSpeed = 100
    m_NoRayCheck = 0
    m_GroundMaxDis = 15
    m_HateFactor = 1
    m_ExtraModelDistance = 0
    m_HeightOffset = 0
    m_OnGame = 1
    
    def __init__(self, oGame, nid):
        super().__init__(oGame, nid)
        self.m_Owner = 0
        self.m_PrivateAttr = { }
        self.m_CommonPerform = ()
        self.m_Dead = 0
        self.m_CastingSkill = { }
        self.m_BackSwingSkill = { }
        self.m_ReplacePerform = { }
        self.m_SummonDict = { }
        self.m_BulletDict = { }
        self.m_DieDisablePassive = None
        self.m_ImmobilizeSource = { }
        self.m_LockedCallOut = { }
        self.m_LockedSkill = { }
        self.m_LockableCallOut = { }
        self.m_ActionNum = 0
        self.m_LastActionNum = SERVER_ACTION_NUM_MAX
        self.m_HP = 0
        self.m_Armor = 0
        self.m_Shield = 0
        self.m_Energy = 0
        self.m_ExcessHP = 0
        self.m_ExcessShield = 0
        self.m_ExcessArmor = 0
        self.m_ExcessHPRatio = 1
        self.m_ExcessShieldRatio = 1
        self.m_ExcessArmorRatio = 1
        self.m_MaxExcessAttr = 100000
        self.m_Grade = 1
        self.m_FinalDam = 0
        self.m_FinalAttack = 0
        self.m_PositiveElementFactorValue = 0
        self.m_PositiveElementFactor = { }
        self.m_PositiveElementFactorValueByType = { }
        self.m_PositiveElementFactorByType = { }
        self.m_ElementType = DAM_TYPE_NORMAL
        self.m_ForbidRuleInfo = { }
        self.m_ForbidTypeInfo = { }
        self.m_ThresholdDict = {
            HPARMORSHIELD_RADIO_ADD: [],
            HPARMORSHIELD_RADIO_SUB: [],
            HPARMOR_RADIO_ADD: [],
            HPARMOR_RADIO_SUB: [],
            ARMOR_RADIO_ADD: [],
            ARMOR_RADIO_SUB: [],
            SHIELD_RADIO_ADD: [],
            SHIELD_RADIO_SUB: [],
            HP_RADIO_ADD: [],
            HP_RADIO_SUB: [] }
        self.m_TransEvt = { }
        self.m_TransEvtToSort = { }
        self.m_UsePriority = [
            MSG_WAR_ATTACK,
            MSG_WAR_PERFORM]
        self.m_NeedMonitorAttrDict = { }
        self.m_FollowDieObjs = { }
        self.SetAttr('DebuffPeriod', 100, 0)
        self.SetAttr('DebuffFactor', 100, BASEATTR_REFRESH | BASEATTR_CLIENT)
        self.SetAttr('FireAbnormalFactor', ABNORMAL_DEFAULT, 0)
        self.SetAttr('ThunderAbnormalFactor', ABNORMAL_DEFAULT, 0)
        self.SetAttr('CorrisionAbnormalFactor', ABNORMAL_DEFAULT, 0)
        self.SetBitAttr('SpecialKey')
        self.SetBitAttr('LogicKey')
        self.InitStateAttr()
        self.InitOtherAttr()
        self.InitCon()
        self.m_ElemenFatctor = cl_only.DeepCopy(g_ElementFactor)
        self.m_CurMaxElemenFactor = { }
        self.InitCurMaxElemenFactor()
        self.m_ElementFactorInfo = { }
        self.m_ImmuneElementRestrainted = { }
        self.m_MustElementRestrainted = { }
        self.m_DyingModel = None
        self.m_Resistance = None
        self.m_DeadReason = None
        self.m_PassLayerClearKey = { }
        self.m_ChanegActionSpeed = { }
        self.m_UseActionSpeed = ''
        self.m_ActSpFrameShaft = { }
        self.m_BaseDamRatio = { }
        self.m_BaseRecvDamRatio = { }
        self.m_SkillCheckExtraArgs = { }
        self.SkillCheckArgs = (0, 0)
        self.m_CustomFactor = { }

    
    def InitCon(self):
        self.m_State = cl_container.statecon.CStateContainer(self)
        self.m_StateTimeUnit = cl_object.timeunit.CStateTimeUnit(self)
        self.m_PFPassTimeUnit = cl_object.timeunit.CPassiveTimeUnit(self)
        self.m_Perform = cl_container.performcon.CPerformContainer(self)
        self.m_ElementTypeObj = cl_object.elementtype.CElementType(self, self.m_ElementType, 0)
        self.m_EleAbnormal = cl_abnormalconf.GetAbnormalEleDam(self, self.m_FightType)

    
    def InitCurMaxElemenFactor(self):
        for iKey, dValue in self.m_ElemenFatctor.items():
            iMaxValue = max(dValue.values())
            self.m_CurMaxElemenFactor[iKey] = iMaxValue
        

    
    def InitWarValue(self):
        self.InitPerform()

    
    def Release(self):
        if self.m_ReleaseFlag:
            return None
        if self.m_PassLayerClearKey:
            oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
            cl_msgcenter.DoneAttention(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, 'PassLayerClearData')
        self.m_Perform.AllPerformDisable(iNotify = 0)
        self.m_Perform.Release()
        lstSummon = list(self.m_SummonDict)
        for iSummon in lstSummon:
            oSummon = self.m_Game.GetObject(iSummon)
            if oSummon:
                oSummon.Remove('PlayerRelease')
        
        self.m_SummonDict = { }
        self.m_State.Release()
        self.m_StateTimeUnit.Release()
        self.m_PFPassTimeUnit.Release()
        self.m_EleAbnormal.Release()
        for sAttr, iCnt in self.m_NeedMonitorAttrDict.items():
            if iCnt <= 0:
                continue
            oAttr = self.m_PrivateAttr[sAttr]
            oAttr.Refresh = oAttr._Refresh
            del oAttr.Refresh
            del oAttr._Refresh
        
        self.m_NeedMonitorAttrDict = { }
        for oAttr in self.m_PrivateAttr.values():
            oAttr.ClearAll()
        
        self.m_PrivateAttr = { }
        self.m_ElementTypeObj = None
        self.m_Perform = None
        self.m_State = None
        self.m_StateTimeUnit = None
        self.m_PFPassTimeUnit = None
        self.m_EleAbnormal = None
        lstBullet = list(self.m_BulletDict.values())
        for oBullet in lstBullet:
            oBullet.Unstall()
        
        self.m_BulletDict = { }
        self.m_DyingModel = None
        self.m_Resistance = None
        self.m_ElementFactorInfo = { }
        self.m_DeadReason = None
        self.m_ThresholdDict = { }
        super(CWarrior, self).Release()

    
    def AttReason(self, pfobj, iActNum):
        if pfobj.m_MainPerform:
            iPerform = pfobj.m_MainPerform
        else:
            iPerform = pfobj.m_SID
        oItem = pfobj.GetMyItem()
        if oItem:
            dData = {
                'Item': oItem.m_ID,
                'ItemSID': oItem.m_SID,
                'ItemType': oItem.Type() }
        else:
            dData = { }
        dData['ActNum'] = iActNum
        dData['FightType'] = self.m_FightType
        oReason = CPerformReason(iPerform, self.m_Owner, self.m_SID, self.m_FightType, None, dData)
        return oReason

    
    def OnInitToScene(self, tPos):
        self.SkillCheckArgs = cl_modeldefine.GetModelDefine(self.m_Shape, 'Physx')
        self.UpdateShieldRecoverStatus()
        if 'REnergy' in self.m_PrivateAttr and self.QueryAttr('REnergy') > 0:
            self.UpdateEnergyRecoverStatus()

    
    def InitStateAttr(self):
        self.SetMaxAttr('IgnoreST%d' % STATE_CLS_HELP)
        self.SetMaxAttr('IgnoreST%d' % STATE_CLS_ABNORMAL)
        self.SetMaxAttr('IgnoreST%d' % STATE_CLS_SPECIAL)
        self.SetBitAttr('IgnoreSTEff')
        self.SetBitAttr('ForbidEnableSTEff')
        self.SetBitAttr('ForbidEnableSTEffByMonster')

    
    def InitOtherAttr(self):
        self.SetBitAttr('Ignore_Hold_MoveSpeed')

    
    def SetAttr(self, sAttr, iValue, iRefresh):
        if sAttr not in self.m_PrivateAttr:
            oAttr = cl_object.baseattr.NewAttr(self, sAttr, iValue, iRefresh)
            self.m_PrivateAttr[sAttr] = oAttr
        else:
            oAttr = self.m_PrivateAttr[sAttr]
            oAttr.ChangeBase(self, iValue)
        if sAttr == 'AttSpeed':
            self.GS2CPropChange('B%s' % sAttr)

    
    def HasAttr(self, sAttr):
        return sAttr in self.m_PrivateAttr

    
    def GetAttr(self, sAttr):
        return self.m_PrivateAttr[sAttr]

    
    def QueryAttrExt(self, sAttr):
        oAttr = self.m_PrivateAttr['%s' % sAttr[1:]]
        if oAttr.m_Refresh:
            oAttr.Refresh(self)
        return oAttr.m_CurValue - oAttr.m_BaseValue

    
    def QueryAttrBase(self, sAttr):
        oAttr = self.m_PrivateAttr['%s' % sAttr[1:]]
        return oAttr.m_BaseValue

    
    def QueryAttr(self, sAttr):
        oAttr = self.m_PrivateAttr[sAttr]
        if oAttr.m_Refresh:
            oAttr.Refresh(self)
        if oAttr.m_ForceCurValue is not None:
            return oAttr.m_ForceCurValue
        return oAttr.m_CurValue

    
    def QueryAttrNotForce(self, sAttr):
        oAttr = self.m_PrivateAttr[sAttr]
        if oAttr.m_Refresh:
            oAttr.Refresh(self)
        return oAttr.m_CurValue

    
    def QueryAttrForecast(self, sAttr):
        pass

    
    def HasAttrFactor(self, sAttr, sKey):
        return self.m_PrivateAttr[sAttr].HasFactor(sKey)

    
    def HasForceAtt(self, sAttr, sKey = ''):
        oAttr = self.m_PrivateAttr[sAttr]
        return oAttr.HasForce(sKey)

    
    def AttrChange(self, sAttr, iMul, iAdd, sKey, iRefresh = 1, iSave = 0, iPreExclude = 0):
        if iRefresh:
            self.m_PrivateAttr[sAttr].AddValue(self, iMul, iAdd, sKey, iSave, iPreExclude)
        else:
            self.m_PrivateAttr[sAttr].AddValue(None, iMul, iAdd, sKey, iSave, iPreExclude)

    
    def AttrClear(self, sAttr, sKey, iRefresh = 1):
        if iRefresh:
            self.m_PrivateAttr[sAttr].ClearValue(self, sKey)
        else:
            self.m_PrivateAttr[sAttr].ClearValue(None, sKey)

    
    def AttrForceSet(self, sAttr, iValue, sKey, iRefresh = 1):
        if iRefresh:
            self.m_PrivateAttr[sAttr].SetForceValue(self, iValue, sKey)
        else:
            self.m_PrivateAttr[sAttr].SetForceValue(None, iValue, sKey)

    
    def AttrForceClear(self, sAttr, sKey, iRefresh = 1):
        if iRefresh:
            self.m_PrivateAttr[sAttr].ClearForceValue(self, sKey)
        else:
            self.m_PrivateAttr[sAttr].ClearForceValue(None, sKey)

    
    def RefreshAttr(self, sAttr, iValue):
        self.GS2CPropChange(sAttr, iValue)

    
    def SetBitAttr(self, sAttr):
        if sAttr not in self.m_PrivateAttr:
            oAttr = cl_object.bitattr.CBitAttr(sAttr)
            self.m_PrivateAttr[sAttr] = oAttr

    
    def QueryBitAttr(self, sAttr):
        if sAttr not in self.m_PrivateAttr:
            return 0
        oBitAttr = self.m_PrivateAttr[sAttr]
        if oBitAttr.m_Refresh:
            oBitAttr.Refresh()
        return oBitAttr.m_CurVal

    
    def AddBitAttr(self, sAttr, sKey, iKey, bSync = True):
        if sAttr not in self.m_PrivateAttr:
            return None
        oAttr = self.m_PrivateAttr[sAttr]
        oAttr.AddValue(sKey, iKey)
        if sAttr == 'SpecialKey':
            if MIN_FIGHT_KEY <= iKey and iKey <= FIGHT_KEY_ALL and oAttr.NeedRefresh():
                if bSync:
                    self.GS2CPropChange('FightMark')
                if iKey == FIGHT_KEY_WUDI and self.IsWudi():
                    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_WUDI, self, { }, iSub = WUDI_START)

    
    def ClearBitAttr(self, sAttr, sKey, iKey, bSync = True):
        if sAttr not in self.m_PrivateAttr:
            return None
        oAttr = self.m_PrivateAttr[sAttr]
        oAttr.ClearValue(sKey, iKey)
        if sAttr == 'SpecialKey':
            if MIN_FIGHT_KEY <= iKey and iKey <= FIGHT_KEY_ALL and oAttr.NeedRefresh():
                if bSync:
                    self.GS2CPropChange('FightMark')
                if iKey == FIGHT_KEY_WUDI and not self.IsWudi():
                    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_WUDI, self, { }, iSub = WUDI_END)

    
    def GetBitAttrKeyInfo(self, sAttr, iKey):
        if sAttr not in self.m_PrivateAttr:
            return { }
        oBitAttr = self.m_PrivateAttr[sAttr]
        return oBitAttr.GetKeyInfo(iKey)

    
    def CheckBitAttrKey(self, sAttr, iKey):
        if sAttr not in self.m_PrivateAttr:
            return 0
        oBitAttr = self.m_PrivateAttr[sAttr]
        return oBitAttr.CheckKey(iKey)

    
    def SetSumAttr(self, sAttr, bClient):
        if sAttr not in self.m_PrivateAttr:
            oAttr = cl_object.sumattr.CSumAttr(sAttr, bClient)
            self.m_PrivateAttr[sAttr] = oAttr

    
    def QuerySumAttr(self, sAttr):
        if sAttr not in self.m_PrivateAttr:
            return 0
        return self.m_PrivateAttr[sAttr].GetValue()

    
    def QuerySumAttrByKey(self, sAttr, sKey):
        if sAttr not in self.m_PrivateAttr:
            return 0
        return self.m_PrivateAttr[sAttr].GetValueByKey(sKey)

    
    def AddSumAttr(self, sAttr, sKey, iVal):
        if sAttr not in self.m_PrivateAttr:
            return None
        self.m_PrivateAttr[sAttr].AddValue(self, sKey, iVal)

    
    def UpdateSumAttr(self, sAttr, sKey, iVal):
        if sAttr not in self.m_PrivateAttr:
            return None
        self.m_PrivateAttr[sAttr].UpdateValue(self, sKey, iVal)

    
    def SubSumAttr(self, sAttr, iVal):
        if sAttr not in self.m_PrivateAttr:
            return None
        self.m_PrivateAttr[sAttr].SubValue(self, iVal)

    
    def ClearSumAttr(self, sAttr, sKey):
        if sAttr not in self.m_PrivateAttr:
            return 0
        return self.m_PrivateAttr[sAttr].ClearValue(self, sKey)

    
    def SetMaxAttr(self, sAttr):
        if sAttr not in self.m_PrivateAttr:
            oAttr = cl_object.maxattr.CMaxAttr(self.m_Game, sAttr)
            self.m_PrivateAttr[sAttr] = oAttr

    
    def QueryMaxAttr(self, sAttr):
        if sAttr not in self.m_PrivateAttr:
            return 0
        return self.m_PrivateAttr[sAttr].GetValue()

    
    def QueryMaxAttrTime(self, sAttr):
        if sAttr not in self.m_PrivateAttr:
            return 0
        return self.m_PrivateAttr[sAttr].GetTime()

    
    def AddMaxAttr(self, sAttr, sKey, iValue, iTime):
        if sAttr not in self.m_PrivateAttr:
            return 0
        return self.m_PrivateAttr[sAttr].AddValue(sKey, iValue, iTime)

    
    def ClearMaxAttr(self, sAttr, sKey):
        if sAttr not in self.m_PrivateAttr:
            return 0
        return self.m_PrivateAttr[sAttr].ClearValue(sKey)

    
    def CheckIgnoreAttrChange(self, sSource, sAttr, iAdd, iMul):
        iIgnoreAttrChange = self.QueryBitAttr('Ignore_{}_{}'.format(sSource, sAttr))
        if iIgnoreAttrChange & ITEM_BUFF_TYPE == ITEM_BUFF_TYPE:
            if iAdd > 0 or iMul > 0:
                return True
        if iIgnoreAttrChange & ITEM_DEBUFF_TYPE == ITEM_DEBUFF_TYPE:
            if iAdd < 0 or iMul < 0:
                return True
        return False

    
    def AttrChangeFixedAddition(self, sAttr, sKey, iValue):
        if sAttr not in self.m_PrivateAttr:
            return None
        self.m_PrivateAttr[sAttr].AddFixedAddition(self, sKey, iValue)

    
    def AttrClearFixedAddition(self, sAttr, sKey):
        if sAttr not in self.m_PrivateAttr:
            return None
        self.m_PrivateAttr[sAttr].RemoveFixedAddition(self, sKey)

    
    def TurnSpeed(self):
        return self.QueryAttr('TurnSpeed')

    
    def MoveSpeed(self):
        return self.QueryAttr('MoveSpeed')

    
    def ShieldMax(self):
        return self.QueryAttr('ShieldMax')

    
    def RShield(self):
        return self.QueryAttr('RShield')

    
    def GetShieldStatus(self):
        return self.Query('ShieldStatus')

    
    def GetShieldRecoverFrame(self):
        iTime = self.QueryAttr('ShieldRecoverTime')
        return Time2Frame(iTime)

    
    def GetShieldRecoverFullFrame(self):
        iFullFrame = 0
        if not self.Query('StopShieldRecoverInfo'):
            iRShield = self.QueryAttr('RShield')
            if iRShield > 0:
                iMaxShield = self.ShieldMax()
                iShield = self.Shield()
                if iShield < iMaxShield:
                    iFullFrame = (iMaxShield - iShield) * GAME_FRAME * 100 // iMaxShield // iRShield + 1
        return iFullFrame

    
    def UpdateShieldRecoverStatus(self):
        iFullFrame = self.GetShieldRecoverFullFrame()
        if self.Query('ShieldStatus'):
            self.Remove_Call_Out('ShieldRecoverStatusEnterStop')
            if not iFullFrame:
                self.Shield()
                self.Set('ShieldStatus', 0)
                self.GS2CPropChange('Shield')
                self.GS2CPropChange('ShieldStatus')
                dMsgInfo = {
                    'AID': self.m_ID,
                    'CurVID': self.m_ID }
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SHIELDFINSH, self, dMsgInfo)
            elif iFullFrame:
                self.Shield()
                self.Set('ShieldStatus', 1)
                self.GS2CPropChange('Shield')
                self.GS2CPropChange('ShieldStatus')
                dMsgInfo = {
                    'AID': self.m_ID,
                    'CurVID': self.m_ID }
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SHIELD_RECOVER, self, dMsgInfo)
        if None:
            self.Call_Out(self.UpdateShieldRecoverStatus, iFullFrame, 'ShieldRecoverStatusEnterStop')

    
    def StopShieldRecover(self, sFlag, iRestartFrame = GAME_FRAME_INF):
        dStop = self.SetDefault('StopShieldRecoverInfo', { })
        if sFlag in dStop:
            return None
        dStop[sFlag] = self.m_Game.GetFrameNum()
        if iRestartFrame > 0 and iRestartFrame != GAME_FRAME_INF:
            self.Call_Out(Functor(self.StartShieldRecover, sFlag), iRestartFrame, 'ShieldRecoverSchedule' + sFlag)
        self.UpdateShieldRecoverStatus()

    
    def StartShieldRecover(self, sFlag):
        dStop = self.SetDefault('StopShieldRecoverInfo', { })
        if sFlag in dStop:
            self.Remove_Call_Out('ShieldRecoverSchedule' + sFlag)
            dStop.pop(sFlag)
        self.UpdateShieldRecoverStatus()

    
    def UpdateHaltShieldRecover(self, iRestartFrame):
        dStop = self.SetDefault('StopShieldRecoverInfo', { })
        if 'Halt' in dStop:
            self.Remove_Call_Out('ShieldRecoverScheduleHalt')
            dStop.pop('Halt')
        if iRestartFrame > 0:
            self.StopShieldRecover('Halt', iRestartFrame)
        else:
            self.UpdateShieldRecoverStatus()

    
    def HaltShieldRecover(self, iHaltShieldRecovry = 1):
        if self.Query('ShieldStatus'):
            if self.IsForbid(FORBID_BREAKSHIELDRECOVER) or not iHaltShieldRecovry:
                return None
        if not iHaltShieldRecovry:
            iShieldRecoverFrame = 0
        else:
            iShieldRecoverFrame = self.GetShieldRecoverFrame()
        self.UpdateHaltShieldRecover(iShieldRecoverFrame)

    
    def GetShieldRecoverHaltFrame(self):
        dStop = self.Query('StopShieldRecoverInfo', { })
        return dStop.get('Halt', 0)

    
    def HP(self):
        if self.IsDead():
            return 0
        iRHP = self.QueryAttr('RHP')
        if iRHP and self.m_HP > 0:
            iFrame = self.Query('CalHPFrame')
            iNowFrame = self.m_Game.GetFrameNum()
            self.Set('CalHPFrame', iNowFrame)
            if iFrame and iFrame < iNowFrame:
                iHPMax = self.QueryAttr('HPMax')
                iAdd = (iNowFrame - iFrame) * iRHP
                self.m_HP += iAdd
                if self.m_HP > iHPMax:
                    self.m_HP = iHPMax
        return self.m_HP

    
    def Armor(self):
        return self.m_Armor

    
    def Shield(self):
        iShieldMax = self.QueryAttr('ShieldMax')
        iNowFrame = self.m_Game.GetFrameNum()
        iFrame = self.Query('CalShieldFrame', iNowFrame)
        iAddFrame = iNowFrame - iFrame
        self.Set('CalShieldFrame', iNowFrame)
        if iAddFrame > 0 and self.Query('ShieldStatus'):
            iRShield = self.QueryAttr('RShield')
            if iRShield > 0:
                iAdd = iShieldMax * iRShield * iAddFrame // GAME_FRAME // 100
                self.m_Shield += iAdd
        if self.m_Shield > iShieldMax:
            self.m_Shield = iShieldMax
        return self.m_Shield

    
    def ValidHPAttr(self, sAttr):
        return sAttr in g_HpTypeIndex

    
    def GetHpInfoByRatio(self, dRatio):
        iHp = self.QueryAttr('HPMax') * dRatio['HPRatio'] // 100
        iShield = self.QueryAttr('ShieldMax') * dRatio['ShieldRatio'] // 100
        iArmor = self.QueryAttr('ArmorMax') * dRatio['ArmorRatio'] // 100
        return {
            'HP': iHp,
            'Shield': iShield,
            'Armor': iArmor }

    
    def ExcessHP(self):
        oAttr = self.m_PrivateAttr['HPMax']
        if oAttr.m_ForceCurValue is not None:
            return 0
        return self.m_ExcessHP

    
    def ExcessShield(self):
        oAttr = self.m_PrivateAttr['ShieldMax']
        if oAttr.m_ForceCurValue is not None:
            return 0
        return self.m_ExcessShield

    
    def ExcessArmor(self):
        oAttr = self.m_PrivateAttr['ArmorMax']
        if oAttr.m_ForceCurValue is not None:
            return 0
        return self.m_ExcessArmor

    
    def SetMaxExcessAttr(self, iMaxVal):
        if iMaxVal < 0:
            iMaxVal = 0
        self.m_MaxExcessAttr = iMaxVal

    
    def GetExcessValuesByType(self, sType):
        if sType == 'HP':
            return self.ExcessHP()
        if sType == 'Shield':
            return self.ExcessShield()
        if sType == 'Armor':
            return self.ExcessArmor()
        return 0

    
    def GetExcessRatioByType(self, sType):
        if sType == 'HP':
            return self.m_ExcessHPRatio
        if sType == 'Shield':
            return self.m_ExcessShieldRatio
        if sType == 'Armor':
            return self.m_ExcessArmorRatio
        return 1

    
    def UpdateExcessAttr(self, sAttr):
        sExcessKey = 'm_Excess%s' % sAttr
        iCurVal = self.__dict__[sExcessKey]
        oAttr = self.m_PrivateAttr['%sMax' % sAttr]
        fChangeRatio = oAttr.CalMulChangeRatio()
        sExcessAttrRatio = 'm_Excess%sRatio' % sAttr
        fCurRatio = self.__dict__[sExcessAttrRatio]
        sExcessAttr = 'Excess%s' % sAttr
        if fChangeRatio == fCurRatio:
            if iCurVal:
                self.GS2CPropChange(sExcessAttr)
            return None
        if not fCurRatio:
            fCurRatio = 1
        self.__dict__[sExcessAttrRatio] = fChangeRatio
        if iCurVal:
            iNewVal = int((iCurVal / fCurRatio) * fChangeRatio)
            self.TrueModifyExcessAttr(sAttr, iNewVal - iCurVal)

    
    def AddExcessAttr(self, sAttr, iAdd, iHPModify = 1):
        sExcessAttrRatio = 'm_Excess%sRatio' % sAttr
        fCurRatio = self.__dict__[sExcessAttrRatio]
        if not fCurRatio:
            fCurRatio = 1
        self.TrueModifyExcessAttr(sAttr, int(iAdd * fCurRatio), iHPModify)

    
    def TrueModifyExcessAttr(self, sAttr, iChange, iHPModify = 1, iAttackPlayer = 0):
        if not iChange:
            return iChange
        sExcessAttr = 'Excess%s' % sAttr
        sExcessKey = 'm_%s' % sExcessAttr
        iOldExcess = self.__dict__[sExcessKey]
        if iChange <= 0 and iOldExcess <= 0:
            return iChange
        iNewExcess = iOldExcess + iChange
        if iNewExcess < 0:
            iNewExcess = 0
        else:
            iTotalExcessAttr = self.ExcessHP() + self.ExcessShield() + self.ExcessArmor()
            if iTotalExcessAttr + iChange > self.m_MaxExcessAttr:
                iNewExcess = (self.m_MaxExcessAttr - iTotalExcessAttr) + iOldExcess
        self.__dict__[sExcessKey] = iNewExcess
        sMaxAttr = '%sMax' % sAttr
        oAttrFunc = getattr(self, sAttr)
        iOldMaxVal = self.QueryAttr(sMaxAttr)
        iOldVal = oAttrFunc()
        self.m_PrivateAttr[sMaxAttr].SetExcessVal(None, iNewExcess)
        iCurMaxVal = self.QueryAttr(sMaxAttr)
        self.GS2CCachePropChange(sMaxAttr, iCurMaxVal, iAttackPlayer)
        iNewVal = oAttrFunc()
        if iNewVal > iCurMaxVal:
            iNewVal = iCurMaxVal
            sKey = 'm_%s' % sAttr
            self.__dict__[sKey] = iCurMaxVal
        if iChange < 0:
            iChange += iOldVal - iNewVal
        elif iHPModify:
            iAttrChange = iCurMaxVal - iOldMaxVal - iNewVal - iOldVal
            oReason = cl_object.reason.CStrReason('过量属性刷新')
            self.HPDirectModify(sAttr, self.m_ID, iAttrChange, oReason, iCalExcess = 0)
        if sMaxAttr in self.m_NeedMonitorAttrDict:
            iSub = BASIC_PROP_NAME[sMaxAttr][0]
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ATTR_CHANGE, self, { }, iSub = iSub)
        self.GS2CCachePropChange(sAttr, iNewVal, iAttackPlayer)
        self.GS2CCachePropChange(sExcessAttr, iNewExcess, iAttackPlayer)
        return iChange

    
    def LoadExcessAttr(self, sAttr, iValue):
        sExcessKey = 'm_Excess%s' % sAttr
        self.__dict__[sExcessKey] = iValue
        sMaxAttr = '%sMax' % sAttr
        self.m_PrivateAttr[sMaxAttr].SetExcessVal(None, iValue)

    
    def Energy(self):
        iEnergyMax = self.QueryAttr('EnergyMax')
        iNowFrame = self.m_Game.GetFrameNum()
        iFrame = self.Query('CalEnergyFrame', iNowFrame)
        iAddFrame = iNowFrame - iFrame
        self.Set('CalEnergyFrame', iNowFrame)
        if iAddFrame > 0 and self.Query('EnergyStatus'):
            iREnergy = self.QueryAttr('REnergy')
            if iREnergy > 0:
                iAdd = (iEnergyMax * iREnergy // 100) * iAddFrame // GAME_FRAME // 100
                self.m_Energy += iAdd
        if self.m_Energy > iEnergyMax:
            self.m_Energy = iEnergyMax
        return self.m_Energy

    
    def EnergyMax(self):
        return self.QueryAttr('EnergyMax')

    
    def REnergy(self):
        return self.QueryAttr('REnergy')

    
    def UpdateEnergyRecoverStatus(self):
        if self.Query('StopEnergyRecoverInfo'):
            bRecover = False
        else:
            iREnergy = self.QueryAttr('REnergy')
            if iREnergy <= 0:
                bRecover = False
            else:
                iMaxEnergy = self.EnergyMax()
                iEnergy = self.Energy()
                if iEnergy < iMaxEnergy:
                    bRecover = True
                    iFullFrame = (iMaxEnergy - iEnergy) * GAME_FRAME * 100 // iMaxEnergy // iREnergy // 100 + 1
                else:
                    bRecover = False
        if self.Query('EnergyStatus'):
            self.Remove_Call_Out('EnergyRecoverStatusEnterStop')
            if not bRecover:
                self.Energy()
                self.Set('EnergyStatus', 0)
                self.GS2CPropChange('Energy')
                self.GS2CPropChange('EnergyStatus')
            elif bRecover:
                self.Energy()
                self.Set('EnergyStatus', 1)
                self.GS2CPropChange('Energy')
                self.GS2CPropChange('EnergyStatus')
        if None:
            self.Call_Out(self.UpdateEnergyRecoverStatus, iFullFrame, 'EnergyRecoverStatusEnterStop')

    
    def StopEnergyRecover(self, sFlag, iRestartFrame = GAME_FRAME_INF):
        dStop = self.SetDefault('StopEnergyRecoverInfo', { })
        if sFlag in dStop:
            return None
        iUpdate = 0 if dStop else 1
        dStop[sFlag] = self.m_Game.GetFrameNum()
        if iRestartFrame > 0 and iRestartFrame != GAME_FRAME_INF:
            self.Call_Out(Functor(self.StartEnergyRecover, sFlag), iRestartFrame, 'EnergyRecoverSchedule' + sFlag)
        if iUpdate:
            self.UpdateEnergyRecoverStatus()

    
    def StartEnergyRecover(self, sFlag):
        dStop = self.SetDefault('StopEnergyRecoverInfo', { })
        if sFlag in dStop:
            self.Remove_Call_Out('EnergyRecoverSchedule' + sFlag)
            dStop.pop(sFlag)
        if not dStop:
            self.UpdateEnergyRecoverStatus()

    
    def EnergyModify(self, iChange, iReason = 0, oSkill = None):
        dBeforeChangeMsg = {
            'EnergyChange': iChange,
            'Reason': iReason,
            'Skill': oSkill }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_BEFORE_CHANGE_ENERGY, self, dBeforeChangeMsg)
        iMax = self.QueryAttr('EnergyMax')
        iOld = self.Energy()
        iChange = dBeforeChangeMsg['EnergyChange']
        iNew = iOld + iChange
        if iNew > iMax:
            iNew = iMax
        elif iNew < 0:
            iNew = 0
        self.m_Energy = iNew
        if iNew != iOld:
            self.GS2CPropChange('Energy')
        self.UpdateEnergyRecoverStatus()
        iTrueEnergyChange = abs(iOld - iNew)
        if iNew < iOld:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_COST_ENERGY, self, {
                'EnergyCost': iTrueEnergyChange,
                'TrueEnergyChange': iTrueEnergyChange,
                'Reason': iReason,
                'Skill': oSkill })
        elif iNew > iOld:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ADD_ENERGY, self, {
                'AddEnergy': iTrueEnergyChange,
                'TrueEnergyChange': iTrueEnergyChange,
                'Reason': iReason,
                'Skill': oSkill })

    
    def TrueModify(self, sAttr, oAttack, iChange, iOldMax = 0, iCalExcess = 0):
        if iChange < 0 and iCalExcess:
            if not oAttack or oAttack.m_ID != self.m_ID:
                iAttackPlayer = oAttack.m_PlayerID if oAttack else 0
                iChange = self.TrueModifyExcessAttr(sAttr, iChange, iAttackPlayer = iAttackPlayer)
                if iChange == 0:
                    return 0
        iMax = self.QueryAttr('%sMax' % sAttr)
        sKey = 'm_%s' % sAttr
        iOld = self.__dict__[sKey]
        iNew = iOld + iChange
        if iNew > iMax:
            iChange = iMax - iOld
            iNew = iMax
        elif iNew < 0:
            iChange = -iOld
            iNew = 0
        if iNew == iOld:
            return 0
        self.__dict__[sKey] = iNew
        self.RefreshHPThreshold(sAttr, iOld, iNew, iOldMax = iOldMax)
        self.TriggerMixThresholdChange(sAttr, iOld, iNew)
        if self.m_OwnerPlayerID:
            self.GS2CPropChange(sAttr, iNew)
        else:
            self.m_Game.CachePropChange(self.m_ID, sAttr, iNew, oAttack.m_PlayerID if oAttack else 0)
        return iChange

    
    def HPDirectModify(self, sAttr, iAttack, iChange, oReason, iOldMax = 0, iCalExcess = 1):
        if self.IsDead():
            return None
        oAttack = None if self.m_PlayerID else self.m_Game.GetObject(iAttack)
        iRealChange = self.TrueModify(sAttr, oAttack, iChange, iOldMax, iCalExcess)
        dMsgInfo = {
            'AID': iAttack,
            'CurVID': self.m_ID }
        iHpIndex = g_HpTypeIndex[sAttr]
        if iChange < 0:
            iRealChange = -iRealChange
            dMsgInfo['IsDam'] = True
            lstTotalDam = [
                0,
                0,
                0]
            lstTotalDam[iHpIndex] = iRealChange
            dMsgInfo['TotalDam'] = lstTotalDam
        else:
            dMsgInfo['IsDam'] = False
            lstTotalCure = [
                0,
                0,
                0]
            lstTotalCure[iHpIndex] = iRealChange
            dMsgInfo['TotalCure'] = lstTotalCure
        dMsgInfo['TrueChange'] = [
            (iRealChange, oReason)]
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_HP_CHANGE, self, dMsgInfo)
        if self.m_HP <= 0:
            if iChange < 0:
                self.SetDieFinalInfo(-iChange, iAttack)
            if sAttr != 'HP':
                WarobjLog.Debug('%d %d hpdirectmodify attr:%s %s' % (self.m_Game.m_ID, self.m_PlayerID, sAttr, oReason))
            self.EnterDie(iAttack, oReason)

    
    def HPModifyCure(self, iAttack, lstChange):
        if self.DiePriorityType() == DIE_PRIORITY_TYPE_DIE:
            return 0
        if self.IsDead() or not lstChange:
            return 0
        lstTotalChange = [
            0,
            0,
            0]
        lstTrueChange = []
        oAttack = self.m_Game.GetObject(iAttack)
        iTargetPlayer = oAttack.m_PlayerID if oAttack and oAttack.m_PlayerID else self.m_PlayerID
        for iChange, oReason in lstChange:
            iDamType = oReason.Query('DamType', 0)
            if iDamType & DAM_USE_SHIELD and self.IsForbid(FORBID_SHIELDCURE):
                continue
            iRestChange = iChange
            iTrueChange = 0
            for idx, sAttr, iUseType in g_CureTypeSequence:
                if iDamType & iUseType:
                    iTrueChange = self.TrueModify(sAttr, oAttack, iRestChange)
                    lstTotalChange[idx] += iTrueChange
                    lstTrueChange.append((iTrueChange, oReason))
                    if iRestChange == iTrueChange:
                        break
                    iRestChange -= iTrueChange
            
            iTrueChange = sum(lstTotalChange)
            if iTargetPlayer and iTrueChange and oReason.Query('ShowTips', 1) and self.m_ValidShowTips:
                iActNum = oReason.Query('ActNum', 0)
            oSkill = self.m_Game.m_SkillMgr.GetSkill(iAttack, iActNum) if iActNum else None
            cl_snetwar.GS2CWStatusHP(self, oSkill, iTargetPlayer, iAttack, iActNum, iChange, iDamType, 0, 0, 0, 1, 0)
        
        self.UpdateShieldRecoverStatus()
        dMsgInfo = {
            'AID': iAttack,
            'CurVID': self.m_ID,
            'TrueChange': lstTrueChange,
            'TotalCure': lstTotalChange,
            'IsDam': False,
            'CureInfo': lstChange }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_HP_CHANGE, self, dMsgInfo)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_REVTOTALCURE, self, dMsgInfo)
        return sum(lstTotalChange)

    
    def DebugHPModifyCureFull(self):
        lstChange = []
        dChangeInfo = {
            'HPMax': DAM_USE_HP,
            'ShieldMax': DAM_USE_SHIELD,
            'ArmorMax': DAM_USE_ARMOR }
        for sAttr, iDamType in dChangeInfo.items():
            iChange = self.QueryAttr(sAttr)
            oReason = CStrReason('免死亡', None, {
                'DamType': iDamType })
            lstChange.append([
                iChange,
                oReason])
        
        self.HPModifyCure(self.m_ID, lstChange)

    
    def HPModifyDam(self, iAttack, lstChange):
        if self.IsDead() or not lstChange:
            return ([
                0,
                0,
                0], [], [])
        oGame = self.m_Game
        if iAttack:
            iCurFrame = oGame.GetFrameNum()
            self.Set('Injured%d' % iAttack, iCurFrame)
        oPart = None
        if self.m_Part:
            oPart = self.m_Game.GetObject(self.m_Part, PY_FLAG_DEAD)
        lstCurData = [
            self.Shield(),
            self.Armor(),
            self.HP()]
        lstCurPartData = [
            0,
            0,
            0] if not oPart else [
            oPart.Shield(),
            oPart.Armor(),
            oPart.HP()]
        lstOldData = lstCurData[:]
        lstTotalChange = [
            0,
            0,
            0]
        lstExcessChange = []
        lstTrueChange = []
        tDieData = None
        iShieldIdx = g_HpTypeIndex['Shield']
        iBreakShield = 0
        oAttack = oGame.GetObject(iAttack)
        iDeductionDamage = 0
        iTargetPlayer = oAttack.m_OwnerPlayerID if oAttack and oAttack.m_OwnerPlayerID else self.m_PlayerID
        iAllAbnormal = 0
        for idxChange, (iChange, oReason) in enumerate(lstChange):
            iDamType = oReason.Query('DamType', 0)
            lstExtraFactorElement = oReason.Query('ExtraFactorElement', [])
            iActNum = oReason.Query('ActNum', 0)
            oSkill = oGame.m_SkillMgr.GetSkill(iAttack, iActNum) if iActNum else None
            bHitPart = False
            if oPart:
                iHitArea = oSkill.m_Update['CurHitArea'] if oSkill and 'CurHitArea' in oSkill.m_Update else 0
                lstContainHitArea = GetContainHitArea(oPart)
                if iHitArea in lstContainHitArea:
                    bHitPart = True
            lstPredictChange = [
                0,
                0,
                0]
            iCurTotal = 0
            for idx, sAttr, iUseType in g_DamTypeSequence:
                iCur = lstCurData[idx] if not bHitPart else lstCurPartData[idx]
                iCurTotal += iCur
                if iCur:
                    if iDamType & iUseType:
                        (lstPredictChange[idx], iChange) = self.CalcRealDamage(sAttr, iDamType, lstExtraFactorElement, iChange, iCur, oAttack, oReason)
                        if not iChange:
                            break
            
            if iChange:
                iLastIndex = None
                lstData = lstOldData if not bHitPart else lstCurPartData
                for idx, iValue in enumerate(lstData):
                    if iValue > 0:
                        iLastIndex = idx
                
                if iLastIndex is not None:
                    (_, sAttr, iUseType) = g_DamTypeSequence[iLastIndex]
                    if iDamType & iUseType:
                        iChange = iChange * self.GetElementFactor(iDamType, lstExtraFactorElement, g_Attr2HPType[sAttr], oAttack, oReason) // 10000
            dMsgInfo = {
                'AID': iAttack,
                'VID': self.m_ID,
                'PredictChange': lstPredictChange,
                'ExcessChange': iChange,
                'PartTotalChange': [
                    0,
                    0,
                    0],
                'PartExcessChange': 0,
                'RS': oReason,
                'DamType': iDamType }
            if oSkill:
                dMsgInfo['Skill'] = oSkill
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_PREDICTDAM, oAttack, dMsgInfo, iSub = self.m_SubAttackMsg, oGame = oGame)
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_PREDICTDAMED, self, dMsgInfo)
            iDamType = dMsgInfo['DamType']
            if oReason.Query('DamType') & DAM_MASK_PART == DAM_TYPE_SHIELD:
                return ([], [], [])
            if 'Halt' in dMsgInfo:
                continue
            if oPart:
                oPart.OnPartDamage(self, dMsgInfo)
            lstPredictChange = dMsgInfo['PredictChange']
            iExcessChange = dMsgInfo['ExcessChange']
            lstPartTotalChange = dMsgInfo['PartTotalChange']
            iPartExcessChange = dMsgInfo['PartExcessChange']
            iDeductionDamage += (dMsgInfo['DeductionDamage'] if 'DeductionDamage' in dMsgInfo else 0)
            iChange = iExcessChange + iPartExcessChange
            if iChange:
                lstExcessChange.append((iChange, oReason))
            iRealChange = 0
            for idx, sAttr, _ in g_DamTypeSequence:
                if lstPredictChange[idx]:
                    iTrueChange = -self.TrueModify(sAttr, oAttack, -lstPredictChange[idx], iCalExcess = 1)
                    lstTotalChange[idx] += iTrueChange
                    iRealChange += iTrueChange
                if lstPartTotalChange[idx]:
                    iTrueChange = lstPartTotalChange[idx]
                    lstTotalChange[idx] += iTrueChange
                    iRealChange += iTrueChange
                lstCurData[idx] = self.__dict__['m_%s' % sAttr]
            
            if not iBreakShield and lstOldData[iShieldIdx] > 0 and lstCurData[iShieldIdx] == 0:
                iBreakShield = 1
            lstTrueChange.append((iRealChange, oReason))
            iTipDam = sum(lstPredictChange)
            iPartTipDam = sum(lstPartTotalChange)
            if lstPredictChange[g_DamTypeSequence[2][0]]:
                iTipDam += iExcessChange
            if lstPartTotalChange[g_DamTypeSequence[2][0]]:
                iPartTipDam += iPartExcessChange
            iTriggerAbnormal = self.m_EleAbnormal.TryTriggerEleAbnormal(oSkill, iTipDam, oReason) if oSkill else 0
            iAllAbnormal |= iTriggerAbnormal
            if iTargetPlayer and self.m_ValidShowTips and oReason.Query('ShowTips', 1):
                iInitDam = oReason.Query('InitDam')
                iWeaked = 1 if iInitDam > iTipDam else 0
                iLuckyHitEff = oReason.Query('LuckyHitEff', 1) if oSkill else 1
                iExInfo = oReason.Query('ExInfo', 1)
                if iExInfo is None:
                    iExInfo = 0
                if not (iExInfo & EXSHOWTIPS_ALL) and oSkill and 'ExShowTips' in oSkill.m_Collect:
                    iExShowTips = oSkill.m_Collect['ExShowTips']
                else:
                    iExShowTips = 0
                iExInfo = iExInfo | iExShowTips
                if iTipDam:
                    cl_snetwar.GS2CWStatusHP(self, oSkill, iTargetPlayer, iAttack, iActNum, iTipDam, iDamType, iTriggerAbnormal, iBreakShield, iWeaked, iLuckyHitEff, iExInfo)
                if iPartTipDam:
                    cl_snetwar.GS2CWStatusHP(self, oSkill, iTargetPlayer, iAttack, iActNum, iPartTipDam, iDamType, iTriggerAbnormal, iBreakShield, iWeaked, iLuckyHitEff, iExInfo)
            if self.m_HP < 1:
                self.SetDieFinalInfo(iTipDam + iPartTipDam, iAttack)
                tDieData = [
                    iAttack,
                    oReason]
                lstExcessChange.extend(lstChange[idxChange + 1:])
                break
        
        dMsgInfo = {
            'AID': iAttack,
            'CurVID': self.m_ID,
            'OriginAID': iAttack,
            'TrueChange': lstTrueChange,
            'ExcessChange': lstExcessChange,
            'TotalDam': lstTotalChange,
            'IsDam': True,
            'RS': oReason,
            'OldHpData': lstOldData,
            'NewHpData': lstCurData,
            'DieData': tDieData,
            'DeductionDamage': iDeductionDamage,
            'EleAbnormal': iAllAbnormal }
        oReason = lstChange[0][1]
        iActNum = oReason.Query('ActNum', 0)
        oSkill = oGame.m_SkillMgr.GetSkill(iAttack, iActNum)
        if oSkill:
            dMsgInfo['Skill'] = oSkill
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_HP_CHANGE, self, dMsgInfo)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DEALTOTALDAM, oAttack, dMsgInfo, iSub = self.m_SubAttackMsg, oGame = oGame)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_REVTOTALDAM, self, dMsgInfo)
        iExecuteType = self.Query('BeExecuted', 0)
        if iExecuteType:
            self.Set('BeExecuted', 0)
            iBreakShield = 1 if self.m_Shield > 0 else 0
            dMsgInfo['ExecutType'] = iExecuteType
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_EXECUTE, oAttack, dMsgInfo, oGame = oGame)
            cl_snetwar.GS2CWStatusHP(self, oSkill, iTargetPlayer, iAttack, iActNum, 99999900, DAM_TYPE_TRUE, 0, iBreakShield, 0, 1, 1)
            self.HPDirectModify('Shield', iAttack, -(self.m_Shield), oReason)
            self.HPDirectModify('HP', iAttack, -(self.m_HP), oReason)
        if iBreakShield:
            if self.m_FightType == WARRIOR_PET:
                sText = f'''{self.m_Game.m_ID} pet {self.m_SID} breakshield'''
                SendAlert('err', sText)
                TraceLog('err', sText)
            else:
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_BREAKSHIELD, self, dMsgInfo)
                cl_snetwar.GS2CBreakShield(self, iAttack)
        iArmorIdx = g_HpTypeIndex['Armor']
        if lstOldData[iArmorIdx] and not lstCurData[iArmorIdx]:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_BREAKARMOR, self, dMsgInfo)
            cl_snetwar.GS2CBreakArmor(self, iAttack)
        self.UpdateShieldRecoverStatus()
        if tDieData:
            self.EnterDie(*tDieData)
            self.ClearDieFinalInfo()
        return (lstTotalChange, lstTrueChange, lstExcessChange)

    
    def CalcRealDamage(self, sAttr, iDamType, lstExtraFactorElement, iChange, iHas, oAttack, oReason):
        iRealChange = iChange * self.GetElementFactor(iDamType, lstExtraFactorElement, g_Attr2HPType[sAttr], oAttack, oReason) // 10000
        if iRealChange > iHas:
            return (iHas, iChange - iChange * iHas // iRealChange)
        return (iRealChange, 0)

    
    def AddHPThreshold(self, iThreshold, iDirect, sKey, func):
        if iDirect not in self.m_ThresholdDict:
            return None
        lstHPThreshold = self.m_ThresholdDict[iDirect]
        lstHPThreshold.append((iThreshold, sKey, func))
        lstHPThreshold.sort(key = functools.cmp_to_key(CompareTuple))
        if iDirect & RADIO_ADD:
            iCheckThreshold = 0
        else:
            iCheckThreshold = 100
        if iDirect in (HPARMORSHIELD_RADIO_SUB, HPARMORSHIELD_RADIO_ADD):
            sAttr = 'HPArmorShield'
        elif iDirect & RADIO_MIX_HPARMOR == RADIO_MIX_HPARMOR:
            sAttr = 'HPArmor'
        elif iDirect & RADIO_HP:
            sAttr = 'HP'
        elif iDirect & RADIO_SHIELD:
            sAttr = 'Shield'
        elif iDirect & RADIO_ARMOR:
            sAttr = 'Armor'
        self.Remove_Call_Out('%sThreshold' % sAttr)
        self.Call_Out(Functor(self.RefreshHPThreshold, sAttr, -1, -1, iCheckThreshold, -1), 1, '%sThreshold' % sAttr)

    
    def ClearHPThreshold(self, iClearThreshold, iDirect, sClearKey):
        if iDirect not in self.m_ThresholdDict:
            return None
        lstHPThreshold = []
        for iThreshold, sKey, func in self.m_ThresholdDict[iDirect]:
            if iClearThreshold == iThreshold and sClearKey == sKey:
                continue
            lstHPThreshold.append((iThreshold, sKey, func))
        
        self.m_ThresholdDict[iDirect] = lstHPThreshold

    
    def ClearHPThresholdByKey(self, iDirect, sClearKey):
        if iDirect not in self.m_ThresholdDict:
            return None
        lstHPThreshold = []
        for iThreshold, sKey, func in self.m_ThresholdDict[iDirect]:
            if sClearKey == sKey:
                continue
            lstHPThreshold.append((iThreshold, sKey, func))
        
        self.m_ThresholdDict[iDirect] = lstHPThreshold

    
    def RefreshHPThreshold(self, sAttr, iOldVal, iNowVal, iOldRatio = -1, iNowRatio = -1, iOldMax = 0):
        self.Remove_Call_Out('%sThreshold' % sAttr)
        if iNowVal == -1:
            iNowVal = self.GetThresholdNowVal(sAttr)
        iMax = self.GetThresholdMaxVal(sAttr)
        if iMax == 0:
            return None
        if iOldRatio == -1:
            if iOldMax <= 0:
                iOldMax = iMax
            iOldRatio = iOldVal * 100 // iOldMax
        if iNowRatio == -1:
            iNowRatio = iNowVal * 100 // iMax
        iAttrDirect = g_ThresholdDirect[sAttr]
        if iOldRatio > iNowRatio:
            iDirect = iAttrDirect | RADIO_SUB
        else:
            iDirect = iAttrDirect | RADIO_ADD
        for iThreshold, _, func in self.m_ThresholdDict[iDirect]:
            if iDirect & RADIO_ADD:
                if iOldRatio >= iThreshold or iNowRatio < iThreshold:
                    continue
                continue
            if iDirect & RADIO_SUB:
                if iNowRatio > iThreshold or iOldRatio <= iThreshold:
                    continue
                continue
            func(self, {
                'Threshold': iThreshold,
                'Direct': iDirect,
                'OldVal': iOldVal,
                'NowVal': iNowVal })
        
        iRecover = self.GetThresholdRecoverVal(sAttr)
        if not iRecover:
            return None
        for iThreshold, _, _ in self.m_ThresholdDict[iAttrDirect | RADIO_ADD]:
            if iNowRatio >= iThreshold:
                continue
            iThresholdVal = iThreshold * iMax // 100
            iDelayFrame = (iThresholdVal - iNowVal) // iRecover + 2
            if sAttr in ('Shield', 'HPArmorShield'):
                iHaltStartFrame = self.GetShieldRecoverHaltFrame()
                if iHaltStartFrame:
                    iDelayFrame += self.GetShieldRecoverFrame() + self.m_Game.GetFrameNum() - iHaltStartFrame
            if not iDelayFrame:
                iDelayFrame = GAME_FRAME
            self.Call_Out(Functor(self.RefreshHPThreshold, sAttr, iNowVal, -1), iDelayFrame, '%sThreshold' % sAttr)
        

    
    def TriggerMixThresholdChange(self, sAttr, iOldVal, iNowVal):
        if sAttr not in g_MixThresholdInfo:
            return None
        for sPatAttr, iMixDirect, sMixAttr in g_MixThresholdInfo[sAttr]:
            if iOldVal > iNowVal:
                iDirect = iMixDirect | RADIO_SUB
            else:
                iDirect = iMixDirect | RADIO_ADD
            if iDirect not in self.m_ThresholdDict or not self.m_ThresholdDict[iDirect]:
                continue
            iVal = self.GetThresholdNowVal(sPatAttr)
            iMixOldVal = iVal + iOldVal
            iMixNowVal = iVal + iNowVal
            iMixMaxVal = self.GetThresholdMaxVal(sMixAttr)
            iMixOldRat = iMixOldVal * 100 // iMixMaxVal
            iMixNewRat = iMixNowVal * 100 // iMixMaxVal
            self.RefreshHPThreshold(sMixAttr, iMixOldVal, iMixNowVal, iMixOldRat, iMixNewRat)
        

    
    def GetThresholdMaxVal(self, sAttr):
        if sAttr == 'HPArmor':
            return self.QueryAttr('HPMax') + self.QueryAttr('ArmorMax')
        if sAttr == 'HPArmorShield':
            return self.QueryAttr('HPMax') + self.QueryAttr('ArmorMax') + self.QueryAttr('ShieldMax')
        return self.QueryAttr('%sMax' % sAttr)

    
    def GetThresholdNowVal(self, sAttr):
        if sAttr == 'HPArmor':
            return self.HP() + self.Armor()
        if sAttr == 'HPShield':
            return self.HP() + self.Shield()
        if sAttr == 'ArmorShield':
            return self.Armor() + self.Shield()
        if sAttr == 'HPArmorShield':
            return self.HP() + self.Armor() + self.Shield()
        return getattr(self, sAttr)()

    
    def GetThresholdRecoverVal(self, sAttr):
        if sAttr == 'HPArmor':
            return self.QueryAttr('RHP')
        if sAttr == 'Armor':
            return 0
        if sAttr == 'HP':
            return self.QueryAttr('RHP')
        if sAttr == 'Shield':
            if len(self.Query('StopShieldRecoverInfo', { })) > 1:
                return 0
            return PerSecond2PerFrame(self.QueryAttr('ShieldMax') * self.RShield() // 100)
        if sAttr == 'HPArmorShield':
            iRecover = self.QueryAttr('RHP')
            if len(self.Query('StopShieldRecoverInfo', { })) <= 1:
                iRecover += PerSecond2PerFrame(self.QueryAttr('ShieldMax') * self.RShield() // 100)
            return iRecover

    
    def AddRefreshAttr(self, sAttr):
        
        def _Refresh(oAttr, obj):
            oAttr = oAttr._Refresh(obj)
            if oAttr and obj:
                iSub = BASIC_PROP_NAME[oAttr.m_Attr][0]
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ATTR_CHANGE, obj, { }, iSub = iSub)

        if sAttr not in self.m_PrivateAttr:
            return None
        oAttr = self.m_PrivateAttr[sAttr]
        if sAttr not in self.m_NeedMonitorAttrDict:
            self.m_NeedMonitorAttrDict[sAttr] = 0
        self.m_NeedMonitorAttrDict[sAttr] += 1
        if self.m_NeedMonitorAttrDict[sAttr] == 1:
            oAttr._Refresh = oAttr.Refresh
            oAttr.Refresh = types.MethodType(_Refresh, oAttr)

    
    def DelRefreshAttr(self, sAttr):
        if sAttr not in self.m_PrivateAttr or sAttr not in self.m_NeedMonitorAttrDict:
            return None
        self.m_NeedMonitorAttrDict[sAttr] -= 1
        if self.m_NeedMonitorAttrDict[sAttr] == 0:
            oAttr = self.m_PrivateAttr[sAttr]
            oAttr.Refresh = oAttr._Refresh
            del oAttr.Refresh
            del oAttr._Refresh
            oAttr.Refresh(self)

    
    def ClearDiePriority(self, sReason):
        dDiePriority = self.Query('DiePriority', None)
        if not dDiePriority:
            return None
        iPriority = dDiePriority.pop(sReason, 0)
        iCurMaxPriority = self.Query('MaxDiePriority', 0)
        if iPriority == iCurMaxPriority:
            if not dDiePriority:
                self.Delete('DiePriority')
                self.Delete('MaxDiePriority')
            else:
                iNewMaxPriority = max(dDiePriority.values())
                self.Set('MaxDiePriority', iNewMaxPriority)

    
    def SetDiePriority(self, iPriority, sReason):
        if iPriority not in DIE_PRIORITY:
            return None
        dDiePriority = self.SetDefault('DiePriority', { })
        dDiePriority[sReason] = iPriority
        iCurMaxPriority = self.Query('MaxDiePriority', 0)
        if iCurMaxPriority < iPriority:
            self.Set('MaxDiePriority', iPriority)

    
    def DiePriorityType(self):
        iCurMaxPriority = self.Query('MaxDiePriority', 0)
        if not iCurMaxPriority:
            return DIE_PRIORITY_TYPE_NONE
        return DIE_PRIORITY[iCurMaxPriority]

    
    def AddExecuteType(self, iType):
        iCurType = self.Query('BeExecuted', 0)
        self.Set('BeExecuted', iCurType | iType)

    
    def EnterDie(self, iAttack, oReason):
        if self.IsDead():
            return None
        dMsgInfo = {
            'VID': self.m_ID,
            'AID': iAttack,
            'RS': oReason }
        if iAttack:
            oSkill = self.m_Game.m_SkillMgr.GetSkill(iAttack, oReason.Query('ActNum', 0))
            if oSkill:
                dMsgInfo['Skill'] = oSkill
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DIE_BEFORE_MAIN, self, dMsgInfo)
        if self.m_HP > 0:
            return None
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DIE_BEFORE, self, dMsgInfo)
        iDiePriorityType = self.DiePriorityType()
        if iDiePriorityType == DIE_PRIORITY_TYPE_NONE:
            if 'Halt' in dMsgInfo:
                return None
            if self.m_HP > 0:
                return None
        if iDiePriorityType == DIE_PRIORITY_TYPE_NO_DIE:
            return None
        if self.m_FightType & CTRLWARRIOR_MASK:
            if self.Query('DebugStatus') & DEBUG_STATUS_NODIE == DEBUG_STATUS_NODIE and self.DiePriorityType() != DIE_PRIORITY_TYPE_DIE:
                self.DebugHPModifyCureFull()
            else:
                oDieElement = self.m_Game.m_WarMgr.GetComponent('PVEDieElement')
                if oDieElement:
                    if self.m_FightType & WARRIOR_HERO:
                        oDieElement.HeroEnterDie(self, iAttack, oReason)
                    elif self.m_FightType & WARRIOR_SERVANT:
                        oDieElement.ServantEnterDie(self, iAttack, oReason)
                    elif self.m_FightType & WARRIOR_PET:
                        oDieElement.PetEnterDie(self, iAttack, oReason)
                    else:
                        oDieElement.MonsterEnterDie(self, iAttack, oReason)
                else:
                    self.Die(iAttack, oReason)
                    self.RealDie()
        else:
            self.Die(iAttack, oReason)

    
    def ResetByDie(self):
        if self.m_Agent:
            self.m_Agent.HaltPerform(self.m_Agent)
            self.m_Agent.PauseAgent('Die')
        self.Stop()
        self.StopShieldRecover('Die')
        self.StopEnergyRecover('Die')

    
    def Stop(self):
        if self.m_Agent:
            self.m_Agent.Stop()
        super().Stop()

    
    def DieDisablePassive(self):
        lstPerform = self.GetPerformSIDByType(PF_TYPE_PASSIVE)
        lstDisable = []
        for iPerform in lstPerform:
            oPerform = self.GetPerform(iPerform)
            if oPerform.m_Enable and oPerform.m_DieDisable:
                oPerform.Disable(self)
                lstDisable.append(iPerform)
        
        if lstDisable:
            self.m_DieDisablePassive = lstDisable

    
    def DieClearEffect(self):
        for oState in self.m_State.Values():
            if oState.m_DieRemove:
                self.m_State.RemoveItem(oState.m_ID)
        
        self.DieDisablePassive()
        cl_action.HaltAllCasting(self, 'Die')
        self.ClearWaitSkill()
        self.Forbid(cl_forbid.DIE_RULE, '死亡禁止')

    
    def Die(self, iAttack, oReason):
        if self.IsDead():
            return None
        dMsgInfo = {
            'VID': self.m_ID,
            'AID': iAttack,
            'RS': oReason,
            'FinalDam': self.m_FinalDam }
        oGame = self.m_Game
        if iAttack:
            oSkill = oGame.m_SkillMgr.GetSkill(iAttack, oReason.Query('ActNum', 0))
            if oSkill:
                dMsgInfo['Skill'] = oSkill
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DIE_EXECUTE_BEFORE, self, dMsgInfo)
        self.m_Dead = DEAD_FLAG_DIED
        self.m_DeadReason = oReason
        self.ResetByDie()
        oGame.SetPyFlag(self.m_ID, PY_FLAG_DIED, 1)
        if self.m_FightType & CTRLWARRIOR_MASK and self.m_PhyModel:
            self.m_PhyModel.SetCtrlFlag(CTRL_FLAG_FOR_DEAD, 0)
        if iAttack:
            oAttack = oGame.GetObject(iAttack)
            self.SendKillMsg(oAttack, dMsgInfo)
        self.DieClearEffect()
        self.GS2CPropChange('Dead')
        cl_snetwar.GS2CDie(self, self.m_FinalAttack, self.m_FinalDam)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DIE, self, dMsgInfo, iSub = self.m_Side)
        if self.m_Dead != DEAD_FLAG_DIED:
            WarobjLog.Alert('%d %d die err hp:%s dead:%s %s' % (oGame.m_ID, self.m_PlayerID, self.m_HP, self.m_Dead, oReason))
            return None
        if self.m_FollowDieObjs:
            dFollowDie = self.m_FollowDieObjs
            self.m_FollowDieObjs = { }
            for iID in dFollowDie:
                oFollowDieObj = oGame.GetObject(iID, PY_FLAG_DEAD)
                if oFollowDieObj:
                    oReason = cl_object.reason.CStrReason('FollowDie', None, {
                        'DamType': DAM_TYPE_SCENE | DAM_TYPE_TRUE | DAM_USE_HP })
                    oFollowDieObj.HPDirectModify('HP', iAttack, -oFollowDieObj.HP(), oReason)
                    if oFollowDieObj.m_Part and not oFollowDieObj.IsDead():
                        oFollowDieObj.HPDirectModify('HP', iAttack, -oFollowDieObj.HP(), oReason)
            
        self.DieRemove()

    
    def DieRemove(self):
        if not self.m_Delete:
            return None
        iDelay = max(1, self.m_RemoveDelay)
        self.Call_Out(Functor(self.Remove, 'DieRemove'), iDelay, 'DieRemove')

    
    def SetDelete(self, iFlag):
        self.m_Delete = iFlag

    
    def SetExtraModelDistance(self, fDistance):
        self.m_ExtraModelDistance = fDistance

    
    def SetHeightOffset(self, iValue):
        self.m_HeightOffset = iValue

    
    def SendKillMsg(self, oAttack, dMsgInfo):
        if self.Query('Killed%d' % self.m_ID):
            return None
        self.Set('Killed%d' % self.m_ID, 1)
        oGame = self.m_Game
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_KILL, oAttack, dMsgInfo, iSub = self.m_SubAttackMsg, oGame = oGame)
        if oAttack and oAttack.m_FightType & SEND_ASSISTKILL_FIGHTTYPE:
            oScene = oGame.m_SceneMgr.GetScene(self.m_Scene)
            lstHero = oScene.GetHeros() if oScene else []
            iCurFrame = oGame.GetFrameNum()
            for iHero in lstHero:
                oHero = oGame.GetObject(iHero)
                if not oHero or oHero.IsRealDied():
                    continue
                iLastFrame = self.Query('Injured%d' % iHero)
                if not iLastFrame or iLastFrame + self.m_AssistKillFrame < iCurFrame:
                    continue
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ASSISTKILL, oHero, dMsgInfo, iSub = self.m_SubAttackMsg, oGame = oGame)
            

    
    def DyingClearEffect(self):
        for oState in self.m_State.Values():
            if oState.m_DieRemove:
                self.m_State.RemoveItem(oState.m_ID)
        
        for oState in self.m_State.Values():
            if oState.m_DyingRemove:
                self.m_State.RemoveItem(oState.m_ID)
        
        self.DieDisablePassive()
        cl_action.HaltAllCasting(self, 'Dying')
        self.Forbid(cl_forbid.DYING_RULE, '濒死禁止')

    
    def Dying(self, iAttack, oReason, dDyingInfo = None):
        if dDyingInfo is None:
            dDyingInfo = { }
        self.ResetByDie()
        oGame = self.m_Game
        self.m_Dead = DEAD_FLAG_DYING
        oGame.SetPyFlag(self.m_ID, PY_FLAG_DYING, 1)
        if self.m_FightType & CTRLWARRIOR_MASK:
            self.m_PhyModel.SetCtrlFlag(CTRL_FLAG_FOR_DEAD, 0)
            if self.m_FightType == WARRIOR_HERO:
                if not self.m_DyingModel:
                    (fRadius, fHeight) = cl_modeldefine.GetModelDefine(self.m_Shape, 'Physx')
                    dParam = {
                        'Radius': fRadius,
                        'Height': fHeight }
                    self.m_DyingModel = cl_engphyobj.CreatePhyModel(self, PAMOD_TYPE_DYING, PXLAYER_PLAYER_DYING, dParam)
                    self.m_DyingModel.SetCtrlFlag(CTRL_FLAG_HERO_DYING, 0)
                else:
                    self.m_DyingModel.SetCtrlFlag(CTRL_FLAG_SIM, 1)
        dMsgInfo = {
            'VID': self.m_ID,
            'AID': iAttack,
            'RS': oReason }
        if iAttack:
            oAttack = oGame.GetObject(iAttack)
            oSkill = oGame.m_SkillMgr.GetSkill(iAttack, oReason.Query('ActNum', 0))
            if oSkill:
                dMsgInfo['Skill'] = oSkill
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_KILL, oAttack, dMsgInfo, iSub = self.m_SubAttackMsg, oGame = self.m_Game)
        self.DyingClearEffect()
        self.GS2CPropChange('Dead')
        cl_snetwar.GS2CDie(self, self.m_FinalAttack, self.m_FinalDam)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DIE, self, dMsgInfo, iSub = self.m_Side)
        if self.m_Dead != DEAD_FLAG_DYING:
            WarobjLog.Alert('%d %d dying err hp:%s dead:%s %s' % (oGame.m_ID, self.m_PlayerID, self.m_HP, self.m_Dead, oReason))
            return None
        self.OnDying(dDyingInfo)
        if self.m_FightType & WARRIOR_SERVANT:
            dPlayer = {
                self.m_OwnerPlayerID: 1 }
            cl_notify.SendCommonNotify(oGame, dPlayer, 2365, {
                '$name': self.Name() })
        else:
            dPlayer = { }
            dPlayer.update(oGame.GetRealPlayers())
            dPlayer.pop(self.m_PlayerID, 0)
            cl_notify.SendCommonNotify(oGame, dPlayer, 2101, {
                '$$playername': self.Name() })
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DYING, self, dMsgInfo)

    
    def OnDying(self, dDyingInfo):
        iStateCount = dDyingInfo.get('StateCount', 1)
        oState = cl_state.AddState(self, STATE_DYING, STATE_TIME_FOREVER, 0, {
            'AID': self.m_ID,
            'RS': CStrReason('dying') })
        oState.SetMaxCount(self, iStateCount)
        oState.Enable(self)

    
    def GetDyingSecond(self):
        oState = self.m_State.GetItemBySID(STATE_DYING)
        if oState:
            return oState.m_MaxCount - oState.GetCount()
        return 0

    
    def RealDieClearEffect(self):
        oState = self.m_State.GetItemBySID(STATE_DYING)
        if oState:
            self.m_State.RemoveItem(oState.m_ID)
        self.DieClearEffect()

    
    def RealDie(self, oReason = None):
        self.m_Dead = DEAD_FLAG_REAL
        oGame = self.m_Game
        self.Stop()
        oGame.SetPyFlag(self.m_ID, PY_FLAG_DYING, 0)
        oGame.SetPyFlag(self.m_ID, PY_FLAG_DIED, 1)
        self.RealDieClearEffect()
        cl_snetwar.GS2CRealDie(self)
        self.GS2CPropChange('Dead')
        dMsgInfo = {
            'VID': self.m_ID,
            'RS': oReason }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DIEDIST, self, dMsgInfo)

    
    def RelifeClearEffect(self):
        oState = self.m_State.GetItemBySID(STATE_DYING)
        if oState:
            self.m_State.RemoveItem(oState.m_ID)

    
    def Relife(self, dReason, dRelifeInfo = None):
        if dRelifeInfo is None:
            dRelifeInfo = {
                'HP': self.QueryAttr('HPMax'),
                'Shield': self.QueryAttr('ShieldMax'),
                'Armor': self.QueryAttr('ArmorMax') }
        iDead = self.m_Dead
        self.ClearDieFinalInfo()
        oGame = self.m_Game
        iPlayerID = self.m_PlayerID
        if iPlayerID:
            WarobjLog.Info('%d %d relife %s' % (oGame.m_ID, iPlayerID, dReason))
        oGame.SetPyFlag(self.m_ID, PY_FLAG_DEAD, 0)
        if self.m_FightType & CTRLWARRIOR_MASK and self.m_PhyModel:
            self.m_PhyModel.SetCtrlFlag(CTRL_FLAG_FOR_DEAD, 1)
            if self.m_FightType == WARRIOR_HERO and self.m_DyingModel:
                self.m_DyingModel.SetCtrlFlag(CTRL_FLAG_SIM, 0)
        self.RelifeClearEffect()
        self.m_Dead = 0
        self.GS2CPropChange('Dead')
        cl_snetwar.GS2CRelife(self, dReason['Type'])
        for sAttr, iValue in dRelifeInfo.items():
            self.TrueModify(sAttr, None, iValue - self.__dict__['m_%s' % sAttr])
        
        dReason['ShowTips'] = 0
        oReason = CStrReason('复活', dData = dReason)
        iAID = dReason['AID'] if 'AID' in dReason else self.m_ID
        dMsgInfo = {
            'VID': self.m_ID,
            'AID': iAID,
            'RS': oReason,
            'Hero': self.m_ID,
            'Dead': iDead }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_RELIFE, self, dMsgInfo)
        self.OnRelife()
        if iPlayerID and 'CloseNotify' not in dReason:
            oAttack = oGame.GetObject(iAID)
            if iAID == self.m_ID or not oAttack:
                cl_notify.SendCommonNotify(oGame, oGame.GetRealPlayers(), 2102, {
                    '$$playername': self.Name() })
            elif oAttack and oAttack.m_FightType & WARRIOR_SERVANT:
                cl_notify.SendCommonNotify(oGame, oGame.GetRealPlayers(), 2142, {
                    '$name': oAttack.Name(),
                    '$$playername': self.Name() })
            else:
                cl_notify.SendCommonNotify(oGame, oGame.GetRealPlayers(), 2104, {
                    '$$playername1': oAttack.Name(),
                    '$$playername2': self.Name() })

    
    def RelifeEnablePassive(self):
        if self.m_DieDisablePassive:
            for iPerform in self.m_DieDisablePassive:
                oPerform = self.GetPerform(iPerform)
                if oPerform:
                    oPerform.Enable(self)
            
            self.m_DieDisablePassive = None

    
    def OnRelife(self):
        if self.m_Agent:
            self.m_Agent.ResumeAgent('Die')
        self.RelifeEnablePassive()
        self.StartShieldRecover('Die')
        self.StartEnergyRecover('Die')
        self.UnForbid(cl_forbid.DIE_RULE, '死亡禁止')
        self.UnForbid(cl_forbid.DYING_RULE, '濒死禁止')
        if self.m_FightType & WARRIOR_HERO == WARRIOR_HERO:
            iTime = int(self.m_Game.GetWarData().GetConfig().get('WudiTime', 300))
            oState = cl_state.AddState(self, STATE_RELIFE, STATE_TIME_LIMIT, Time2Frame(iTime), {
                'AID': self.m_ID,
                'RS': CStrReason('复活') })
            if oState:
                oState.Enable(self)
            oGame = self.m_Game
            oScene = oGame.m_SceneMgr.GetScene(self.m_Scene)
            if not oScene:
                return None
            for iHero in oScene.GetHeros():
                if iHero == self.m_ID:
                    continue
                oHero = oGame.GetObject(iHero, PY_FLAG_DEAD)
                if not oHero:
                    continue
                if oHero.m_State.GetItemBySID(STATE_UNDER_ATTACK):
                    oState = cl_state.AddState(self, STATE_UNDER_ATTACK, STATE_TIME_FOREVER, 0, {
                        'AID': self.m_ID,
                        'RS': cl_object.reason.CStrReason('Relife') })
                    if oState:
                        oState.Enable(oHero)
                    break
            

    
    def AddRelifeInfo(self, iType, sKey, iTime, iTimes, iPriority, dRatio = None, iMaxTimes = 0):
        if iType not in TYPE_RELIFE_ALL:
            return None
        dInfo = self.Query('RelifeInfo', { })
        dType = dInfo.setdefault(iType, { })
        if sKey in dType:
            return None
        if not iMaxTimes:
            iMaxTimes = iTimes
        dType[sKey] = [
            iTime,
            iTimes,
            iMaxTimes,
            iPriority]
        if dRatio:
            dRelifeRatio = self.SetDefault('RelifeRatio', { })
            dRelifeRatio[(iType, sKey)] = dRatio
        self.Set('RelifeInfo', dInfo)

    
    def ClearRelifeInfo(self, iType, sKey):
        if iType not in TYPE_RELIFE_ALL:
            return None
        dInfo = self.Query('RelifeInfo', { })
        if iType not in dInfo:
            return None
        if sKey not in dInfo[iType]:
            return None
        dInfo[iType].pop(sKey)
        if not dInfo[iType]:
            dInfo.pop(iType)
        self.Set('RelifeInfo', dInfo)

    
    def GetFirstRelifeInfo(self):
        iGetType = 0
        sGetKey = ''
        iGetTime = 0
        dRelifeInfo = self.Query('RelifeInfo', { })
        sSpecificRelife = self.Query('SpecificRelife')
        for iType, dType in sorted(dRelifeInfo.items(), key = (lambda item: g_RelifePriority[item[0]])):
            iGetPriority = 16777215
            for sKey, (iTime, iTimes, iMaxTimes, iPriority) in dType.items():
                if sSpecificRelife and sKey != sSpecificRelife:
                    continue
                if iTimes > 0 and iPriority < iGetPriority:
                    iGetType = iType
                    sGetKey = sKey
                    iGetTime = iTime
                    iGetPriority = iPriority
            
            if iGetType:
                break
        
        return (iGetType, sGetKey, iGetTime)

    
    def GetRelifeTimes(self, iType, sKey):
        if iType not in TYPE_RELIFE_ALL:
            return 0
        dInfo = self.Query('RelifeInfo', { })
        if iType not in dInfo:
            return 0
        if sKey not in dInfo[iType]:
            return 0
        return dInfo[iType][sKey][1]

    
    def GetRelifeTimesAndMaxTimesByType(self, iType):
        if iType not in TYPE_RELIFE_ALL:
            return (0, 0)
        dInfo = self.Query('RelifeInfo', { })
        if iType not in dInfo:
            return (0, 0)
        iTimesSum = 0
        iMaxTimesSum = 0
        for tInfo in dInfo[iType].values():
            iTimesSum += tInfo[1]
            iMaxTimesSum += tInfo[2]
        
        return (iTimesSum, iMaxTimesSum)

    
    def CostRelifeTimes(self, iType, sKey):
        if iType not in TYPE_RELIFE_ALL:
            raise Exception('cost relife times type error')
        dInfo = self.Query('RelifeInfo', { })
        if iType not in dInfo:
            raise Exception('cost relife times type error')
        if sKey not in dInfo[iType]:
            raise Exception('cost relife times key error')
        if dInfo[iType][sKey][1] <= 0:
            raise Exception('cost relife times times error')
        dInfo[iType][sKey][1] -= 1
        self.Set('RelifeInfo', dInfo)
        dMsgInfo = {
            'Type': iType,
            'Key': sKey,
            'LeftTimes': dInfo[iType][sKey][1] }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_COSTRELIFES, self, dMsgInfo)

    
    def SaveRelifeInfoByType(self, iType):
        dInfo = self.Query('RelifeInfo', { })
        if iType in dInfo:
            return cl_only.DeepCopy(dInfo[iType])
        return { }

    
    def LoadRelifeInfoByType(self, iType, dTypeInfo):
        if not dTypeInfo:
            return None
        dInfo = self.SetDefault('RelifeInfo', { })
        dInfo[iType] = dTypeInfo

    
    def Forbid(self, iRule, sReason):
        dForbidRule = self.m_ForbidRuleInfo
        if iRule not in dForbidRule:
            dForbidRule[iRule] = { }
        if sReason in dForbidRule[iRule]:
            return None
        dForbidRule[iRule][sReason] = 1
        dForbidType = self.m_ForbidTypeInfo
        dForbid = cl_forbid.GetRule2Forbid(iRule)
        for iType in dForbid:
            if iType not in dForbidType:
                dForbidType[iType] = 1
                continue
            dForbidType[iType] += 1
        
        self.OnForbid(iRule, dForbid, sReason)

    
    def OnForbid(self, iRule, dForbid, sReason):
        if FORBID_SHIELDRECOVER in dForbid:
            self.StopShieldRecover('Forbid-%d.%s' % (iRule, sReason))

    
    def IsForbid(self, iType, dPassRule = None, iWeapon = 0, iCache = 0):
        if dPassRule:
            for iRule in self.m_ForbidRuleInfo:
                if iRule in dPassRule:
                    continue
                dForbid = cl_forbid.GetRule2Forbid(iRule)
                if iType in dForbid:
                    return 1
            
        elif iType in self.m_ForbidTypeInfo:
            return 1
        return 0

    
    def HasRule(self, iRule):
        return iRule in self.m_ForbidRuleInfo

    
    def UnForbid(self, iRule, sReason):
        dForbidRule = self.m_ForbidRuleInfo
        if iRule not in dForbidRule:
            return None
        if sReason not in dForbidRule[iRule]:
            return None
        dForbidRule[iRule].pop(sReason)
        if not dForbidRule[iRule]:
            dForbidRule.pop(iRule)
        dForbidType = self.m_ForbidTypeInfo
        dForbid = cl_forbid.GetRule2Forbid(iRule)
        for iType in dForbid:
            if dForbidType[iType] > 1:
                dForbidType[iType] -= 1
                continue
            dForbidType.pop(iType)
        
        self.OnUnForbid(iRule, dForbid, sReason)

    
    def OnUnForbid(self, iRule, dForbid, sReason):
        if FORBID_SHIELDRECOVER in dForbid:
            self.StartShieldRecover('Forbid-%d.%s' % (iRule, sReason))

    
    def StartCastingSkill(self, oSkill, lstEndFunc):
        iActNum = oSkill.m_Base['ActNum']
        if iActNum in self.m_CastingSkill:
            return None
        self.m_CastingSkill[oSkill.m_Base['ActNum']] = {
            'Weapon': oSkill.m_Base['Weapon'],
            'pfid': oSkill.m_Base['pfid'],
            'EndFunc': lstEndFunc }
        cl_action.CastingForbid(self, oSkill)

    
    def OverCastingSkill(self, oSkill):
        iActNum = oSkill.m_Base['ActNum']
        if iActNum in self.m_CastingSkill:
            dInfo = self.m_CastingSkill.pop(iActNum)
            for func in dInfo['EndFunc']:
                func(self)
            

    
    def GetCastingByPF(self, iPerformSID, iWeapon = 0):
        for dCasting in self.m_CastingSkill.values():
            if not dCasting['pfid'] == iPerformSID or not iWeapon:
                if dCasting['Weapon'] == iWeapon:
                    return dCasting
        
        return { }

    
    def StartBackSwingSkill(self, oSkill, iFrame):
        iFrame = self.GetChangeSpeedDelayFrame(iFrame)
        self.m_BackSwingSkill[oSkill.m_Base['pfid']] = self.m_Game.GetFrameNum() + iFrame

    
    def BackSwingChangeSpeed(self, sOldKey, dFrameShaft):
        if not self.m_BackSwingSkill:
            return None
        iNowFrameNum = self.m_Game.GetFrameNum()
        dBackSwing = { }
        iBackSwing = 999999
        for iPerformSID, iOldBackSwingNum in self.m_BackSwingSkill.items():
            if iNowFrameNum >= iOldBackSwingNum:
                continue
            iNewBackSwing = self.GetDelayFrameOnChangeSpeed(iOldBackSwingNum, sOldKey, dFrameShaft)
            if iBackSwing > iNewBackSwing:
                iBackSwing = iNewBackSwing
            dBackSwing[iPerformSID] = iNewBackSwing + iNowFrameNum
        
        oAgent = self.m_Agent
        if oAgent:
            oAgent.m_GameSpace.CallDelayUpdate(oAgent, iBackSwing + 1)
        self.m_BackSwingSkill = dBackSwing

    
    def CheckCastingAndBackSwingByPF(self, iPerformSID):
        if iPerformSID in self.m_BackSwingSkill:
            if self.m_Game.GetFrameNum() >= self.m_BackSwingSkill[iPerformSID]:
                self.m_BackSwingSkill.pop(iPerformSID)
            else:
                return 1
        if self.GetCastingByPF(iPerformSID):
            return 1
        return 0

    
    def GetBackSwingRemainingFrame(self, iPerformSID):
        if iPerformSID in self.m_BackSwingSkill:
            return max(0, self.m_BackSwingSkill[iPerformSID] - self.m_Game.GetFrameNum())
        return 0

    
    def GetAllCasting(self):
        return list(self.m_CastingSkill.items())

    
    def SetCastingEndFunc(self, oSkill, func):
        iActNum = oSkill.m_Base['ActNum']
        if iActNum in self.m_CastingSkill:
            dCasting = self.m_CastingSkill[iActNum]
            dCasting['EndFunc'].append(func)

    
    def GetThumped(self, dData, iProb = 0, iClient = 1):
        return 0

    
    def GetKnockedBack(self, dData, iProb):
        return 0

    
    def GetDamTypeByPart(self, iHitPart):
        dHitPartToType = GetGlobalHitPartToType()
        if iHitPart in dHitPartToType:
            return dHitPartToType[iHitPart]
        return 0

    
    def GetDamamgePartType(self, iHitPart, iAttack):
        if iHitPart == MONSTER_PART_SHIELD:
            for iShieldState in STATE_SHIELD_LIST:
                if self.m_State.GetItemBySID(iShieldState):
                    break
            else:
                iHitPart = MONSTER_PART_UNTAGGED
        elif iHitPart == MONSTER_PART_SECKILL and not (self.QueryBitAttr('LogicKey') & FIGHT3_KEY_IGNELBEEXECUTED):
            oState = self.m_State.GetItemBySource(STATE_SECKILL, iAttack)
            if oState:
                self.AddExecuteType(EXECUTETYPE_PART_SECKILL)
            else:
                iHitPart = MONSTER_PART_UNTAGGED
        if self.m_State.GetItemBySID(STATE_WEAKER):
            iHitPart = MONSTER_PART_WEAKNESS
        iDamPartType = self.GetDamTypeByPart(iHitPart)
        return iDamPartType

    
    def CalLuckyHitEff(self, dData):
        iLuckyHit = dData['LuckyHit']
        if iLuckyHit <= 0:
            return (1, 0)
        iMaxLuckyHit = dData['MaxLuckyHit'] if 'MaxLuckyHit' in dData else 0
        if iMaxLuckyHit > 0 and iLuckyHit > iMaxLuckyHit:
            iLuckyHit = iMaxLuckyHit
        iBaseRatio = iLuckyHit // 100 + 1
        iNextRatioProb = iLuckyHit % 100
        iLuckHitEff = iBaseRatio
        if self.m_Game.Random(100) < iNextRatioProb:
            iLuckHitEff = iBaseRatio + 1
        return (iLuckHitEff, iLuckyHit)

    
    def ChangeDamageByPartType(self, iDam, iDamType, dDamage):
        iDamPartType = iDamType & DAM_MASK_PART
        if iDamPartType == DAM_TYPE_WEAKNESS and 'CrazyEff' in dDamage and 'ForbidCrazy' not in dDamage:
            iDam = iDam * dDamage['CrazyEff'] // 10000
        elif iDamPartType == DAM_TYPE_HARDNESS and self.HasAttr('HardEff'):
            iDam = iDam * self.QueryAttr('HardEff') // 10000
        return iDam

    
    def CheckIgnoreDam(self, iAttack, dInfo):
        if self.QueryBitAttr('SpecialKey') & FIGHT_KEY_IGNOREDAMAGE:
            iActNum = dInfo['RS'].Query('ActNum', 0)
            oSkill = self.m_Game.m_SkillMgr.GetSkill(iAttack, iActNum) if iActNum else None
            self.GS2CImmunity(oSkill, iAttack, iActNum, IMMUNITY_WUDI)
            return 1
        return 0

    
    def ReceiveAttack(self, iAttack, oSkill, bExplosion, iSubTrajectory = 0):
        if self.IsDead():
            return 0
        dVictim = oSkill.m_Update[self.m_ID]
        dVictim['FlowDam'] = []
        dVictim['CurVID'] = self.m_ID
        dVictim['DamFactor'] = {
            OBJ_VICTIM: { },
            OBJ_ATTACK: { } }
        if 'CurHitPos' in oSkill.m_Update:
            dVictim['CurHitPos'] = oSkill.m_Update['CurHitPos']
        dData = {
            'AID': iAttack,
            'Skill': oSkill }
        dData.update(dVictim)
        oAttack = self.m_Game.GetObject(iAttack)
        if not iSubTrajectory:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_MAIN_ATTACK, oAttack, dData, iSub = self.m_SubAttackMsg, oGame = self.m_Game)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ATTACK, oAttack, dData, iSub = self.m_SubAttackMsg, oGame = self.m_Game)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ATTACKED, self, dData)
        if bExplosion:
            lstMainDam = dData['MainDam']
            for index, (_, oReason) in enumerate(lstMainDam):
                lstMainDam[index][1] = oReason.ExtInfo({
                    'Explosion': True })
            
            dData['RS'] = dData['RS'].ExtInfo({
                'Explosion': True })
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ATTACKPF, oAttack, dData, iSub = self.m_SubAttackMsg, oGame = self.m_Game)
        dVictim['RS'] = dData['RS']
        if self.IsIgnoreAtt():
            self.GS2CImmunity(oSkill, iAttack, oSkill.m_Base['ActNum'], IMMUNITY_WUDI)
            return 0
        self.GetThumped(dData)
        (dVictim['LuckyHitEff'], dVictim['LuckyHit']) = self.CalLuckyHitEff(dData)
        dVictim['Skill'] = oSkill
        iHP = self.ReceiveDamage(iAttack, dVictim)
        return iHP

    
    def ReceivePerform(self, iAttack, oSkill):
        if self.IsDead():
            return 0
        dVictim = oSkill.m_Update[self.m_ID]
        dVictim['FlowDam'] = []
        dVictim['CurVID'] = self.m_ID
        dVictim['DamFactor'] = {
            OBJ_VICTIM: { },
            OBJ_ATTACK: { } }
        if 'CurHitPos' in oSkill.m_Update:
            dVictim['CurHitPos'] = oSkill.m_Update['CurHitPos']
        dData = {
            'AID': iAttack,
            'Skill': oSkill }
        dData.update(dVictim)
        oAttack = self.m_Game.GetObject(iAttack)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_PERFORM, oAttack, dData, iSub = self.m_SubAttackMsg, oGame = self.m_Game)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_PERFORMED, self, dData)
        self.GetThumped(dData)
        dVictim['RS'] = dData['RS']
        iHP = self.ReceiveDamage(iAttack, dVictim)
        return iHP

    
    def ReceiveState(self, iAttack, dState):
        if self.IsDead():
            return 0
        dState['FlowDam'] = []
        if 'DamFactor' not in dState or not dState['DamFactor']:
            dState['DamFactor'] = {
                OBJ_VICTIM: { },
                OBJ_ATTACK: { } }
        dState['CurVID'] = self.m_ID
        oAttack = self.m_Game.GetObject(iAttack)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_STATE, oAttack, dState, iSub = self.m_SubAttackMsg, oGame = self.m_Game)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_STATEED, self, dState)
        iHP = self.ReceiveDamage(iAttack, dState)
        return iHP

    
    def ReceiveScene(self, lstMainDam):
        if self.IsDead():
            return 0
        dMsgInfo = {
            'MainDam': lstMainDam,
            'FlowDam': [],
            'CurVID': self.m_ID,
            'RS': lstMainDam[0][1],
            'DamFactor': {
                OBJ_VICTIM: { },
                OBJ_ATTACK: { } } }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SCENEED, self, dMsgInfo)
        iHP = self.ReceiveDamage(0, dMsgInfo)
        return iHP

    
    def ReceiveDamage(self, iAttack, dDamage, iSendMsg = 1):
        if self.IsDead():
            return 0
        oAttack = self.m_Game.GetObject(iAttack)
        if oAttack:
            dDamage['DamFactor'][OBJ_ATTACK].update(oAttack.m_BaseDamRatio)
        if self.m_BaseRecvDamRatio:
            dDamage['DamFactor'][OBJ_VICTIM].update(self.m_BaseRecvDamRatio)
        dData = {
            'AID': iAttack }
        dData.update(dDamage)
        iActNum = dDamage['RS'].Query('ActNum', 0)
        if iActNum:
            oSkill = self.m_Game.m_SkillMgr.GetSkill(iAttack, iActNum)
            if 'Skill' in dData and oSkill != dData['Skill']:
                cl_object.logging.SkillLog.Alert('skill noequal %s %s != %s %s' % (dData['Skill'], dData['Skill'].m_Base, oSkill, oSkill.m_Base))
            elif not oSkill:
                cl_object.logging.SkillLog.Alert('skill noskill %s %s %s' % (iActNum, dDamage['RS'], dData))
            dData['Skill'] = oSkill
        else:
            oSkill = None
        if iSendMsg:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_RECEIVEDAM, oAttack, dData, iSub = self.m_SubAttackMsg, oGame = self.m_Game)
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_RECEIVEDAMED, self, dData)
        if self.CheckIgnoreDam(iAttack, dData):
            return 0
        if 'Halt' in dData:
            if self.m_FightType & WARRIOR_HERO:
                self.GS2CImmunity(oSkill, iAttack, iActNum, IMMUNITY_PERFORM)
            return 0
        iHaltShieldRecovry = dData['HaltShieldRecovry'] if 'HaltShieldRecovry' in dData else 1
        self.HaltShieldRecover(iHaltShieldRecovry)
        lstDam = cl_formula.CalDamage(self, dData)
        lstDam.sort(key = functools.cmp_to_key((lambda d1, d2: d1[1].Query('DamType', 0) & DAM_MASK_ELEMENT - d2[1].Query('DamType', 0) & DAM_MASK_ELEMENT)))
        if not lstDam and self.m_FightType & WARRIOR_HERO:
            iShowType = dData['ShowType'] if 'ShowType' in dData else 0
            if iShowType != IMMUNITY_SHOWCOVER:
                self.GS2CImmunity(oSkill, iAttack, iActNum, IMMUNITY_PERFORM)
        (lstTotalChange, _, _) = self.HPModifyDam(iAttack, lstDam)
        return sum(lstTotalChange)

    
    def ReceiveCure(self, iAttack, dCure, iSendMsg = 1):
        if self.IsDead():
            return 0
        dData = {
            'AID': iAttack,
            'CurVID': self.m_ID }
        dData.update(dCure)
        iActNum = dCure['RS'].Query('ActNum', 0)
        if iActNum:
            oSkill = self.m_Game.m_SkillMgr.GetSkill(iAttack, iActNum)
            if oSkill:
                dData['Skill'] = oSkill
        oAttack = self.m_Game.GetObject(iAttack)
        if iSendMsg:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CURE, oAttack, dData, iSub = self.m_SubAttackMsg, oGame = self.m_Game)
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CUREED, self, dData)
        return self.HPModifyCure(iAttack, dData['MainCure'] + dData['FlowCure'])

    
    def GS2CImmunity(self, oSkill, iAttack, iActNum, iKey):
        if self.m_ValidShowTips:
            cl_snetwar.GS2CImmunity(self, oSkill, iAttack, iActNum, iKey)

    
    def GetActionNum(self):
        self.m_ActionNum += 1
        if self.m_ActionNum >= SERVER_ACTION_NUM_MAX:
            self.m_ActionNum = 1
        iActNum = self.m_ActionNum
        return iActNum

    
    def SetLastActionNum(self, iActNum):
        self.m_LastActionNum = iActNum

    
    def GetLastActionNum(self):
        iNewActNum = self.m_LastActionNum + 100
        if iNewActNum >= CLIENT_ACTION_NUM_MAX:
            iNewActNum = SERVER_ACTION_NUM_MAX + 100
        return iNewActNum

    
    def InitPerform(self):
        if self.m_AttPerform:
            self.AddPerform(self.m_AttPerform, 1)
        for iPerform in chain(self.m_PerformList, self.m_CommonPerform):
            self.AddPerform(iPerform, 1)
        

    
    def AddPerform(self, iPerform, iLevel, iItem = 0, iEnable = 1):
        return self.m_Perform.AddPerform(self, iPerform, iLevel, iEnable, iItem)

    
    def RemovePerform(self, iPerform):
        self.m_Perform.RemovePerform(self, iPerform)

    
    def EnablePerform(self, iPerform, iNotify):
        self.m_Perform.EnablePerform(self, iPerform, iNotify)

    
    def DisablePerform(self, iPerform, iNotify):
        self.m_Perform.DisablePerform(self, iPerform, iNotify)

    
    def GetPerformIfNoThenNew(self, iPerform):
        if self.m_ReleaseFlag:
            return None
        pfobj = self.GetPerform(iPerform)
        if not pfobj:
            pfobj = self.AddPerform(iPerform, 1)
        return pfobj

    
    def GetPerform(self, iPerform, iItemID = 0, iOwnPfid = 0):
        if self.m_ReleaseFlag:
            return None
        return self.m_Perform.GetPerform(iPerform)

    
    def GetPerformSIDByType(self, iPFType):
        return self.m_Perform.GetPerformSIDByType(iPFType)

    
    def HaltWaitSkill(self, iActNum):
        pass

    
    def ClearWaitSkill(self):
        pass

    
    def GetAttackPos(self, iFrame = 0):
        if iFrame:
            (ox, oy, oz) = self.GetLastPos(iFrame)
        else:
            (ox, oy, oz) = self.GetPos()
        iAddy = self.m_ModelHeight * 0.8
        return (ox, oy + iAddy, oz)

    
    def GetCenter(self):
        (x, y, z) = self.GetPos()
        return (x, y + self.m_ModelHeight * 0.5, z)

    
    def GetGroundPos(self):
        vPos = self.GetPos()
        if not self.m_Scene:
            return vPos
        fGroundDis = self.m_Game.Scene_GroundDistance(self.m_Scene, (vPos[0], vPos[1] + 1.8, vPos[2]), self.m_GroundMaxDis, PXMASK_GROUNDBLK, self.m_ID)
        vPos = (vPos[0], (vPos[1] - fGroundDis) + 1.8, vPos[2])
        if fGroundDis >= self.m_GroundMaxDis:
            WarobjLog.Debug('%s %s monster %d inGroundMaxDis %s %s' % (self.m_Game.m_ID, self.m_LineIdx, self.m_SID, vPos, fGroundDis))
        return vPos

    
    def AttrCache(self):
        dAttr = {
            'Side': self.m_Side }
        for sAttr, oAttr in self.m_PrivateAttr.items():
            if not oAttr.m_JoinAttrCache:
                continue
            dAttr[sAttr] = oAttr.GetValue(self)
        
        return dAttr

    
    def EventCache(self):
        dEvent = { }
        for iMsgKey, dInfo in self.m_TransEvt.items():
            dEvent[iMsgKey] = { }
            if iMsgKey in self.m_TransEvtToSort:
                dSorted = { }
                self.m_TransEvtToSort.pop(iMsgKey)
                lstPriority = sorted(dInfo, reverse = True)
                for iPriority in lstPriority:
                    dSorted[iPriority] = dInfo[iPriority]
                
                self.m_TransEvt[iMsgKey] = dSorted
            else:
                lstPriority = dInfo
            for iPriority in lstPriority:
                dOnce = { }
                for sKey, (func, iOnce) in dInfo[iPriority].items():
                    dEvent[iMsgKey][sKey] = (func, iOnce, iPriority)
                    if iOnce:
                        dOnce[sKey] = 1
                
                for sKey in dOnce:
                    dInfo[iPriority].pop(sKey)
                
            
        
        return dEvent

    
    def SetTransEvt(self, iMsg, iMsgKey, func, iOnce, iPriority, sKey):
        if iMsgKey not in self.m_TransEvt:
            self.m_TransEvt[iMsgKey] = { }
        if iPriority not in self.m_TransEvt[iMsgKey]:
            self.m_TransEvt[iMsgKey][iPriority] = { }
            if iMsg in self.m_UsePriority:
                self.m_TransEvtToSort[iMsgKey] = True
        self.m_TransEvt[iMsgKey][iPriority][sKey] = (func, iOnce)

    
    def MixPFAttrCache(self, dAttrCache):
        if 'ElementType' in dAttrCache and not (dAttrCache['ElementType'] & DAM_TYPE_ELEMENT) and self.m_ElementType & DAM_TYPE_ELEMENT:
            dAttrCache['ElementType'] = self.m_ElementType
        return dAttrCache

    
    def SetDieFlag(self, iFlag):
        self.m_Dead = iFlag

    
    def IsDied(self):
        return self.m_Dead == DEAD_FLAG_DIED

    
    def IsDying(self):
        return self.m_Dead == DEAD_FLAG_DYING

    
    def IsRealDied(self):
        return self.m_Dead == DEAD_FLAG_REAL

    
    def IsDead(self):
        if not self.m_Dead == DEAD_FLAG_DIED or self.m_Dead == DEAD_FLAG_DYING:
            pass
        return self.m_Dead == DEAD_FLAG_REAL

    
    def IsDeadNoDying(self):
        if not self.m_Dead == DEAD_FLAG_DIED:
            pass
        return self.m_Dead == DEAD_FLAG_REAL

    
    def IsIgnoreAtt(self):
        if self.QueryBitAttr('SpecialKey') & FIGHT3_KEY_IGNOREATT:
            return 1
        return 0

    
    def IsNeglectAttack(self, oSkill):
        if self.IsDead():
            return True
        return super(CWarrior, self).IsNeglectAttack(oSkill)

    
    def IsWudi(self):
        if self.QueryBitAttr('SpecialKey') & FIGHT_KEY_WUDI:
            return 1
        return 0

    
    def CheckLogicKey(self, iMark):
        if self.QueryBitAttr('LogicKey') & iMark:
            return 1
        return 0

    
    def CheckSpecialKey(self, iMark):
        if self.QueryBitAttr('SpecialKey') & iMark:
            return 1
        return 0

    
    def IsImmobilize(self):
        if self.QueryBitAttr('SpecialKey') & FIGHT_KEY_IMMOBILIZE:
            return 1
        return 0

    
    def IsUnbalance(self):
        if self.m_State.GetItemBySID(STATE_UNBALANCE):
            return 1
        return 0

    
    def IsReducingSpeed(self):
        return self.m_State.HasStateInList(STATE_SUBSPD_LIST)

    
    def GetReducingSpeedNum(self):
        return self.m_State.GetGetStateNumInList(STATE_SUBSPD_LIST)

    
    def IsReducingActionSpeed(self):
        if self.m_ChanegActionSpeed:
            return 1

    
    def FightMark(self):
        return (self.QueryBitAttr('SpecialKey') & FIGHT_KEY_ALL) >> FIGHT_KEY_OFFSET

    
    def FightMark2(self):
        return (self.QueryBitAttr('SpecialKey') & FIGHT2_KEY_ALL) >> FIGHT2_KEY_OFFSET

    
    def Call_Out_Lockable(self, func, iDelay, sFlag):
        if iDelay < 1:
            WarobjLog.Error('%d:%s delay is %d' % (self.m_SID, sFlag, iDelay))
            iDelay = 1
        iCallFrame = self.m_Game.GetFrameNum() + iDelay
        if iCallFrame in self.m_LockableCallOut:
            lstFunc = self.m_LockableCallOut[iCallFrame].setdefault(sFlag, [])
            lstFunc.append(func)
        else:
            self.m_LockableCallOut[iCallFrame] = {
                sFlag: [
                    func] }
            self.m_Game.TimerCall(self.m_ID, self.LockableCallBack, iDelay, 'suscallout%d' % iCallFrame)

    
    def Remove_Call_Out_Lockable(self, sFlag):
        lstRemove = []
        for iCallFrame, dCallOut in self.m_LockableCallOut.items():
            if sFlag in dCallOut:
                dCallOut.pop(sFlag)
                if not dCallOut:
                    lstRemove.append(iCallFrame)
        
        for iCallFrame in lstRemove:
            self.m_LockableCallOut.pop(iCallFrame)
        

    
    def LockableCallBack(self):
        iCurFrame = self.m_Game.GetFrameNum()
        if iCurFrame not in self.m_LockableCallOut:
            return None
        dCallOut = self.m_LockableCallOut.pop(iCurFrame)
        for lstFunc in dCallOut.values():
            for func in lstFunc:
                func()
            
        
        dCallOut.clear()

    
    def SetImmobilize(self, sKey, iSourceTarget):
        if self.IsDead():
            return None
        if self.m_FightType & WARRIOR_BOSS == WARRIOR_BOSS and self.IsWudi():
            return None
        oTarget = self.m_Game.GetObject(iSourceTarget)
        if oTarget:
            dMsgInfo = {
                'AID': iSourceTarget,
                'VID': self.m_ID,
                'Key': sKey,
                'Immobilize': 1 }
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CAUSE_ADDIMMOBILIZE, oTarget, dMsgInfo)
        if self.m_ImmobilizeSource:
            self.m_ImmobilizeSource[sKey] = 1
            return None
        self.m_ImmobilizeSource[sKey] = 1
        sImmobilizeKey = 'Immobilize'
        oGame = self.m_Game
        if self.m_Agent:
            self.m_Agent.PauseAgent(sImmobilizeKey)
        if self.m_FaceCtrl:
            self.m_FaceCtrl.LockFace(self, oGame.GetFacing(self.m_ID), sImmobilizeKey, False)
        self.Forbid(cl_forbid.IMMOBILIZE_RULE, sImmobilizeKey)
        oGame.SetImmobilized(self.m_ID, 1)
        dAllCallOut = { }
        iCurFrame = oGame.GetFrameNum()
        for iCallFrame, dCall in self.m_LockableCallOut.items():
            dAllCallOut[iCallFrame - iCurFrame] = dCall
        
        self.m_LockedCallOut = dAllCallOut
        self.m_LockableCallOut = { }
        self.LockCastingSkill(sImmobilizeKey)
        self.AddBitAttr('SpecialKey', sImmobilizeKey, FIGHT_KEY_IMMOBILIZE)
        self.AddBitAttr('LogicKey', sImmobilizeKey, FIGHT3_KEY_IGNOREKNOCKBACK | FIGHT3_KEY_IGNORETHUMP)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ADDIMMOBILIZE, self, { })

    
    def LockCastingSkill(self, sKey):
        dSkillCall = { }
        oSkillMgr = self.m_Game.m_SkillMgr
        iAttack = self.m_ID
        for iActNum in self.m_CastingSkill:
            oSkill = oSkillMgr.GetSkill(iAttack, iActNum)
            oSkill.SuspendCallOut(sKey)
            dSkillCall[iActNum] = 1
        
        self.m_LockedSkill = dSkillCall

    
    def ClearImmobilize(self, sKey, iSourceTarget):
        if self.IsDead() or self.m_ReleaseFlag:
            return None
        if sKey not in self.m_ImmobilizeSource:
            return None
        oTarget = self.m_Game.GetObject(iSourceTarget)
        if oTarget:
            dMsgInfo = {
                'AID': iSourceTarget,
                'VID': self.m_ID,
                'Key': sKey,
                'Immobilize': 0 }
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CAUSE_CLEARIMMOBILIZE, oTarget, dMsgInfo)
        self.m_ImmobilizeSource.pop(sKey)
        if self.m_ImmobilizeSource:
            return None
        sImmobilizeKey = 'Immobilize'
        if self.m_Agent:
            self.m_Agent.ResumeAgent(sImmobilizeKey)
        if self.m_FaceCtrl:
            self.m_FaceCtrl.UnLockFace(self, sImmobilizeKey, True)
        self.UnForbid(cl_forbid.IMMOBILIZE_RULE, sImmobilizeKey)
        self.ClearBitAttr('SpecialKey', sImmobilizeKey, FIGHT_KEY_IMMOBILIZE)
        self.ClearBitAttr('LogicKey', sImmobilizeKey, FIGHT3_KEY_IGNOREKNOCKBACK | FIGHT3_KEY_IGNORETHUMP)
        oGame = self.m_Game
        oGame.SetImmobilized(self.m_ID, 0)
        self.m_LockableCallOut = { }
        iCurFrame = oGame.GetFrameNum()
        for iFrame, dCall in self.m_LockedCallOut.items():
            iCallFrame = iCurFrame + iFrame
            self.m_LockableCallOut[iCallFrame] = dCall
            if iFrame == 0:
                self.LockableCallBack()
                continue
            oGame.TimerCall(self.m_ID, self.LockableCallBack, iFrame, 'suscallout%d' % iCallFrame)
        
        self.m_LockedCallOut = { }
        self.RestoreSkill(sImmobilizeKey)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CLEARIMMOBILIZE, self, { })

    
    def RestoreSkill(self, sKey):
        if not (self.m_LockedSkill) or not (self.m_CastingSkill):
            return None
        oGame = self.m_Game
        oSkillMgr = oGame.m_SkillMgr
        iAttack = self.m_ID
        dRestoreSkill = self.m_LockedSkill
        self.m_LockedSkill = { }
        for iActNum in dRestoreSkill:
            if iActNum not in self.m_CastingSkill:
                continue
            oSkill = oSkillMgr.GetSkill(iAttack, iActNum)
            if oSkill and not (oSkill.m_Base):
                continue
            if oSkill:
                oSkill.RestoreCallOut(sKey)
        

    
    def AddStateTime(self, idx, iFrame, dState):
        self.m_StateTimeUnit.AddQueue(idx, iFrame, dState)

    
    def AddPFPassTime(self, idx, iFrame, dPassInfo):
        self.m_PFPassTimeUnit.StopWait(idx)
        self.m_PFPassTimeUnit.AddQueue(idx, iFrame, dPassInfo)

    
    def GetPFPassTimeInfo(self, idx):
        dIdx2Frame = self.m_PFPassTimeUnit.m_Idx2Frame
        dWaitFrame = self.m_PFPassTimeUnit.m_WaitFrame
        iCallFrame = dIdx2Frame[idx] if idx in dIdx2Frame else 0
        dFrameInfo = dWaitFrame[iCallFrame] if iCallFrame in dWaitFrame else { }
        if idx in dFrameInfo:
            return dFrameInfo[idx]
        return { }

    
    def DelStateTime(self, idx):
        self.m_StateTimeUnit.StopWait(idx)

    
    def DelPFPassTime(self, idx):
        self.m_PFPassTimeUnit.StopWait(idx)

    
    def HasStateTime(self, iState):
        return self.m_StateTimeUnit.HasUnit(iState)

    
    def HasPFPassTime(self, idx):
        return self.m_PFPassTimeUnit.HasUnit(idx)

    
    def DoStateTimeUnit(self, idx, dInfo):
        iState = (idx // MAX_STATE_TYPE) * MAX_STATE_TYPE
        oState = self.m_State.GetItem(iState)
        if oState:
            iFlag = idx % MAX_STATE_TYPE
            if iFlag == STATE_IDX_DELAY:
                oState.DelayAction(self, dInfo)
            elif iFlag == STATE_IDX_COUNT:
                oState.OnCountFull(self, dInfo)
            elif iFlag == STATE_IDX_LIMITCOUNT:
                oState.RefreshLimitCount(self)
            else:
                self.m_State.RemoveItem(oState.m_ID)

    
    def DoPFPassTimeUnit(self, idx, dPassInfo):
        iPerform = dPassInfo['pfid']
        iItem = dPassInfo['ItemID']
        iOwnPfid = dPassInfo.get('OwnPfid', 0)
        pfobj = self.GetPerform(iPerform, iItem, iOwnPfid)
        if not pfobj:
            return None
        pfobj.DoPassTimeCallBack(self, dPassInfo)

    
    def ClearStateTime(self, iState):
        for idx in [
            STATE_IDX_DEFAULT,
            STATE_IDX_DELAY,
            STATE_IDX_COUNT,
            STATE_IDX_LIMITCOUNT]:
            self.m_StateTimeUnit.StopWait(iState + idx)
        

    
    def GetTimeUnitCBFrameByIdx(self, idx):
        dIdx2Frame = self.m_PFPassTimeUnit.m_Idx2Frame
        if idx not in dIdx2Frame:
            return 0
        return dIdx2Frame[idx]

    
    def LeaveScene(self, iNewScene):
        super(CWarrior, self).LeaveScene(iNewScene)
        self.ClearWaitSkill()
        for dCall in self.m_LockableCallOut.values():
            dCall.clear()
        
        self.m_LockableCallOut = { }
        for dCall in self.m_LockedCallOut.values():
            dCall.clear()
        
        self.m_LockedCallOut = { }

    
    def NetAddTo(self, dPlayer):
        super(CWarrior, self).NetAddTo(dPlayer)
        self.m_State.Refresh(dPlayer)
        self.m_Perform.Refresh(dPlayer)

    
    def SkillCheckHitPos(self, oSkill, iHitFrame, vHitPos):
        vLast = self.GetLastPos(iHitFrame)
        (fModelRadius, fModelHeight) = self.SkillCheckArgs
        if not cl_perform.cartoon.argcheck.PosAroundCheck(oSkill, vHitPos, vLast, fModelRadius * 2, fModelHeight):
            return False
        return True

    
    def SetSkillCheckArgs(self, fRadius, fHeight, bCalExtra = True):
        if bCalExtra and self.m_SkillCheckExtraArgs:
            (fExtraRadius, fExtraHeight) = self.GetSkillCheckExtraArgs()
            fRadius += fExtraRadius
            fHeight += fExtraHeight
        self.SkillCheckArgs = (fRadius, fHeight)

    
    def ClearSkillCheckArgs(self):
        (fRadius, fHeight) = cl_modeldefine.GetModelDefine(self.m_Shape, 'Physx')
        if self.m_SkillCheckExtraArgs:
            (fExtraRadius, fExtraHeight) = self.GetSkillCheckExtraArgs()
            fRadius += fExtraRadius
            fHeight += fExtraHeight
        self.SkillCheckArgs = (fRadius, fHeight)

    
    def AddSkillCheckExtraArgs(self, sKey, fRadius, fHeight):
        (fCurRadius, fCurHeight) = self.SkillCheckArgs
        if sKey in self.m_SkillCheckExtraArgs:
            (fOldExtraRadius, fOldExtraHeight) = self.m_SkillCheckExtraArgs[sKey]
            fCurRadius -= fOldExtraRadius
            fCurHeight -= fOldExtraHeight
        fCurRadius += fRadius
        fCurHeight += fHeight
        self.m_SkillCheckExtraArgs[sKey] = (fRadius, fHeight)
        self.SetSkillCheckArgs(fCurRadius, fCurHeight, bCalExtra = False)

    
    def ClearSkillCheckExtraArgs(self, sKey):
        if sKey in self.m_SkillCheckExtraArgs:
            (fOldExtraRadius, fOldExtraHeight) = self.m_SkillCheckExtraArgs.pop(sKey)
            (fCurRadius, fCurHeight) = self.SkillCheckArgs
            fCurRadius -= fOldExtraRadius
            fCurHeight -= fOldExtraHeight
            self.SetSkillCheckArgs(fCurRadius, fCurHeight, bCalExtra = False)

    
    def GetSkillCheckExtraArgs(self):
        (fExtraRadiusTotal, fExtraHeightTotal) = (0, 0)
        for fExtraRadius, fExtraHeight in self.m_SkillCheckExtraArgs.values():
            fExtraRadiusTotal += fExtraRadius
            fExtraHeightTotal += fExtraHeight
        
        return (fExtraRadiusTotal, fExtraHeightTotal)

    
    def GetElementFactor(self, iDamType, lstExtraElement, iHPType, oAttack, oReason):
        iFactor = 0
        iEleType = iDamType & DAM_TYPE_ELEMENT
        if oAttack or oAttack.m_MustElementRestrainted or oReason.Query('MustElementRestraint', 0):
            if iDamType & DAM_TYPE_NORMAL:
                iFactor = self.m_ElemenFatctor[DAM_TYPE_NORMAL][iHPType]
            for iType in self.m_ElemenFatctor:
                if iEleType & iType == iType:
                    iEleFactor = self.m_CurMaxElemenFactor[iType]
                    if iEleFactor > iFactor:
                        iFactor = iEleFactor
            
            for iExtraType in lstExtraElement:
                if iExtraType & iDamType:
                    pass
                if not (iExtraType & DAM_TYPE_ELEMENT) and iExtraType in self.m_ElemenFatctor:
                    iExtraFactor = self.m_CurMaxElemenFactor[iExtraType]
                    if iExtraFactor > iFactor:
                        iFactor = iExtraFactor
            
        else:
            for iType in self.m_ElemenFatctor:
                if iDamType & iType == iType:
                    iFactor = max(iFactor, self.m_ElemenFatctor[iType][iHPType])
            
            for iExtraType in lstExtraElement:
                if iExtraType in self.m_ElemenFatctor and iHPType in self.m_ElemenFatctor[iExtraType]:
                    iExtraFactor = self.m_ElemenFatctor[iExtraType][iHPType]
                    if iExtraFactor > iFactor:
                        iFactor = iExtraFactor
            
        if oAttack:
            if (oAttack.m_ImmuneElementRestrainted or oReason.Query('ImmuneElementRestraint', 0)) and iFactor < 10000 and iEleType:
                iFactor = 10000
            elif iEleType & g_PositiveElement[iHPType]:
                if oAttack.m_PositiveElementFactorValue:
                    iFactor += oAttack.m_PositiveElementFactorValue
                if iEleType in oAttack.m_PositiveElementFactorValueByType:
                    iFactor += oAttack.m_PositiveElementFactorValueByType[iEleType]
        if not iFactor:
            iFactor = 10000
        return iFactor

    
    def AddElementFactor(self, iDamType, iHPType, iRadio, sKey):
        dDamTypeInfo = self.m_ElementFactorInfo.setdefault(iDamType, { })
        dHPTypeInfo = dDamTypeInfo.setdefault(iHPType, { })
        dHPTypeInfo[sKey] = iRadio
        self.RefreshElementFactor(iDamType, iHPType)

    
    def RemoveElementFactor(self, iDamType, iHPType, sKey):
        if iDamType in self.m_ElementFactorInfo and iHPType in self.m_ElementFactorInfo[iDamType]:
            dHPTypeInfo = self.m_ElementFactorInfo[iDamType][iHPType]
            if sKey in dHPTypeInfo:
                dHPTypeInfo.pop(sKey)
                self.RefreshElementFactor(iDamType, iHPType)

    
    def RefreshElementFactor(self, iDamType, iHPType):
        if iDamType in self.m_ElementFactorInfo and iHPType in self.m_ElementFactorInfo[iDamType]:
            dHPTypeInfo = self.m_ElementFactorInfo[iDamType][iHPType]
            iRadioCount = sum(dHPTypeInfo.values())
            if iRadioCount < -10000:
                iRadioCount = -10000
            iNewValue = g_ElementFactor[iDamType][iHPType] * (10000 + iRadioCount) // 10000
            self.m_ElemenFatctor[iDamType][iHPType] = iNewValue
            dValue = self.m_ElemenFatctor[iDamType]
            self.m_CurMaxElemenFactor[iDamType] = max(dValue.values())

    
    def AddImmuneElementRestraint(self, sKey):
        self.m_ImmuneElementRestrainted[sKey] = 1

    
    def RemoveImmuneElementRestraint(self, sKey):
        if sKey in self.m_ImmuneElementRestrainted:
            self.m_ImmuneElementRestrainted.pop(sKey)

    
    def SetMustElementRestraint(self, sKey):
        self.m_MustElementRestrainted[sKey] = 1

    
    def ClearMustElementRestraint(self, sKey):
        if sKey in self.m_MustElementRestrainted:
            self.m_MustElementRestrainted.pop(sKey)

    
    def AddSummon(self, iSummon):
        self.m_SummonDict[iSummon] = 1

    
    def GetSummon(self, iFightType):
        dSummon = self.m_SummonDict
        if not dSummon:
            return None
        for iSummon in dSummon:
            oSummon = self.m_Game.GetObject(iSummon, PY_FLAG_DEAD)
            if not oSummon:
                continue
            if oSummon.m_FightType & iFightType == iFightType:
                return oSummon
        

    
    def CustomAttrValue(self, sAttr):
        iValue = None
        if sAttr == 'DeadPunishmentTimes':
            iValue = self.QuerySavedData(sAttr)
        elif sAttr == 'RestDyingSecond':
            iValue = self.QuerySavedData(sAttr)
        elif sAttr == 'DyingTimes':
            iValue = self.QuerySavedData(sAttr)
        elif sAttr == 'RollRelicCnt':
            iValue = self.QuerySavedData(sAttr)
        elif sAttr == 'RelicChooseAllCnt':
            iValue = self.QuerySavedData(sAttr)
        return iValue

    
    def ReduceActionSpeed(self, sKey, iReduceSpeed, iRecoverFrame, iRecoverValue):
        if not self.m_ChanegActionSpeed:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CAUSE_REDUCEACTIONSPEEDED, self, { })
        iActionSpeed = 100 - iReduceSpeed
        self.m_ChanegActionSpeed[sKey] = {
            'Speed': iActionSpeed,
            'LastChangeFrameNum': self.m_Game.GetFrameNum(),
            'RecoverFrame': iRecoverFrame,
            'RecoverValue': iRecoverValue,
            'Enable': 1 }
        if iRecoverFrame > 0 and iRecoverValue > 0:
            self.Call_Out(Functor(self.IntervalRecoverActionSpeed, sKey), iRecoverFrame, 'ActionSpeedRecover' + sKey)
        if iActionSpeed < self.m_ActionSpeed:
            self.TrueReduceActionSpeed(sKey)

    
    def IntervalRecoverActionSpeed(self, sKey):
        dChange = self.m_ChanegActionSpeed
        if sKey not in dChange:
            return None
        iActionSpeed = dChange[sKey]['Speed']
        iActionSpeed += dChange[sKey]['RecoverValue']
        if iActionSpeed >= 100:
            iActionSpeed = 100
        else:
            self.Call_Out(Functor(self.IntervalRecoverActionSpeed, sKey), dChange[sKey]['RecoverFrame'], 'ActionSpeedRecover' + sKey)
        dChange[sKey]['Speed'] = iActionSpeed
        dChange[sKey]['LastChangeFrameNum'] = self.m_Game.GetFrameNum()
        if self.m_UseActionSpeed == sKey:
            self.UpdateActionSpeed()
        if iActionSpeed == 100:
            dChange.pop(sKey, { })

    
    def UpdateActionSpeed(self):
        dChange = self.m_ChanegActionSpeed
        if not dChange:
            if self.m_ActionSpeed != 100:
                lstState = []
                for oState in self.m_State.m_Item.values():
                    lstState.append(oState.m_SID)
                
                WarobjLog.Alert(f'''{self.m_Game} update actionspeed err {lstState}''')
                self.ClearActionSpeed()
            return None
        sMinKey = ''
        iMinSpeed = 100
        for sChangeKey, dInfo in dChange.items():
            if not dInfo['Enable']:
                continue
            iChangeSpeed = dInfo['Speed']
            if iChangeSpeed < iMinSpeed:
                iMinSpeed = iChangeSpeed
                sMinKey = sChangeKey
        
        if not sMinKey:
            self.ClearActionSpeed()
            return None
        if self.m_UseActionSpeed == sMinKey:
            self.ChangeActionSpeedProp(iMinSpeed)
        else:
            self.TrueReduceActionSpeed(sMinKey)

    
    def ClearActionSpeed(self):
        if self.m_ActionSpeed != 100:
            if self.m_UseActionSpeed and self.m_ChanegActionSpeed[self.m_UseActionSpeed]['Enable'] and self.m_ChanegActionSpeed[self.m_UseActionSpeed]['RecoverFrame'] > 0 and self.m_ChanegActionSpeed[self.m_UseActionSpeed]['Speed'] == 100:
                self.ChangeActionSpeedProp(100)
            else:
                self.TrueReduceActionSpeed(self.m_UseActionSpeed)
        self.m_ChanegActionSpeed = { }
        self.m_UseActionSpeed = ''
        self.m_ActSpFrameShaft = { }

    
    def TrueReduceActionSpeed(self, sKey):
        sOldKey = self.m_UseActionSpeed
        iOldSpeed = self.m_ActionSpeed
        self.m_UseActionSpeed = sKey
        iNewSpeed = self.m_ChanegActionSpeed[sKey]['Speed'] if self.m_ChanegActionSpeed[sKey]['Enable'] else 100
        self.ChangeActionSpeedProp(iNewSpeed)
        if iOldSpeed == iNewSpeed:
            return None
        oGame = self.m_Game
        dFrameShaft = self.m_ActSpFrameShaft
        self.m_ActSpFrameShaft = { }
        for iActNum in self.m_CastingSkill.keys():
            oSkill = oGame.m_SkillMgr.GetSkill(self.m_ID, iActNum)
            oSkill.ChangeSpeed(sOldKey, dFrameShaft)
        
        self.BackSwingChangeSpeed(sOldKey, dFrameShaft)
        if self.Query('Struck'):
            self.StruckChangeSpeed(sOldKey, dFrameShaft)

    
    def StruckChangeSpeed(self, sOldKey, dFrameShaft):
        pass

    
    def ChangeActionSpeedProp(self, iNewSpeed):
        if iNewSpeed > 100:
            iNewSpeed = 100
        sKey = 'ChangeActionSpeed'
        if iNewSpeed == 100:
            self.AttrClear('MoveSpeed', sKey)
            self.AttrClear('TurnSpeed', sKey)
        else:
            iMoveSpeed = -(100 - iNewSpeed) * 100
            self.AttrChange('MoveSpeed', iMoveSpeed, 0, sKey)
            self.AttrChange('TurnSpeed', iMoveSpeed, 0, sKey)
        self.m_ActionSpeed = iNewSpeed
        self.GS2CPropChange('ActionSpeed')

    
    def PreCalCallFrame(self, iFrame, iCurSpeed, iRecoverFrame, iRecoverValue, iLastFrameNum, iCurFrameNum):
        if iLastFrameNum:
            iPassFrame = iCurFrameNum - iLastFrameNum
            iNextFrame = iRecoverFrame - iPassFrame
            if not iNextFrame:
                iCurSpeed += iRecoverValue
                iNextFrame = iRecoverFrame
            else:
                iNextFrame = iRecoverFrame
        iRecoverCount = ((None - iCurSpeed) + iRecoverValue - 1) // iRecoverValue
        dShaft = { }
        iTimePassFrame = 0
        for _ in range(iRecoverCount):
            if iFrame < iNextFrame:
                break
            iTimePassFrame += iNextFrame
            iFrame -= iNextFrame
            iOldSpeed = iCurSpeed
            iCurSpeed += iRecoverValue
            if iCurSpeed > 100:
                iCurSpeed = 100
            iFrame = (iFrame * iOldSpeed + iCurSpeed - 1) // iCurSpeed
            dShaft[iCurFrameNum + iTimePassFrame] = iFrame
            iNextFrame = iRecoverFrame
        
        iFrame += iTimePassFrame
        self.m_ActSpFrameShaft[iCurFrameNum + iFrame] = dShaft
        return iFrame

    
    def GetChangeSpeedDelayFrame(self, iFrame, iOldSpeed = 100):
        sKey = self.m_UseActionSpeed
        if not sKey:
            return iFrame
        dChange = self.m_ChanegActionSpeed
        if sKey not in dChange:
            return iFrame
        iCurSpeed = self.m_ActionSpeed
        if iCurSpeed == iOldSpeed:
            return iFrame
        iFrame = (iFrame * iOldSpeed + iCurSpeed - 1) // iCurSpeed
        if iFrame < 1:
            return 1
        dInfo = dChange[sKey]
        iRecoverFrame = dInfo['RecoverFrame']
        iRecoverValue = dInfo['RecoverValue']
        if iRecoverFrame and iRecoverValue:
            iLastFrameNum = dInfo['LastChangeFrameNum']
            iCurFrameNum = self.m_Game.GetFrameNum()
            iFrame = self.PreCalCallFrame(iFrame, iCurSpeed, iRecoverFrame, iRecoverValue, iLastFrameNum, iCurFrameNum)
        return iFrame

    
    def GetDelayFrameOnChangeSpeed(self, iCallFrameNum, sOldKey, dFrameShaft):
        iCurFrameNum = self.m_Game.GetFrameNum()
        iNewSpeed = self.m_ActionSpeed
        dInfo = self.m_ChanegActionSpeed[self.m_UseActionSpeed]
        iRecoverFrame = dInfo['RecoverFrame']
        iRecoverValue = dInfo['RecoverValue']
        if sOldKey:
            dOldInfo = self.m_ChanegActionSpeed[sOldKey]
            iOldSpeed = dOldInfo['Speed']
            iLastFrameNum = dOldInfo['LastChangeFrameNum']
        else:
            iOldSpeed = 100
            iLastFrameNum = iCurFrameNum
        if iCallFrameNum in dFrameShaft and iLastFrameNum in dFrameShaft[iCallFrameNum]:
            iNewFrame = dFrameShaft[iCallFrameNum][iLastFrameNum] - iCurFrameNum - iLastFrameNum
        else:
            iNewFrame = iCallFrameNum - iCurFrameNum
        iNewFrame = (iNewFrame * iOldSpeed + iNewSpeed - 1) // iNewSpeed
        if iRecoverFrame and iRecoverValue:
            iNewFrame = self.PreCalCallFrame(iNewFrame, iNewSpeed, iRecoverFrame, iRecoverValue, iLastFrameNum, iCurFrameNum)
        if iNewFrame < 1:
            WarobjLog.Debug('%s %s delayframe%s<1 %s %s %s %s %s %s' % (self.m_Game.m_ID, self.m_SID, iNewFrame, iOldSpeed, iCurFrameNum, iCallFrameNum, sOldKey, dFrameShaft, self.m_ChanegActionSpeed))
            iNewFrame = 1
        return iNewFrame

    
    def ClearActionSpeedEffect(self, sKey):
        self.Remove_Call_Out('ActionSpeedRecover' + sKey)
        self.AttrClear('MoveSpeed', sKey)
        self.AttrClear('TurnSpeed', sKey)
        dChange = self.m_ChanegActionSpeed
        if sKey not in dChange:
            return None
        if self.m_UseActionSpeed == sKey:
            dChange[sKey]['Enable'] = 0
            self.UpdateActionSpeed()
        dChange.pop(sKey, { })
        if not dChange:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CAUSE_REDUCEACTIONSPEEDEDEND, self, { })

    
    def GetOwner(self):
        return self.m_Game.GetObject(self.m_Owner)

    
    def GetOwnObjectID(self, iObjectType):
        if iObjectType == OBJECT_OWNER:
            return self.m_ID
        if iObjectType == OBJECT_SELFOWNER:
            return self.m_Owner
        return 0

    
    def GetOwnObject(self, iObjectType):
        iObject = self.GetOwnObjectID(iObjectType)
        return self.m_Game.GetObject(iObject)

    
    def CheckDamTraceCD(self):
        skey = 'LastDamTraceFrameNum'
        iCurDamTraceFrameNum = self.m_Game.GetFrameNum()
        iLastDamTraceFrameNum = self.Query(skey, 0)
        if iCurDamTraceFrameNum - iLastDamTraceFrameNum > Second2Frame(1800) or iLastDamTraceFrameNum == 0:
            self.Set(skey, iCurDamTraceFrameNum)
            return 1
        return 0

    
    def AddPassLayerClearKey(self, sKey):
        if not self.m_PassLayerClearKey:
            oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
            cl_msgcenter.AddAttentionFunc(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.OnLayerStart, 'PassLayerClearData')
        self.m_PassLayerClearKey[sKey] = 1

    
    def DelPassLayerClearKey(self, sKey):
        self.m_PassLayerClearKey.pop(sKey, 0)
        if not self.m_PassLayerClearKey:
            oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
            cl_msgcenter.DoneAttention(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, 'PassLayerClearData')

    
    def OnLayerStart(self, _oLinster, oWarMgr, dMsgInfo):
        for sKey in self.m_PassLayerClearKey:
            self.Delete(sKey)
        

    
    def GetTrapThumped(self):
        pass

    
    def SetDieFinalInfo(self, iDam, iAttack):
        if self.m_FinalDam:
            return None
        self.m_FinalDam = iDam
        self.m_FinalAttack = iAttack

    
    def ClearDieFinalInfo(self):
        (self.m_FinalDam, self.m_FinalAttack) = (0, 0)

    
    def ChangeBaseDamRatio(self, sKey, iAdd, iMul, iMask = 0):
        if not iAdd and not iMul:
            return None
        self.m_BaseDamRatio[sKey] = (iAdd, iMul, iMask)

    
    def ClearBaseDamRatioByKey(self, sKey):
        if sKey not in self.m_BaseDamRatio:
            return None
        self.m_BaseDamRatio.pop(sKey)

    
    def GetBaseDamAddRatio(self):
        iInit = 10000
        dResult = {
            0: iInit }
        for iAdd, _, iMask in self.m_BaseDamRatio.values():
            if iMask not in dResult:
                dResult[iMask] = iInit + iAdd
                continue
            dResult[iMask] += iAdd
        
        return dResult

    
    def GetBaseDamMulRatio(self):
        iInit = 10000
        dResult = {
            0: iInit }
        for _, iMul, iMask in self.m_BaseDamRatio.values():
            if iMask not in dResult:
                dResult[iMask] = iInit * (10000 + iMul) // 10000
                continue
            dResult[iMask] = dResult[iMask] * (10000 + iMul) // 10000
        
        return dResult

    
    def GetBaseDamRatio(self):
        return self.m_BaseDamRatio

    
    def ChangeBaseRecvDamRatio(self, sKey, iAdd, iMul, iMask = 0):
        if not iAdd and not iMul:
            return None
        self.m_BaseRecvDamRatio[sKey] = (iAdd, iMul, iMask)

    
    def ClearBaseRecvDamRatioByKey(self, sKey):
        if sKey not in self.m_BaseRecvDamRatio:
            return None
        self.m_BaseRecvDamRatio.pop(sKey)

    
    def JudgeIgnoreStateEff(self, iAttack, iEffType):
        if not self.CheckBitAttrKey('IgnoreSTEff', iEffType | IGNORESTATE_EFF_FLAG):
            return 1
        oAttack = self.m_Game.GetObject(iAttack, PY_FLAG_DEAD)
        if not oAttack:
            return 0
        dInfo = {
            'IgnoreStateEff': 0,
            'VID': self.m_ID,
            'AID': iAttack,
            'EffType': iEffType }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_IGNORESTATE_EFF, oAttack, dInfo)
        return dInfo['IgnoreStateEff']

    
    def ClearTransFactorInState(self, tStateUseTransFactor, sKey):
        pass

    
    def GetStateUseTransFactor(self):
        pass

    
    def AddCustomValue(self, sArg, iVal, sReason):
        if sArg not in self.m_CustomFactor:
            self.m_CustomFactor[sArg] = {
                'Value': iVal,
                'Factor': {
                    sReason: iVal } }
            return None
        dArgInfo = self.m_CustomFactor[sArg]
        dFactor = dArgInfo['Factor']
        if sReason not in dFactor:
            dArgInfo['Value'] += iVal
        else:
            iOldVal = dFactor[sReason]
            iDiff = iVal - iOldVal
            dArgInfo['Value'] += iDiff
        dFactor[sReason] = iVal

    
    def GetCustomValue(self, sArg, iDefault = 0):
        if sArg not in self.m_CustomFactor:
            return iDefault
        return self.m_CustomFactor[sArg]['Value']

    
    def DelCustomFactor(self, sArg, sReason):
        if sArg not in self.m_CustomFactor:
            return None
        dArgInfo = self.m_CustomFactor[sArg]
        dFactor = dArgInfo['Factor']
        if sReason not in dFactor:
            return None
        iVal = dFactor.pop(sReason)
        if not dFactor:
            self.m_CustomFactor.pop(sArg)
            return None
        dArgInfo['Value'] -= iVal



def CompareTuple(t1, t2):
    return t1[0] - t2[0]

