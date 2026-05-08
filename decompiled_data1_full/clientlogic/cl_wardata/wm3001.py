# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/wm3001.pyc
# RelativePath: clientlogic/cl_wardata/wm3001.pyc
# Source Generated with Decompyle++
# File: wm3001.pyc (Python 3.6)

from __future__ import absolute_import
from cl_warmgr.mobject import CWarManager as CCustomWarMgr
from cl_commondefines import BACKPACK_BLOOM, BACKPACK_CORROSIVESPIKES, BACKPACK_HPDAM, BACKPACK_METEOR, BACKPACK_SELFEXPLODE, BACKPACK_SHOOTOFF, BACKPACK_THUNDERBLADE, BACKPACK_TOXICHAZE, CAPACITOR_WAND, DICE_CONTROL, DICE_EJECT, DICE_METEOR, DICE_SELFEXPLODE, DICE_SPRINT, DICE_WAVE, ENDLESS_REAL, ENDLESS_TIME, GAMETYPE_DESTROY, HIDELV_TYPE_CASH, HIDELV_TYPE_DEFEND, HIDELV_TYPE_ELITE, HIDELV_TYPE_JUMP, HIDELV_TYPE_NORMAL, HIDELV_TYPE_PETROCHEMICAL, HIDELV_TYPE_SIGHT, HIDELV_TYPE_TRAP, LAYER_CHOOSE_CHALLENGE, LAYER_CHOOSE_CRAFTSMAN, LAYER_CHOOSE_DICESHOP, LAYER_CHOOSE_EVENTNPC, LAYER_CHOOSE_GSCASHSHOP, LAYER_CHOOSE_HIDE, LAYER_CHOOSE_PETSHOP, LAYER_CHOOSE_REGROUPRELIC, LAYER_CHOOSE_RELICLOTTERY, LAYER_CHOOSE_S7SHOP, LAYER_CHOOSE_S8SHOP, LAYER_CHOOSE_SHOP, LAYER_CHOOSE_TASKNPC, LAYER_CHOOSE_WANDSHOP, LEVEL_TYPE_BOSS, LEVEL_TYPE_FIGHT, LEVEL_TYPE_HALL, LEVEL_TYPE_HIDE, LIGHTNING_WANDCOMP, METEOR_WANDCOMP, MODE_REAL_ENDLESS, MODE_SNOWMOUNTAINS, ORBIT_WAND, OVERLOAD_WAND, ROUND_EXTRULE_APPEARCHALLENGE, ROUND_EXTRULE_REPLACECONFIG_CHALLENGE, ROUND_EXTRULE_REPLACEMONSTER, ROUND_EXTRULE_SMASHOBSTACLE_CREATEMONSTER_LOCKROOM, ROUND_EXTRULE_TRANSOBSTACLE_TO_MONSTER, S8_THIRDACTIVE_ELITE_TEAM, S8_THIRDACTIVE_FISH_DRAGON, S8_THIRDACTIVE_GLUTTONY, S8_THIRDACTIVE_SHIELD, S8_THIRDACTIVE_SUPER_MUSHROOM, SEASONFUNC_ACTION_PET, SEASONFUNC_FUSERESET_PET, SEASONFUNC_FUSE_PET, SEASONFUNC_OPEN_WANDABILITY, SEASONFUNC_REFRESH_PETSHOP, SEASONFUNC_S7_OPEN_ENHANCE, SWORD_WANDCOMP, WARRIOR_ELITE
from cl_newformula import Func201, Func202, Func205, Func209, Func221, Func244, Func245, Func544, Func572, Func605, Func656, Func678, Func690, Func766
from math import ceil
import cl_msgcenter
import cl_warmgr.waraction as waraction
import cl_warmgr.warcondition as warcondition
import cl_warmgr.initresourceelement
import cl_warmgr.levelctrl
import cl_warmgr.warreport
import cl_warmgr.pvedieelement
import cl_warmgr.weaponanalyse
import cl_warmgr.teaminfoelement
import cl_warmgr.roundelement
import cl_warmgr.monsterspelement
import cl_warmgr.watchelement
import cl_warmgr.saveelement
import cl_warmgr.bigdataanalyse
import cl_warmgr.teamsaveelement
import cl_signal
import cl_warmgr.rescueelement
import cl_warmgr.recycledropelement
import cl_warmgr.checkcheatelement
import cl_warmgr.hangupkickelement
import cl_warmgr.suitelement
import cl_warmgr.snowmountainelement
import cl_warmgr.ridingaloneelement
import cl_warmgr.monsterrelicelement
import cl_warmgr.rollrelicelement
import cl_warmgr.weaponstoreelement
import cl_warmgr.talentfusionelement
import cl_warmgr.taskelement
import cl_warmgr.endlesselement
import cl_warmgr.teammateaielement
import cl_warmgr.relictalentelement
import cl_warmgr.realendlesselement
import cl_warmgr.deviceelement
import cl_warmgr.conquerelement
import cl_warmgr.regrouprelicelement
import cl_warmgr.newbietutorialelement
import cl_warmgr.seasonsuitelement
import cl_warmgr.wandelement
import cl_warmgr.diceelement
import cl_warmgr.backpackelement
import cl_warmgr.playerextraelement
import cl_warmgr.s8element

def ChooseAction11101009(oWarMgr, iLevel):
    return warcondition.WarCheckHistoryKillBoss(oWarMgr, iLevel, {
        39011: 1 }, 5)


def ForceAction11101009(oWarMgr, iLevel):
    return warcondition.WarCheckForceLevel(oWarMgr, iLevel, {
        39011: 1 }, 5)


def ChooseAction11103154(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction11103155(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction11103157(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction11103161(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction11103158(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction11103159(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction11103160(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction11103162(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction11103165(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction11103167(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction11103168(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction11103169(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction11103170(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction11103171(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction11103172(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction11103173(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction11103174(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction11105101(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction11105102(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction11105103(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction11105104(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction11105105(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction11105106(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction11105107(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction11105109(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction11105110(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction11105114(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction11105111(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction11105112(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction11105113(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction11105115(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction11105116(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction21202003(oWarMgr, iLevel):
    return warcondition.WarCheckHistoryKillBoss(oWarMgr, iLevel, {
        39131: 1 }, 5)


def ForceAction21202003(oWarMgr, iLevel):
    return warcondition.WarCheckForceLevel(oWarMgr, iLevel, {
        39131: 1 }, 5)


def ChooseAction21203141(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction21203142(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction21203143(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction21203145(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction21203146(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction21203144(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction21203147(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction21203148(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction21203149(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction21203150(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction21203151(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction21203152(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction21203153(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction21203154(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction21203155(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction21203156(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction21203157(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction21205101(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction21205102(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction21205103(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction21205104(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction21205105(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction21205106(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction21205107(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction21205108(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction21205109(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction21205110(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction21205111(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction21205112(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction21205113(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction21205114(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction21205115(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction21205116(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction21205117(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction21205118(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction21205119(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction31301003(oWarMgr, iLevel):
    return warcondition.WarCheckHistoryKillBoss(oWarMgr, iLevel, {
        39051: 1 }, 3)


def ForceAction31301003(oWarMgr, iLevel):
    return warcondition.WarCheckForceLevel(oWarMgr, iLevel, {
        39051: 1 }, 3)


def ChooseAction31302101(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction31302102(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction31302103(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction31302104(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction31302105(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction31302120(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction31302107(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction31302108(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction31302161(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction31302162(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction31302110(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction31302111(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction31302112(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction31302113(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction31302114(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction31302115(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction31302163(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction31303101(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction31303102(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction31303103(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction31303104(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction31303105(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction31303106(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction31303107(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction31303108(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 0


def ChooseAction31303110(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction31303111(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction31303112(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction31303109(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction31303113(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction31303116(oWarMgr, iLevel):
    return warcondition.WarCheckNewVerLayer(oWarMgr, iLevel) == 1


def ChooseAction41403001(oWarMgr, iLevel):
    if warcondition.WarCheckSpecifcMode(oWarMgr, iLevel, 1002) == 0 and warcondition.WarCheckCycle(oWarMgr, iLevel, 9) == 0:
        pass
    return warcondition.WarCheckCycle(oWarMgr, iLevel, 10) == 0


def ChooseAction41403002(oWarMgr, iLevel):
    if not warcondition.WarCheckSpecifcMode(oWarMgr, iLevel, 1002) or warcondition.WarCheckCycle(oWarMgr, iLevel, 9):
        pass
    return warcondition.WarCheckCycle(oWarMgr, iLevel, 10)


def ChooseAction41403003(oWarMgr, iLevel):
    if warcondition.WarCheckHistoryKillBoss(oWarMgr, iLevel, {
        39241: 1,
        39251: 1 }, 3) and warcondition.WarCheckSpecifcMode(oWarMgr, iLevel, 1002) == 0 and warcondition.WarCheckCycle(oWarMgr, iLevel, 9) == 0:
        pass
    return warcondition.WarCheckCycle(oWarMgr, iLevel, 10) == 0


def ForceAction41403003(oWarMgr, iLevel):
    if warcondition.WarCheckForceLevel(oWarMgr, iLevel, {
        39241: 1,
        39251: 1 }, 3) and warcondition.WarCheckSpecifcMode(oWarMgr, iLevel, 1002) == 0 and warcondition.WarCheckCycle(oWarMgr, iLevel, 9) == 0:
        pass
    return warcondition.WarCheckCycle(oWarMgr, iLevel, 10) == 0


def ChooseAction41403004(oWarMgr, iLevel):
    if warcondition.WarCheckSpecifcMode(oWarMgr, iLevel, 1002) or warcondition.WarCheckCycle(oWarMgr, iLevel, 9) or warcondition.WarCheckCycle(oWarMgr, iLevel, 10):
        pass
    return warcondition.WarCheckHistoryKillBoss(oWarMgr, iLevel, {
        39241: 1,
        39251: 1 }, 3)


def ForceAction41403004(oWarMgr, iLevel):
    if not warcondition.WarCheckForceLevel(oWarMgr, iLevel, {
        39241: 1,
        39251: 1 }, 3) and warcondition.WarCheckCycle(oWarMgr, iLevel, 9) or warcondition.WarCheckSpecifcMode(oWarMgr, iLevel, 1002):
        pass
    return warcondition.WarCheckCycle(oWarMgr, iLevel, 10)


class CInitResourceElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'INITBULLET': ((4502, 30), (4503, 10), (4504, 4), (4508, 8)) }


class CLevelCtrlElement(cl_warmgr.mobject.CElementData):
    m_LevelCtrlConf = {
        1: {
            'CtrlSize': 4,
            'HallInfo': 1100001,
            'BossInfo': {
                'BossStore': {
                    1101009: 10,
                    1101006: 10,
                    1101007: 0 },
                'BossExtra': {
                    1101009: (ChooseAction11101009, ForceAction11101009),
                    1101006: (None, None),
                    1101007: (None, None) },
                'ChallengeStore': {
                    (3, 9): [
                        (1080, 1),
                        (1106, 1),
                        (1102, 1),
                        (1119, 1),
                        (1120, 1),
                        (1121, 1)],
                    (3, 8): [
                        (1080, 1),
                        (1106, 1),
                        (1092, 0),
                        (1099, 1),
                        (1102, 1)] },
                'SingleChallengeStore': {
                    (3, 9): [
                        (1080, 1),
                        (1106, 1),
                        (1102, 1),
                        (1120, 1),
                        (1121, 1)],
                    (3, 8): [] },
                'ExcludeChallengeArea': {
                    (3, 9): [
                        (1010103, 2),
                        (1010103, 3)],
                    (3, 8): [
                        (1010103, 2),
                        (1010103, 3)] },
                'UnSpawnRuleInfo': {
                    1101009: [],
                    1101006: [],
                    1101007: [] },
                'ChallengeModeLimit': {
                    (3, 9, 0): {
                        'MULTI': [],
                        'SINGLE': [] },
                    (3, 8, 0): {
                        'MULTI': [],
                        'SINGLE': [] } },
                'AIBosslevelEnhance': {
                    1101009: 40,
                    1101006: 40,
                    1101007: 0 } },
            'NpcInfo': {
                'shop': {
                    1005: 10 },
                'craftsman': {
                    1018: 10 },
                'gscashshop': {
                    1054: 10 },
                'tasknpc': {
                    1065: 10 },
                'petshop': {
                    1068: 10 },
                'reliclottery': {
                    1071: 10 },
                'regrouprelic': {
                    1069: 10 },
                'wandshop': {
                    1072: 10 },
                'diceshop': {
                    1073: 10 },
                's7shop': {
                    1074: 10 },
                's8shop': {
                    1075: 10 } },
            'CtrlInfo': {
                1: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (1101176, 1101177, 1101178, 1101179, 1101180, 1101181, 1101182, 1101183, 1101184, 1101185, 1101186),
                    'NormalFilter': {
                        1101176: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1101177: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1101178: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1101179: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1101180: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1101181: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1101182: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1101183: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1101184: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1101185: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1101186: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None } },
                    'MediumStore': (),
                    'HardStore': (),
                    'NormalWeight': {
                        GAMETYPE_DESTROY: 100 },
                    'MediumWeight': { },
                    'HardWeight': { },
                    'ChallengeStore': {
                        (3, 10): None,
                        (3, 9): None,
                        (3, 8): [],
                        (3, 0): [
                            (1003, 1)],
                        (2, 0): [
                            (1003, 1)],
                        (1, 0): None },
                    'SingleChallengeStore': {
                        (3, 10): [],
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelRoomChallenge': {
                        (3, 10): [],
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelExcludeChallenge': {
                        (3, 10): {
                            1101201: [],
                            1101202: [],
                            1101203: [],
                            1101209: [],
                            1101210: [],
                            1101217: [] },
                        3: {
                            1101201: [],
                            1101202: [],
                            1101203: [],
                            1101209: [],
                            1101210: [],
                            1101217: [] },
                        2: {
                            1101201: [],
                            1101202: [],
                            1101203: [],
                            1101209: [],
                            1101210: [],
                            1101217: [] },
                        1: {
                            1101201: [],
                            1101202: [],
                            1101203: [],
                            1101209: [],
                            1101210: [],
                            1101217: [] } },
                    'HideLevel': {
                        1: {
                            1101201: 1,
                            1101202: 1,
                            1101203: 1,
                            1101209: 1,
                            1101210: 1,
                            1101217: 1 },
                        2: {
                            1101201: 1,
                            1101202: 1,
                            1101203: 1,
                            1101209: 1,
                            1101210: 1,
                            1101217: 1 },
                        3: {
                            1101201: 1,
                            1101202: 1,
                            1101203: 1,
                            1101209: 1,
                            1101210: 1,
                            1101217: 1 } },
                    'HideLevelStore': {
                        (3, 10): {
                            (1101217, 1, 0, (0, 1000), -1): 10,
                            (1101210, 1, 0, (0, 1000), -1): 10,
                            (1101209, 1, 0, (0, 1000), -1): 10,
                            (1101203, 1, 0, (0, 1000), -1): 10,
                            (1101202, 1, 0, (0, 1000), -1): 10,
                            (1101201, 1, 0, (0, 1000), -1): 10 },
                        3: {
                            (1101217, 1, 0, (0, 1000), -1): 10,
                            (1101210, 1, 0, (0, 1000), -1): 10,
                            (1101209, 1, 0, (0, 1000), -1): 10,
                            (1101203, 1, 0, (0, 1000), -1): 10,
                            (1101202, 1, 0, (0, 1000), -1): 10,
                            (1101201, 1, 0, (0, 1000), -1): 10 },
                        2: {
                            (1101217, 1, 0, (0, 1000), -1): 10,
                            (1101210, 1, 0, (0, 1000), -1): 10,
                            (1101209, 1, 0, (0, 1000), -1): 10,
                            (1101203, 1, 0, (0, 1000), -1): 10,
                            (1101202, 1, 0, (0, 1000), -1): 10,
                            (1101201, 1, 0, (0, 1000), -1): 10 },
                        1: {
                            (1101217, 1, 0, (0, 1000), -1): 10,
                            (1101210, 1, 0, (0, 1000), -1): 10,
                            (1101209, 1, 0, (0, 1000), -1): 10,
                            (1101203, 1, 0, (0, 1000), -1): 10,
                            (1101202, 1, 0, (0, 1000), -1): 10,
                            (1101201, 1, 0, (0, 1000), -1): 10 } },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': {
                        (3, 10): [],
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'AIlevelEnhance': 24 },
                2: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (1102133, 1102134, 1102135, 1102136, 1102137, 1102138, 1102139, 1102140),
                    'NormalFilter': {
                        1102133: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1102134: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1102135: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1102136: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1102137: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1102138: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1102139: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1102140: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None } },
                    'MediumStore': (),
                    'HardStore': (),
                    'NormalWeight': {
                        GAMETYPE_DESTROY: 100 },
                    'MediumWeight': { },
                    'HardWeight': { },
                    'ChallengeStore': {
                        (3, 10): None,
                        (3, 9): [
                            (1099, 1),
                            (1081, 1),
                            (1083, 1)],
                        (3, 8): [
                            (1077, 0),
                            (1081, 1),
                            (1100, 1)],
                        (3, 0): [
                            (1001, 1),
                            (1003, 1)],
                        (2, 0): [
                            (1001, 1),
                            (1003, 1),
                            (1053, 1)],
                        (1, 0): None },
                    'SingleChallengeStore': {
                        (3, 10): [],
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelRoomChallenge': {
                        (3, 10): [],
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelExcludeChallenge': {
                        (3, 10): {
                            1101201: [],
                            1101202: [],
                            1101203: [],
                            1101601: [
                                1001,
                                1004,
                                1008,
                                1073],
                            1101602: [],
                            1101603: [],
                            1101605: [
                                1001,
                                1073],
                            1101606: [] },
                        3: {
                            1101201: [],
                            1101202: [],
                            1101203: [],
                            1101601: [
                                1001,
                                1004,
                                1008,
                                1073],
                            1101602: [],
                            1101603: [],
                            1101605: [
                                1001,
                                1073],
                            1101606: [] },
                        2: {
                            1101201: [],
                            1101202: [],
                            1101203: [],
                            1101601: [],
                            1101602: [],
                            1101603: [],
                            1101605: [],
                            1101606: [] },
                        1: {
                            1101201: [],
                            1101202: [],
                            1101203: [],
                            1101601: [],
                            1101602: [],
                            1101603: [] } },
                    'HideLevel': {
                        1: {
                            1101201: 1,
                            1101202: 1,
                            1101203: 1,
                            1101601: 1,
                            1101602: 5,
                            1101603: 5 },
                        2: {
                            1101201: 1,
                            1101202: 1,
                            1101203: 1,
                            1101601: 1,
                            1101602: 5,
                            1101603: 5,
                            1101605: 1,
                            1101606: 4 },
                        3: {
                            1101201: 1,
                            1101202: 1,
                            1101203: 1,
                            1101601: 1,
                            1101602: 5,
                            1101603: 5,
                            1101605: 1,
                            1101606: 4 } },
                    'HideLevelStore': {
                        (3, 10): {
                            (1101606, 4, 0, (40, 1000), -1): 0,
                            (1101605, 1, 0, (40, 1000), -1): 10,
                            (1101603, 5, 1, (0, 1000), -1): 2,
                            (1101602, 5, 1, (0, 1000), -1): 8,
                            (1101601, 1, 0, (0, 1000), -1): 10,
                            (1101203, 1, 0, (0, 1000), -1): 10,
                            (1101202, 1, 0, (0, 1000), -1): 10,
                            (1101201, 1, 0, (0, 1000), -1): 10 },
                        3: {
                            (1101606, 4, 0, (40, 1000), -1): 0,
                            (1101605, 1, 0, (40, 1000), -1): 10,
                            (1101603, 5, 1, (0, 1000), -1): 2,
                            (1101602, 5, 1, (0, 1000), -1): 8,
                            (1101601, 1, 0, (0, 1000), -1): 10,
                            (1101203, 1, 0, (0, 1000), -1): 10,
                            (1101202, 1, 0, (0, 1000), -1): 10,
                            (1101201, 1, 0, (0, 1000), -1): 10 },
                        2: {
                            (1101606, 4, 0, (40, 1000), -1): 0,
                            (1101605, 1, 0, (40, 1000), -1): 10,
                            (1101603, 5, 1, (0, 1000), -1): 2,
                            (1101602, 5, 1, (0, 1000), -1): 8,
                            (1101601, 1, 0, (0, 1000), -1): 10,
                            (1101203, 1, 0, (0, 1000), -1): 10,
                            (1101202, 1, 0, (0, 1000), -1): 10,
                            (1101201, 1, 0, (0, 1000), -1): 10 },
                        1: {
                            (1101603, 5, 1, (0, 1000), -1): 2,
                            (1101602, 5, 1, (0, 1000), -1): 8,
                            (1101601, 1, 0, (0, 1000), -1): 10,
                            (1101203, 1, 0, (0, 1000), -1): 10,
                            (1101202, 1, 0, (0, 1000), -1): 10,
                            (1101201, 1, 0, (0, 1000), -1): 10 } },
                    'HideLevelConfMap': {
                        1101606: 1101606,
                        1101616: 1101606,
                        1101626: 1101606,
                        1101636: 1101606 },
                    'HideLevelAllocMap': {
                        1101606: [
                            1101606,
                            1101616,
                            1101626,
                            1101636] },
                    'ExcludeChallengeArea': {
                        (3, 10): [],
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'AIlevelEnhance': 34 },
                3: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (1103154, 1103155, 1103157, 1103161, 1103158, 1103159, 1103160, 1103162, 1103165, 1103167, 1103168, 1103169, 1103170, 1103171, 1103172, 1103173, 1103174),
                    'NormalFilter': {
                        1103154: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction11103154 },
                        1103155: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction11103155 },
                        1103157: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction11103157 },
                        1103161: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction11103161 },
                        1103158: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction11103158 },
                        1103159: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction11103159 },
                        1103160: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction11103160 },
                        1103162: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction11103162 },
                        1103165: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction11103165 },
                        1103167: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction11103167 },
                        1103168: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction11103168 },
                        1103169: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction11103169 },
                        1103170: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction11103170 },
                        1103171: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction11103171 },
                        1103172: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction11103172 },
                        1103173: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction11103173 },
                        1103174: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction11103174 } },
                    'MediumStore': (),
                    'HardStore': (),
                    'NormalWeight': {
                        GAMETYPE_DESTROY: 100 },
                    'MediumWeight': { },
                    'HardWeight': { },
                    'ChallengeStore': {
                        (3, 10): None,
                        (3, 9): [
                            (1079, 1),
                            (1030, 1),
                            (1081, 1),
                            (1099, 1),
                            (1080, 1)],
                        (3, 8): [
                            (1078, 1),
                            (1080, 1),
                            (1082, 1),
                            (1105, 1)],
                        (3, 0): [
                            (1003, 1),
                            (1008, 1),
                            (1044, 1),
                            (1055, 1)],
                        (2, 0): [
                            (1003, 1),
                            (1008, 1),
                            (1053, 1)],
                        (1, 0): [
                            (1003, 1),
                            (1004, 1),
                            (1052, 1)] },
                    'SingleChallengeStore': {
                        (3, 10): [],
                        (3, 9): [
                            (1079, 1),
                            (1030, 1),
                            (1081, 1),
                            (1099, 1),
                            (1080, 1)],
                        (3, 8): [
                            (1078, 1),
                            (1080, 1),
                            (1105, 1)],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelRoomChallenge': {
                        (3, 10): [],
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelExcludeChallenge': {
                        (3, 10): {
                            1101602: [],
                            1101603: [],
                            1101604: [],
                            1101111: [],
                            1101204: [],
                            1101205: [],
                            1101206: [],
                            1101207: [],
                            1101208: [],
                            1101233: [],
                            1101234: [],
                            1101251: [],
                            1101252: [],
                            1101215: [],
                            1101606: [],
                            1101703: [],
                            1101702: [],
                            1101216: [],
                            1101225: [],
                            1101226: [],
                            1101227: [],
                            1101228: [],
                            1101230: [],
                            1101235: [],
                            1101706: [],
                            1101238: [],
                            1101229: [],
                            1101237: [],
                            1101231: [],
                            1101239: [],
                            1101236: [],
                            1101240: [],
                            1101704: [],
                            1101241: [] },
                        3: {
                            1101201: [],
                            1101601: [
                                1001,
                                1004,
                                1008,
                                1073],
                            1101602: [],
                            1101603: [],
                            1101604: [],
                            1101605: [
                                1001,
                                1073],
                            1101111: [],
                            1101204: [],
                            1101205: [],
                            1101206: [],
                            1101207: [],
                            1101208: [],
                            1101233: [],
                            1101234: [],
                            1101251: [],
                            1101252: [],
                            1101215: [],
                            1101606: [],
                            1101703: [],
                            1101702: [],
                            1101216: [],
                            1101225: [],
                            1101226: [],
                            1101227: [],
                            1101228: [],
                            1101230: [],
                            1101235: [],
                            1101706: [],
                            1101238: [],
                            1101229: [],
                            1101237: [],
                            1101231: [],
                            1101239: [],
                            1101236: [],
                            1101240: [],
                            1101704: [],
                            1101241: [] },
                        2: {
                            1101201: [],
                            1101601: [],
                            1101602: [],
                            1101603: [],
                            1101604: [],
                            1101605: [],
                            1101111: [],
                            1101204: [],
                            1101205: [],
                            1101206: [],
                            1101207: [],
                            1101208: [],
                            1101251: [],
                            1101252: [],
                            1101215: [],
                            1101606: [],
                            1101703: [],
                            1101216: [],
                            1101225: [],
                            1101226: [],
                            1101227: [],
                            1101228: [],
                            1101230: [],
                            1101235: [],
                            1101706: [],
                            1101238: [],
                            1101229: [],
                            1101237: [],
                            1101231: [],
                            1101239: [],
                            1101236: [],
                            1101240: [],
                            1101704: [],
                            1101241: [] },
                        1: {
                            1101201: [],
                            1101601: [],
                            1101602: [],
                            1101603: [],
                            1101604: [],
                            1101605: [],
                            1101111: [],
                            1101204: [],
                            1101205: [],
                            1101206: [],
                            1101207: [],
                            1101208: [],
                            1101251: [],
                            1101252: [],
                            1101215: [],
                            1101606: [],
                            1101216: [],
                            1101225: [],
                            1101226: [],
                            1101227: [],
                            1101228: [],
                            1101230: [],
                            1101235: [],
                            1101706: [],
                            1101238: [],
                            1101229: [],
                            1101237: [],
                            1101231: [],
                            1101239: [],
                            1101236: [],
                            1101240: [],
                            1101704: [],
                            1101241: [] } },
                    'HideLevel': {
                        1: {
                            1101201: 1,
                            1101601: 1,
                            1101602: 5,
                            1101603: 5,
                            1101604: 5,
                            1101605: 1,
                            1101111: 3,
                            1101204: 3,
                            1101205: 3,
                            1101206: 3,
                            1101207: 3,
                            1101208: 3,
                            1101251: 3,
                            1101252: 3,
                            1101215: 8,
                            1101606: 4,
                            1101216: 3,
                            1101225: 3,
                            1101226: 7,
                            1101227: 3,
                            1101228: 8,
                            1101230: 3,
                            1101235: 7,
                            1101706: 2,
                            1101238: 7,
                            1101229: 3,
                            1101237: 8,
                            1101231: 5,
                            1101239: 1,
                            1101236: 3,
                            1101240: 1,
                            1101704: 2,
                            1101241: 1 },
                        2: {
                            1101201: 1,
                            1101601: 1,
                            1101602: 5,
                            1101603: 5,
                            1101604: 5,
                            1101605: 1,
                            1101111: 3,
                            1101204: 3,
                            1101205: 3,
                            1101206: 3,
                            1101207: 3,
                            1101208: 3,
                            1101251: 3,
                            1101252: 3,
                            1101215: 8,
                            1101606: 4,
                            1101703: 2,
                            1101216: 3,
                            1101225: 3,
                            1101226: 7,
                            1101227: 3,
                            1101228: 8,
                            1101230: 3,
                            1101235: 7,
                            1101706: 2,
                            1101238: 7,
                            1101229: 3,
                            1101237: 8,
                            1101231: 5,
                            1101239: 1,
                            1101236: 3,
                            1101240: 1,
                            1101704: 2,
                            1101241: 1 },
                        3: {
                            1101201: 1,
                            1101601: 1,
                            1101602: 5,
                            1101603: 5,
                            1101604: 5,
                            1101605: 1,
                            1101111: 3,
                            1101204: 3,
                            1101205: 3,
                            1101206: 3,
                            1101207: 3,
                            1101208: 3,
                            1101233: 7,
                            1101234: 7,
                            1101251: 3,
                            1101252: 3,
                            1101215: 8,
                            1101606: 4,
                            1101703: 2,
                            1101702: 2,
                            1101216: 3,
                            1101225: 3,
                            1101226: 7,
                            1101227: 3,
                            1101228: 8,
                            1101230: 3,
                            1101235: 7,
                            1101706: 2,
                            1101238: 7,
                            1101229: 3,
                            1101237: 8,
                            1101231: 5,
                            1101239: 1,
                            1101236: 3,
                            1101240: 1,
                            1101704: 2,
                            1101241: 1 } },
                    'HideLevelStore': {
                        (3, 10): {
                            (1101241, 1, 4, (0, 1000), 1): 10,
                            (1101704, 2, 6, (10, 1000), 1): 0,
                            (1101240, 1, 0, (0, 1000), 1): 10,
                            (1101236, 3, 4, (10, 1000), 1): 10,
                            (1101239, 1, 4, (0, 1000), 1): 10,
                            (1101231, 5, 1, (0, 1000), 1): 10,
                            (1101237, 8, 0, (10, 1000), 1): 10,
                            (1101229, 3, 4, (10, 1000), 1): 10,
                            (1101238, 7, 5, (10, 1000), 1): 10,
                            (1101706, 2, 6, (10, 1000), 1): 10,
                            (1101235, 7, 5, (10, 1000), 1): 10,
                            (1101230, 3, 4, (10, 1000), 1): 10,
                            (1101228, 8, 0, (10, 1000), 1): 10,
                            (1101227, 3, 4, (10, 1000), 1): 10,
                            (1101226, 7, 5, (10, 1000), 1): 10,
                            (1101225, 3, 4, (10, 1000), 1): 10,
                            (1101216, 3, 4, (30, 1000), 0): 10,
                            (1101702, 2, 6, (0, 1000), 0): 10,
                            (1101703, 2, 6, (0, 1000), 0): 10,
                            (1101606, 4, 0, (40, 1000), 0): 0,
                            (1101215, 8, 0, (40, 1000), 0): 10,
                            (1101252, 3, 4, (10, 1000), 0): 10,
                            (1101251, 3, 4, (0, 1000), 0): 10,
                            (1101234, 7, 5, (40, 1000), 0): 10,
                            (1101233, 7, 5, (40, 1000), 0): 10,
                            (1101208, 3, 2, (30, 1000), 0): 10,
                            (1101207, 3, 3, (40, 1000), 0): 10,
                            (1101206, 3, 3, (10, 1000), 0): 10,
                            (1101205, 3, 2, (10, 1000), 0): 10,
                            (1101204, 3, 0, (30, 1000), 0): 10,
                            (1101111, 3, 0, (0, 1000), 0): 10,
                            (1101604, 5, 1, (20, 1000), 0): 2,
                            (1101603, 5, 1, (0, 1000), 0): 4,
                            (1101602, 5, 1, (0, 1000), 0): 4 },
                        3: {
                            (1101241, 1, 4, (0, 1000), 1): 10,
                            (1101704, 2, 6, (10, 1000), 1): 0,
                            (1101240, 1, 0, (0, 1000), 1): 10,
                            (1101236, 3, 4, (10, 1000), 1): 10,
                            (1101239, 1, 4, (0, 1000), 1): 10,
                            (1101231, 5, 1, (0, 1000), 1): 10,
                            (1101237, 8, 0, (10, 1000), 1): 10,
                            (1101229, 3, 4, (10, 1000), 1): 10,
                            (1101238, 7, 5, (10, 1000), 1): 10,
                            (1101706, 2, 6, (10, 1000), 1): 10,
                            (1101235, 7, 5, (10, 1000), 1): 10,
                            (1101230, 3, 4, (10, 1000), 1): 10,
                            (1101228, 8, 0, (10, 1000), 1): 10,
                            (1101227, 3, 4, (10, 1000), 1): 10,
                            (1101226, 7, 5, (10, 1000), 1): 10,
                            (1101225, 3, 4, (10, 1000), 1): 10,
                            (1101216, 3, 4, (30, 1000), 0): 10,
                            (1101702, 2, 6, (0, 1000), 0): 10,
                            (1101703, 2, 6, (0, 1000), 0): 10,
                            (1101606, 4, 0, (40, 1000), 0): 0,
                            (1101215, 8, 0, (40, 1000), 0): 10,
                            (1101252, 3, 4, (10, 1000), 0): 10,
                            (1101251, 3, 4, (0, 1000), 0): 10,
                            (1101234, 7, 5, (40, 1000), 0): 10,
                            (1101233, 7, 5, (40, 1000), 0): 10,
                            (1101208, 3, 2, (30, 1000), 0): 10,
                            (1101207, 3, 3, (40, 1000), 0): 10,
                            (1101206, 3, 3, (10, 1000), 0): 10,
                            (1101205, 3, 2, (10, 1000), 0): 10,
                            (1101204, 3, 0, (30, 1000), 0): 10,
                            (1101111, 3, 0, (0, 1000), 0): 10,
                            (1101605, 1, 0, (40, 1000), 0): 10,
                            (1101604, 5, 1, (20, 1000), 0): 2,
                            (1101603, 5, 1, (0, 1000), 0): 4,
                            (1101602, 5, 1, (0, 1000), 0): 4,
                            (1101601, 1, 0, (0, 1000), 0): 10,
                            (1101201, 1, 0, (0, 1000), 0): 10 },
                        2: {
                            (1101241, 1, 4, (0, 1000), 1): 10,
                            (1101704, 2, 6, (10, 1000), 1): 0,
                            (1101240, 1, 0, (0, 1000), 1): 10,
                            (1101236, 3, 4, (10, 1000), 1): 10,
                            (1101239, 1, 4, (0, 1000), 1): 10,
                            (1101231, 5, 1, (0, 1000), 1): 10,
                            (1101237, 8, 0, (10, 1000), 1): 10,
                            (1101229, 3, 4, (10, 1000), 1): 10,
                            (1101238, 7, 5, (10, 1000), 1): 10,
                            (1101706, 2, 6, (10, 1000), 1): 10,
                            (1101235, 7, 5, (10, 1000), 1): 10,
                            (1101230, 3, 4, (10, 1000), 1): 10,
                            (1101228, 8, 0, (10, 1000), 1): 10,
                            (1101227, 3, 4, (10, 1000), 1): 10,
                            (1101226, 7, 5, (10, 1000), 1): 10,
                            (1101225, 3, 4, (10, 1000), 1): 10,
                            (1101216, 3, 4, (30, 1000), 0): 10,
                            (1101703, 2, 6, (0, 1000), 0): 10,
                            (1101606, 4, 0, (40, 1000), 0): 0,
                            (1101215, 8, 0, (40, 1000), 0): 10,
                            (1101252, 3, 4, (10, 1000), 0): 10,
                            (1101251, 3, 4, (0, 1000), 0): 10,
                            (1101208, 3, 2, (30, 1000), 0): 10,
                            (1101207, 3, 3, (40, 1000), 0): 10,
                            (1101206, 3, 3, (10, 1000), 0): 10,
                            (1101205, 3, 2, (10, 1000), 0): 10,
                            (1101204, 3, 0, (30, 1000), 0): 10,
                            (1101111, 3, 0, (0, 1000), 0): 10,
                            (1101605, 1, 0, (40, 1000), 0): 10,
                            (1101604, 5, 1, (20, 1000), 0): 2,
                            (1101603, 5, 1, (0, 1000), 0): 4,
                            (1101602, 5, 1, (0, 1000), 0): 4,
                            (1101601, 1, 0, (0, 1000), 0): 10,
                            (1101201, 1, 0, (0, 1000), 0): 10 },
                        1: {
                            (1101241, 1, 4, (0, 1000), 1): 10,
                            (1101704, 2, 6, (10, 1000), 1): 0,
                            (1101240, 1, 0, (0, 1000), 1): 10,
                            (1101236, 3, 4, (10, 1000), 1): 10,
                            (1101239, 1, 4, (0, 1000), 1): 10,
                            (1101231, 5, 1, (0, 1000), 1): 10,
                            (1101237, 8, 0, (10, 1000), 1): 10,
                            (1101229, 3, 4, (10, 1000), 1): 10,
                            (1101238, 7, 5, (10, 1000), 1): 10,
                            (1101706, 2, 6, (10, 1000), 1): 10,
                            (1101235, 7, 5, (10, 1000), 1): 10,
                            (1101230, 3, 4, (10, 1000), 1): 10,
                            (1101228, 8, 0, (10, 1000), 1): 10,
                            (1101227, 3, 4, (10, 1000), 1): 10,
                            (1101226, 7, 5, (10, 1000), 1): 10,
                            (1101225, 3, 4, (10, 1000), 1): 10,
                            (1101216, 3, 4, (30, 1000), 0): 10,
                            (1101606, 4, 0, (40, 1000), 0): 0,
                            (1101215, 8, 0, (40, 1000), 0): 10,
                            (1101252, 3, 4, (10, 1000), 0): 10,
                            (1101251, 3, 4, (0, 1000), 0): 10,
                            (1101208, 3, 2, (30, 1000), 0): 10,
                            (1101207, 3, 3, (40, 1000), 0): 10,
                            (1101206, 3, 3, (10, 1000), 0): 10,
                            (1101205, 3, 2, (10, 1000), 0): 10,
                            (1101204, 3, 0, (30, 1000), 0): 10,
                            (1101111, 3, 0, (0, 1000), 0): 10,
                            (1101605, 1, 0, (40, 1000), 0): 10,
                            (1101604, 5, 1, (20, 1000), 0): 2,
                            (1101603, 5, 1, (0, 1000), 0): 4,
                            (1101602, 5, 1, (0, 1000), 0): 4,
                            (1101601, 1, 0, (0, 1000), 0): 10,
                            (1101201, 1, 0, (0, 1000), 0): 10 } },
                    'HideLevelConfMap': {
                        1101606: 1101606,
                        1101616: 1101606,
                        1101626: 1101606,
                        1101636: 1101606 },
                    'HideLevelAllocMap': {
                        1101606: [
                            1101606,
                            1101616,
                            1101626,
                            1101636] },
                    'ExcludeChallengeArea': {
                        (3, 10): [],
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'AIlevelEnhance': 39 },
                4: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (1105101, 1105102, 1105103, 1105104, 1105105, 1105106, 1105107, 1105109, 1105110, 1105114, 1105111, 1105112, 1105113, 1105115, 1105116),
                    'NormalFilter': {
                        1105101: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction11105101 },
                        1105102: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction11105102 },
                        1105103: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction11105103 },
                        1105104: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction11105104 },
                        1105105: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction11105105 },
                        1105106: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction11105106 },
                        1105107: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction11105107 },
                        1105109: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction11105109 },
                        1105110: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction11105110 },
                        1105114: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction11105114 },
                        1105111: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction11105111 },
                        1105112: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction11105112 },
                        1105113: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction11105113 },
                        1105115: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction11105115 },
                        1105116: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction11105116 } },
                    'MediumStore': (),
                    'HardStore': (),
                    'NormalWeight': {
                        GAMETYPE_DESTROY: 100 },
                    'MediumWeight': { },
                    'HardWeight': { },
                    'ChallengeStore': {
                        (3, 10): None,
                        (3, 9): [
                            (1080, 1),
                            (1073, 1),
                            (1079, 1),
                            (1101, 1),
                            (1051, 1)],
                        (3, 8): [
                            (1081, 1),
                            (1073, 1),
                            (1106, 1),
                            (1103, 1),
                            (1101, 1)],
                        (3, 0): [
                            (1008, 1),
                            (1038, 1),
                            (1051, 1),
                            (1056, 1),
                            (1061, 1)],
                        (2, 0): [
                            (1002, 1),
                            (1034, 1),
                            (1051, 1),
                            (1056, 1),
                            (1060, 1)],
                        (1, 0): [
                            (1003, 1),
                            (1054, 1)] },
                    'SingleChallengeStore': {
                        (3, 10): [],
                        (3, 9): [
                            (1080, 1),
                            (1073, 0),
                            (1079, 1),
                            (1051, 1)],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelRoomChallenge': {
                        (3, 10): [],
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelExcludeChallenge': {
                        (3, 10): {
                            1101603: [],
                            1101604: [],
                            1101111: [],
                            1101204: [],
                            1101205: [],
                            1101206: [],
                            1101207: [],
                            1101208: [],
                            1101233: [],
                            1101234: [],
                            1101251: [],
                            1101252: [],
                            1101215: [],
                            1101606: [],
                            1101703: [],
                            1101702: [],
                            1101216: [],
                            1101225: [],
                            1101226: [],
                            1101227: [],
                            1101228: [],
                            1101230: [],
                            1101235: [],
                            1101706: [],
                            1101238: [],
                            1101229: [],
                            1101237: [],
                            1101231: [],
                            1101239: [],
                            1101236: [],
                            1101240: [],
                            1101704: [],
                            1101241: [] },
                        3: {
                            1101603: [],
                            1101604: [],
                            1101605: [
                                1001,
                                1073],
                            1101111: [],
                            1101204: [],
                            1101205: [],
                            1101206: [],
                            1101207: [],
                            1101208: [],
                            1101233: [],
                            1101234: [],
                            1101251: [],
                            1101252: [],
                            1101215: [],
                            1101606: [],
                            1101703: [],
                            1101702: [],
                            1101216: [],
                            1101225: [],
                            1101226: [],
                            1101227: [],
                            1101228: [],
                            1101230: [],
                            1101235: [],
                            1101706: [],
                            1101238: [],
                            1101229: [],
                            1101237: [],
                            1101231: [],
                            1101239: [],
                            1101236: [],
                            1101240: [],
                            1101704: [],
                            1101241: [] },
                        2: {
                            1101201: [],
                            1101603: [],
                            1101604: [],
                            1101605: [],
                            1101111: [],
                            1101204: [],
                            1101205: [],
                            1101206: [],
                            1101207: [],
                            1101208: [],
                            1101233: [],
                            1101234: [],
                            1101251: [],
                            1101252: [],
                            1101215: [],
                            1101606: [],
                            1101703: [],
                            1101216: [],
                            1101225: [],
                            1101226: [],
                            1101227: [],
                            1101228: [],
                            1101230: [],
                            1101235: [],
                            1101706: [],
                            1101238: [],
                            1101229: [],
                            1101237: [],
                            1101231: [],
                            1101239: [],
                            1101236: [],
                            1101240: [],
                            1101704: [],
                            1101241: [] },
                        1: {
                            1101201: [],
                            1101603: [],
                            1101604: [],
                            1101605: [],
                            1101111: [],
                            1101204: [],
                            1101205: [],
                            1101206: [],
                            1101207: [],
                            1101208: [],
                            1101251: [],
                            1101252: [],
                            1101215: [],
                            1101606: [],
                            1101216: [],
                            1101225: [],
                            1101226: [],
                            1101227: [],
                            1101228: [],
                            1101230: [],
                            1101235: [],
                            1101706: [],
                            1101238: [],
                            1101229: [],
                            1101237: [],
                            1101231: [],
                            1101239: [],
                            1101236: [],
                            1101240: [],
                            1101704: [],
                            1101241: [] } },
                    'HideLevel': {
                        1: {
                            1101201: 1,
                            1101603: 5,
                            1101604: 5,
                            1101605: 1,
                            1101111: 3,
                            1101204: 3,
                            1101205: 3,
                            1101206: 3,
                            1101207: 3,
                            1101208: 3,
                            1101251: 3,
                            1101252: 3,
                            1101215: 8,
                            1101606: 4,
                            1101216: 3,
                            1101225: 3,
                            1101226: 7,
                            1101227: 3,
                            1101228: 8,
                            1101230: 3,
                            1101235: 7,
                            1101706: 2,
                            1101238: 7,
                            1101229: 3,
                            1101237: 8,
                            1101231: 5,
                            1101239: 1,
                            1101236: 3,
                            1101240: 1,
                            1101704: 2,
                            1101241: 1 },
                        2: {
                            1101201: 1,
                            1101603: 5,
                            1101604: 5,
                            1101605: 1,
                            1101111: 3,
                            1101204: 3,
                            1101205: 3,
                            1101206: 3,
                            1101207: 3,
                            1101208: 3,
                            1101233: 7,
                            1101234: 7,
                            1101251: 3,
                            1101252: 3,
                            1101215: 8,
                            1101606: 4,
                            1101703: 2,
                            1101216: 3,
                            1101225: 3,
                            1101226: 7,
                            1101227: 3,
                            1101228: 8,
                            1101230: 3,
                            1101235: 7,
                            1101706: 2,
                            1101238: 7,
                            1101229: 3,
                            1101237: 8,
                            1101231: 5,
                            1101239: 1,
                            1101236: 3,
                            1101240: 1,
                            1101704: 2,
                            1101241: 1 },
                        3: {
                            1101603: 5,
                            1101604: 5,
                            1101605: 1,
                            1101111: 3,
                            1101204: 3,
                            1101205: 3,
                            1101206: 3,
                            1101207: 3,
                            1101208: 3,
                            1101233: 7,
                            1101234: 7,
                            1101251: 3,
                            1101252: 3,
                            1101215: 8,
                            1101606: 4,
                            1101703: 2,
                            1101702: 2,
                            1101216: 3,
                            1101225: 3,
                            1101226: 7,
                            1101227: 3,
                            1101228: 8,
                            1101230: 3,
                            1101235: 7,
                            1101706: 2,
                            1101238: 7,
                            1101229: 3,
                            1101237: 8,
                            1101231: 5,
                            1101239: 1,
                            1101236: 3,
                            1101240: 1,
                            1101704: 2,
                            1101241: 1 } },
                    'HideLevelStore': {
                        (3, 10): {
                            (1101241, 1, 4, (0, 1000), 1): 10,
                            (1101704, 2, 6, (10, 1000), 1): 0,
                            (1101240, 1, 0, (0, 1000), 1): 10,
                            (1101236, 3, 4, (10, 1000), 1): 10,
                            (1101239, 1, 4, (0, 1000), 1): 10,
                            (1101231, 5, 1, (0, 1000), 1): 10,
                            (1101237, 8, 0, (10, 1000), 1): 10,
                            (1101229, 3, 4, (10, 1000), 1): 10,
                            (1101238, 7, 5, (10, 1000), 1): 10,
                            (1101706, 2, 6, (10, 1000), 1): 10,
                            (1101235, 7, 5, (10, 1000), 1): 10,
                            (1101230, 3, 4, (10, 1000), 1): 10,
                            (1101228, 8, 0, (10, 1000), 1): 10,
                            (1101227, 3, 4, (10, 1000), 1): 10,
                            (1101226, 7, 5, (10, 1000), 1): 10,
                            (1101225, 3, 4, (10, 1000), 1): 10,
                            (1101216, 3, 4, (30, 1000), 0): 10,
                            (1101702, 2, 6, (0, 1000), 0): 10,
                            (1101703, 2, 6, (0, 1000), 0): 10,
                            (1101606, 4, 0, (40, 1000), 0): 0,
                            (1101215, 8, 0, (40, 1000), 0): 10,
                            (1101252, 3, 4, (10, 1000), 0): 10,
                            (1101251, 3, 4, (0, 1000), 0): 10,
                            (1101234, 7, 5, (40, 1000), 0): 10,
                            (1101233, 7, 5, (40, 1000), 0): 10,
                            (1101208, 3, 2, (30, 1000), 0): 10,
                            (1101207, 3, 3, (40, 1000), 0): 10,
                            (1101206, 3, 3, (10, 1000), 0): 10,
                            (1101205, 3, 2, (10, 1000), 0): 10,
                            (1101204, 3, 0, (30, 1000), 0): 10,
                            (1101111, 3, 0, (0, 1000), 0): 10,
                            (1101604, 5, 1, (20, 1000), 0): 6,
                            (1101603, 5, 1, (0, 1000), 0): 4 },
                        3: {
                            (1101241, 1, 4, (0, 1000), 1): 10,
                            (1101704, 2, 6, (10, 1000), 1): 0,
                            (1101240, 1, 0, (0, 1000), 1): 10,
                            (1101236, 3, 4, (10, 1000), 1): 10,
                            (1101239, 1, 4, (0, 1000), 1): 10,
                            (1101231, 5, 1, (0, 1000), 1): 10,
                            (1101237, 8, 0, (10, 1000), 1): 10,
                            (1101229, 3, 4, (10, 1000), 1): 10,
                            (1101238, 7, 5, (10, 1000), 1): 10,
                            (1101706, 2, 6, (10, 1000), 1): 10,
                            (1101235, 7, 5, (10, 1000), 1): 10,
                            (1101230, 3, 4, (10, 1000), 1): 10,
                            (1101228, 8, 0, (10, 1000), 1): 10,
                            (1101227, 3, 4, (10, 1000), 1): 10,
                            (1101226, 7, 5, (10, 1000), 1): 10,
                            (1101225, 3, 4, (10, 1000), 1): 10,
                            (1101216, 3, 4, (30, 1000), 0): 10,
                            (1101702, 2, 6, (0, 1000), 0): 10,
                            (1101703, 2, 6, (0, 1000), 0): 10,
                            (1101606, 4, 0, (40, 1000), 0): 0,
                            (1101215, 8, 0, (40, 1000), 0): 10,
                            (1101252, 3, 4, (10, 1000), 0): 10,
                            (1101251, 3, 4, (0, 1000), 0): 10,
                            (1101234, 7, 5, (40, 1000), 0): 10,
                            (1101233, 7, 5, (40, 1000), 0): 10,
                            (1101208, 3, 2, (30, 1000), 0): 10,
                            (1101207, 3, 3, (40, 1000), 0): 10,
                            (1101206, 3, 3, (10, 1000), 0): 10,
                            (1101205, 3, 2, (10, 1000), 0): 10,
                            (1101204, 3, 0, (30, 1000), 0): 10,
                            (1101111, 3, 0, (0, 1000), 0): 10,
                            (1101605, 1, 0, (40, 1000), 0): 10,
                            (1101604, 5, 1, (20, 1000), 0): 6,
                            (1101603, 5, 1, (0, 1000), 0): 4 },
                        2: {
                            (1101241, 1, 4, (0, 1000), 1): 10,
                            (1101704, 2, 6, (10, 1000), 1): 0,
                            (1101240, 1, 0, (0, 1000), 1): 10,
                            (1101236, 3, 4, (10, 1000), 1): 10,
                            (1101239, 1, 4, (0, 1000), 1): 10,
                            (1101231, 5, 1, (0, 1000), 1): 10,
                            (1101237, 8, 0, (10, 1000), 1): 10,
                            (1101229, 3, 4, (10, 1000), 1): 10,
                            (1101238, 7, 5, (10, 1000), 1): 10,
                            (1101706, 2, 6, (10, 1000), 1): 10,
                            (1101235, 7, 5, (10, 1000), 1): 10,
                            (1101230, 3, 4, (10, 1000), 1): 10,
                            (1101228, 8, 0, (10, 1000), 1): 10,
                            (1101227, 3, 4, (10, 1000), 1): 10,
                            (1101226, 7, 5, (10, 1000), 1): 10,
                            (1101225, 3, 4, (10, 1000), 1): 10,
                            (1101216, 3, 4, (30, 1000), 0): 10,
                            (1101703, 2, 6, (0, 1000), 0): 10,
                            (1101606, 4, 0, (40, 1000), 0): 0,
                            (1101215, 8, 0, (40, 1000), 0): 10,
                            (1101252, 3, 4, (10, 1000), 0): 10,
                            (1101251, 3, 4, (0, 1000), 0): 10,
                            (1101234, 7, 0, (40, 1000), 0): 10,
                            (1101233, 7, 0, (40, 1000), 0): 10,
                            (1101208, 3, 2, (30, 1000), 0): 10,
                            (1101207, 3, 3, (40, 1000), 0): 10,
                            (1101206, 3, 3, (10, 1000), 0): 10,
                            (1101205, 3, 2, (10, 1000), 0): 10,
                            (1101204, 3, 0, (30, 1000), 0): 10,
                            (1101111, 3, 0, (0, 1000), 0): 10,
                            (1101605, 1, 0, (40, 1000), 0): 10,
                            (1101604, 5, 1, (20, 1000), 0): 6,
                            (1101603, 5, 1, (0, 1000), 0): 4,
                            (1101201, 1, 0, (0, 1000), 0): 10 },
                        1: {
                            (1101241, 1, 4, (0, 1000), 1): 10,
                            (1101704, 2, 6, (10, 1000), 1): 0,
                            (1101240, 1, 0, (0, 1000), 1): 10,
                            (1101236, 3, 4, (10, 1000), 1): 10,
                            (1101239, 1, 4, (0, 1000), 1): 10,
                            (1101231, 5, 1, (0, 1000), 1): 10,
                            (1101237, 8, 0, (10, 1000), 1): 10,
                            (1101229, 3, 4, (10, 1000), 1): 10,
                            (1101238, 7, 5, (10, 1000), 1): 10,
                            (1101706, 2, 6, (10, 1000), 1): 10,
                            (1101235, 7, 5, (10, 1000), 1): 10,
                            (1101230, 3, 4, (10, 1000), 1): 10,
                            (1101228, 8, 0, (10, 1000), 1): 10,
                            (1101227, 3, 4, (10, 1000), 1): 10,
                            (1101226, 7, 5, (10, 1000), 1): 10,
                            (1101225, 3, 4, (10, 1000), 1): 10,
                            (1101216, 3, 4, (30, 1000), 0): 10,
                            (1101606, 4, 0, (40, 1000), 0): 0,
                            (1101215, 8, 0, (40, 1000), 0): 10,
                            (1101252, 3, 4, (10, 1000), 0): 10,
                            (1101251, 3, 4, (0, 1000), 0): 10,
                            (1101208, 3, 2, (30, 1000), 0): 10,
                            (1101207, 3, 3, (40, 1000), 0): 10,
                            (1101206, 3, 3, (10, 1000), 0): 10,
                            (1101205, 3, 2, (10, 1000), 0): 10,
                            (1101204, 3, 0, (30, 1000), 0): 10,
                            (1101111, 3, 0, (0, 1000), 0): 10,
                            (1101605, 1, 0, (40, 1000), 0): 10,
                            (1101604, 5, 1, (20, 1000), 0): 6,
                            (1101603, 5, 1, (0, 1000), 0): 4,
                            (1101201, 1, 0, (0, 1000), 0): 10 } },
                    'HideLevelConfMap': {
                        1101606: 1101606,
                        1101616: 1101606,
                        1101626: 1101606,
                        1101636: 1101606 },
                    'HideLevelAllocMap': {
                        1101606: [
                            1101606,
                            1101616,
                            1101626,
                            1101636] },
                    'ExcludeChallengeArea': {
                        (3, 10): [],
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'AIlevelEnhance': 42 } },
            'LayerChoose': {
                1: {
                    LAYER_CHOOSE_CRAFTSMAN: (1, 0, 0, 99, {
                        1: 0,
                        2: 5,
                        3: 30,
                        4: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_SHOP: (1, 1, 1, 99, {
                        1: 0,
                        2: 5,
                        3: 30,
                        4: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_EVENTNPC: (2, 0, 1, 99, {
                        1: 0,
                        2: 15,
                        3: 25,
                        4: 20 }, {
                        1: 0,
                        2: 1,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_CHALLENGE: (1, 0, 0, 99, {
                        1: 0,
                        2: 0,
                        3: 20,
                        4: 80 }, { }),
                    LAYER_CHOOSE_HIDE: (4, 1, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 30,
                        4: 20 }, {
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1 }) },
                2: {
                    LAYER_CHOOSE_CRAFTSMAN: (1, 0, 0, 99, {
                        1: 0,
                        2: 5,
                        3: 30,
                        4: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_SHOP: (1, 1, 1, 99, {
                        1: 0,
                        2: 5,
                        3: 30,
                        4: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_EVENTNPC: (2, 0, 1, 99, {
                        1: 0,
                        2: 15,
                        3: 25,
                        4: 20 }, {
                        1: 0,
                        2: 1,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_CHALLENGE: (1, 0, 0, 99, {
                        1: 15,
                        2: 20,
                        3: 25,
                        4: 40 }, { }),
                    LAYER_CHOOSE_HIDE: (4, 1, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 30,
                        4: 20 }, {
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1 }) },
                3: {
                    LAYER_CHOOSE_S8SHOP: (4, 0, 4, 4, {
                        1: 10,
                        2: 10,
                        3: 10,
                        4: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_S7SHOP: (2, 0, 2, 2, {
                        1: 0,
                        2: 0,
                        3: 10,
                        4: 0 }, {
                        1: 0,
                        2: 0,
                        3: 1,
                        4: 0 }),
                    LAYER_CHOOSE_DICESHOP: (2, 0, 2, 2, {
                        1: 0,
                        2: 10,
                        3: 0,
                        4: 10 }, {
                        1: 0,
                        2: 1,
                        3: 0,
                        4: 1 }),
                    LAYER_CHOOSE_WANDSHOP: (1, 0, 1, 1, {
                        1: 0,
                        2: 0,
                        3: 10,
                        4: 0 }, {
                        1: 0,
                        2: 0,
                        3: 1,
                        4: 0 }),
                    LAYER_CHOOSE_REGROUPRELIC: (1, 0, 1, 1, {
                        1: 0,
                        2: 0,
                        3: 10,
                        4: 0 }, {
                        1: 0,
                        2: 0,
                        3: 1,
                        4: 0 }),
                    LAYER_CHOOSE_RELICLOTTERY: (1, 0, 1, 1, {
                        1: 0,
                        2: 0,
                        3: 0,
                        4: 10 }, {
                        1: 0,
                        2: 0,
                        3: 0,
                        4: 1 }),
                    LAYER_CHOOSE_PETSHOP: (1, 0, 1, 1, {
                        1: 0,
                        2: 0,
                        3: 0,
                        4: 10 }, {
                        1: 0,
                        2: 0,
                        3: 0,
                        4: 1 }),
                    LAYER_CHOOSE_TASKNPC: (1, 0, 1, 1, {
                        1: 0,
                        2: 0,
                        3: 8,
                        4: 10 }, {
                        1: 0,
                        2: 0,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_GSCASHSHOP: (1, 1, 1, 99, {
                        1: 0,
                        2: 5,
                        3: 30,
                        4: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_CRAFTSMAN: (1, 0, 0, 99, {
                        1: 0,
                        2: 5,
                        3: 30,
                        4: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_SHOP: (1, 1, 1, 99, {
                        1: 0,
                        2: 5,
                        3: 30,
                        4: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_EVENTNPC: (2, 0, 1, 99, {
                        1: 0,
                        2: 15,
                        3: 25,
                        4: 20 }, {
                        1: 0,
                        2: 1,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_CHALLENGE: ((lambda *a: 1 + (Func221(*a) // 8) * 3), 0, 1, 99, {
                        1: 25,
                        2: 25,
                        3: 25,
                        4: 25 }, { }),
                    LAYER_CHOOSE_HIDE: (4, 1, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 30,
                        4: 20 }, {
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1 }) } },
            'BaseGrade': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: (2, 0),
                        2: (5, 0),
                        3: (7, 0),
                        4: (9, 0) },
                    LEVEL_TYPE_FIGHT: {
                        1: (1, 0),
                        2: (3, 0),
                        3: (5, 0),
                        4: (7, 0) },
                    LEVEL_TYPE_BOSS: (10, 0),
                    LEVEL_TYPE_HALL: (0, 0) },
                10: {
                    LEVEL_TYPE_HIDE: {
                        1: (1, 0),
                        2: (3, 0),
                        3: (5, 0),
                        4: (7, 0) },
                    LEVEL_TYPE_FIGHT: {
                        1: (1, 0),
                        2: (3, 0),
                        3: (5, 0),
                        4: (7, 0) },
                    LEVEL_TYPE_BOSS: (10, 0),
                    LEVEL_TYPE_HALL: (0, 0) } },
            'MonsterAttAdjust': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                        4: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                        4: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func209(*a) - 1) * 20000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 20000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 20000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                        ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0),
                        ('MoveSpeed', (lambda *a: (Func209(*a) - 1) * 500 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                        ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)] },
                10: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                        4: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                        4: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func209(*a) - 1) * 20000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 20000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 20000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                        ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0),
                        ('MoveSpeed', (lambda *a: (Func209(*a) - 1) * 500 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                        ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)] } },
            'EliteAttAdjust': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                        4: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                        4: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                        ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                        ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)] },
                10: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                        4: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                        4: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func209(*a) - 1) * 11000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 11000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 11000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                        ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func209(*a) - 1) * 11000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 11000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 11000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                        ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)] } },
            'ItemChoose': 1001 },
        2: {
            'CtrlSize': 3,
            'HallInfo': 1100004,
            'BossInfo': {
                'BossStore': {
                    1202001: 10,
                    1202003: 10 },
                'BossExtra': {
                    1202001: (None, None),
                    1202003: (ChooseAction21202003, ForceAction21202003) },
                'ChallengeStore': {
                    (3, 9): [
                        (1080, 1),
                        (1105, 1),
                        (1103, 1),
                        (1102, 1),
                        (1119, 1),
                        (1120, 1),
                        (1121, 1)],
                    (3, 8): [
                        (1077, 0),
                        (1080, 1),
                        (1099, 1),
                        (1102, 1)] },
                'SingleChallengeStore': {
                    (3, 9): [
                        (1080, 1),
                        (1105, 1),
                        (1103, 1),
                        (1102, 1),
                        (1120, 1),
                        (1121, 1)],
                    (3, 8): [] },
                'ExcludeChallengeArea': {
                    (3, 9): [],
                    (3, 8): [] },
                'UnSpawnRuleInfo': {
                    1202001: [],
                    1202003: [] },
                'ChallengeModeLimit': {
                    (3, 9, 0): {
                        'MULTI': [],
                        'SINGLE': [] },
                    (3, 8, 0): {
                        'MULTI': [],
                        'SINGLE': [] } },
                'AIBosslevelEnhance': {
                    1202001: 50,
                    1202003: 50 } },
            'NpcInfo': {
                'shop': {
                    1005: 10 },
                'craftsman': {
                    1018: 10 },
                'gscashshop': {
                    1054: 10 },
                'tasknpc': {
                    1065: 10 },
                'petshop': {
                    1068: 10 },
                'reliclottery': {
                    1071: 10 },
                'wandshop': {
                    1072: 10 },
                'diceshop': {
                    1073: 10 },
                's7shop': {
                    1074: 10 },
                's8shop': {
                    1075: 10 } },
            'CtrlInfo': {
                1: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (1202108, 1202109, 1202110, 1202111, 1202112, 1202113, 1202114, 1202115, 1202116, 1202117, 1202118, 1202119),
                    'NormalFilter': {
                        1202108: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1202109: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1202110: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1202111: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1202112: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1202113: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1202114: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1202115: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1202116: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1202117: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1202118: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1202119: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None } },
                    'MediumStore': (),
                    'HardStore': (),
                    'NormalWeight': {
                        GAMETYPE_DESTROY: 100 },
                    'MediumWeight': { },
                    'HardWeight': { },
                    'ChallengeStore': {
                        (3, 10): None,
                        (3, 9): [
                            (1051, 1),
                            (1125, 1),
                            (1124, 1),
                            (1100, 1),
                            (1129, 1),
                            (1030, 1),
                            (1099, 1)],
                        (3, 8): [
                            (1077, 0),
                            (1082, 1),
                            (1104, 1),
                            (1105, 1),
                            (1078, 1)],
                        (3, 0): [
                            (1040, 1),
                            (1045, 1)],
                        (2, 0): [
                            (1007, 1),
                            (1015, 1)],
                        (1, 0): [
                            (1009, 1),
                            (1053, 1),
                            (1007, 1)] },
                    'SingleChallengeStore': {
                        (3, 10): [],
                        (3, 9): [
                            (1051, 1),
                            (1099, 1),
                            (1124, 1),
                            (1100, 1),
                            (1030, 1),
                            (1125, 1)],
                        (3, 8): [
                            (1077, 0),
                            (1082, 1),
                            (1105, 1),
                            (1078, 1)],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelRoomChallenge': {
                        (3, 10): [],
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelExcludeChallenge': {
                        (3, 10): {
                            1201112: [
                                1129],
                            1201114: [
                                1129],
                            1201603: [],
                            1201904: [],
                            1201902: [],
                            1201115: [
                                1129],
                            1201116: [
                                1129],
                            1201117: [
                                1129],
                            1204103: [
                                1129],
                            1201604: [],
                            1201213: [] },
                        3: {
                            1201112: [
                                1129],
                            1201114: [
                                1129],
                            1201603: [],
                            1201904: [],
                            1201902: [],
                            1201115: [
                                1129],
                            1201116: [
                                1129],
                            1201117: [
                                1129],
                            1204103: [
                                1129],
                            1201202: [],
                            1201604: [],
                            1201203: [],
                            1201213: [] },
                        2: {
                            1201112: [],
                            1201114: [],
                            1201603: [],
                            1201904: [],
                            1201902: [],
                            1201115: [],
                            1201116: [],
                            1201117: [],
                            1204103: [],
                            1201202: [],
                            1201604: [],
                            1201203: [],
                            1201213: [] },
                        1: {
                            1201112: [],
                            1201114: [],
                            1201603: [],
                            1201115: [],
                            1201116: [],
                            1201117: [],
                            1204103: [],
                            1201202: [],
                            1201203: [],
                            1201213: [] } },
                    'HideLevel': {
                        1: {
                            1201112: 3,
                            1201114: 3,
                            1201603: 5,
                            1201115: 3,
                            1201116: 3,
                            1201117: 3,
                            1204103: 3,
                            1201202: 1,
                            1201203: 1,
                            1201213: 3 },
                        2: {
                            1201112: 3,
                            1201114: 3,
                            1201603: 5,
                            1201904: 6,
                            1201902: 6,
                            1201115: 3,
                            1201116: 3,
                            1201117: 3,
                            1204103: 3,
                            1201202: 1,
                            1201604: 5,
                            1201203: 1,
                            1201213: 3 },
                        3: {
                            1201112: 3,
                            1201114: 3,
                            1201603: 5,
                            1201904: 6,
                            1201902: 6,
                            1201115: 3,
                            1201116: 3,
                            1201117: 3,
                            1204103: 3,
                            1201202: 1,
                            1201604: 5,
                            1201203: 1,
                            1201213: 3 } },
                    'HideLevelStore': {
                        (3, 10): {
                            (1201213, 3, 1, (20, 1000), -1): 10,
                            (1201604, 5, 2, (10, 1000), -1): 10,
                            (1204103, 3, 0, (40, 1000), -1): 10,
                            (1201117, 3, 0, (20, 1000), -1): 10,
                            (1201116, 3, 1, (20, 1000), -1): 10,
                            (1201115, 3, 1, (0, 1000), -1): 10,
                            (1201902, 6, 0, (20, 1000), -1): 10,
                            (1201904, 6, 0, (20, 1000), -1): 10,
                            (1201603, 5, 2, (10, 1000), -1): 10,
                            (1201114, 3, 0, (0, 1000), -1): 10,
                            (1201112, 3, 0, (0, 1000), -1): 10 },
                        3: {
                            (1201213, 3, 1, (20, 1000), -1): 10,
                            (1201203, 1, 0, (0, 1000), -1): 10,
                            (1201604, 5, 2, (10, 1000), -1): 10,
                            (1201202, 1, 0, (0, 1000), -1): 10,
                            (1204103, 3, 0, (40, 1000), -1): 10,
                            (1201117, 3, 0, (20, 1000), -1): 10,
                            (1201116, 3, 1, (20, 1000), -1): 10,
                            (1201115, 3, 1, (0, 1000), -1): 10,
                            (1201902, 6, 0, (20, 1000), -1): 10,
                            (1201904, 6, 0, (20, 1000), -1): 10,
                            (1201603, 5, 2, (10, 1000), -1): 10,
                            (1201114, 3, 0, (0, 1000), -1): 10,
                            (1201112, 3, 0, (0, 1000), -1): 10 },
                        2: {
                            (1201213, 3, 1, (20, 1000), -1): 10,
                            (1201203, 1, 0, (0, 1000), -1): 10,
                            (1201604, 5, 2, (10, 1000), -1): 10,
                            (1201202, 1, 0, (0, 1000), -1): 10,
                            (1204103, 3, 0, (40, 1000), -1): 10,
                            (1201117, 3, 0, (20, 1000), -1): 10,
                            (1201116, 3, 1, (20, 1000), -1): 10,
                            (1201115, 3, 1, (0, 1000), -1): 10,
                            (1201902, 6, 0, (20, 1000), -1): 10,
                            (1201904, 6, 0, (20, 1000), -1): 10,
                            (1201603, 5, 2, (10, 1000), -1): 10,
                            (1201114, 3, 0, (0, 1000), -1): 10,
                            (1201112, 3, 0, (0, 1000), -1): 10 },
                        1: {
                            (1201213, 3, 1, (20, 1000), -1): 10,
                            (1201203, 1, 0, (0, 1000), -1): 10,
                            (1201202, 1, 0, (0, 1000), -1): 10,
                            (1204103, 3, 0, (40, 1000), -1): 10,
                            (1201117, 3, 0, (20, 1000), -1): 10,
                            (1201116, 3, 1, (20, 1000), -1): 10,
                            (1201115, 3, 1, (0, 1000), -1): 10,
                            (1201603, 5, 0, (10, 1000), -1): 10,
                            (1201114, 3, 0, (0, 1000), -1): 10,
                            (1201112, 3, 0, (0, 1000), -1): 10 } },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': {
                        (3, 10): [],
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'AIlevelEnhance': 47 },
                2: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (1203141, 1203142, 1203143, 1203145, 1203146, 1203144, 1203147, 1203148, 1203149, 1203150, 1203151, 1203152, 1203153, 1203154, 1203155, 1203156, 1203157),
                    'NormalFilter': {
                        1203141: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21203141 },
                        1203142: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21203142 },
                        1203143: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21203143 },
                        1203145: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21203145 },
                        1203146: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21203146 },
                        1203144: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21203144 },
                        1203147: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21203147 },
                        1203148: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21203148 },
                        1203149: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21203149 },
                        1203150: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21203150 },
                        1203151: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21203151 },
                        1203152: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21203152 },
                        1203153: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21203153 },
                        1203154: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21203154 },
                        1203155: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21203155 },
                        1203156: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21203156 },
                        1203157: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21203157 } },
                    'MediumStore': (),
                    'HardStore': (),
                    'NormalWeight': {
                        GAMETYPE_DESTROY: 100 },
                    'MediumWeight': { },
                    'HardWeight': { },
                    'ChallengeStore': {
                        (3, 10): None,
                        (3, 9): [
                            (1130, 1),
                            (1080, 1),
                            (1125, 1),
                            (1126, 1),
                            (1128, 1),
                            (1122, 0),
                            (1084, 1),
                            (1140, 1),
                            (1142, 1),
                            (1143, 1)],
                        (3, 8): [
                            (1051, 1),
                            (1106, 1),
                            (1083, 1),
                            (1100, 1),
                            (1101, 1),
                            (1140, 1)],
                        (3, 0): [
                            (1005, 1),
                            (1039, 1),
                            (1052, 1),
                            (1057, 1),
                            (1066, 1),
                            (1141, 1),
                            (1142, 1),
                            (1143, 1)],
                        (2, 0): [
                            (1005, 1),
                            (1011, 1),
                            (1035, 1),
                            (1052, 1),
                            (1057, 1),
                            (1065, 1),
                            (1141, 1)],
                        (1, 0): [
                            (1009, 1),
                            (1015, 1),
                            (1141, 1)] },
                    'SingleChallengeStore': {
                        (3, 10): [],
                        (3, 9): [
                            (1130, 1),
                            (1080, 1),
                            (1125, 1),
                            (1126, 1),
                            (1122, 0),
                            (1084, 1),
                            (1140, 1),
                            (1142, 1)],
                        (3, 8): [
                            (1051, 1),
                            (1106, 1),
                            (1083, 1),
                            (1100, 1),
                            (1140, 1)],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelRoomChallenge': {
                        (3, 10): [],
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelExcludeChallenge': {
                        (3, 10): {
                            1201112: [
                                1129,
                                1143],
                            1201114: [
                                1129,
                                1143],
                            1201603: [],
                            1201904: [],
                            1201902: [],
                            1201115: [
                                1129,
                                1143],
                            1201116: [
                                1129,
                                1143],
                            1201117: [
                                1129,
                                1143],
                            1204103: [
                                1129,
                                1143],
                            1201604: [],
                            1201703: [],
                            1201701: [],
                            1201220: [],
                            1201213: [
                                1143],
                            1201906: [],
                            1201223: [
                                1143],
                            1201226: [
                                1143],
                            1201705: [] },
                        3: {
                            1201112: [
                                1129,
                                1143],
                            1201114: [
                                1129,
                                1143],
                            1201603: [],
                            1201904: [],
                            1201902: [],
                            1201115: [
                                1129,
                                1143],
                            1201116: [
                                1129,
                                1143],
                            1201117: [
                                1129,
                                1143],
                            1204103: [
                                1129,
                                1143],
                            1201202: [],
                            1201604: [],
                            1201203: [],
                            1201703: [],
                            1201701: [],
                            1201220: [],
                            1201213: [
                                1143],
                            1201906: [],
                            1201223: [
                                1143],
                            1201225: [
                                1143],
                            1201226: [
                                1143],
                            1201227: [
                                1143],
                            1201224: [
                                1143],
                            1201705: [] },
                        2: {
                            1201112: [],
                            1201114: [],
                            1201603: [],
                            1201904: [],
                            1201902: [],
                            1201115: [],
                            1201116: [],
                            1201117: [],
                            1204103: [],
                            1201202: [],
                            1201604: [],
                            1201203: [],
                            1201703: [],
                            1201220: [],
                            1201213: [],
                            1201906: [],
                            1201223: [],
                            1201225: [],
                            1201226: [],
                            1201227: [],
                            1201224: [],
                            1201705: [] },
                        1: {
                            1201112: [],
                            1201114: [],
                            1201603: [],
                            1201115: [],
                            1201116: [],
                            1201117: [],
                            1204103: [],
                            1201202: [],
                            1201203: [],
                            1201220: [],
                            1201213: [],
                            1201223: [],
                            1201225: [],
                            1201226: [],
                            1201227: [],
                            1201224: [] } },
                    'HideLevel': {
                        1: {
                            1201112: 3,
                            1201114: 3,
                            1201603: 5,
                            1201115: 3,
                            1201116: 3,
                            1201117: 3,
                            1204103: 3,
                            1201202: 1,
                            1201203: 1,
                            1201220: 8,
                            1201213: 3,
                            1201223: 3,
                            1201225: 1,
                            1201226: 3,
                            1201227: 1,
                            1201224: 1 },
                        2: {
                            1201112: 3,
                            1201114: 3,
                            1201603: 5,
                            1201904: 6,
                            1201902: 6,
                            1201115: 3,
                            1201116: 3,
                            1201117: 3,
                            1204103: 3,
                            1201202: 1,
                            1201604: 5,
                            1201203: 1,
                            1201703: 2,
                            1201220: 8,
                            1201213: 3,
                            1201906: 6,
                            1201223: 3,
                            1201225: 1,
                            1201226: 3,
                            1201227: 1,
                            1201224: 1,
                            1201705: 2 },
                        3: {
                            1201112: 3,
                            1201114: 3,
                            1201603: 5,
                            1201904: 6,
                            1201902: 6,
                            1201115: 3,
                            1201116: 3,
                            1201117: 3,
                            1204103: 3,
                            1201202: 1,
                            1201604: 5,
                            1201203: 1,
                            1201703: 2,
                            1201701: 2,
                            1201220: 8,
                            1201213: 3,
                            1201906: 6,
                            1201223: 3,
                            1201225: 1,
                            1201226: 3,
                            1201227: 1,
                            1201224: 1,
                            1201705: 2 } },
                    'HideLevelStore': {
                        (3, 10): {
                            (1201705, 2, 0, (0, 1000), 1): 10,
                            (1201226, 3, 1, (0, 1000), 1): 10,
                            (1201223, 3, 1, (20, 1000), 1): 10,
                            (1201906, 6, 0, (40, 1000), 1): 10,
                            (1201213, 3, 1, (20, 1000), 0): 10,
                            (1201220, 8, 0, (40, 1000), 0): 10,
                            (1201701, 2, 6, (0, 1000), 0): 10,
                            (1201703, 2, 6, (0, 1000), 0): 10,
                            (1201604, 5, 2, (10, 1000), 0): 10,
                            (1204103, 3, 0, (40, 1000), 0): 10,
                            (1201117, 3, 0, (20, 1000), 0): 10,
                            (1201116, 3, 1, (20, 1000), 0): 10,
                            (1201115, 3, 1, (0, 1000), 0): 10,
                            (1201902, 6, 0, (20, 1000), 0): 0,
                            (1201904, 6, 0, (20, 1000), 0): 0,
                            (1201603, 5, 2, (10, 1000), 0): 10,
                            (1201114, 3, 0, (0, 1000), 0): 10,
                            (1201112, 3, 0, (0, 1000), 0): 10 },
                        3: {
                            (1201705, 2, 0, (0, 1000), 1): 10,
                            (1201224, 1, 0, (0, 1000), 1): 10,
                            (1201227, 1, 0, (0, 1000), 1): 10,
                            (1201226, 3, 1, (0, 1000), 1): 10,
                            (1201225, 1, 0, (0, 1000), 1): 10,
                            (1201223, 3, 1, (20, 1000), 1): 10,
                            (1201906, 6, 0, (40, 1000), 1): 10,
                            (1201213, 3, 1, (20, 1000), 0): 10,
                            (1201220, 8, 0, (40, 1000), 0): 10,
                            (1201701, 2, 6, (0, 1000), 0): 10,
                            (1201703, 2, 6, (0, 1000), 0): 10,
                            (1201203, 1, 0, (0, 1000), 0): 10,
                            (1201604, 5, 2, (10, 1000), 0): 10,
                            (1201202, 1, 0, (0, 1000), 0): 10,
                            (1204103, 3, 0, (40, 1000), 0): 10,
                            (1201117, 3, 0, (20, 1000), 0): 10,
                            (1201116, 3, 1, (20, 1000), 0): 10,
                            (1201115, 3, 1, (0, 1000), 0): 10,
                            (1201902, 6, 0, (20, 1000), 0): 0,
                            (1201904, 6, 0, (20, 1000), 0): 0,
                            (1201603, 5, 2, (10, 1000), 0): 10,
                            (1201114, 3, 0, (0, 1000), 0): 10,
                            (1201112, 3, 0, (0, 1000), 0): 10 },
                        2: {
                            (1201705, 2, 0, (0, 1000), 1): 10,
                            (1201224, 1, 0, (0, 1000), 1): 10,
                            (1201227, 1, 0, (0, 1000), 1): 10,
                            (1201226, 3, 1, (0, 1000), 1): 10,
                            (1201225, 1, 0, (0, 1000), 1): 10,
                            (1201223, 3, 1, (20, 1000), 1): 10,
                            (1201906, 6, 0, (40, 1000), 1): 10,
                            (1201213, 3, 1, (20, 1000), 0): 10,
                            (1201220, 8, 0, (40, 1000), 0): 10,
                            (1201703, 2, 6, (0, 1000), 0): 10,
                            (1201203, 1, 0, (0, 1000), 0): 10,
                            (1201604, 5, 2, (10, 1000), 0): 10,
                            (1201202, 1, 0, (0, 1000), 0): 10,
                            (1204103, 3, 0, (40, 1000), 0): 10,
                            (1201117, 3, 0, (20, 1000), 0): 10,
                            (1201116, 3, 1, (20, 1000), 0): 10,
                            (1201115, 3, 1, (0, 1000), 0): 10,
                            (1201902, 6, 0, (20, 1000), 0): 10,
                            (1201904, 6, 0, (20, 1000), 0): 10,
                            (1201603, 5, 2, (10, 1000), 0): 10,
                            (1201114, 3, 0, (0, 1000), 0): 10,
                            (1201112, 3, 0, (0, 1000), 0): 10 },
                        1: {
                            (1201224, 1, 0, (0, 1000), 1): 10,
                            (1201227, 1, 0, (0, 1000), 1): 10,
                            (1201226, 3, 1, (0, 1000), 1): 10,
                            (1201225, 1, 0, (0, 1000), 1): 10,
                            (1201223, 3, 1, (20, 1000), 1): 10,
                            (1201213, 3, 1, (20, 1000), 0): 10,
                            (1201220, 8, 0, (40, 1000), 0): 10,
                            (1201203, 1, 0, (0, 1000), 0): 10,
                            (1201202, 1, 0, (0, 1000), 0): 10,
                            (1204103, 3, 0, (40, 1000), 0): 10,
                            (1201117, 3, 0, (20, 1000), 0): 10,
                            (1201116, 3, 1, (20, 1000), 0): 10,
                            (1201115, 3, 1, (0, 1000), 0): 10,
                            (1201603, 5, 0, (10, 1000), 0): 10,
                            (1201114, 3, 0, (0, 1000), 0): 10,
                            (1201112, 3, 0, (0, 1000), 0): 10 } },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': {
                        (3, 10): [],
                        (3, 9): [
                            (1120404, 9),
                            (1120108, 6)],
                        (3, 8): [
                            (1120404, 9),
                            (1120108, 6)],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'AIlevelEnhance': 49 },
                3: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (1205101, 1205102, 1205103, 1205104, 1205105, 1205106, 1205107, 1205108, 1205109, 1205110, 1205111, 1205112, 1205113, 1205114, 1205115, 1205116, 1205117, 1205118, 1205119),
                    'NormalFilter': {
                        1205101: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21205101 },
                        1205102: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21205102 },
                        1205103: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21205103 },
                        1205104: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21205104 },
                        1205105: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21205105 },
                        1205106: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21205106 },
                        1205107: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21205107 },
                        1205108: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21205108 },
                        1205109: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21205109 },
                        1205110: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21205110 },
                        1205111: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21205111 },
                        1205112: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21205112 },
                        1205113: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21205113 },
                        1205114: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21205114 },
                        1205115: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21205115 },
                        1205116: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21205116 },
                        1205117: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21205117 },
                        1205118: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21205118 },
                        1205119: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction21205119 } },
                    'MediumStore': (),
                    'HardStore': (),
                    'NormalWeight': {
                        GAMETYPE_DESTROY: 100 },
                    'MediumWeight': { },
                    'HardWeight': { },
                    'ChallengeStore': {
                        (3, 10): None,
                        (3, 9): [
                            (1051, 1),
                            (1082, 1),
                            (1124, 1),
                            (1116, 1),
                            (1105, 1),
                            (1122, 0),
                            (1121, 1),
                            (1120, 1),
                            (1140, 1),
                            (1142, 1),
                            (1143, 1),
                            (1146, 1)],
                        (3, 8): [
                            (1081, 1),
                            (1074, 1),
                            (1079, 1),
                            (1089, 1),
                            (1103, 1),
                            (1140, 1),
                            (1147, 1)],
                        (3, 0): [
                            (1026, 1),
                            (1027, 1),
                            (1043, 1),
                            (1052, 1),
                            (1055, 1),
                            (1057, 1),
                            (1141, 1),
                            (1142, 1),
                            (1143, 1)],
                        (2, 0): [
                            (1018, 1),
                            (1026, 1),
                            (1027, 1),
                            (1141, 1)],
                        (1, 0): [
                            (1015, 1),
                            (1030, 1),
                            (1035, 1),
                            (1065, 1),
                            (1141, 1)] },
                    'SingleChallengeStore': {
                        (3, 10): [],
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelRoomChallenge': {
                        (3, 10): [],
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelExcludeChallenge': {
                        (3, 10): {
                            1201112: [
                                1129,
                                1143],
                            1201114: [
                                1129,
                                1143],
                            1201603: [],
                            1201904: [],
                            1201902: [],
                            1201115: [
                                1129,
                                1143],
                            1201116: [
                                1129,
                                1143],
                            1201117: [
                                1129,
                                1143],
                            1204103: [
                                1129,
                                1143],
                            1201604: [],
                            1201703: [],
                            1201701: [],
                            1201220: [],
                            1201213: [
                                1143],
                            1201906: [],
                            1201223: [
                                1143],
                            1201226: [
                                1143],
                            1201705: [] },
                        3: {
                            1201112: [
                                1129,
                                1143],
                            1201114: [
                                1129,
                                1143],
                            1201603: [],
                            1201904: [],
                            1201902: [],
                            1201115: [
                                1129,
                                1143],
                            1201116: [
                                1129,
                                1143],
                            1201117: [
                                1129,
                                1143],
                            1204103: [
                                1129,
                                1143],
                            1201202: [],
                            1201604: [],
                            1201203: [],
                            1201703: [],
                            1201701: [],
                            1201220: [],
                            1201213: [
                                1143],
                            1201906: [],
                            1201223: [
                                1143],
                            1201225: [
                                1143],
                            1201226: [
                                1143],
                            1201227: [
                                1143],
                            1201224: [
                                1143],
                            1201705: [] },
                        2: {
                            1201112: [],
                            1201114: [],
                            1201603: [],
                            1201904: [],
                            1201902: [],
                            1201115: [],
                            1201116: [],
                            1201117: [],
                            1204103: [],
                            1201202: [],
                            1201604: [],
                            1201203: [],
                            1201703: [],
                            1201220: [],
                            1201213: [],
                            1201906: [],
                            1201223: [],
                            1201225: [],
                            1201226: [],
                            1201227: [],
                            1201224: [],
                            1201705: [] },
                        1: {
                            1201112: [],
                            1201114: [],
                            1201603: [],
                            1201115: [],
                            1201116: [],
                            1201117: [],
                            1204103: [],
                            1201202: [],
                            1201203: [],
                            1201220: [],
                            1201213: [],
                            1201223: [],
                            1201225: [],
                            1201226: [],
                            1201227: [],
                            1201224: [] } },
                    'HideLevel': {
                        1: {
                            1201112: 3,
                            1201114: 3,
                            1201603: 5,
                            1201115: 3,
                            1201116: 3,
                            1201117: 3,
                            1204103: 3,
                            1201202: 1,
                            1201203: 1,
                            1201220: 8,
                            1201213: 3,
                            1201223: 3,
                            1201225: 1,
                            1201226: 3,
                            1201227: 1,
                            1201224: 1 },
                        2: {
                            1201112: 3,
                            1201114: 3,
                            1201603: 5,
                            1201904: 6,
                            1201902: 6,
                            1201115: 3,
                            1201116: 3,
                            1201117: 3,
                            1204103: 3,
                            1201202: 1,
                            1201604: 5,
                            1201203: 1,
                            1201703: 2,
                            1201220: 8,
                            1201213: 3,
                            1201906: 6,
                            1201223: 3,
                            1201225: 1,
                            1201226: 3,
                            1201227: 1,
                            1201224: 1,
                            1201705: 2 },
                        3: {
                            1201112: 3,
                            1201114: 3,
                            1201603: 5,
                            1201904: 6,
                            1201902: 6,
                            1201115: 3,
                            1201116: 3,
                            1201117: 3,
                            1204103: 3,
                            1201202: 1,
                            1201604: 5,
                            1201203: 1,
                            1201703: 2,
                            1201701: 2,
                            1201220: 8,
                            1201213: 3,
                            1201906: 6,
                            1201223: 3,
                            1201225: 1,
                            1201226: 3,
                            1201227: 1,
                            1201224: 1,
                            1201705: 2 } },
                    'HideLevelStore': {
                        (3, 10): {
                            (1201705, 2, 0, (0, 1000), 1): 10,
                            (1201226, 3, 1, (0, 1000), 1): 10,
                            (1201223, 3, 1, (20, 1000), 1): 10,
                            (1201906, 6, 0, (40, 1000), 1): 10,
                            (1201213, 3, 1, (20, 1000), 0): 10,
                            (1201220, 8, 0, (40, 1000), 0): 10,
                            (1201701, 2, 6, (0, 1000), 0): 10,
                            (1201703, 2, 6, (0, 1000), 0): 10,
                            (1201604, 5, 2, (10, 1000), 0): 10,
                            (1204103, 3, 0, (40, 1000), 0): 10,
                            (1201117, 3, 0, (20, 1000), 0): 10,
                            (1201116, 3, 1, (20, 1000), 0): 10,
                            (1201115, 3, 1, (0, 1000), 0): 10,
                            (1201902, 6, 0, (20, 1000), 0): 10,
                            (1201904, 6, 0, (20, 1000), 0): 10,
                            (1201603, 5, 2, (10, 1000), 0): 10,
                            (1201114, 3, 0, (0, 1000), 0): 10,
                            (1201112, 3, 0, (0, 1000), 0): 10 },
                        3: {
                            (1201705, 2, 0, (0, 1000), 1): 10,
                            (1201224, 1, 0, (0, 1000), 1): 10,
                            (1201227, 1, 0, (0, 1000), 1): 10,
                            (1201226, 3, 1, (0, 1000), 1): 10,
                            (1201225, 1, 0, (0, 1000), 1): 10,
                            (1201223, 3, 1, (20, 1000), 1): 10,
                            (1201906, 6, 0, (40, 1000), 1): 10,
                            (1201213, 3, 1, (20, 1000), 0): 10,
                            (1201220, 8, 0, (40, 1000), 0): 10,
                            (1201701, 2, 6, (0, 1000), 0): 10,
                            (1201703, 2, 6, (0, 1000), 0): 10,
                            (1201203, 1, 0, (0, 1000), 0): 10,
                            (1201604, 5, 2, (10, 1000), 0): 10,
                            (1201202, 1, 0, (0, 1000), 0): 10,
                            (1204103, 3, 0, (40, 1000), 0): 10,
                            (1201117, 3, 0, (20, 1000), 0): 10,
                            (1201116, 3, 1, (20, 1000), 0): 10,
                            (1201115, 3, 1, (0, 1000), 0): 10,
                            (1201902, 6, 0, (20, 1000), 0): 10,
                            (1201904, 6, 0, (20, 1000), 0): 10,
                            (1201603, 5, 2, (10, 1000), 0): 10,
                            (1201114, 3, 0, (0, 1000), 0): 10,
                            (1201112, 3, 0, (0, 1000), 0): 10 },
                        2: {
                            (1201705, 2, 0, (0, 1000), 1): 10,
                            (1201224, 1, 0, (0, 1000), 1): 10,
                            (1201227, 1, 0, (0, 1000), 1): 10,
                            (1201226, 3, 1, (0, 1000), 1): 10,
                            (1201225, 1, 0, (0, 1000), 1): 10,
                            (1201223, 3, 1, (20, 1000), 1): 10,
                            (1201906, 6, 0, (40, 1000), 1): 10,
                            (1201213, 3, 1, (20, 1000), 0): 10,
                            (1201220, 8, 0, (40, 1000), 0): 10,
                            (1201703, 2, 6, (0, 1000), 0): 10,
                            (1201203, 1, 0, (0, 1000), 0): 10,
                            (1201604, 5, 2, (10, 1000), 0): 10,
                            (1201202, 1, 0, (0, 1000), 0): 10,
                            (1204103, 3, 0, (40, 1000), 0): 10,
                            (1201117, 3, 0, (20, 1000), 0): 10,
                            (1201116, 3, 1, (20, 1000), 0): 10,
                            (1201115, 3, 1, (0, 1000), 0): 10,
                            (1201902, 6, 0, (20, 1000), 0): 10,
                            (1201904, 6, 0, (20, 1000), 0): 10,
                            (1201603, 5, 2, (10, 1000), 0): 10,
                            (1201114, 3, 0, (0, 1000), 0): 10,
                            (1201112, 3, 0, (0, 1000), 0): 10 },
                        1: {
                            (1201224, 1, 0, (0, 1000), 1): 10,
                            (1201227, 1, 0, (0, 1000), 1): 10,
                            (1201226, 3, 1, (0, 1000), 1): 10,
                            (1201225, 1, 0, (0, 1000), 1): 10,
                            (1201223, 3, 1, (20, 1000), 1): 10,
                            (1201213, 3, 1, (20, 1000), 0): 10,
                            (1201220, 8, 0, (40, 1000), 0): 10,
                            (1201203, 1, 0, (0, 1000), 0): 10,
                            (1201202, 1, 0, (0, 1000), 0): 10,
                            (1204103, 3, 0, (40, 1000), 0): 10,
                            (1201117, 3, 0, (20, 1000), 0): 10,
                            (1201116, 3, 1, (20, 1000), 0): 10,
                            (1201115, 3, 1, (0, 1000), 0): 10,
                            (1201603, 5, 0, (10, 1000), 0): 10,
                            (1201114, 3, 0, (0, 1000), 0): 10,
                            (1201112, 3, 0, (0, 1000), 0): 10 } },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': {
                        (3, 10): [],
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [
                            (1120501, 4),
                            (1120501, 5)],
                        (2, 0): [
                            (1120501, 4),
                            (1120501, 5)],
                        (1, 0): [] },
                    'AIlevelEnhance': 51 } },
            'LayerChoose': {
                1: {
                    LAYER_CHOOSE_CRAFTSMAN: (3, 1, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_SHOP: (1, 1, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_EVENTNPC: (2, 0, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_CHALLENGE: (1, 0, 0, 99, {
                        1: 25,
                        2: 35,
                        3: 40 }, { }),
                    LAYER_CHOOSE_HIDE: (3, 1, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }) },
                2: {
                    LAYER_CHOOSE_CRAFTSMAN: (3, 1, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_SHOP: (1, 1, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_EVENTNPC: (2, 0, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_CHALLENGE: (1, 0, 0, 99, {
                        1: 30,
                        2: 30,
                        3: 40 }, { }),
                    LAYER_CHOOSE_HIDE: (3, 1, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }) },
                3: {
                    LAYER_CHOOSE_S8SHOP: (3, 0, 3, 3, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_S7SHOP: (2, 0, 2, 2, {
                        1: 10,
                        2: 0,
                        3: 10 }, {
                        1: 1,
                        2: 0,
                        3: 1 }),
                    LAYER_CHOOSE_DICESHOP: (2, 0, 2, 2, {
                        1: 0,
                        2: 10,
                        3: 10 }, {
                        1: 0,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_WANDSHOP: (2, 0, 2, 2, {
                        1: 0,
                        2: 10,
                        3: 0 }, {
                        1: 0,
                        2: 1,
                        3: 0 }),
                    LAYER_CHOOSE_RELICLOTTERY: (2, 0, 2, 2, {
                        1: 0,
                        2: 10,
                        3: 10 }, {
                        1: 0,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_PETSHOP: (2, 0, 2, 2, {
                        1: 10,
                        2: 0,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_TASKNPC: (1, 0, 1, 1, {
                        1: 10,
                        2: 10,
                        3: 5 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_GSCASHSHOP: (1, 1, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_CRAFTSMAN: (3, 1, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_SHOP: (1, 1, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_EVENTNPC: (2, 0, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_CHALLENGE: ((lambda *a: 1 + (Func221(*a) // 8) * 5), 0, 1, 99, {
                        1: 30,
                        2: 30,
                        3: 30 }, { }),
                    LAYER_CHOOSE_HIDE: (3, 1, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }) } },
            'BaseGrade': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: (12, 0),
                        2: (15, 0),
                        3: (18, 0) },
                    LEVEL_TYPE_FIGHT: {
                        1: (11, 0),
                        2: (14, 0),
                        3: (17, 0) },
                    LEVEL_TYPE_BOSS: (20, 0),
                    LEVEL_TYPE_HALL: (0, 0) },
                10: {
                    LEVEL_TYPE_HIDE: {
                        1: (13, 0),
                        2: (16, 0),
                        3: (19, 0) },
                    LEVEL_TYPE_FIGHT: {
                        1: (11, 0),
                        2: (14, 0),
                        3: (17, 0) },
                    LEVEL_TYPE_BOSS: (20, 0),
                    LEVEL_TYPE_HALL: (0, 0) } },
            'MonsterAttAdjust': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func209(*a) - 1) * 20000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 20000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 20000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                        ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0),
                        ('MoveSpeed', (lambda *a: (Func209(*a) - 1) * 500 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                        ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)] },
                10: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func209(*a) - 1) * 20000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 20000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 20000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                        ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0),
                        ('MoveSpeed', (lambda *a: (Func209(*a) - 1) * 500 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                        ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)] } },
            'EliteAttAdjust': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                        ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                        ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)] },
                10: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func209(*a) - 1) * 11000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 11000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 11000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                        ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func209(*a) - 1) * 11000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 11000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 11000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                        ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)] } },
            'ItemChoose': 1002 },
        3: {
            'CtrlSize': 3,
            'HallInfo': 1100005,
            'BossInfo': {
                'BossStore': {
                    1301002: 10,
                    1301003: 10 },
                'BossExtra': {
                    1301002: (None, None),
                    1301003: (ChooseAction31301003, ForceAction31301003) },
                'ChallengeStore': {
                    (3, 9): [
                        (1103, 1),
                        (1102, 1),
                        (1119, 1),
                        (1120, 1),
                        (1121, 1)],
                    (3, 8): [
                        (1106, 1),
                        (1077, 0),
                        (1080, 0),
                        (1099, 1),
                        (1102, 1)] },
                'SingleChallengeStore': {
                    (3, 9): [
                        (1103, 1),
                        (1102, 1),
                        (1120, 1),
                        (1121, 1)],
                    (3, 8): [] },
                'ExcludeChallengeArea': {
                    (3, 9): [],
                    (3, 8): [] },
                'UnSpawnRuleInfo': {
                    1301002: [],
                    1301003: [] },
                'ChallengeModeLimit': {
                    (3, 9, 0): {
                        'MULTI': [],
                        'SINGLE': [] },
                    (3, 8, 0): {
                        'MULTI': [],
                        'SINGLE': [] } },
                'AIBosslevelEnhance': {
                    1301002: 55,
                    1301003: 55 } },
            'NpcInfo': {
                'shop': {
                    1005: 10 },
                'craftsman': {
                    1018: 10 },
                'gscashshop': {
                    1054: 10 },
                'tasknpc': {
                    1065: 10 },
                'petshop': {
                    1068: 10 },
                'reliclottery': {
                    1071: 10 },
                'wandshop': {
                    1072: 10 },
                'diceshop': {
                    1073: 10 },
                's7shop': {
                    1074: 10 },
                's8shop': {
                    1075: 10 } },
            'CtrlInfo': {
                1: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (1301101, 1301102, 1301103, 1301104, 1301105, 1301106, 1301107, 1301108),
                    'NormalFilter': {
                        1301101: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1301102: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1301103: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1301104: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1301105: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1301106: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1301107: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1301108: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None } },
                    'MediumStore': (),
                    'HardStore': (),
                    'NormalWeight': {
                        GAMETYPE_DESTROY: 100 },
                    'MediumWeight': { },
                    'HardWeight': { },
                    'ChallengeStore': {
                        (3, 10): None,
                        (3, 9): [
                            (1051, 1),
                            (1130, 1),
                            (1120, 1),
                            (1128, 1),
                            (1129, 1),
                            (1080, 1),
                            (1126, 1)],
                        (3, 8): [
                            (1077, 0),
                            (1078, 1),
                            (1106, 1),
                            (1051, 1),
                            (1104, 1),
                            (1105, 1)],
                        (3, 0): [
                            (1029, 1),
                            (1042, 1),
                            (1068, 1),
                            (1054, 1)],
                        (2, 0): [
                            (1029, 1),
                            (1067, 1),
                            (1054, 1)],
                        (1, 0): [
                            (1028, 1),
                            (1067, 1)] },
                    'SingleChallengeStore': {
                        (3, 10): [],
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelRoomChallenge': {
                        (3, 10): [],
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelExcludeChallenge': {
                        (3, 10): {
                            1300102: [
                                1129],
                            1300103: [
                                1129],
                            1300104: [],
                            1301902: [],
                            1300105: [
                                1129],
                            1300106: [
                                1129],
                            1300107: [
                                1129],
                            1300108: [
                                1129],
                            1300109: [
                                1129],
                            1300110: [
                                1129],
                            1300111: [
                                1129],
                            1301903: [],
                            1301904: [] },
                        3: {
                            1300102: [
                                1129],
                            1300103: [
                                1129],
                            1300104: [],
                            1301902: [],
                            1300105: [
                                1129],
                            1300106: [
                                1129],
                            1300107: [
                                1129],
                            1300108: [
                                1129],
                            1300109: [
                                1129],
                            1300110: [
                                1129],
                            1301201: [],
                            1301202: [],
                            1300111: [
                                1129],
                            1301903: [],
                            1301904: [] },
                        2: {
                            1300102: [],
                            1300103: [],
                            1300104: [],
                            1301902: [],
                            1300105: [],
                            1300106: [],
                            1300107: [],
                            1300108: [],
                            1300109: [],
                            1300110: [],
                            1301201: [],
                            1301202: [],
                            1300111: [] },
                        1: {
                            1300102: [],
                            1300103: [],
                            1300104: [],
                            1300105: [],
                            1300106: [],
                            1300107: [],
                            1300108: [],
                            1300109: [],
                            1300110: [],
                            1301201: [],
                            1301202: [],
                            1300111: [] } },
                    'HideLevel': {
                        1: {
                            1300102: 3,
                            1300103: 3,
                            1300104: 8,
                            1300105: 3,
                            1300106: 3,
                            1300107: 3,
                            1300108: 3,
                            1300109: 3,
                            1300110: 3,
                            1301201: 1,
                            1301202: 1,
                            1300111: 3 },
                        2: {
                            1300102: 3,
                            1300103: 3,
                            1300104: 8,
                            1301902: 6,
                            1300105: 3,
                            1300106: 3,
                            1300107: 3,
                            1300108: 3,
                            1300109: 3,
                            1300110: 3,
                            1301201: 1,
                            1301202: 1,
                            1300111: 3 },
                        3: {
                            1300102: 3,
                            1300103: 3,
                            1300104: 8,
                            1301902: 6,
                            1300105: 3,
                            1300106: 3,
                            1300107: 3,
                            1300108: 3,
                            1300109: 3,
                            1300110: 3,
                            1301201: 1,
                            1301202: 1,
                            1300111: 3,
                            1301903: 6,
                            1301904: 6 } },
                    'HideLevelStore': {
                        (3, 10): {
                            (1301904, 6, 0, (10, 1000), -1): 0,
                            (1301903, 6, 0, (10, 1000), -1): 0,
                            (1300111, 3, 4, (10, 1000), -1): 10,
                            (1300110, 3, 3, (10, 1000), -1): 10,
                            (1300109, 3, 2, (0, 1000), -1): 10,
                            (1300108, 3, 3, (20, 1000), -1): 10,
                            (1300107, 3, 2, (40, 1000), -1): 10,
                            (1300106, 3, 0, (40, 1000), -1): 10,
                            (1300105, 3, 4, (40, 1000), -1): 10,
                            (1301902, 6, 0, (10, 1000), -1): 10,
                            (1300104, 8, 0, (40, 1000), -1): 10,
                            (1300103, 3, 1, (20, 1000), -1): 10,
                            (1300102, 3, 1, (0, 1000), -1): 10 },
                        3: {
                            (1301904, 6, 0, (10, 1000), -1): 0,
                            (1301903, 6, 0, (10, 1000), -1): 0,
                            (1300111, 3, 4, (10, 1000), -1): 10,
                            (1301202, 1, 0, (0, 1000), -1): 10,
                            (1301201, 1, 0, (0, 1000), -1): 10,
                            (1300110, 3, 3, (10, 1000), -1): 10,
                            (1300109, 3, 2, (0, 1000), -1): 10,
                            (1300108, 3, 3, (20, 1000), -1): 10,
                            (1300107, 3, 2, (40, 1000), -1): 10,
                            (1300106, 3, 0, (40, 1000), -1): 10,
                            (1300105, 3, 4, (40, 1000), -1): 10,
                            (1301902, 6, 0, (10, 1000), -1): 10,
                            (1300104, 8, 0, (40, 1000), -1): 10,
                            (1300103, 3, 1, (20, 1000), -1): 10,
                            (1300102, 3, 1, (0, 1000), -1): 10 },
                        2: {
                            (1300111, 3, 4, (10, 1000), -1): 10,
                            (1301202, 1, 0, (0, 1000), -1): 10,
                            (1301201, 1, 0, (0, 1000), -1): 10,
                            (1300110, 3, 3, (10, 1000), -1): 10,
                            (1300109, 3, 2, (0, 1000), -1): 10,
                            (1300108, 3, 3, (20, 1000), -1): 10,
                            (1300107, 3, 2, (40, 1000), -1): 10,
                            (1300106, 3, 0, (40, 1000), -1): 10,
                            (1300105, 3, 4, (40, 1000), -1): 10,
                            (1301902, 6, 0, (10, 1000), -1): 10,
                            (1300104, 8, 0, (40, 1000), -1): 10,
                            (1300103, 3, 1, (20, 1000), -1): 10,
                            (1300102, 3, 1, (0, 1000), -1): 10 },
                        1: {
                            (1300111, 3, 4, (10, 1000), -1): 10,
                            (1301202, 1, 0, (0, 1000), -1): 10,
                            (1301201, 1, 0, (0, 1000), -1): 10,
                            (1300110, 3, 3, (10, 1000), -1): 10,
                            (1300109, 3, 2, (0, 1000), -1): 10,
                            (1300108, 3, 3, (20, 1000), -1): 10,
                            (1300107, 3, 2, (40, 1000), -1): 10,
                            (1300106, 3, 0, (40, 1000), -1): 10,
                            (1300105, 3, 4, (40, 1000), -1): 10,
                            (1300104, 8, 0, (40, 1000), -1): 10,
                            (1300103, 3, 1, (20, 1000), -1): 10,
                            (1300102, 3, 1, (0, 1000), -1): 10 } },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': {
                        (3, 10): [],
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'AIlevelEnhance': 50 },
                2: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (1302101, 1302102, 1302103, 1302104, 1302105, 1302120, 1302107, 1302108, 1302161, 1302162, 1302110, 1302111, 1302112, 1302113, 1302114, 1302115, 1302163),
                    'NormalFilter': {
                        1302101: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction31302101 },
                        1302102: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction31302102 },
                        1302103: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction31302103 },
                        1302104: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction31302104 },
                        1302105: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction31302105 },
                        1302120: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction31302120 },
                        1302107: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction31302107 },
                        1302108: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction31302108 },
                        1302161: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction31302161 },
                        1302162: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction31302162 },
                        1302110: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction31302110 },
                        1302111: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction31302111 },
                        1302112: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction31302112 },
                        1302113: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction31302113 },
                        1302114: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction31302114 },
                        1302115: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction31302115 },
                        1302163: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction31302163 } },
                    'MediumStore': (),
                    'HardStore': (),
                    'NormalWeight': {
                        GAMETYPE_DESTROY: 100 },
                    'MediumWeight': { },
                    'HardWeight': { },
                    'ChallengeStore': {
                        (3, 10): None,
                        (3, 9): [
                            (1082, 1),
                            (1121, 1),
                            (1103, 1),
                            (1125, 1),
                            (1126, 1),
                            (1123, 0),
                            (1105, 1)],
                        (3, 8): [
                            (1081, 1),
                            (1083, 1),
                            (1075, 1),
                            (1106, 1),
                            (1101, 0),
                            (1100, 1)],
                        (3, 0): [
                            (1024, 1),
                            (1030, 1),
                            (1047, 1),
                            (1050, 1),
                            (1052, 1),
                            (1053, 1),
                            (1056, 1)],
                        (2, 0): [
                            (1017, 1),
                            (1024, 1),
                            (1030, 1),
                            (1050, 1),
                            (1053, 1)],
                        (1, 0): [
                            (1024, 1)] },
                    'SingleChallengeStore': {
                        (3, 10): [],
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelRoomChallenge': {
                        (3, 10): [],
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelExcludeChallenge': {
                        (3, 10): {
                            1300102: [
                                1129],
                            1300103: [],
                            1300104: [],
                            1301902: [],
                            1300105: [
                                1129],
                            1300106: [
                                1129],
                            1300107: [
                                1129],
                            1300108: [
                                1129],
                            1300109: [
                                1129],
                            1300110: [
                                1129],
                            1300701: [],
                            1300702: [],
                            1300111: [
                                1129],
                            1301903: [],
                            1301904: [],
                            1301905: [],
                            1301906: [],
                            1301203: [
                                1129],
                            1301204: [
                                1129],
                            1301205: [
                                1129],
                            1301206: [],
                            1301208: [],
                            1302703: [],
                            1301207: [],
                            1302704: [],
                            1301210: [
                                1129],
                            1301209: [],
                            1301212: [],
                            1301214: [] },
                        3: {
                            1300102: [
                                1129],
                            1300103: [],
                            1300104: [],
                            1301902: [],
                            1300105: [
                                1129],
                            1300106: [
                                1129],
                            1300107: [
                                1129],
                            1300108: [
                                1129],
                            1300109: [
                                1129],
                            1300110: [
                                1129],
                            1301201: [],
                            1301202: [],
                            1300701: [],
                            1300702: [],
                            1300111: [
                                1129],
                            1301903: [],
                            1301904: [],
                            1301203: [
                                1129],
                            1301204: [
                                1129],
                            1301205: [
                                1129],
                            1301206: [],
                            1301208: [],
                            1302703: [],
                            1301906: [],
                            1301209: [],
                            1301207: [],
                            1302704: [],
                            1301210: [
                                1129],
                            1301212: [],
                            1301214: [] },
                        2: {
                            1300102: [],
                            1300103: [],
                            1300104: [],
                            1301902: [],
                            1300105: [],
                            1300106: [],
                            1300107: [],
                            1300108: [],
                            1300109: [],
                            1300110: [],
                            1301201: [],
                            1301202: [],
                            1300702: [],
                            1300111: [],
                            1301203: [
                                1129],
                            1301204: [
                                1129],
                            1301205: [
                                1129],
                            1301206: [],
                            1301208: [],
                            1302703: [],
                            1301906: [],
                            1301209: [],
                            1301207: [],
                            1302704: [],
                            1301210: [
                                1129],
                            1301212: [],
                            1301214: [] },
                        1: {
                            1300102: [],
                            1300103: [],
                            1300104: [],
                            1300105: [],
                            1300106: [],
                            1300107: [],
                            1300108: [],
                            1300109: [],
                            1300110: [],
                            1301201: [],
                            1301202: [],
                            1300111: [],
                            1301203: [
                                1129],
                            1301204: [
                                1129],
                            1301205: [
                                1129],
                            1301206: [],
                            1301208: [],
                            1301209: [],
                            1301207: [],
                            1301210: [
                                1129],
                            1301212: [],
                            1301214: [] } },
                    'HideLevel': {
                        1: {
                            1300102: 3,
                            1300103: 3,
                            1300104: 8,
                            1300105: 3,
                            1300106: 3,
                            1300107: 3,
                            1300108: 3,
                            1300109: 3,
                            1300110: 3,
                            1301201: 1,
                            1301202: 1,
                            1300111: 3,
                            1301203: 3,
                            1301204: 3,
                            1301205: 3,
                            1301206: 1,
                            1301208: 1,
                            1301209: 1,
                            1301207: 8,
                            1301210: 3,
                            1301212: 8,
                            1301214: 8 },
                        2: {
                            1300102: 3,
                            1300103: 3,
                            1300104: 8,
                            1301902: 6,
                            1300105: 3,
                            1300106: 3,
                            1300107: 3,
                            1300108: 3,
                            1300109: 3,
                            1300110: 3,
                            1301201: 1,
                            1301202: 1,
                            1300702: 2,
                            1300111: 3,
                            1301203: 3,
                            1301204: 3,
                            1301205: 3,
                            1301206: 1,
                            1301208: 1,
                            1302703: 2,
                            1301906: 6,
                            1301209: 1,
                            1301207: 8,
                            1302704: 2,
                            1301210: 3,
                            1301212: 8,
                            1301214: 8 },
                        3: {
                            1300102: 3,
                            1300103: 3,
                            1300104: 8,
                            1301902: 6,
                            1300105: 3,
                            1300106: 3,
                            1300107: 3,
                            1300108: 3,
                            1300109: 3,
                            1300110: 3,
                            1301201: 1,
                            1301202: 1,
                            1300701: 2,
                            1300702: 2,
                            1300111: 3,
                            1301903: 6,
                            1301904: 6,
                            1301203: 3,
                            1301204: 3,
                            1301205: 3,
                            1301206: 1,
                            1301208: 1,
                            1302703: 2,
                            1301906: 6,
                            1301209: 1,
                            1301207: 8,
                            1302704: 2,
                            1301210: 3,
                            1301212: 8,
                            1301214: 8,
                            1301905: 6 } },
                    'HideLevelStore': {
                        (3, 10): {
                            (1301214, 8, 0, (40, 1000), 1): 10,
                            (1301212, 8, 0, (40, 1000), 1): 10,
                            (1301209, 1, 0, (0, 1000), 1): 10,
                            (1301210, 3, 4, (40, 1000), 1): 10,
                            (1302704, 2, 6, (0, 1000), 1): 10,
                            (1301207, 8, 0, (40, 1000), 1): 10,
                            (1302703, 2, 0, (0, 1000), 1): 10,
                            (1301208, 1, 0, (0, 1000), 1): 10,
                            (1301206, 1, 0, (0, 1000), 1): 10,
                            (1301205, 3, 4, (40, 1000), 1): 10,
                            (1301204, 3, 4, (40, 1000), 1): 10,
                            (1301203, 3, 4, (40, 1000), 1): 10,
                            (1301906, 6, 0, (10, 1000), 1): 10,
                            (1301905, 6, 0, (10, 1000), 0): 0,
                            (1301904, 6, 0, (10, 1000), 0): 0,
                            (1301903, 6, 0, (10, 1000), 0): 0,
                            (1300111, 3, 4, (10, 1000), 0): 10,
                            (1300702, 2, 6, (0, 1000), 0): 10,
                            (1300701, 2, 6, (0, 1000), 0): 10,
                            (1300110, 3, 3, (10, 1000), 0): 10,
                            (1300109, 3, 2, (0, 1000), 0): 10,
                            (1300108, 3, 3, (20, 1000), 0): 10,
                            (1300107, 3, 2, (40, 1000), 0): 10,
                            (1300106, 3, 0, (40, 1000), 0): 10,
                            (1300105, 3, 4, (40, 1000), 0): 10,
                            (1301902, 6, 0, (10, 1000), 0): 10,
                            (1300104, 8, 0, (40, 1000), 0): 10,
                            (1300103, 3, 1, (20, 1000), 0): 10,
                            (1300102, 3, 1, (0, 1000), 0): 10 },
                        3: {
                            (1301214, 8, 0, (40, 1000), 1): 10,
                            (1301212, 8, 0, (40, 1000), 1): 10,
                            (1301210, 3, 4, (40, 1000), 1): 10,
                            (1302704, 2, 6, (0, 1000), 1): 10,
                            (1301207, 8, 0, (40, 1000), 1): 10,
                            (1301209, 1, 0, (0, 1000), 1): 10,
                            (1301906, 6, 0, (10, 1000), 1): 10,
                            (1302703, 2, 0, (0, 1000), 1): 10,
                            (1301208, 1, 0, (0, 1000), 1): 10,
                            (1301206, 1, 0, (0, 1000), 1): 10,
                            (1301205, 3, 4, (40, 1000), 1): 10,
                            (1301204, 3, 4, (40, 1000), 1): 10,
                            (1301203, 3, 4, (40, 1000), 1): 10,
                            (1301904, 6, 0, (10, 1000), 0): 0,
                            (1301903, 6, 0, (10, 1000), 0): 0,
                            (1300111, 3, 4, (10, 1000), 0): 10,
                            (1300702, 2, 6, (0, 1000), 0): 10,
                            (1300701, 2, 6, (0, 1000), 0): 10,
                            (1301202, 1, 0, (0, 1000), 0): 10,
                            (1301201, 1, 0, (0, 1000), 0): 10,
                            (1300110, 3, 3, (10, 1000), 0): 10,
                            (1300109, 3, 2, (0, 1000), 0): 10,
                            (1300108, 3, 3, (20, 1000), 0): 10,
                            (1300107, 3, 2, (40, 1000), 0): 10,
                            (1300106, 3, 0, (40, 1000), 0): 10,
                            (1300105, 3, 4, (40, 1000), 0): 10,
                            (1301902, 6, 0, (10, 1000), 0): 10,
                            (1300104, 8, 0, (40, 1000), 0): 10,
                            (1300103, 3, 1, (20, 1000), 0): 10,
                            (1300102, 3, 1, (0, 1000), 0): 10 },
                        2: {
                            (1301214, 8, 0, (40, 1000), 1): 10,
                            (1301212, 8, 0, (40, 1000), 1): 10,
                            (1301210, 3, 4, (40, 1000), 1): 10,
                            (1302704, 2, 6, (0, 1000), 1): 10,
                            (1301207, 8, 0, (40, 1000), 1): 10,
                            (1301209, 1, 0, (0, 1000), 1): 10,
                            (1301906, 6, 0, (10, 1000), 1): 10,
                            (1302703, 2, 0, (0, 1000), 1): 10,
                            (1301208, 1, 0, (0, 1000), 1): 10,
                            (1301206, 1, 0, (0, 1000), 1): 10,
                            (1301205, 3, 4, (40, 1000), 1): 10,
                            (1301204, 3, 4, (40, 1000), 1): 10,
                            (1301203, 3, 4, (40, 1000), 1): 10,
                            (1300111, 3, 4, (10, 1000), 0): 10,
                            (1300702, 2, 6, (0, 1000), 0): 10,
                            (1301202, 1, 0, (0, 1000), 0): 10,
                            (1301201, 1, 0, (0, 1000), 0): 10,
                            (1300110, 3, 3, (10, 1000), 0): 10,
                            (1300109, 3, 2, (0, 1000), 0): 10,
                            (1300108, 3, 3, (20, 1000), 0): 10,
                            (1300107, 3, 2, (40, 1000), 0): 10,
                            (1300106, 3, 0, (40, 1000), 0): 10,
                            (1300105, 3, 4, (40, 1000), 0): 10,
                            (1301902, 6, 0, (10, 1000), 0): 10,
                            (1300104, 8, 0, (40, 1000), 0): 10,
                            (1300103, 3, 1, (20, 1000), 0): 10,
                            (1300102, 3, 1, (0, 1000), 0): 10 },
                        1: {
                            (1301214, 8, 0, (40, 1000), 1): 10,
                            (1301212, 8, 0, (40, 1000), 1): 10,
                            (1301210, 3, 4, (40, 1000), 1): 10,
                            (1301207, 8, 0, (40, 1000), 1): 10,
                            (1301209, 1, 0, (0, 1000), 1): 10,
                            (1301208, 1, 0, (0, 1000), 1): 10,
                            (1301206, 1, 0, (0, 1000), 1): 10,
                            (1301205, 3, 4, (40, 1000), 1): 10,
                            (1301204, 3, 4, (40, 1000), 1): 10,
                            (1301203, 3, 4, (40, 1000), 1): 10,
                            (1300111, 3, 4, (10, 1000), 0): 10,
                            (1301202, 1, 0, (0, 1000), 0): 10,
                            (1301201, 1, 0, (0, 1000), 0): 10,
                            (1300110, 3, 3, (10, 1000), 0): 10,
                            (1300109, 3, 2, (0, 1000), 0): 10,
                            (1300108, 3, 3, (20, 1000), 0): 10,
                            (1300107, 3, 2, (40, 1000), 0): 10,
                            (1300106, 3, 0, (40, 1000), 0): 10,
                            (1300105, 3, 4, (40, 1000), 0): 10,
                            (1300104, 8, 0, (40, 1000), 0): 10,
                            (1300103, 3, 1, (20, 1000), 0): 10,
                            (1300102, 3, 1, (0, 1000), 0): 10 } },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': {
                        (3, 10): [],
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'AIlevelEnhance': 52 },
                3: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (1303101, 1303102, 1303103, 1303104, 1303105, 1303106, 1303107, 1303108, 1303110, 1303111, 1303112, 1303109, 1303113, 1303116),
                    'NormalFilter': {
                        1303101: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction31303101 },
                        1303102: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction31303102 },
                        1303103: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction31303103 },
                        1303104: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction31303104 },
                        1303105: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction31303105 },
                        1303106: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction31303106 },
                        1303107: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction31303107 },
                        1303108: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction31303108 },
                        1303110: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction31303110 },
                        1303111: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction31303111 },
                        1303112: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction31303112 },
                        1303109: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction31303109 },
                        1303113: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction31303113 },
                        1303116: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': ChooseAction31303116 } },
                    'MediumStore': (),
                    'HardStore': (),
                    'NormalWeight': {
                        GAMETYPE_DESTROY: 100 },
                    'MediumWeight': { },
                    'HardWeight': { },
                    'ChallengeStore': {
                        (3, 10): None,
                        (3, 9): [
                            (1120, 1),
                            (1082, 1),
                            (1103, 1),
                            (1117, 1),
                            (1105, 1),
                            (1121, 1),
                            (1123, 0),
                            (1130, 1)],
                        (3, 8): [
                            (1080, 1),
                            (1082, 1),
                            (1078, 1),
                            (1085, 1),
                            (1090, 1),
                            (1103, 1)],
                        (3, 0): [
                            (1030, 1),
                            (1041, 1),
                            (1046, 1),
                            (1050, 1),
                            (1053, 1),
                            (1064, 1)],
                        (2, 0): [
                            (1016, 1),
                            (1030, 1),
                            (1036, 1),
                            (1037, 1),
                            (1050, 1),
                            (1063, 1)],
                        (1, 0): [
                            (1025, 1),
                            (1029, 1)] },
                    'SingleChallengeStore': {
                        (3, 10): [],
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelRoomChallenge': {
                        (3, 10): [],
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelExcludeChallenge': {
                        (3, 10): {
                            1300102: [
                                1129],
                            1300103: [
                                1129],
                            1300104: [],
                            1301902: [],
                            1300105: [
                                1129],
                            1300106: [
                                1129],
                            1300107: [
                                1129],
                            1300108: [
                                1129],
                            1300109: [
                                1129],
                            1300110: [
                                1129],
                            1300701: [],
                            1300702: [],
                            1300111: [
                                1129],
                            1301903: [],
                            1301904: [],
                            1301905: [],
                            1301203: [
                                1129],
                            1301204: [
                                1129],
                            1301205: [
                                1129],
                            1301206: [],
                            1301208: [],
                            1302703: [],
                            1301906: [],
                            1301209: [],
                            1301210: [
                                1129],
                            1301207: [],
                            1302704: [],
                            1301212: [],
                            1301214: [] },
                        3: {
                            1300102: [
                                1129],
                            1300103: [
                                1129],
                            1300104: [],
                            1301902: [],
                            1300105: [
                                1129],
                            1300106: [
                                1129],
                            1300107: [
                                1129],
                            1300108: [
                                1129],
                            1300109: [
                                1129],
                            1300110: [
                                1129],
                            1301201: [],
                            1301202: [],
                            1300701: [],
                            1300702: [],
                            1300111: [
                                1129],
                            1301903: [],
                            1301904: [],
                            1301203: [
                                1129],
                            1301204: [
                                1129],
                            1301205: [
                                1129],
                            1301206: [],
                            1301208: [],
                            1302703: [],
                            1301906: [],
                            1301209: [],
                            1301207: [],
                            1302704: [],
                            1301210: [
                                1129],
                            1301212: [],
                            1301214: [] },
                        2: {
                            1300102: [],
                            1300103: [],
                            1300104: [],
                            1301902: [],
                            1300105: [],
                            1300106: [],
                            1300107: [],
                            1300108: [],
                            1300109: [],
                            1300110: [],
                            1301201: [],
                            1301202: [],
                            1300702: [],
                            1300111: [],
                            1301203: [
                                1129],
                            1301204: [
                                1129],
                            1301205: [
                                1129],
                            1301206: [],
                            1301208: [],
                            1302703: [],
                            1301906: [],
                            1301209: [],
                            1301207: [],
                            1302704: [],
                            1301210: [
                                1129],
                            1301212: [],
                            1301214: [] },
                        1: {
                            1300102: [],
                            1300103: [],
                            1300104: [],
                            1300105: [],
                            1300106: [],
                            1300107: [],
                            1300108: [],
                            1300109: [],
                            1300110: [],
                            1301201: [],
                            1301202: [],
                            1300111: [],
                            1301203: [
                                1129],
                            1301204: [
                                1129],
                            1301205: [
                                1129],
                            1301206: [],
                            1301208: [],
                            1301209: [],
                            1301207: [],
                            1301210: [
                                1129],
                            1301212: [],
                            1301214: [] } },
                    'HideLevel': {
                        1: {
                            1300102: 3,
                            1300103: 3,
                            1300104: 8,
                            1300105: 3,
                            1300106: 3,
                            1300107: 3,
                            1300108: 3,
                            1300109: 3,
                            1300110: 3,
                            1301201: 1,
                            1301202: 1,
                            1300111: 3,
                            1301203: 3,
                            1301204: 3,
                            1301205: 3,
                            1301206: 1,
                            1301208: 1,
                            1301209: 1,
                            1301207: 8,
                            1301210: 3,
                            1301212: 8,
                            1301214: 8 },
                        2: {
                            1300102: 3,
                            1300103: 3,
                            1300104: 8,
                            1301902: 6,
                            1300105: 3,
                            1300106: 3,
                            1300107: 3,
                            1300108: 3,
                            1300109: 3,
                            1300110: 3,
                            1301201: 1,
                            1301202: 1,
                            1300702: 2,
                            1300111: 3,
                            1301203: 3,
                            1301204: 3,
                            1301205: 3,
                            1301206: 1,
                            1301208: 1,
                            1302703: 2,
                            1301906: 6,
                            1301209: 1,
                            1301207: 8,
                            1302704: 2,
                            1301210: 3,
                            1301212: 8,
                            1301214: 8 },
                        3: {
                            1300102: 3,
                            1300103: 3,
                            1300104: 8,
                            1301902: 6,
                            1300105: 3,
                            1300106: 3,
                            1300107: 3,
                            1300108: 3,
                            1300109: 3,
                            1300110: 3,
                            1301201: 1,
                            1301202: 1,
                            1300701: 2,
                            1300702: 2,
                            1300111: 3,
                            1301903: 6,
                            1301904: 6,
                            1301203: 3,
                            1301204: 3,
                            1301205: 3,
                            1301206: 1,
                            1301208: 1,
                            1302703: 2,
                            1301906: 6,
                            1301209: 1,
                            1301207: 8,
                            1302704: 2,
                            1301210: 3,
                            1301212: 8,
                            1301214: 8,
                            1301905: 6 } },
                    'HideLevelStore': {
                        (3, 10): {
                            (1301214, 8, 0, (40, 1000), 1): 10,
                            (1301212, 8, 0, (40, 1000), 1): 10,
                            (1302704, 2, 6, (0, 1000), 1): 10,
                            (1301207, 8, 0, (40, 1000), 1): 10,
                            (1301210, 3, 4, (40, 1000), 1): 10,
                            (1301209, 1, 0, (0, 1000), 1): 10,
                            (1301906, 6, 0, (10, 1000), 1): 10,
                            (1302703, 2, 0, (0, 1000), 1): 10,
                            (1301208, 1, 0, (0, 1000), 1): 10,
                            (1301206, 1, 0, (0, 1000), 1): 10,
                            (1301205, 3, 4, (40, 1000), 1): 10,
                            (1301204, 3, 4, (40, 1000), 1): 10,
                            (1301203, 3, 4, (40, 1000), 1): 10,
                            (1301905, 6, 0, (10, 1000), 0): 0,
                            (1301904, 6, 0, (10, 1000), 0): 0,
                            (1301903, 6, 0, (10, 1000), 0): 0,
                            (1300111, 3, 4, (10, 1000), 0): 10,
                            (1300702, 2, 6, (0, 1000), 0): 10,
                            (1300701, 2, 6, (0, 1000), 0): 10,
                            (1300110, 3, 3, (10, 1000), 0): 10,
                            (1300109, 3, 2, (0, 1000), 0): 10,
                            (1300108, 3, 3, (20, 1000), 0): 10,
                            (1300107, 3, 2, (40, 1000), 0): 10,
                            (1300106, 3, 0, (40, 1000), 0): 10,
                            (1300105, 3, 4, (40, 1000), 0): 10,
                            (1301902, 6, 0, (10, 1000), 0): 10,
                            (1300104, 8, 0, (40, 1000), 0): 10,
                            (1300103, 3, 1, (20, 1000), 0): 10,
                            (1300102, 3, 1, (0, 1000), 0): 10 },
                        3: {
                            (1301214, 8, 0, (40, 1000), 1): 10,
                            (1301212, 8, 0, (40, 1000), 1): 10,
                            (1301210, 3, 4, (40, 1000), 1): 10,
                            (1302704, 2, 6, (0, 1000), 1): 10,
                            (1301207, 8, 0, (40, 1000), 1): 10,
                            (1301209, 1, 0, (0, 1000), 1): 10,
                            (1301906, 6, 0, (10, 1000), 1): 10,
                            (1302703, 2, 0, (0, 1000), 1): 10,
                            (1301208, 1, 0, (0, 1000), 1): 10,
                            (1301206, 1, 0, (0, 1000), 1): 10,
                            (1301205, 3, 4, (40, 1000), 1): 10,
                            (1301204, 3, 4, (40, 1000), 1): 10,
                            (1301203, 3, 4, (40, 1000), 1): 10,
                            (1301904, 6, 0, (10, 1000), 0): 0,
                            (1301903, 6, 0, (10, 1000), 0): 0,
                            (1300111, 3, 4, (10, 1000), 0): 10,
                            (1300702, 2, 6, (0, 1000), 0): 10,
                            (1300701, 2, 6, (0, 1000), 0): 10,
                            (1301202, 1, 0, (0, 1000), 0): 10,
                            (1301201, 1, 0, (0, 1000), 0): 10,
                            (1300110, 3, 3, (10, 1000), 0): 10,
                            (1300109, 3, 2, (0, 1000), 0): 10,
                            (1300108, 3, 3, (20, 1000), 0): 10,
                            (1300107, 3, 2, (40, 1000), 0): 10,
                            (1300106, 3, 0, (40, 1000), 0): 10,
                            (1300105, 3, 4, (40, 1000), 0): 10,
                            (1301902, 6, 0, (10, 1000), 0): 10,
                            (1300104, 8, 0, (40, 1000), 0): 10,
                            (1300103, 3, 1, (20, 1000), 0): 10,
                            (1300102, 3, 1, (0, 1000), 0): 10 },
                        2: {
                            (1301214, 8, 0, (40, 1000), 1): 10,
                            (1301212, 8, 0, (40, 1000), 1): 10,
                            (1301210, 3, 4, (40, 1000), 1): 10,
                            (1302704, 2, 6, (0, 1000), 1): 10,
                            (1301207, 8, 0, (40, 1000), 1): 10,
                            (1301209, 1, 0, (0, 1000), 1): 10,
                            (1301906, 6, 0, (10, 1000), 1): 10,
                            (1302703, 2, 0, (0, 1000), 1): 10,
                            (1301208, 1, 0, (0, 1000), 1): 10,
                            (1301206, 1, 0, (0, 1000), 1): 10,
                            (1301205, 3, 4, (40, 1000), 1): 10,
                            (1301204, 3, 4, (40, 1000), 1): 10,
                            (1301203, 3, 4, (40, 1000), 1): 10,
                            (1300111, 3, 4, (10, 1000), 0): 10,
                            (1300702, 2, 6, (0, 1000), 0): 10,
                            (1301202, 1, 0, (0, 1000), 0): 10,
                            (1301201, 1, 0, (0, 1000), 0): 10,
                            (1300110, 3, 3, (10, 1000), 0): 10,
                            (1300109, 3, 2, (0, 1000), 0): 10,
                            (1300108, 3, 3, (20, 1000), 0): 10,
                            (1300107, 3, 2, (40, 1000), 0): 10,
                            (1300106, 3, 0, (40, 1000), 0): 10,
                            (1300105, 3, 4, (40, 1000), 0): 10,
                            (1301902, 6, 0, (10, 1000), 0): 10,
                            (1300104, 8, 0, (40, 1000), 0): 10,
                            (1300103, 3, 1, (20, 1000), 0): 10,
                            (1300102, 3, 1, (0, 1000), 0): 10 },
                        1: {
                            (1301214, 8, 0, (40, 1000), 1): 10,
                            (1301212, 8, 0, (40, 1000), 1): 10,
                            (1301210, 3, 4, (40, 1000), 1): 10,
                            (1301207, 8, 0, (40, 1000), 1): 10,
                            (1301209, 1, 0, (0, 1000), 1): 10,
                            (1301208, 1, 0, (0, 1000), 1): 10,
                            (1301206, 1, 0, (0, 1000), 1): 10,
                            (1301205, 3, 4, (40, 1000), 1): 10,
                            (1301204, 3, 4, (40, 1000), 1): 10,
                            (1301203, 3, 4, (40, 1000), 1): 10,
                            (1300111, 3, 4, (10, 1000), 0): 10,
                            (1301202, 1, 0, (0, 1000), 0): 10,
                            (1301201, 1, 0, (0, 1000), 0): 10,
                            (1300110, 3, 3, (10, 1000), 0): 10,
                            (1300109, 3, 2, (0, 1000), 0): 10,
                            (1300108, 3, 3, (20, 1000), 0): 10,
                            (1300107, 3, 2, (40, 1000), 0): 10,
                            (1300106, 3, 0, (40, 1000), 0): 10,
                            (1300105, 3, 4, (40, 1000), 0): 10,
                            (1300104, 8, 0, (40, 1000), 0): 10,
                            (1300103, 3, 1, (20, 1000), 0): 10,
                            (1300102, 3, 1, (0, 1000), 0): 10 } },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': {
                        (3, 10): [],
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'AIlevelEnhance': 55 } },
            'LayerChoose': {
                1: {
                    LAYER_CHOOSE_CRAFTSMAN: (3, 1, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_SHOP: (1, 1, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_EVENTNPC: (2, 1, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_CHALLENGE: (1, 0, 0, 99, {
                        1: 25,
                        2: 35,
                        3: 40 }, { }),
                    LAYER_CHOOSE_HIDE: (3, 1, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }) },
                2: {
                    LAYER_CHOOSE_CRAFTSMAN: (3, 1, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_SHOP: (1, 1, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_EVENTNPC: (2, 1, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_CHALLENGE: (1, 0, 0, 99, {
                        1: 30,
                        2: 30,
                        3: 40 }, { }),
                    LAYER_CHOOSE_HIDE: (3, 1, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }) },
                3: {
                    LAYER_CHOOSE_S8SHOP: (3, 0, 3, 3, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_S7SHOP: (2, 0, 1, 1, {
                        1: 0,
                        2: 10,
                        3: 0 }, {
                        1: 0,
                        2: 1,
                        3: 0 }),
                    LAYER_CHOOSE_DICESHOP: (2, 0, 2, 2, {
                        1: 0,
                        2: 10,
                        3: 10 }, {
                        1: 0,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_WANDSHOP: (2, 0, 2, 2, {
                        1: 0,
                        2: 10,
                        3: 0 }, {
                        1: 0,
                        2: 1,
                        3: 0 }),
                    LAYER_CHOOSE_RELICLOTTERY: (2, 0, 2, 2, {
                        1: 0,
                        2: 10,
                        3: 10 }, {
                        1: 0,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_PETSHOP: (2, 0, 2, 2, {
                        1: 10,
                        2: 0,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_TASKNPC: (2, 0, 2, 2, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_GSCASHSHOP: (1, 1, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_CRAFTSMAN: (3, 1, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_SHOP: (1, 1, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_EVENTNPC: (2, 1, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_CHALLENGE: ((lambda *a: 1 + (Func221(*a) // 8) * 6), 0, 1, 99, {
                        1: 30,
                        2: 30,
                        3: 30 }, { }),
                    LAYER_CHOOSE_HIDE: (3, 1, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }) } },
            'BaseGrade': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: (22, 0),
                        2: (25, 0),
                        3: (28, 0) },
                    LEVEL_TYPE_FIGHT: {
                        1: (21, 0),
                        2: (24, 0),
                        3: (27, 0) },
                    LEVEL_TYPE_BOSS: (30, 0),
                    LEVEL_TYPE_HALL: (0, 0) },
                10: {
                    LEVEL_TYPE_HIDE: {
                        1: (24, 0),
                        2: (27, 0),
                        3: (30, 0) },
                    LEVEL_TYPE_FIGHT: {
                        1: (21, 0),
                        2: (24, 0),
                        3: (27, 0) },
                    LEVEL_TYPE_BOSS: (30, 0),
                    LEVEL_TYPE_HALL: (0, 0) } },
            'MonsterAttAdjust': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func209(*a) - 1) * 20000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 20000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 20000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                        ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0),
                        ('MoveSpeed', (lambda *a: (Func209(*a) - 1) * 500 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                        ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)] },
                10: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func209(*a) - 1) * 20000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 20000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 20000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                        ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0),
                        ('MoveSpeed', (lambda *a: (Func209(*a) - 1) * 500 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                        ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)] } },
            'EliteAttAdjust': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                        ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                        ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)] },
                10: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func209(*a) - 1) * 11000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 11000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 11000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                        ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func209(*a) - 1) * 11000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 11000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 11000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                        ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)] } },
            'ItemChoose': 1003 },
        4: {
            'CtrlSize': 2,
            'HallInfo': 1400001,
            'BossInfo': {
                'BossStore': {
                    1403001: 10,
                    1403002: 10,
                    1403003: 10,
                    1403004: 10 },
                'BossExtra': {
                    1403001: (ChooseAction41403001, None),
                    1403002: (ChooseAction41403002, None),
                    1403003: (ChooseAction41403003, ForceAction41403003),
                    1403004: (ChooseAction41403004, ForceAction41403004) },
                'ChallengeStore': {
                    (3, 9): [
                        (1105, 0),
                        (1103, 1),
                        (1102, 1),
                        (1120, 1),
                        (1119, 1),
                        (1121, 1)],
                    (3, 0): [
                        (1080, 1),
                        (1092, 1),
                        (1099, 1),
                        (1102, 1)],
                    (3, 8): [
                        (1080, 1),
                        (1092, 1),
                        (1099, 1),
                        (1102, 1)] },
                'SingleChallengeStore': {
                    (3, 9): [
                        (1105, 0),
                        (1103, 1),
                        (1102, 1),
                        (1120, 1),
                        (1121, 1)],
                    (3, 0): [],
                    (3, 8): [] },
                'ExcludeChallengeArea': {
                    (3, 9): [],
                    (3, 0): [],
                    (3, 8): [] },
                'UnSpawnRuleInfo': {
                    1403001: [],
                    1403002: [],
                    1403003: [],
                    1403004: [] },
                'ChallengeModeLimit': {
                    (3, 9, 1002): {
                        'MULTI': [
                            (1105, 0),
                            (1103, 1),
                            (1102, 1),
                            (1120, 1),
                            (1119, 1),
                            (1121, 1)],
                        'SINGLE': [
                            (1105, 0),
                            (1103, 1),
                            (1102, 1),
                            (1120, 1),
                            (1121, 1)] },
                    (3, 9, 0): {
                        'MULTI': [],
                        'SINGLE': [] },
                    (3, 0, 1002): {
                        'MULTI': [
                            (1080, 1),
                            (1092, 1),
                            (1099, 1),
                            (1102, 1)],
                        'SINGLE': [] },
                    (3, 8, 0): {
                        'MULTI': [],
                        'SINGLE': [] } },
                'AIBosslevelEnhance': {
                    1403001: 100,
                    1403002: 100,
                    1403003: 100,
                    1403004: 100 } },
            'NpcInfo': {
                'shop': {
                    1059: 10 },
                'craftsman': {
                    1018: 10 },
                'gscashshop': {
                    1054: 10 },
                'tasknpc': {
                    1065: 10 },
                'petshop': {
                    1068: 10 },
                'reliclottery': {
                    1071: 10 },
                'wandshop': {
                    1072: 10 },
                'diceshop': {
                    1073: 10 },
                's7shop': {
                    1074: 10 },
                's8shop': {
                    1075: 10 } },
            'CtrlInfo': {
                1: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (1401101, 1401102, 1401103, 1401104, 1401105, 1401106, 1401107),
                    'NormalFilter': {
                        1401101: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1401102: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1401103: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1401104: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1401105: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1401106: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1401107: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None } },
                    'MediumStore': (),
                    'HardStore': (),
                    'NormalWeight': {
                        GAMETYPE_DESTROY: 100 },
                    'MediumWeight': { },
                    'HardWeight': { },
                    'ChallengeStore': {
                        (3, 10): None,
                        (3, 9): [
                            (1130, 1),
                            (1082, 1),
                            (1120, 1),
                            (1126, 1),
                            (1105, 1),
                            (1127, 0)],
                        (3, 8): [
                            (1078, 1),
                            (1082, 1),
                            (1083, 1),
                            (1104, 1),
                            (1105, 1)],
                        (3, 0): [
                            (1003, 1),
                            (1051, 1),
                            (1095, 1),
                            (1096, 1)],
                        (2, 0): [
                            (1003, 1),
                            (1051, 1),
                            (1095, 1)],
                        (1, 0): [
                            (1003, 1)] },
                    'SingleChallengeStore': {
                        (3, 10): [],
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelRoomChallenge': {
                        (3, 10): [],
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelExcludeChallenge': {
                        (3, 10): {
                            1401204: [
                                1129],
                            1401205: [
                                1129] },
                        3: {
                            1401201: [],
                            1401204: [
                                1129],
                            1401205: [
                                1129] },
                        2: {
                            1401201: [],
                            1401204: [],
                            1401205: [] },
                        1: {
                            1401201: [],
                            1401204: [],
                            1401205: [] } },
                    'HideLevel': {
                        1: {
                            1401201: 1,
                            1401204: 3,
                            1401205: 3 },
                        2: {
                            1401201: 1,
                            1401204: 3,
                            1401205: 3 },
                        3: {
                            1401201: 1,
                            1401204: 3,
                            1401205: 3 } },
                    'HideLevelStore': {
                        (3, 10): {
                            (1401205, 3, 0, (0, 1000), -1): 10,
                            (1401204, 3, 0, (0, 1000), -1): 10 },
                        3: {
                            (1401205, 3, 0, (0, 1000), -1): 10,
                            (1401204, 3, 0, (0, 1000), -1): 10,
                            (1401201, 1, 0, (0, 1000), -1): 10 },
                        2: {
                            (1401205, 3, 0, (0, 1000), -1): 10,
                            (1401204, 3, 0, (0, 1000), -1): 10,
                            (1401201, 1, 0, (0, 1000), -1): 10 },
                        1: {
                            (1401205, 3, 0, (0, 1000), -1): 10,
                            (1401204, 3, 0, (0, 1000), -1): 10,
                            (1401201, 1, 0, (0, 1000), -1): 10 } },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': {
                        (3, 10): [],
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'AIlevelEnhance': 72 },
                2: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (1402101, 1402102, 1402103, 1402105, 1402104, 1402106, 1402107, 1402108),
                    'NormalFilter': {
                        1402101: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1402102: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1402103: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1402105: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1402104: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1402106: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1402107: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1402108: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None } },
                    'MediumStore': (),
                    'HardStore': (),
                    'NormalWeight': {
                        GAMETYPE_DESTROY: 100 },
                    'MediumWeight': { },
                    'HardWeight': { },
                    'ChallengeStore': {
                        (3, 10): None,
                        (3, 9): [
                            (1051, 1),
                            (1127, 0),
                            (1103, 1),
                            (1130, 1),
                            (1121, 1),
                            (1120, 1),
                            (1118, 1)],
                        (3, 8): [
                            (1077, 0),
                            (1106, 1),
                            (1091, 1),
                            (1098, 1),
                            (1103, 1)],
                        (3, 0): [
                            (1050, 1),
                            (1054, 1),
                            (1056, 1),
                            (1087, 1),
                            (1093, 1),
                            (1094, 1)],
                        (2, 0): [
                            (1050, 1),
                            (1054, 1),
                            (1056, 1),
                            (1087, 1),
                            (1093, 1)],
                        (1, 0): [
                            (1054, 1),
                            (1087, 1)] },
                    'SingleChallengeStore': {
                        (3, 10): [],
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelRoomChallenge': {
                        (3, 10): [],
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelExcludeChallenge': {
                        (3, 10): {
                            1401202: [
                                1129] },
                        3: {
                            1401202: [
                                1129],
                            1401203: [
                                1129],
                            1401206: [] },
                        2: {
                            1401202: [],
                            1401203: [],
                            1401206: [] },
                        1: {
                            1401202: [],
                            1401203: [],
                            1401206: [] } },
                    'HideLevel': {
                        1: {
                            1401202: 3,
                            1401203: 1,
                            1401206: 1 },
                        2: {
                            1401202: 3,
                            1401203: 1,
                            1401206: 1 },
                        3: {
                            1401202: 3,
                            1401203: 1,
                            1401206: 1 } },
                    'HideLevelStore': {
                        (3, 10): {
                            (1401202, 3, 0, (0, 1000), -1): 10 },
                        3: {
                            (1401206, 1, 0, (0, 1000), -1): 10,
                            (1401203, 1, 0, (0, 1000), -1): 10,
                            (1401202, 3, 0, (0, 1000), -1): 10 },
                        2: {
                            (1401206, 1, 0, (0, 1000), -1): 10,
                            (1401203, 1, 0, (0, 1000), -1): 10,
                            (1401202, 3, 0, (0, 1000), -1): 10 },
                        1: {
                            (1401206, 1, 0, (0, 1000), -1): 10,
                            (1401203, 1, 0, (0, 1000), -1): 10,
                            (1401202, 3, 0, (0, 1000), -1): 10 } },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': {
                        (3, 10): [],
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'AIlevelEnhance': 95 } },
            'LayerChoose': {
                1: {
                    LAYER_CHOOSE_CRAFTSMAN: (3, 1, 0, 99, {
                        1: 10,
                        2: 10 }, {
                        1: 1,
                        2: 1 }),
                    LAYER_CHOOSE_SHOP: (1, 1, 1, 99, {
                        1: 10,
                        2: 10 }, {
                        1: 1,
                        2: 1 }),
                    LAYER_CHOOSE_EVENTNPC: (2, 1, 1, 99, {
                        1: 10,
                        2: 10 }, {
                        1: 1,
                        2: 1 }),
                    LAYER_CHOOSE_CHALLENGE: (1, 0, 0, 99, {
                        1: 25,
                        2: 35 }, { }),
                    LAYER_CHOOSE_HIDE: (2, 1, 0, 99, {
                        1: 10,
                        2: 10 }, {
                        1: 1,
                        2: 1 }) },
                2: {
                    LAYER_CHOOSE_CRAFTSMAN: (3, 1, 0, 99, {
                        1: 10,
                        2: 10 }, {
                        1: 1,
                        2: 1 }),
                    LAYER_CHOOSE_SHOP: (1, 1, 1, 99, {
                        1: 10,
                        2: 10 }, {
                        1: 1,
                        2: 1 }),
                    LAYER_CHOOSE_EVENTNPC: (2, 1, 1, 99, {
                        1: 10,
                        2: 10 }, {
                        1: 1,
                        2: 1 }),
                    LAYER_CHOOSE_CHALLENGE: (1, 0, 0, 99, {
                        1: 30,
                        2: 30 }, { }),
                    LAYER_CHOOSE_HIDE: (2, 1, 0, 99, {
                        1: 10,
                        2: 10 }, {
                        1: 1,
                        2: 1 }) },
                3: {
                    LAYER_CHOOSE_S8SHOP: (2, 0, 2, 2, {
                        1: 10,
                        2: 10 }, {
                        1: 1,
                        2: 1 }),
                    LAYER_CHOOSE_S7SHOP: (2, 0, 2, 2, {
                        1: 0,
                        2: 10 }, {
                        1: 0,
                        2: 1 }),
                    LAYER_CHOOSE_DICESHOP: (1, 0, 1, 1, {
                        1: 0,
                        2: 10 }, {
                        1: 0,
                        2: 1 }),
                    LAYER_CHOOSE_WANDSHOP: (2, 0, 2, 2, {
                        1: 0,
                        2: 10 }, {
                        1: 0,
                        2: 1 }),
                    LAYER_CHOOSE_RELICLOTTERY: (1, 0, 1, 1, {
                        1: 10,
                        2: 0 }, {
                        1: 1,
                        2: 0 }),
                    LAYER_CHOOSE_PETSHOP: (2, 0, 2, 2, {
                        1: 10,
                        2: 10 }, {
                        1: 1,
                        2: 1 }),
                    LAYER_CHOOSE_TASKNPC: (0, 0, 0, 0, {
                        1: 10,
                        2: 10 }, {
                        1: 1,
                        2: 1 }),
                    LAYER_CHOOSE_GSCASHSHOP: (0, 0, 0, 0, {
                        1: 10,
                        2: 10 }, {
                        1: 1,
                        2: 1 }),
                    LAYER_CHOOSE_CRAFTSMAN: (3, 1, 0, 99, {
                        1: 10,
                        2: 10 }, {
                        1: 1,
                        2: 1 }),
                    LAYER_CHOOSE_SHOP: (1, 1, 1, 99, {
                        1: 10,
                        2: 10 }, {
                        1: 1,
                        2: 1 }),
                    LAYER_CHOOSE_EVENTNPC: (2, 1, 1, 99, {
                        1: 10,
                        2: 10 }, {
                        1: 1,
                        2: 1 }),
                    LAYER_CHOOSE_CHALLENGE: ((lambda *a: 1 + (Func221(*a) // 8) * 4), 0, 1, 99, {
                        1: 30,
                        2: 30 }, { }),
                    LAYER_CHOOSE_HIDE: (2, 1, 0, 99, {
                        1: 10,
                        2: 10 }, {
                        1: 1,
                        2: 1 }) } },
            'BaseGrade': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: (32, 0),
                        2: (35, 0) },
                    LEVEL_TYPE_FIGHT: {
                        1: (31, 0),
                        2: (34, 0) },
                    LEVEL_TYPE_BOSS: (37, 0),
                    LEVEL_TYPE_HALL: (0, 0) },
                10: {
                    LEVEL_TYPE_HIDE: {
                        1: (35, 0),
                        2: (38, 0) },
                    LEVEL_TYPE_FIGHT: {
                        1: (31, 0),
                        2: (34, 0) },
                    LEVEL_TYPE_BOSS: (37, 0),
                    LEVEL_TYPE_HALL: (0, 0) } },
            'MonsterAttAdjust': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func209(*a) - 1) * 20000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 20000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 20000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                        ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0),
                        ('MoveSpeed', (lambda *a: (Func209(*a) - 1) * 500 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                        ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)] },
                10: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func209(*a) - 1) * 20000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 20000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 20000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                        ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0),
                        ('MoveSpeed', (lambda *a: (Func209(*a) - 1) * 500 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 7000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                        ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)] } },
            'EliteAttAdjust': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                        ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                        ('Toughness', (lambda *a: (Func209(*a) - 1) * 2000 + 0), 0)] },
                10: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 15000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                            ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                            ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func209(*a) - 1) * 11000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 11000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 11000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                        ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func209(*a) - 1) * 11000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ShieldMax', (lambda *a: (Func209(*a) - 1) * 11000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('ArmorMax', (lambda *a: (Func209(*a) - 1) * 11000 * (1 + Func221(*a) // 8) * Func605(*a)), 0),
                        ('Att', (lambda *a: (Func209(*a) - 1) * 2000 * (1 + (Func221(*a) // 8) * 1) + 0), 0),
                        ('Toughness', (lambda *a: 5000 + (Func209(*a) - 1) * 1000 + 0), 0)] } },
            'ItemChoose': 1004 } }
    m_LayerAndLevelMap = { }
    m_ChooseItem = {
        1001: {
            (1, 4): {
                'WeaponChoose': (2, 1, 1001),
                'GoldenCupChoose': (0, 0, 4101),
                'RelicChoose': (0, 0, 0) },
            (1, 3): {
                'WeaponChoose': (1, 1, 1001),
                'GoldenCupChoose': (0, 0, 4101),
                'RelicChoose': (0, 0, 0) },
            (1, 2): {
                'WeaponChoose': (1, 1, 1001),
                'GoldenCupChoose': (0, 0, 4101),
                'RelicChoose': (0, 0, 0) },
            (1, 1): {
                'WeaponChoose': (1, 0, 1001),
                'GoldenCupChoose': (0, 0, 4101),
                'RelicChoose': (0, 0, 0) } },
        1002: {
            (2, 3): {
                'WeaponChoose': (3, 1, 1001),
                'GoldenCupChoose': (0, 0, 4101),
                'RelicChoose': (0, 0, 0) },
            (2, 2): {
                'WeaponChoose': (2, 1, 1001),
                'GoldenCupChoose': (0, 0, 4101),
                'RelicChoose': (0, 0, 0) },
            (2, 1): {
                'WeaponChoose': (2, 1, 1001),
                'GoldenCupChoose': (0, 0, 4101),
                'RelicChoose': (0, 0, 0) } },
        1003: {
            (3, 3): {
                'WeaponChoose': (3, 1, 1001),
                'GoldenCupChoose': (0, 0, 4101),
                'RelicChoose': (0, 0, 0) },
            (3, 2): {
                'WeaponChoose': (2, 1, 1001),
                'GoldenCupChoose': (0, 0, 4101),
                'RelicChoose': (0, 0, 0) },
            (3, 1): {
                'WeaponChoose': (2, 1, 1001),
                'GoldenCupChoose': (0, 0, 4101),
                'RelicChoose': (0, 0, 0) } },
        1004: {
            (4, 2): {
                'WeaponChoose': (2, 1, 1001),
                'GoldenCupChoose': (0, 0, 4101),
                'RelicChoose': (0, 0, 0) },
            (4, 1): {
                'WeaponChoose': (2, 1, 1001),
                'GoldenCupChoose': (0, 0, 4101),
                'RelicChoose': (0, 0, 0) } } }
    m_SightLevelConf = {
        1001: {
            'PFInterval': 100,
            'PFCnt': 1,
            'PosData': {
                2: [
                    3] },
            'Target': {
                1043: {
                    'Speed': [
                        10,
                        11],
                    'Scale': 0.01,
                    'HP': 100,
                    'Weight': 100,
                    'Cnt': [
                        0,
                        1] } } },
        1002: {
            'PFInterval': 80,
            'PFCnt': 1,
            'PosData': {
                11: [
                    1],
                12: [
                    2],
                13: [
                    3] },
            'Target': {
                1043: {
                    'Speed': [
                        4,
                        5],
                    'Scale': 1.5,
                    'HP': 100,
                    'Weight': 100,
                    'Cnt': [
                        5,
                        7] } } },
        1003: {
            'PFInterval': 50,
            'PFCnt': 1,
            'PosData': {
                11: [
                    1],
                12: [
                    2],
                13: [
                    3] },
            'Target': {
                1043: {
                    'Speed': [
                        4,
                        5],
                    'Scale': 1.5,
                    'HP': 100,
                    'Weight': 85,
                    'Cnt': [
                        9,
                        10] } } },
        1004: {
            'PFInterval': 50,
            'PFCnt': 1,
            'PosData': {
                14: [
                    4],
                15: [
                    5],
                16: [
                    6] },
            'Target': {
                1043: {
                    'Speed': [
                        4,
                        5],
                    'Scale': 1.5,
                    'HP': 100,
                    'Weight': 75,
                    'Cnt': [
                        10,
                        11] } } },
        1005: {
            'PFInterval': 100,
            'PFCnt': 2,
            'PosData': {
                14: [
                    4],
                15: [
                    5],
                16: [
                    6] },
            'Target': {
                1043: {
                    'Speed': [
                        4,
                        5],
                    'Scale': 1.5,
                    'HP': 100,
                    'Weight': 75,
                    'Cnt': [
                        12,
                        16] } } },
        1006: {
            'PFInterval': 50,
            'PFCnt': 1,
            'PosData': {
                14: [
                    4],
                15: [
                    5],
                16: [
                    6] },
            'Target': {
                1043: {
                    'Speed': [
                        4,
                        5],
                    'Scale': 1.5,
                    'HP': 100,
                    'Weight': 70,
                    'Cnt': [
                        12,
                        16] } } },
        1007: {
            'PFInterval': 40,
            'PFCnt': 1,
            'PosData': {
                17: [
                    7],
                18: [
                    8],
                19: [
                    9] },
            'Target': {
                1043: {
                    'Speed': [
                        4,
                        5],
                    'Scale': 1.5,
                    'HP': 100,
                    'Weight': 65,
                    'Cnt': [
                        18,
                        20] } } },
        1008: {
            'PFInterval': 50,
            'PFCnt': 1,
            'PosData': {
                17: [
                    7],
                18: [
                    8],
                19: [
                    9] },
            'Target': {
                1043: {
                    'Speed': [
                        4,
                        5],
                    'Scale': 1.5,
                    'HP': 100,
                    'Weight': 60,
                    'Cnt': [
                        18,
                        20] } } },
        1009: {
            'PFInterval': 40,
            'PFCnt': 1,
            'PosData': {
                17: [
                    7],
                18: [
                    8],
                19: [
                    9] },
            'Target': {
                1043: {
                    'Speed': [
                        4,
                        5],
                    'Scale': 1.5,
                    'HP': 100,
                    'Weight': 100,
                    'Cnt': [
                        20,
                        21] } } },
        1010: {
            'PFInterval': 50,
            'PFCnt': 1,
            'PosData': {
                17: [
                    7],
                18: [
                    8],
                19: [
                    9] },
            'Target': {
                1043: {
                    'Speed': [
                        4,
                        5],
                    'Scale': 1.5,
                    'HP': 100,
                    'Weight': 10,
                    'Cnt': [
                        20,
                        21] } } } }


class CWarreport(cl_warmgr.mobject.CElementData):
    pass


class CPVEDieElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'RelifeData': 1001,
        'InitDyingSecond': 16,
        'MinDyingSecond': 4,
        'TimesSubSecond': {
            (3, 10): 3,
            (0, 0): 2 } }


class CWeaponAnalyse(cl_warmgr.mobject.CElementData):
    pass


class CTeamInfoElement(cl_warmgr.mobject.CElementData):
    pass


class CRoundElement(cl_warmgr.mobject.CElementData):
    m_DebuffProp = {
        1: 0,
        2: 0,
        3: 0,
        4: 0 }
    m_Debuff = {
        1110: 10,
        1111: 10,
        1112: 10,
        1113: 10,
        1114: 10,
        1115: 0,
        1116: 0,
        1117: 0,
        1118: 10,
        1119: 10 }
    m_MonsterAttrAdjust = {
        1: { },
        2: {
            'Att': 4000,
            'HPMax': 4000,
            'ArmorMax': 4000,
            'ShieldMax': 4000,
            'MoveSpeed': 1500 },
        3: {
            'Att': 8000,
            'HPMax': 14000,
            'ArmorMax': 14000,
            'ShieldMax': 14000,
            'MoveSpeed': 2500 } }
    m_CycleMonsterAttrAdjust = {
        1: { },
        2: { },
        3: {
            1: {
                (0, 0): {
                    0: {
                        'Att': (lambda *a: max(int(Func201(*a) * -2000 + Func202(*a) * -200 + 5000), 2000)),
                        'HPMax': (lambda *a: min(int(Func201(*a) * 6000 + Func202(*a) * 1000 - 6000), int(16000 + Func544(*a, **{
'sAttr': 'HPMax' })))),
                        'ArmorMax': (lambda *a: min(int(Func201(*a) * 6000 + Func202(*a) * 1000 - 6000), int(16000 + Func544(*a, **{
'sAttr': 'ArmorMax' })))),
                        'ShieldMax': (lambda *a: min(int(Func201(*a) * 6000 + Func202(*a) * 1000 - 6000), int(16000 + Func544(*a, **{
'sAttr': 'ShieldMax' })))),
                        'MoveSpeed': 200 } } },
            2: {
                (0, 0): {
                    0: {
                        'Att': (lambda *a: max(int(Func201(*a) * -4000 + Func202(*a) * -400 + 10000), 4000)),
                        'HPMax': (lambda *a: min(int(Func201(*a) * 12000 + Func202(*a) * 2000 - 12000), int(32000 + Func544(*a, **{
'sAttr': 'HPMax' }) * 2))),
                        'ArmorMax': (lambda *a: min(int(Func201(*a) * 12000 + Func202(*a) * 2000 - 12000), int(32000 + Func544(*a, **{
'sAttr': 'ArmorMax' }) * 2))),
                        'ShieldMax': (lambda *a: min(int(Func201(*a) * 12000 + Func202(*a) * 2000 - 12000), int(32000 + Func544(*a, **{
'sAttr': 'ShieldMax' }) * 2))),
                        'MoveSpeed': 400 } } },
            3: {
                (0, 0): {
                    0: {
                        'Att': (lambda *a: max(int(Func201(*a) * -6000 + Func202(*a) * -600 + 15000), 6000)),
                        'HPMax': (lambda *a: min(int(Func201(*a) * 18000 + Func202(*a) * 3000 - 18000), int(48000 + Func544(*a, **{
'sAttr': 'HPMax' }) * 3))),
                        'ArmorMax': (lambda *a: min(int(Func201(*a) * 18000 + Func202(*a) * 3000 - 18000), int(48000 + Func544(*a, **{
'sAttr': 'ArmorMax' }) * 3))),
                        'ShieldMax': (lambda *a: min(int(Func201(*a) * 18000 + Func202(*a) * 3000 - 18000), int(48000 + Func544(*a, **{
'sAttr': 'ShieldMax' }) * 3))),
                        'MoveSpeed': 600 } } },
            4: {
                (0, 0): {
                    0: {
                        'Att': (lambda *a: max(int(Func201(*a) * -8000 + Func202(*a) * -800 + 20000), 8000)),
                        'HPMax': (lambda *a: min(int(Func201(*a) * 24000 + Func202(*a) * 4000 - 24000), int(64000 + Func544(*a, **{
'sAttr': 'HPMax' }) * 4))),
                        'ArmorMax': (lambda *a: min(int(Func201(*a) * 24000 + Func202(*a) * 4000 - 24000), int(64000 + Func544(*a, **{
'sAttr': 'ArmorMax' }) * 4))),
                        'ShieldMax': (lambda *a: min(int(Func201(*a) * 24000 + Func202(*a) * 4000 - 24000), int(64000 + Func544(*a, **{
'sAttr': 'ShieldMax' }) * 4))),
                        'MoveSpeed': 800 } } },
            5: {
                (0, 0): {
                    0: {
                        'Att': (lambda *a: max(int(Func201(*a) * -10000 + Func202(*a) * -1000 + 25000), 10000)),
                        'HPMax': (lambda *a: min(int(Func201(*a) * 30000 + Func202(*a) * 5000 - 30000), int(80000 + Func544(*a, **{
'sAttr': 'HPMax' }) * 5))),
                        'ArmorMax': (lambda *a: min(int(Func201(*a) * 30000 + Func202(*a) * 5000 - 30000), int(80000 + Func544(*a, **{
'sAttr': 'ArmorMax' }) * 5))),
                        'ShieldMax': (lambda *a: min(int(Func201(*a) * 30000 + Func202(*a) * 5000 - 30000), int(80000 + Func544(*a, **{
'sAttr': 'ShieldMax' }) * 5))),
                        'MoveSpeed': 1000 } } },
            6: {
                (0, 0): {
                    0: {
                        'Att': (lambda *a: max(int(Func201(*a) * -12000 + Func202(*a) * -1200 + 30000), 12000)),
                        'HPMax': (lambda *a: min(int(Func201(*a) * 36000 + Func202(*a) * 6000 - 36000), int(96000 + Func544(*a, **{
'sAttr': 'HPMax' }) * 6))),
                        'ArmorMax': (lambda *a: min(int(Func201(*a) * 36000 + Func202(*a) * 6000 - 36000), int(96000 + Func544(*a, **{
'sAttr': 'ArmorMax' }) * 6))),
                        'ShieldMax': (lambda *a: min(int(Func201(*a) * 36000 + Func202(*a) * 6000 - 36000), int(96000 + Func544(*a, **{
'sAttr': 'ShieldMax' }) * 6))),
                        'MoveSpeed': 1200 } } },
            7: {
                (0, 0): {
                    0: {
                        'Att': (lambda *a: max(int(Func201(*a) * -14000 + Func202(*a) * -1400 + 35000), 14000)),
                        'HPMax': (lambda *a: min(int(Func201(*a) * 42000 + Func202(*a) * 7000 - 42000), int(112000 + Func544(*a, **{
'sAttr': 'HPMax' }) * 7))),
                        'ArmorMax': (lambda *a: min(int(Func201(*a) * 42000 + Func202(*a) * 7000 - 42000), int(112000 + Func544(*a, **{
'sAttr': 'ArmorMax' }) * 7))),
                        'ShieldMax': (lambda *a: min(int(Func201(*a) * 42000 + Func202(*a) * 7000 - 42000), int(112000 + Func544(*a, **{
'sAttr': 'ShieldMax' }) * 7))),
                        'MoveSpeed': 1400 } } },
            8: {
                (0, 0): {
                    0: {
                        'Att': (lambda *a: max(int(Func201(*a) * -14000 + Func202(*a) * -1400 + 35000), 14000)),
                        'HPMax': (lambda *a: min(int(Func201(*a) * 42000 + Func202(*a) * 7000 - 42000), int(112000 + Func544(*a, **{
'sAttr': 'HPMax' }) * 7))),
                        'ArmorMax': (lambda *a: min(int(Func201(*a) * 42000 + Func202(*a) * 7000 - 42000), int(112000 + Func544(*a, **{
'sAttr': 'ArmorMax' }) * 7))),
                        'ShieldMax': (lambda *a: min(int(Func201(*a) * 42000 + Func202(*a) * 7000 - 42000), int(112000 + Func544(*a, **{
'sAttr': 'ShieldMax' }) * 7))),
                        'MoveSpeed': 1400 } } },
            9: {
                (0, 0): {
                    0: {
                        'Att': (lambda *a: max(int(Func201(*a) * -14000 + Func202(*a) * -1400 + 35000), 14000)),
                        'HPMax': (lambda *a: min(int(Func201(*a) * 42000 + Func202(*a) * 7000 - 42000), int(112000 + Func544(*a, **{
'sAttr': 'HPMax' }) * 7))),
                        'ArmorMax': (lambda *a: min(int(Func201(*a) * 42000 + Func202(*a) * 7000 - 42000), int(112000 + Func544(*a, **{
'sAttr': 'ArmorMax' }) * 7))),
                        'ShieldMax': (lambda *a: min(int(Func201(*a) * 42000 + Func202(*a) * 7000 - 42000), int(112000 + Func544(*a, **{
'sAttr': 'ShieldMax' }) * 7))),
                        'MoveSpeed': 1400 } } },
            10: {
                (2, 1): {
                    0: {
                        'Att': (lambda *a: max(int(Func201(*a) * -14000 + Func202(*a) * -1400 + 35000), 14000)),
                        'HPMax': (lambda *a: min(int((0.6 + 0.42 * (Func201(*a) - 2) + 0.07 * Func202(*a)) * 85000 * 1.17 ** min(Func244(*a) + Func245(*a) - 5, 11)), int(410000 + Func544(*a, **{
'sAttr': 'HPMax' }) * 70))),
                        'ArmorMax': (lambda *a: min(int((0.6 + 0.42 * (Func201(*a) - 2) + 0.07 * Func202(*a)) * 85000 * 1.17 ** min(Func244(*a) + Func245(*a) - 5, 11)), int(410000 + Func544(*a, **{
'sAttr': 'HPMax' }) * 70))),
                        'ShieldMax': (lambda *a: min(int((0.6 + 0.42 * (Func201(*a) - 2) + 0.07 * Func202(*a)) * 85000 * 1.17 ** min(Func244(*a) + Func245(*a) - 5, 11)), int(410000 + Func544(*a, **{
'sAttr': 'HPMax' }) * 70))),
                        'MoveSpeed': 1400 },
                    1: {
                        'HPMax': (lambda *a: min(int((0.6 + 0.48 * (Func201(*a) - 2) + 0.07 * Func202(*a)) * 100000 * 1.18 ** min(Func244(*a) + Func245(*a) - 5, 11)), int(530000 + Func544(*a, **{
'sAttr': 'HPMax' }) * 100))),
                        'ArmorMax': (lambda *a: min(int((0.6 + 0.48 * (Func201(*a) - 2) + 0.07 * Func202(*a)) * 100000 * 1.18 ** min(Func244(*a) + Func245(*a) - 5, 11)), int(530000 + Func544(*a, **{
'sAttr': 'HPMax' }) * 100))),
                        'ShieldMax': (lambda *a: min(int((0.6 + 0.48 * (Func201(*a) - 2) + 0.07 * Func202(*a)) * 100000 * 1.18 ** min(Func244(*a) + Func245(*a) - 5, 11)), int(530000 + Func544(*a, **{
'sAttr': 'HPMax' }) * 100))) },
                    3: {
                        'HPMax': (lambda *a: min(int((0.6 + 0.5 * (Func201(*a) - 2) + 0.06 * Func202(*a)) * 75000 * 1.16 ** min(Func244(*a) + Func245(*a) - 5, 11)), int(350000 + Func544(*a, **{
'sAttr': 'HPMax' }) * 60))),
                        'ArmorMax': (lambda *a: min(int((0.6 + 0.5 * (Func201(*a) - 2) + 0.06 * Func202(*a)) * 75000 * 1.16 ** min(Func244(*a) + Func245(*a) - 5, 11)), int(350000 + Func544(*a, **{
'sAttr': 'HPMax' }) * 60))),
                        'ShieldMax': (lambda *a: min(int((0.6 + 0.5 * (Func201(*a) - 2) + 0.06 * Func202(*a)) * 75000 * 1.16 ** min(Func244(*a) + Func245(*a) - 5, 11)), int(350000 + Func544(*a, **{
'sAttr': 'HPMax' }) * 60))) } },
                (0, 0): {
                    0: {
                        'Att': (lambda *a: max(int(Func201(*a) * -14000 + Func202(*a) * -1400 + 35000), 14000)),
                        'HPMax': (lambda *a: min(int(Func201(*a) * 42000 + Func202(*a) * 7000 - 42000), int(112000 + Func544(*a, **{
'sAttr': 'HPMax' }) * 7))),
                        'ArmorMax': (lambda *a: min(int(Func201(*a) * 42000 + Func202(*a) * 7000 - 42000), int(112000 + Func544(*a, **{
'sAttr': 'ArmorMax' }) * 7))),
                        'ShieldMax': (lambda *a: min(int(Func201(*a) * 42000 + Func202(*a) * 7000 - 42000), int(112000 + Func544(*a, **{
'sAttr': 'ShieldMax' }) * 7))),
                        'MoveSpeed': 1400 } } } } }
    m_ModeMonsterAttrAdjust = {
        1: { },
        2: { },
        3: {
            MODE_SNOWMOUNTAINS: {
                'HPMax': 6000,
                'ArmorMax': 6000,
                'ShieldMax': 6000 } } }
    m_CycleMonsterRewardAdjust = {
        3: {
            1: {
                501: 500 },
            2: {
                501: 1000 },
            3: {
                501: 1500 },
            4: {
                501: 2000 },
            5: {
                501: 2500 },
            6: {
                501: 3000 },
            7: {
                501: 3500 },
            8: {
                501: 4000 },
            9: {
                501: 4000 } } }
    m_ExtRule = {
        (3, 10): {
            ROUND_EXTRULE_REPLACECONFIG_CHALLENGE: {
                2: {
                    1148: 1,
                    1151: 1 },
                3: {
                    1149: 1,
                    1158: 1 },
                4: {
                    1150: 1 } },
            ROUND_EXTRULE_APPEARCHALLENGE: {
                ENDLESS_REAL: {
                    1: 1135,
                    2: 1136,
                    3: 1137,
                    4: 1138 },
                ENDLESS_TIME: {
                    1: 1131,
                    2: 1132,
                    3: 1133,
                    4: 1134 },
                'Default': {
                    2: 1113,
                    3: 1114,
                    4: 1115 } },
            ROUND_EXTRULE_REPLACEMONSTER: {
                20041: 30041,
                20042: 30041,
                20031: 30041 } },
        (0, 0): {
            ROUND_EXTRULE_TRANSOBSTACLE_TO_MONSTER: {
                1215: {
                    'TransRatio': 30,
                    'MonsterSID': 20061 } },
            ROUND_EXTRULE_SMASHOBSTACLE_CREATEMONSTER_LOCKROOM: { } },
        (3, 9): {
            ROUND_EXTRULE_REPLACECONFIG_CHALLENGE: {
                2: {
                    1116: 1,
                    1146: 1 },
                3: {
                    1117: 1,
                    1157: 1 },
                4: {
                    1118: 1 } },
            ROUND_EXTRULE_APPEARCHALLENGE: {
                ENDLESS_REAL: {
                    1: 1135,
                    2: 1136,
                    3: 1137,
                    4: 1138 },
                ENDLESS_TIME: {
                    1: 1131,
                    2: 1132,
                    3: 1133,
                    4: 1134 },
                'Default': {
                    2: 1113,
                    3: 1114,
                    4: 1115 } },
            ROUND_EXTRULE_REPLACEMONSTER: {
                20041: 30041,
                20042: 30041,
                20031: 30041 } } }
    m_Config = {
        'CycleGSCashRelief': (lambda *a: 100 - (10 - Func221(*a)) * 5),
        'MonsterRecvDamAdjust': {
            (3, 10): {
                1: {
                    2: -1500,
                    3: -2500,
                    4: -3500 },
                2: {
                    3: -1000,
                    4: -2000 } } },
        'BendShopNpc': 1053,
        'SleepBendShopNpc': 1062,
        'SleepBendShopLayer': 4 }


class CMonsterSuperElement(cl_warmgr.mobject.CElementData):
    m_SuperConfig = {
        MODE_REAL_ENDLESS: {
            LEVEL_TYPE_HIDE: {
                1: {
                    'ChooseRatio': (lambda *a: max(int((Func221(*a) + 1) / 3), 1) * 15 + 15),
                    'LevelConfig': {
                        1: {
                            'LevelLimit': 8,
                            'LevelLive': (lambda *a: (Func221(*a) - 1) / 4 + 2),
                            'RoomLimit': (lambda *a: Func221(*a) / 8 + 5),
                            'RoomLive': (lambda *a: (Func221(*a) - 1) / 4 + 2) },
                        2: {
                            'LevelLimit': 8,
                            'LevelLive': (lambda *a: (Func221(*a) - 1) / 4 + 2),
                            'RoomLimit': (lambda *a: Func221(*a) / 8 + 5),
                            'RoomLive': (lambda *a: (Func221(*a) - 1) / 4 + 2) },
                        3: {
                            'LevelLimit': 8,
                            'LevelLive': (lambda *a: (Func221(*a) - 1) / 4 + 2),
                            'RoomLimit': (lambda *a: Func221(*a) / 8 + 5),
                            'RoomLive': (lambda *a: (Func221(*a) - 1) / 4 + 2) },
                        4: {
                            'LevelLimit': 8,
                            'LevelLive': (lambda *a: (Func221(*a) - 1) / 4 + 2),
                            'RoomLimit': (lambda *a: Func221(*a) / 8 + 5),
                            'RoomLive': (lambda *a: (Func221(*a) - 1) / 4 + 2) } },
                    'SuperLevel': 0 },
                2: {
                    'ChooseRatio': (lambda *a: max(int((Func221(*a) + 1) / 3), 1) * 15 + 15),
                    'LevelConfig': {
                        1: {
                            'LevelLimit': 8,
                            'LevelLive': (lambda *a: (Func221(*a) - 1) / 4 + 2),
                            'RoomLimit': (lambda *a: Func221(*a) / 8 + 5),
                            'RoomLive': (lambda *a: (Func221(*a) - 1) / 4 + 2) },
                        2: {
                            'LevelLimit': 8,
                            'LevelLive': (lambda *a: (Func221(*a) - 1) / 4 + 2),
                            'RoomLimit': (lambda *a: Func221(*a) / 8 + 5),
                            'RoomLive': (lambda *a: (Func221(*a) - 1) / 4 + 2) },
                        3: {
                            'LevelLimit': 8,
                            'LevelLive': (lambda *a: (Func221(*a) - 1) / 4 + 2),
                            'RoomLimit': (lambda *a: Func221(*a) / 8 + 5),
                            'RoomLive': (lambda *a: (Func221(*a) - 1) / 4 + 2) } },
                    'SuperLevel': 0 },
                3: {
                    'ChooseRatio': (lambda *a: max(int((Func221(*a) + 1) / 3), 1) * 15 + 15),
                    'LevelConfig': {
                        1: {
                            'LevelLimit': 8,
                            'LevelLive': (lambda *a: (Func221(*a) - 1) / 4 + 2),
                            'RoomLimit': (lambda *a: Func221(*a) / 8 + 5),
                            'RoomLive': (lambda *a: (Func221(*a) - 1) / 4 + 2) },
                        2: {
                            'LevelLimit': 8,
                            'LevelLive': (lambda *a: (Func221(*a) - 1) / 4 + 2),
                            'RoomLimit': (lambda *a: Func221(*a) / 8 + 5),
                            'RoomLive': (lambda *a: (Func221(*a) - 1) / 4 + 2) },
                        3: {
                            'LevelLimit': 8,
                            'LevelLive': (lambda *a: (Func221(*a) - 1) / 4 + 2),
                            'RoomLimit': (lambda *a: Func221(*a) / 8 + 5),
                            'RoomLive': (lambda *a: (Func221(*a) - 1) / 4 + 2) } },
                    'SuperLevel': 0 },
                4: {
                    'ChooseRatio': (lambda *a: max(int((Func221(*a) + 1) / 3), 1) * 15 + 15),
                    'LevelConfig': {
                        1: {
                            'LevelLimit': 8,
                            'LevelLive': (lambda *a: (Func221(*a) - 1) / 4 + 2),
                            'RoomLimit': (lambda *a: Func221(*a) / 8 + 5),
                            'RoomLive': (lambda *a: (Func221(*a) - 1) / 4 + 2) },
                        2: {
                            'LevelLimit': 8,
                            'LevelLive': (lambda *a: (Func221(*a) - 1) / 4 + 2),
                            'RoomLimit': (lambda *a: Func221(*a) / 8 + 5),
                            'RoomLive': (lambda *a: (Func221(*a) - 1) / 4 + 2) } },
                    'SuperLevel': 0 } },
            LEVEL_TYPE_FIGHT: {
                1: {
                    'ChooseRatio': (lambda *a: min(int((Func205(*a) - 1) * Func205(*a) * 25), int(Func205(*a) * 25))),
                    'LevelConfig': {
                        1: {
                            'LevelLimit': (lambda *a: Func205(*a) * 3 + 19),
                            'LevelLive': (lambda *a: Func205(*a) / 2 + 4),
                            'RoomLimit': (lambda *a: Func205(*a) + 5),
                            'RoomLive': (lambda *a: Func205(*a) / 2 + 2) },
                        2: {
                            'LevelLimit': (lambda *a: Func205(*a) * 3 + 19),
                            'LevelLive': (lambda *a: Func205(*a) / 2 + 4),
                            'RoomLimit': (lambda *a: Func205(*a) + 5),
                            'RoomLive': (lambda *a: Func205(*a) / 2 + 2) },
                        3: {
                            'LevelLimit': (lambda *a: Func205(*a) * 3 + 19),
                            'LevelLive': (lambda *a: Func205(*a) / 2 + 4),
                            'RoomLimit': (lambda *a: Func205(*a) + 5),
                            'RoomLive': (lambda *a: Func205(*a) / 2 + 2) },
                        4: {
                            'LevelLimit': (lambda *a: Func205(*a) * 3 + 19),
                            'LevelLive': (lambda *a: Func205(*a) / 2 + 4),
                            'RoomLimit': (lambda *a: Func205(*a) + 5),
                            'RoomLive': (lambda *a: Func205(*a) / 2 + 2) } },
                    'SuperLevel': 0 },
                2: {
                    'ChooseRatio': (lambda *a: min(int((Func205(*a) - 1) * Func205(*a) * 25), int(Func205(*a) * 25))),
                    'LevelConfig': {
                        1: {
                            'LevelLimit': (lambda *a: Func205(*a) * 3 + 19),
                            'LevelLive': (lambda *a: Func205(*a) / 2 + 4),
                            'RoomLimit': (lambda *a: Func205(*a) + 5),
                            'RoomLive': (lambda *a: Func205(*a) / 2 + 2) },
                        2: {
                            'LevelLimit': (lambda *a: Func205(*a) * 3 + 19),
                            'LevelLive': (lambda *a: Func205(*a) / 2 + 4),
                            'RoomLimit': (lambda *a: Func205(*a) + 5),
                            'RoomLive': (lambda *a: Func205(*a) / 2 + 2) },
                        3: {
                            'LevelLimit': (lambda *a: Func205(*a) * 3 + 19),
                            'LevelLive': (lambda *a: Func205(*a) / 2 + 4),
                            'RoomLimit': (lambda *a: Func205(*a) + 5),
                            'RoomLive': (lambda *a: Func205(*a) / 2 + 2) } },
                    'SuperLevel': 0 },
                3: {
                    'ChooseRatio': (lambda *a: min(int((Func205(*a) - 1) * Func205(*a) * 25), int(Func205(*a) * 25))),
                    'LevelConfig': {
                        1: {
                            'LevelLimit': (lambda *a: Func205(*a) * 3 + 19),
                            'LevelLive': (lambda *a: Func205(*a) / 2 + 4),
                            'RoomLimit': (lambda *a: Func205(*a) + 5),
                            'RoomLive': (lambda *a: Func205(*a) / 2 + 2) },
                        2: {
                            'LevelLimit': (lambda *a: Func205(*a) * 3 + 19),
                            'LevelLive': (lambda *a: Func205(*a) / 2 + 4),
                            'RoomLimit': (lambda *a: Func205(*a) + 5),
                            'RoomLive': (lambda *a: Func205(*a) / 2 + 2) },
                        3: {
                            'LevelLimit': (lambda *a: Func205(*a) * 3 + 19),
                            'LevelLive': (lambda *a: Func205(*a) / 2 + 4),
                            'RoomLimit': (lambda *a: Func205(*a) + 5),
                            'RoomLive': (lambda *a: Func205(*a) / 2 + 2) } },
                    'SuperLevel': 0 },
                4: {
                    'ChooseRatio': (lambda *a: min(int((Func205(*a) - 1) * Func205(*a) * 25), int(Func205(*a) * 25))),
                    'LevelConfig': {
                        1: {
                            'LevelLimit': (lambda *a: Func205(*a) * 3 + 19),
                            'LevelLive': (lambda *a: Func205(*a) / 2 + 4),
                            'RoomLimit': (lambda *a: Func205(*a) + 5),
                            'RoomLive': (lambda *a: Func205(*a) / 2 + 2) },
                        2: {
                            'LevelLimit': (lambda *a: Func205(*a) * 3 + 19),
                            'LevelLive': (lambda *a: Func205(*a) / 2 + 4),
                            'RoomLimit': (lambda *a: Func205(*a) + 5),
                            'RoomLive': (lambda *a: Func205(*a) / 2 + 2) } },
                    'SuperLevel': 0 } } },
        'Default': {
            LEVEL_TYPE_HIDE: {
                1: {
                    'ChooseRatio': (lambda *a: max(int((Func221(*a) + 1) / 3), 1) * 15 + 15),
                    'LevelConfig': {
                        1: {
                            'LevelLimit': 8,
                            'LevelLive': (lambda *a: (Func221(*a) - 1) / 4 + 2),
                            'RoomLimit': (lambda *a: Func221(*a) / 8 + 5),
                            'RoomLive': (lambda *a: (Func221(*a) - 1) / 4 + 2) },
                        2: {
                            'LevelLimit': 8,
                            'LevelLive': (lambda *a: (Func221(*a) - 1) / 4 + 2),
                            'RoomLimit': (lambda *a: Func221(*a) / 8 + 5),
                            'RoomLive': (lambda *a: (Func221(*a) - 1) / 4 + 2) },
                        3: {
                            'LevelLimit': 8,
                            'LevelLive': (lambda *a: (Func221(*a) - 1) / 4 + 2),
                            'RoomLimit': (lambda *a: Func221(*a) / 8 + 5),
                            'RoomLive': (lambda *a: (Func221(*a) - 1) / 4 + 2) },
                        4: {
                            'LevelLimit': 8,
                            'LevelLive': (lambda *a: (Func221(*a) - 1) / 4 + 2),
                            'RoomLimit': (lambda *a: Func221(*a) / 8 + 5),
                            'RoomLive': (lambda *a: (Func221(*a) - 1) / 4 + 2) } },
                    'SuperLevel': 0 },
                2: {
                    'ChooseRatio': (lambda *a: max(int((Func221(*a) + 1) / 3), 1) * 15 + 15),
                    'LevelConfig': {
                        1: {
                            'LevelLimit': 8,
                            'LevelLive': (lambda *a: (Func221(*a) - 1) / 4 + 2),
                            'RoomLimit': (lambda *a: Func221(*a) / 8 + 5),
                            'RoomLive': (lambda *a: (Func221(*a) - 1) / 4 + 2) },
                        2: {
                            'LevelLimit': 8,
                            'LevelLive': (lambda *a: (Func221(*a) - 1) / 4 + 2),
                            'RoomLimit': (lambda *a: Func221(*a) / 8 + 5),
                            'RoomLive': (lambda *a: (Func221(*a) - 1) / 4 + 2) },
                        3: {
                            'LevelLimit': 8,
                            'LevelLive': (lambda *a: (Func221(*a) - 1) / 4 + 2),
                            'RoomLimit': (lambda *a: Func221(*a) / 8 + 5),
                            'RoomLive': (lambda *a: (Func221(*a) - 1) / 4 + 2) } },
                    'SuperLevel': 0 },
                3: {
                    'ChooseRatio': (lambda *a: max(int((Func221(*a) + 1) / 3), 1) * 15 + 15),
                    'LevelConfig': {
                        1: {
                            'LevelLimit': 8,
                            'LevelLive': (lambda *a: (Func221(*a) - 1) / 4 + 2),
                            'RoomLimit': (lambda *a: Func221(*a) / 8 + 5),
                            'RoomLive': (lambda *a: (Func221(*a) - 1) / 4 + 2) },
                        2: {
                            'LevelLimit': 8,
                            'LevelLive': (lambda *a: (Func221(*a) - 1) / 4 + 2),
                            'RoomLimit': (lambda *a: Func221(*a) / 8 + 5),
                            'RoomLive': (lambda *a: (Func221(*a) - 1) / 4 + 2) },
                        3: {
                            'LevelLimit': 8,
                            'LevelLive': (lambda *a: (Func221(*a) - 1) / 4 + 2),
                            'RoomLimit': (lambda *a: Func221(*a) / 8 + 5),
                            'RoomLive': (lambda *a: (Func221(*a) - 1) / 4 + 2) } },
                    'SuperLevel': 0 },
                4: {
                    'ChooseRatio': (lambda *a: max(int((Func221(*a) + 1) / 3), 1) * 15 + 15),
                    'LevelConfig': {
                        1: {
                            'LevelLimit': 8,
                            'LevelLive': (lambda *a: (Func221(*a) - 1) / 4 + 2),
                            'RoomLimit': (lambda *a: Func221(*a) / 8 + 5),
                            'RoomLive': (lambda *a: (Func221(*a) - 1) / 4 + 2) },
                        2: {
                            'LevelLimit': 8,
                            'LevelLive': (lambda *a: (Func221(*a) - 1) / 4 + 2),
                            'RoomLimit': (lambda *a: Func221(*a) / 8 + 5),
                            'RoomLive': (lambda *a: (Func221(*a) - 1) / 4 + 2) } },
                    'SuperLevel': 0 } },
            LEVEL_TYPE_FIGHT: {
                1: {
                    'ChooseRatio': (lambda *a: min(int((Func205(*a) - 1) * Func205(*a) * 25), int(Func205(*a) * 25))),
                    'LevelConfig': {
                        1: {
                            'LevelLimit': (lambda *a: Func205(*a) * 3 - 3),
                            'LevelLive': (lambda *a: Func205(*a) / 2 + 0),
                            'RoomLimit': (lambda *a: Func205(*a) - 1),
                            'RoomLive': (lambda *a: Func205(*a) / 2 + 0) },
                        2: {
                            'LevelLimit': (lambda *a: Func205(*a) * 3 - 1),
                            'LevelLive': (lambda *a: Func205(*a) / 2 + 0),
                            'RoomLimit': (lambda *a: Func205(*a) + 0),
                            'RoomLive': (lambda *a: Func205(*a) / 2 + 0) },
                        3: {
                            'LevelLimit': (lambda *a: Func205(*a) * 3 + 1),
                            'LevelLive': (lambda *a: Func205(*a) / 2 + 1),
                            'RoomLimit': (lambda *a: Func205(*a) + 1),
                            'RoomLive': (lambda *a: Func205(*a) / 2 + 1) },
                        4: {
                            'LevelLimit': (lambda *a: Func205(*a) * 3 + 3),
                            'LevelLive': (lambda *a: Func205(*a) / 2 + 1),
                            'RoomLimit': (lambda *a: Func205(*a) + 1),
                            'RoomLive': (lambda *a: Func205(*a) / 2 + 1) } },
                    'SuperLevel': 0 },
                2: {
                    'ChooseRatio': (lambda *a: min(int((Func205(*a) - 1) * Func205(*a) * 25), int(Func205(*a) * 25))),
                    'LevelConfig': {
                        1: {
                            'LevelLimit': (lambda *a: Func205(*a) * 3 + 5),
                            'LevelLive': (lambda *a: Func205(*a) / 2 + 1),
                            'RoomLimit': (lambda *a: Func205(*a) + 2),
                            'RoomLive': (lambda *a: Func205(*a) / 2 + 1) },
                        2: {
                            'LevelLimit': (lambda *a: Func205(*a) * 3 + 7),
                            'LevelLive': (lambda *a: Func205(*a) / 2 + 1),
                            'RoomLimit': (lambda *a: Func205(*a) + 2),
                            'RoomLive': (lambda *a: Func205(*a) / 2 + 1) },
                        3: {
                            'LevelLimit': (lambda *a: Func205(*a) * 3 + 9),
                            'LevelLive': (lambda *a: Func205(*a) / 2 + 2),
                            'RoomLimit': (lambda *a: Func205(*a) + 3),
                            'RoomLive': (lambda *a: Func205(*a) / 2 + 2) } },
                    'SuperLevel': 0 },
                3: {
                    'ChooseRatio': (lambda *a: min(int((Func205(*a) - 1) * Func205(*a) * 25), int(Func205(*a) * 25))),
                    'LevelConfig': {
                        1: {
                            'LevelLimit': (lambda *a: Func205(*a) * 3 + 11),
                            'LevelLive': (lambda *a: Func205(*a) / 2 + 2),
                            'RoomLimit': (lambda *a: Func205(*a) + 4),
                            'RoomLive': (lambda *a: Func205(*a) / 2 + 2) },
                        2: {
                            'LevelLimit': (lambda *a: Func205(*a) * 3 + 13),
                            'LevelLive': (lambda *a: Func205(*a) / 2 + 2),
                            'RoomLimit': (lambda *a: Func205(*a) + 4),
                            'RoomLive': (lambda *a: Func205(*a) / 2 + 2) },
                        3: {
                            'LevelLimit': (lambda *a: Func205(*a) * 3 + 15),
                            'LevelLive': (lambda *a: Func205(*a) / 2 + 3),
                            'RoomLimit': (lambda *a: Func205(*a) + 5),
                            'RoomLive': (lambda *a: Func205(*a) / 2 + 3) } },
                    'SuperLevel': 0 },
                4: {
                    'ChooseRatio': (lambda *a: min(int((Func205(*a) - 1) * Func205(*a) * 25), int(Func205(*a) * 25))),
                    'LevelConfig': {
                        1: {
                            'LevelLimit': (lambda *a: Func205(*a) * 3 + 17),
                            'LevelLive': (lambda *a: Func205(*a) / 2 + 4),
                            'RoomLimit': (lambda *a: Func205(*a) + 5),
                            'RoomLive': (lambda *a: Func205(*a) / 2 + 2) },
                        2: {
                            'LevelLimit': (lambda *a: Func205(*a) * 3 + 19),
                            'LevelLive': (lambda *a: Func205(*a) / 2 + 4),
                            'RoomLimit': (lambda *a: Func205(*a) + 5),
                            'RoomLive': (lambda *a: Func205(*a) / 2 + 2) } },
                    'SuperLevel': 0 } } } }
    m_AffixConfig = {
        MODE_REAL_ENDLESS: {
            LEVEL_TYPE_HIDE: {
                (3, 8): {
                    6114: WARRIOR_ELITE },
                (3, 7): {
                    6114: WARRIOR_ELITE },
                (3, 6): {
                    6114: WARRIOR_ELITE },
                (3, 5): {
                    6114: WARRIOR_ELITE },
                (3, 4): {
                    6101: 0,
                    6102: 0,
                    6103: 0,
                    6107: 0,
                    6114: WARRIOR_ELITE },
                (3, 3): {
                    6101: 0,
                    6102: 0,
                    6103: 0,
                    6107: 0,
                    6114: WARRIOR_ELITE },
                (3, 2): {
                    6101: 0,
                    6102: 0,
                    6103: 0,
                    6107: 0,
                    6114: WARRIOR_ELITE },
                (3, 1): {
                    6101: 0,
                    6102: 0,
                    6103: 0,
                    6107: 0,
                    6114: WARRIOR_ELITE } },
            LEVEL_TYPE_FIGHT: { } },
        'Default': {
            LEVEL_TYPE_HIDE: {
                (3, 8): {
                    6114: WARRIOR_ELITE },
                (3, 7): {
                    6114: WARRIOR_ELITE },
                (3, 6): {
                    6114: WARRIOR_ELITE },
                (3, 5): {
                    6114: WARRIOR_ELITE },
                (3, 4): {
                    6101: 0,
                    6102: 0,
                    6103: 0,
                    6107: 0,
                    6114: WARRIOR_ELITE },
                (3, 3): {
                    6101: 0,
                    6102: 0,
                    6103: 0,
                    6107: 0,
                    6114: WARRIOR_ELITE },
                (3, 2): {
                    6101: 0,
                    6102: 0,
                    6103: 0,
                    6107: 0,
                    6114: WARRIOR_ELITE },
                (3, 1): {
                    6101: 0,
                    6102: 0,
                    6103: 0,
                    6107: 0,
                    6114: WARRIOR_ELITE } },
            LEVEL_TYPE_FIGHT: { } } }


class CWatchElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'WatchPF': 1502,
        'RelifeNeedGoalRoomNum': 1,
        'RelifeCost': (lambda *a: min(5000, 20 * (1 + (min(4, Func201(*a)) - 1) * 0.1 + (Func202(*a) - 1) * 0.02 + (Func205(*a) - 1) * 0.4) * 2.5 ** Func766(*a) * Func678(*a) / 100)) }


class CSaveElement(cl_warmgr.mobject.CElementData):
    pass


class CBigDataAnalyseMgr(cl_warmgr.mobject.CElementData):
    pass


class CTeamSaveElement(cl_warmgr.mobject.CElementData):
    pass


class CSignalElement(cl_warmgr.mobject.CElementData):
    pass


class CRescueElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'm_HaltInfo': {
            103: 1,
            108: 1,
            321: 0,
            323: 1,
            322: 1,
            40108: 1,
            30108: 1,
            10108: 1,
            50108: 1,
            10149: 0,
            20149: 0,
            143: 0,
            198: 0 },
        'm_IgnoreHalt': [
            1323,
            9214,
            1019,
            1021,
            1018,
            1017,
            12013,
            9703,
            9793,
            1024] }


class CRecycleDropElement(cl_warmgr.mobject.CElementData):
    pass


class CCheckCheatElement(cl_warmgr.mobject.CElementData):
    pass


class CHangUpKickElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'TOTALTIME': 120000,
        'CHECKTIME': 2000 }


class CSuitElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'LimiteBene': {
            13723: 10 },
        'LimitBeneLayer': (2, 3, 4) }


class CSnowMountainElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'ELITE': (31642, 33811),
        'REPLACENPC': {
            1062: 1053 },
        'EXTRACHALLENGE': {
            1: {
                1088: 1,
                1110: 1 },
            2: {
                1089: 1,
                1147: 1 },
            3: {
                1090: 1,
                1157: 1 },
            4: {
                1091: 1 } } }


class CRidingAloneElement(cl_warmgr.mobject.CElementData):
    pass


class CMonsterRelicElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'PlayerChooseCnt': {
            1: {
                'Master': 4,
                'Member': 0 },
            2: {
                'Master': 2,
                'Member': 2 },
            3: {
                'Master': 2,
                'Member': 1 },
            4: {
                'Master': 1,
                'Member': 1 } },
        'MonsterUseRelicCnt': {
            2: {
                'Normal': 1,
                'Super': 2,
                'Elite': 3,
                'Boss': 0 },
            3: {
                'Normal': 2,
                'Super': 3,
                'Elite': 4,
                'Boss': 0 },
            4: {
                'Normal': 3,
                'Super': 4,
                'Elite': 5,
                'Boss': 0 } },
        'QualityWeight': {
            2: {
                1: 166,
                2: 157,
                4: 45,
                8: 18 },
            3: {
                1: 159,
                2: 159,
                4: 48,
                8: 48 },
            4: {
                1: 152,
                2: 161,
                4: 51,
                8: 78 } },
        'RelicMG': 2420,
        'EndlessConfigLayer': 4,
        'AssignMonsterType': {
            3165: 'Elite' },
        'DropProbability': {
            'Normal': 200,
            'Elite': 1000 },
        'SeasonExtMonRelicCnt': { },
        'DropWeight': [
            30,
            10],
        'Version': 2,
        'FloorDropCnt': 60,
        'TotalOptionCnt': 12,
        'OptionCnt': 3,
        'OptionalCnt': 2,
        'LevelDropLimit': {
            (4, 1): 2,
            (3, 1): 2,
            (2, 1): 2 },
        'DelayPickTime': 500,
        'KillDropSeason': [
            4],
        'KillDropCycle': [] }


class CRollRelicElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'RelicDrop': {
            1: 2414,
            2: 2415,
            4: 2416 },
        'RelicPerform': {
            1: 2417,
            2: 2418,
            4: 2419 } }


class CWeaponstoreElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'ReplaceNpc': 1064,
        'LimitChallengeType': (12, 2, 17, 4, 18, 20, 23),
        'RefreshNpcLayer': (3, 4),
        'LimitHideLevelType': (5, 6, 8),
        'MaxAnimaNum': 2,
        'AnimaCost': (lambda *a: ceil(150 * Func678(*a) / 100)) }


class CTalentFusionElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'InitLayer': 1,
        'ChooseNum': (6, 2),
        'CommonTalentWeight': 10,
        'MaxNum': 2,
        'ExChooseWeightInfo': { },
        'ChooseWeight': 10 }


class CTaskElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'MaxRunningTask': 3 }


class CEndlessElement(cl_warmgr.mobject.CElementData):
    m_LayerConfig = {
        1: {
            'LayerChoose': {
                3: {
                    LAYER_CHOOSE_S7SHOP: (0, 0, 0, 0, {
                        1: 0,
                        2: 0,
                        3: 10,
                        4: 0 }, {
                        1: 0,
                        2: 0,
                        3: 1,
                        4: 0 }),
                    LAYER_CHOOSE_WANDSHOP: (1, 0, 1, 1, {
                        1: 0,
                        2: 0,
                        3: 10,
                        4: 0 }, {
                        1: 0,
                        2: 0,
                        3: 1,
                        4: 0 }),
                    LAYER_CHOOSE_PETSHOP: (1, 0, 1, 1, {
                        1: 0,
                        2: 0,
                        3: 0,
                        4: 10 }, {
                        1: 0,
                        2: 0,
                        3: 0,
                        4: 1 }),
                    LAYER_CHOOSE_TASKNPC: (0, 0, 0, 0, {
                        1: 0,
                        2: 0,
                        3: 8,
                        4: 10 }, {
                        1: 0,
                        2: 0,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_GSCASHSHOP: (0, 0, 0, 0, {
                        1: 0,
                        2: 5,
                        3: 30,
                        4: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_CRAFTSMAN: (1, 1, 0, 1, {
                        1: 0,
                        2: 5,
                        3: 30,
                        4: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_SHOP: (1, 0, 1, 1, {
                        1: 0,
                        2: 5,
                        3: 30,
                        4: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_EVENTNPC: (2, 1, 1, 3, {
                        1: 0,
                        2: 15,
                        3: 25,
                        4: 20 }, {
                        1: 0,
                        2: 1,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_CHALLENGE: ((lambda *a: 1 + (Func221(*a) // 8) * 3), 0, 1, 99, {
                        1: 25,
                        2: 25,
                        3: 25,
                        4: 25 }, { }),
                    LAYER_CHOOSE_HIDE: (0, 0, 0, 0, {
                        1: 10,
                        2: 10,
                        3: 30,
                        4: 20 }, {
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1 }) } } },
        2: {
            'LayerChoose': {
                3: {
                    LAYER_CHOOSE_S7SHOP: (0, 0, 0, 0, {
                        1: 0,
                        2: 0,
                        3: 10,
                        4: 0 }, {
                        1: 0,
                        2: 0,
                        3: 1,
                        4: 0 }),
                    LAYER_CHOOSE_WANDSHOP: (1, 0, 1, 1, {
                        1: 0,
                        2: 10,
                        3: 0 }, {
                        1: 0,
                        2: 1,
                        3: 0 }),
                    LAYER_CHOOSE_PETSHOP: (1, 0, 1, 1, {
                        1: 0,
                        2: 0,
                        3: 10 }, {
                        1: 0,
                        2: 0,
                        3: 1 }),
                    LAYER_CHOOSE_TASKNPC: (0, 0, 0, 0, {
                        1: 10,
                        2: 10,
                        3: 5 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_GSCASHSHOP: (0, 0, 0, 0, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_CRAFTSMAN: (1, 1, 0, 1, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_SHOP: (1, 0, 1, 1, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_EVENTNPC: (2, 1, 1, 2, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_CHALLENGE: ((lambda *a: 1 + (Func221(*a) // 8) * 5), 0, 1, 99, {
                        1: 30,
                        2: 30,
                        3: 30 }, { }),
                    LAYER_CHOOSE_HIDE: (0, 0, 0, 0, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }) } } },
        3: {
            'LayerChoose': {
                3: {
                    LAYER_CHOOSE_S7SHOP: (0, 0, 0, 0, {
                        1: 0,
                        2: 0,
                        3: 10,
                        4: 0 }, {
                        1: 0,
                        2: 0,
                        3: 1,
                        4: 0 }),
                    LAYER_CHOOSE_WANDSHOP: (1, 0, 1, 1, {
                        1: 0,
                        2: 10,
                        3: 0 }, {
                        1: 0,
                        2: 1,
                        3: 0 }),
                    LAYER_CHOOSE_PETSHOP: (1, 0, 1, 1, {
                        1: 0,
                        2: 0,
                        3: 10 }, {
                        1: 0,
                        2: 0,
                        3: 1 }),
                    LAYER_CHOOSE_TASKNPC: (0, 0, 0, 0, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_GSCASHSHOP: (0, 0, 0, 0, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_CRAFTSMAN: (1, 1, 0, 1, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_SHOP: (1, 0, 1, 1, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_EVENTNPC: (2, 1, 1, 2, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_CHALLENGE: ((lambda *a: 1 + (Func221(*a) // 8) * 6), 0, 1, 99, {
                        1: 30,
                        2: 30,
                        3: 30 }, { }),
                    LAYER_CHOOSE_HIDE: (0, 0, 0, 0, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }) } } },
        4: {
            'LayerChoose': {
                3: {
                    LAYER_CHOOSE_S7SHOP: (0, 0, 0, 0, {
                        1: 0,
                        2: 0,
                        3: 10,
                        4: 0 }, {
                        1: 0,
                        2: 0,
                        3: 1,
                        4: 0 }),
                    LAYER_CHOOSE_WANDSHOP: (1, 0, 1, 1, {
                        1: 0,
                        2: 10 }, {
                        1: 0,
                        2: 1 }),
                    LAYER_CHOOSE_PETSHOP: (1, 0, 1, 1, {
                        1: 0,
                        2: 10 }, {
                        1: 0,
                        2: 1 }),
                    LAYER_CHOOSE_TASKNPC: (0, 0, 0, 0, {
                        1: 10,
                        2: 10 }, {
                        1: 1,
                        2: 1 }),
                    LAYER_CHOOSE_GSCASHSHOP: (0, 0, 0, 0, {
                        1: 10,
                        2: 10 }, {
                        1: 1,
                        2: 1 }),
                    LAYER_CHOOSE_CRAFTSMAN: (1, 1, 0, 1, {
                        1: 10,
                        2: 10 }, {
                        1: 1,
                        2: 1 }),
                    LAYER_CHOOSE_SHOP: (1, 0, 1, 1, {
                        1: 10,
                        2: 10 }, {
                        1: 1,
                        2: 1 }),
                    LAYER_CHOOSE_EVENTNPC: (1, 0, 1, 1, {
                        1: 10,
                        2: 10 }, {
                        1: 1,
                        2: 1 }),
                    LAYER_CHOOSE_CHALLENGE: ((lambda *a: 1 + (Func221(*a) // 8) * 4), 0, 1, 99, {
                        1: 30,
                        2: 30 }, { }),
                    LAYER_CHOOSE_HIDE: (0, 0, 0, 0, {
                        1: 10,
                        2: 10 }, {
                        1: 1,
                        2: 1 }) } } } }
    m_InitPassive = [
        4396]
    m_MonsterGrade = 262
    m_MonsterExtraInfo = {
        5: (1, 3),
        8: ((lambda *a: (Func201(*a) * 10 - 75) / 4), (lambda *a: (Func201(*a) * 10 - 75) / 2)),
        18: (2, 3),
        28: (2, 4),
        38: (3, 4) }
    m_BossAttrAdjust = {
        'HPMax': (lambda *a: 1000 * min(10, Func201(*a) - 4)),
        'Att': (lambda *a: min(10000, 2500 * (Func201(*a) - 4))) }
    
    m_WeaponGrade = lambda *a: 7 + Func201(*a)
    m_MonsterResistance = 2000
    m_MonsterResistanceAdd = {
        5: (200, 400),
        10: (100, 200),
        12: (50, 100),
        14: (20, 50),
        18: (10, 10),
        28: (5, 5) }
    m_LevelCountdown = {
        5: (4000, 6000),
        8: (3500, 5500) }
    m_Config = {
        'ValidCycle': 9,
        'ReplaceNpc': {
            1027: 1066,
            1061: 1066,
            1062: 1053 },
        'StartLayer': 5,
        'GapLayer': 2,
        'FilterLayerCnt': 2,
        'BossDropInfo': {
            'Cash': 300,
            'GSCash': 30 },
        'DemonDropInfo': {
            'Cash': 100,
            'GSCash': 10 },
        'InteractGoldenCupReward': {
            'Cash': 300,
            'GSCash': 30 },
        'MonsterInitPerform': {
            'Default': [
                4398],
            3924: [
                4399],
            3925: [
                4399],
            3902: [
                4399],
            3904: [
                4399] },
        'GivenBaseLayer': {
            7: 4 },
        'NoSameBossEndLayer': 8,
        'InitTime': 60000,
        'ExcludeCacheMG': [
            4001],
        'MonsterTeamFactor': {
            'Normal': 0.7,
            'Elite': 0.5,
            'Boss': 0.7 },
        'LimitMonsterResistance': 9500,
        'CampFireNpc': {
            1: 1204 } }


class CTeammateAIElement(cl_warmgr.mobject.CElementData):
    m_AIMemberChooseBene = {
        201: {
            1: {
                13502: 10,
                13503: 10,
                13513: 10 } },
        205: {
            1: {
                13504: 10,
                13505: 10,
                13506: 10 } },
        206: {
            1: {
                13509: 10,
                13514: 10,
                13535: 10,
                13536: 10 } },
        207: {
            1: {
                13510: 10,
                13511: 10,
                13512: 10,
                13525: 10 } },
        212: {
            1: {
                13515: 10,
                13516: 10,
                13517: 10,
                13518: 10 } },
        213: {
            1: {
                13519: 10,
                13520: 10,
                13521: 10,
                13526: 10 } },
        215: {
            1: {
                13527: 10,
                13528: 10,
                13529: 10,
                13534: 10 } },
        216: {
            1: {
                13543: 10,
                13544: 10,
                13545: 10,
                13549: 10 } },
        217: {
            1: {
                13540: 10,
                13541: 10,
                13542: 10,
                13548: 10 } },
        218: {
            1: {
                13550: 10,
                13551: 10,
                13553: 10,
                13559: 10 } },
        219: {
            1: {
                13554: 10,
                13555: 10,
                13556: 10,
                13557: 10 } },
        214: {
            1: {
                13547: 10,
                13530: 10,
                13531: 10,
                13532: 10 } } }
    m_Config = {
        'HeroBasicPassive': [
            6950,
            6951,
            6952,
            6963,
            6966,
            6967],
        'HeroPassive': {
            201: [
                6954],
            205: [
                6953],
            206: [
                6962],
            207: [
                6955],
            212: [
                6956],
            213: [
                6957],
            214: [
                6958],
            215: [
                6959],
            216: [
                6960],
            217: [
                6961],
            218: [
                6964],
            219: [
                6965],
            220: [
                6968],
            221: [
                6969] },
        'DamReduceRatioInfo': {
            0: 0,
            5: 25,
            20: 50,
            30: 75,
            40: 90,
            50: 99 },
        'DamThreshold': 20,
        'Weapon': {
            1003: 1,
            1004: 1,
            1016: 1,
            1102: 1,
            1104: 1,
            1108: 1,
            1205: 1,
            1209: 1,
            1501: 1,
            1303: 1,
            1309: 1,
            1504: 1,
            1017: 1 },
        'RelicNoChoosed': [],
        'RelicWhiteList': [
            5862],
        'PerformWhiteList': [
            15012],
        'TaskPassiveWhiteList': {
            1010: [
                40042],
            1110: [
                40054],
            1210: [
                40056] },
        'AIConvertRatio': 0.6,
        'BossShareDropProb': 25,
        'BossShareDropCnt': {
            1: 25,
            2: 50,
            3: 25 },
        'BossShareDropMG': {
            1001: 10,
            2401: 10 },
        'BeneWhiteList': [
            13708,
            13719],
        'RewardBeneLayer': [
            1,
            2,
            3],
        'Fsm': {
            206: 'Hero.HeroNearFsm',
            219: 'Hero.XiuMoNearFsm',
            213: 'Hero.QianSuiNearFsm',
            220: 'Hero.CangJueFsm' },
        'SeasonSuitRelicWeight': 20,
        'SeasonSuitWhiteList': [
            15112,
            15126,
            15160,
            15124] }


class CRelicTalentElement(cl_warmgr.mobject.CSeasonElementData):
    m_Config = {
        'EnableRound': [
            3],
        'RelicOptionCnt': 3,
        'ForbidRelic': [
            5818,
            5755,
            5779,
            5752,
            5780],
        'MagicNpc': {
            1516: 0,
            1517: 0,
            1518: 0,
            1519: 0 },
        'ExcludeBossDropLayer': [
            4],
        'ForbidSuit': [
            15014],
        'MagicDrop': {
            3: 5530,
            2: 5529,
            1: 5528 },
        'MagicBossWeight': {
            (3, 3): 10 },
        'MagicNpcWeight': {
            (1, 3): 20,
            (2, 3): 10 },
        'MagicNotify': 9462,
        'MagicRoomCLGWeight': {
            (2, 3): 10,
            (1, 3): 20 },
        'MagicRoomCLG': [
            10,
            2],
        'EventNpc': {
            2: {
                2301: 10,
                2302: 10 },
            3: {
                2301: 10,
                2302: 10 },
            4: {
                2301: 10,
                2302: 10 } },
        'MinimumMagic': 2 }


class CRealEndlessElement(cl_warmgr.mobject.CElementData):
    m_LayerConfig = {
        1: {
            'LayerChoose': {
                3: {
                    LAYER_CHOOSE_S7SHOP: (0, 0, 0, 0, {
                        1: 0,
                        2: 0,
                        3: 10,
                        4: 0 }, {
                        1: 0,
                        2: 0,
                        3: 1,
                        4: 0 }),
                    LAYER_CHOOSE_WANDSHOP: (1, 0, 1, 1, {
                        1: 0,
                        2: 0,
                        3: 10,
                        4: 0 }, {
                        1: 0,
                        2: 0,
                        3: 1,
                        4: 0 }),
                    LAYER_CHOOSE_PETSHOP: (1, 0, 1, 1, {
                        1: 0,
                        2: 0,
                        3: 0,
                        4: 10 }, {
                        1: 0,
                        2: 0,
                        3: 0,
                        4: 1 }),
                    LAYER_CHOOSE_TASKNPC: (0, 0, 0, 0, {
                        1: 0,
                        2: 0,
                        3: 8,
                        4: 10 }, {
                        1: 0,
                        2: 0,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_GSCASHSHOP: (1, 1, 1, 99, {
                        1: 0,
                        2: 5,
                        3: 30,
                        4: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_CRAFTSMAN: (1, 0, 0, 99, {
                        1: 0,
                        2: 5,
                        3: 30,
                        4: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_SHOP: (1, 1, 1, 99, {
                        1: 0,
                        2: 5,
                        3: 30,
                        4: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_EVENTNPC: (2, 0, 1, 99, {
                        1: 0,
                        2: 15,
                        3: 25,
                        4: 20 }, {
                        1: 0,
                        2: 1,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_CHALLENGE: ((lambda *a: 1 + (Func221(*a) // 8) * 3), 0, 1, 99, {
                        1: 25,
                        2: 25,
                        3: 25,
                        4: 25 }, { }),
                    LAYER_CHOOSE_HIDE: (4, 1, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 30,
                        4: 20 }, {
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1 }) } } },
        2: {
            'LayerChoose': {
                3: {
                    LAYER_CHOOSE_S7SHOP: (0, 0, 0, 0, {
                        1: 0,
                        2: 0,
                        3: 10,
                        4: 0 }, {
                        1: 0,
                        2: 0,
                        3: 1,
                        4: 0 }),
                    LAYER_CHOOSE_WANDSHOP: (1, 0, 1, 1, {
                        1: 0,
                        2: 10,
                        3: 0 }, {
                        1: 0,
                        2: 1,
                        3: 0 }),
                    LAYER_CHOOSE_PETSHOP: (1, 0, 1, 1, {
                        1: 0,
                        2: 0,
                        3: 10 }, {
                        1: 0,
                        2: 0,
                        3: 1 }),
                    LAYER_CHOOSE_TASKNPC: (0, 0, 0, 0, {
                        1: 10,
                        2: 10,
                        3: 5 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_GSCASHSHOP: (1, 1, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_CRAFTSMAN: (3, 1, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_SHOP: (1, 1, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_EVENTNPC: (2, 0, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_CHALLENGE: ((lambda *a: 1 + (Func221(*a) // 8) * 5), 0, 1, 99, {
                        1: 30,
                        2: 30,
                        3: 30 }, { }),
                    LAYER_CHOOSE_HIDE: (3, 1, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }) } } },
        3: {
            'LayerChoose': {
                3: {
                    LAYER_CHOOSE_S7SHOP: (0, 0, 0, 0, {
                        1: 0,
                        2: 0,
                        3: 10,
                        4: 0 }, {
                        1: 0,
                        2: 0,
                        3: 1,
                        4: 0 }),
                    LAYER_CHOOSE_WANDSHOP: (1, 0, 1, 1, {
                        1: 0,
                        2: 10,
                        3: 0 }, {
                        1: 0,
                        2: 1,
                        3: 0 }),
                    LAYER_CHOOSE_PETSHOP: (1, 0, 1, 1, {
                        1: 0,
                        2: 0,
                        3: 10 }, {
                        1: 0,
                        2: 0,
                        3: 1 }),
                    LAYER_CHOOSE_TASKNPC: (0, 0, 0, 0, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_GSCASHSHOP: (1, 1, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_CRAFTSMAN: (3, 1, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_SHOP: (1, 1, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_EVENTNPC: (2, 1, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_CHALLENGE: ((lambda *a: 1 + (Func221(*a) // 8) * 6), 0, 1, 99, {
                        1: 30,
                        2: 30,
                        3: 30 }, { }),
                    LAYER_CHOOSE_HIDE: (3, 1, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }) } } },
        4: {
            'LayerChoose': {
                3: {
                    LAYER_CHOOSE_S7SHOP: (0, 0, 0, 0, {
                        1: 0,
                        2: 0,
                        3: 10,
                        4: 0 }, {
                        1: 0,
                        2: 0,
                        3: 1,
                        4: 0 }),
                    LAYER_CHOOSE_WANDSHOP: (1, 0, 1, 1, {
                        1: 0,
                        2: 10 }, {
                        1: 0,
                        2: 1 }),
                    LAYER_CHOOSE_PETSHOP: (1, 0, 1, 1, {
                        1: 0,
                        2: 10 }, {
                        1: 0,
                        2: 1 }),
                    LAYER_CHOOSE_TASKNPC: (0, 0, 0, 0, {
                        1: 10,
                        2: 10 }, {
                        1: 1,
                        2: 1 }),
                    LAYER_CHOOSE_GSCASHSHOP: (1, 1, 1, 99, {
                        1: 10,
                        2: 10 }, {
                        1: 1,
                        2: 1 }),
                    LAYER_CHOOSE_CRAFTSMAN: (3, 1, 0, 99, {
                        1: 10,
                        2: 10 }, {
                        1: 1,
                        2: 1 }),
                    LAYER_CHOOSE_SHOP: (1, 1, 1, 99, {
                        1: 10,
                        2: 10 }, {
                        1: 1,
                        2: 1 }),
                    LAYER_CHOOSE_EVENTNPC: (2, 1, 1, 99, {
                        1: 10,
                        2: 10 }, {
                        1: 1,
                        2: 1 }),
                    LAYER_CHOOSE_CHALLENGE: ((lambda *a: 1 + (Func221(*a) // 8) * 4), 0, 1, 99, {
                        1: 30,
                        2: 30 }, { }),
                    LAYER_CHOOSE_HIDE: (2, 1, 0, 99, {
                        1: 10,
                        2: 10 }, {
                        1: 1,
                        2: 1 }) } } } }
    m_InitPassive = [
        4396]
    m_MonsterGrade = 160
    m_MonsterExtraInfo = {
        5: (3, 4),
        40: (3, 3),
        55: (3, 2),
        80: (3, 4),
        130: (3, 2),
        255: (2, 4),
        505: (2, 3),
        900: (2, 2) }
    m_BossAttrAdjust = {
        'HPMax': (lambda *a: 1000 * min(10, Func201(*a) - 4)),
        'Att': (lambda *a: min(10000, 2500 * (Func201(*a) - 4))) }
    
    m_WeaponGrade = lambda *a: 7 + Func201(*a)
    m_MonsterResistance = 0
    m_MonsterResistanceAdd = {
        5: (100, 100),
        12: (35, 70),
        20: (25, 50),
        28: (20, 40),
        50: (10, 10) }
    m_LevelCountdown = { }
    m_Config = {
        'ValidCycle': 1,
        'ReplaceNpc': {
            1027: 1066,
            1061: 1066,
            1062: 1053 },
        'StartLayer': 5,
        'GapLayer': 2,
        'FilterLayerCnt': 2,
        'MonsterInitPerform': {
            'Default': [
                4398],
            3924: [
                4399],
            3925: [
                4399],
            3902: [
                4399],
            3904: [
                4399] },
        'ExcludeCacheMG': [
            4001],
        'GoldenCupConfig': {
            'Boss': 1061 },
        'FilterHideLevelType': {
            2: 1 },
        'MonsterTeamFactor': {
            'Normal': 0.8,
            'Elite': 0.6,
            'Boss': 0.7 },
        'LimitMonsterResistance': 9900,
        'CampFireNpc': {
            1: 1204 } }


class CDeviceElement(cl_warmgr.mobject.CSeasonElementData):
    m_Config = {
        'EnableRound': [
            3],
        'SummonStela': 1202,
        'MaxLayerCount': 2,
        'MaxLevelCount': 1,
        'ExcludeLevel': {
            1: [
                1,
                2,
                3,
                4] },
        'AddExtComponentPosLayer': [
            1,
            2,
            3],
        'ChooseDevice': [
            1001,
            1002,
            1003],
        'MaxCompPos': 3,
        'DeviceChallengeReward': {
            'EnergyPoint': {
                5: 10000 } },
        'PassBoxRewardDelay': 150,
        'RewardConfig': {
            1: 1001,
            2: 1002,
            4: 1003 },
        'BossForceDropComp': {
            'Layer': [
                1,
                2,
                3],
            'Config': {
                1001: (50100, 50101, 50102),
                1002: (50120, 50121, 50122),
                1003: (50140, 50141, 50142) } },
        'MinDropHeroExclusiveLayer': 3,
        'ExcludeLevelChosenCompNum': 47 }


class CConquerElement(cl_warmgr.mobject.CSeasonElementData):
    m_Config = {
        'EnableRound': [
            3],
        'LevelMonster': {
            (0, 4, 2): [
                20891],
            (0, 4, 1): [
                21281,
                21641],
            (1, 3, 3): [
                22811,
                22831,
                22821,
                21431],
            (1, 3, 2): [
                22031,
                22021,
                21811],
            (0, 3, 3): [
                22811,
                22831,
                22821,
                21431],
            (0, 3, 2): [
                22031,
                22021,
                21811],
            (0, 3, 1): [
                22811,
                22831,
                22821,
                21431],
            (1, 2, 3): [
                24221,
                20861],
            (1, 2, 2): [
                21311,
                21821,
                22051,
                24221],
            (1, 2, 1): [
                21621,
                21421,
                21251],
            (0, 2, 3): [
                21621,
                21421,
                21251],
            (0, 2, 2): [
                22011,
                21221,
                21251],
            (0, 2, 1): [
                21621,
                21421,
                21251],
            (0, 1, 4): [
                20831,
                21611],
            (0, 1, 3): [
                21231,
                20831] },
        'ConquerProcess': (lambda *a: 20 + Func572(*a) * 60),
        'ConquerRate': (lambda *a: 80 + 60 * ((Func656(*a) + Func690(*a) - 1) / Func572(*a))),
        'HaltInfo': {
            103: 1,
            108: 1,
            321: 0,
            323: 1,
            322: 1,
            40108: 1,
            30108: 1,
            10108: 1,
            50108: 1,
            10149: 0,
            20149: 0,
            143: 0,
            198: 0 },
        'IgnoreHalt': (1323, 9214, 1019, 1021, 1018, 1017, 12013, 9703, 9793, 1024),
        'ConquerRadius': 5,
        'FirstWeakTime': 700,
        'WeakAddTime': 100,
        'BanPlusPF': (6107, 6114),
        'BanAttrPlus': (6202,),
        'PlusLevel': {
            (4, 1): 1,
            (3, 2): 1,
            (2, 2): 1 },
        'EndlessLevel': {
            (4, 1): 1,
            (3, 2): 1,
            (2, 2): 1,
            (1, 3): 1 },
        'ActiveAbilityCost': 100,
        'FuseCost': 100,
        'SingleFuseMaxResetTimes': 2,
        'PetGrowthNormal': {
            'HPMax': 10,
            'AttInfo': {
                1: 20,
                2: 30,
                3: 30,
                4: 40 } },
        'PetGrowthCycle': {
            'HPMax': 20,
            'AttInfo': {
                1: 20,
                2: 40,
                3: 60,
                4: 80 } },
        'RarePetEggMinimum': 3,
        'ConquerRewardRareEggProb': 30,
        'ConquerRewardEggSID': {
            1: 5535,
            2: 5536 },
        'PlusLevelExtEggCnt': 1,
        'ExcludeArea': ((1120343, 6),),
        'PetShopTypeWeight': 20 }
    m_AllSeasonFunc = [
        SEASONFUNC_FUSE_PET,
        SEASONFUNC_ACTION_PET,
        SEASONFUNC_REFRESH_PETSHOP,
        SEASONFUNC_FUSERESET_PET]


class CRegroupRelicElement(cl_warmgr.mobject.CSeasonElementData):
    m_Config = {
        'EnableRound': [
            3],
        'ForceOpenElement': [
            'MonsterRelicElement'],
        'RegroupRelicNpc': 1069,
        'NoRepeatBossRelicLayer': 0,
        'DropMysteryRelicRatio': 5,
        'InitBlankRelicNum': 2,
        'ExtLotteryNpc': [
            (2, 2),
            (3, 2)] }


class CNewbieTutorialElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'CrazyDamTrigger': {
            'PlayerGrade': (0, 8),
            'PlayTimes': (0, 3),
            'LimitRange': (1, 2),
            'ExtraRule': [],
            'MaxDisplayTimes': 1,
            'OwnColdTime': 9000,
            'Notify': 9607 },
        'LuckyHitTrigger': {
            'PlayerGrade': (0, 12),
            'PlayTimes': (0, 7),
            'LimitRange': (0, 0),
            'ExtraRule': [],
            'MaxDisplayTimes': 1,
            'OwnColdTime': 9000,
            'Notify': 9626 },
        'MultiLuckyHitTrigger': {
            'PlayerGrade': (25, 45),
            'PlayTimes': (0, 12),
            'LimitRange': (0, 0),
            'ExtraRule': [],
            'MaxDisplayTimes': 3,
            'OwnColdTime': 9000,
            'Notify': 9608 },
        'ExplosionTrigger': {
            'PlayerGrade': (10, 45),
            'PlayTimes': (0, 12),
            'LimitRange': (0, 0),
            'ExtraRule': [
                1],
            'MaxDisplayTimes': 2,
            'OwnColdTime': 9000,
            'Notify': 9609 },
        'VertigoTrigger': {
            'PlayerGrade': (10, 45),
            'PlayTimes': (0, 12),
            'LimitRange': (0, 0),
            'ExtraRule': [
                1],
            'MaxDisplayTimes': 2,
            'OwnColdTime': 9000,
            'Notify': 9610 },
        'PoisonTrigger': {
            'PlayerGrade': (10, 45),
            'PlayTimes': (0, 12),
            'LimitRange': (0, 0),
            'ExtraRule': [
                1],
            'MaxDisplayTimes': 2,
            'OwnColdTime': 9000,
            'Notify': 9611 },
        'ThunderDamTrigger': {
            'PlayerGrade': (0, 12),
            'PlayTimes': (0, 7),
            'LimitRange': (0, 0),
            'ExtraRule': [],
            'MaxDisplayTimes': 1,
            'OwnColdTime': 9000,
            'Notify': 9612 },
        'FireDamTrigger': {
            'PlayerGrade': (0, 12),
            'PlayTimes': (0, 7),
            'LimitRange': (1, 4),
            'ExtraRule': [],
            'MaxDisplayTimes': 1,
            'OwnColdTime': 9000,
            'Notify': 9613 },
        'CorrosionDamTrigger': {
            'PlayerGrade': (10, 18),
            'PlayTimes': (0, 10),
            'LimitRange': (0, 0),
            'ExtraRule': [
                1],
            'MaxDisplayTimes': 1,
            'OwnColdTime': 9000,
            'Notify': 9614 },
        'ShareColdTime': 3000,
        'lockModify': {
            'lstLock': [
                1211,
                1010,
                1303],
            'dModify': {
                2125: -80,
                2126: -80,
                2123: -80 } },
        'UnlockModify': {
            1209: {
                2127: 5000 },
            1010: {
                2125: 5000 },
            1303: {
                2125: 5000 },
            1211: {
                2126: 5000 },
            1401: {
                2106: 5000 } },
        'MaxModifyTimes': 3 }


class CSeasonSuitElement(cl_warmgr.mobject.CSeasonElementData):
    m_Config = {
        'InitChooseSuit': [
            15135,
            15136,
            15137],
        'BeneTakeEffectSuit': {
            13725: [
                15106,
                15107,
                15124,
                15126] } }


class CWandElement(cl_warmgr.mobject.CSeasonElementData):
    m_Config = {
        'EnableRound': [
            3],
        'WandShopNpc': 1072,
        'ReplaceAFPF': {
            6101: 6117,
            6102: 6119,
            6103: 6118,
            6105: 6120,
            6111: 6121 },
        'WandMG': (601, 1000),
        'WandDropLayerLimit': 2,
        'GuaranteedDropCount': 30,
        'WandDamageStatistics': {
            1736: METEOR_WANDCOMP,
            1970: ORBIT_WAND,
            1968: CAPACITOR_WAND,
            1974: LIGHTNING_WANDCOMP,
            1975: SWORD_WANDCOMP,
            51209: OVERLOAD_WAND,
            1746: METEOR_WANDCOMP },
        'AbilityQualityFloatingRange': {
            1: (0, 20),
            2: (40, 100),
            3: (120, 160),
            4: (180, 200) },
        'ReverseAbilityFloatingRange': {
            1: (180, 200),
            2: (100, 160),
            3: (40, 80),
            4: (0, 20) },
        'AbilityChooseRatio': {
            'NegativeRatio': 0,
            'HasNegative': {
                1: 20,
                2: 40,
                3: 30,
                4: 10 },
            'NotNegative': {
                1: 30,
                2: 50,
                3: 15,
                4: 5 } } }
    m_AllSeasonFunc = [
        SEASONFUNC_OPEN_WANDABILITY]


class CDiceElement(cl_warmgr.mobject.CSeasonElementData):
    m_Config = {
        'EnableRound': [
            3],
        'TempPointRange': {
            1: {
                1: [
                    1,
                    2,
                    3],
                2: [
                    4,
                    5],
                3: [
                    6] },
            2: {
                2: [
                    1,
                    2,
                    3,
                    4,
                    5],
                3: [
                    6,
                    7,
                    8,
                    9,
                    10],
                4: [
                    11,
                    12] },
            3: {
                3: [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10],
                4: [
                    11,
                    12,
                    13,
                    14,
                    15,
                    16],
                5: [
                    17,
                    18] } },
        'DiceRewardNum': 0,
        'DiceRewardDelay': 150,
        'DiceRewardConfig': {
            1: {
                1: 1000,
                2: 0,
                3: 0 },
            2: {
                1: 0,
                2: 100,
                3: 0 },
            3: {
                1: 0,
                2: 100,
                3: 0 },
            4: {
                1: 0,
                2: 0,
                3: 100 } },
        'DropDiceConfig': {
            1: {
                1: 0,
                2: 0,
                3: 0 },
            2: {
                1: 0,
                2: 0,
                3: 0 },
            3: {
                1: 0,
                2: 0,
                3: 0 },
            4: {
                1: 0,
                2: 0,
                3: 0 } },
        'DiceShopNpc': 1073,
        'ChallengeLvWeightInfo': {
            1: {
                1: 10,
                2: 40,
                3: 40 },
            2: {
                2: 10,
                3: 50,
                4: 30 },
            3: {
                3: 10,
                4: 60,
                5: 30 },
            4: {
                3: 0,
                4: 30,
                5: 70 } },
        'ChallengeLvToPoint': {
            1: {
                1: [
                    1,
                    3],
                2: [
                    4,
                    5],
                3: [
                    6] },
            2: {
                2: [
                    1,
                    5],
                3: [
                    6,
                    10],
                4: [
                    11,
                    12] },
            3: {
                3: [
                    8,
                    10],
                4: [
                    11,
                    16],
                5: [
                    17,
                    18] },
            4: {
                3: [
                    1,
                    10],
                4: [
                    11,
                    16],
                5: [
                    17,
                    18] } },
        'ChallengePutInfo': [
            1152,
            1153,
            1154,
            1155,
            1156],
        'ChallengeIgnoreInfo': [
            1054,
            1082],
        'ChallengePutWeight': 10,
        'SelectionPacketDropInfo': {
            1: 2,
            2: 2,
            3: 3 },
        'PacketChallengeDropInfo': {
            1: 1,
            2: 2,
            3: 3 },
        'SelectionPacketQualityInfo': {
            1: 5550,
            2: 5551,
            3: 5552 },
        'DiceEnergyInfo': {
            'SeasonChallenge': {
                1: 3,
                2: 4,
                3: 5,
                4: 6 },
            'KillBoss': {
                1: 6,
                2: 8,
                3: 10,
                4: 12 } },
        'ExtraDiceShop': {
            1: {
                4: 1 },
            2: {
                3: 1 } },
        'DropDiceShape': {
            1: 5549,
            2: 5555,
            3: 5556 },
        'DiceDamagePerform': {
            12033: DICE_SPRINT,
            12034: DICE_EJECT,
            1978: DICE_CONTROL,
            1981: DICE_WAVE,
            1749: DICE_METEOR,
            1983: DICE_CONTROL,
            1984: DICE_CONTROL,
            7355: DICE_SELFEXPLODE },
        'DiceQualityAddEnergy': {
            1: 2,
            2: 3,
            3: 4,
            4: 6,
            5: 12 },
        'WarInitDiceEnergy': 10,
        'RollPointWeight': {
            6: 10,
            12: 10,
            18: 10 } }


class CBackpackElement(cl_warmgr.mobject.CSeasonElementData):
    m_Config = {
        'EnableRound': [
            3],
        'DropCrystalTotalPointWeight': {
            1: {
                (3, 4): 100 },
            2: {
                (3, 4): 100 },
            3: {
                (3, 4): 100 },
            4: {
                (3, 4): 100 } },
        'PassBoxDropS7ItemNum': [
            0,
            0],
        'KillBossDropS7ItemNum': [
            0,
            0],
        'OpenBossShopNpc': 1,
        'SeasonShopNpcSID': 1074,
        'KillLayerBossUnlockConEquipAreaSize': {
            0: (4, 4),
            1: (4, 4),
            2: (4, 4),
            3: (4, 4) },
        'MaxConEquipAreaSize': [
            4,
            4],
        'OpenFirstHallShopNpc': 1,
        'BackpackDamagePerform': {
            7355: BACKPACK_SELFEXPLODE,
            12041: BACKPACK_SHOOTOFF,
            12040: BACKPACK_CORROSIVESPIKES,
            12042: BACKPACK_THUNDERBLADE,
            1992: BACKPACK_TOXICHAZE,
            1991: BACKPACK_METEOR,
            1998: BACKPACK_BLOOM,
            2007: BACKPACK_THUNDERBLADE,
            51670: BACKPACK_HPDAM },
        'SeasonChallengePutWeight': {
            1159: 20,
            1160: 20,
            1161: 20,
            1162: 20 },
        'SeasonChallengeIgnore': [],
        'SeasonChallengeGuaranteeCount': 5,
        'ExtraS7ShopNpc': {
            2: {
                1: 1 } },
        'SeasonChallengeLayerRewardLimit': 2,
        'AIEnableWhitePF': [
            6628,
            6629,
            6630,
            6631,
            6632,
            6633,
            6634,
            6635],
        'AIMoudleWhite': [
            2017,
            2044],
        'SeasonChallengeDropGoodSID': 1217 }
    m_AllSeasonFunc = [
        SEASONFUNC_S7_OPEN_ENHANCE]


class CPlayerExtraElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'SpeedPassive': 0 }


class CS8Element(cl_warmgr.mobject.CSeasonElementData):
    m_Config = {
        'EnableRound': [
            3],
        'OpenFirstHallShopNpc': 1,
        'OpenBossShopNpc': 1,
        'SeasonShopNpcSID': 1075,
        'S8DamagePerform': {
            52001: S8_THIRDACTIVE_SHIELD,
            52002: S8_THIRDACTIVE_SUPER_MUSHROOM,
            52003: S8_THIRDACTIVE_ELITE_TEAM,
            52004: S8_THIRDACTIVE_FISH_DRAGON,
            52005: S8_THIRDACTIVE_GLUTTONY,
            2006: S8_THIRDACTIVE_SHIELD } }


class CWarManager(CCustomWarMgr):
    m_SID = 3001
    m_StepInfo = { }
    m_InitStep = []
    m_ComponentCls = {
        'InitResourceElement': (cl_warmgr.initresourceelement.GetComponentClass, CInitResourceElement),
        'LevelCtrl': (cl_warmgr.levelctrl.GetComponentClass, CLevelCtrlElement),
        'Warreport': (cl_warmgr.warreport.GetComponentClass, CWarreport),
        'PVEDieElement': (cl_warmgr.pvedieelement.GetComponentClass, CPVEDieElement),
        'WeaponAnalyse': (cl_warmgr.weaponanalyse.GetComponentClass, CWeaponAnalyse),
        'TeamInfo': (cl_warmgr.teaminfoelement.GetComponentClass, CTeamInfoElement),
        'RoundElement': (cl_warmgr.roundelement.GetComponentClass, CRoundElement),
        'MonsterSuper': (cl_warmgr.monsterspelement.GetComponentClass, CMonsterSuperElement),
        'WatchElement': (cl_warmgr.watchelement.GetComponentClass, CWatchElement),
        'SaveElement': (cl_warmgr.saveelement.GetComponentClass, CSaveElement),
        'BigDataAnalyseMgr': (cl_warmgr.bigdataanalyse.GetComponentClass, CBigDataAnalyseMgr),
        'TeamSaveElement': (cl_warmgr.teamsaveelement.GetComponentClass, CTeamSaveElement),
        'SignalElement': (cl_signal.GetComponentClass, CSignalElement),
        'RescueElement': (cl_warmgr.rescueelement.GetComponentClass, CRescueElement),
        'RecycleDropElement': (cl_warmgr.recycledropelement.GetComponentClass, CRecycleDropElement),
        'CheckCheatElement': (cl_warmgr.checkcheatelement.GetComponentClass, CCheckCheatElement),
        'HangUpKickElement': (cl_warmgr.hangupkickelement.GetComponentClass, CHangUpKickElement),
        'SuitElement': (cl_warmgr.suitelement.GetComponentClass, CSuitElement),
        'SnowMountainElement': (cl_warmgr.snowmountainelement.GetComponentClass, CSnowMountainElement),
        'RidingAloneElement': (cl_warmgr.ridingaloneelement.GetComponentClass, CRidingAloneElement),
        'MonsterRelicElement': (cl_warmgr.monsterrelicelement.GetComponentClass, CMonsterRelicElement),
        'RollRelicElement': (cl_warmgr.rollrelicelement.GetComponentClass, CRollRelicElement),
        'WeaponStoreElement': (cl_warmgr.weaponstoreelement.GetComponentClass, CWeaponstoreElement),
        'TalentFusionElement': (cl_warmgr.talentfusionelement.GetComponentClass, CTalentFusionElement),
        'TaskElement': (cl_warmgr.taskelement.GetComponentClass, CTaskElement),
        'EndlessElement': (cl_warmgr.endlesselement.GetComponentClass, CEndlessElement),
        'TeammateAI': (cl_warmgr.teammateaielement.GetComponentClass, CTeammateAIElement),
        'RelicTalentElement': (cl_warmgr.relictalentelement.GetComponentClass, CRelicTalentElement),
        'RealEndlessElement': (cl_warmgr.realendlesselement.GetComponentClass, CRealEndlessElement),
        'DeviceElement': (cl_warmgr.deviceelement.GetComponentClass, CDeviceElement),
        'ConquerElement': (cl_warmgr.conquerelement.GetComponentClass, CConquerElement),
        'RegroupRelicElement': (cl_warmgr.regrouprelicelement.GetComponentClass, CRegroupRelicElement),
        'NewbieTutorialElement': (cl_warmgr.newbietutorialelement.GetComponentClass, CNewbieTutorialElement),
        'SeasonSuitElement': (cl_warmgr.seasonsuitelement.GetComponentClass, CSeasonSuitElement),
        'WandElement': (cl_warmgr.wandelement.GetComponentClass, CWandElement),
        'DiceElement': (cl_warmgr.diceelement.GetComponentClass, CDiceElement),
        'BackpackElement': (cl_warmgr.backpackelement.GetComponentClass, CBackpackElement),
        'PlayerExtraElement': (cl_warmgr.playerextraelement.GetComponentClass, CPlayerExtraElement),
        'S8Element': (cl_warmgr.s8element.GetComponentClass, CS8Element) }
    m_SeasonFuncConfing = {
        SEASONFUNC_S7_OPEN_ENHANCE: 'BackpackElement',
        SEASONFUNC_OPEN_WANDABILITY: 'WandElement',
        SEASONFUNC_FUSERESET_PET: 'ConquerElement',
        SEASONFUNC_REFRESH_PETSHOP: 'ConquerElement',
        SEASONFUNC_ACTION_PET: 'ConquerElement',
        SEASONFUNC_FUSE_PET: 'ConquerElement' }
    m_AllSeasonElement = {
        'RelicTalentElement': 1,
        'DeviceElement': 1,
        'ConquerElement': 1,
        'RegroupRelicElement': 1,
        'SeasonSuitElement': 1,
        'WandElement': 1,
        'DiceElement': 1,
        'BackpackElement': 1,
        'S8Element': 1 }
    m_NewVerLayer = {
        1301205,
        1303113,
        1301206,
        1101704,
        1101706,
        1301207,
        1303111,
        1301208,
        1303116,
        1301906,
        1302163,
        1301209,
        1301210,
        1101225,
        1101226,
        1101227,
        1101228,
        1101229,
        1101230,
        1101231,
        1201705,
        1302703,
        1302704,
        1101235,
        1101236,
        1101237,
        1101238,
        1101239,
        1101240,
        1101241,
        1103167,
        1103168,
        1103169,
        1103170,
        1103171,
        1103172,
        1103173,
        1103174,
        1201223,
        1201224,
        1201225,
        1201226,
        1201227,
        1203148,
        1203149,
        1203150,
        1203151,
        1203152,
        1203153,
        1203154,
        1203155,
        1203156,
        1105109,
        1105110,
        1105111,
        1105112,
        1105113,
        1105114,
        1105115,
        1105116,
        1203157,
        1302110,
        1302111,
        1302112,
        1302113,
        1302114,
        1302115,
        1301204,
        1301212,
        1301214,
        1303112,
        1303109,
        1303110,
        1201906,
        1301203,
        1205111,
        1205112,
        1205113,
        1205114,
        1205115,
        1205116,
        1205117,
        1205118,
        1205119}
    m_SeasonElement = {
        1: [
            'RelicTalentElement'],
        2: [
            'DeviceElement'],
        3: [
            'ConquerElement'],
        4: [
            'RegroupRelicElement',
            'SeasonSuitElement'],
        5: [
            'WandElement'],
        6: [
            'DiceElement'],
        7: [
            'BackpackElement'],
        8: [
            'S8Element'] }

