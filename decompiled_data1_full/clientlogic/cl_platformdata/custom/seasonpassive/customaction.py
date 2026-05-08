# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/custom/seasonpassive/customaction.pyc
# RelativePath: clientlogic/cl_platformdata/custom/seasonpassive/customaction.pyc
# Source Generated with Decompyle++
# File: customaction.pyc (Python 3.6)

import cl_state
import cl_formula
import cl_war
import cl_notify
import cl_reward
import cl_evact
import cl_object.reason
from cl_only import Time2Frame, SendAlert, PY_FLAG_DEAD
from cl_commondefines import STATE_TIME_LIMIT, S7_FOGPOISON_STATE, BASEATTR_REFRESH, BASEATTR_CLIENT, MG_SOURCE_SEASONMODULE, MG_BULLET, MG_CASH, MG_TRIGGER, WARRIOR_SUMMON_AIRFOLLOWEFFECT, MG_DROP_HP, WARRIOR_MONSTER, STATE_TIME_FOREVER

def CustomAction51588_1(oHero, oEventCB, dInfo):
    sKey = 'EventCreateSummon-%s' % oEventCB.m_Key
    dSummon = oHero.Query(sKey, { })
    if not dSummon:
        return None
    iAddLifeTime = dInfo['AddLifeTime']
    iMaxLifeTime = dInfo['MaxSummonTime']
    oGame = oHero.m_Game
    for iSummon in dSummon:
        oSummon = oGame.GetObject(iSummon)
        if not oSummon:
            continue
        iCurLifeTime = min(oSummon.RemainFrame() + iAddLifeTime, iMaxLifeTime)
        oSummon.SetLifeFrame(iCurLifeTime)
    


def CustomAction51588_2(oHero, oEventCB, dInfo):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTrans['TargetList']
    if not lstTar:
        return None
    iTarget = lstTar[0]
    oTarget = oHero.m_Game.GetObject(iTarget)
    if not oTarget:
        return None
    iHeroID = oHero.m_ID
    oState = oTarget.m_State.GetItemBySource(S7_FOGPOISON_STATE, iHeroID)
    iAddFrame = Time2Frame(dInfo['AddTime'])
    if not oState:
        dEventInfo = oEventCB.GetCBEventInfo()
        iPerformSid = dEventInfo['pfid']
        oLifeCycle = dEventInfo['LifeCycle']
        oPerform = oLifeCycle.GetObject()
        oState = AddFogPoisonState(oHero, oTarget, iPerformSid, iAddFrame, sReason = oHero.AttReason(oPerform, 0))
        if not oState:
            return None
    iAddCount = cl_formula.GetResultByData(oHero, dInfo['AddCount'], oEventCB.GetCBEventInfo())
    oState.AddCount(oTarget, iAddCount, iAddFrame)


def AddFogPoisonState(oHero, oTarget, iSourcePerform, iAddFrame, sReason = ''):
    iHeroID = oHero.m_ID
    dStatArgs = {
        'AID': iHeroID,
        'RS': sReason,
        'pfid': iSourcePerform,
        'arg': {
            'Spread': oHero.Query('p51599SetSpread', 0),
            'MaxCount': oHero.Query('p51599SetMaxCount', 0),
            'BaseCountDam': oHero.GetCustomValue('PF1992CountDam', 0),
            'BaseTalentDam': oHero.GetCustomValue('PF1992TalentDam', 0),
            'OtherDamMul': oHero.GetCustomValue('PF1992DamMul', 0),
            'DeBuffDamMul': oHero.GetCustomValue('PF1992DeBuffMul', 0),
            'Interval': oHero.GetCustomValue('PF1992Interval', 0) } }
    oState = cl_state.AddState(oTarget, S7_FOGPOISON_STATE, STATE_TIME_LIMIT, iAddFrame, dStatArgs)
    if not oState:
        return None
    oState.Enable(oTarget)
    return oState


def CustomAction51680(oHero, oEventCB, dInfo):
    oPerform = oHero.GetPerform(dInfo['PerformSID'])
    if not oPerform:
        return None
    oGame = oHero.m_Game
    iScene = oHero.m_Scene
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return None
    iDamRatio = oHero.GetCustomValue('PF51680DamRatio', 0)
    iDamMul = oHero.GetCustomValue('PF51680DamMul', 0)
    iDamRatioEle = oHero.GetCustomValue('PF51680DamRatioEle', 0)
    iOwner = oHero.m_ID
    lstSummon = oScene.GetObjectsByType('Summon')
    for iSummon in lstSummon:
        oSummon = oGame.GetObject(iSummon)
        if not oSummon or oSummon.m_Owner != iOwner:
            continue
        if dInfo['SummonSID'] and oSummon.m_SID != dInfo['SummonSID']:
            continue
        lstMonster = oSummon.Query('MonsterInPoison', [])
        if not lstMonster:
            continue
        for iMonster in lstMonster:
            oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
            if not oMonster:
                continue
            oState = oMonster.m_State.GetItemBySource(S7_FOGPOISON_STATE, oHero.m_ID)
            iStateCnt = oState.GetCount() if oState else 0
            iBaseDamRatio = iDamRatioEle if iDamRatioEle and oMonster.m_State.HasState(dInfo['EleStateSID']) else iDamRatio
            dData = {
                'Dam': int(iBaseDamRatio * (1 + iStateCnt * iDamMul / 100) // 100),
                'UseTrajectory': 1 }
            dPerform = {
                'Custom': dData }
            dData['LockTarget'] = [
                iMonster]
            dPerform['VID'] = iMonster
            dData['LockTrigger'] = iMonster
            cl_war.UsePerform(oHero, oPerform, dPerform)
        
    


def CustomAction51677(oHero, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'CurVID' in dMsgInfo:
        iVictim = dMsgInfo['CurVID']
    elif 'VID' in dMsgInfo:
        iVictim = dMsgInfo['VID']
    else:
        return None
    oGame = oHero.m_Game
    oVictim = oGame.GetObject(iVictim)
    if not oVictim:
        return None
    iMonsterSID = oVictim.m_SID
    clsMonsterData = oHero.m_Game.m_WarData.GetMonsterData(iMonsterSID)
    if not clsMonsterData:
        return None
    dReward = clsMonsterData.m_Reward
    if not dReward:
        return None
    iRound = oGame.m_WarMgr.m_Round
    if iRound not in dReward:
        cl_notify.GS2CDebugMsg(oGame, oHero.m_ID, '未配置战场%d小怪%s周目%d掉落' % (oGame.m_WarMgr.m_SID, iMonsterSID, iRound))
        iRound = sorted(dReward)[0]
    dReward = dReward[iRound]
    dFinalReward = { }
    dRatio = {
        MG_TRIGGER: oHero.GetCustomValue('PF51677Trigger'),
        MG_CASH: oHero.GetCustomValue('PF51677Cash'),
        MG_BULLET: oHero.GetCustomValue('PF51677Bullet') }
    for iMiniGame in dReward:
        iMiniGameProb = dReward[iMiniGame][0]
        if iMiniGameProb == 0:
            continue
        clsData = oGame.m_WarData.GetMiniGameData(iMiniGame)
        if not clsData or clsData.m_Type not in (MG_BULLET, MG_CASH, MG_TRIGGER):
            continue
        if clsData.m_Type == MG_TRIGGER and iMiniGame != MG_DROP_HP:
            continue
        iMiniGameOriTimes = dReward[iMiniGame][1]
        dFinalReward[iMiniGame] = (dRatio[clsData.m_Type], iMiniGameOriTimes)
    
    if not dFinalReward:
        return None
    dExtInfo = {
        'Abandoner': oVictim.m_ID,
        'OnlyRewardAttack': 1,
        'Source': MG_SOURCE_SEASONMODULE }
    cl_reward.RewardItemByMiniGame(oVictim, oHero.m_ID, dFinalReward, 'ModuleReward%d' % oHero.m_ID, MG_SOURCE_SEASONMODULE, dExtInfo)


def CustomAction51669(oHero, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'VID' not in dMsgInfo:
        return None
    iStateSID = dInfo['StateSID']
    if 'StateSID' not in dMsgInfo or dMsgInfo['StateSID'] != iStateSID:
        return None
    oPerform = oEventCB.GetObject()
    dTransInfo = oEventCB.GetCBTransInfo()
    dTransInfo['TargetList'] = [
        dMsgInfo['VID']]
    cl_evact.EventTargetGetRangeTargetByFightType(oHero, oEventCB, oPerform.GetArgValue('Distance'), WARRIOR_MONSTER, 1, 0, oPerform.GetArgValue('EnemyCnt'), 0, 1, 0, 0)
    lstTargetList = dTransInfo['TargetList']
    if not lstTargetList:
        return None
    oGame = oHero.m_Game
    iAttack = oHero.m_ID
    iPerform = oPerform.m_SID
    iCurFrame = oGame.GetFrameNum()
    iAddCount = oPerform.GetArgValue('SpreadCnt')
    dEventInfo = oEventCB.GetCBEventInfo()
    dArgs = {
        'MaxCnt': oPerform.GetArgValue('MaxCnt') }
    for iTarget in lstTargetList:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget or not FilterCD(oTarget, iAttack, iCurFrame):
            continue
        oState = oTarget.m_State.GetStateBySource(iStateSID, iAttack, 0)
        if not oState:
            oReason = cl_object.reason.CPerformReason(iPerform, oHero.m_ID, oHero.m_SID, oHero.m_FightType, None, { })
            dStatArgs = {
                'AID': iAttack,
                'RS': oReason,
                'pfid': iPerform,
                'PFLV': dEventInfo['PFLV'],
                'arg': dArgs }
            oState = cl_state.AddState(oTarget, iStateSID, STATE_TIME_FOREVER, 0, dStatArgs)
            if not oState:
                continue
            oState.Enable(oTarget)
        oState.AddCount(oTarget, iAddCount, 0)
    


def FilterCD(oTarget, iAttack, iCurFrame):
    sKey = '51669CDMark'
    dMarkCDInfo = oTarget.Query(sKey, { })
    if iAttack in dMarkCDInfo:
        (iRecordFrame, iFrame) = dMarkCDInfo[iAttack]
        if iRecordFrame + iFrame > iCurFrame:
            return 0
    return 1

