# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/w3020/phasechallenge.pyc
# RelativePath: clientlogic/cl_wardata/w3020/phasechallenge.pyc
# Source Generated with Decompyle++
# File: phasechallenge.pyc (Python 3.6)

from cl_resmgr.resdata import CPhaseChallengeData as CCustom
from cl_commondefines import CHALLENGE_GOAL_TARGET, CHALLENGE_SUCCESS, PHASE_CHALLENGE_BOXMONSTER, PHASE_CHALLENGE_GOLDENELITE, PHASE_CHALLENGE_KILLBOXMONSTER, PHASE_CHALLENGE_SEARCHTREASURE
from cl_newformula import Func204

class CPhaseChallengeData1001(CCustom):
    m_SID = 1001
    m_Type = PHASE_CHALLENGE_BOXMONSTER
    m_ChallengeName = '钱龙秘藏'
    m_ReadyNotify = '#s(219|挑战即将开始| $remain#$total|9032)'
    m_ChallengeNotify = '#s(220|钱龙秘藏|攻击钱龙获得奖励！| $remain#$total|9032)'
    m_SuccessNotify = '#s(221|钱龙秘藏|挑战成功!|9034)'
    m_FailedNotify = '#s(223|钱龙秘藏|挑战结束!|9033)'
    m_EffectState = 0
    m_ReadyTime = 500
    m_ChallengeTime = 10000
    m_Reward = {
        CHALLENGE_GOAL_TARGET: {
            2417: (10000, 1),
            2419: (10000, 1),
            105: (10000, 30),
            3021: (10000, 8),
            401: (5000, 1) },
        CHALLENGE_SUCCESS: {
            2416: (10000, 1),
            2418: (10000, 1),
            105: (10000, 50),
            3022: (10000, 12),
            401: (10000, 1) } }
    m_Param = (23432, 60, 90, 2132, 50, 0, 2134, 1000, 300, 15, 20)
    m_IgnoreSingle = 0
    m_HpConfig = {
        1: 1,
        2: 1.6,
        3: 2.2,
        4: 2.8 }


class CPhaseChallengeData1002(CCustom):
    m_SID = 1002
    m_Type = PHASE_CHALLENGE_KILLBOXMONSTER
    m_ChallengeName = '狩猎钱龙'
    m_ReadyNotify = '#s(219|挑战即将开始| $remain#$total|9032)'
    m_ChallengeNotify = '#s(220|狩猎钱龙|击败$target只钱龙\n（$cur/ $target）| $remain#$total|9032)'
    m_SuccessNotify = '#s(221|狩猎钱龙|挑战成功!|9034)'
    m_FailedNotify = '#s(223|狩猎钱龙|挑战结束!|9033)'
    m_EffectState = 0
    m_ReadyTime = 300
    m_ChallengeTime = 10000
    m_Reward = {
        CHALLENGE_GOAL_TARGET: {
            2417: (10000, 1),
            2419: (10000, 1),
            105: (10000, 30),
            3021: (10000, 8),
            401: (5000, 1) },
        CHALLENGE_SUCCESS: {
            2416: (10000, 1),
            2418: (10000, 1),
            105: (10000, 50),
            3022: (10000, 12),
            401: (10000, 1) } }
    m_Param = (23433, 50, 140, (lambda *a: 6 + Func204(*a)), {
        1002: 1 }, 0, (lambda *a: 4 + Func204(*a)), 50, 0, 0)
    m_IgnoreSingle = 0
    m_HpConfig = {
        1: 1,
        2: 1.6,
        3: 2.2,
        4: 2.8 }


class CPhaseChallengeData1003(CCustom):
    m_SID = 1003
    m_Type = PHASE_CHALLENGE_SEARCHTREASURE
    m_ChallengeName = '限时寻宝'
    m_ReadyNotify = '#s(219|请尽快前往寻宝区域！| $remain#$total|9032)'
    m_ChallengeNotify = '#s(225|限时寻宝|坚守寻宝区域，搜寻真正的宝藏！| $remain#$total|9032)'
    m_SuccessNotify = '#s(221|限时寻宝|宝藏已被找到！|9124)'
    m_FailedNotify = '#s(223|限时寻宝|时间到！寻宝结束！|9127)'
    m_EffectState = 0
    m_ReadyTime = 500
    m_ChallengeTime = 10000
    m_Reward = {
        CHALLENGE_GOAL_TARGET: {
            105: (10000, 5),
            3021: (10000, 8),
            401: (10000, 1) },
        CHALLENGE_SUCCESS: {
            2416: (10000, 1),
            2418: (10000, 1),
            105: (10000, 35),
            3022: (10000, 12),
            401: (10000, 1) } }
    m_Param = ((lambda *a: 1390 - Func204(*a) * 190), (lambda *a: Func204(*a) + 3), {
        1100: 1,
        1101: 1,
        1102: 1,
        1103: 1,
        1104: 1,
        1105: 1 }, 6, 1031, 20, 0, (lambda *a: (3 + Func204(*a)) * 50 + 100), 150)
    m_IgnoreSingle = 0
    m_HpConfig = { }


class CPhaseChallengeData1004(CCustom):
    m_SID = 1004
    m_Type = PHASE_CHALLENGE_GOLDENELITE
    m_ChallengeName = '黄金精英怪'
    m_ReadyNotify = '#s(219|【黄金精英怪】即将出现！| $remain#$total|9032)'
    m_ChallengeNotify = '#s(220|黄金精英怪|攻击黄金精英怪获得奖励！| $remain#$total|9032)'
    m_SuccessNotify = '#s(221|黄金精英怪|挑战成功!||9034)'
    m_FailedNotify = '#s(223|黄金精英怪|挑战结束!||9033)'
    m_EffectState = 0
    m_ReadyTime = 500
    m_ChallengeTime = 10000
    m_Reward = {
        CHALLENGE_GOAL_TARGET: {
            105: (10000, 3),
            3022: (10000, 2),
            401: (10000, 1) },
        CHALLENGE_SUCCESS: {
            2416: (10000, 1),
            2418: (10000, 1),
            105: (10000, 40),
            3023: (10000, 6),
            401: (10000, 1) } }
    m_Param = (33001, 90, 140, 24021, 0, 20, 1000, 0, 50, 0, 0, 15, 20)
    m_IgnoreSingle = 0
    m_HpConfig = {
        1: 1,
        2: 1.6,
        3: 2.2,
        4: 2.8 }


class CPhaseChallengeData2001(CCustom):
    m_SID = 2001
    m_Type = PHASE_CHALLENGE_BOXMONSTER
    m_ChallengeName = '钱龙秘藏'
    m_ReadyNotify = '#s(219|挑战即将开始| $remain#$total|9032)'
    m_ChallengeNotify = '#s(220|钱龙秘藏|攻击钱龙获得奖励！| $remain#$total|9032)'
    m_SuccessNotify = '#s(221|钱龙秘藏|挑战成功!|9034)'
    m_FailedNotify = '#s(223|钱龙秘藏|挑战结束!|9033)'
    m_EffectState = 0
    m_ReadyTime = 500
    m_ChallengeTime = 10000
    m_Reward = {
        CHALLENGE_GOAL_TARGET: {
            2417: (10000, 1),
            2419: (10000, 1),
            105: (10000, 30),
            3021: (10000, 8),
            401: (5000, 1) },
        CHALLENGE_SUCCESS: {
            2416: (10000, 1),
            2418: (10000, 1),
            105: (10000, 50),
            3022: (10000, 12),
            401: (10000, 1) } }
    m_Param = (23422, 50, 80, 2132, 50, 0, 2134, 1000, 300, 15, 20)
    m_IgnoreSingle = 0
    m_HpConfig = {
        1: 1,
        2: 1.6,
        3: 2.2,
        4: 2.8 }


class CPhaseChallengeData2002(CCustom):
    m_SID = 2002
    m_Type = PHASE_CHALLENGE_KILLBOXMONSTER
    m_ChallengeName = '狩猎钱龙'
    m_ReadyNotify = '#s(219|挑战即将开始| $remain#$total|9032)'
    m_ChallengeNotify = '#s(220|狩猎钱龙|击败$target只钱龙\n（$cur/ $target）| $remain#$total|9032)'
    m_SuccessNotify = '#s(221|狩猎钱龙|挑战成功!|9034)'
    m_FailedNotify = '#s(223|狩猎钱龙|挑战结束!|9033)'
    m_EffectState = 0
    m_ReadyTime = 300
    m_ChallengeTime = 10000
    m_Reward = {
        CHALLENGE_GOAL_TARGET: {
            2417: (10000, 1),
            2419: (10000, 1),
            105: (10000, 30),
            3021: (10000, 8),
            401: (5000, 1) },
        CHALLENGE_SUCCESS: {
            2416: (10000, 1),
            2418: (10000, 1),
            105: (10000, 50),
            3022: (10000, 12),
            401: (10000, 1) } }
    m_Param = (23423, 50, 120, (lambda *a: 6 + Func204(*a)), {
        2002: 1 }, 0, (lambda *a: 4 + Func204(*a)), 50, 0, 0)
    m_IgnoreSingle = 0
    m_HpConfig = {
        1: 1,
        2: 1.6,
        3: 2.2,
        4: 2.8 }


class CPhaseChallengeData2003(CCustom):
    m_SID = 2003
    m_Type = PHASE_CHALLENGE_SEARCHTREASURE
    m_ChallengeName = '限时寻宝'
    m_ReadyNotify = '#s(219|请尽快前往寻宝区域！| $remain#$total|9032)'
    m_ChallengeNotify = '#s(225|限时寻宝|坚守寻宝区域，搜寻真正的宝藏！| $remain#$total|9032)'
    m_SuccessNotify = '#s(221|限时寻宝|宝藏已被找到！|9124)'
    m_FailedNotify = '#s(223|限时寻宝|时间到！寻宝结束！|9127)'
    m_EffectState = 0
    m_ReadyTime = 500
    m_ChallengeTime = 10000
    m_Reward = {
        CHALLENGE_GOAL_TARGET: {
            105: (10000, 5),
            3021: (10000, 8),
            401: (10000, 1) },
        CHALLENGE_SUCCESS: {
            2416: (10000, 1),
            2418: (10000, 1),
            105: (10000, 35),
            3022: (10000, 12),
            401: (10000, 1) } }
    m_Param = ((lambda *a: 1390 - Func204(*a) * 190), (lambda *a: Func204(*a) + 3), {
        2100: 1,
        2101: 1,
        2102: 1,
        2103: 1,
        2104: 1,
        2105: 1 }, 5, 1033, 15, 0, (lambda *a: (3 + Func204(*a)) * 50 + 100), 150)
    m_IgnoreSingle = 0
    m_HpConfig = { }

