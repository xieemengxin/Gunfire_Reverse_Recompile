# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/wm3007.pyc
# RelativePath: clientlogic/cl_wardata/wm3007.pyc
# Source Generated with Decompyle++
# File: wm3007.pyc (Python 3.6)

from __future__ import absolute_import
from cl_warmgr.mobject import CWarManager as CCustomWarMgr
from cl_commondefines import GAMETYPE_DESTROY, HIDELV_TYPE_CASH, HIDELV_TYPE_ELITE, HIDELV_TYPE_NORMAL, HIDELV_TYPE_TRAP, LAYER_CHOOSE_CHALLENGE, LAYER_CHOOSE_CRAFTSMAN, LAYER_CHOOSE_EVENTNPC, LAYER_CHOOSE_GSCASHSHOP, LAYER_CHOOSE_HIDE, LAYER_CHOOSE_SHOP, LAYER_CHOOSE_TASKNPC, LEVEL_TYPE_BOSS, LEVEL_TYPE_FIGHT, LEVEL_TYPE_HALL, LEVEL_TYPE_HIDE, MODE_REAL_ENDLESS, MODE_SNOWMOUNTAINS, ROUND_EXTRULE_APPEARCHALLENGE, ROUND_EXTRULE_REPLACECONFIG_CHALLENGE, ROUND_EXTRULE_REPLACEMONSTER, WARRIOR_ELITE
from cl_newformula import Func201, Func202, Func204, Func205, Func221, Func544
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
import cl_warmgr.hangupkickelement
import cl_warmgr.reportsaveelement
import cl_warmgr.suitelement
import cl_warmgr.snowmountainelement
import cl_warmgr.ridingaloneelement
import cl_warmgr.monsterrelicelement
import cl_warmgr.rollrelicelement
import cl_warmgr.weaponstoreelement
import cl_warmgr.talentfusionelement
import cl_warmgr.taskelement
import cl_warmgr.endlesselement
import cl_warmgr.realendlesselement
import cl_warmgr.relictalentelement
import cl_warmgr.teammateaielement

def ChooseAction11101009(oWarMgr, iLevel):
    return warcondition.WarCheckHistoryKillBoss(oWarMgr, iLevel, {
        39011: 1 }, 5)


def ForceAction11101009(oWarMgr, iLevel):
    return warcondition.WarCheckForceLevel(oWarMgr, iLevel, {
        39011: 1 }, 5)


def ChooseAction21202003(oWarMgr, iLevel):
    return warcondition.WarCheckHistoryKillBoss(oWarMgr, iLevel, {
        39131: 1 }, 5)


def ForceAction21202003(oWarMgr, iLevel):
    return warcondition.WarCheckForceLevel(oWarMgr, iLevel, {
        39131: 1 }, 5)


def ChooseAction31301003(oWarMgr, iLevel):
    return warcondition.WarCheckHistoryKillBoss(oWarMgr, iLevel, {
        39051: 1 }, 3)


def ForceAction31301003(oWarMgr, iLevel):
    return warcondition.WarCheckForceLevel(oWarMgr, iLevel, {
        39051: 1 }, 3)


def ChooseAction41403001(oWarMgr, iLevel):
    if warcondition.WarCheckSpecifcMode(oWarMgr, iLevel, 1002) == 0:
        pass
    return warcondition.WarCheckCycle(oWarMgr, iLevel, 9) == 0


def ChooseAction41403002(oWarMgr, iLevel):
    if warcondition.WarCheckSpecifcMode(oWarMgr, iLevel, 1002):
        pass
    return warcondition.WarCheckCycle(oWarMgr, iLevel, 9)


def ChooseAction41403003(oWarMgr, iLevel):
    if warcondition.WarCheckHistoryKillBoss(oWarMgr, iLevel, {
        39241: 1,
        39251: 1 }, 3) and warcondition.WarCheckSpecifcMode(oWarMgr, iLevel, 1002) == 0:
        pass
    return warcondition.WarCheckCycle(oWarMgr, iLevel, 9) == 0


def ForceAction41403003(oWarMgr, iLevel):
    if warcondition.WarCheckForceLevel(oWarMgr, iLevel, {
        39241: 1,
        39251: 1 }, 3) and warcondition.WarCheckSpecifcMode(oWarMgr, iLevel, 1002) == 0:
        pass
    return warcondition.WarCheckCycle(oWarMgr, iLevel, 9) == 0


def ChooseAction41403004(oWarMgr, iLevel):
    if warcondition.WarCheckSpecifcMode(oWarMgr, iLevel, 1002) or warcondition.WarCheckCycle(oWarMgr, iLevel, 9):
        pass
    return warcondition.WarCheckHistoryKillBoss(oWarMgr, iLevel, {
        39241: 1,
        39251: 1 }, 3)


def ForceAction41403004(oWarMgr, iLevel):
    if not warcondition.WarCheckForceLevel(oWarMgr, iLevel, {
        39241: 1,
        39251: 1 }, 3) and warcondition.WarCheckSpecifcMode(oWarMgr, iLevel, 1002):
        pass
    return warcondition.WarCheckCycle(oWarMgr, iLevel, 9)


class CInitResourceElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'INITBULLET': ((4502, 60), (4503, 25), (4504, 12), (4508, 8)) }


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
                        (1120, 0),
                        (1121, 0)],
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
                        (1120, 0),
                        (1121, 0)],
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
                    1101009: 0,
                    1101006: 0,
                    1101007: 0 } },
            'NpcInfo': {
                'shop': {
                    1005: 10 },
                'craftsman': {
                    1018: 10 },
                'gscashshop': {
                    1054: 10 },
                'tasknpc': {
                    1065: 10 } },
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
                        (3, 9): None,
                        (3, 8): None,
                        (3, 0): [
                            (1003, 1)],
                        (2, 0): [
                            (1003, 1)],
                        (1, 0): None },
                    'SingleChallengeStore': {
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelRoomChallenge': {
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelExcludeChallenge': {
                        1: {
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
                        3: {
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
                        1: {
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
                        3: {
                            (1101217, 1, 0, (0, 1000), -1): 10,
                            (1101210, 1, 0, (0, 1000), -1): 10,
                            (1101209, 1, 0, (0, 1000), -1): 10,
                            (1101203, 1, 0, (0, 1000), -1): 10,
                            (1101202, 1, 0, (0, 1000), -1): 10,
                            (1101201, 1, 0, (0, 1000), -1): 10 } },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': {
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'AIlevelEnhance': 0 },
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
                        (3, 9): [
                            (1099, 1),
                            (1081, 1),
                            (1083, 1)],
                        (3, 8): [
                            (1077, 0),
                            (1081, 1),
                            (1100, 1)],
                        (3, 0): [
                            (1003, 1),
                            (1008, 1),
                            (1044, 1),
                            (1053, 1),
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
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelRoomChallenge': {
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelExcludeChallenge': {
                        1: {
                            1101201: [],
                            1101601: [],
                            7101602: [],
                            7101603: [],
                            7101604: [],
                            1101605: [] },
                        2: {
                            1101201: [],
                            1101601: [],
                            7101602: [],
                            7101603: [],
                            7101604: [],
                            1101605: [] },
                        3: {
                            1101201: [],
                            1101601: [
                                1001,
                                1004,
                                1008,
                                1073],
                            7101602: [],
                            7101603: [],
                            7101604: [],
                            1101605: [
                                1001,
                                1073] } },
                    'HideLevel': {
                        1: {
                            1101201: 1,
                            1101601: 5,
                            7101602: 5,
                            7101603: 5,
                            7101604: 5,
                            1101605: 5 },
                        2: {
                            1101201: 1,
                            1101601: 5,
                            7101602: 5,
                            7101603: 5,
                            7101604: 5,
                            1101605: 5 },
                        3: {
                            1101201: 1,
                            1101601: 5,
                            7101602: 5,
                            7101603: 5,
                            7101604: 5,
                            1101605: 5 } },
                    'HideLevelStore': {
                        1: {
                            (1101605, 5, 0, (40, 1000), -1): 10,
                            (7101604, 5, 1, (20, 1000), -1): 2,
                            (7101603, 5, 1, (0, 1000), -1): 4,
                            (7101602, 5, 1, (0, 1000), -1): 4,
                            (1101601, 5, 0, (0, 1000), -1): 10,
                            (1101201, 1, 0, (0, 1000), -1): 10 },
                        2: {
                            (1101605, 5, 0, (40, 1000), -1): 10,
                            (7101604, 5, 1, (20, 1000), -1): 2,
                            (7101603, 5, 1, (0, 1000), -1): 4,
                            (7101602, 5, 1, (0, 1000), -1): 4,
                            (1101601, 5, 0, (0, 1000), -1): 10,
                            (1101201, 1, 0, (0, 1000), -1): 10 },
                        3: {
                            (1101605, 5, 0, (40, 1000), -1): 10,
                            (7101604, 5, 1, (20, 1000), -1): 2,
                            (7101603, 5, 1, (0, 1000), -1): 4,
                            (7101602, 5, 1, (0, 1000), -1): 4,
                            (1101601, 5, 0, (0, 1000), -1): 10,
                            (1101201, 1, 0, (0, 1000), -1): 10 } },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': {
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'AIlevelEnhance': 0 },
                3: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (7103154, 7103165, 7103157, 7103159, 7103155, 7103158, 7103160, 7103161, 7103162),
                    'NormalFilter': {
                        7103154: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7103165: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7103157: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7103159: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7103155: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7103158: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7103160: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7103161: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7103162: {
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
                            (1053, 1),
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
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelExcludeChallenge': {
                        1: {
                            1101201: [],
                            1101601: [],
                            7101602: [],
                            7101603: [],
                            7101604: [],
                            1101605: [],
                            7101111: [],
                            1101204: [],
                            7101205: [],
                            1101206: [],
                            1101207: [],
                            7101208: [],
                            1101251: [],
                            1101252: [],
                            1101215: [],
                            1101216: [] },
                        2: {
                            1101201: [],
                            1101601: [],
                            7101602: [],
                            7101603: [],
                            7101604: [],
                            1101605: [],
                            7101111: [],
                            1101204: [],
                            7101205: [],
                            1101206: [],
                            1101207: [],
                            7101208: [],
                            1101251: [],
                            1101252: [],
                            1101215: [],
                            1101216: [] },
                        3: {
                            1101201: [],
                            1101601: [
                                1001,
                                1004,
                                1008,
                                1073],
                            7101602: [],
                            7101603: [],
                            7101604: [],
                            1101605: [
                                1001,
                                1073],
                            7101111: [],
                            1101204: [],
                            7101205: [],
                            1101206: [],
                            1101207: [],
                            7101208: [],
                            1101251: [],
                            1101252: [],
                            1101215: [],
                            1101216: [] } },
                    'HideLevel': {
                        1: {
                            1101201: 1,
                            1101601: 5,
                            7101602: 5,
                            7101603: 5,
                            7101604: 5,
                            1101605: 5,
                            7101111: 3,
                            1101204: 3,
                            7101205: 3,
                            1101206: 3,
                            1101207: 3,
                            7101208: 3,
                            1101251: 3,
                            1101252: 3,
                            1101215: 8,
                            1101216: 3 },
                        2: {
                            1101201: 1,
                            1101601: 5,
                            7101602: 5,
                            7101603: 5,
                            7101604: 5,
                            1101605: 5,
                            7101111: 3,
                            1101204: 3,
                            7101205: 3,
                            1101206: 3,
                            1101207: 3,
                            7101208: 3,
                            1101251: 3,
                            1101252: 3,
                            1101215: 8,
                            1101216: 3 },
                        3: {
                            1101201: 1,
                            1101601: 5,
                            7101602: 5,
                            7101603: 5,
                            7101604: 5,
                            1101605: 5,
                            7101111: 3,
                            1101204: 3,
                            7101205: 3,
                            1101206: 3,
                            1101207: 3,
                            7101208: 3,
                            1101251: 3,
                            1101252: 3,
                            1101215: 8,
                            1101216: 3 } },
                    'HideLevelStore': {
                        1: {
                            (1101216, 3, 4, (30, 1000), -1): 10,
                            (1101215, 8, 0, (40, 1000), -1): 10,
                            (1101252, 3, 4, (10, 1000), -1): 10,
                            (1101251, 3, 4, (0, 1000), -1): 10,
                            (7101208, 3, 2, (30, 1000), -1): 10,
                            (1101207, 3, 3, (40, 1000), -1): 10,
                            (1101206, 3, 3, (10, 1000), -1): 10,
                            (7101205, 3, 2, (10, 1000), -1): 10,
                            (1101204, 3, 0, (30, 1000), -1): 10,
                            (7101111, 3, 0, (0, 1000), -1): 10,
                            (1101605, 5, 0, (40, 1000), -1): 10,
                            (7101604, 5, 1, (20, 1000), -1): 2,
                            (7101603, 5, 1, (0, 1000), -1): 4,
                            (7101602, 5, 1, (0, 1000), -1): 4,
                            (1101601, 5, 0, (0, 1000), -1): 10,
                            (1101201, 1, 0, (0, 1000), -1): 10 },
                        2: {
                            (1101216, 3, 4, (30, 1000), -1): 10,
                            (1101215, 8, 0, (40, 1000), -1): 10,
                            (1101252, 3, 4, (10, 1000), -1): 10,
                            (1101251, 3, 4, (0, 1000), -1): 10,
                            (7101208, 3, 2, (30, 1000), -1): 10,
                            (1101207, 3, 3, (40, 1000), -1): 10,
                            (1101206, 3, 3, (10, 1000), -1): 10,
                            (7101205, 3, 2, (10, 1000), -1): 10,
                            (1101204, 3, 0, (30, 1000), -1): 10,
                            (7101111, 3, 0, (0, 1000), -1): 10,
                            (1101605, 5, 0, (40, 1000), -1): 10,
                            (7101604, 5, 1, (20, 1000), -1): 2,
                            (7101603, 5, 1, (0, 1000), -1): 4,
                            (7101602, 5, 1, (0, 1000), -1): 4,
                            (1101601, 5, 0, (0, 1000), -1): 10,
                            (1101201, 1, 0, (0, 1000), -1): 10 },
                        3: {
                            (1101216, 3, 4, (30, 1000), -1): 10,
                            (1101215, 8, 0, (40, 1000), -1): 10,
                            (1101252, 3, 4, (10, 1000), -1): 10,
                            (1101251, 3, 4, (0, 1000), -1): 10,
                            (7101208, 3, 2, (30, 1000), -1): 10,
                            (1101207, 3, 3, (40, 1000), -1): 10,
                            (1101206, 3, 3, (10, 1000), -1): 10,
                            (7101205, 3, 2, (10, 1000), -1): 10,
                            (1101204, 3, 0, (30, 1000), -1): 10,
                            (7101111, 3, 0, (0, 1000), -1): 10,
                            (1101605, 5, 0, (40, 1000), -1): 10,
                            (7101604, 5, 1, (20, 1000), -1): 2,
                            (7101603, 5, 1, (0, 1000), -1): 4,
                            (7101602, 5, 1, (0, 1000), -1): 4,
                            (1101601, 5, 0, (0, 1000), -1): 10,
                            (1101201, 1, 0, (0, 1000), -1): 10 } },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': {
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'AIlevelEnhance': 0 },
                4: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (7105104, 7105102, 7105103, 7105101, 7105105, 7105106, 7105107),
                    'NormalFilter': {
                        7105104: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7105102: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7105103: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7105101: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7105105: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7105106: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7105107: {
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
                            (1015, 1),
                            (1038, 1),
                            (1051, 1),
                            (1056, 1),
                            (1061, 1)],
                        (2, 0): [
                            (1002, 1),
                            (1015, 1),
                            (1034, 1),
                            (1051, 1),
                            (1056, 1),
                            (1060, 1)],
                        (1, 0): [
                            (1003, 1)] },
                    'SingleChallengeStore': {
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
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelExcludeChallenge': {
                        1: {
                            1101201: [],
                            7101603: [],
                            7101604: [],
                            1101605: [],
                            7101111: [],
                            1101204: [],
                            7101205: [],
                            1101206: [],
                            1101207: [],
                            7101208: [],
                            1101251: [],
                            1101252: [],
                            1101215: [],
                            1101216: [] },
                        2: {
                            1101201: [],
                            7101603: [],
                            7101604: [],
                            1101605: [],
                            7101111: [],
                            1101204: [],
                            7101205: [],
                            1101206: [],
                            1101207: [],
                            7101208: [],
                            1101251: [],
                            1101252: [],
                            1101215: [],
                            1101216: [] },
                        3: {
                            7101603: [],
                            7101604: [],
                            1101605: [
                                1001,
                                1073],
                            7101111: [],
                            1101204: [],
                            7101205: [],
                            1101206: [],
                            1101207: [],
                            7101208: [],
                            1101251: [],
                            1101252: [],
                            1101215: [],
                            1101216: [] } },
                    'HideLevel': {
                        1: {
                            1101201: 1,
                            7101603: 5,
                            7101604: 5,
                            1101605: 5,
                            7101111: 3,
                            1101204: 3,
                            7101205: 3,
                            1101206: 3,
                            1101207: 3,
                            7101208: 3,
                            1101251: 3,
                            1101252: 3,
                            1101215: 8,
                            1101216: 3 },
                        2: {
                            1101201: 1,
                            7101603: 5,
                            7101604: 5,
                            1101605: 5,
                            7101111: 3,
                            1101204: 3,
                            7101205: 3,
                            1101206: 3,
                            1101207: 3,
                            7101208: 3,
                            1101251: 3,
                            1101252: 3,
                            1101215: 8,
                            1101216: 3 },
                        3: {
                            7101603: 5,
                            7101604: 5,
                            1101605: 5,
                            7101111: 3,
                            1101204: 3,
                            7101205: 3,
                            1101206: 3,
                            1101207: 3,
                            7101208: 3,
                            1101251: 3,
                            1101252: 3,
                            1101215: 8,
                            1101216: 3 } },
                    'HideLevelStore': {
                        1: {
                            (1101216, 3, 4, (30, 1000), -1): 10,
                            (1101215, 8, 0, (40, 1000), -1): 10,
                            (1101252, 3, 4, (10, 1000), -1): 10,
                            (1101251, 3, 4, (0, 1000), -1): 10,
                            (7101208, 3, 2, (30, 1000), -1): 10,
                            (1101207, 3, 3, (40, 1000), -1): 10,
                            (1101206, 3, 3, (10, 1000), -1): 10,
                            (7101205, 3, 2, (10, 1000), -1): 10,
                            (1101204, 3, 0, (30, 1000), -1): 10,
                            (7101111, 3, 0, (0, 1000), -1): 10,
                            (1101605, 5, 0, (40, 1000), -1): 10,
                            (7101604, 5, 1, (20, 1000), -1): 6,
                            (7101603, 5, 1, (0, 1000), -1): 4,
                            (1101201, 1, 0, (0, 1000), -1): 10 },
                        2: {
                            (1101216, 3, 4, (30, 1000), -1): 10,
                            (1101215, 8, 0, (40, 1000), -1): 10,
                            (1101252, 3, 4, (10, 1000), -1): 10,
                            (1101251, 3, 4, (0, 1000), -1): 10,
                            (7101208, 3, 2, (30, 1000), -1): 10,
                            (1101207, 3, 3, (40, 1000), -1): 10,
                            (1101206, 3, 3, (10, 1000), -1): 10,
                            (7101205, 3, 2, (10, 1000), -1): 10,
                            (1101204, 3, 0, (30, 1000), -1): 10,
                            (7101111, 3, 0, (0, 1000), -1): 10,
                            (1101605, 5, 0, (40, 1000), -1): 10,
                            (7101604, 5, 1, (20, 1000), -1): 6,
                            (7101603, 5, 1, (0, 1000), -1): 4,
                            (1101201, 1, 0, (0, 1000), -1): 10 },
                        3: {
                            (1101216, 3, 4, (30, 1000), -1): 10,
                            (1101215, 8, 0, (40, 1000), -1): 10,
                            (1101252, 3, 4, (10, 1000), -1): 10,
                            (1101251, 3, 4, (0, 1000), -1): 10,
                            (7101208, 3, 2, (30, 1000), -1): 10,
                            (1101207, 3, 3, (40, 1000), -1): 10,
                            (1101206, 3, 3, (10, 1000), -1): 10,
                            (7101205, 3, 2, (10, 1000), -1): 10,
                            (1101204, 3, 0, (30, 1000), -1): 10,
                            (7101111, 3, 0, (0, 1000), -1): 10,
                            (1101605, 5, 0, (40, 1000), -1): 10,
                            (7101604, 5, 1, (20, 1000), -1): 6,
                            (7101603, 5, 1, (0, 1000), -1): 4 } },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': {
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'AIlevelEnhance': 0 } },
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
                    LAYER_CHOOSE_HIDE: (2, 0, 0, 99, {
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
                    LAYER_CHOOSE_HIDE: (2, 0, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 30,
                        4: 20 }, {
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1 }) },
                3: {
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
                    LAYER_CHOOSE_CHALLENGE: ((lambda *a: 1 + (Func221(*a) // 8) * 3), 0, 0, 99, {
                        1: 15,
                        2: 20,
                        3: 25,
                        4: 40 }, { }),
                    LAYER_CHOOSE_HIDE: (2, 0, 0, 99, {
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
                    LEVEL_TYPE_HALL: (0, 0) } },
            'MonsterAttAdjust': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        4: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        4: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * (15000 + Func204(*a) * 2500)), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (15000 + Func204(*a) * 2500)), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (15000 + Func204(*a) * 2500)), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                        ('MoveSpeed', (lambda *a: (Func204(*a) - 1) * 500 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] } },
            'EliteAttAdjust': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        4: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        4: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] } },
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
                    1202001: 0,
                    1202003: 0 } },
            'NpcInfo': {
                'shop': {
                    1005: 10 },
                'craftsman': {
                    1018: 10 },
                'gscashshop': {
                    1054: 10 },
                'tasknpc': {
                    1065: 10 } },
            'CtrlInfo': {
                1: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (7202111, 7202114, 7202115, 7202108, 7202109, 7202116, 7202110, 7202112, 7202113, 7202117, 7202118, 7202119),
                    'NormalFilter': {
                        7202111: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7202114: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7202115: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7202108: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7202109: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7202116: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7202110: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7202112: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7202113: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7202117: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7202118: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7202119: {
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
                            (1045, 1),
                            (1050, 1)],
                        (2, 0): [
                            (1007, 1),
                            (1015, 1),
                            (1050, 1)],
                        (1, 0): [
                            (1009, 1),
                            (1054, 1),
                            (1007, 1)] },
                    'SingleChallengeStore': {
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
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelExcludeChallenge': {
                        1: {
                            1201112: [],
                            1201114: [],
                            7201604: [],
                            1201115: [],
                            1201116: [],
                            1201117: [],
                            1204103: [],
                            7201202: [],
                            7201203: [],
                            1201213: [] },
                        2: {
                            1201112: [],
                            1201114: [],
                            7201603: [],
                            7201604: [],
                            1201115: [],
                            1201116: [],
                            1201117: [],
                            1204103: [],
                            7201202: [],
                            7201203: [],
                            1201213: [] },
                        3: {
                            1201112: [],
                            1201114: [],
                            7201603: [],
                            7201604: [],
                            1201115: [],
                            1201116: [],
                            1201117: [],
                            1204103: [],
                            7201202: [],
                            7201203: [],
                            1201213: [] } },
                    'HideLevel': {
                        1: {
                            1201112: 3,
                            1201114: 3,
                            7201604: 5,
                            1201115: 3,
                            1201116: 3,
                            1201117: 3,
                            1204103: 3,
                            7201202: 1,
                            7201203: 1,
                            1201213: 3 },
                        2: {
                            1201112: 3,
                            1201114: 3,
                            7201603: 5,
                            7201604: 5,
                            1201115: 3,
                            1201116: 3,
                            1201117: 3,
                            1204103: 3,
                            7201202: 1,
                            7201203: 1,
                            1201213: 3 },
                        3: {
                            1201112: 3,
                            1201114: 3,
                            7201603: 5,
                            7201604: 5,
                            1201115: 3,
                            1201116: 3,
                            1201117: 3,
                            1204103: 3,
                            7201202: 1,
                            7201203: 1,
                            1201213: 3 } },
                    'HideLevelStore': {
                        1: {
                            (1201213, 3, 1, (20, 1000), -1): 10,
                            (7201203, 1, 0, (0, 1000), -1): 10,
                            (7201202, 1, 0, (0, 1000), -1): 10,
                            (1204103, 3, 0, (40, 1000), -1): 10,
                            (1201117, 3, 0, (20, 1000), -1): 10,
                            (1201116, 3, 1, (20, 1000), -1): 10,
                            (1201115, 3, 1, (0, 1000), -1): 10,
                            (7201604, 5, 0, (10, 1000), -1): 10,
                            (1201114, 3, 0, (0, 1000), -1): 10,
                            (1201112, 3, 0, (0, 1000), -1): 10 },
                        2: {
                            (1201213, 3, 1, (20, 1000), -1): 10,
                            (7201203, 1, 0, (0, 1000), -1): 10,
                            (7201202, 1, 0, (0, 1000), -1): 10,
                            (1204103, 3, 0, (40, 1000), -1): 10,
                            (1201117, 3, 0, (20, 1000), -1): 10,
                            (1201116, 3, 1, (20, 1000), -1): 10,
                            (1201115, 3, 1, (0, 1000), -1): 10,
                            (7201604, 5, 2, (10, 1000), -1): 10,
                            (7201603, 5, 2, (20, 1000), -1): 10,
                            (1201114, 3, 0, (0, 1000), -1): 10,
                            (1201112, 3, 0, (0, 1000), -1): 10 },
                        3: {
                            (1201213, 3, 1, (20, 1000), -1): 10,
                            (7201203, 1, 0, (0, 1000), -1): 10,
                            (7201202, 1, 0, (0, 1000), -1): 10,
                            (1204103, 3, 0, (40, 1000), -1): 10,
                            (1201117, 3, 0, (20, 1000), -1): 10,
                            (1201116, 3, 1, (20, 1000), -1): 10,
                            (1201115, 3, 1, (0, 1000), -1): 10,
                            (7201604, 5, 2, (10, 1000), -1): 10,
                            (7201603, 5, 2, (20, 1000), -1): 10,
                            (1201114, 3, 0, (0, 1000), -1): 10,
                            (1201112, 3, 0, (0, 1000), -1): 10 } },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': {
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'AIlevelEnhance': 0 },
                2: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (7203143, 7203141, 7203147, 7203142, 7203144, 7203145, 7203146),
                    'NormalFilter': {
                        7203143: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7203141: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7203147: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7203142: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7203144: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7203145: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7203146: {
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
                        (3, 9): [
                            (1130, 1),
                            (1080, 1),
                            (1125, 1),
                            (1126, 1),
                            (1128, 1),
                            (1122, 0),
                            (1084, 1)],
                        (3, 8): [
                            (1051, 1),
                            (1106, 1),
                            (1083, 1),
                            (1100, 1),
                            (1101, 1)],
                        (3, 0): [
                            (1005, 1),
                            (1039, 1),
                            (1050, 1),
                            (1052, 1),
                            (1057, 1),
                            (1066, 1)],
                        (2, 0): [
                            (1005, 1),
                            (1011, 1),
                            (1035, 1),
                            (1050, 1),
                            (1052, 1),
                            (1057, 1),
                            (1065, 1)],
                        (1, 0): [
                            (1009, 1)] },
                    'SingleChallengeStore': {
                        (3, 9): [
                            (1130, 1),
                            (1080, 1),
                            (1125, 1),
                            (1126, 1),
                            (1122, 0),
                            (1084, 1)],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelRoomChallenge': {
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelExcludeChallenge': {
                        1: {
                            1201112: [],
                            1201114: [],
                            7201604: [],
                            1201115: [],
                            1201116: [],
                            1201117: [],
                            1204103: [],
                            7201203: [],
                            7201202: [],
                            1201220: [],
                            1201213: [] },
                        2: {
                            1201112: [],
                            1201114: [],
                            7201603: [],
                            7201604: [],
                            1201115: [],
                            1201116: [],
                            1201117: [],
                            1204103: [],
                            7201202: [],
                            7201203: [],
                            1201220: [],
                            1201213: [] },
                        3: {
                            1201112: [],
                            1201114: [],
                            7201603: [],
                            7201604: [],
                            1201115: [],
                            1201116: [],
                            1201117: [],
                            1204103: [],
                            7201202: [],
                            7201203: [],
                            1201220: [],
                            1201213: [] } },
                    'HideLevel': {
                        1: {
                            1201112: 3,
                            1201114: 3,
                            7201604: 5,
                            1201115: 3,
                            1201116: 3,
                            1201117: 3,
                            1204103: 3,
                            7201203: 1,
                            7201202: 1,
                            1201220: 8,
                            1201213: 3 },
                        2: {
                            1201112: 3,
                            1201114: 3,
                            7201603: 5,
                            7201604: 5,
                            1201115: 3,
                            1201116: 3,
                            1201117: 3,
                            1204103: 3,
                            7201202: 1,
                            7201203: 1,
                            1201220: 8,
                            1201213: 3 },
                        3: {
                            1201112: 3,
                            1201114: 3,
                            7201603: 5,
                            7201604: 5,
                            1201115: 3,
                            1201116: 3,
                            1201117: 3,
                            1204103: 3,
                            7201202: 1,
                            7201203: 1,
                            1201220: 8,
                            1201213: 3 } },
                    'HideLevelStore': {
                        1: {
                            (1201213, 3, 1, (20, 1000), -1): 10,
                            (1201220, 8, 0, (40, 1000), -1): 10,
                            (7201202, 1, 0, (0, 1000), -1): 10,
                            (7201203, 1, 0, (0, 1000), -1): 10,
                            (1204103, 3, 0, (40, 1000), -1): 10,
                            (1201117, 3, 0, (20, 1000), -1): 10,
                            (1201116, 3, 1, (20, 1000), -1): 10,
                            (1201115, 3, 1, (0, 1000), -1): 10,
                            (7201604, 5, 0, (10, 1000), -1): 10,
                            (1201114, 3, 0, (0, 1000), -1): 10,
                            (1201112, 3, 0, (0, 1000), -1): 10 },
                        2: {
                            (1201213, 3, 1, (20, 1000), -1): 10,
                            (1201220, 8, 0, (40, 1000), -1): 10,
                            (7201203, 1, 0, (0, 1000), -1): 10,
                            (7201202, 1, 0, (0, 1000), -1): 10,
                            (1204103, 3, 0, (40, 1000), -1): 10,
                            (1201117, 3, 0, (20, 1000), -1): 10,
                            (1201116, 3, 1, (20, 1000), -1): 10,
                            (1201115, 3, 1, (0, 1000), -1): 10,
                            (7201604, 5, 2, (10, 1000), -1): 10,
                            (7201603, 5, 2, (20, 1000), -1): 10,
                            (1201114, 3, 0, (0, 1000), -1): 10,
                            (1201112, 3, 0, (0, 1000), -1): 10 },
                        3: {
                            (1201213, 3, 1, (20, 1000), -1): 10,
                            (1201220, 8, 0, (40, 1000), -1): 10,
                            (7201203, 1, 0, (0, 1000), -1): 10,
                            (7201202, 1, 0, (0, 1000), -1): 10,
                            (1204103, 3, 0, (40, 1000), -1): 10,
                            (1201117, 3, 0, (20, 1000), -1): 10,
                            (1201116, 3, 1, (20, 1000), -1): 10,
                            (1201115, 3, 1, (0, 1000), -1): 10,
                            (7201604, 5, 2, (10, 1000), -1): 10,
                            (7201603, 5, 2, (20, 1000), -1): 10,
                            (1201114, 3, 0, (0, 1000), -1): 10,
                            (1201112, 3, 0, (0, 1000), -1): 10 } },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': {
                        (3, 9): [
                            (1120404, 9),
                            (1120108, 6)],
                        (3, 8): [
                            (1120404, 9),
                            (1120108, 6),
                            (1120342, 2),
                            (1120342, 3),
                            (1120342, 4)],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'AIlevelEnhance': 0 },
                3: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (7205101, 7205104, 7205103, 7205107, 7205102, 7205108, 7205105, 7205106, 7205110, 7205109),
                    'NormalFilter': {
                        7205101: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7205104: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7205103: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7205107: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7205102: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7205108: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7205105: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7205106: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7205110: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7205109: {
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
                        (3, 9): [
                            (1051, 1),
                            (1082, 1),
                            (1124, 1),
                            (1116, 1),
                            (1105, 1),
                            (1122, 0),
                            (1121, 1),
                            (1120, 1)],
                        (3, 8): [
                            (1081, 1),
                            (1074, 1),
                            (1079, 1),
                            (1089, 1),
                            (1103, 1)],
                        (3, 0): [
                            (1026, 1),
                            (1027, 1),
                            (1043, 1),
                            (1052, 1),
                            (1054, 1),
                            (1055, 1),
                            (1057, 1)],
                        (2, 0): [
                            (1018, 1),
                            (1026, 1),
                            (1027, 1),
                            (1054, 1)],
                        (1, 0): [
                            (1030, 1),
                            (1035, 1),
                            (1065, 1)] },
                    'SingleChallengeStore': {
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelRoomChallenge': {
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelExcludeChallenge': {
                        1: {
                            1201112: [],
                            1201114: [],
                            7201604: [],
                            1201115: [],
                            1201116: [],
                            1201117: [],
                            1204103: [],
                            7201202: [],
                            7201203: [],
                            1201220: [],
                            1201213: [] },
                        2: {
                            1201112: [],
                            1201114: [],
                            7201603: [],
                            7201604: [],
                            1201115: [],
                            1201116: [],
                            1201117: [],
                            1204103: [],
                            7201202: [],
                            7201203: [],
                            1201220: [],
                            1201213: [] },
                        3: {
                            1201112: [],
                            1201114: [],
                            7201603: [],
                            7201604: [],
                            1201115: [],
                            1201116: [],
                            1201117: [],
                            1204103: [],
                            7201202: [],
                            7201203: [],
                            1201220: [],
                            1201213: [] } },
                    'HideLevel': {
                        1: {
                            1201112: 3,
                            1201114: 3,
                            7201604: 5,
                            1201115: 3,
                            1201116: 3,
                            1201117: 3,
                            1204103: 3,
                            7201202: 1,
                            7201203: 1,
                            1201220: 8,
                            1201213: 3 },
                        2: {
                            1201112: 3,
                            1201114: 3,
                            7201603: 5,
                            7201604: 5,
                            1201115: 3,
                            1201116: 3,
                            1201117: 3,
                            1204103: 3,
                            7201202: 1,
                            7201203: 1,
                            1201220: 8,
                            1201213: 3 },
                        3: {
                            1201112: 3,
                            1201114: 3,
                            7201603: 5,
                            7201604: 5,
                            1201115: 3,
                            1201116: 3,
                            1201117: 3,
                            1204103: 3,
                            7201202: 1,
                            7201203: 1,
                            1201220: 8,
                            1201213: 3 } },
                    'HideLevelStore': {
                        1: {
                            (1201213, 3, 1, (20, 1000), -1): 10,
                            (1201220, 8, 0, (40, 1000), -1): 10,
                            (7201203, 1, 0, (0, 1000), -1): 10,
                            (7201202, 1, 0, (0, 1000), -1): 10,
                            (1204103, 3, 0, (40, 1000), -1): 10,
                            (1201117, 3, 0, (20, 1000), -1): 10,
                            (1201116, 3, 1, (20, 1000), -1): 10,
                            (1201115, 3, 1, (0, 1000), -1): 10,
                            (7201604, 5, 0, (10, 1000), -1): 10,
                            (1201114, 3, 0, (0, 1000), -1): 10,
                            (1201112, 3, 0, (0, 1000), -1): 10 },
                        2: {
                            (1201213, 3, 1, (20, 1000), -1): 10,
                            (1201220, 8, 0, (40, 1000), -1): 10,
                            (7201203, 1, 0, (0, 1000), -1): 10,
                            (7201202, 1, 0, (0, 1000), -1): 10,
                            (1204103, 3, 0, (40, 1000), -1): 10,
                            (1201117, 3, 0, (20, 1000), -1): 10,
                            (1201116, 3, 1, (20, 1000), -1): 10,
                            (1201115, 3, 1, (0, 1000), -1): 10,
                            (7201604, 5, 2, (10, 1000), -1): 10,
                            (7201603, 5, 2, (20, 1000), -1): 10,
                            (1201114, 3, 0, (0, 1000), -1): 10,
                            (1201112, 3, 0, (0, 1000), -1): 10 },
                        3: {
                            (1201213, 3, 1, (20, 1000), -1): 10,
                            (1201220, 8, 0, (40, 1000), -1): 10,
                            (7201203, 1, 0, (0, 1000), -1): 10,
                            (7201202, 1, 0, (0, 1000), -1): 10,
                            (1204103, 3, 0, (40, 1000), -1): 10,
                            (1201117, 3, 0, (20, 1000), -1): 10,
                            (1201116, 3, 1, (20, 1000), -1): 10,
                            (1201115, 3, 1, (0, 1000), -1): 10,
                            (7201604, 5, 2, (10, 1000), -1): 10,
                            (7201603, 5, 2, (20, 1000), -1): 10,
                            (1201114, 3, 0, (0, 1000), -1): 10,
                            (1201112, 3, 0, (0, 1000), -1): 10 } },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': {
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'AIlevelEnhance': 0 } },
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
                    LAYER_CHOOSE_HIDE: (2, 0, 0, 99, {
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
                    LAYER_CHOOSE_HIDE: (2, 0, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }) },
                3: {
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
                    LAYER_CHOOSE_CHALLENGE: ((lambda *a: 1 + (Func221(*a) // 8) * 5), 0, 0, 99, {
                        1: 30,
                        2: 30,
                        3: 40 }, { }),
                    LAYER_CHOOSE_HIDE: (2, 0, 0, 99, {
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
                    LEVEL_TYPE_HALL: (0, 0) } },
            'MonsterAttAdjust': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * (15000 + Func204(*a) * 2500)), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (15000 + Func204(*a) * 2500)), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (15000 + Func204(*a) * 2500)), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                        ('MoveSpeed', (lambda *a: (Func204(*a) - 1) * 500 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] } },
            'EliteAttAdjust': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] } },
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
                    1301002: 0,
                    1301003: 0 } },
            'NpcInfo': {
                'shop': {
                    1005: 10 },
                'craftsman': {
                    1018: 10 },
                'gscashshop': {
                    1054: 10 },
                'tasknpc': {
                    1065: 10 } },
            'CtrlInfo': {
                1: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (7301104, 7301108, 7301107, 7301101, 7301102, 7301103, 7301106, 7301105),
                    'NormalFilter': {
                        7301104: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7301108: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7301107: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7301101: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7301102: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7301103: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7301106: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7301105: {
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
                            (1068, 1)],
                        (2, 0): [
                            (1029, 1),
                            (1067, 1)],
                        (1, 0): [
                            (1028, 1),
                            (1067, 1)] },
                    'SingleChallengeStore': {
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelRoomChallenge': {
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelExcludeChallenge': {
                        1: {
                            1300104: [],
                            1300105: [],
                            1300106: [],
                            1300107: [],
                            1300108: [],
                            1300109: [],
                            1300110: [],
                            7301201: [],
                            7301202: [],
                            7300102: [],
                            7300103: [],
                            1300111: [] },
                        2: {
                            1300104: [],
                            1300105: [],
                            1300106: [],
                            1300107: [],
                            1300108: [],
                            1300109: [],
                            1300110: [],
                            7301201: [],
                            7301202: [],
                            7300102: [],
                            7300103: [],
                            1300111: [] },
                        3: {
                            1300104: [],
                            1300105: [],
                            1300106: [],
                            1300107: [],
                            1300108: [],
                            1300109: [],
                            1300110: [],
                            7301201: [],
                            7301202: [],
                            7300102: [],
                            7300103: [],
                            1300111: [] } },
                    'HideLevel': {
                        1: {
                            1300104: 8,
                            1300105: 3,
                            1300106: 3,
                            1300107: 3,
                            1300108: 3,
                            1300109: 3,
                            1300110: 3,
                            7301201: 1,
                            7301202: 1,
                            7300102: 3,
                            7300103: 3,
                            1300111: 3 },
                        2: {
                            1300104: 8,
                            1300105: 3,
                            1300106: 3,
                            1300107: 3,
                            1300108: 3,
                            1300109: 3,
                            1300110: 3,
                            7301201: 1,
                            7301202: 1,
                            7300102: 3,
                            7300103: 3,
                            1300111: 3 },
                        3: {
                            1300104: 8,
                            1300105: 3,
                            1300106: 3,
                            1300107: 3,
                            1300108: 3,
                            1300109: 3,
                            1300110: 3,
                            7301201: 1,
                            7301202: 1,
                            7300102: 3,
                            7300103: 3,
                            1300111: 3 } },
                    'HideLevelStore': {
                        1: {
                            (1300111, 3, 4, (10, 1000), -1): 10,
                            (7300103, 3, 1, (20, 1000), -1): 10,
                            (7300102, 3, 1, (0, 1000), -1): 10,
                            (7301202, 1, 0, (0, 1000), -1): 10,
                            (7301201, 1, 0, (0, 1000), -1): 10,
                            (1300110, 3, 3, (0, 1000), -1): 10,
                            (1300109, 3, 2, (0, 1000), -1): 10,
                            (1300108, 3, 3, (20, 1000), -1): 10,
                            (1300107, 3, 2, (40, 1000), -1): 10,
                            (1300106, 3, 0, (40, 1000), -1): 10,
                            (1300105, 3, 4, (40, 1000), -1): 10,
                            (1300104, 8, 0, (40, 1000), -1): 0 },
                        2: {
                            (1300111, 3, 4, (10, 1000), -1): 10,
                            (7300103, 3, 1, (20, 1000), -1): 10,
                            (7300102, 3, 1, (0, 1000), -1): 10,
                            (7301202, 1, 0, (0, 1000), -1): 10,
                            (7301201, 1, 0, (0, 1000), -1): 10,
                            (1300110, 3, 3, (10, 1000), -1): 10,
                            (1300109, 3, 2, (0, 1000), -1): 10,
                            (1300108, 3, 3, (20, 1000), -1): 10,
                            (1300107, 3, 2, (40, 1000), -1): 10,
                            (1300106, 3, 0, (40, 1000), -1): 10,
                            (1300105, 3, 4, (40, 1000), -1): 10,
                            (1300104, 8, 0, (40, 1000), -1): 0 },
                        3: {
                            (1300111, 3, 4, (10, 1000), -1): 10,
                            (7300103, 3, 1, (20, 1000), -1): 10,
                            (7300102, 3, 1, (0, 1000), -1): 10,
                            (7301202, 1, 0, (0, 1000), -1): 10,
                            (7301201, 1, 0, (0, 1000), -1): 10,
                            (1300110, 3, 3, (10, 1000), -1): 10,
                            (1300109, 3, 2, (0, 1000), -1): 10,
                            (1300108, 3, 3, (20, 1000), -1): 10,
                            (1300107, 3, 2, (40, 1000), -1): 10,
                            (1300106, 3, 0, (40, 1000), -1): 10,
                            (1300105, 3, 4, (40, 1000), -1): 10,
                            (1300104, 8, 0, (40, 1000), -1): 0 } },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': {
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'AIlevelEnhance': 0 },
                2: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (7302107, 7302161, 7302162, 7302104, 7302103, 7302101, 7302102, 7302105, 7302108, 7302120),
                    'NormalFilter': {
                        7302107: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7302161: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7302162: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7302104: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7302103: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7302101: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7302102: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7302105: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7302108: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7302120: {
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
                            (1052, 1),
                            (1056, 1)],
                        (2, 0): [
                            (1017, 1),
                            (1024, 1),
                            (1030, 1),
                            (1053, 1)],
                        (1, 0): [
                            (1024, 1)] },
                    'SingleChallengeStore': {
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelRoomChallenge': {
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelExcludeChallenge': {
                        1: {
                            1300105: [],
                            1300106: [],
                            1300107: [],
                            1300108: [],
                            1300109: [],
                            1300110: [],
                            7301201: [],
                            7301202: [],
                            7300102: [],
                            7300103: [],
                            1300111: [],
                            1300104: [] },
                        2: {
                            1300105: [],
                            1300106: [],
                            1300107: [],
                            1300108: [],
                            1300109: [],
                            1300110: [],
                            7301201: [],
                            7301202: [],
                            7300102: [],
                            7300103: [],
                            1300111: [],
                            1300104: [] },
                        3: {
                            1300105: [],
                            1300106: [],
                            1300107: [],
                            1300108: [],
                            1300109: [],
                            1300110: [],
                            7301201: [],
                            7301202: [],
                            7300102: [],
                            7300103: [],
                            1300111: [],
                            1300104: [] } },
                    'HideLevel': {
                        1: {
                            1300105: 3,
                            1300106: 3,
                            1300107: 3,
                            1300108: 3,
                            1300109: 3,
                            1300110: 3,
                            7301201: 1,
                            7301202: 1,
                            7300102: 3,
                            7300103: 3,
                            1300111: 3,
                            1300104: 8 },
                        2: {
                            1300105: 3,
                            1300106: 3,
                            1300107: 3,
                            1300108: 3,
                            1300109: 3,
                            1300110: 3,
                            7301201: 1,
                            7301202: 1,
                            7300102: 3,
                            7300103: 3,
                            1300111: 3,
                            1300104: 8 },
                        3: {
                            1300105: 3,
                            1300106: 3,
                            1300107: 3,
                            1300108: 3,
                            1300109: 3,
                            1300110: 3,
                            7301201: 1,
                            7301202: 1,
                            7300102: 3,
                            7300103: 3,
                            1300111: 3,
                            1300104: 8 } },
                    'HideLevelStore': {
                        1: {
                            (1300104, 8, 0, (40, 1000), -1): 10,
                            (1300111, 3, 4, (10, 1000), -1): 10,
                            (7300103, 3, 1, (20, 1000), -1): 10,
                            (7300102, 3, 1, (0, 1000), -1): 10,
                            (7301202, 1, 0, (0, 1000), -1): 10,
                            (7301201, 1, 0, (0, 1000), -1): 10,
                            (1300110, 3, 3, (0, 1000), -1): 10,
                            (1300109, 3, 2, (0, 1000), -1): 10,
                            (1300108, 3, 3, (20, 1000), -1): 10,
                            (1300107, 3, 2, (40, 1000), -1): 10,
                            (1300106, 3, 0, (40, 1000), -1): 10,
                            (1300105, 3, 4, (40, 1000), -1): 10 },
                        2: {
                            (1300104, 8, 0, (40, 1000), -1): 10,
                            (1300111, 3, 4, (10, 1000), -1): 10,
                            (7300103, 3, 1, (20, 1000), -1): 10,
                            (7300102, 3, 1, (0, 1000), -1): 10,
                            (7301202, 1, 0, (0, 1000), -1): 10,
                            (7301201, 1, 0, (0, 1000), -1): 10,
                            (1300110, 3, 3, (10, 1000), -1): 10,
                            (1300109, 3, 2, (0, 1000), -1): 10,
                            (1300108, 3, 3, (20, 1000), -1): 10,
                            (1300107, 3, 2, (40, 1000), -1): 10,
                            (1300106, 3, 0, (40, 1000), -1): 10,
                            (1300105, 3, 4, (40, 1000), -1): 10 },
                        3: {
                            (1300104, 8, 0, (40, 1000), -1): 10,
                            (1300111, 3, 4, (10, 1000), -1): 10,
                            (7300103, 3, 1, (20, 1000), -1): 10,
                            (7300102, 3, 1, (0, 1000), -1): 10,
                            (7301202, 1, 0, (0, 1000), -1): 10,
                            (7301201, 1, 0, (0, 1000), -1): 10,
                            (1300110, 3, 3, (10, 1000), -1): 10,
                            (1300109, 3, 2, (0, 1000), -1): 10,
                            (1300108, 3, 3, (20, 1000), -1): 10,
                            (1300107, 3, 2, (40, 1000), -1): 10,
                            (1300106, 3, 0, (40, 1000), -1): 10,
                            (1300105, 3, 4, (40, 1000), -1): 10 } },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': {
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'AIlevelEnhance': 0 },
                3: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (7303106, 7303105, 7303102, 7303104, 7303101, 7303103, 7303108, 7303107),
                    'NormalFilter': {
                        7303106: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7303105: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7303102: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7303104: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7303101: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7303103: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7303108: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7303107: {
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
                            (1064, 1)],
                        (2, 0): [
                            (1016, 1),
                            (1030, 1),
                            (1036, 1),
                            (1037, 1),
                            (1063, 1)],
                        (1, 0): [
                            (1025, 1),
                            (1029, 1)] },
                    'SingleChallengeStore': {
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelRoomChallenge': {
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelExcludeChallenge': {
                        1: {
                            1300105: [],
                            1300106: [],
                            1300107: [],
                            1300108: [],
                            1300109: [],
                            1300110: [],
                            7301201: [],
                            7301202: [],
                            7300102: [],
                            7300103: [],
                            1300111: [],
                            1300104: [] },
                        2: {
                            1300105: [],
                            1300106: [],
                            1300107: [],
                            1300108: [],
                            1300109: [],
                            1300110: [],
                            7301201: [],
                            7301202: [],
                            7300102: [],
                            7300103: [],
                            1300111: [],
                            1300104: [] },
                        3: {
                            1300105: [],
                            1300106: [],
                            1300107: [],
                            1300108: [],
                            1300109: [],
                            1300110: [],
                            7301201: [],
                            7301202: [],
                            7300102: [],
                            7300103: [],
                            1300111: [],
                            1300104: [] } },
                    'HideLevel': {
                        1: {
                            1300105: 3,
                            1300106: 3,
                            1300107: 3,
                            1300108: 3,
                            1300109: 3,
                            1300110: 3,
                            7301201: 1,
                            7301202: 1,
                            7300102: 3,
                            7300103: 3,
                            1300111: 3,
                            1300104: 8 },
                        2: {
                            1300105: 3,
                            1300106: 3,
                            1300107: 3,
                            1300108: 3,
                            1300109: 3,
                            1300110: 3,
                            7301201: 1,
                            7301202: 1,
                            7300102: 3,
                            7300103: 3,
                            1300111: 3,
                            1300104: 8 },
                        3: {
                            1300105: 3,
                            1300106: 3,
                            1300107: 3,
                            1300108: 3,
                            1300109: 3,
                            1300110: 3,
                            7301201: 1,
                            7301202: 1,
                            7300102: 3,
                            7300103: 3,
                            1300111: 3,
                            1300104: 8 } },
                    'HideLevelStore': {
                        1: {
                            (1300104, 8, 0, (40, 1000), -1): 10,
                            (1300111, 3, 4, (10, 1000), -1): 10,
                            (7300103, 3, 1, (20, 1000), -1): 10,
                            (7300102, 3, 1, (0, 1000), -1): 10,
                            (7301202, 1, 0, (0, 1000), -1): 10,
                            (7301201, 1, 0, (0, 1000), -1): 10,
                            (1300110, 3, 3, (0, 1000), -1): 10,
                            (1300109, 3, 2, (0, 1000), -1): 10,
                            (1300108, 3, 3, (20, 1000), -1): 10,
                            (1300107, 3, 2, (40, 1000), -1): 10,
                            (1300106, 3, 0, (40, 1000), -1): 10,
                            (1300105, 3, 4, (40, 1000), -1): 10 },
                        2: {
                            (1300104, 8, 0, (40, 1000), -1): 10,
                            (1300111, 3, 4, (10, 1000), -1): 10,
                            (7300103, 3, 1, (20, 1000), -1): 10,
                            (7300102, 3, 1, (0, 1000), -1): 10,
                            (7301202, 1, 0, (0, 1000), -1): 10,
                            (7301201, 1, 0, (0, 1000), -1): 10,
                            (1300110, 3, 3, (10, 1000), -1): 10,
                            (1300109, 3, 2, (0, 1000), -1): 10,
                            (1300108, 3, 3, (20, 1000), -1): 10,
                            (1300107, 3, 2, (40, 1000), -1): 10,
                            (1300106, 3, 0, (40, 1000), -1): 10,
                            (1300105, 3, 4, (40, 1000), -1): 10 },
                        3: {
                            (1300104, 8, 0, (40, 1000), -1): 10,
                            (1300111, 3, 4, (10, 1000), -1): 10,
                            (7300103, 3, 1, (20, 1000), -1): 10,
                            (7300102, 3, 1, (0, 1000), -1): 10,
                            (7301202, 1, 0, (0, 1000), -1): 10,
                            (7301201, 1, 0, (0, 1000), -1): 10,
                            (1300110, 3, 3, (10, 1000), -1): 10,
                            (1300109, 3, 2, (0, 1000), -1): 10,
                            (1300108, 3, 3, (20, 1000), -1): 10,
                            (1300107, 3, 2, (40, 1000), -1): 10,
                            (1300106, 3, 0, (40, 1000), -1): 10,
                            (1300105, 3, 4, (40, 1000), -1): 10 } },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': {
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'AIlevelEnhance': 0 } },
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
                    LAYER_CHOOSE_HIDE: (2, 0, 0, 99, {
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
                    LAYER_CHOOSE_HIDE: (2, 0, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 1,
                        3: 1 }) },
                3: {
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
                    LAYER_CHOOSE_CHALLENGE: ((lambda *a: 1 + (Func221(*a) // 8) * 6), 0, 0, 99, {
                        1: 30,
                        2: 30,
                        3: 40 }, { }),
                    LAYER_CHOOSE_HIDE: (2, 0, 0, 99, {
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
                    LEVEL_TYPE_HALL: (0, 0) } },
            'MonsterAttAdjust': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * (15000 + Func204(*a) * 2500)), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (15000 + Func204(*a) * 2500)), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (15000 + Func204(*a) * 2500)), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                        ('MoveSpeed', (lambda *a: (Func204(*a) - 1) * 500 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] } },
            'EliteAttAdjust': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] } },
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
                    1403001: 0,
                    1403002: 0,
                    1403003: 0,
                    1403004: 0 } },
            'NpcInfo': {
                'shop': {
                    1059: 10 },
                'craftsman': {
                    1018: 10 },
                'gscashshop': {
                    1054: 10 },
                'tasknpc': {
                    1065: 10 } },
            'CtrlInfo': {
                1: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (7401101, 7401102, 7401103, 7401104, 7401105, 7401106, 7401107),
                    'NormalFilter': {
                        7401101: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7401102: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7401103: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7401104: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7401105: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7401106: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7401107: {
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
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelRoomChallenge': {
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelExcludeChallenge': {
                        1: {
                            7401201: [],
                            7401205: [],
                            7401204: [] },
                        2: {
                            7401201: [],
                            7401205: [],
                            7401204: [] },
                        3: {
                            7401201: [],
                            7401205: [],
                            7401204: [] } },
                    'HideLevel': {
                        1: {
                            7401201: 1,
                            7401205: 3,
                            7401204: 3 },
                        2: {
                            7401201: 1,
                            7401205: 3,
                            7401204: 3 },
                        3: {
                            7401201: 1,
                            7401205: 3,
                            7401204: 3 } },
                    'HideLevelStore': {
                        1: {
                            (7401204, 3, 0, (0, 1000), -1): 10,
                            (7401205, 3, 0, (0, 1000), -1): 10,
                            (7401201, 1, 0, (0, 1000), -1): 10 },
                        2: {
                            (7401204, 3, 0, (0, 1000), -1): 10,
                            (7401205, 3, 0, (0, 1000), -1): 10,
                            (7401201, 1, 0, (0, 1000), -1): 10 },
                        3: {
                            (7401204, 3, 0, (0, 1000), -1): 10,
                            (7401205, 3, 0, (0, 1000), -1): 10,
                            (7401201, 1, 0, (0, 1000), -1): 10 } },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': {
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'AIlevelEnhance': 0 },
                2: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (7402103, 7402104, 7402102, 7402101, 7402105, 7402106, 7402107, 7402108),
                    'NormalFilter': {
                        7402103: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7402104: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7402102: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7402101: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7402105: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7402106: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7402107: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7402108: {
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
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelRoomChallenge': {
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelExcludeChallenge': {
                        1: {
                            7401202: [],
                            7401203: [],
                            1401206: [] },
                        2: {
                            7401202: [],
                            7401203: [],
                            1401206: [] },
                        3: {
                            7401202: [],
                            7401203: [],
                            1401206: [] } },
                    'HideLevel': {
                        1: {
                            7401202: 3,
                            7401203: 1,
                            1401206: 1 },
                        2: {
                            7401202: 3,
                            7401203: 1,
                            1401206: 1 },
                        3: {
                            7401202: 3,
                            7401203: 1,
                            1401206: 1 } },
                    'HideLevelStore': {
                        1: {
                            (1401206, 1, 0, (0, 1000), -1): 10,
                            (7401203, 1, 0, (0, 1000), -1): 10,
                            (7401202, 3, 0, (0, 1000), -1): 10 },
                        2: {
                            (1401206, 1, 0, (0, 1000), -1): 10,
                            (7401203, 1, 0, (0, 1000), -1): 10,
                            (7401202, 3, 0, (0, 1000), -1): 10 },
                        3: {
                            (1401206, 1, 0, (0, 1000), -1): 10,
                            (7401203, 1, 0, (0, 1000), -1): 10,
                            (7401202, 3, 0, (0, 1000), -1): 10 } },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': {
                        (3, 9): [],
                        (3, 8): [],
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'AIlevelEnhance': 0 } },
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
                    LAYER_CHOOSE_HIDE: (1, 0, 0, 99, {
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
                    LAYER_CHOOSE_HIDE: (1, 0, 0, 99, {
                        1: 10,
                        2: 10 }, {
                        1: 1,
                        2: 1 }) },
                3: {
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
                    LAYER_CHOOSE_HIDE: (1, 0, 0, 99, {
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
                    LEVEL_TYPE_HALL: (0, 0) } },
            'MonsterAttAdjust': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * (15000 + Func204(*a) * 2500)), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (15000 + Func204(*a) * 2500)), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (15000 + Func204(*a) * 2500)), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                        ('MoveSpeed', (lambda *a: (Func204(*a) - 1) * 500 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (-500 * Func204(*a) * Func204(*a) + 4500 * Func204(*a) - 2000)), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] } },
            'EliteAttAdjust': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * (7500 + Func204(*a) * 2500)), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 3000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] } },
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
    m_SightLevelConf = { }


class CWarreport(cl_warmgr.mobject.CElementData):
    pass


class CPVEDieElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'RelifeData': 1004,
        'InitDyingSecond': 20,
        'MinDyingSecond': 5,
        'TimesSubSecond': {
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
            'MoveSpeed': 1500 },
        3: {
            'MoveSpeed': 2500 } }
    m_CycleMonsterAttrAdjust = {
        1: { },
        2: { },
        3: {
            1: {
                (0, 0): {
                    0: {
                        'Att': (lambda *a: min(int(Func201(*a) * 300 + Func202(*a) * 50 - 100), 1000)),
                        'HPMax': (lambda *a: min(int(Func201(*a) * 4000 + Func202(*a) * 800 - 4000), int(12000 + Func544(*a, **{
'sAttr': 'HPMax' })))),
                        'ArmorMax': (lambda *a: min(int(Func201(*a) * 4000 + Func202(*a) * 800 - 4000), int(12000 + Func544(*a, **{
'sAttr': 'ArmorMax' })))),
                        'ShieldMax': (lambda *a: min(int(Func201(*a) * 4000 + Func202(*a) * 800 - 4000), int(12000 + Func544(*a, **{
'sAttr': 'ShieldMax' })))),
                        'MoveSpeed': 0 } } },
            2: {
                (0, 0): {
                    0: {
                        'Att': (lambda *a: min(int(Func201(*a) * 600 + Func202(*a) * 100 - 200), 2000)),
                        'HPMax': (lambda *a: min(int(Func201(*a) * 8000 + Func202(*a) * 1600 - 8000), int(24000 + Func544(*a, **{
'sAttr': 'HPMax' }) * 2))),
                        'ArmorMax': (lambda *a: min(int(Func201(*a) * 8000 + Func202(*a) * 1600 - 8000), int(24000 + Func544(*a, **{
'sAttr': 'ArmorMax' }) * 2))),
                        'ShieldMax': (lambda *a: min(int(Func201(*a) * 8000 + Func202(*a) * 1600 - 8000), int(24000 + Func544(*a, **{
'sAttr': 'ShieldMax' }) * 2))),
                        'MoveSpeed': 0 } } },
            3: {
                (0, 0): {
                    0: {
                        'Att': (lambda *a: min(int(Func201(*a) * 900 + Func202(*a) * 150 - 300), 3000)),
                        'HPMax': (lambda *a: min(int(Func201(*a) * 12000 + Func202(*a) * 2400 - 12000), int(36000 + Func544(*a, **{
'sAttr': 'HPMax' }) * 3))),
                        'ArmorMax': (lambda *a: min(int(Func201(*a) * 12000 + Func202(*a) * 2400 - 12000), int(36000 + Func544(*a, **{
'sAttr': 'ArmorMax' }) * 3))),
                        'ShieldMax': (lambda *a: min(int(Func201(*a) * 12000 + Func202(*a) * 2400 - 12000), int(36000 + Func544(*a, **{
'sAttr': 'ShieldMax' }) * 3))),
                        'MoveSpeed': 0 } } },
            4: {
                (0, 0): {
                    0: {
                        'Att': (lambda *a: min(int(Func201(*a) * 1200 + Func202(*a) * 200 - 400), 4000)),
                        'HPMax': (lambda *a: min(int(Func201(*a) * 16000 + Func202(*a) * 3200 - 16000), int(48000 + Func544(*a, **{
'sAttr': 'HPMax' }) * 4))),
                        'ArmorMax': (lambda *a: min(int(Func201(*a) * 16000 + Func202(*a) * 3200 - 16000), int(48000 + Func544(*a, **{
'sAttr': 'ArmorMax' }) * 4))),
                        'ShieldMax': (lambda *a: min(int(Func201(*a) * 16000 + Func202(*a) * 3200 - 16000), int(48000 + Func544(*a, **{
'sAttr': 'ShieldMax' }) * 4))),
                        'MoveSpeed': 0 } } },
            5: {
                (0, 0): {
                    0: {
                        'Att': (lambda *a: min(int(Func201(*a) * 1500 + Func202(*a) * 250 - 500), 5000)),
                        'HPMax': (lambda *a: min(int(Func201(*a) * 20000 + Func202(*a) * 4000 - 20000), int(60000 + Func544(*a, **{
'sAttr': 'HPMax' }) * 5))),
                        'ArmorMax': (lambda *a: min(int(Func201(*a) * 20000 + Func202(*a) * 4000 - 20000), int(60000 + Func544(*a, **{
'sAttr': 'ArmorMax' }) * 5))),
                        'ShieldMax': (lambda *a: min(int(Func201(*a) * 20000 + Func202(*a) * 4000 - 20000), int(60000 + Func544(*a, **{
'sAttr': 'ShieldMax' }) * 5))),
                        'MoveSpeed': 0 } } },
            6: {
                (0, 0): {
                    0: {
                        'Att': (lambda *a: min(int(Func201(*a) * 1800 + Func202(*a) * 300 - 600), 6000)),
                        'HPMax': (lambda *a: min(int(Func201(*a) * 24000 + Func202(*a) * 4800 - 24000), int(72000 + Func544(*a, **{
'sAttr': 'HPMax' }) * 6))),
                        'ArmorMax': (lambda *a: min(int(Func201(*a) * 24000 + Func202(*a) * 4800 - 24000), int(72000 + Func544(*a, **{
'sAttr': 'ArmorMax' }) * 6))),
                        'ShieldMax': (lambda *a: min(int(Func201(*a) * 24000 + Func202(*a) * 4800 - 24000), int(72000 + Func544(*a, **{
'sAttr': 'ShieldMax' }) * 6))),
                        'MoveSpeed': 0 } } },
            7: {
                (0, 0): {
                    0: {
                        'Att': (lambda *a: min(int(Func201(*a) * 2100 + Func202(*a) * 350 - 700), 7000)),
                        'HPMax': (lambda *a: min(int(Func201(*a) * 28000 + Func202(*a) * 5600 - 28000), int(84000 + Func544(*a, **{
'sAttr': 'HPMax' }) * 7))),
                        'ArmorMax': (lambda *a: min(int(Func201(*a) * 28000 + Func202(*a) * 5600 - 28000), int(84000 + Func544(*a, **{
'sAttr': 'ArmorMax' }) * 7))),
                        'ShieldMax': (lambda *a: min(int(Func201(*a) * 28000 + Func202(*a) * 5600 - 28000), int(84000 + Func544(*a, **{
'sAttr': 'ShieldMax' }) * 7))),
                        'MoveSpeed': 0 } } },
            8: {
                (0, 0): {
                    0: {
                        'Att': (lambda *a: min(int(Func201(*a) * 2100 + Func202(*a) * 350 - 700), 7000)),
                        'HPMax': (lambda *a: min(int(Func201(*a) * 28000 + Func202(*a) * 5600 - 28000), int(84000 + Func544(*a, **{
'sAttr': 'HPMax' }) * 7))),
                        'ArmorMax': (lambda *a: min(int(Func201(*a) * 28000 + Func202(*a) * 5600 - 28000), int(84000 + Func544(*a, **{
'sAttr': 'ArmorMax' }) * 7))),
                        'ShieldMax': (lambda *a: min(int(Func201(*a) * 28000 + Func202(*a) * 5600 - 28000), int(84000 + Func544(*a, **{
'sAttr': 'ShieldMax' }) * 7))),
                        'MoveSpeed': 0 } } },
            9: {
                (0, 0): {
                    0: {
                        'Att': (lambda *a: min(int(Func201(*a) * 2100 + Func202(*a) * 350 - 700), 7000)),
                        'HPMax': (lambda *a: min(int(Func201(*a) * 28000 + Func202(*a) * 5600 - 28000), int(84000 + Func544(*a, **{
'sAttr': 'HPMax' }) * 7))),
                        'ArmorMax': (lambda *a: min(int(Func201(*a) * 28000 + Func202(*a) * 5600 - 28000), int(84000 + Func544(*a, **{
'sAttr': 'ArmorMax' }) * 7))),
                        'ShieldMax': (lambda *a: min(int(Func201(*a) * 28000 + Func202(*a) * 5600 - 28000), int(84000 + Func544(*a, **{
'sAttr': 'ShieldMax' }) * 7))),
                        'MoveSpeed': 0 } } } } }
    m_ModeMonsterAttrAdjust = {
        1: { },
        2: { },
        3: {
            MODE_SNOWMOUNTAINS: {
                'HPMax': 4000,
                'ArmorMax': 4000,
                'ShieldMax': 4000 } } }
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
                501: 4500 } } }
    m_ExtRule = {
        (3, 9): {
            ROUND_EXTRULE_REPLACECONFIG_CHALLENGE: {
                2: {
                    1116: 1 },
                3: {
                    1117: 1 },
                4: {
                    1118: 1 } },
            ROUND_EXTRULE_APPEARCHALLENGE: {
                'Default': {
                    2: 1113,
                    3: 1114,
                    4: 1115 } },
            ROUND_EXTRULE_REPLACEMONSTER: {
                20041: 30041,
                20042: 30041,
                20031: 30041 } } }
    m_Config = {
        'BendShopNpc': 1054,
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
                (3, 9): {
                    6114: WARRIOR_ELITE },
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
            LEVEL_TYPE_FIGHT: {
                (3, 7): {
                    6114: WARRIOR_ELITE },
                (3, 6): {
                    6114: WARRIOR_ELITE },
                (3, 5): {
                    6114: WARRIOR_ELITE },
                (3, 4): {
                    6114: WARRIOR_ELITE },
                (3, 3): {
                    6114: WARRIOR_ELITE },
                (3, 2): {
                    6114: WARRIOR_ELITE },
                (3, 1): {
                    6114: WARRIOR_ELITE },
                (3, 9): {
                    6114: WARRIOR_ELITE },
                (3, 8): {
                    6114: WARRIOR_ELITE } } } }


class CWatchElement(cl_warmgr.mobject.CElementData):
    pass


class CSaveElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'AutoSave': 1,
        'PreventSL': 1 }


class CBigDataAnalyseMgr(cl_warmgr.mobject.CElementData):
    pass


class CTeamSaveElement(cl_warmgr.mobject.CElementData):
    pass


class CSignalElement(cl_warmgr.mobject.CElementData):
    pass


class CRescueElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'm_HaltInfo': {
            103: 0,
            108: 0,
            321: 1,
            323: 1,
            322: 1,
            40108: 1,
            30108: 0,
            10108: 1,
            50108: 1,
            10149: 0,
            20149: 0,
            143: 0,
            198: 0,
            20108: 1 },
        'm_IgnoreHalt': [
            1323,
            12013] }


class CRecycleDropElement(cl_warmgr.mobject.CElementData):
    pass


class CHangUpKickElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'TOTALTIME': 120000,
        'CHECKTIME': 2000 }


class CReportSaveElement(cl_warmgr.mobject.CElementData):
    pass


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
                1088: 1 },
            2: {
                1089: 1 },
            3: {
                1090: 1 },
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
        'TotalOptionCnt': 12,
        'OptionCnt': 3,
        'SetRelicCnt': {
            3165: 5 },
        'RelicMG': 2420,
        'EndlessConfigLayer': 4,
        'EndlessStartLayer': 0,
        'EndlessGapLayer': 0 }


class CRollRelicElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'RelicDrop': 2401,
        'RelicPerform': {
            1: 2417,
            2: 2418,
            4: 2419 } }


class CWeaponstoreElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'ReplaceNpc': 1064,
        'LimitChallengeType': (12, 2, 17, 4),
        'RefreshNpcLayer': (3, 4),
        'LimitHideLevelType': (5, 6, 8),
        'MaxAnimaNum': 2,
        'AnimaCost': 150 }


class CTalentFusionElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'InitLayer': 1,
        'ChooseNum': (6, 2),
        'CommonTalentWeight': 50,
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
        'LimitMonsterResistance': 9500 }


class CRealEndlessElement(cl_warmgr.mobject.CElementData):
    m_LayerConfig = {
        1: {
            'LayerChoose': {
                3: {
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
        'LimitMonsterResistance': 9900 }


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
            20,
            5],
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
        'MinimumMagic': 2,
        'MagicRoomCLGCertain': {
            1088: {
                (1, 3): 20,
                (2, 3): 10 },
            1089: {
                (1, 3): 20,
                (2, 3): 10 },
            1090: {
                (1, 3): 20,
                (2, 3): 10 },
            1091: {
                (1, 3): 20,
                (2, 3): 10 },
            1116: {
                (1, 3): 20,
                (2, 3): 10 },
            1117: {
                (1, 3): 20,
                (2, 3): 10 },
            1118: {
                (1, 3): 20,
                (2, 3): 10 } } }


class CTeammateAIElement(cl_warmgr.mobject.CElementData):
    m_AIMemberChooseBene = { }
    m_Config = {
        'HeroBasicPassive': [
            6950,
            6951,
            6952,
            6963],
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
                6961] },
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
            1504: 1 },
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
                40056] } }


class CWarManager(CCustomWarMgr):
    m_SID = 3007
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
        'HangUpKickElement': (cl_warmgr.hangupkickelement.GetComponentClass, CHangUpKickElement),
        'ReportSaveElement': (cl_warmgr.reportsaveelement.GetComponentClass, CReportSaveElement),
        'SuitElement': (cl_warmgr.suitelement.GetComponentClass, CSuitElement),
        'SnowMountainElement': (cl_warmgr.snowmountainelement.GetComponentClass, CSnowMountainElement),
        'RidingAloneElement': (cl_warmgr.ridingaloneelement.GetComponentClass, CRidingAloneElement),
        'MonsterRelicElement': (cl_warmgr.monsterrelicelement.GetComponentClass, CMonsterRelicElement),
        'RollRelicElement': (cl_warmgr.rollrelicelement.GetComponentClass, CRollRelicElement),
        'WeaponStoreElement': (cl_warmgr.weaponstoreelement.GetComponentClass, CWeaponstoreElement),
        'TalentFusionElement': (cl_warmgr.talentfusionelement.GetComponentClass, CTalentFusionElement),
        'TaskElement': (cl_warmgr.taskelement.GetComponentClass, CTaskElement),
        'EndlessElement': (cl_warmgr.endlesselement.GetComponentClass, CEndlessElement),
        'RealEndlessElement': (cl_warmgr.realendlesselement.GetComponentClass, CRealEndlessElement),
        'RelicTalentElement': (cl_warmgr.relictalentelement.GetComponentClass, CRelicTalentElement),
        'TeammateAI': (cl_warmgr.teammateaielement.GetComponentClass, CTeammateAIElement) }
    m_SeasonFuncConfing = { }
    m_AllSeasonElement = {
        'RelicTalentElement': 1 }
    m_NewVerLayer = set()
    m_SeasonElement = {
        1: [
            'RelicTalentElement'] }

