# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/custom/task/customaction.pyc
# RelativePath: clientlogic/cl_platformdata/custom/task/customaction.pyc
# Source Generated with Decompyle++
# File: customaction.pyc (Python 3.6)

from cl_commondefines import NWARRIOR_DROP_DEMON, VIRTUAL_ITEM_DROP, FAKEMG_GOLDENCUP, VIRTUAL_ITEM_GOLDENCUP, FAKEMG_UPGRADERELIC, NWARRIOR_DROP_RELIC, RELIC_TYPE_CURSE
from cl_only import SendAlert
from cl_cscommondef import QUALITY_TYPE_LOW, QUALITY_TYPE_NORMAL, QUALITY_TYPE_HIGH
from cl_object.logging import TaskLog
import cl_formula
import cl_evact

def CustomActionFailLog(oWarrior, oLifeCycle, dInfo):
    if 'ExtraInfo' in dInfo:
        TaskLog.Debug('%s %s %s break shield armor' % (oWarrior.m_Game, oWarrior.m_PlayerID, oLifeCycle.Key()))
    else:
        TaskLog.Debug('%s %s %s lifedisable' % (oWarrior.m_Game, oWarrior.m_PlayerID, oLifeCycle.Key()))


def CustomAction1301(oWarrior, oLifeCycle, dInfo):
    if 'ForceNum' not in dInfo or 'SID' not in dInfo:
        SendAlert('err', '%stask no rewardinfo customaction1301' % oLifeCycle.m_Key)
        return None
    iForceNum = cl_formula.GetResultByData(oWarrior, dInfo['ForceNum'], {
        'LifeCycle': oLifeCycle })
    vDropPos = oWarrior.GetGroundPos()
    pid = oWarrior.m_PlayerID
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
    oWarrior.m_Game.GetResMgr().CreateDrop(oWarrior.m_Scene, NWARRIOR_DROP_DEMON, vDropPos, [
        dInfo], { }, {
        'DropSource': pid,
        'Quality': 2 }, iOwner = oWarrior.m_ID)


def CustomAction1302(oWarrior, oLifeCycle, dInfo):
    oTask = oLifeCycle.GetObject()
    if 'RewardRelicLevel' not in dInfo or 'RewardNum' not in dInfo:
        SendAlert('err', '%stask no rewardinfo -customaction1302' % oLifeCycle.m_Key)
        return None
    iKillNum = oTask.GetRecordStat(1)
    iType = QUALITY_TYPE_LOW
    if 'RewardLegendRelic' in dInfo and iKillNum >= dInfo['RewardLegendRelic']:
        iType = QUALITY_TYPE_HIGH
    elif 'RewardRareRelic' in dInfo and iKillNum >= dInfo['RewardRareRelic']:
        iType = QUALITY_TYPE_NORMAL
    iRewardRelicLevel = dInfo['RewardRelicLevel']
    vDropPos = oWarrior.GetPos()
    lstRewardRelic = oWarrior.m_RelicCon.RandomChooseRelic(dInfo['RewardNum'], iExcludeCurseRelic = 1, iChooseQuality = iType, lstExcludeRelicLevel = [
        iRewardRelicLevel])
    lstReward = []
    for iRewardRelic in lstRewardRelic:
        dReward = {
            'item': VIRTUAL_ITEM_DROP,
            'info': {
                'DropType': NWARRIOR_DROP_RELIC,
                'DropInfo': [
                    iRewardRelic],
                'DropPos': vDropPos,
                'DropLevel': iRewardRelicLevel } }
        lstReward.append(dReward)
    
    TaskLog.Debug('%s 1302 taskreward pos %s %s' % (oWarrior.m_Game.m_ID, oWarrior.m_PlayerID, vDropPos))
    dRelicInfo = {
        FAKEMG_UPGRADERELIC: (0, lstReward, {
            'Player': oWarrior.m_ID,
            'ExtStaticInfo': { },
            'ExtraInfo': { } }) }
    oWarrior.m_Game.GetResMgr().CreateDrop(oWarrior.m_Scene, NWARRIOR_DROP_DEMON, vDropPos, [
        dRelicInfo], { }, {
        'DropSource': oWarrior.m_PlayerID,
        'Quality': 2 }, iOwner = oWarrior.m_ID)


def CheckAndSetPerformFlag(oTarget, oEventCB, iPerformSID):
    dPerformSID = oTarget.QuerySavedData('save.task1043', { })
    if iPerformSID in dPerformSID:
        return None
    dPerformSID[iPerformSID] = 1
    oTarget.SetSavedData('save.task1043', dPerformSID)
    cl_evact.CBAddWarSeasonTaskValue(oTarget, oEventCB, 1)


def CustomAction1043_1(oTarget, oEventCB, dInfo):
    oRelicCon = oTarget.m_RelicCon
    for oPerform in oRelicCon.GetAllRelicByType(RELIC_TYPE_CURSE):
        CheckAndSetPerformFlag(oTarget, oEventCB, oPerform.m_SID)
    


def CustomAction1043_2(oTarget, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'iPerform' not in dMsgInfo:
        return None
    CheckAndSetPerformFlag(oTarget, oEventCB, dMsgInfo['iPerform'])

