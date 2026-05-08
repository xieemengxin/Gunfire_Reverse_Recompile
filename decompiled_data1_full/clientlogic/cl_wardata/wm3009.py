# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/wm3009.pyc
# RelativePath: clientlogic/cl_wardata/wm3009.pyc
# Source Generated with Decompyle++
# File: wm3009.pyc (Python 3.6)

from __future__ import absolute_import
from cl_warmgr.mobject import CWarManager as CCustomWarMgr
from cl_commondefines import GAMETYPE_DESTROY, HIDELV_TYPE_CASH, HIDELV_TYPE_ELITE, HIDELV_TYPE_NORMAL, HIDELV_TYPE_TRAP, LAYER_CHOOSE_CHALLENGE, LAYER_CHOOSE_CRAFTSMAN, LAYER_CHOOSE_EVENTNPC, LAYER_CHOOSE_HIDE, LAYER_CHOOSE_SHOP, LEVEL_TYPE_BOSS, LEVEL_TYPE_FIGHT, LEVEL_TYPE_HALL, LEVEL_TYPE_HIDE
from cl_newformula import Func204, Func231
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
import cl_warmgr.daytrialelement
import cl_warmgr.recycledropelement
import cl_warmgr.rollrelicelement

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


class CInitResourceElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'INITBULLET': ((4502, 225), (4503, 60), (4504, 15), (4508, 8)) }


class CLevelCtrlElement(cl_warmgr.mobject.CElementData):
    m_LevelCtrlConf = {
        1: {
            'CtrlSize': 4,
            'HallInfo': 1100011,
            'BossInfo': {
                'BossStore': {
                    1101009: 10,
                    1101006: 10,
                    1101007: 0 },
                'BossExtra': {
                    1101009: (ChooseAction11101009, ForceAction11101009),
                    1101006: (None, None),
                    1101007: (None, None) },
                'ChallengeStore': { },
                'SingleChallengeStore': { },
                'ExcludeChallengeArea': { },
                'UnSpawnRuleInfo': {
                    1101009: [],
                    1101006: [],
                    1101007: [] },
                'ChallengeModeLimit': { },
                'AIBosslevelEnhance': {
                    1101009: 0,
                    1101006: 0,
                    1101007: 0 } },
            'NpcInfo': {
                'shop': {
                    1005: 10 },
                'craftsman': {
                    1018: 10 } },
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
                        (3, 0): [
                            (1003, 1)],
                        (2, 0): [
                            (1003, 1)],
                        (1, 0): None },
                    'SingleChallengeStore': {
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelRoomChallenge': {
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelExcludeChallenge': {
                        1: {
                            1101201: [],
                            1101202: [],
                            1101203: [],
                            1101209: [],
                            1101210: [] },
                        2: {
                            1101201: [],
                            1101202: [],
                            1101203: [],
                            1101209: [],
                            1101210: [],
                            7101602: [] },
                        3: {
                            1101201: [],
                            1101202: [],
                            1101203: [],
                            1101209: [],
                            1101210: [] } },
                    'HideLevel': {
                        1: {
                            1101201: 1,
                            1101202: 1,
                            1101203: 1,
                            1101209: 1,
                            1101210: 1 },
                        2: {
                            1101201: 1,
                            1101202: 1,
                            1101203: 1,
                            1101209: 1,
                            1101210: 1,
                            7101602: 5 },
                        3: {
                            1101201: 1,
                            1101202: 1,
                            1101203: 1,
                            1101209: 1,
                            1101210: 1 } },
                    'HideLevelStore': {
                        1: {
                            (1101210, 1, 0, (0, 1000), -1): 10,
                            (1101209, 1, 0, (0, 1000), -1): 10,
                            (1101203, 1, 0, (0, 1000), -1): 10,
                            (1101202, 1, 0, (0, 1000), -1): 10,
                            (1101201, 1, 0, (0, 1000), -1): 10 },
                        2: {
                            (7101602, 5, 0, (0, 1000), -1): 8,
                            (1101210, 1, 0, (0, 1000), -1): 10,
                            (1101209, 1, 0, (0, 1000), -1): 10,
                            (1101203, 1, 0, (0, 1000), -1): 10,
                            (1101202, 1, 0, (0, 1000), -1): 10,
                            (1101201, 1, 0, (0, 1000), -1): 10 },
                        3: {
                            (1101210, 1, 0, (0, 1000), -1): 10,
                            (1101209, 1, 0, (0, 1000), -1): 10,
                            (1101203, 1, 0, (0, 1000), -1): 10,
                            (1101202, 1, 0, (0, 1000), -1): 10,
                            (1101201, 1, 0, (0, 1000), -1): 10 } },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': {
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
                        (3, 0): [
                            (1001, 1),
                            (1003, 1),
                            (1051, 1),
                            (1053, 1)],
                        (2, 0): [
                            (1001, 1),
                            (1003, 1),
                            (1053, 1),
                            (1008, 1)],
                        (1, 0): [
                            (1003, 1),
                            (1004, 1),
                            (1052, 1)] },
                    'SingleChallengeStore': {
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelRoomChallenge': {
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
                            7101112: [] },
                        2: {
                            1101201: [],
                            1101601: [],
                            7101602: [],
                            7101603: [],
                            7101604: [],
                            1101605: [],
                            7101112: [] },
                        3: {
                            1101201: [],
                            1101601: [],
                            7101602: [],
                            7101603: [],
                            7101604: [],
                            1101605: [],
                            7101112: [] } },
                    'HideLevel': {
                        1: {
                            1101201: 1,
                            1101601: 5,
                            7101602: 5,
                            7101603: 5,
                            7101604: 5,
                            1101605: 5,
                            7101112: 8 },
                        2: {
                            1101201: 1,
                            1101601: 5,
                            7101602: 5,
                            7101603: 5,
                            7101604: 5,
                            1101605: 5,
                            7101112: 8 },
                        3: {
                            1101201: 1,
                            1101601: 5,
                            7101602: 5,
                            7101603: 5,
                            7101604: 5,
                            1101605: 5,
                            7101112: 8 } },
                    'HideLevelStore': {
                        1: {
                            (7101112, 8, 0, (40, 1000), -1): 0,
                            (1101605, 5, 0, (40, 1000), -1): 10,
                            (7101604, 5, 1, (20, 1000), -1): 0,
                            (7101603, 5, 1, (0, 1000), -1): 0,
                            (7101602, 5, 1, (0, 1000), -1): 0,
                            (1101601, 5, 0, (0, 1000), -1): 10,
                            (1101201, 1, 0, (0, 1000), -1): 10 },
                        2: {
                            (7101112, 8, 0, (40, 1000), -1): 0,
                            (1101605, 5, 0, (40, 1000), -1): 10,
                            (7101604, 5, 1, (20, 1000), -1): 0,
                            (7101603, 5, 1, (0, 1000), -1): 2,
                            (7101602, 5, 1, (0, 1000), -1): 8,
                            (1101601, 5, 0, (0, 1000), -1): 10,
                            (1101201, 1, 0, (0, 1000), -1): 10 },
                        3: {
                            (7101112, 8, 0, (40, 1000), -1): 0,
                            (1101605, 5, 0, (40, 1000), -1): 10,
                            (7101604, 5, 1, (20, 1000), -1): 0,
                            (7101603, 5, 1, (0, 1000), -1): 0,
                            (7101602, 5, 1, (0, 1000), -1): 0,
                            (1101601, 5, 0, (0, 1000), -1): 10,
                            (1101201, 1, 0, (0, 1000), -1): 10 } },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': {
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
                        (3, 0): [
                            (1003, 1),
                            (1008, 1),
                            (1052, 1),
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
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelRoomChallenge': {
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
                            1101205: [],
                            1101206: [],
                            1101207: [],
                            1101208: [],
                            1101251: [],
                            1101252: [],
                            7101112: [] },
                        2: {
                            1101201: [],
                            1101601: [],
                            7101602: [],
                            7101603: [],
                            7101604: [],
                            1101605: [],
                            7101111: [],
                            1101204: [],
                            1101205: [],
                            1101206: [],
                            1101207: [],
                            1101208: [],
                            1101251: [],
                            1101252: [],
                            7101112: [] },
                        3: {
                            1101201: [],
                            1101601: [],
                            7101602: [],
                            7101603: [],
                            7101604: [],
                            1101605: [],
                            7101111: [],
                            1101204: [],
                            1101205: [],
                            1101206: [],
                            1101207: [],
                            1101208: [],
                            1101251: [],
                            1101252: [],
                            7101112: [] } },
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
                            1101205: 3,
                            1101206: 3,
                            1101207: 3,
                            1101208: 3,
                            1101251: 3,
                            1101252: 3,
                            7101112: 8 },
                        2: {
                            1101201: 1,
                            1101601: 5,
                            7101602: 5,
                            7101603: 5,
                            7101604: 5,
                            1101605: 5,
                            7101111: 3,
                            1101204: 3,
                            1101205: 3,
                            1101206: 3,
                            1101207: 3,
                            1101208: 3,
                            1101251: 3,
                            1101252: 3,
                            7101112: 8 },
                        3: {
                            1101201: 1,
                            1101601: 5,
                            7101602: 5,
                            7101603: 5,
                            7101604: 5,
                            1101605: 5,
                            7101111: 3,
                            1101204: 3,
                            1101205: 3,
                            1101206: 3,
                            1101207: 3,
                            1101208: 3,
                            1101251: 3,
                            1101252: 3,
                            7101112: 8 } },
                    'HideLevelStore': {
                        1: {
                            (7101112, 8, 0, (40, 1000), -1): 0,
                            (1101252, 3, 4, (10, 1000), -1): 10,
                            (1101251, 3, 4, (0, 1000), -1): 10,
                            (1101208, 3, 2, (30, 1000), -1): 10,
                            (1101207, 3, 3, (40, 1000), -1): 10,
                            (1101206, 3, 3, (10, 1000), -1): 10,
                            (1101205, 3, 2, (10, 1000), -1): 10,
                            (1101204, 3, 0, (30, 1000), -1): 10,
                            (7101111, 3, 0, (0, 1000), -1): 10,
                            (1101605, 5, 0, (40, 1000), -1): 10,
                            (7101604, 5, 1, (20, 1000), -1): 0,
                            (7101603, 5, 1, (0, 1000), -1): 0,
                            (7101602, 5, 1, (0, 1000), -1): 0,
                            (1101601, 5, 0, (0, 1000), -1): 10,
                            (1101201, 1, 0, (0, 1000), -1): 10 },
                        2: {
                            (7101112, 8, 0, (40, 1000), -1): 0,
                            (1101252, 3, 4, (10, 1000), -1): 10,
                            (1101251, 3, 4, (0, 1000), -1): 10,
                            (1101208, 3, 2, (30, 1000), -1): 10,
                            (1101207, 3, 3, (40, 1000), -1): 10,
                            (1101206, 3, 3, (10, 1000), -1): 10,
                            (1101205, 3, 2, (10, 1000), -1): 10,
                            (1101204, 3, 0, (30, 1000), -1): 10,
                            (7101111, 3, 0, (0, 1000), -1): 10,
                            (1101605, 5, 0, (40, 1000), -1): 10,
                            (7101604, 5, 1, (20, 1000), -1): 2,
                            (7101603, 5, 1, (0, 1000), -1): 4,
                            (7101602, 5, 1, (0, 1000), -1): 0,
                            (1101601, 5, 0, (0, 1000), -1): 10,
                            (1101201, 1, 0, (0, 1000), -1): 10 },
                        3: {
                            (7101112, 8, 0, (40, 1000), -1): 0,
                            (1101252, 3, 4, (10, 1000), -1): 10,
                            (1101251, 3, 4, (0, 1000), -1): 10,
                            (1101208, 3, 2, (30, 1000), -1): 10,
                            (1101207, 3, 3, (40, 1000), -1): 10,
                            (1101206, 3, 3, (10, 1000), -1): 10,
                            (1101205, 3, 2, (10, 1000), -1): 10,
                            (1101204, 3, 0, (30, 1000), -1): 10,
                            (7101111, 3, 0, (0, 1000), -1): 10,
                            (1101605, 5, 0, (40, 1000), -1): 10,
                            (7101604, 5, 1, (20, 1000), -1): 0,
                            (7101603, 5, 1, (0, 1000), -1): 0,
                            (7101602, 5, 1, (0, 1000), -1): 0,
                            (1101601, 5, 0, (0, 1000), -1): 10,
                            (1101201, 1, 0, (0, 1000), -1): 10 } },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': {
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
                        (3, 0): [
                            (1008, 1),
                            (1050, 1),
                            (1051, 1),
                            (1054, 1),
                            (1055, 1),
                            (1056, 1)],
                        (2, 0): [
                            (1015, 1),
                            (1051, 1),
                            (1056, 1)],
                        (1, 0): [
                            (1003, 1)] },
                    'SingleChallengeStore': {
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelRoomChallenge': {
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
                            1101205: [],
                            1101206: [],
                            1101207: [],
                            1101208: [],
                            1101251: [],
                            1101252: [],
                            7101112: [] },
                        2: {
                            1101201: [],
                            7101603: [],
                            7101604: [],
                            1101605: [],
                            7101111: [],
                            1101204: [],
                            1101205: [],
                            1101206: [],
                            1101207: [],
                            1101208: [],
                            1101251: [],
                            1101252: [],
                            7101112: [] },
                        3: {
                            7101603: [],
                            7101604: [],
                            1101605: [],
                            7101111: [],
                            1101204: [],
                            1101205: [],
                            1101206: [],
                            1101207: [],
                            1101208: [],
                            1101251: [],
                            1101252: [],
                            7101112: [] } },
                    'HideLevel': {
                        1: {
                            1101201: 1,
                            7101603: 5,
                            7101604: 5,
                            1101605: 5,
                            7101111: 3,
                            1101204: 3,
                            1101205: 3,
                            1101206: 3,
                            1101207: 3,
                            1101208: 3,
                            1101251: 3,
                            1101252: 3,
                            7101112: 8 },
                        2: {
                            1101201: 1,
                            7101603: 5,
                            7101604: 5,
                            1101605: 5,
                            7101111: 3,
                            1101204: 3,
                            1101205: 3,
                            1101206: 3,
                            1101207: 3,
                            1101208: 3,
                            1101251: 3,
                            1101252: 3,
                            7101112: 8 },
                        3: {
                            7101603: 5,
                            7101604: 5,
                            1101605: 5,
                            7101111: 3,
                            1101204: 3,
                            1101205: 3,
                            1101206: 3,
                            1101207: 3,
                            1101208: 3,
                            1101251: 3,
                            1101252: 3,
                            7101112: 8 } },
                    'HideLevelStore': {
                        1: {
                            (7101112, 8, 0, (40, 1000), -1): 0,
                            (1101252, 3, 4, (10, 1000), -1): 10,
                            (1101251, 3, 4, (0, 1000), -1): 10,
                            (1101208, 3, 2, (30, 1000), -1): 10,
                            (1101207, 3, 3, (40, 1000), -1): 10,
                            (1101206, 3, 3, (10, 1000), -1): 10,
                            (1101205, 3, 2, (10, 1000), -1): 10,
                            (1101204, 3, 0, (30, 1000), -1): 10,
                            (7101111, 3, 0, (0, 1000), -1): 10,
                            (1101605, 5, 0, (40, 1000), -1): 10,
                            (7101604, 5, 1, (20, 1000), -1): 0,
                            (7101603, 5, 1, (0, 1000), -1): 0,
                            (1101201, 1, 0, (0, 1000), -1): 10 },
                        2: {
                            (7101112, 8, 0, (40, 1000), -1): 0,
                            (1101252, 3, 4, (10, 1000), -1): 10,
                            (1101251, 3, 4, (0, 1000), -1): 10,
                            (1101208, 3, 2, (30, 1000), -1): 10,
                            (1101207, 3, 3, (40, 1000), -1): 10,
                            (1101206, 3, 3, (10, 1000), -1): 10,
                            (1101205, 3, 2, (10, 1000), -1): 10,
                            (1101204, 3, 0, (30, 1000), -1): 10,
                            (7101111, 3, 0, (0, 1000), -1): 10,
                            (1101605, 5, 0, (40, 1000), -1): 10,
                            (7101604, 5, 1, (20, 1000), -1): 6,
                            (7101603, 5, 1, (0, 1000), -1): 4,
                            (1101201, 1, 0, (0, 1000), -1): 10 },
                        3: {
                            (7101112, 8, 0, (40, 1000), -1): 0,
                            (1101252, 3, 4, (10, 1000), -1): 10,
                            (1101251, 3, 4, (0, 1000), -1): 10,
                            (1101208, 3, 2, (30, 1000), -1): 10,
                            (1101207, 3, 3, (40, 1000), -1): 10,
                            (1101206, 3, 3, (10, 1000), -1): 10,
                            (1101205, 3, 2, (10, 1000), -1): 10,
                            (1101204, 3, 0, (30, 1000), -1): 10,
                            (7101111, 3, 0, (0, 1000), -1): 10,
                            (1101605, 5, 0, (40, 1000), -1): 10,
                            (7101604, 5, 1, (20, 1000), -1): 6,
                            (7101603, 5, 1, (0, 1000), -1): 4 } },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': {
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'AIlevelEnhance': 0 } },
            'LayerChoose': {
                1: {
                    LAYER_CHOOSE_CRAFTSMAN: (2, 0, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10,
                        4: 10 }, {
                        1: 1,
                        2: 2,
                        3: 2,
                        4: 1 }),
                    LAYER_CHOOSE_SHOP: (2, 0, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10,
                        4: 10 }, {
                        1: 1,
                        2: 2,
                        3: 2,
                        4: 1 }),
                    LAYER_CHOOSE_EVENTNPC: (2, 0, 0, 99, {
                        1: 0,
                        2: 10,
                        3: 30,
                        4: 20 }, {
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_CHALLENGE: (3, 0, 0, 99, {
                        1: 15,
                        2: 30,
                        3: 30,
                        4: 40 }, {
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_HIDE: (3, 0, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 10,
                        4: 10 }, { }) },
                2: {
                    LAYER_CHOOSE_CRAFTSMAN: (2, 0, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10,
                        4: 10 }, {
                        1: 1,
                        2: 2,
                        3: 2,
                        4: 1 }),
                    LAYER_CHOOSE_SHOP: (2, 0, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10,
                        4: 10 }, {
                        1: 1,
                        2: 2,
                        3: 2,
                        4: 1 }),
                    LAYER_CHOOSE_EVENTNPC: (2, 0, 0, 99, {
                        1: 0,
                        2: 10,
                        3: 30,
                        4: 20 }, {
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_CHALLENGE: (3, 0, 0, 99, {
                        1: 15,
                        2: 30,
                        3: 30,
                        4: 40 }, {
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_HIDE: (3, 0, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 10,
                        4: 10 }, { }) },
                3: {
                    LAYER_CHOOSE_CRAFTSMAN: (2, 0, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10,
                        4: 10 }, {
                        1: 1,
                        2: 2,
                        3: 2,
                        4: 2 }),
                    LAYER_CHOOSE_SHOP: (2, 0, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10,
                        4: 10 }, {
                        1: 1,
                        2: 2,
                        3: 2,
                        4: 1 }),
                    LAYER_CHOOSE_EVENTNPC: (2, 0, 0, 99, {
                        1: 0,
                        2: 10,
                        3: 30,
                        4: 20 }, {
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_CHALLENGE: (3, 0, 0, 99, {
                        1: 15,
                        2: 30,
                        3: 30,
                        4: 40 }, {
                        1: 1,
                        2: 1,
                        3: 1,
                        4: 1 }),
                    LAYER_CHOOSE_HIDE: (3, 0, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 10,
                        4: 10 }, { }) } },
            'BaseGrade': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: (8, 0),
                        2: (11, 0),
                        3: (14, 0),
                        4: (18, 0) },
                    LEVEL_TYPE_FIGHT: {
                        1: (7, 0),
                        2: (10, 0),
                        3: (13, 0),
                        4: (17, 0) },
                    LEVEL_TYPE_BOSS: (20, 0),
                    LEVEL_TYPE_HALL: (0, 0) } },
            'MonsterAttAdjust': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        4: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        4: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * 20000 + 0), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 20000 + 0), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 20000 + 0), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                        ('MoveSpeed', (lambda *a: (Func204(*a) - 1) * 500 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] } },
            'EliteAttAdjust': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        4: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        4: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] } },
            'ItemChoose': 1001 },
        2: {
            'CtrlSize': 3,
            'HallInfo': 1100012,
            'BossInfo': {
                'BossStore': {
                    1202001: 10,
                    1202003: 10 },
                'BossExtra': {
                    1202001: (None, None),
                    1202003: (ChooseAction21202003, ForceAction21202003) },
                'ChallengeStore': { },
                'SingleChallengeStore': { },
                'ExcludeChallengeArea': { },
                'UnSpawnRuleInfo': {
                    1202001: [],
                    1202003: [] },
                'ChallengeModeLimit': { },
                'AIBosslevelEnhance': {
                    1202001: 0,
                    1202003: 0 } },
            'NpcInfo': {
                'shop': {
                    1005: 10 },
                'craftsman': {
                    1018: 10 } },
            'CtrlInfo': {
                1: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (7202111, 7202114, 7202115, 7202108, 7202109, 7202110, 7202116, 7202113),
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
                        7202110: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7202116: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7202113: {
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
                        (3, 0): [
                            (1030, 1),
                            (1050, 1),
                            (1053, 1),
                            (1054, 1),
                            (1056, 1)],
                        (2, 0): [
                            (1015, 1),
                            (1050, 1)],
                        (1, 0): [
                            (1009, 1),
                            (1054, 1)] },
                    'SingleChallengeStore': {
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelRoomChallenge': {
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
                            7201203: [] },
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
                            7201203: [] },
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
                            7201203: [] } },
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
                            7201203: 1 },
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
                            7201203: 1 },
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
                            7201203: 1 } },
                    'HideLevelStore': {
                        1: {
                            (7201203, 1, 0, (0, 1000), -1): 10,
                            (7201202, 1, 0, (0, 1000), -1): 10,
                            (1204103, 3, 0, (40, 1000), -1): 10,
                            (1201117, 3, 0, (20, 1000), -1): 10,
                            (1201116, 3, 1, (20, 1000), -1): 10,
                            (1201115, 3, 1, (0, 1000), -1): 10,
                            (7201604, 5, 0, (10, 1000), -1): 0,
                            (1201114, 3, 0, (0, 1000), -1): 10,
                            (1201112, 3, 0, (0, 1000), -1): 10 },
                        2: {
                            (7201203, 1, 0, (0, 1000), -1): 10,
                            (7201202, 1, 0, (0, 1000), -1): 10,
                            (1204103, 3, 0, (40, 1000), -1): 10,
                            (1201117, 3, 0, (20, 1000), -1): 10,
                            (1201116, 3, 1, (20, 1000), -1): 10,
                            (1201115, 3, 1, (0, 1000), -1): 10,
                            (7201604, 5, 2, (10, 1000), -1): 0,
                            (7201603, 5, 2, (20, 1000), -1): 0,
                            (1201114, 3, 0, (0, 1000), -1): 10,
                            (1201112, 3, 0, (0, 1000), -1): 10 },
                        3: {
                            (7201203, 1, 0, (0, 1000), -1): 10,
                            (7201202, 1, 0, (0, 1000), -1): 10,
                            (1204103, 3, 0, (40, 1000), -1): 10,
                            (1201117, 3, 0, (20, 1000), -1): 10,
                            (1201116, 3, 1, (20, 1000), -1): 10,
                            (1201115, 3, 1, (0, 1000), -1): 10,
                            (7201604, 5, 2, (10, 1000), -1): 0,
                            (7201603, 5, 2, (20, 1000), -1): 0,
                            (1201114, 3, 0, (0, 1000), -1): 10,
                            (1201112, 3, 0, (0, 1000), -1): 10 } },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': {
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
                        (3, 0): [
                            (1005, 1),
                            (1030, 1),
                            (1050, 1),
                            (1051, 1),
                            (1052, 1),
                            (1055, 1),
                            (1056, 1)],
                        (2, 0): [
                            (1005, 1),
                            (1050, 1),
                            (1052, 1),
                            (1057, 1)],
                        (1, 0): [
                            (1009, 1)] },
                    'SingleChallengeStore': {
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelRoomChallenge': {
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
                            1201119: [],
                            7201202: [] },
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
                            1201119: [] },
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
                            1201119: [] } },
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
                            1201119: 8,
                            7201202: 1 },
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
                            1201119: 8 },
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
                            1201119: 8 } },
                    'HideLevelStore': {
                        1: {
                            (7201202, 1, 0, (0, 1000), -1): 10,
                            (1201119, 8, 0, (40, 1000), -1): 0,
                            (7201203, 1, 0, (0, 1000), -1): 10,
                            (1204103, 3, 0, (40, 1000), -1): 10,
                            (1201117, 3, 0, (20, 1000), -1): 10,
                            (1201116, 3, 1, (20, 1000), -1): 10,
                            (1201115, 3, 1, (0, 1000), -1): 10,
                            (7201604, 5, 0, (10, 1000), -1): 0,
                            (1201114, 3, 0, (0, 1000), -1): 10,
                            (1201112, 3, 0, (0, 1000), -1): 10 },
                        2: {
                            (1201119, 8, 0, (40, 1000), -1): 0,
                            (7201203, 1, 0, (0, 1000), -1): 10,
                            (7201202, 1, 0, (0, 1000), -1): 10,
                            (1204103, 3, 0, (40, 1000), -1): 10,
                            (1201117, 3, 0, (20, 1000), -1): 10,
                            (1201116, 3, 1, (20, 1000), -1): 10,
                            (1201115, 3, 1, (0, 1000), -1): 10,
                            (7201604, 5, 2, (10, 1000), -1): 0,
                            (7201603, 5, 2, (20, 1000), -1): 0,
                            (1201114, 3, 0, (0, 1000), -1): 10,
                            (1201112, 3, 0, (0, 1000), -1): 10 },
                        3: {
                            (1201119, 8, 0, (40, 1000), -1): 0,
                            (7201203, 1, 0, (0, 1000), -1): 10,
                            (7201202, 1, 0, (0, 1000), -1): 10,
                            (1204103, 3, 0, (40, 1000), -1): 10,
                            (1201117, 3, 0, (20, 1000), -1): 10,
                            (1201116, 3, 1, (20, 1000), -1): 10,
                            (1201115, 3, 1, (0, 1000), -1): 10,
                            (7201604, 5, 2, (10, 1000), -1): 0,
                            (7201603, 5, 2, (20, 1000), -1): 0,
                            (1201114, 3, 0, (0, 1000), -1): 10,
                            (1201112, 3, 0, (0, 1000), -1): 10 } },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': {
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'AIlevelEnhance': 0 },
                3: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (7205101, 7205104, 7205103, 7205107, 7205102, 7205105, 7205108, 7205106),
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
                        7205105: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7205108: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7205106: {
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
                        (3, 0): [
                            (1026, 1),
                            (1027, 1),
                            (1050, 1),
                            (1054, 1),
                            (1055, 1)],
                        (2, 0): [
                            (1026, 1),
                            (1027, 1),
                            (1054, 1),
                            (1052, 1),
                            (1057, 1),
                            (1056, 1)],
                        (1, 0): [
                            (1030, 1)] },
                    'SingleChallengeStore': {
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelRoomChallenge': {
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
                            1201119: [] },
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
                            1201119: [] },
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
                            1201119: [] } },
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
                            1201119: 8 },
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
                            1201119: 8 },
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
                            1201119: 8 } },
                    'HideLevelStore': {
                        1: {
                            (1201119, 8, 0, (40, 1000), -1): 0,
                            (7201203, 1, 0, (0, 1000), -1): 10,
                            (7201202, 1, 0, (0, 1000), -1): 10,
                            (1204103, 3, 0, (40, 1000), -1): 10,
                            (1201117, 3, 0, (20, 1000), -1): 10,
                            (1201116, 3, 1, (20, 1000), -1): 10,
                            (1201115, 3, 1, (0, 1000), -1): 10,
                            (7201604, 5, 0, (10, 1000), -1): 0,
                            (1201114, 3, 0, (0, 1000), -1): 10,
                            (1201112, 3, 0, (0, 1000), -1): 10 },
                        2: {
                            (1201119, 8, 0, (40, 1000), -1): 0,
                            (7201203, 1, 0, (0, 1000), -1): 10,
                            (7201202, 1, 0, (0, 1000), -1): 10,
                            (1204103, 3, 0, (40, 1000), -1): 10,
                            (1201117, 3, 0, (20, 1000), -1): 10,
                            (1201116, 3, 1, (20, 1000), -1): 10,
                            (1201115, 3, 1, (0, 1000), -1): 10,
                            (7201604, 5, 2, (10, 1000), -1): 0,
                            (7201603, 5, 2, (20, 1000), -1): 0,
                            (1201114, 3, 0, (0, 1000), -1): 10,
                            (1201112, 3, 0, (0, 1000), -1): 10 },
                        3: {
                            (1201119, 8, 0, (40, 1000), -1): 0,
                            (7201203, 1, 0, (0, 1000), -1): 10,
                            (7201202, 1, 0, (0, 1000), -1): 10,
                            (1204103, 3, 0, (40, 1000), -1): 10,
                            (1201117, 3, 0, (20, 1000), -1): 10,
                            (1201116, 3, 1, (20, 1000), -1): 10,
                            (1201115, 3, 1, (0, 1000), -1): 10,
                            (7201604, 5, 2, (10, 1000), -1): 0,
                            (7201603, 5, 2, (20, 1000), -1): 0,
                            (1201114, 3, 0, (0, 1000), -1): 10,
                            (1201112, 3, 0, (0, 1000), -1): 10 } },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': {
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'AIlevelEnhance': 0 } },
            'LayerChoose': {
                1: {
                    LAYER_CHOOSE_CRAFTSMAN: (2, 0, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 2,
                        3: 1 }),
                    LAYER_CHOOSE_SHOP: (2, 0, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 2,
                        3: 2 }),
                    LAYER_CHOOSE_EVENTNPC: (2, 0, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 30 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_CHALLENGE: (3, 0, 0, 99, {
                        1: 30,
                        2: 30,
                        3: 40 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_HIDE: (3, 0, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, { }) },
                2: {
                    LAYER_CHOOSE_CRAFTSMAN: (2, 0, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 2,
                        3: 1 }),
                    LAYER_CHOOSE_SHOP: (2, 0, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 2,
                        3: 2 }),
                    LAYER_CHOOSE_EVENTNPC: (2, 0, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 30 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_CHALLENGE: (3, 0, 0, 99, {
                        1: 30,
                        2: 30,
                        3: 40 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_HIDE: (3, 0, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, { }) },
                3: {
                    LAYER_CHOOSE_CRAFTSMAN: (2, 0, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 2,
                        3: 1 }),
                    LAYER_CHOOSE_SHOP: (2, 0, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 2,
                        3: 2 }),
                    LAYER_CHOOSE_EVENTNPC: (2, 0, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 30 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_CHALLENGE: (3, 0, 0, 99, {
                        1: 30,
                        2: 30,
                        3: 40 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_HIDE: (3, 0, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, { }) } },
            'BaseGrade': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: (10, 0),
                        2: (14, 0),
                        3: (18, 0) },
                    LEVEL_TYPE_FIGHT: {
                        1: (9, 0),
                        2: (13, 0),
                        3: (17, 0) },
                    LEVEL_TYPE_BOSS: (20, 0),
                    LEVEL_TYPE_HALL: (0, 0) } },
            'MonsterAttAdjust': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * 20000 + 0), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 20000 + 0), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 20000 + 0), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                        ('MoveSpeed', (lambda *a: (Func204(*a) - 1) * 500 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] } },
            'EliteAttAdjust': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] } },
            'ItemChoose': 1002 },
        3: {
            'CtrlSize': 3,
            'HallInfo': 1100013,
            'BossInfo': {
                'BossStore': {
                    1301002: 10,
                    1301003: 10 },
                'BossExtra': {
                    1301002: (None, None),
                    1301003: (ChooseAction31301003, ForceAction31301003) },
                'ChallengeStore': { },
                'SingleChallengeStore': { },
                'ExcludeChallengeArea': { },
                'UnSpawnRuleInfo': {
                    1301002: [],
                    1301003: [] },
                'ChallengeModeLimit': { },
                'AIBosslevelEnhance': {
                    1301002: 0,
                    1301003: 0 } },
            'NpcInfo': {
                'shop': {
                    1005: 10 },
                'craftsman': {
                    1018: 10 } },
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
                        (3, 0): [
                            (1029, 1),
                            (1050, 1),
                            (1051, 1),
                            (1052, 1),
                            (1054, 1)],
                        (2, 0): [
                            (1029, 1),
                            (1028, 1)],
                        (1, 0): [
                            (1028, 1)] },
                    'SingleChallengeStore': {
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelRoomChallenge': {
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
                        (3, 0): [
                            (1024, 1),
                            (1055, 1),
                            (1056, 1)],
                        (2, 0): [
                            (1024, 1),
                            (1030, 1),
                            (1053, 1)],
                        (1, 0): [
                            (1024, 1)] },
                    'SingleChallengeStore': {
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelRoomChallenge': {
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
                        (3, 0): [
                            (1050, 1),
                            (1055, 1),
                            (1056, 1)],
                        (2, 0): [
                            (1029, 1),
                            (1030, 1),
                            (1056, 1)],
                        (1, 0): [
                            (1025, 1),
                            (1029, 1)] },
                    'SingleChallengeStore': {
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelRoomChallenge': {
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
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'AIlevelEnhance': 0 } },
            'LayerChoose': {
                1: {
                    LAYER_CHOOSE_CRAFTSMAN: (2, 0, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 2,
                        3: 1 }),
                    LAYER_CHOOSE_SHOP: (2, 0, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 2,
                        3: 2 }),
                    LAYER_CHOOSE_EVENTNPC: (2, 0, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 30 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_CHALLENGE: (3, 0, 0, 99, {
                        1: 30,
                        2: 30,
                        3: 40 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_HIDE: (3, 0, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, { }) },
                2: {
                    LAYER_CHOOSE_CRAFTSMAN: (2, 0, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 2,
                        3: 1 }),
                    LAYER_CHOOSE_SHOP: (2, 0, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 2,
                        3: 2 }),
                    LAYER_CHOOSE_EVENTNPC: (2, 0, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 30 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_CHALLENGE: (3, 0, 0, 99, {
                        1: 30,
                        2: 30,
                        3: 40 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_HIDE: (3, 0, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, { }) },
                3: {
                    LAYER_CHOOSE_CRAFTSMAN: (2, 0, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 2,
                        3: 1 }),
                    LAYER_CHOOSE_SHOP: (2, 0, 1, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, {
                        1: 1,
                        2: 2,
                        3: 2 }),
                    LAYER_CHOOSE_EVENTNPC: (2, 0, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 30 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_CHALLENGE: (3, 0, 0, 99, {
                        1: 30,
                        2: 30,
                        3: 40 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_HIDE: (3, 0, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 10 }, { }) } },
            'BaseGrade': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: (10, 0),
                        2: (14, 0),
                        3: (18, 0) },
                    LEVEL_TYPE_FIGHT: {
                        1: (9, 0),
                        2: (13, 0),
                        3: (17, 0) },
                    LEVEL_TYPE_BOSS: (20, 0),
                    LEVEL_TYPE_HALL: (0, 0) } },
            'MonsterAttAdjust': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', -1500, 0),
                            ('ShieldMax', -1500, 0),
                            ('ArmorMax', -1500, 0),
                            ('Att', -2000, 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', -1500, 0),
                            ('ShieldMax', -1500, 0),
                            ('ArmorMax', -1500, 0),
                            ('Att', -2000, 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', -1500, 0),
                            ('ShieldMax', -1500, 0),
                            ('ArmorMax', -1500, 0),
                            ('Att', -2000, 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', -1500, 0),
                            ('ShieldMax', -1500, 0),
                            ('ArmorMax', -1500, 0),
                            ('Att', -2000, 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', -1500, 0),
                            ('ShieldMax', -1500, 0),
                            ('ArmorMax', -1500, 0),
                            ('Att', -2000, 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', -1500, 0),
                            ('ShieldMax', -1500, 0),
                            ('ArmorMax', -1500, 0),
                            ('Att', -2000, 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * 20000 + 0), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 20000 + 0), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 20000 + 0), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                        ('MoveSpeed', (lambda *a: (Func204(*a) - 1) * 500 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] } },
            'EliteAttAdjust': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', -5000, 0),
                            ('ShieldMax', -5000, 0),
                            ('ArmorMax', -5000, 0),
                            ('Att', -2000, 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', -5000, 0),
                            ('ShieldMax', -5000, 0),
                            ('ArmorMax', -5000, 0),
                            ('Att', -2000, 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', -5000, 0),
                            ('ShieldMax', -5000, 0),
                            ('ArmorMax', -5000, 0),
                            ('Att', -2000, 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', -1500, 0),
                            ('ShieldMax', -1500, 0),
                            ('ArmorMax', -1500, 0),
                            ('Att', -2000, 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', -1500, 0),
                            ('ShieldMax', -1500, 0),
                            ('ArmorMax', -1500, 0),
                            ('Att', -2000, 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', -1500, 0),
                            ('ShieldMax', -1500, 0),
                            ('ArmorMax', -1500, 0),
                            ('Att', -2000, 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] } },
            'ItemChoose': 1003 },
        4: {
            'CtrlSize': 2,
            'HallInfo': 1400011,
            'BossInfo': {
                'BossStore': {
                    1403001: 10 },
                'BossExtra': {
                    1403001: (None, None) },
                'ChallengeStore': { },
                'SingleChallengeStore': { },
                'ExcludeChallengeArea': { },
                'UnSpawnRuleInfo': {
                    1403001: [] },
                'ChallengeModeLimit': { },
                'AIBosslevelEnhance': {
                    1403001: 0 } },
            'NpcInfo': {
                'shop': {
                    1005: 10 },
                'craftsman': {
                    1018: 10 } },
            'CtrlInfo': {
                1: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (7401101, 7401102, 7401103, 7401105, 7401104),
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
                        7401105: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7401104: {
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
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelRoomChallenge': {
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
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'AIlevelEnhance': 0 },
                2: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (7402103, 7402104, 7402102, 7402101, 7402105, 7402106),
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
                            'ChooseAction': None } },
                    'MediumStore': (),
                    'HardStore': (),
                    'NormalWeight': {
                        GAMETYPE_DESTROY: 100 },
                    'MediumWeight': { },
                    'HardWeight': { },
                    'ChallengeStore': {
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
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelRoomChallenge': {
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'HideLevelExcludeChallenge': {
                        1: {
                            7401202: [],
                            7401203: [] },
                        2: {
                            7401202: [],
                            7401203: [] },
                        3: {
                            7401202: [],
                            7401203: [] } },
                    'HideLevel': {
                        1: {
                            7401202: 3,
                            7401203: 1 },
                        2: {
                            7401202: 3,
                            7401203: 1 },
                        3: {
                            7401202: 3,
                            7401203: 1 } },
                    'HideLevelStore': {
                        1: {
                            (7401203, 1, 0, (0, 1000), -1): 10,
                            (7401202, 3, 0, (0, 1000), -1): 10 },
                        2: {
                            (7401203, 1, 0, (0, 1000), -1): 10,
                            (7401202, 3, 0, (0, 1000), -1): 10 },
                        3: {
                            (7401203, 1, 0, (0, 1000), -1): 10,
                            (7401202, 3, 0, (0, 1000), -1): 10 } },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': {
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'AIlevelEnhance': 0 } },
            'LayerChoose': {
                2: {
                    LAYER_CHOOSE_CRAFTSMAN: (2, 0, 1, 99, {
                        1: 10,
                        2: 10 }, {
                        1: 1,
                        2: 1 }),
                    LAYER_CHOOSE_SHOP: (2, 0, 1, 99, {
                        1: 10,
                        2: 10 }, {
                        1: 1,
                        2: 1 }),
                    LAYER_CHOOSE_EVENTNPC: (2, 0, 0, 99, {
                        1: 10,
                        2: 10 }, {
                        1: 1,
                        2: 1 }),
                    LAYER_CHOOSE_CHALLENGE: (3, 0, 0, 99, {
                        1: 30,
                        2: 30 }, { }),
                    LAYER_CHOOSE_HIDE: (3, 0, 0, 99, {
                        1: 10,
                        2: 10 }, { }) } },
            'BaseGrade': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: (8, 0),
                        2: (14, 0) },
                    LEVEL_TYPE_FIGHT: {
                        1: (9, 0),
                        2: (15, 0) },
                    LEVEL_TYPE_BOSS: (20, 0),
                    LEVEL_TYPE_HALL: (0, 0) } },
            'MonsterAttAdjust': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', -8500, 0),
                            ('ShieldMax', -8500, 0),
                            ('ArmorMax', -8500, 0),
                            ('Att', -4000, 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', -7500, 0),
                            ('ShieldMax', -7500, 0),
                            ('ArmorMax', -7500, 0),
                            ('Att', -3000, 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', -8500, 0),
                            ('ShieldMax', -8500, 0),
                            ('ArmorMax', -8500, 0),
                            ('Att', -4000, 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', -7500, 0),
                            ('ShieldMax', -7500, 0),
                            ('ArmorMax', -7500, 0),
                            ('Att', -3000, 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * 20000 + 0), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 20000 + 0), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 20000 + 0), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                        ('MoveSpeed', (lambda *a: (Func204(*a) - 1) * 500 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 7000 + 0), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] } },
            'EliteAttAdjust': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', -8500, 0),
                            ('ShieldMax', -8500, 0),
                            ('ArmorMax', -8500, 0),
                            ('Att', -3000, 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', -8500, 0),
                            ('ShieldMax', -8500, 0),
                            ('ArmorMax', -8500, 0),
                            ('Att', -3000, 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', -2500, 0),
                            ('ShieldMax', -2500, 0),
                            ('ArmorMax', -2500, 0),
                            ('Att', -3000, 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', -1500, 0),
                            ('ShieldMax', -1500, 0),
                            ('ArmorMax', -1500, 0),
                            ('Att', -3000, 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] } },
            'ItemChoose': 1004 } }
    m_LayerAndLevelMap = {
        (4, 3): (2, 4),
        (4, 2): (2, 3),
        (4, 1): (2, 1),
        (4, 0): (1, 0),
        (3, 4): (2, 4),
        (3, 3): (2, 3),
        (3, 2): (2, 1),
        (3, 1): (1, 4),
        (3, 0): (1, 0),
        (2, 4): (2, 4),
        (2, 3): (2, 3),
        (2, 2): (2, 1),
        (2, 1): (1, 4),
        (2, 0): (1, 0),
        (1, 5): (2, 4),
        (1, 4): (2, 3),
        (1, 3): (2, 1),
        (1, 2): (1, 4),
        (1, 1): (1, 3),
        (1, 0): (1, 0) }
    m_ChooseItem = {
        1001: {
            (1, 4): {
                'WeaponChoose': (2, 0, 1001),
                'GoldenCupChoose': (0, 0, 4101),
                'RelicChoose': (1, 0, 2401) },
            (1, 3): {
                'WeaponChoose': (2, 0, 1001),
                'GoldenCupChoose': (0, 0, 4101),
                'RelicChoose': (1, 0, 2401) },
            (1, 2): {
                'WeaponChoose': (1, 0, 1001),
                'GoldenCupChoose': (0, 0, 4101),
                'RelicChoose': (1, 0, 2401) },
            (1, 1): {
                'WeaponChoose': (1, 0, 1001),
                'GoldenCupChoose': (0, 0, 4101),
                'RelicChoose': (1, 0, 2401) } },
        1002: {
            (2, 3): {
                'WeaponChoose': (2, 0, 1001),
                'GoldenCupChoose': (0, 0, 4101),
                'RelicChoose': (2, 0, 2401) },
            (2, 2): {
                'WeaponChoose': (2, 0, 1001),
                'GoldenCupChoose': (0, 0, 4101),
                'RelicChoose': (1, 0, 2401) },
            (2, 1): {
                'WeaponChoose': (2, 0, 1001),
                'GoldenCupChoose': (0, 0, 4101),
                'RelicChoose': (1, 0, 2401) } },
        1003: {
            (3, 3): {
                'WeaponChoose': (2, 0, 1001),
                'GoldenCupChoose': (0, 0, 4101),
                'RelicChoose': (2, 0, 2401) },
            (3, 2): {
                'WeaponChoose': (2, 0, 1001),
                'GoldenCupChoose': (0, 0, 4101),
                'RelicChoose': (1, 0, 2401) },
            (3, 1): {
                'WeaponChoose': (2, 0, 1001),
                'GoldenCupChoose': (0, 0, 4101),
                'RelicChoose': (1, 0, 2401) } },
        1004: {
            (4, 2): {
                'WeaponChoose': (3, 0, 1001),
                'GoldenCupChoose': (0, 0, 4101),
                'RelicChoose': (2, 0, 2401) },
            (4, 1): {
                'WeaponChoose': (3, 0, 1001),
                'GoldenCupChoose': (0, 0, 4101),
                'RelicChoose': (2, 0, 2401) } },
        1005: {
            (1, 4): {
                'WeaponChoose': (2, 0, 1001),
                'GoldenCupChoose': (2, 0, 4101),
                'RelicChoose': (6, 0, 2401) },
            (1, 3): {
                'WeaponChoose': (2, 0, 1001),
                'GoldenCupChoose': (2, 0, 4101),
                'RelicChoose': (5, 0, 2401) },
            (1, 2): {
                'WeaponChoose': (1, 0, 1001),
                'GoldenCupChoose': (1, 0, 4101),
                'RelicChoose': (3, 0, 2401) },
            (1, 1): {
                'WeaponChoose': (1, 0, 1001),
                'GoldenCupChoose': (1, 0, 4101),
                'RelicChoose': (2, 0, 2401) } },
        1006: {
            (2, 3): {
                'WeaponChoose': (2, 0, 1001),
                'GoldenCupChoose': (2, 0, 4101),
                'RelicChoose': (6, 0, 2401) },
            (2, 2): {
                'WeaponChoose': (2, 0, 1001),
                'GoldenCupChoose': (2, 0, 4101),
                'RelicChoose': (5, 0, 2401) },
            (2, 1): {
                'WeaponChoose': (2, 0, 1001),
                'GoldenCupChoose': (2, 0, 4101),
                'RelicChoose': (5, 0, 2401) } },
        1007: {
            (3, 3): {
                'WeaponChoose': (2, 0, 1001),
                'GoldenCupChoose': (2, 0, 4101),
                'RelicChoose': (6, 0, 2401) },
            (3, 2): {
                'WeaponChoose': (2, 0, 1001),
                'GoldenCupChoose': (2, 0, 4101),
                'RelicChoose': (5, 0, 2401) },
            (3, 1): {
                'WeaponChoose': (2, 0, 1001),
                'GoldenCupChoose': (2, 0, 4101),
                'RelicChoose': (5, 0, 2401) } },
        1008: {
            (4, 2): {
                'WeaponChoose': (3, 0, 1001),
                'GoldenCupChoose': (3, 0, 4101),
                'RelicChoose': (8, 0, 2401) },
            (4, 1): {
                'WeaponChoose': (3, 0, 1001),
                'GoldenCupChoose': (3, 0, 4101),
                'RelicChoose': (8, 0, 2401) } } }
    m_SightLevelConf = { }


class CWarreport(cl_warmgr.mobject.CElementData):
    pass


class CPVEDieElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'RelifeData': 1002,
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
        1: {
            'MoveSpeed': 1500 },
        2: {
            'MoveSpeed': 1500 },
        3: {
            'MoveSpeed': 2500 } }
    m_CycleMonsterAttrAdjust = {
        1: { },
        2: { },
        3: { } }
    m_ModeMonsterAttrAdjust = {
        1: { },
        2: { },
        3: { } }
    m_CycleMonsterRewardAdjust = { }
    m_ExtRule = { }


class CMonsterSuperElement(cl_warmgr.mobject.CElementData):
    m_SuperConfig = {
        'Default': {
            LEVEL_TYPE_FIGHT: {
                1: {
                    'ChooseRatio': (lambda *a: 10 + min(int(Func231(*a) // 3), 50)),
                    'LevelConfig': {
                        1: {
                            'LevelLimit': (lambda *a: 4 + min(int(Func231(*a) // 35), 4)),
                            'LevelLive': 1,
                            'RoomLimit': (lambda *a: 1 + min(int(Func231(*a) // 70), 2)),
                            'RoomLive': 1 },
                        2: {
                            'LevelLimit': (lambda *a: 6 + min(int(Func231(*a) // 35), 4)),
                            'LevelLive': 1,
                            'RoomLimit': (lambda *a: 2 + min(int(Func231(*a) // 70), 2)),
                            'RoomLive': 1 },
                        3: {
                            'LevelLimit': (lambda *a: 9 + min(int(Func231(*a) // 35), 4)),
                            'LevelLive': 1,
                            'RoomLimit': (lambda *a: 2 + min(int(Func231(*a) // 70), 2)),
                            'RoomLive': 1 },
                        4: {
                            'LevelLimit': (lambda *a: 11 + min(int(Func231(*a) // 35), 4)),
                            'LevelLive': (lambda *a: 1 + min(int(Func231(*a) // 100), 1)),
                            'RoomLimit': (lambda *a: 3 + min(int(Func231(*a) // 70), 2)),
                            'RoomLive': (lambda *a: 1 + min(int(Func231(*a) // 100), 1)) } },
                    'SuperLevel': 2 },
                2: {
                    'ChooseRatio': (lambda *a: 10 + min(int(Func231(*a) // 3), 50)),
                    'LevelConfig': {
                        1: {
                            'LevelLimit': (lambda *a: 6 + min(int(Func231(*a) // 35), 4)),
                            'LevelLive': 1,
                            'RoomLimit': (lambda *a: 2 + min(int(Func231(*a) // 70), 2)),
                            'RoomLive': 1 },
                        2: {
                            'LevelLimit': (lambda *a: 9 + min(int(Func231(*a) // 35), 4)),
                            'LevelLive': 1,
                            'RoomLimit': (lambda *a: 2 + min(int(Func231(*a) // 70), 2)),
                            'RoomLive': 1 },
                        3: {
                            'LevelLimit': (lambda *a: 11 + min(int(Func231(*a) // 35), 4)),
                            'LevelLive': (lambda *a: 1 + min(int(Func231(*a) // 100), 1)),
                            'RoomLimit': (lambda *a: 3 + min(int(Func231(*a) // 70), 2)),
                            'RoomLive': (lambda *a: 1 + min(int(Func231(*a) // 100), 1)) } },
                    'SuperLevel': 2 },
                3: {
                    'ChooseRatio': (lambda *a: 10 + min(int(Func231(*a) // 3), 50)),
                    'LevelConfig': {
                        1: {
                            'LevelLimit': (lambda *a: 6 + min(int(Func231(*a) // 35), 4)),
                            'LevelLive': 1,
                            'RoomLimit': (lambda *a: 2 + min(int(Func231(*a) // 70), 2)),
                            'RoomLive': 1 },
                        2: {
                            'LevelLimit': (lambda *a: 9 + min(int(Func231(*a) // 35), 4)),
                            'LevelLive': 1,
                            'RoomLimit': (lambda *a: 2 + min(int(Func231(*a) // 70), 2)),
                            'RoomLive': 1 },
                        3: {
                            'LevelLimit': (lambda *a: 11 + min(int(Func231(*a) // 35), 4)),
                            'LevelLive': (lambda *a: 1 + min(int(Func231(*a) // 100), 1)),
                            'RoomLimit': (lambda *a: 3 + min(int(Func231(*a) // 70), 2)),
                            'RoomLive': (lambda *a: 1 + min(int(Func231(*a) // 100), 1)) } },
                    'SuperLevel': 2 },
                4: {
                    'ChooseRatio': (lambda *a: 10 + min(int(Func231(*a) // 3), 50)),
                    'LevelConfig': {
                        1: {
                            'LevelLimit': (lambda *a: 6 + min(int(Func231(*a) // 35), 4)),
                            'LevelLive': 1,
                            'RoomLimit': (lambda *a: 2 + min(int(Func231(*a) // 70), 2)),
                            'RoomLive': 1 },
                        2: {
                            'LevelLimit': (lambda *a: 9 + min(int(Func231(*a) // 35), 4)),
                            'LevelLive': 1,
                            'RoomLimit': (lambda *a: 2 + min(int(Func231(*a) // 70), 2)),
                            'RoomLive': 1 } },
                    'SuperLevel': 2 } } } }
    m_AffixConfig = {
        'Default': {
            LEVEL_TYPE_FIGHT: { } } }


class CWatchElement(cl_warmgr.mobject.CElementData):
    pass


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
            321: 1,
            323: 1,
            322: 1,
            40108: 1,
            30108: 1,
            10108: 1,
            50108: 1,
            10149: 0,
            20149: 0,
            143: 1,
            198: 0 },
        'm_IgnoreHalt': [
            12013] }


class CDayTrialElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'm_GlobalItem': (1002, 1001),
        'm_DayReward': (100, 30, 5) }


class CRecycleDropElement(cl_warmgr.mobject.CElementData):
    pass


class CRollRelicElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'RelicDrop': {
            1: 2415,
            2: 2416,
            4: 2417 },
        'RelicPerform': {
            1: 2418,
            2: 2419,
            4: 2420 } }


class CWarManager(CCustomWarMgr):
    m_SID = 3009
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
        'DayTrialElement': (cl_warmgr.daytrialelement.GetComponentClass, CDayTrialElement),
        'RecycleDropElement': (cl_warmgr.recycledropelement.GetComponentClass, CRecycleDropElement),
        'RollRelicElement': (cl_warmgr.rollrelicelement.GetComponentClass, CRollRelicElement) }
    m_SeasonFuncConfing = { }
    m_AllSeasonElement = { }
    m_NewVerLayer = set()
    m_SeasonElement = { }

