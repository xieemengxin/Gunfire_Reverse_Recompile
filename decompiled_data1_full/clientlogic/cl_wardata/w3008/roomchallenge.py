# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/w3008/roomchallenge.pyc
# RelativePath: clientlogic/cl_wardata/w3008/roomchallenge.pyc
# Source Generated with Decompyle++
# File: roomchallenge.pyc (Python 3.6)

from cl_resmgr.resdata import CRoomChallengeData as CCustom
from cl_commondefines import ALLVERLAYER_VALID, CHALLENGE_ABERRANCE, CHALLENGE_APPENDSKILL, CHALLENGE_BOXMONSTER, CHALLENGE_DEFEND, CHALLENGE_ELITE, CHALLENGE_EXTRAMONSTER, CHALLENGE_KILLSUMMON, CHALLENGE_LIMITCONVOY, CHALLENGE_LIMITDEFEND, CHALLENGE_LIMITLIVE, CHALLENGE_LIMITTIME, CHALLENGE_NOTIFY, CHALLENGE_NOTIFYLIMITTIME, CHALLENGE_PLAYERPERFORM, CHALLENGE_TRAP

class CRoomChallengeData1001(CCustom):
    m_SID = 1001
    m_Type = CHALLENGE_KILLSUMMON
    m_ChallengeName = '妖气转生'
    m_ChallengeNotify = '#s(215|1001|9032)'
    m_SuccessNotify = '#s(216|1001|9034)'
    m_FailedNotify = '#s(182|敌人被击败后会化身独角金龟|9033)'
    m_EffectState = 20033
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (10000, 1) },
        2: {
            401: (10000, 1),
            2401: (10000, 1) },
        3: {
            401: (10000, 1),
            2401: (10000, 1) } }
    m_Param = ({
        20011: 100 },)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1002(CCustom):
    m_SID = 1002
    m_Type = CHALLENGE_EXTRAMONSTER
    m_ChallengeName = '精英坐镇'
    m_ChallengeNotify = '#s(215|1002|9032)'
    m_SuccessNotify = '#s(216|1002|9034)'
    m_FailedNotify = '#s(186|精英马头锐士出现了！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (31231,)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = [
        (1110502, 1),
        (1110502, 6),
        (1110502, 7),
        (1110502, 9)]


class CRoomChallengeData1003(CCustom):
    m_SID = 1003
    m_Type = CHALLENGE_APPENDSKILL
    m_ChallengeName = '妖气附体'
    m_ChallengeNotify = '#s(215|1003|9032)'
    m_SuccessNotify = '#s(216|1003|9034)'
    m_FailedNotify = '#s(182|敌人被击败后会发生爆炸|9033)'
    m_EffectState = 20032
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (10000, 1) },
        2: {
            401: (10000, 1),
            2401: (10000, 1) },
        3: {
            401: (10000, 1),
            2401: (10000, 1) } }
    m_Param = (4075, None, None)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = [
        (1110103, 1),
        (1110303, 5),
        (1110502, 8)]


class CRoomChallengeData1004(CCustom):
    m_SID = 1004
    m_Type = CHALLENGE_ABERRANCE
    m_ChallengeName = '妖气惊变'
    m_ChallengeNotify = '#s(215|1004|9032)'
    m_SuccessNotify = '#s(216|1004|9034)'
    m_FailedNotify = '#s(182|敌人都变成硝石勇士了！|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (10000, 1) },
        2: {
            401: (10000, 1),
            2401: (10000, 1) },
        3: {
            401: (10000, 1),
            2401: (10000, 1) } }
    m_Param = (22211,)
    m_ExcludeLastRoom = 1
    m_ExcludeArea = [
        (1110103, 1),
        (1110303, 5)]


class CRoomChallengeData1005(CCustom):
    m_SID = 1005
    m_Type = CHALLENGE_KILLSUMMON
    m_ChallengeName = '妖气转生'
    m_ChallengeNotify = '#s(215|1005|9032)'
    m_SuccessNotify = '#s(216|1005|9034)'
    m_FailedNotify = '#s(182|敌人被击败后化身大漠幼豚|9033)'
    m_EffectState = 20033
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (10000, 1) },
        2: {
            401: (10000, 1),
            2401: (10000, 1) },
        3: {
            401: (10000, 1),
            2401: (10000, 1) } }
    m_Param = ({
        20021: 100 },)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1006(CCustom):
    m_SID = 1006
    m_Type = CHALLENGE_EXTRAMONSTER
    m_ChallengeName = '精英坐镇'
    m_ChallengeNotify = '#s(215|1006|9032)'
    m_SuccessNotify = '#s(216|1006|9034)'
    m_FailedNotify = '#s(186|精英沙蜥出现了！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (32421,)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1007(CCustom):
    m_SID = 1007
    m_Type = CHALLENGE_EXTRAMONSTER
    m_ChallengeName = '精英坐镇'
    m_ChallengeNotify = '#s(215|1007|9032)'
    m_SuccessNotify = '#s(216|1007|9034)'
    m_FailedNotify = '#s(186|精英土狼出现了！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (30211,)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1008(CCustom):
    m_SID = 1008
    m_Type = CHALLENGE_ABERRANCE
    m_ChallengeName = '妖气惊变'
    m_ChallengeNotify = '#s(215|1008|9032)'
    m_SuccessNotify = '#s(216|1008|9034)'
    m_FailedNotify = '#s(182|敌人都变成右矛兵了！|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (10000, 1) },
        2: {
            401: (10000, 1),
            2401: (10000, 1) },
        3: {
            401: (10000, 1),
            2401: (10000, 1) } }
    m_Param = (20834,)
    m_ExcludeLastRoom = 1
    m_ExcludeArea = [
        (1110303, 5),
        (1110502, 8)]


class CRoomChallengeData1009(CCustom):
    m_SID = 1009
    m_Type = CHALLENGE_ABERRANCE
    m_ChallengeName = '妖气惊变'
    m_ChallengeNotify = '#s(215|1009|9032)'
    m_SuccessNotify = '#s(216|1009|9034)'
    m_FailedNotify = '#s(182|敌人都变成流寇电刀手了！|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (10000, 1) },
        2: {
            401: (10000, 1),
            2401: (10000, 1) },
        3: {
            401: (10000, 1),
            2401: (10000, 1) } }
    m_Param = (20852,)
    m_ExcludeLastRoom = 1
    m_ExcludeArea = [
        (1110103, 1)]


class CRoomChallengeData1010(CCustom):
    m_SID = 1010
    m_Type = CHALLENGE_LIMITTIME
    m_ChallengeName = '争分夺秒'
    m_ChallengeNotify = '#s(175|限时通过获得额外奖励| $remain#$total|9032)'
    m_SuccessNotify = '#s(185|限时通过获得额外奖励|9034)'
    m_FailedNotify = '#s(186|限时通过获得额外奖励|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (5000,)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1011(CCustom):
    m_SID = 1011
    m_Type = CHALLENGE_EXTRAMONSTER
    m_ChallengeName = '精英突入'
    m_ChallengeNotify = '#s(215|1011|9032)'
    m_SuccessNotify = '#s(216|1011|9034)'
    m_FailedNotify = '#s(186|精英沙蜥出现了！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (32421,)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1012(CCustom):
    m_SID = 1012
    m_Type = CHALLENGE_LIMITCONVOY
    m_ChallengeName = '争分夺秒'
    m_ChallengeNotify = '#s(172|限定时间护送目标到达终点!|9034)'
    m_SuccessNotify = '#s(181|限定时间护送目标到达目标点!|9034)'
    m_FailedNotify = '#s(182|限定时间护送目标到达目标点!|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (18000, 1039001)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1013(CCustom):
    m_SID = 1013
    m_Type = CHALLENGE_DEFEND
    m_ChallengeName = '守护封印'
    m_ChallengeNotify = '#s(171|阻止怪物破坏封印|9032)'
    m_SuccessNotify = '#s(183|阻止怪物破坏封印|9034)'
    m_FailedNotify = '#s(184|阻止怪物破坏封印|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (1121001, 300, 300, 0)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1014(CCustom):
    m_SID = 1014
    m_Type = CHALLENGE_LIMITDEFEND
    m_ChallengeName = '守护封印'
    m_ChallengeNotify = '#s(172|封印稳定中| $remain#$total|9032)'
    m_SuccessNotify = '#s(183|封印稳定中|9034)'
    m_FailedNotify = '#s(184|封印稳定中!|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (1121001, 18000, 300, 300, 0)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1015(CCustom):
    m_SID = 1015
    m_Type = CHALLENGE_APPENDSKILL
    m_ChallengeName = '弱点打击'
    m_ChallengeNotify = '#s(215|1015|9032)'
    m_SuccessNotify = '#s(216|1015|9034)'
    m_FailedNotify = '#s(182|暴击伤害提高，其他伤害降低！|9033)'
    m_EffectState = 20035
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (10000, 1) },
        2: {
            401: (10000, 1),
            2401: (10000, 1) },
        3: {
            401: (10000, 1),
            2401: (10000, 1) } }
    m_Param = (4106, None, None)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = [
        (1110502, 8)]


class CRoomChallengeData1016(CCustom):
    m_SID = 1016
    m_Type = CHALLENGE_EXTRAMONSTER
    m_ChallengeName = '精英坐镇'
    m_ChallengeNotify = '#s(215|1016|9032)'
    m_SuccessNotify = '#s(216|1016|9034)'
    m_FailedNotify = '#s(186|精英虚无僧出现了！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (32831,)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1017(CCustom):
    m_SID = 1017
    m_Type = CHALLENGE_EXTRAMONSTER
    m_ChallengeName = '精英坐镇'
    m_ChallengeNotify = '#s(215|1017|9032)'
    m_SuccessNotify = '#s(216|1017|9034)'
    m_FailedNotify = '#s(186|精英鲶人武士出现了！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (30871,)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1018(CCustom):
    m_SID = 1018
    m_Type = CHALLENGE_EXTRAMONSTER
    m_ChallengeName = '精英坐镇'
    m_ChallengeNotify = '#s(215|1018|9032)'
    m_SuccessNotify = '#s(216|1018|9034)'
    m_FailedNotify = '#s(186|精英流寇帮凶出现了！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (31251,)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1019(CCustom):
    m_SID = 1019
    m_Type = CHALLENGE_ABERRANCE
    m_ChallengeName = '妖气惊变'
    m_ChallengeNotify = '#s(215|1019|9032)'
    m_SuccessNotify = '#s(216|1019|9034)'
    m_FailedNotify = '#s(182|敌人都变成剧毒沙蜥了！|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (10000, 1) },
        2: {
            401: (10000, 1),
            2401: (10000, 1) },
        3: {
            401: (10000, 1),
            2401: (10000, 1) } }
    m_Param = (22441,)
    m_ExcludeLastRoom = 1
    m_ExcludeArea = []


class CRoomChallengeData1020(CCustom):
    m_SID = 1020
    m_Type = CHALLENGE_LIMITLIVE
    m_ChallengeName = '争分夺秒'
    m_ChallengeNotify = '#s(176|限时存活!| $remain#$total|9032)'
    m_SuccessNotify = '#s(181|限时存活!|9034)'
    m_FailedNotify = '#s(182|限时存活!|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (0, 12000)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1021(CCustom):
    m_SID = 1021
    m_Type = CHALLENGE_PLAYERPERFORM
    m_ChallengeName = '越战越勇'
    m_ChallengeNotify = '#s(215|1021|9032)'
    m_SuccessNotify = '#s(216|10219034)'
    m_FailedNotify = '#s(182|持续受伤！击败敌人获得治疗|9033)'
    m_EffectState = 20036
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (10000, 1) },
        2: {
            401: (10000, 1),
            2401: (10000, 1) },
        3: {
            401: (10000, 1),
            2401: (10000, 1) } }
    m_Param = (4114, None)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1022(CCustom):
    m_SID = 1022
    m_Type = CHALLENGE_PLAYERPERFORM
    m_ChallengeName = '越战越勇'
    m_ChallengeNotify = '#s(215|1022|9032)'
    m_SuccessNotify = '#s(216|1022|9034)'
    m_FailedNotify = '#s(182|持续受伤！击败敌人获得治疗|9033)'
    m_EffectState = 20036
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (10000, 1) },
        2: {
            401: (10000, 1),
            2401: (10000, 1) },
        3: {
            401: (10000, 1),
            2401: (10000, 1) } }
    m_Param = (4115, None)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1023(CCustom):
    m_SID = 1023
    m_Type = CHALLENGE_LIMITCONVOY
    m_ChallengeName = '争分夺秒'
    m_ChallengeNotify = '#s(172|限定时间护送目标到达目标点!|9034)'
    m_SuccessNotify = '#s(181|限定时间护送目标到达目标点!|9034)'
    m_FailedNotify = '#s(182|限定时间护送目标到达目标点!|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (28000, 1039001)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1024(CCustom):
    m_SID = 1024
    m_Type = CHALLENGE_KILLSUMMON
    m_ChallengeName = '妖气转生'
    m_ChallengeNotify = '#s(215|1024|9032)'
    m_SuccessNotify = '#s(216|1024|9034)'
    m_FailedNotify = '#s(182|敌人被击败后化身自爆灯笼鬼|9033)'
    m_EffectState = 20033
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (10000, 1) },
        2: {
            401: (10000, 1),
            2401: (10000, 1) },
        3: {
            401: (10000, 1),
            2401: (10000, 1) } }
    m_Param = ({
        20041: 100 },)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1025(CCustom):
    m_SID = 1025
    m_Type = CHALLENGE_KILLSUMMON
    m_ChallengeName = '妖气转生'
    m_ChallengeNotify = '#s(215|1025|9032)'
    m_SuccessNotify = '#s(216|1025|9034)'
    m_FailedNotify = '#s(182|敌人被击败后化身招潮蟹|9033)'
    m_EffectState = 20033
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (10000, 1) },
        2: {
            401: (10000, 1),
            2401: (10000, 1) },
        3: {
            401: (10000, 1),
            2401: (10000, 1) } }
    m_Param = ({
        23211: 100 },)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1026(CCustom):
    m_SID = 1026
    m_Type = CHALLENGE_ABERRANCE
    m_ChallengeName = '妖气惊变'
    m_ChallengeNotify = '#s(215|1026|9032)'
    m_SuccessNotify = '#s(216|1026|9034)'
    m_FailedNotify = '#s(182|敌人都变成马贼军师了！|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (10000, 1) },
        2: {
            401: (10000, 1),
            2401: (10000, 1) },
        3: {
            401: (10000, 1),
            2401: (10000, 1) } }
    m_Param = (21622,)
    m_ExcludeLastRoom = 1
    m_ExcludeArea = []


class CRoomChallengeData1027(CCustom):
    m_SID = 1027
    m_Type = CHALLENGE_KILLSUMMON
    m_ChallengeName = '妖气转生'
    m_ChallengeNotify = '#s(215|1027|9032)'
    m_SuccessNotify = '#s(216|1027|9034)'
    m_FailedNotify = '#s(182|敌人被击败后化身大漠沙虫|9033)'
    m_EffectState = 20033
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (10000, 1) },
        2: {
            401: (10000, 1),
            2401: (10000, 1) },
        3: {
            401: (10000, 1),
            2401: (10000, 1) } }
    m_Param = ({
        20422: 100 },)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1028(CCustom):
    m_SID = 1028
    m_Type = CHALLENGE_ABERRANCE
    m_ChallengeName = '妖气惊变'
    m_ChallengeNotify = '#s(215|1028|9032)'
    m_SuccessNotify = '#s(216|1028|9034)'
    m_FailedNotify = '#s(182|敌人都变成鲶人武士了！|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (10000, 1) },
        2: {
            401: (10000, 1),
            2401: (10000, 1) },
        3: {
            401: (10000, 1),
            2401: (10000, 1) } }
    m_Param = (20873,)
    m_ExcludeLastRoom = 1
    m_ExcludeArea = []


class CRoomChallengeData1029(CCustom):
    m_SID = 1029
    m_Type = CHALLENGE_ABERRANCE
    m_ChallengeName = '妖气惊变'
    m_ChallengeNotify = '#s(215|1029|9032)'
    m_SuccessNotify = '#s(216|1029|9034)'
    m_FailedNotify = '#s(182|敌人都变成鲶人蚌兵了！|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (10000, 1) },
        2: {
            401: (10000, 1),
            2401: (10000, 1) },
        3: {
            401: (10000, 1),
            2401: (10000, 1) } }
    m_Param = (21062,)
    m_ExcludeLastRoom = 1
    m_ExcludeArea = []


class CRoomChallengeData1030(CCustom):
    m_SID = 1030
    m_Type = CHALLENGE_APPENDSKILL
    m_ChallengeName = '妖气附体'
    m_ChallengeNotify = '#s(215|1030|9032)'
    m_SuccessNotify = '#s(216|1030|9034)'
    m_FailedNotify = '#s(182|敌人被击败后会生成毒雾|9033)'
    m_EffectState = 20034
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (10000, 1) },
        2: {
            401: (10000, 1),
            2401: (10000, 1) },
        3: {
            401: (10000, 1),
            2401: (10000, 1) } }
    m_Param = (4104, None, None)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1031(CCustom):
    m_SID = 1031
    m_Type = CHALLENGE_LIMITCONVOY
    m_ChallengeName = '测试-限时护送事件'
    m_ChallengeNotify = '#s(171|限定时间护送目标到达目标点!|9034)'
    m_SuccessNotify = '#s(181|限定时间护送目标到达目标点!|9034)'
    m_FailedNotify = '#s(182|限定时间护送目标到达目标点!|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (3000, 1039002)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1032(CCustom):
    m_SID = 1032
    m_Type = CHALLENGE_LIMITTIME
    m_ChallengeName = '争分夺秒'
    m_ChallengeNotify = '#s(175|限时通过获得额外奖励| $remain#$total|9032)'
    m_SuccessNotify = '#s(187|限时通过获得额外奖励|9034)'
    m_FailedNotify = '#s(188|限时通过获得额外奖励|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (12000,)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1033(CCustom):
    m_SID = 1033
    m_Type = CHALLENGE_NOTIFYLIMITTIME
    m_ChallengeName = '争分夺秒'
    m_ChallengeNotify = '#s(175|限时通过获得额外奖励| $remain#$total|9032)'
    m_SuccessNotify = '#s(187|限时通过获得额外奖励|9034)'
    m_FailedNotify = '#s(188|限时通过获得额外奖励|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (12000, 7954, 1, 2, 7955, 1, 2)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1034(CCustom):
    m_SID = 1034
    m_Type = CHALLENGE_EXTRAMONSTER
    m_ChallengeName = '精英坐镇'
    m_ChallengeNotify = '#s(215|1034|9032)'
    m_SuccessNotify = '#s(216|1034|9034)'
    m_FailedNotify = '#s(186|精英独角金龟出现了！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (30011,)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1035(CCustom):
    m_SID = 1035
    m_Type = CHALLENGE_EXTRAMONSTER
    m_ChallengeName = '精英坐镇'
    m_ChallengeNotify = '#s(215|1035|9032)'
    m_SuccessNotify = '#s(216|1035|9034)'
    m_FailedNotify = '#s(186|精英流寇纵毒者出现了！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (32011,)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = [
        (1120234, 4),
        (1120234, 5),
        (1120234, 10),
        (1120234, 11),
        (1120342, 1),
        (1120410, 4),
        (1120410, 6),
        (1120410, 8),
        (1120410, 10)]


class CRoomChallengeData1036(CCustom):
    m_SID = 1036
    m_Type = CHALLENGE_EXTRAMONSTER
    m_ChallengeName = '精英坐镇'
    m_ChallengeNotify = '#s(215|1036|9032)'
    m_SuccessNotify = '#s(216|1036|9034)'
    m_FailedNotify = '#s(186|精英巡海夜叉出现了！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (31261,)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1037(CCustom):
    m_SID = 1037
    m_Type = CHALLENGE_EXTRAMONSTER
    m_ChallengeName = '精英坐镇'
    m_ChallengeNotify = '#s(215|1037|9032)'
    m_SuccessNotify = '#s(216|1037|9034)'
    m_FailedNotify = '#s(186|精英虚妄僧出现了！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (32821,)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1038(CCustom):
    m_SID = 1038
    m_Type = CHALLENGE_ELITE
    m_ChallengeName = '精英突入'
    m_ChallengeNotify = '#s(215|1038|9032)'
    m_SuccessNotify = '#s(216|1038|9034)'
    m_FailedNotify = '#s(186|精英马头锐士出现了！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (31231, 20, 50)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = [
        (1110502, 1),
        (1110502, 6),
        (1110502, 7),
        (1110502, 9)]


class CRoomChallengeData1039(CCustom):
    m_SID = 1039
    m_Type = CHALLENGE_ELITE
    m_ChallengeName = '精英突入'
    m_ChallengeNotify = '#s(215|1039|9032)'
    m_SuccessNotify = '#s(216|1039|9034)'
    m_FailedNotify = '#s(186|精英沙蜥出现了！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (32421, 50, 80)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1040(CCustom):
    m_SID = 1040
    m_Type = CHALLENGE_ELITE
    m_ChallengeName = '精英突入'
    m_ChallengeNotify = '#s(215|1040|9032)'
    m_SuccessNotify = '#s(216|1040|9034)'
    m_FailedNotify = '#s(186|精英土狼出现了！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (30211, 20, 80)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1041(CCustom):
    m_SID = 1041
    m_Type = CHALLENGE_ELITE
    m_ChallengeName = '精英突入'
    m_ChallengeNotify = '#s(215|1041|9032)'
    m_SuccessNotify = '#s(216|1041|9034)'
    m_FailedNotify = '#s(186|精英虚无僧出现了！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (32831, 50, 80)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1042(CCustom):
    m_SID = 1042
    m_Type = CHALLENGE_ELITE
    m_ChallengeName = '精英突入'
    m_ChallengeNotify = '#s(215|1042|9032)'
    m_SuccessNotify = '#s(216|1042|9034)'
    m_FailedNotify = '#s(186|精英鲶人武士出现了！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (30871, 20, 80)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1043(CCustom):
    m_SID = 1043
    m_Type = CHALLENGE_ELITE
    m_ChallengeName = '精英突入'
    m_ChallengeNotify = '#s(215|1043|9032)'
    m_SuccessNotify = '#s(216|1043|9034)'
    m_FailedNotify = '#s(186|精英流寇帮凶出现了！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (31251, 20, 50)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1044(CCustom):
    m_SID = 1044
    m_Type = CHALLENGE_ELITE
    m_ChallengeName = '精英突入'
    m_ChallengeNotify = '#s(215|1044|9032)'
    m_SuccessNotify = '#s(216|1044|9034)'
    m_FailedNotify = '#s(186|精英独角金龟出现了！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (30011, 50, 80)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1045(CCustom):
    m_SID = 1045
    m_Type = CHALLENGE_ELITE
    m_ChallengeName = '精英突入'
    m_ChallengeNotify = '#s(215|1045|9032)'
    m_SuccessNotify = '#s(216|1045|9034)'
    m_FailedNotify = '#s(186|精英流寇纵毒者出现了！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (32011, 50, 80)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = [
        (1120234, 4),
        (1120234, 5),
        (1120234, 10),
        (1120234, 11),
        (1120342, 1),
        (1120410, 4),
        (1120410, 6),
        (1120410, 8),
        (1120410, 10)]


class CRoomChallengeData1046(CCustom):
    m_SID = 1046
    m_Type = CHALLENGE_ELITE
    m_ChallengeName = '精英突入'
    m_ChallengeNotify = '#s(215|1046|9032)'
    m_SuccessNotify = '#s(216|1046|9034)'
    m_FailedNotify = '#s(186|精英巡海夜叉出现了！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (31261, 50, 80)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1047(CCustom):
    m_SID = 1047
    m_Type = CHALLENGE_ELITE
    m_ChallengeName = '精英突入'
    m_ChallengeNotify = '#s(215|1047|9032)'
    m_SuccessNotify = '#s(216|1047|9034)'
    m_FailedNotify = '#s(186|精英虚妄僧出现了！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (32821, 50, 80)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1048(CCustom):
    m_SID = 1048
    m_Type = CHALLENGE_ABERRANCE
    m_ChallengeName = '妖气惊变'
    m_ChallengeNotify = '#s(215|1048|9032)'
    m_SuccessNotify = '#s(216|1048|9034)'
    m_FailedNotify = '#s(182|敌人都变成巡海夜叉了！|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (10000, 1) },
        2: {
            401: (10000, 1),
            2401: (10000, 1) },
        3: {
            401: (10000, 1),
            2401: (10000, 1) } }
    m_Param = (21262,)
    m_ExcludeLastRoom = 1
    m_ExcludeArea = []


class CRoomChallengeData1049(CCustom):
    m_SID = 1049
    m_Type = CHALLENGE_ABERRANCE
    m_ChallengeName = '妖气惊变'
    m_ChallengeNotify = '#s(215|1049|9032)'
    m_SuccessNotify = '#s(216|1049|9034)'
    m_FailedNotify = '#s(182|敌人都变成马贼隐士了！|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (10000, 1) },
        2: {
            401: (10000, 1),
            2401: (10000, 1) },
        3: {
            401: (10000, 1),
            2401: (10000, 1) } }
    m_Param = (21422,)
    m_ExcludeLastRoom = 1
    m_ExcludeArea = []


class CRoomChallengeData1050(CCustom):
    m_SID = 1050
    m_Type = CHALLENGE_PLAYERPERFORM
    m_ChallengeName = '雪上加霜'
    m_ChallengeNotify = '#s(215|1050|9032)'
    m_SuccessNotify = '#s(216|1050|9034)'
    m_FailedNotify = '#s(182|英雄被破盾或破甲后短暂减速！|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (10000, 1) },
        2: {
            401: (10000, 1),
            2401: (10000, 1) },
        3: {
            401: (10000, 1),
            2401: (10000, 1) } }
    m_Param = (4142, None)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1051(CCustom):
    m_SID = 1051
    m_Type = CHALLENGE_APPENDSKILL
    m_ChallengeName = '延时退场'
    m_ChallengeNotify = '#s(215|1051|9032)'
    m_SuccessNotify = '#s(216|1051|9034)'
    m_FailedNotify = '#s(182|怪物被击杀时，延迟其死亡时间！|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (10000, 1) },
        2: {
            401: (10000, 1),
            2401: (10000, 1) },
        3: {
            401: (10000, 1),
            2401: (10000, 1) } }
    m_Param = (4143, None, None)
    m_ExcludeLastRoom = 1
    m_ExcludeArea = [
        (1110502, 8)]


class CRoomChallengeData1052(CCustom):
    m_SID = 1052
    m_Type = CHALLENGE_APPENDSKILL
    m_ChallengeName = '移花接木'
    m_ChallengeNotify = '#s(215|1052|9032)'
    m_SuccessNotify = '#s(216|1052|9034)'
    m_FailedNotify = '#s(182|怪物会根据已损失生命值治疗周围的其他怪物！|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (10000, 1) },
        2: {
            401: (10000, 1),
            2401: (10000, 1) },
        3: {
            401: (10000, 1),
            2401: (10000, 1) } }
    m_Param = (4144, None, None)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = [
        (1110303, 5)]


class CRoomChallengeData1053(CCustom):
    m_SID = 1053
    m_Type = CHALLENGE_APPENDSKILL
    m_ChallengeName = '战损修复'
    m_ChallengeNotify = '#s(215|1053|9032)'
    m_SuccessNotify = '#s(216|1053|9034)'
    m_FailedNotify = '#s(182|怪物受到伤害后，4秒内回复此伤害60%的生命值！|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (10000, 1) },
        2: {
            401: (10000, 1),
            2401: (10000, 1) },
        3: {
            401: (10000, 1),
            2401: (10000, 1) } }
    m_Param = (4145, None, None)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = [
        (1110303, 5)]


class CRoomChallengeData1054(CCustom):
    m_SID = 1054
    m_Type = CHALLENGE_APPENDSKILL
    m_ChallengeName = '琉璃屏障'
    m_ChallengeNotify = '#s(215|1054|9032)'
    m_SuccessNotify = '#s(216|1054|9034)'
    m_FailedNotify = '#s(182|怪物首次受伤时，短时间内免疫伤害和控制！|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (10000, 1) },
        2: {
            401: (10000, 1),
            2401: (10000, 1) },
        3: {
            401: (10000, 1),
            2401: (10000, 1) } }
    m_Param = (4146, None, None)
    m_ExcludeLastRoom = 1
    m_ExcludeArea = []


class CRoomChallengeData1055(CCustom):
    m_SID = 1055
    m_Type = CHALLENGE_PLAYERPERFORM
    m_ChallengeName = '腐蚀反噬'
    m_ChallengeNotify = '#s(215|1055|9032)'
    m_SuccessNotify = '#s(216|1055|9034)'
    m_FailedNotify = '#s(182|贴近怪物时触发减速效果！|9033)'
    m_EffectState = 1212
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (10000, 1) },
        2: {
            401: (10000, 1),
            2401: (10000, 1) },
        3: {
            401: (10000, 1),
            2401: (10000, 1) } }
    m_Param = (4148, None)
    m_ExcludeLastRoom = 1
    m_ExcludeArea = [
        (1110303, 5)]


class CRoomChallengeData1056(CCustom):
    m_SID = 1056
    m_Type = CHALLENGE_APPENDSKILL
    m_ChallengeName = '愈战愈艰'
    m_ChallengeNotify = '#s(215|1056|9032)'
    m_SuccessNotify = '#s(216|1056|9034)'
    m_FailedNotify = '#s(182|剩余怪物数量越少，怪物属性越强！|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (10000, 1) },
        2: {
            401: (10000, 1),
            2401: (10000, 1) },
        3: {
            401: (10000, 1),
            2401: (10000, 1) } }
    m_Param = (4149, None, None)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = [
        (1110502, 8)]


class CRoomChallengeData1057(CCustom):
    m_SID = 1057
    m_Type = CHALLENGE_TRAP
    m_ChallengeName = '流沙陷阱'
    m_ChallengeNotify = '#s(215|1057|9032)'
    m_SuccessNotify = '#s(216|1057|9034)'
    m_FailedNotify = '#s(182|每隔一段时间会在英雄脚下生成陷阱！|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (10000, 1) },
        2: {
            401: (10000, 1),
            2401: (10000, 1) },
        3: {
            401: (10000, 1),
            2401: (10000, 1) } }
    m_Param = (1163, 1650, 400, 0, 300)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = [
        (1120110, 2),
        (1120234, 1),
        (1120234, 2),
        (1120342, 2),
        (1120342, 4),
        (1120342, 5),
        (1120410, 7),
        (1120410, 9),
        (1120501, 9)]


class CRoomChallengeData1058(CCustom):
    m_SID = 1058
    m_Type = CHALLENGE_BOXMONSTER
    m_ChallengeName = '钱龙秘藏'
    m_ChallengeNotify = '#s(175|攻击钱龙获得奖励！| $remain#$total|9032)'
    m_SuccessNotify = '#s(185|攻击钱龙获得奖励！|9032)'
    m_FailedNotify = '#s(186|攻击钱龙获得奖励！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (23431, 300, 6000, 2132, 25, 2133, 2134, 1000, 500)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1059(CCustom):
    m_SID = 1059
    m_Type = CHALLENGE_DEFEND
    m_ChallengeName = '守护封印'
    m_ChallengeNotify = '#s(171|阻止敌人破坏封印|9032)'
    m_SuccessNotify = '#s(183|阻止敌人破坏封印|9034)'
    m_FailedNotify = '#s(184|阻止敌人破坏封印|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (1142001, 300, 300, 12)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1060(CCustom):
    m_SID = 1060
    m_Type = CHALLENGE_EXTRAMONSTER
    m_ChallengeName = '精英坐镇'
    m_ChallengeNotify = '#s(215|1060|9032)'
    m_SuccessNotify = '#s(216|1060|9034)'
    m_FailedNotify = '#s(186|精英右矛兵出现了！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (30831,)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = [
        (1110502, 1),
        (1110502, 6),
        (1110502, 7),
        (1110502, 9)]


class CRoomChallengeData1061(CCustom):
    m_SID = 1061
    m_Type = CHALLENGE_ELITE
    m_ChallengeName = '精英突入'
    m_ChallengeNotify = '#s(215|1061|9032)'
    m_SuccessNotify = '#s(216|1061|9034)'
    m_FailedNotify = '#s(186|精英右矛兵出现了！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (30831, 50, 80)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = [
        (1110502, 1),
        (1110502, 6),
        (1110502, 7),
        (1110502, 9)]


class CRoomChallengeData1062(CCustom):
    m_SID = 1062
    m_Type = CHALLENGE_NOTIFY
    m_ChallengeName = '沉睡石像'
    m_ChallengeNotify = '#s(171|小心射击，不要惊醒石化怪物！|9032)'
    m_SuccessNotify = '#s(181|小心射击，不要惊醒石化怪物！|9034)'
    m_FailedNotify = '#s(182|小心射击，不要惊醒石化怪物！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = ()
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1063(CCustom):
    m_SID = 1063
    m_Type = CHALLENGE_EXTRAMONSTER
    m_ChallengeName = '精英坐镇'
    m_ChallengeNotify = '#s(215|1063|9032)'
    m_SuccessNotify = '#s(216|1063|9034)'
    m_FailedNotify = '#s(186|精英敖龙出现了！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (32031,)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1064(CCustom):
    m_SID = 1064
    m_Type = CHALLENGE_ELITE
    m_ChallengeName = '精英突入'
    m_ChallengeNotify = '#s(215|1064|9032)'
    m_SuccessNotify = '#s(216|1064|9034)'
    m_FailedNotify = '#s(186|精英敖龙出现了！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (32031, 50, 80)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1065(CCustom):
    m_SID = 1065
    m_Type = CHALLENGE_EXTRAMONSTER
    m_ChallengeName = '精英坐镇'
    m_ChallengeNotify = '#s(215|1065|9032)'
    m_SuccessNotify = '#s(216|1065|9034)'
    m_FailedNotify = '#s(186|精英马贼隐士出现了！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (31421,)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1066(CCustom):
    m_SID = 1066
    m_Type = CHALLENGE_ELITE
    m_ChallengeName = '精英突入'
    m_ChallengeNotify = '#s(215|1066|9032)'
    m_SuccessNotify = '#s(216|1066|9034)'
    m_FailedNotify = '#s(186|精英马贼隐士出现了！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (31421, 50, 80)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1067(CCustom):
    m_SID = 1067
    m_Type = CHALLENGE_EXTRAMONSTER
    m_ChallengeName = '精英坐镇'
    m_ChallengeNotify = '#s(215|1067|9032)'
    m_SuccessNotify = '#s(216|1067|9034)'
    m_FailedNotify = '#s(186|精英河童出现了！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (32811,)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1068(CCustom):
    m_SID = 1068
    m_Type = CHALLENGE_ELITE
    m_ChallengeName = '精英突入'
    m_ChallengeNotify = '#s(215|1068|9032)'
    m_SuccessNotify = '#s(216|1068|9034)'
    m_FailedNotify = '#s(186|精英河童出现了！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (32811, 50, 80)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1071(CCustom):
    m_SID = 1071
    m_Type = CHALLENGE_BOXMONSTER
    m_ChallengeName = '钱龙秘藏'
    m_ChallengeNotify = '#s(175|攻击钱龙获得奖励！| $remain#$total|9032)'
    m_SuccessNotify = '#s(185|攻击钱龙获得奖励！|9032)'
    m_FailedNotify = '#s(186|攻击钱龙获得奖励！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (23421, 300, 6000, 2132, 25, 2133, 2134, 1000, 500)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1072(CCustom):
    m_SID = 1072
    m_Type = CHALLENGE_BOXMONSTER
    m_ChallengeName = '钱龙秘藏'
    m_ChallengeNotify = '#s(175|攻击钱龙获得奖励！| $remain#$total|9032)'
    m_SuccessNotify = '#s(185|攻击钱龙获得奖励！|9032)'
    m_FailedNotify = '#s(186|攻击钱龙获得奖励！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (23411, 300, 6000, 2132, 25, 2133, 2134, 1000, 500)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1087(CCustom):
    m_SID = 1087
    m_Type = CHALLENGE_KILLSUMMON
    m_ChallengeName = '妖气转生'
    m_ChallengeNotify = '#s(215|1087|9032)'
    m_SuccessNotify = '#s(216|1087|9034)'
    m_FailedNotify = '#s(182|敌人被击败后化身雪地原住！|9033)'
    m_EffectState = 20033
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (10000, 1) },
        2: {
            401: (10000, 1),
            2401: (10000, 1) },
        3: {
            401: (10000, 1),
            2401: (10000, 1) } }
    m_Param = ({
        23614: 100 },)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []

