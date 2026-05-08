# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p2511.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p2511.pyc
# Source Generated with Decompyle++
# File: p2511.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_only import PY_FLAG_DEAD
from . import CTalent as CCustomPerform
from cl_commondefines import OBJ_SELF, PF_SUBMSG_CAREERPF, WARRIOR_BARRIER, WARRIOR_HERO
from cl_newformula import Func304, Func331

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVESUMMON, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COST_ENERGY, -1, 2, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVESUMMON, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COST_ENERGY, -1, 2, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVESUMMON, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COST_ENERGY, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1307, 0, None):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32394, 0, { }, 1, 0, None)
        if cl_evcon.CheckTalentLevel(oWarrior, oEventCB, 2511) <= 2:
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 32394, (lambda *a: Func331(*a, **{
'sid': 2511 }) * 2000))
        if cl_evcon.CheckTalentLevel(oWarrior, oEventCB, 2511) == 3:
            cl_evact.EventCBSetStateStatisticsByOrderAndAddType(oWarrior, oEventCB, (lambda *a: ((Func304(*a, **{
'sAttr': 'EnergyMax' }) - Func304(*a, **{
'sAttr': 'Energy' })) / Func304(*a, **{
'sAttr': 'EnergyMax' })) * 100), 32394, 'EnergyCostRatio', 0, 0)
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 32394, (lambda *a: ((Func304(*a, **{
'sAttr': 'EnergyMax' }) - Func304(*a, **{
'sAttr': 'Energy' })) / Func304(*a, **{
'sAttr': 'EnergyMax' })) * 6000 + Func331(*a, **{
'sid': 2511 }) * 2000))


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckSummonFightType(oWarrior, oEventCB, WARRIOR_BARRIER):
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 32394, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 32372):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventGetTargetBySummonType(oWarrior, oEventCB, WARRIOR_BARRIER)
        cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, cl_action.CommonGetSummonAttr(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_BARRIER, 'Width') / 2 + 1, WARRIOR_HERO, 1, 0, 0, 0, 0, None, None)
        CustomAction(oWarrior, oEventCB, {
            'CountStateID': 32394,
            'EffectStateID': 32393,
            'RecordKey': 'EnergyRatio',
            'Level1': 0.4,
            'Level2': 0.5,
            'Level3': 0.6,
            'DamFactor1': 2000,
            'DamFactor2': 4000,
            'DamFactor3': 6000 })


class CPerform(CCustomPerform):
    m_SID = 2511
    m_Name = '高压运转'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 106


def CustomAction(oWarrior, oEventCB, dInfo):
    oTalent = oWarrior.m_TalentCon.GetPerform(2511)
    if not oTalent:
        return None
    iTalent = oTalent.m_Level
    oCountState = oWarrior.m_State.GetItemBySID(dInfo['CountStateID'])
    if not oCountState:
        return None
    iEnergy = oWarrior.Energy()
    iEnergyMax = oWarrior.EnergyMax()
    sKey = 'EnergyCostRatio'
    if sKey not in oCountState.m_Data:
        oCountState.m_Data[sKey] = 0
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iEnergyCost = dMsgInfo['EnergyCost'] if 'EnergyCost' in dMsgInfo else 0
    iEnergyCostRatio = oCountState.m_Data[sKey] + int((iEnergyCost / iEnergyMax) * 100)
    oCountState.m_Data[sKey] = iEnergyCostRatio
    iCurEnergyRatio = (iEnergy / iEnergyMax) * 100
    iNewCount = 0
    sTalent = str(iTalent)
    iGainEffect = dInfo['Level' + sTalent]
    iDamFactor = dInfo['DamFactor' + sTalent]
    iNewCount = int(iDamFactor + iGainEffect * iEnergyCostRatio * 100)
    oCountState.SetCount(oWarrior, iNewCount)
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oSummon = oWarrior.GetSummon(WARRIOR_BARRIER)
    if not oSummon:
        return None
    iEffectStateId = dInfo['EffectStateID']
    for iTarget in dTransInfo['TargetList']:
        oTarget = oWarrior.m_Game.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            continue
        oState = oTarget.m_State.GetItemBySource(iEffectStateId, oSummon.m_ID)
        if not oState:
            return None
        oState.SetCount(oTarget, iNewCount)
        oEnableState = oTarget.m_State.GetEnableItemBySID(iEffectStateId)
        if not oEnableState:
            continue
        if oState.m_ID != oEnableState.m_ID and iNewCount > oEnableState.GetCount():
            oTarget.m_State.Replace(oTarget, oEnableState, oState, False)
    

