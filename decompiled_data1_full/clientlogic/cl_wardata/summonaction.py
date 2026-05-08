# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/summonaction.pyc
# RelativePath: clientlogic/cl_wardata/summonaction.pyc
# Source Generated with Decompyle++
# File: summonaction.pyc (Python 3.6)

from cl_commondefines import DAM_USE_HP, DAM_TYPE_SCENE, MG_SOURCE_KILLSUMMON, SIDE_TYPE_HERO
from cl_only import Time2Frame, Functor, PY_FLAG_DEAD
import cl_reward
import cl_msgcenter
import cl_object

def SummonSetCircleParam(oSummon, iTime, iCnt, iAction, iUpFrame):
    oSummon.SetCircleParam(iTime, iCnt, iAction, iUpFrame)


def SummonSetDieWithOwner(oSummon, iNoDieWhenCartoonUse):
    iOwner = oSummon.m_Owner
    oFunc = Functor(DieWithOwner, iNoDieWhenCartoonUse)
    sFlag = 'DieWithOwner'
    cl_msgcenter.AddAttentionFunc(oSummon, iOwner, cl_msgcenter.MSG_WAR_DIE, oFunc, sFlag)
    cl_msgcenter.AddAttentionFunc(oSummon, iOwner, cl_msgcenter.MSG_WAR_HATCH, oFunc, sFlag)


def DieWithOwner(iNoDieWhenCartoonUse, oSummon, oOwenr, dMsgInfo):
    iOwner = oSummon.m_Owner
    sFlag = 'DieWithOwner'
    cl_msgcenter.DoneAttention(oSummon, iOwner, cl_msgcenter.MSG_WAR_DIE, sFlag)
    cl_msgcenter.DoneAttention(oSummon, iOwner, cl_msgcenter.MSG_WAR_HATCH, sFlag)
    if oSummon.IsDead():
        return None
    if iNoDieWhenCartoonUse and oSummon.Query('CartoonUse'):
        return None
    oReason = cl_object.reason.CStrReason('DieWithOwner', None, {
        'DamType': DAM_TYPE_SCENE | DAM_USE_HP })
    oSummon.HPModifyDam(0, [
        [
            oSummon.HP(),
            oReason]])


def SummonSetDieRemoveOwnerState(oSummon, iState):
    cl_msgcenter.AddAttentionFunc(oSummon, oSummon.m_ID, cl_msgcenter.MSG_WAR_DIE, Functor(DieRemoveStateByDie, iState), 'DieRemoveOwnerState')


def DieRemoveStateByDie(iState, oSummon, oOwenr, dMsgInfo):
    cl_msgcenter.DoneAttention(oSummon, oSummon.m_Owner, cl_msgcenter.MSG_WAR_DIE, 'DieRemoveOwnerState')
    oGame = oSummon.m_Game
    oOwner = oGame.GetObject(oSummon.m_Owner, PY_FLAG_DEAD)
    if not oOwner:
        return None
    oState = oOwner.m_State.GetItemBySID(iState)
    if not oState:
        return None
    oOwner.m_State.RemoveItem(oState.m_ID)


def SummonDieRewardItemList(oSummon, oKiller, dMiniGame, iDelay, iLimitHeroSide):
    if iLimitHeroSide and oKiller and oKiller.m_Side != SIDE_TYPE_HERO:
        return None
    iHero = oKiller.m_ID if oKiller else 0
    sKey = 'SummonDieReward'
    dExtInfo = {
        'CalOffset': 0,
        'CheckGoldenCup': 1 }
    dReward = { }
    for iMiniGame, dInfo in dMiniGame.items():
        dReward[iMiniGame] = (dInfo['Prop'], dInfo['Times'])
    
    if not iDelay:
        cl_reward.RewardItemByMiniGame(oSummon, iHero, dReward, sKey, MG_SOURCE_KILLSUMMON, dExtInfo)
    else:
        oSummon.Call_Out(Functor(cl_reward.RewardItemByMiniGame, oSummon, iHero, dReward, sKey, MG_SOURCE_KILLSUMMON, dExtInfo), Time2Frame(iDelay), sKey)

