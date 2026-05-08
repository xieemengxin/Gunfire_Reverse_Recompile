# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/playway/playwayitem.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/playway/playwayitem.pyc
# Source Generated with Decompyle++
# File: playwayitem.pyc (Python 3.6)

from cl_cscommondef import *

class CItem1001(object):
    m_SID = 1001
    m_Name = '#NT#通用一幕额外刷怪'
    m_Rule = [
        (DAY_TRIAL_CHANGE_MONSTER_CNT, (1, 1))]


class CItem1002(object):
    m_SID = 1002
    m_Name = '#NT#第三幕八腕目元素触发概率调整'
    m_Rule = [
        (DAY_TRIAL_MONSTER_ADD_SKILL, (6700, {
            22021: 10 }))]


class CItem1011(object):
    m_SID = 1011
    m_Name = '#NT#武器暴击时才能造成伤害及效果'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (6701,))]


class CItem1012(object):
    m_SID = 1012
    m_Name = '#NT#所有武器暴击倍率+400%'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (16702,))]


class CItem1013(object):
    m_SID = 1013
    m_Name = '#NT#屏蔽火焰之环伤害'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (6703,))]


class CItem1014(object):
    m_SID = 1014
    m_Name = '#NT#屏蔽技能伤害'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (6704,))]


class CItem1015(object):
    m_SID = 1015
    m_Name = '#NT#猎头人额外增加暴击倍率'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (6705,))]


class CItem1021(object):
    m_SID = 1021
    m_Name = '#NT#英雄额外获得2次复活机会'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (6711,))]


class CItem1022(object):
    m_SID = 1022
    m_Name = '#NT#怪物有50%概率复活1次'
    m_Rule = [
        (DAY_TRIAL_MONSTER_ADD_SKILL, (6712, { }))]


class CItem1023(object):
    m_SID = 1023
    m_Name = '#NT#三重轮回概率增加3倍'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (6713,))]


class CItem1024(object):
    m_SID = 1024
    m_Name = '#NT#复活节屏蔽隐藏关'
    m_Rule = [
        (DAY_TRIAL_FILTER_ASSIGN_HIDELEVEL, ((1101234, 1101233),))]


class CItem1025(object):
    m_SID = 1025
    m_Name = '#NT#【低等级】玩家每复活一次，造成的伤害增加(80-玩家等级)/200*100%'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (6714,))]


class CItem1026(object):
    m_SID = 1026
    m_Name = '#NT#复活后持续掉血，若击败敌人则短时间无敌'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (6715,))]


class CItem1031(object):
    m_SID = 1031
    m_Name = '#NT#初始秘卷'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_RELIC, (5704, 0)),
        (DAY_TRIAL_PLAYER_ADD_RELIC, (5703, 0))]


class CItem1032(object):
    m_SID = 1032
    m_Name = '#NT#怪物生命值降低'
    m_Rule = [
        (DAY_TRIAL_MONSTER_ADD_SKILL, (6721, { }))]


class CItem1033(object):
    m_SID = 1033
    m_Name = '#NT#无法获得包子'
    m_Rule = [
        (DAY_TRIAL_REPLACENPC, ({
            1005: {
                6001: 10 },
            1059: {
                6001: 10 } },)),
        (DAY_TRIAL_PLAYER_ADD_SKILL, (6722,))]


class CItem1034(object):
    m_SID = 1034
    m_Name = '#NT#英雄额外获得1次复活机会'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (6723,))]


class CItem1035(object):
    m_SID = 1035
    m_Name = '#NT#1003一滴血屏蔽房间挑战'
    m_Rule = [
        (DAY_TRIAL_IGNORECHALLENGE, ('30091050|30091053|30091052|30091022|30091021|30091057|30091051',))]


class CItem1036(object):
    m_SID = 1036
    m_Name = '#NT#1003-滴血主题-npc屏蔽'
    m_Rule = [
        (DAY_TRIAL_REPLACENPC, ({
            2102: {
                2105: 10,
                2101: 10,
                2109: 10,
                2118: 10,
                2121: 10,
                2122: 10,
                2112: 10,
                2114: 10,
                2116: 10 },
            2103: {
                2105: 10,
                2101: 10,
                2109: 10,
                2118: 10,
                2121: 10,
                2122: 10,
                2112: 10,
                2114: 10,
                2116: 10 },
            2104: {
                2105: 10,
                2101: 10,
                2109: 10,
                2118: 10,
                2121: 10,
                2122: 10,
                2112: 10,
                2114: 10,
                2116: 10 },
            2108: {
                2105: 10,
                2101: 10,
                2109: 10,
                2118: 10,
                2121: 10,
                2122: 10,
                2112: 10,
                2114: 10,
                2116: 10 },
            2110: {
                2105: 10,
                2101: 10,
                2109: 10,
                2118: 10,
                2121: 10,
                2122: 10,
                2112: 10,
                2114: 10,
                2116: 10 },
            2115: {
                2105: 10,
                2101: 10,
                2109: 10,
                2118: 10,
                2121: 10,
                2122: 10,
                2112: 10,
                2114: 10,
                2116: 10 },
            2117: {
                2105: 10,
                2101: 10,
                2109: 10,
                2118: 10,
                2121: 10,
                2122: 10,
                2112: 10,
                2114: 10,
                2116: 10 },
            2119: {
                2105: 10,
                2101: 10,
                2109: 10,
                2118: 10,
                2121: 10,
                2122: 10,
                2112: 10,
                2114: 10,
                2116: 10 },
            2123: {
                2105: 10,
                2101: 10,
                2109: 10,
                2118: 10,
                2121: 10,
                2122: 10,
                2112: 10,
                2114: 10,
                2116: 10 },
            2106: {
                2105: 10,
                2101: 10,
                2109: 10,
                2118: 10,
                2121: 10,
                2122: 10,
                2112: 10,
                2114: 10,
                2116: 10 },
            2107: {
                2105: 10,
                2101: 10,
                2109: 10,
                2118: 10,
                2121: 10,
                2122: 10,
                2112: 10,
                2114: 10,
                2116: 10 },
            2120: {
                2105: 10,
                2101: 10,
                2109: 10,
                2118: 10,
                2121: 10,
                2122: 10,
                2112: 10,
                2114: 10,
                2116: 10 } },))]


class CItem1037(object):
    m_SID = 1037
    m_Name = '#NT#狭路相逢屏蔽吸血法师怪'
    m_Rule = [
        (DAY_TRIAL_REPLACE_MONSTER, ({
            32831: 32821,
            22831: 22821 },))]


class CItem1038(object):
    m_SID = 1038
    m_Name = '#NT#召唤物血量为1'
    m_Rule = [
        (DAY_TRIAL_SUMMON_ADD_SKILL, (6724,))]


class CItem1039(object):
    m_SID = 1039
    m_Name = '#NT#狭路相逢屏蔽不适合关卡'
    m_Rule = [
        (DAY_TRIAL_FILTER_ASSIGN_HIDELEVEL, ((1101602, 1101603, 1101604, 1201603, 1201604),))]


class CItem1040(object):
    m_SID = 1040
    m_Name = '#NT#狭路相逢电池血量'
    m_Rule = [
        (DAY_TRIAL_BUILD_ADD_SKILL, (6795, {
            1169: 10 }))]


class CItem1041(object):
    m_SID = 1041
    m_Name = '#NT#大幅提升秘卷和金爵的掉落'
    m_Rule = []


class CItem1042(object):
    m_SID = 1042
    m_Name = '#NT#玩家生命随铜币数量增加而减少'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (16732,))]


class CItem1043(object):
    m_SID = 1043
    m_Name = '#NT#击杀一个怪物扣40铜币'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (6733,)),
        (DAY_TRIAL_MONSTER_ADD_SKILL, (6737, { }))]


class CItem1044(object):
    m_SID = 1044
    m_Name = '#NT#拾取秘卷，金爵会得铜币'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (6734,))]


class CItem1045(object):
    m_SID = 1045
    m_Name = '#NT#商品和强化装备获取对应的铜币'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (6735,)),
        (DAY_TRIAL_REPLACENPC, ({
            1005: {
                6004: 10 },
            1018: {
                6007: 10 } },))]


class CItem1046(object):
    m_SID = 1046
    m_Name = '#NT#屏蔽场外金币天赋'
    m_Rule = [
        (DAY_TRIAL_FILTER_SUBLIME, (6513,)),
        (DAY_TRIAL_FILTER_SUBLIME, (6518,)),
        (DAY_TRIAL_FILTER_SUBLIME, (6527,)),
        (DAY_TRIAL_FILTER_SUBLIME, (6542,)),
        (DAY_TRIAL_FILTER_SUBLIME, (6543,)),
        (DAY_TRIAL_FILTER_SUBLIME, (6561,)),
        (DAY_TRIAL_FILTER_SUBLIME, (6544,))]


class CItem1047(object):
    m_SID = 1047
    m_Name = '#NT#经济压力NPC事件宝箱替换'
    m_Rule = [
        (DAY_TRIAL_REPLACENPC, ({
            2101: {
                4103: 10,
                4011: 10,
                4012: 10,
                4013: 10,
                4104: 10,
                4105: 10 },
            2102: {
                4103: 10,
                4011: 10,
                4012: 10,
                4013: 10,
                4104: 10,
                4105: 10 },
            2103: {
                4103: 10,
                4011: 10,
                4012: 10,
                4013: 10,
                4104: 10,
                4105: 10 },
            2104: {
                4103: 10,
                4011: 10,
                4012: 10,
                4013: 10,
                4104: 10,
                4105: 10 },
            2105: {
                4103: 10,
                4011: 10,
                4012: 10,
                4013: 10,
                4104: 10,
                4105: 10 },
            2106: {
                4103: 10,
                4011: 10,
                4012: 10,
                4013: 10,
                4104: 10,
                4105: 10 },
            2107: {
                4103: 10,
                4011: 10,
                4012: 10,
                4013: 10,
                4104: 10,
                4105: 10 },
            2108: {
                4103: 10,
                4011: 10,
                4012: 10,
                4013: 10,
                4104: 10,
                4105: 10 },
            2109: {
                4103: 10,
                4011: 10,
                4012: 10,
                4013: 10,
                4104: 10,
                4105: 10 },
            2110: {
                4103: 10,
                4011: 10,
                4012: 10,
                4013: 10,
                4104: 10,
                4105: 10 },
            2111: {
                4103: 10,
                4011: 10,
                4012: 10,
                4013: 10,
                4104: 10,
                4105: 10 },
            2112: {
                4103: 10,
                4011: 10,
                4012: 10,
                4013: 10,
                4104: 10,
                4105: 10 },
            2113: {
                4103: 10,
                4011: 10,
                4012: 10,
                4013: 10,
                4104: 10,
                4105: 10 },
            2114: {
                4103: 10,
                4011: 10,
                4012: 10,
                4013: 10,
                4104: 10,
                4105: 10 },
            2115: {
                4103: 10,
                4011: 10,
                4012: 10,
                4013: 10,
                4104: 10,
                4105: 10 },
            2116: {
                4103: 10,
                4011: 10,
                4012: 10,
                4013: 10,
                4104: 10,
                4105: 10 },
            2117: {
                4103: 10,
                4011: 10,
                4012: 10,
                4013: 10,
                4104: 10,
                4105: 10 },
            2118: {
                4103: 10,
                4011: 10,
                4012: 10,
                4013: 10,
                4104: 10,
                4105: 10 },
            2119: {
                4103: 10,
                4011: 10,
                4012: 10,
                4013: 10,
                4104: 10,
                4105: 10 },
            2120: {
                4103: 10,
                4011: 10,
                4012: 10,
                4013: 10,
                4104: 10,
                4105: 10 },
            2121: {
                4103: 10,
                4011: 10,
                4012: 10,
                4013: 10,
                4104: 10,
                4105: 10 },
            2122: {
                4103: 10,
                4011: 10,
                4012: 10,
                4013: 10,
                4104: 10,
                4105: 10 },
            2123: {
                4103: 10,
                4011: 10,
                4012: 10,
                4013: 10,
                4104: 10,
                4105: 10 } },))]


class CItem1048(object):
    m_SID = 1048
    m_Name = '#NT#经济压力通关宝箱替换'
    m_Rule = [
        (DAY_TRIAL_REPLACENPC, ({
            1003: {
                6008: 10 },
            1006: {
                6009: 10 },
            1050: {
                6010: 10 },
            1055: {
                6010: 10 } },))]


class CItem1049(object):
    m_SID = 1049
    m_Name = '#NT#经济压力扣除铜币机制'
    m_Rule = [
        (DAY_TRIAL_LEVELGOAL_ADD_SKILL, (6738,)),
        (DAY_TRIAL_CHALLENGEOVER_ADD_SKILL, (6739,))]


class CItem1050(object):
    m_SID = 1050
    m_Name = '#NT#【低等级】暴击时扣除铜币，每个敌人最多触发一次'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (6740,))]


class CItem1051(object):
    m_SID = 1051
    m_Name = '#NT#生命偷取'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (6751,))]


class CItem1052(object):
    m_SID = 1052
    m_Name = '#NT#护盾值/护甲值全部转化为生命值'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (6752,))]


class CItem1053(object):
    m_SID = 1053
    m_Name = '#NT#无法获得包子'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (6722,)),
        (DAY_TRIAL_REPLACENPC, ({
            1005: {
                6001: 10 },
            1059: {
                6001: 10 } },))]


class CItem1054(object):
    m_SID = 1054
    m_Name = '#NT#1005-吸血主题-npc替换'
    m_Rule = [
        (DAY_TRIAL_REPLACENPC, ({
            2101: {
                4004: 10,
                4005: 10,
                4006: 10,
                4101: 10,
                4102: 10 },
            2102: {
                4004: 10,
                4005: 10,
                4006: 10,
                4101: 10,
                4102: 10 },
            2103: {
                4004: 10,
                4005: 10,
                4006: 10,
                4101: 10,
                4102: 10 },
            2104: {
                4004: 10,
                4005: 10,
                4006: 10,
                4101: 10,
                4102: 10 },
            2105: {
                4004: 10,
                4005: 10,
                4006: 10,
                4101: 10,
                4102: 10 },
            2106: {
                4004: 10,
                4005: 10,
                4006: 10,
                4101: 10,
                4102: 10 },
            2107: {
                4004: 10,
                4005: 10,
                4006: 10,
                4101: 10,
                4102: 10 },
            2108: {
                4004: 10,
                4005: 10,
                4006: 10,
                4101: 10,
                4102: 10 },
            2109: {
                4004: 10,
                4005: 10,
                4006: 10,
                4101: 10,
                4102: 10 },
            2110: {
                4004: 10,
                4005: 10,
                4006: 10,
                4101: 10,
                4102: 10 },
            2111: {
                4004: 10,
                4005: 10,
                4006: 10,
                4101: 10,
                4102: 10 },
            2112: {
                4004: 10,
                4005: 10,
                4006: 10,
                4101: 10,
                4102: 10 },
            2113: {
                4004: 10,
                4005: 10,
                4006: 10,
                4101: 10,
                4102: 10 },
            2114: {
                4004: 10,
                4005: 10,
                4006: 10,
                4101: 10,
                4102: 10 },
            2115: {
                4004: 10,
                4005: 10,
                4006: 10,
                4101: 10,
                4102: 10 },
            2116: {
                4004: 10,
                4005: 10,
                4006: 10,
                4101: 10,
                4102: 10 },
            2117: {
                4004: 10,
                4005: 10,
                4006: 10,
                4101: 10,
                4102: 10 },
            2118: {
                4004: 10,
                4005: 10,
                4006: 10,
                4101: 10,
                4102: 10 },
            2119: {
                4004: 10,
                4005: 10,
                4006: 10,
                4101: 10,
                4102: 10 },
            2120: {
                4004: 10,
                4005: 10,
                4006: 10,
                4101: 10,
                4102: 10 },
            2121: {
                4004: 10,
                4005: 10,
                4006: 10,
                4101: 10,
                4102: 10 },
            2122: {
                4004: 10,
                4005: 10,
                4006: 10,
                4101: 10,
                4102: 10 },
            2123: {
                4004: 10,
                4005: 10,
                4006: 10,
                4101: 10,
                4102: 10 } },))]


class CItem1061(object):
    m_SID = 1061
    m_Name = '#NT#开局3传说'
    m_Rule = [
        (DAY_TRIAL_PLAYER_RANDOM_RELIC, (RELIC_TYPE_NORMAL, QUALITY_TYPE_HIGH, 3))]


class CItem1062(object):
    m_SID = 1062
    m_Name = '#NT#开局3诅咒'
    m_Rule = [
        (DAY_TRIAL_PLAYER_RANDOM_RELIC, (RELIC_TYPE_CURSE, 0, 3))]


class CItem1063(object):
    m_SID = 1063
    m_Name = '#NT#无法丢弃秘卷'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (6761,))]


class CItem1064(object):
    m_SID = 1064
    m_Name = '#NT#秘卷相关NPC替换'
    m_Rule = [
        (DAY_TRIAL_REPLACENPC, ({
            2101: {
                4001: 10,
                4002: 10,
                4003: 10 },
            2102: {
                4001: 10,
                4002: 10,
                4003: 10 },
            2103: {
                4001: 10,
                4002: 10,
                4003: 10 },
            2104: {
                4001: 10,
                4002: 10,
                4003: 10 },
            2105: {
                4001: 10,
                4002: 10,
                4003: 10 },
            2106: {
                4001: 10,
                4002: 10,
                4003: 10 },
            2107: {
                4001: 10,
                4002: 10,
                4003: 10 },
            2108: {
                4001: 10,
                4002: 10,
                4003: 10 },
            2109: {
                4001: 10,
                4002: 10,
                4003: 10 },
            2110: {
                4001: 10,
                4002: 10,
                4003: 10 },
            2111: {
                4001: 10,
                4002: 10,
                4003: 10 },
            2112: {
                4001: 10,
                4002: 10,
                4003: 10 },
            2113: {
                4001: 10,
                4002: 10,
                4003: 10 },
            2114: {
                4001: 10,
                4002: 10,
                4003: 10 },
            2115: {
                4001: 10,
                4002: 10,
                4003: 10 },
            2116: {
                4001: 10,
                4002: 10,
                4003: 10 },
            2117: {
                4001: 10,
                4002: 10,
                4003: 10 },
            2118: {
                4001: 10,
                4002: 10,
                4003: 10 },
            2119: {
                4001: 10,
                4002: 10,
                4003: 10 },
            2120: {
                4001: 10,
                4002: 10,
                4003: 10 },
            2121: {
                4001: 10,
                4002: 10,
                4003: 10 },
            2122: {
                4001: 10,
                4002: 10,
                4003: 10 },
            2123: {
                4001: 10,
                4002: 10,
                4003: 10 } },)),
        (DAY_TRIAL_CHANGE_CHOOSE_CNT, (LAYER_CHOOSE_EVENTNPC, 2, {
            (3, 3): 2,
            (2, 3): 2,
            (4, 2): 2,
            (4, 1): 2,
            (1, 4): 2 }))]


class CItem1065(object):
    m_SID = 1065
    m_Name = '#NT#开局额外获得N个稀有秘卷'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (6789,))]


class CItem1071(object):
    m_SID = 1071
    m_Name = '#NT#所有非元素武器随机获得一种属性'
    m_Rule = [
        (DAY_TRIAL_CHANGE_WEAPON_DAM_TYPE, (4832, 4833, 4834))]


class CItem1072(object):
    m_SID = 1072
    m_Name = '#NT#所有武器元素异常概率*3'
    m_Rule = [
        (DAY_TRIAL_CHANGE_WEAPON_DEBUFF_PROB, (20000, 0))]


class CItem1073(object):
    m_SID = 1073
    m_Name = '#NT#元素异常会扩散7m以内所有单位'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (6773,))]


class CItem1075(object):
    m_SID = 1075
    m_Name = '#NT#修改怪物词缀抽取'
    m_Rule = [
        (DAY_TRIAL_CHANGE_MONSTER_AF, ({
            6101: (33, 0),
            6102: (33, 0),
            6103: (34, 0) },))]


class CItem1076(object):
    m_SID = 1076
    m_Name = '#NT#增加元素被克制减伤比例和元素克制增伤比例'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (16775,)),
        (DAY_TRIAL_MONSTER_ADD_SKILL, (16775, { }))]


class CItem1077(object):
    m_SID = 1077
    m_Name = '#NT#对怪物造成的元素异常效果增强'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (6788,))]


class CItem1081(object):
    m_SID = 1081
    m_Name = '#NT#击杀怪物掉落宝'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (6781,)),
        (DAY_TRIAL_MONSTER_ADD_SKILL, (6785, { }))]


class CItem1082(object):
    m_SID = 1082
    m_Name = '#NT#玩家拾取宝珠后加40%移速3s'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (6782,))]


class CItem1083(object):
    m_SID = 1083
    m_Name = '#NT#玩家每拾取一个宝珠获得一层buff'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (6783,))]


class CItem1084(object):
    m_SID = 1084
    m_Name = '#NT#宝珠消失时将6m内的怪物进行连接'
    m_Rule = [
        (DAY_TRIAL_USE_PERFORM_WHEN_DRIO_DISPPEAR, (1675, 1163, 200)),
        (DAY_TRIAL_PLAYER_ADD_SKILL, (6784,))]


class CItem1085(object):
    m_SID = 1085
    m_Name = '#NT#直面强敌屏蔽房间挑战'
    m_Rule = [
        (DAY_TRIAL_IGNORECHALLENGE, ('30091030|30091055|30091050|30091003|30091004',))]


class CItem1086(object):
    m_SID = 1086
    m_Name = '#NT#妖晶遗华初始武器宝箱替换'
    m_Rule = [
        (DAY_TRIAL_REPLACENPC, ({
            6005: {
                6011: 10 } },))]


class CItem1087(object):
    m_SID = 1087
    m_Name = '#NT#【低等级】每一层结晶效果，都使武器伤害额外增加'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (6786,))]


class CItem1091(object):
    m_SID = 1091
    m_Name = '#NT#只掉落可以触发爆炸的武器'
    m_Rule = []


class CItem1092(object):
    m_SID = 1092
    m_Name = '#NT#1009爆炸狂欢屏蔽房间挑战'
    m_Rule = [
        (DAY_TRIAL_IGNORECHALLENGE, ('30091015',))]


class CItem1093(object):
    m_SID = 1093
    m_Name = '#NT#额外附加最高射击伤害'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (16793,)),
        (DAY_TRIAL_EXTRA_INFO, (2000,))]


class CItem1094(object):
    m_SID = 1094
    m_Name = '#NT#爆炸狂欢加伤'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (6790,))]


class CItem1101(object):
    m_SID = 1101
    m_Name = '破旧瞄具'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4601,))]


class CItem1102(object):
    m_SID = 1102
    m_Name = '意外治疗'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4602,))]


class CItem1103(object):
    m_SID = 1103
    m_Name = '动能装甲'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (14603,))]


class CItem1111(object):
    m_SID = 1111
    m_Name = '精确瞄准'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4401,))]


class CItem1112(object):
    m_SID = 1112
    m_Name = '命运处决'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4402,))]


class CItem1113(object):
    m_SID = 1113
    m_Name = '幸运累积'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4403,))]


class CItem1114(object):
    m_SID = 1114
    m_Name = '元素暴击'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4404,))]


class CItem1201(object):
    m_SID = 1201
    m_Name = '#NT#怪物复活后，生命值减少50%且攻速（攻击间隔）与移速增加30%'
    m_Rule = [
        (DAY_TRIAL_MONSTER_ADD_SKILL, (4611, { }))]


class CItem1202(object):
    m_SID = 1202
    m_Name = '高额诊费'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4612,))]


class CItem1203(object):
    m_SID = 1203
    m_Name = '轮回遗病'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4613,))]


class CItem1211(object):
    m_SID = 1211
    m_Name = '关键时停'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4411,))]


class CItem1212(object):
    m_SID = 1212
    m_Name = '额外遗产'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4412,))]


class CItem1213(object):
    m_SID = 1213
    m_Name = '强效转生'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4413,))]


class CItem1301(object):
    m_SID = 1301
    m_Name = '禁止误伤'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4621,))]


class CItem1302(object):
    m_SID = 1302
    m_Name = '生命顽强'
    m_Rule = [
        (DAY_TRIAL_MONSTER_ADD_SKILL, (4622, { }))]


class CItem1303(object):
    m_SID = 1303
    m_Name = '天赋屏障'
    m_Rule = [
        (DAY_TRIAL_MONSTER_ADD_SKILL, (4623, { }))]


class CItem1304(object):
    m_SID = 1304
    m_Name = '妖力侵蚀'
    m_Rule = [
        (DAY_TRIAL_MONSTER_ADD_SKILL, (4624, { }))]


class CItem1311(object):
    m_SID = 1311
    m_Name = '火力倾泻'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4421,))]


class CItem1312(object):
    m_SID = 1312
    m_Name = '极速追击'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (14422,))]


class CItem1313(object):
    m_SID = 1313
    m_Name = '凤凰浴火'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4423,))]


class CItem1314(object):
    m_SID = 1314
    m_Name = '绝地求生'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4424,))]


class CItem1401(object):
    m_SID = 1401
    m_Name = '无商不奸'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4631,))]


class CItem1402(object):
    m_SID = 1402
    m_Name = '雪上加霜'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4632,))]


class CItem1403(object):
    m_SID = 1403
    m_Name = '贪财小妖'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4634,))]


class CItem1411(object):
    m_SID = 1411
    m_Name = '良心商家'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4431,)),
        (DAY_TRIAL_REPLACENPC, ({
            1005: {
                6006: 10 },
            6004: {
                6006: 10 } },)),
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4432,))]


class CItem1412(object):
    m_SID = 1412
    m_Name = '#NT#工匠处武器强化一次强化等级+2'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4432,))]


class CItem1413(object):
    m_SID = 1413
    m_Name = '元素货币'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (14433,))]


class CItem1414(object):
    m_SID = 1414
    m_Name = '#NT#玩家每通关一次扣除当前40%铜币'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4434,))]


class CItem1415(object):
    m_SID = 1415
    m_Name = '刮刮乐'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (6787,))]


class CItem1501(object):
    m_SID = 1501
    m_Name = '#NT#使用冲刺技能额外消耗5%生命值'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4641,))]


class CItem1502(object):
    m_SID = 1502
    m_Name = '诅咒弹夹'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4642,))]


class CItem1503(object):
    m_SID = 1503
    m_Name = '伤口撕裂'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4643,))]


class CItem1504(object):
    m_SID = 1504
    m_Name = '#NT#1005持续扣血屏蔽房间挑战'
    m_Rule = [
        (DAY_TRIAL_IGNORECHALLENGE, ('30091021|30091022|30091050',))]


class CItem1505(object):
    m_SID = 1505
    m_Name = '#NT#生命回复效果增加'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (6798,))]


class CItem1511(object):
    m_SID = 1511
    m_Name = '超额汲取'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4441,))]


class CItem1512(object):
    m_SID = 1512
    m_Name = '额外血源'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (14442,))]


class CItem1513(object):
    m_SID = 1513
    m_Name = '猩红满溢'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (14443,))]


class CItem1514(object):
    m_SID = 1514
    m_Name = '状态良好'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4444,))]


class CItem1515(object):
    m_SID = 1515
    m_Name = '伤情延迟'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4445,))]


class CItem1601(object):
    m_SID = 1601
    m_Name = '有限行囊'
    m_Rule = [
        (DAY_TRIAL_SET_MAX_RELIC, (10,))]


class CItem1602(object):
    m_SID = 1602
    m_Name = '各安天命'
    m_Rule = [
        (DAY_TRIAL_REPLACENPC, ({
            1514: {
                1598: 10 },
            1515: {
                1599: 10 },
            1516: {
                1599: 10 },
            1517: {
                1599: 10 },
            1518: {
                1599: 10 },
            1520: {
                1598: 10 },
            1519: {
                1599: 10 } },))]


class CItem1603(object):
    m_SID = 1603
    m_Name = '命途多舛'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4651,))]


class CItem1611(object):
    m_SID = 1611
    m_Name = '厄运之子'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4451,))]


class CItem1612(object):
    m_SID = 1612
    m_Name = '传奇赠品'
    m_Rule = [
        (DAY_TRIAL_ADD_RELIC_WHEN_PICK_RELIC, (QUALITY_TYPE_HIGH, 30092401))]


class CItem1613(object):
    m_SID = 1613
    m_Name = '幸运卷轴'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4452,))]


class CItem1614(object):
    m_SID = 1614
    m_Name = '逆天改命'
    m_Rule = [
        (DAY_TRIAL_SET_REFRESH_RELIC, (5, 2401))]


class CItem1701(object):
    m_SID = 1701
    m_Name = '元素荒漠'
    m_Rule = [
        (DAY_TRIAL_CHANGE_ELEMENT_DAM, (4661,))]


class CItem1702(object):
    m_SID = 1702
    m_Name = '元素烙印'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (14662,))]


class CItem1703(object):
    m_SID = 1703
    m_Name = '元素过敏'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (14663,))]


class CItem1711(object):
    m_SID = 1711
    m_Name = '元素勃发'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4461,))]


class CItem1712(object):
    m_SID = 1712
    m_Name = '元素遗宝'
    m_Rule = [
        (DAY_TRIAL_RANDOM_RELIC_IN_LIST, ({
            5781: 0,
            5782: 0,
            5783: 0,
            5795: 1,
            5796: 1,
            5797: 1 },))]


class CItem1713(object):
    m_SID = 1713
    m_Name = '元素成长'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4463,))]


class CItem1801(object):
    m_SID = 1801
    m_Name = '定点火力'
    m_Rule = [
        (DAY_TRIAL_USE_PERFORM_WHEN_DRIO_DISPPEAR, (1693, 1163, 200))]


class CItem1802(object):
    m_SID = 1802
    m_Name = '伤害豁免'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4672,)),
        (DAY_TRIAL_BEAD_DROP_SCENEEVENT_DROP, (6, 4674, 50))]


class CItem1803(object):
    m_SID = 1803
    m_Name = '治愈之息'
    m_Rule = [
        (DAY_TRIAL_USE_PERFORM_WHEN_DRIO_DISPPEAR, (1676, 1163, 200))]


class CItem1811(object):
    m_SID = 1811
    m_Name = '充能核心'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (14664,))]


class CItem1812(object):
    m_SID = 1812
    m_Name = '移动装置'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_RELIC, (5761, 1)),
        (DAY_TRIAL_PLAYER_ADD_RELIC, (5774, 1))]


class CItem1813(object):
    m_SID = 1813
    m_Name = '奥术结晶'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4473,))]


class CItem1901(object):
    m_SID = 1901
    m_Name = '友军伤害'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4681,))]


class CItem1902(object):
    m_SID = 1902
    m_Name = '劣质火药'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (14682,))]


class CItem1903(object):
    m_SID = 1903
    m_Name = '底力爆发'
    m_Rule = [
        (DAY_TRIAL_MONSTER_ADD_SKILL, (4683, { }))]


class CItem1904(object):
    m_SID = 1904
    m_Name = '#NT#怪物受到爆炸伤害在3s内会以流血形式扣除'
    m_Rule = [
        (DAY_TRIAL_MONSTER_ADD_SKILL, (4684, { }))]


class CItem1911(object):
    m_SID = 1911
    m_Name = '枪火时间'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (14481,))]


class CItem1912(object):
    m_SID = 1912
    m_Name = '精准制导'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4482,))]


class CItem1913(object):
    m_SID = 1913
    m_Name = '聚能火炮'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4483,))]


class CItem1914(object):
    m_SID = 1914
    m_Name = '炮火连天'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4484,))]


class CItem1915(object):
    m_SID = 1915
    m_Name = '#NT#屏蔽钱龙挑战关'
    m_Rule = [
        (DAY_TRIAL_FILTER_ASSIGN_HIDELEVEL, ((1300104, 1101112, 1201119, 1101215, 1201220),))]


class CItem1916(object):
    m_SID = 1916
    m_Name = '#NT#修改主线关卡道具抽取配置'
    m_Rule = [
        (DAY_TRIAL_CHANGE_MAINLV_ITEMCHOOSE, ({
            1004: 1,
            1005: 2,
            1006: 3 },))]


class CItem2001(object):
    m_SID = 2001
    m_Name = '#NT#武器穿透+1'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (6791,))]


class CItem2002(object):
    m_SID = 2002
    m_Name = '#NT#武器伤害不随距离衰减'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (6792,))]


class CItem2003(object):
    m_SID = 2003
    m_Name = '#NT#只掉落狙击枪'
    m_Rule = []


class CItem2004(object):
    m_SID = 2004
    m_Name = '#NT#不掉落标准弹'
    m_Rule = [
        (DAY_TRIAL_CHANGE_MINIGAME_INFO, (4502, 0, -15))]


class CItem2005(object):
    m_SID = 2005
    m_Name = '#NT#1010狙击精英屏蔽房间挑战'
    m_Rule = [
        (DAY_TRIAL_IGNORECHALLENGE, ('30091051',))]


class CItem2006(object):
    m_SID = 2006
    m_Name = '#NT#一击击杀增加武器属性'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (6794,))]


class CItem2007(object):
    m_SID = 2007
    m_Name = '#NT#【低等级】狙击枪造成额外伤害（距离越远伤害越高，距离最大取50米）'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (6796,))]


class CItem2031(object):
    m_SID = 2031
    m_Name = '#NT#每次通关复活次数补满'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (6797,))]


class CItem2101(object):
    m_SID = 2101
    m_Name = '擒贼擒王'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4693,)),
        (DAY_TRIAL_MONSTER_ADD_SKILL, (4691, { }))]


class CItem2102(object):
    m_SID = 2102
    m_Name = '关键失误'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4692,)),
        (DAY_TRIAL_CHANGE_ELEMENT_DAM, (4694,)),
        (DAY_TRIAL_MONSTER_ADD_SKILL, (4695, { }))]


class CItem2103(object):
    m_SID = 2103
    m_Name = '妖蛰庇护'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4696,)),
        (DAY_TRIAL_IGNORECHALLENGE, ('30081054|30081051',)),
        (DAY_TRIAL_FILTER_ASSIGN_HIDELEVEL, ((1101234, 1101233),)),
        (DAY_TRIAL_FILTER_ASSIGN_MAINLEVEL, ((1105102, 1105103, 1105104, 1105105, 1105106),))]


class CItem2111(object):
    m_SID = 2111
    m_Name = '连续执行'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4491,))]


class CItem2112(object):
    m_SID = 2112
    m_Name = '爆炸弹头'
    m_Rule = [
        (DAY_TRIAL_MONSTER_ADD_SKILL, (4492, { }))]


class CItem2113(object):
    m_SID = 2113
    m_Name = '摄魂一击'
    m_Rule = [
        (DAY_TRIAL_PLAYER_ADD_SKILL, (4493,))]

