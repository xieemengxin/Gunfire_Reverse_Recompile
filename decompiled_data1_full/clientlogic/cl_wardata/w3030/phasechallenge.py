# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/w3030/phasechallenge.pyc
# RelativePath: clientlogic/cl_wardata/w3030/phasechallenge.pyc
# Source Generated with Decompyle++
# File: phasechallenge.pyc (Python 3.6)

from cl_resmgr.resdata import CPhaseChallengeData as CCustom
from cl_commondefines import CHALLENGE_GOAL_TARGET, CHALLENGE_SUCCESS, PHASE_CHALLENGE_BOXMONSTER, PHASE_CHALLENGE_KILLBOXMONSTER, PHASE_CHALLENGE_SEARCHTREASURE, PHASE_CHALLENGE_SINGLEPOINTOCCUPY
from cl_newformula import Func204, Func241, Func242

class CPhaseChallengeData2001(CCustom):
    m_SID = 2001
    m_Type = PHASE_CHALLENGE_BOXMONSTER
    m_ChallengeName = '钱龙秘藏'
    m_ReadyNotify = '#s(219|挑战即将开始| $remain#$total|9032)'
    m_ChallengeNotify = '#s(226|击败钱龙获得奖励！| $remain#$total|9032)'
    m_SuccessNotify = '#s(221|挑战成功!|9034)'
    m_FailedNotify = '#s(223|挑战结束!|9033)'
    m_EffectState = 0
    m_ReadyTime = 500
    
    m_ChallengeTime = lambda *a: Func241(*a) - 500
    m_Reward = {
        CHALLENGE_SUCCESS: {
            2416: (10000, 1),
            2418: (10000, 1),
            401: (10000, 1) } }
    m_Param = (23422, 5, 30, 0, 50, 0, 2134, 1000, 300, 15, 20)
    m_IgnoreSingle = 0
    m_HpConfig = {
        1: 1,
        2: 1.2,
        3: 1.4,
        4: 1.6 }


class CPhaseChallengeData2002(CCustom):
    m_SID = 2002
    m_Type = PHASE_CHALLENGE_KILLBOXMONSTER
    m_ChallengeName = '狩猎钱龙'
    m_ReadyNotify = '#s(219|挑战即将开始| $remain#$total|9032)'
    m_ChallengeNotify = '#s(226|击败$target只钱龙\n（$cur/ $target）| $remain#$total|9032)'
    m_SuccessNotify = '#s(221|挑战成功!|9034)'
    m_FailedNotify = '#s(223|挑战结束!|9033)'
    m_EffectState = 0
    m_ReadyTime = 300
    m_ChallengeTime = 7500
    m_Reward = {
        CHALLENGE_GOAL_TARGET: {
            2417: (10000, 1),
            2419: (10000, 1),
            401: (5000, 1) },
        CHALLENGE_SUCCESS: {
            2416: (10000, 1),
            2418: (10000, 1),
            401: (10000, 1) } }
    m_Param = (23423, 50, 120, (lambda *a: 6 + Func204(*a)), {
        2002: 1 }, 0, (lambda *a: 4 + Func204(*a)), 50, 0, 0)
    m_IgnoreSingle = 0
    m_HpConfig = {
        1: 1,
        2: 1.2,
        3: 1.4,
        4: 1.6 }


class CPhaseChallengeData2003(CCustom):
    m_SID = 2003
    m_Type = PHASE_CHALLENGE_SEARCHTREASURE
    m_ChallengeName = '限时寻宝'
    m_ReadyNotify = '#s(219|请尽快前往寻宝区域！| $remain#$total|9032)'
    m_ChallengeNotify = '#s(225|坚守寻宝区域，搜寻真正的宝藏！| $remain#$total|9032)'
    m_SuccessNotify = '#s(221|宝藏已被找到！|9124)'
    m_FailedNotify = '#s(223|时间到！寻宝结束！|9127)'
    m_EffectState = 0
    m_ReadyTime = 500
    m_ChallengeTime = 7500
    m_Reward = {
        CHALLENGE_GOAL_TARGET: {
            2417: (10000, 1),
            2419: (10000, 1),
            401: (5000, 1) },
        CHALLENGE_SUCCESS: {
            2416: (10000, 1),
            2418: (10000, 1),
            401: (10000, 1) } }
    m_Param = ((lambda *a: 1390 - Func204(*a) * 190), (lambda *a: Func204(*a) + 3), {
        2100: 1,
        2002: 1,
        2101: 1 }, 5, 1033, 15, 0, (lambda *a: (3 + Func204(*a)) * 50 + 100), 150)
    m_IgnoreSingle = 0
    m_HpConfig = { }


class CPhaseChallengeData2004(CCustom):
    m_SID = 2004
    m_Type = PHASE_CHALLENGE_SINGLEPOINTOCCUPY
    m_ChallengeName = '单点占领'
    m_ReadyNotify = '#s(219|挑战即将开始| $remain#$total|9032)'
    m_ChallengeNotify = '#s(225|占领区域，坚守阵地！| $remain#$total|9032)'
    m_SuccessNotify = '#s(221|挑战成功!|9124)'
    m_FailedNotify = '#s(223|时间到！挑战结束！|9127)'
    m_EffectState = 0
    m_ReadyTime = 300
    
    m_ChallengeTime = lambda *a: Func241(*a) - 300
    m_Reward = {
        CHALLENGE_SUCCESS: {
            2416: (10000, 1),
            2418: (10000, 1),
            401: (10000, 1) } }
    m_Param = ((lambda *a: 313 * (0.75 + 0.25 * Func242(*a)) / (0.75 + 0.25 * Func204(*a))), 6, 1033, 20, 1032, 1, 50)
    m_IgnoreSingle = 0
    m_HpConfig = { }


class CPhaseChallengeData2005(CCustom):
    m_SID = 2005
    m_Type = PHASE_CHALLENGE_SINGLEPOINTOCCUPY
    m_ChallengeName = '单点占领'
    m_ReadyNotify = '#s(219|挑战即将开始| $remain#$total|9032)'
    m_ChallengeNotify = '#s(225|占领区域，坚守阵地！| $remain#$total|9032)'
    m_SuccessNotify = '#s(221|挑战成功!|9124)'
    m_FailedNotify = '#s(223|时间到！挑战结束！|9127)'
    m_EffectState = 0
    m_ReadyTime = 300
    
    m_ChallengeTime = lambda *a: Func241(*a) - 300
    m_Reward = {
        CHALLENGE_SUCCESS: {
            2416: (10000, 1),
            2418: (10000, 1),
            401: (10000, 1) } }
    m_Param = ((lambda *a: 313 * (0.75 + 0.25 * Func242(*a)) / (0.75 + 0.25 * Func204(*a))), 6, 1033, 20, 1032, 2, 50)
    m_IgnoreSingle = 0
    m_HpConfig = { }

