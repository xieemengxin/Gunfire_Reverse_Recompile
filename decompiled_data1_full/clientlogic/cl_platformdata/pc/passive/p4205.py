# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4205.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4205.pyc
# Source Generated with Decompyle++
# File: p4205.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_betree.monsteragent as magent
import cl_snetwar
import cl_state
import cl_object.reason
from cl_only import Functor, ChooseKey, SendAlert, DeepCopy, PY_FLAG_DEAD, Time2Frame
from cl_commondefines import WARRIOR_MONSTER, WARRIOR_SUMMON, STATE_TIME_LIMIT
from cl_propdata import BASIC_PROP_NAME
from cl_object.logging import OtherLog
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import FIGHT_KEY_WUDI, HP_RADIO_SUB
from cl_newformula import Func204, Func221

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)
    cl_action.CommonAddSpecialKey(oWarrior, oLifeCycle, FIGHT_KEY_WUDI, None)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 80, HP_RADIO_SUB, 2)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 40, HP_RADIO_SUB, 3)
    CustomAction(oWarrior, oLifeCycle, {
        'SID': {
            3921: 1,
            1053: 1 } })


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func221(*a))) >= 1 and cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func204(*a))) == 3:
        cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'HPMax', -3000, 0, None)
    elif cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func221(*a))) >= 1 and cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func204(*a))) == 4:
        cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'HPMax', -3600, 0, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Phase') < 2:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Phase', 2)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'HPLimit', 40)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'DeadProb', 33)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'BackupDeadCnt', 3)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Phase') < 3:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Phase', 3)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'HPLimit', 0)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'DeadProb', 66)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'BackupDeadCnt', 0)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'BackupLiveCnt', 5)


class CPerform(CCustomPerform):
    m_SID = 4205
    m_Name = '章鱼触手生命连接及轮回血量特殊处理'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = {
        'Phase': 1,
        'HPLimit': 80,
        'DeadProb': 0,
        'BackupLiveCnt': 0,
        'BackupDeadCnt': 0,
        'DeadShape': 3922,
        'DeadDamRatio': 10,
        'WudiState': 33606,
        'SummonWudiState': 33582,
        'WudiStateTime': 300 }
    m_DieDisable = 1


def CustomAction(oWarrior, oLifeCycle, dData):
    
    def ClearEvent(oOwner, oLifeCycle):
        oGame = oOwner.m_Game
        oScene = oGame.m_SceneMgr.GetScene(oOwner.m_Scene)
        if oScene:
            oScene.m_CustomData.pop('TentaclePos', None)
            oScene.m_CustomData.pop('TentacleID', None)
        oGame.DoneGlobalAttention(iTarget, cl_msgcenter.MSG_WAR_CREATEMONSTER, sKey, -1)
        oGame.DoneGlobalAttention(iTarget, cl_msgcenter.MSG_WAR_REMOVEOBJ, sKey, -1)
        oGame.DoneGlobalAttention(iTarget, cl_msgcenter.MSG_WAR_DIE, sKey, -1)
        cl_msgcenter.DoneAttention(oOwner, oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_CREATEMONSTER_BEFORE, sKey, -1)

    iTarget = oWarrior.m_ID
    sKey = oLifeCycle.Key()
    oGame = oWarrior.m_Game
    oGame.AddGlobalAttention(iTarget, cl_msgcenter.MSG_WAR_CREATEMONSTER, Functor(OnCreateMonster, dData), sKey, -1)
    oGame.AddGlobalAttention(iTarget, cl_msgcenter.MSG_WAR_REMOVEOBJ, Functor(OnRemoveMonster, dData), sKey, -1)
    oGame.AddGlobalAttention(iTarget, cl_msgcenter.MSG_WAR_DIE, Functor(OnRemoveMonster, dData), sKey, -1)
    oLifeCycle.AddDisableFunc(ClearEvent)
    cl_msgcenter.AddAttentionFunc(oWarrior, oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_CREATEMONSTER_BEFORE, Functor(OnCreateMonsterBefore, dData), sKey, -1)


def OnCreateMonsterBefore(dData, oListener, oWarmgr, dMsgInfo):
    oGame = oListener.m_Game
    clsMonsterData = oGame.m_ResMgr.m_WarData.GetMonsterData(dMsgInfo['MonsterSID'])
    if not clsMonsterData or clsMonsterData.m_DataSID not in dData['SID']:
        return None
    oPerform = oListener.GetPerform(CPerform.m_SID)
    if not oPerform:
        return None
    dExtInfo = dMsgInfo['ExtInfo']
    if 'TheDead' in dExtInfo:
        iDead = dExtInfo['TheDead']
    else:
        iBackupLiveCnt = oPerform.GetArgValue('BackupLiveCnt', 0)
        iBackupDeadCnt = oPerform.GetArgValue('BackupDeadCnt', 0)
        if iBackupLiveCnt and oPerform.GetArgValue('RandomDeadCnt', 0) >= iBackupLiveCnt:
            oPerform.SetArgValue('RandomDeadCnt', 0)
            iDead = 0
        elif iBackupDeadCnt and oPerform.GetArgValue('RandomLiveCnt', 0) >= iBackupDeadCnt:
            oPerform.SetArgValue('RandomLiveCnt', 0)
            iDead = 1
        else:
            iProb = oPerform.GetArgValue('DeadProb', 0)
            if oGame.Random(100) < iProb:
                iDead = 1
                if iBackupLiveCnt:
                    oPerform.SetArgValue('RandomLiveCnt', 0)
                    oPerform.AddArgValue('RandomDeadCnt', 1)
                else:
                    iDead = 0
                    if iBackupDeadCnt:
                        oPerform.SetArgValue('RandomDeadCnt', 0)
                        oPerform.AddArgValue('RandomLiveCnt', 1)
    if None:
        dExtInfo.setdefault('SetInfo', { })['TheDead'] = 1
        dMsgInfo['AddInfo']['Shape'] = oPerform.GetArgValue('DeadShape', 3922)


def OnCreateMonster(dData, oListener, oSender, dMsgInfo):
    if oSender.m_DataSID not in dData['SID']:
        return None
    oPerform = oListener.GetPerform(CPerform.m_SID)
    if not oPerform:
        return None
    iTarget = oSender.m_ID
    iListener = oListener.m_ID
    sKey = '%s-%s' % (oPerform.Key(), iTarget)
    oSender.Set('TentacleOwner', iListener)
    cl_msgcenter.AddAttentionFunc(oListener, iTarget, cl_msgcenter.MSG_WAR_HP_CHANGE, OnMonsterHPChange, sKey)


def OnRemoveMonster(dData, oListener, oSender, dMsgInfo):
    iTarget = oSender.m_ID
    oGame = oListener.m_Game
    if oSender.m_FightType & WARRIOR_MONSTER:
        if iTarget not in oListener.m_MonsterSummon:
            return None
        oListener.m_MonsterSummon.pop(iTarget)
    elif not oSender.m_FightType & WARRIOR_SUMMON:
        return None
    if oSender.m_DataSID not in dData['SID']:
        return None
    oGame = oListener.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oListener.m_Scene)
    if not oScene:
        return None
    dAllTentacle = oScene.m_CustomData.get('TentaclePos', None)
    dID = oScene.m_CustomData.get('TentacleID', None)
    if not dAllTentacle or not dID:
        return None
    tIndex = dID.pop(iTarget, None)
    if tIndex is None:
        return None
    (key, iIndex) = tIndex
    dAllTentacle.get(key, { }).pop(iIndex, None)


def OnMonsterHPChange(oListener, oSender, dMsgInfo):
    if oListener.IsDead():
        return None
    if oSender.m_ID not in oListener.m_MonsterSummon:
        return None
    oPerform = oListener.GetPerform(CPerform.m_SID)
    if not oPerform:
        return None
    iHp = oListener.HP()
    iHPLimit = oPerform.GetArgValue('HPLimit', 0)
    if iHPLimit:
        iHp = (iHp - oListener.QueryAttr('HPMax') * iHPLimit // 100) + 1
    if iHp <= 0:
        return None
    iAttack = dMsgInfo['AID']
    iTarget = oSender.m_ID
    oListener.Set('LastDamedTentacle', iTarget)
    iTotalDam = 0
    iDamEfficiency = 100
    oGame = oListener.m_Game
    if dMsgInfo['IsDam']:
        iCurFrame = oGame.GetFrameNum()
        oListener.Set('Injured%d' % iAttack, iCurFrame)
        iFactor = -1
        if oSender.Query('TheDead', 0):
            iDeadDamRatio = oPerform.GetArgValue('DeadDamRatio', 0)
            if iDeadDamRatio:
                iDamEfficiency = iDeadDamRatio
            else:
                iFactor = 1
        for iPreChange, oReason in dMsgInfo['TrueChange']:
            iTrueChange = iFactor * min(iDamEfficiency * iPreChange // 100, iHp)
            iHp += iTrueChange
            oListener.HPDirectModify('HP', iAttack, iTrueChange, oReason)
            iTotalDam += iTrueChange
            if iHp <= 0:
                break
        
    if oListener.m_Agent and dMsgInfo['IsDam']:
        magent.DamHateVal(oListener, {
            'IsDam': dMsgInfo['IsDam'],
            'AID': iAttack,
            'TotalDam': [
                -iTotalDam] })
    if iHp <= 0 and (0) < oListener.HP():
        iListener = oListener.m_ID
        iFrame = Time2Frame(oPerform.GetArgValue('WudiStateTime', 0))
        dArgs = {
            'AID': iListener,
            'RS': cl_object.reason.CStrReason('pf4205'),
            'arg': { } }
        oState = cl_state.AddState(oListener, oPerform.GetArgValue('WudiState', 0), STATE_TIME_LIMIT, iFrame, dArgs)
        if oState:
            oState.Enable(oListener)
        for iSummonID in oListener.m_MonsterSummon:
            oSummon = oGame.GetObject(iSummonID, PY_FLAG_DEAD)
            if not oSummon:
                continue
            oSummonState = cl_state.AddState(oSummon, oPerform.GetArgValue('SummonWudiState', 0), STATE_TIME_LIMIT, iFrame, dArgs)
            if oSummonState:
                oSummonState.Enable(oSummon)
        

