# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/w3020/roomchallenge.pyc
# RelativePath: clientlogic/cl_wardata/w3020/roomchallenge.pyc
# Source Generated with Decompyle++
# File: roomchallenge.pyc (Python 3.6)

from cl_resmgr.resdata import CRoomChallengeData as CCustom
from cl_commondefines import ALLVERLAYER_VALID, CHALLENGE_ABERRANCE, CHALLENGE_APPENDSKILL, CHALLENGE_BOXMONSTER, CHALLENGE_DEFEND, CHALLENGE_ELITE, CHALLENGE_EXTRAELITE, CHALLENGE_EXTRAMONSTER, CHALLENGE_KILLSUMMON, CHALLENGE_LIMITCONVOY, CHALLENGE_LIMITDEFEND, CHALLENGE_LIMITLIVE, CHALLENGE_LIMITTIME, CHALLENGE_NOTIFY, CHALLENGE_NOTIFYLIMITTIME, CHALLENGE_PLAYERPERFORM, CHALLENGE_SIGHT, CHALLENGE_SUPERMONSTER, CHALLENGE_TRAP
from cl_newformula import Func235, Func527

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
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (6667, 1) } }
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
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (6667, 1) } }
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
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (6667, 1) } }
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
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (6667, 1) } }
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
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (6667, 1) } }
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
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (6667, 1) } }
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
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (6667, 1) } }
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
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (6667, 1) } }
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
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (6667, 1) } }
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
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (6667, 1) } }
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
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (6667, 1) } }
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
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (6667, 1) } }
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
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (6667, 1) } }
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
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (6667, 1) } }
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
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (6667, 1) } }
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
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (6667, 1) } }
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
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (6667, 1) } }
    m_Param = (4104, None, None)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1031(CCustom):
    m_SID = 1031
    m_Type = CHALLENGE_LIMITCONVOY
    m_ChallengeName = '争分夺秒'
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
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (6667, 1) } }
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
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (6667, 1) } }
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
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (6667, 1) } }
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
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (6667, 1) } }
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
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (6667, 1) } }
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
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (6667, 1) } }
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
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (6667, 1) } }
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
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (6667, 1) } }
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
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (6667, 1) } }
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
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (6667, 1) } }
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
        (1110502, 8),
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
        (1110502, 8),
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


class CRoomChallengeData1069(CCustom):
    m_SID = 1069
    m_Type = CHALLENGE_SIGHT
    m_ChallengeName = '瞄准关挑战（手枪）'
    m_ChallengeNotify = '#s(176|射击目标获取积分！| $remain#$total|9032)'
    m_SuccessNotify = '#s(185|挑战完成！|9034)'
    m_FailedNotify = '#s(186|挑战完成！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (1165, 1673, 4194, 81, 1051, 4800, {
        1043: (lambda *a: 10 + Func527(*a) - 1),
        1056: 0,
        1057: (lambda *a: 50 + 1 * Func527(*a) - 1) }, {
        600: 1,
        1100: 2,
        1500: 3 }, {
        0: 1001,
        100: 1002,
        600: 1003,
        1100: 1004,
        1600: 1005,
        2100: 1006,
        2600: 1007,
        3100: 1008,
        3600: 1009,
        4100: 1010 }, {
        0: 9272,
        1: 9275,
        2: 9276,
        3: 9277,
        4: 9277 }, 1004, {
        5779: 1,
        5780: 1,
        5752: 1,
        2037: 1,
        5795: 1,
        5796: 1,
        5797: 1,
        5726: 1 })
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1070(CCustom):
    m_SID = 1070
    m_Type = CHALLENGE_SIGHT
    m_ChallengeName = '瞄准关挑战（狙击）'
    m_ChallengeNotify = '#s(177|瞄准关挑战开始！剩余次数$remain|9032)'
    m_SuccessNotify = '#s(185|瞄准关挑战开始！|9034)'
    m_FailedNotify = '#s(186|瞄准关挑战开始！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (0, 0, 0, 0, 0, 0, { }, { }, { }, { }, None, { })
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


class CRoomChallengeData1073(CCustom):
    m_SID = 1073
    m_Type = CHALLENGE_KILLSUMMON
    m_ChallengeName = '妖气转生'
    m_ChallengeNotify = '#s(215|1073|9032)'
    m_SuccessNotify = '#s(216|1073|9034)'
    m_FailedNotify = '#s(182|敌人被击败后化身马头锐士或独角金龟!|9033)'
    m_EffectState = 20033
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (1000, 1),
            501: (10000, 10) } }
    m_Param = ({
        20014: 50,
        21233: 50 },)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1074(CCustom):
    m_SID = 1074
    m_Type = CHALLENGE_KILLSUMMON
    m_ChallengeName = '妖气转生'
    m_ChallengeNotify = '#s(215|1074|9032)'
    m_SuccessNotify = '#s(216|1074|9034)'
    m_FailedNotify = '#s(182|敌人被击败后化身黑面流寇或大漠幼豚!|9033)'
    m_EffectState = 20033
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (1000, 1),
            501: (10000, 10) } }
    m_Param = ({
        20023: 50,
        21222: 50 },)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1075(CCustom):
    m_SID = 1075
    m_Type = CHALLENGE_KILLSUMMON
    m_ChallengeName = '妖气转生'
    m_ChallengeNotify = '#s(215|1075|9032)'
    m_SuccessNotify = '#s(216|1075|9034)'
    m_FailedNotify = '#s(182|敌人被击败后化身白鲛或自爆灯笼鬼!|9033)'
    m_EffectState = 20033
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (1000, 1),
            501: (10000, 10) } }
    m_Param = ({
        20042: 50,
        21812: 50 },)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1076(CCustom):
    m_SID = 1076
    m_Type = CHALLENGE_PLAYERPERFORM
    m_ChallengeName = '元素失效'
    m_ChallengeNotify = '#s(212|当前区域武器无法触发$text，换弹后切换随机元素异常类型!|9032)'
    m_SuccessNotify = '#s(217|挑战成功!|9034)'
    m_FailedNotify = '#s(182|挑战失败!|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (1000, 1),
            501: (10000, 10) } }
    m_Param = (4246, 8)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1077(CCustom):
    m_SID = 1077
    m_Type = CHALLENGE_PLAYERPERFORM
    m_ChallengeName = '苦难秘辛'
    m_ChallengeNotify = '#s(215|1077|9032)'
    m_SuccessNotify = '#s(216|1077|9034)'
    m_FailedNotify = '#s(182|怪物的攻击必定触发元素异常！使用冲刺/主要技能或击败敌人后可解除元素异常，并免疫元素异常，持续1秒!|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (1000, 1),
            501: (10000, 10) } }
    m_Param = (4248, None)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1078(CCustom):
    m_SID = 1078
    m_Type = CHALLENGE_SUPERMONSTER
    m_ChallengeName = '全副武装'
    m_ChallengeNotify = '#s(215|1078|9032)'
    m_SuccessNotify = '#s(216|1078|9034)'
    m_FailedNotify = '#s(182|敌人都变成强化怪了！玩家获得临时灵佑【狩猎季节】!|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (1000, 1),
            501: (10000, 10) } }
    m_Param = (13711, {
        6101: 10,
        6102: 10,
        6103: 10,
        6104: 10,
        6105: 10,
        6106: 10,
        6108: 10 }, {
        6201: 10,
        6202: 10,
        6203: 10,
        6204: 10 })
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1079(CCustom):
    m_SID = 1079
    m_Type = CHALLENGE_APPENDSKILL
    m_ChallengeName = '移花接木'
    m_ChallengeNotify = '#s(215|1079|9032)'
    m_SuccessNotify = '#s(216|1079|9034)'
    m_FailedNotify = '#s(182|怪物会根据已损失生命值治疗周围的其他怪物！|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (1000, 1),
            501: (10000, 10) } }
    m_Param = (4144, None, None)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = [
        (1110303, 5)]


class CRoomChallengeData1080(CCustom):
    m_SID = 1080
    m_Type = CHALLENGE_PLAYERPERFORM
    m_ChallengeName = '雪上加霜'
    m_ChallengeNotify = '#s(215|1080|9032)'
    m_SuccessNotify = '#s(216|1080|9034)'
    m_FailedNotify = '#s(182|英雄被破盾或破甲后短暂减速！|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (1000, 1),
            501: (10000, 10) } }
    m_Param = (4142, None)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1081(CCustom):
    m_SID = 1081
    m_Type = CHALLENGE_APPENDSKILL
    m_ChallengeName = '战损修复'
    m_ChallengeNotify = '#s(215|1081|9032)'
    m_SuccessNotify = '#s(216|1081|9034)'
    m_FailedNotify = '#s(182|怪物受到伤害后，4秒内回复此伤害60%的生命值！|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (1000, 1),
            501: (10000, 10) } }
    m_Param = (4145, None, None)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = [
        (1110303, 5)]


class CRoomChallengeData1082(CCustom):
    m_SID = 1082
    m_Type = CHALLENGE_APPENDSKILL
    m_ChallengeName = '琉璃屏障'
    m_ChallengeNotify = '#s(215|1082|9032)'
    m_SuccessNotify = '#s(216|1082|9034)'
    m_FailedNotify = '#s(182|怪物首次受伤时，短时间内免疫伤害和控制！|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (1000, 1),
            501: (10000, 10) } }
    m_Param = (4146, None, None)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1083(CCustom):
    m_SID = 1083
    m_Type = CHALLENGE_APPENDSKILL
    m_ChallengeName = '愈战愈艰'
    m_ChallengeNotify = '#s(215|1083|9032)'
    m_SuccessNotify = '#s(216|1083|9034)'
    m_FailedNotify = '#s(182|剩余怪物数量越少，怪物属性越强！|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (1000, 1),
            501: (10000, 10) } }
    m_Param = (4149, None, None)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = [
        (1110502, 8)]


class CRoomChallengeData1084(CCustom):
    m_SID = 1084
    m_Type = CHALLENGE_TRAP
    m_ChallengeName = '流沙陷阱'
    m_ChallengeNotify = '#s(215|1084|9032)'
    m_SuccessNotify = '#s(216|1084|9034)'
    m_FailedNotify = '#s(182|每隔一段时间会在英雄脚下生成陷阱！|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (1000, 1),
            501: (10000, 10) } }
    m_Param = (1163, 1650, 400, 0, 300)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1085(CCustom):
    m_SID = 1085
    m_Type = CHALLENGE_ABERRANCE
    m_ChallengeName = '妖气惊变'
    m_ChallengeNotify = '#s(215|1085|9032)'
    m_SuccessNotify = '#s(216|1085|9034)'
    m_FailedNotify = '#s(182|敌人都变成虚无僧了！|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (1000, 1),
            501: (10000, 10) } }
    m_Param = (22831,)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1086(CCustom):
    m_SID = 1086
    m_Type = CHALLENGE_APPENDSKILL
    m_ChallengeName = '同生共死'
    m_ChallengeNotify = '#s(215|1086|9032)'
    m_SuccessNotify = '#s(216|1086|9034)'
    m_FailedNotify = '#s(182|怪物被击败时，免疫死亡并进入狂暴状态，区域内的怪物均进入狂暴状态时才能被消灭!|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (1000, 1),
            501: (10000, 10) } }
    m_Param = (4254, None, None)
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
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (6667, 1) } }
    m_Param = ({
        23614: 100 },)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1088(CCustom):
    m_SID = 1088
    m_Type = CHALLENGE_EXTRAELITE
    m_ChallengeName = '群英荟萃'
    m_ChallengeNotify = '#s(215|1088|9032)'
    m_SuccessNotify = '#s(216|1088|9034)'
    m_FailedNotify = '#s(182|大量精英怪出现！|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            501: (10000, 10),
            4101: (10000, 1),
            2404: (10000, 1) },
        2: {
            401: (10000, 1),
            501: (10000, 10),
            4101: (10000, 1),
            2404: (10000, 1) },
        3: {
            401: (10000, 1),
            501: (10000, 10),
            4101: (10000, 1),
            2404: (10000, 1) } }
    m_Param = ((lambda *a: Func235(*a, **{
'sType': 'RidingAlone' }) + 1), 50, {
        (30832, 31232): 50,
        (30012, 30832): 50 }, 0, None, None, None)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = [
        (1110502, 1),
        (1110502, 6),
        (1110502, 7),
        (1110502, 8),
        (1110502, 9)]


class CRoomChallengeData1089(CCustom):
    m_SID = 1089
    m_Type = CHALLENGE_EXTRAELITE
    m_ChallengeName = '群英荟萃'
    m_ChallengeNotify = '#s(215|1089|9032)'
    m_SuccessNotify = '#s(216|1089|9034)'
    m_FailedNotify = '#s(182|大量精英怪出现！|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            501: (10000, 10),
            4101: (10000, 1),
            2404: (10000, 1) },
        2: {
            401: (10000, 1),
            501: (10000, 10),
            4101: (10000, 1),
            2404: (10000, 1) },
        3: {
            401: (10000, 1),
            501: (10000, 10),
            4101: (10000, 1),
            2404: (10000, 1) } }
    m_Param = ((lambda *a: Func235(*a, **{
'sType': 'RidingAlone' }) + 1), 100, {
        (30212, 31422, 31252, 32422, 32012): 50,
        (32422, 32422, 31252, 30212, 32012): 50,
        (30212, 30212, 31252, 30212, 31422): 50,
        (30212, 32422, 32012, 31422, 31252): 50 }, 0, None, None, None)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1090(CCustom):
    m_SID = 1090
    m_Type = CHALLENGE_EXTRAELITE
    m_ChallengeName = '群英荟萃'
    m_ChallengeNotify = '#s(215|1090|9032)'
    m_SuccessNotify = '#s(216|1090|9034)'
    m_FailedNotify = '#s(182|大量精英怪出现！|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            501: (10000, 10),
            4101: (10000, 1),
            2404: (10000, 1) },
        2: {
            401: (10000, 1),
            501: (10000, 10),
            4101: (10000, 1),
            2404: (10000, 1) },
        3: {
            401: (10000, 1),
            501: (10000, 10),
            4101: (10000, 1),
            2404: (10000, 1) } }
    m_Param = ((lambda *a: Func235(*a, **{
'sType': 'RidingAlone' }) + 1), 100, {
        (32823, 32832, 32823, 32832, 32823): 50,
        (32832, 32832, 32032, 32032, 32032): 50,
        (30872, 30872, 32812, 32812, 32832): 50,
        (32032, 32032, 31262, 31262, 32823): 50,
        (32812, 32812, 32812, 32812, 32812): 50,
        (31262, 31262, 31262, 31262, 31262): 50,
        (30872, 30872, 30872, 30872, 30872): 50,
        (30872, 31262, 32032, 32812, 32823): 50 }, 0, None, None, None)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = [
        (1130301, 3),
        (1130301, 4),
        (1130301, 11),
        (1130301, 13),
        (1130301, 14)]


class CRoomChallengeData1091(CCustom):
    m_SID = 1091
    m_Type = CHALLENGE_EXTRAELITE
    m_ChallengeName = '群英荟萃'
    m_ChallengeNotify = '#s(215|1091|9032)'
    m_SuccessNotify = '#s(216|1091|9034)'
    m_FailedNotify = '#s(182|大量精英怪出现！|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            501: (10000, 10),
            4101: (10000, 1),
            2404: (10000, 1) },
        2: {
            401: (10000, 1),
            501: (10000, 10),
            4101: (10000, 1),
            2404: (10000, 1) },
        3: {
            401: (10000, 1),
            501: (10000, 10),
            4101: (10000, 1),
            2404: (10000, 1) } }
    m_Param = ((lambda *a: Func235(*a, **{
'sType': 'RidingAlone' }) + 1), 50, {
        (31642, 33813, 31642, 33813, 33813): 50 }, 0, None, None, None)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1092(CCustom):
    m_SID = 1092
    m_Type = CHALLENGE_PLAYERPERFORM
    m_ChallengeName = '腐蚀反噬'
    m_ChallengeNotify = '#s(215|1092|9032)'
    m_SuccessNotify = '#s(216|1092|9034)'
    m_FailedNotify = '#s(182|贴近怪物时触发减速效果！|9033)'
    m_EffectState = 1212
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (1000, 1),
            501: (10000, 10) } }
    m_Param = (4148, None)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = [
        (1110303, 5)]


class CRoomChallengeData1093(CCustom):
    m_SID = 1093
    m_Type = CHALLENGE_EXTRAMONSTER
    m_ChallengeName = '精英坐镇'
    m_ChallengeNotify = '#s(215|1093|9032)'
    m_SuccessNotify = '#s(216|1093|9034)'
    m_FailedNotify = '#s(186|精英魈骑兵出现了！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (33811,)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1094(CCustom):
    m_SID = 1094
    m_Type = CHALLENGE_EXTRAMONSTER
    m_ChallengeName = '精英突入'
    m_ChallengeNotify = '#s(215|1094|9032)'
    m_SuccessNotify = '#s(216|1094|9034)'
    m_FailedNotify = '#s(186|精英魈骑兵出现了！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (33811,)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1095(CCustom):
    m_SID = 1095
    m_Type = CHALLENGE_EXTRAMONSTER
    m_ChallengeName = '精英坐镇'
    m_ChallengeNotify = '#s(215|1095|9032)'
    m_SuccessNotify = '#s(216|1095|9034)'
    m_FailedNotify = '#s(186|精英雷鸣猎手出现了！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (31641,)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1096(CCustom):
    m_SID = 1096
    m_Type = CHALLENGE_EXTRAMONSTER
    m_ChallengeName = '精英突入'
    m_ChallengeNotify = '#s(215|1096|9032)'
    m_SuccessNotify = '#s(216|1096|9034)'
    m_FailedNotify = '#s(186|精英雷鸣猎手出现了！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (31641,)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1097(CCustom):
    m_SID = 1097
    m_Type = CHALLENGE_ABERRANCE
    m_ChallengeName = '妖气惊变'
    m_ChallengeNotify = '#s(215|1097|9032)'
    m_SuccessNotify = '#s(216|1097|9034)'
    m_FailedNotify = '#s(182|敌人都变成六耳了！|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (6667, 1) } }
    m_Param = (20891,)
    m_ExcludeLastRoom = 1
    m_ExcludeArea = []


class CRoomChallengeData1098(CCustom):
    m_SID = 1098
    m_Type = CHALLENGE_KILLSUMMON
    m_ChallengeName = '妖气转生'
    m_ChallengeNotify = '#s(215|1098|9032)'
    m_SuccessNotify = '#s(216|1098|9034)'
    m_FailedNotify = '#s(182|敌人被击败后化身雪山守卫或雪地原住！|9033)'
    m_EffectState = 20033
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (1000, 1),
            501: (10000, 10) } }
    m_Param = ({
        23611: 50,
        21281: 50 },)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1099(CCustom):
    m_SID = 1099
    m_Type = CHALLENGE_PLAYERPERFORM
    m_ChallengeName = '荆棘丛林'
    m_ChallengeNotify = '#s(215|1099|9032)'
    m_SuccessNotify = '#s(216|1099|9034)'
    m_FailedNotify = '#s(182|英雄移动速度增加，但使用冲刺技能会受到当前生命总值10%的伤害！|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (1000, 1),
            501: (10000, 10) } }
    m_Param = (4279, 0)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1100(CCustom):
    m_SID = 1100
    m_Type = CHALLENGE_APPENDSKILL
    m_ChallengeName = '应激反应'
    m_ChallengeNotify = '#s(215|1100|9032)'
    m_SuccessNotify = '#s(216|1100|9034)'
    m_FailedNotify = '#s(182|敌人受到伤害时会获得大幅移动速度加成，加成会迅速衰减！|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (1000, 1),
            501: (10000, 10) } }
    m_Param = (4280, None, None)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1101(CCustom):
    m_SID = 1101
    m_Type = CHALLENGE_PLAYERPERFORM
    m_ChallengeName = '抵近射击'
    m_ChallengeNotify = '#s(215|1101|9032)'
    m_SuccessNotify = '#s(216|1101|9034)'
    m_FailedNotify = '#s(182|对12米范围内的敌人造成的伤害提升50%，对12米范围外的敌人仅造成1点伤害！|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (1000, 1),
            501: (10000, 10) } }
    m_Param = (4281, 0)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1102(CCustom):
    m_SID = 1102
    m_Type = CHALLENGE_PLAYERPERFORM
    m_ChallengeName = '耐受体质'
    m_ChallengeNotify = '#s(215|1102|9032)'
    m_SuccessNotify = '#s(216|1102|9034)'
    m_FailedNotify = '#s(182|持续造成武器伤害（或技能伤害）时，该种伤害会减少。造成另一种伤害后该效果消失！|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (1000, 1),
            501: (10000, 10) } }
    m_Param = (4283, 0)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1103(CCustom):
    m_SID = 1103
    m_Type = CHALLENGE_APPENDSKILL
    m_ChallengeName = '元素抵抗'
    m_ChallengeNotify = '#s(215|1103|9032)'
    m_SuccessNotify = '#s(216|1103|9034)'
    m_FailedNotify = '#s(182|敌人身上的元素异常类型越多，受到的伤害越少！|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (1000, 1),
            501: (10000, 10) } }
    m_Param = (4284, None, None)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1104(CCustom):
    m_SID = 1104
    m_Type = CHALLENGE_PLAYERPERFORM
    m_ChallengeName = '返璞归真'
    m_ChallengeNotify = '#s(215|1104|9032)'
    m_SuccessNotify = '#s(216|1104|9034)'
    m_FailedNotify = '#s(182|敌人被熔炉命中弱点时会被立即击败，非熔炉造成的伤害减少90%！|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (1000, 1),
            501: (10000, 10) } }
    m_Param = (4285, 0)
    m_ExcludeLastRoom = 1
    m_ExcludeArea = []


class CRoomChallengeData1105(CCustom):
    m_SID = 1105
    m_Type = CHALLENGE_APPENDSKILL
    m_ChallengeName = '无视苦痛'
    m_ChallengeNotify = '#s(215|1105|9032)'
    m_SuccessNotify = '#s(216|1105|9034)'
    m_FailedNotify = '#s(182|敌人所受的60%伤害会在6秒内持续扣除，对玩家造成伤害后会减免剩余伤害|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (1000, 1),
            501: (10000, 10) } }
    m_Param = (4286, None, None)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1106(CCustom):
    m_SID = 1106
    m_Type = CHALLENGE_PLAYERPERFORM
    m_ChallengeName = '元素失效'
    m_ChallengeNotify = '#s(212|当前区域武器无法触发$text，使用冲刺技能后切换随机元素异常类型!|9032)'
    m_SuccessNotify = '#s(217|挑战成功!|9034)'
    m_FailedNotify = '#s(182|挑战失败!|9033)'
    m_EffectState = 0
    m_Reward = {
        1: {
            401: (10000, 1),
            2401: (6667, 1) },
        2: {
            401: (10000, 1),
            2401: (6667, 1) },
        3: {
            401: (10000, 1),
            2401: (1000, 1),
            501: (10000, 10) } }
    m_Param = (4288, 8)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []


class CRoomChallengeData1107(CCustom):
    m_SID = 1107
    m_Type = CHALLENGE_BOXMONSTER
    m_ChallengeName = '二幕宝箱怪挑战'
    m_ChallengeNotify = '#s(175|运用<color=#1CC9E7>宝石灵力</color>消灭真正的钱龙获得奖励！| $remain#$total|9032)'
    m_SuccessNotify = '#s(185|运用<color=#1CC9E7>宝石灵力</color>消灭真正的钱龙获得奖励！|9032)'
    m_FailedNotify = '#s(186|运用<color=#1CC9E7>宝石灵力</color>消灭真正的钱龙获得奖励！|9033)'
    m_EffectState = 0
    m_Reward = { }
    m_Param = (23451, 300, 8000, 2132, 25, 2133, 2134, 1000, 500)
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []

