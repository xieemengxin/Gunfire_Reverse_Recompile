# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/wm3008.pyc
# RelativePath: clientlogic/cl_wardata/wm3008.pyc
# Source Generated with Decompyle++
# File: wm3008.pyc (Python 3.6)

from __future__ import absolute_import
from cl_warmgr.mobject import CWarManager as CCustomWarMgr
from cl_commondefines import GAMETYPE_DESTROY, HIDELV_TYPE_CASH, HIDELV_TYPE_ELITE, HIDELV_TYPE_JUMP, HIDELV_TYPE_NORMAL, HIDELV_TYPE_PETROCHEMICAL, HIDELV_TYPE_TRAP, LAYER_CHOOSE_CHALLENGE, LAYER_CHOOSE_CRAFTSMAN, LAYER_CHOOSE_EVENTNPC, LAYER_CHOOSE_HIDE, LAYER_CHOOSE_SHOP, LEVEL_TYPE_BOSS, LEVEL_TYPE_FIGHT, LEVEL_TYPE_HALL, LEVEL_TYPE_HIDE
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
                            1101202: [],
                            1101203: [] },
                        2: {
                            1101201: [],
                            1101202: [],
                            1101203: [],
                            1101601: [],
                            1101602: [],
                            1101111: [],
                            1101204: [],
                            1101205: [],
                            1101206: [],
                            1101207: [],
                            1101208: [],
                            1101233: [],
                            1101234: [],
                            1101605: [],
                            1101251: [],
                            1101252: [],
                            1101209: [],
                            1101210: [] },
                        3: {
                            1101201: [],
                            1101202: [],
                            1101203: [] } },
                    'HideLevel': {
                        1: {
                            1101201: 1,
                            1101202: 1,
                            1101203: 1 },
                        2: {
                            1101201: 1,
                            1101202: 1,
                            1101203: 1,
                            1101601: 5,
                            1101602: 5,
                            1101111: 3,
                            1101204: 3,
                            1101205: 3,
                            1101206: 3,
                            1101207: 3,
                            1101208: 3,
                            1101233: 7,
                            1101234: 7,
                            1101605: 5,
                            1101251: 3,
                            1101252: 3,
                            1101209: 1,
                            1101210: 1 },
                        3: {
                            1101201: 1,
                            1101202: 1,
                            1101203: 1 } },
                    'HideLevelStore': {
                        1: {
                            (1101203, 1, 0, (0, 1000), -1): 10,
                            (1101202, 1, 0, (0, 1000), -1): 10,
                            (1101201, 1, 0, (0, 1000), -1): 10 },
                        2: {
                            (1101210, 1, 0, (0, 1000), -1): 10,
                            (1101209, 1, 0, (0, 1000), -1): 10,
                            (1101252, 3, 4, (0, 1000), -1): 1,
                            (1101251, 3, 4, (0, 1000), -1): 1,
                            (1101605, 5, 0, (0, 1000), -1): 10,
                            (1101234, 7, 0, (0, 1000), -1): 10,
                            (1101233, 7, 0, (0, 1000), -1): 10,
                            (1101208, 3, 2, (0, 1000), -1): 1,
                            (1101207, 3, 3, (0, 1000), -1): 1,
                            (1101206, 3, 3, (0, 1000), -1): 1,
                            (1101205, 3, 2, (0, 1000), -1): 1,
                            (1101204, 3, 0, (0, 1000), -1): 1,
                            (1101111, 3, 0, (0, 1000), -1): 1,
                            (1101602, 5, 0, (0, 1000), -1): 8,
                            (1101601, 5, 0, (0, 1000), -1): 10,
                            (1101203, 1, 0, (0, 1000), -1): 10,
                            (1101202, 1, 0, (0, 1000), -1): 10,
                            (1101201, 1, 0, (0, 1000), -1): 10 },
                        3: {
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
                            (1053, 1)],
                        (1, 0): [
                            (1001, 1),
                            (1003, 1),
                            (1051, 1),
                            (1053, 1)] },
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
                            1101601: [],
                            1101602: [],
                            1101604: [],
                            1101605: [],
                            1101112: [] },
                        2: {
                            1101201: [],
                            1101202: [],
                            1101203: [],
                            1101601: [],
                            1101602: [],
                            1101603: [],
                            1101111: [],
                            1101204: [],
                            1101205: [],
                            1101206: [],
                            1101207: [],
                            1101208: [],
                            1101233: [],
                            1101234: [],
                            1101605: [],
                            1101251: [],
                            1101252: [],
                            1101112: [] },
                        3: {
                            1101201: [],
                            1101202: [],
                            1101203: [],
                            1101601: [],
                            1101602: [],
                            1101603: [],
                            1101605: [],
                            1101112: [] } },
                    'HideLevel': {
                        1: {
                            1101201: 1,
                            1101202: 1,
                            1101203: 1,
                            1101601: 1,
                            1101602: 1,
                            1101604: 1,
                            1101605: 1,
                            1101112: 8 },
                        2: {
                            1101201: 1,
                            1101202: 1,
                            1101203: 1,
                            1101601: 5,
                            1101602: 5,
                            1101603: 5,
                            1101111: 3,
                            1101204: 3,
                            1101205: 3,
                            1101206: 3,
                            1101207: 3,
                            1101208: 3,
                            1101233: 7,
                            1101234: 7,
                            1101605: 5,
                            1101251: 3,
                            1101252: 3,
                            1101112: 8 },
                        3: {
                            1101201: 1,
                            1101202: 1,
                            1101203: 1,
                            1101601: 1,
                            1101602: 1,
                            1101603: 1,
                            1101605: 1,
                            1101112: 8 } },
                    'HideLevelStore': {
                        1: {
                            (1101112, 8, 0, (0, 1000), -1): 10,
                            (1101605, 1, 0, (0, 1000), -1): 10,
                            (1101604, 1, 0, (0, 1000), -1): 2,
                            (1101602, 1, 0, (0, 1000), -1): 8,
                            (1101601, 1, 0, (0, 1000), -1): 10,
                            (1101203, 1, 0, (0, 1000), -1): 10,
                            (1101202, 1, 0, (0, 1000), -1): 10,
                            (1101201, 1, 0, (0, 1000), -1): 10 },
                        2: {
                            (1101112, 8, 0, (0, 1000), -1): 10,
                            (1101252, 3, 4, (0, 1000), -1): 7,
                            (1101251, 3, 4, (0, 1000), -1): 7,
                            (1101605, 5, 0, (0, 1000), -1): 10,
                            (1101234, 7, 0, (0, 1000), -1): 10,
                            (1101233, 7, 0, (0, 1000), -1): 10,
                            (1101208, 3, 2, (0, 1000), -1): 7,
                            (1101207, 3, 3, (0, 1000), -1): 7,
                            (1101206, 3, 3, (0, 1000), -1): 7,
                            (1101205, 3, 2, (0, 1000), -1): 7,
                            (1101204, 3, 0, (0, 1000), -1): 7,
                            (1101111, 3, 0, (0, 1000), -1): 7,
                            (1101603, 5, 1, (0, 1000), -1): 2,
                            (1101602, 5, 1, (0, 1000), -1): 8,
                            (1101601, 5, 0, (0, 1000), -1): 10,
                            (1101203, 1, 0, (0, 1000), -1): 10,
                            (1101202, 1, 0, (0, 1000), -1): 10,
                            (1101201, 1, 0, (0, 1000), -1): 10 },
                        3: {
                            (1101112, 8, 0, (0, 1000), -1): 10,
                            (1101605, 1, 0, (0, 1000), -1): 10,
                            (1101603, 1, 0, (0, 1000), -1): 2,
                            (1101602, 1, 0, (0, 1000), -1): 8,
                            (1101601, 1, 0, (0, 1000), -1): 10,
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
                3: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (1103154, 1103155, 1103157, 1103161, 1103158, 1103159, 1103160, 1103162, 1103165),
                    'NormalFilter': {
                        1103154: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1103155: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1103157: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1103161: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1103158: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1103159: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1103160: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1103162: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1103165: {
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
                            (1053, 1),
                            (1055, 1)],
                        (1, 0): [
                            (1003, 1),
                            (1008, 1),
                            (1052, 1),
                            (1053, 1)] },
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
                            1101601: [],
                            1101602: [],
                            1101603: [],
                            1101604: [],
                            1101605: [],
                            1101111: [],
                            1101204: [],
                            1101205: [],
                            1101206: [],
                            1101251: [],
                            1101112: [] },
                        2: {
                            1101201: [],
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
                            1101605: [],
                            1101251: [],
                            1101252: [],
                            1101112: [] },
                        3: {
                            1101201: [],
                            1101202: [],
                            1101203: [],
                            1101601: [],
                            1101602: [],
                            1101603: [],
                            1101604: [],
                            1101605: [],
                            1101111: [],
                            1101204: [],
                            1101205: [],
                            1101206: [],
                            1101251: [],
                            1101112: [] } },
                    'HideLevel': {
                        1: {
                            1101201: 1,
                            1101202: 1,
                            1101203: 1,
                            1101601: 1,
                            1101602: 1,
                            1101603: 1,
                            1101604: 1,
                            1101605: 1,
                            1101111: 3,
                            1101204: 3,
                            1101205: 3,
                            1101206: 3,
                            1101251: 3,
                            1101112: 8 },
                        2: {
                            1101201: 1,
                            1101603: 5,
                            1101604: 5,
                            1101111: 3,
                            1101204: 3,
                            1101205: 3,
                            1101206: 3,
                            1101207: 3,
                            1101208: 3,
                            1101233: 7,
                            1101234: 7,
                            1101605: 5,
                            1101251: 3,
                            1101252: 3,
                            1101112: 8 },
                        3: {
                            1101201: 1,
                            1101202: 1,
                            1101203: 1,
                            1101601: 1,
                            1101602: 1,
                            1101603: 1,
                            1101604: 1,
                            1101605: 1,
                            1101111: 3,
                            1101204: 3,
                            1101205: 3,
                            1101206: 3,
                            1101251: 3,
                            1101112: 8 } },
                    'HideLevelStore': {
                        1: {
                            (1101112, 8, 0, (0, 1000), -1): 10,
                            (1101251, 3, 0, (0, 1000), -1): 10,
                            (1101206, 3, 0, (0, 1000), -1): 10,
                            (1101205, 3, 0, (0, 1000), -1): 10,
                            (1101204, 3, 0, (0, 1000), -1): 10,
                            (1101111, 3, 0, (0, 1000), -1): 10,
                            (1101605, 1, 0, (0, 1000), -1): 10,
                            (1101604, 1, 0, (0, 1000), -1): 2,
                            (1101603, 1, 0, (0, 1000), -1): 4,
                            (1101602, 1, 0, (0, 1000), -1): 4,
                            (1101601, 1, 0, (0, 1000), -1): 10,
                            (1101203, 1, 0, (0, 1000), -1): 10,
                            (1101202, 1, 0, (0, 1000), -1): 10,
                            (1101201, 1, 0, (0, 1000), -1): 10 },
                        2: {
                            (1101112, 8, 0, (0, 1000), -1): 10,
                            (1101252, 3, 4, (0, 1000), -1): 10,
                            (1101251, 3, 4, (0, 1000), -1): 10,
                            (1101605, 5, 0, (0, 1000), -1): 10,
                            (1101234, 7, 0, (0, 1000), -1): 10,
                            (1101233, 7, 0, (0, 1000), -1): 10,
                            (1101208, 3, 2, (0, 1000), -1): 10,
                            (1101207, 3, 3, (0, 1000), -1): 10,
                            (1101206, 3, 3, (0, 1000), -1): 10,
                            (1101205, 3, 2, (0, 1000), -1): 10,
                            (1101204, 3, 0, (0, 1000), -1): 10,
                            (1101111, 3, 0, (0, 1000), -1): 10,
                            (1101604, 5, 1, (0, 1000), -1): 2,
                            (1101603, 5, 1, (0, 1000), -1): 4,
                            (1101201, 1, 0, (0, 1000), -1): 10 },
                        3: {
                            (1101112, 8, 0, (0, 1000), -1): 10,
                            (1101251, 3, 0, (0, 1000), -1): 10,
                            (1101206, 3, 0, (0, 1000), -1): 10,
                            (1101205, 3, 0, (0, 1000), -1): 10,
                            (1101204, 3, 0, (0, 1000), -1): 10,
                            (1101111, 3, 0, (0, 1000), -1): 10,
                            (1101605, 1, 0, (0, 1000), -1): 10,
                            (1101604, 1, 0, (0, 1000), -1): 2,
                            (1101603, 1, 0, (0, 1000), -1): 4,
                            (1101602, 1, 0, (0, 1000), -1): 4,
                            (1101601, 1, 0, (0, 1000), -1): 10,
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
                4: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (1105101, 1105102, 1105103, 1105104, 1105105, 1105106, 1105107),
                    'NormalFilter': {
                        1105101: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1105102: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1105103: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1105104: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1105105: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1105106: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1105107: {
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
                            (1051, 1),
                            (1056, 1)],
                        (1, 0): [
                            (1050, 1),
                            (1052, 1),
                            (1057, 1)] },
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
                            1101601: [],
                            1101603: [],
                            1101604: [],
                            1101605: [],
                            1101111: [],
                            1101204: [],
                            1101205: [],
                            1101206: [],
                            1101251: [],
                            1101112: [] },
                        2: {
                            1101201: [],
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
                            1101605: [],
                            1101251: [],
                            1101252: [],
                            1101112: [] },
                        3: {
                            1101201: [],
                            1101202: [],
                            1101203: [],
                            1101601: [],
                            1101603: [],
                            1101604: [],
                            1101605: [],
                            1101111: [],
                            1101204: [],
                            1101205: [],
                            1101206: [],
                            1101251: [],
                            1101112: [] } },
                    'HideLevel': {
                        1: {
                            1101201: 1,
                            1101202: 1,
                            1101203: 1,
                            1101601: 1,
                            1101603: 1,
                            1101604: 1,
                            1101605: 1,
                            1101111: 3,
                            1101204: 3,
                            1101205: 3,
                            1101206: 3,
                            1101251: 3,
                            1101112: 8 },
                        2: {
                            1101201: 1,
                            1101603: 5,
                            1101604: 5,
                            1101111: 3,
                            1101204: 3,
                            1101205: 3,
                            1101206: 3,
                            1101207: 3,
                            1101208: 3,
                            1101233: 7,
                            1101234: 7,
                            1101605: 5,
                            1101251: 3,
                            1101252: 3,
                            1101112: 8 },
                        3: {
                            1101201: 1,
                            1101202: 1,
                            1101203: 1,
                            1101601: 1,
                            1101603: 1,
                            1101604: 1,
                            1101605: 1,
                            1101111: 3,
                            1101204: 3,
                            1101205: 3,
                            1101206: 3,
                            1101251: 3,
                            1101112: 8 } },
                    'HideLevelStore': {
                        1: {
                            (1101112, 8, 0, (0, 1000), -1): 10,
                            (1101251, 3, 0, (0, 1000), -1): 10,
                            (1101206, 3, 0, (0, 1000), -1): 10,
                            (1101205, 3, 0, (0, 1000), -1): 10,
                            (1101204, 3, 0, (0, 1000), -1): 10,
                            (1101111, 3, 0, (0, 1000), -1): 10,
                            (1101605, 1, 0, (0, 1000), -1): 10,
                            (1101604, 1, 0, (0, 1000), -1): 6,
                            (1101603, 1, 0, (0, 1000), -1): 4,
                            (1101601, 1, 0, (0, 1000), -1): 10,
                            (1101203, 1, 0, (0, 1000), -1): 10,
                            (1101202, 1, 0, (0, 1000), -1): 10,
                            (1101201, 1, 0, (0, 1000), -1): 10 },
                        2: {
                            (1101112, 8, 0, (0, 1000), -1): 10,
                            (1101252, 3, 4, (0, 1000), -1): 10,
                            (1101251, 3, 4, (0, 1000), -1): 10,
                            (1101605, 5, 0, (0, 1000), -1): 10,
                            (1101234, 7, 0, (0, 1000), -1): 10,
                            (1101233, 7, 0, (0, 1000), -1): 10,
                            (1101208, 3, 2, (0, 1000), -1): 10,
                            (1101207, 3, 3, (0, 1000), -1): 10,
                            (1101206, 3, 3, (0, 1000), -1): 10,
                            (1101205, 3, 2, (0, 1000), -1): 10,
                            (1101204, 3, 0, (0, 1000), -1): 10,
                            (1101111, 3, 0, (0, 1000), -1): 10,
                            (1101604, 5, 1, (0, 1000), -1): 6,
                            (1101603, 5, 1, (0, 1000), -1): 4,
                            (1101201, 1, 0, (0, 1000), -1): 10 },
                        3: {
                            (1101112, 8, 0, (0, 1000), -1): 10,
                            (1101251, 3, 0, (0, 1000), -1): 10,
                            (1101206, 3, 0, (0, 1000), -1): 10,
                            (1101205, 3, 0, (0, 1000), -1): 10,
                            (1101204, 3, 0, (0, 1000), -1): 10,
                            (1101111, 3, 0, (0, 1000), -1): 10,
                            (1101605, 1, 0, (0, 1000), -1): 10,
                            (1101604, 1, 0, (0, 1000), -1): 6,
                            (1101603, 1, 0, (0, 1000), -1): 4,
                            (1101601, 1, 0, (0, 1000), -1): 10,
                            (1101203, 1, 0, (0, 1000), -1): 10,
                            (1101202, 1, 0, (0, 1000), -1): 10,
                            (1101201, 1, 0, (0, 1000), -1): 10 } },
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
                        (3, 0): [
                            (1030, 1),
                            (1050, 1),
                            (1053, 1),
                            (1054, 1),
                            (1056, 1)],
                        (2, 0): [
                            (1015, 1)],
                        (1, 0): [
                            (1015, 1),
                            (1030, 1),
                            (1050, 1),
                            (1053, 1),
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
                            1201603: [],
                            1201904: [],
                            1201902: [],
                            1201116: [],
                            1201117: [],
                            1204103: [],
                            1201202: [],
                            1201604: [] },
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
                            1201203: [],
                            1201604: [] },
                        3: {
                            1201112: [],
                            1201114: [],
                            1201603: [],
                            1201904: [],
                            1201902: [],
                            1201116: [],
                            1201117: [],
                            1204103: [],
                            1201202: [] } },
                    'HideLevel': {
                        1: {
                            1201112: 3,
                            1201114: 3,
                            1201603: 1,
                            1201904: 1,
                            1201902: 1,
                            1201116: 3,
                            1201117: 3,
                            1204103: 1,
                            1201202: 1,
                            1201604: 1 },
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
                            1201203: 1,
                            1201604: 5 },
                        3: {
                            1201112: 3,
                            1201114: 3,
                            1201603: 1,
                            1201904: 1,
                            1201902: 1,
                            1201116: 3,
                            1201117: 3,
                            1204103: 1,
                            1201202: 1 } },
                    'HideLevelStore': {
                        1: {
                            (1201604, 1, 2, (0, 1000), -1): 10,
                            (1201202, 1, 0, (0, 1000), -1): 10,
                            (1204103, 1, 0, (0, 1000), -1): 10,
                            (1201117, 3, 0, (0, 1000), -1): 10,
                            (1201116, 3, 0, (0, 1000), -1): 10,
                            (1201902, 1, 0, (0, 1000), -1): 10,
                            (1201904, 1, 0, (0, 1000), -1): 10,
                            (1201603, 1, 2, (0, 1000), -1): 10,
                            (1201114, 3, 0, (0, 1000), -1): 10,
                            (1201112, 3, 0, (0, 1000), -1): 10 },
                        2: {
                            (1201604, 5, 2, (0, 1000), -1): 10,
                            (1201203, 1, 0, (0, 1000), -1): 10,
                            (1201202, 1, 0, (0, 1000), -1): 10,
                            (1204103, 3, 0, (0, 1000), -1): 10,
                            (1201117, 3, 0, (0, 1000), -1): 10,
                            (1201116, 3, 1, (0, 1000), -1): 10,
                            (1201115, 3, 1, (0, 1000), -1): 10,
                            (1201902, 6, 0, (0, 1000), -1): 10,
                            (1201904, 6, 0, (0, 1000), -1): 10,
                            (1201603, 5, 2, (0, 1000), -1): 10,
                            (1201114, 3, 0, (0, 1000), -1): 10,
                            (1201112, 3, 0, (0, 1000), -1): 10 },
                        3: {
                            (1201202, 1, 0, (0, 1000), -1): 10,
                            (1204103, 1, 0, (0, 1000), -1): 10,
                            (1201117, 3, 0, (0, 1000), -1): 10,
                            (1201116, 3, 0, (0, 1000), -1): 10,
                            (1201902, 1, 0, (0, 1000), -1): 10,
                            (1201904, 1, 0, (0, 1000), -1): 10,
                            (1201603, 1, 0, (0, 1000), -1): 10,
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
                    'NormalStore': (1203141, 1203142, 1203143, 1203145, 1203146, 1203144, 1203147),
                    'NormalFilter': {
                        1203141: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1203142: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1203143: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1203145: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1203146: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1203144: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1203147: {
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
                            (1052, 1),
                            (1057, 1)],
                        (1, 0): [
                            (1005, 1),
                            (1030, 1),
                            (1050, 1),
                            (1051, 1),
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
                            1201112: [],
                            1201114: [],
                            1201603: [],
                            1201904: [],
                            1201902: [],
                            1201116: [],
                            1201117: [],
                            1204103: [],
                            1201202: [],
                            1201604: [],
                            1201119: [] },
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
                            1201203: [],
                            1201604: [],
                            1201119: [] },
                        3: {
                            1201112: [],
                            1201114: [],
                            1201603: [],
                            1201904: [],
                            1201902: [],
                            1201116: [],
                            1201117: [],
                            1204103: [],
                            1201202: [],
                            1201119: [] } },
                    'HideLevel': {
                        1: {
                            1201112: 3,
                            1201114: 3,
                            1201603: 1,
                            1201904: 1,
                            1201902: 1,
                            1201116: 3,
                            1201117: 3,
                            1204103: 1,
                            1201202: 1,
                            1201604: 1,
                            1201119: 8 },
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
                            1201203: 1,
                            1201604: 5,
                            1201119: 8 },
                        3: {
                            1201112: 3,
                            1201114: 3,
                            1201603: 1,
                            1201904: 1,
                            1201902: 1,
                            1201116: 3,
                            1201117: 3,
                            1204103: 1,
                            1201202: 1,
                            1201119: 8 } },
                    'HideLevelStore': {
                        1: {
                            (1201119, 8, 0, (0, 1000), -1): 10,
                            (1201604, 1, 2, (0, 1000), -1): 10,
                            (1201202, 1, 0, (0, 1000), -1): 10,
                            (1204103, 1, 0, (0, 1000), -1): 10,
                            (1201117, 3, 0, (0, 1000), -1): 10,
                            (1201116, 3, 0, (0, 1000), -1): 10,
                            (1201902, 1, 0, (0, 1000), -1): 10,
                            (1201904, 1, 0, (0, 1000), -1): 10,
                            (1201603, 1, 2, (0, 1000), -1): 10,
                            (1201114, 3, 0, (0, 1000), -1): 10,
                            (1201112, 3, 0, (0, 1000), -1): 10 },
                        2: {
                            (1201119, 8, 0, (0, 1000), -1): 10,
                            (1201604, 5, 2, (0, 1000), -1): 10,
                            (1201203, 1, 0, (0, 1000), -1): 10,
                            (1201202, 1, 0, (0, 1000), -1): 10,
                            (1204103, 3, 0, (0, 1000), -1): 10,
                            (1201117, 3, 0, (0, 1000), -1): 10,
                            (1201116, 3, 1, (0, 1000), -1): 10,
                            (1201115, 3, 1, (0, 1000), -1): 10,
                            (1201902, 6, 0, (0, 1000), -1): 10,
                            (1201904, 6, 0, (0, 1000), -1): 10,
                            (1201603, 5, 2, (0, 1000), -1): 10,
                            (1201114, 3, 0, (0, 1000), -1): 10,
                            (1201112, 3, 0, (0, 1000), -1): 10 },
                        3: {
                            (1201119, 8, 0, (0, 1000), -1): 10,
                            (1201202, 1, 0, (0, 1000), -1): 10,
                            (1204103, 1, 0, (0, 1000), -1): 10,
                            (1201117, 3, 0, (0, 1000), -1): 10,
                            (1201116, 3, 0, (0, 1000), -1): 10,
                            (1201902, 1, 0, (0, 1000), -1): 10,
                            (1201904, 1, 0, (0, 1000), -1): 10,
                            (1201603, 1, 0, (0, 1000), -1): 10,
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
                    'NormalStore': (1205101, 1205102, 1205103, 1205104, 1205105, 1205106, 1205107, 1205108, 1205109, 1205110),
                    'NormalFilter': {
                        1205101: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1205102: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1205103: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1205104: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1205105: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1205106: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1205107: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1205108: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1205109: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1205110: {
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
                            (1052, 1),
                            (1054, 1),
                            (1057, 1)],
                        (1, 0): [
                            (1026, 1),
                            (1027, 1)] },
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
                            1201603: [],
                            1201904: [],
                            1201902: [],
                            1201116: [],
                            1201117: [],
                            1204103: [],
                            1201202: [],
                            1201604: [],
                            1201119: [] },
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
                            1201203: [],
                            1201604: [],
                            1201119: [] },
                        3: {
                            1201112: [],
                            1201114: [],
                            1201603: [],
                            1201904: [],
                            1201902: [],
                            1201116: [],
                            1201117: [],
                            1204103: [],
                            1201202: [],
                            1201119: [] } },
                    'HideLevel': {
                        1: {
                            1201112: 3,
                            1201114: 3,
                            1201603: 1,
                            1201904: 1,
                            1201902: 1,
                            1201116: 3,
                            1201117: 3,
                            1204103: 1,
                            1201202: 1,
                            1201604: 1,
                            1201119: 8 },
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
                            1201203: 1,
                            1201604: 5,
                            1201119: 8 },
                        3: {
                            1201112: 3,
                            1201114: 3,
                            1201603: 1,
                            1201904: 1,
                            1201902: 1,
                            1201116: 3,
                            1201117: 3,
                            1204103: 1,
                            1201202: 1,
                            1201119: 8 } },
                    'HideLevelStore': {
                        1: {
                            (1201119, 8, 0, (0, 1000), -1): 10,
                            (1201604, 1, 2, (0, 1000), -1): 10,
                            (1201202, 1, 0, (0, 1000), -1): 10,
                            (1204103, 1, 0, (0, 1000), -1): 10,
                            (1201117, 3, 0, (0, 1000), -1): 10,
                            (1201116, 3, 0, (0, 1000), -1): 10,
                            (1201902, 1, 0, (0, 1000), -1): 10,
                            (1201904, 1, 0, (0, 1000), -1): 10,
                            (1201603, 1, 2, (0, 1000), -1): 10,
                            (1201114, 3, 0, (0, 1000), -1): 10,
                            (1201112, 3, 0, (0, 1000), -1): 10 },
                        2: {
                            (1201119, 8, 0, (0, 1000), -1): 10,
                            (1201604, 5, 2, (0, 1000), -1): 10,
                            (1201203, 1, 0, (0, 1000), -1): 10,
                            (1201202, 1, 0, (0, 1000), -1): 10,
                            (1204103, 3, 0, (0, 1000), -1): 10,
                            (1201117, 3, 0, (0, 1000), -1): 10,
                            (1201116, 3, 1, (0, 1000), -1): 10,
                            (1201115, 3, 1, (0, 1000), -1): 10,
                            (1201902, 6, 0, (0, 1000), -1): 10,
                            (1201904, 6, 0, (0, 1000), -1): 10,
                            (1201603, 5, 2, (0, 1000), -1): 10,
                            (1201114, 3, 0, (0, 1000), -1): 10,
                            (1201112, 3, 0, (0, 1000), -1): 10 },
                        3: {
                            (1201119, 8, 0, (0, 1000), -1): 10,
                            (1201202, 1, 0, (0, 1000), -1): 10,
                            (1204103, 1, 0, (0, 1000), -1): 10,
                            (1201117, 3, 0, (0, 1000), -1): 10,
                            (1201116, 3, 0, (0, 1000), -1): 10,
                            (1201902, 1, 0, (0, 1000), -1): 10,
                            (1201904, 1, 0, (0, 1000), -1): 10,
                            (1201603, 1, 0, (0, 1000), -1): 10,
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
                        (3, 0): [
                            (1029, 1),
                            (1050, 1),
                            (1051, 1),
                            (1052, 1),
                            (1054, 1)],
                        (2, 0): [
                            (1028, 1),
                            (1029, 1)],
                        (1, 0): [
                            (1029, 1),
                            (1050, 1),
                            (1051, 1),
                            (1052, 1),
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
                            1300102: [],
                            1300103: [],
                            1300104: [],
                            1301902: [],
                            1300105: [],
                            1300106: [],
                            1300107: [],
                            1300108: [],
                            1300109: [],
                            1300110: [] },
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
                        3: {
                            1300102: [],
                            1300103: [],
                            1300104: [],
                            1301902: [],
                            1300105: [],
                            1300106: [],
                            1300107: [],
                            1300108: [],
                            1300109: [],
                            1300110: [] } },
                    'HideLevel': {
                        1: {
                            1300102: 3,
                            1300103: 3,
                            1300104: 8,
                            1301902: 1,
                            1300105: 3,
                            1300106: 3,
                            1300107: 3,
                            1300108: 3,
                            1300109: 3,
                            1300110: 3 },
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
                            1301902: 1,
                            1300105: 3,
                            1300106: 3,
                            1300107: 3,
                            1300108: 3,
                            1300109: 3,
                            1300110: 3 } },
                    'HideLevelStore': {
                        1: {
                            (1300110, 3, 0, (0, 1000), -1): 10,
                            (1300109, 3, 0, (0, 1000), -1): 10,
                            (1300108, 3, 0, (0, 1000), -1): 10,
                            (1300107, 3, 0, (0, 1000), -1): 10,
                            (1300106, 3, 0, (0, 1000), -1): 10,
                            (1300105, 3, 0, (0, 1000), -1): 10,
                            (1301902, 1, 0, (0, 1000), -1): 10,
                            (1300104, 8, 0, (0, 1000), -1): 10,
                            (1300103, 3, 0, (0, 1000), -1): 10,
                            (1300102, 3, 0, (0, 1000), -1): 10 },
                        2: {
                            (1300111, 3, 4, (0, 1000), -1): 10,
                            (1301202, 1, 0, (0, 1000), -1): 10,
                            (1301201, 1, 0, (0, 1000), -1): 10,
                            (1300110, 3, 3, (0, 1000), -1): 10,
                            (1300109, 3, 2, (0, 1000), -1): 10,
                            (1300108, 3, 3, (0, 1000), -1): 10,
                            (1300107, 3, 2, (0, 1000), -1): 10,
                            (1300106, 3, 0, (0, 1000), -1): 10,
                            (1300105, 3, 4, (0, 1000), -1): 10,
                            (1301902, 6, 0, (0, 1000), -1): 10,
                            (1300104, 8, 0, (0, 1000), -1): 10,
                            (1300103, 3, 1, (0, 1000), -1): 10,
                            (1300102, 3, 1, (0, 1000), -1): 10 },
                        3: {
                            (1300110, 3, 0, (0, 1000), -1): 10,
                            (1300109, 3, 0, (0, 1000), -1): 10,
                            (1300108, 3, 0, (0, 1000), -1): 10,
                            (1300107, 3, 0, (0, 1000), -1): 10,
                            (1300106, 3, 0, (0, 1000), -1): 10,
                            (1300105, 3, 0, (0, 1000), -1): 10,
                            (1301902, 1, 0, (0, 1000), -1): 10,
                            (1300104, 8, 0, (0, 1000), -1): 10,
                            (1300103, 3, 0, (0, 1000), -1): 10,
                            (1300102, 3, 0, (0, 1000), -1): 10 } },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': {
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'AIlevelEnhance': 0 },
                2: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (1302101, 1302102, 1302103, 1302104, 1302105, 1302120, 1302107, 1302108, 1302161, 1302162),
                    'NormalFilter': {
                        1302101: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1302102: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1302103: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1302104: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1302105: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1302120: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1302107: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1302108: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1302161: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1302162: {
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
                            (1050, 1),
                            (1052, 1),
                            (1053, 1),
                            (1056, 1)],
                        (1, 0): [
                            (1024, 1),
                            (1055, 1)] },
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
                            1300102: [],
                            1300103: [],
                            1300104: [],
                            1301902: [],
                            1300105: [],
                            1300106: [],
                            1300107: [],
                            1300108: [],
                            1300109: [],
                            1300110: [] },
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
                        3: {
                            1300102: [],
                            1300103: [],
                            1300104: [],
                            1301902: [],
                            1300105: [],
                            1300106: [],
                            1300107: [],
                            1300108: [],
                            1300109: [],
                            1300110: [] } },
                    'HideLevel': {
                        1: {
                            1300102: 3,
                            1300103: 3,
                            1300104: 8,
                            1301902: 1,
                            1300105: 3,
                            1300106: 3,
                            1300107: 3,
                            1300108: 3,
                            1300109: 3,
                            1300110: 3 },
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
                            1301902: 1,
                            1300105: 3,
                            1300106: 3,
                            1300107: 3,
                            1300108: 3,
                            1300109: 3,
                            1300110: 3 } },
                    'HideLevelStore': {
                        1: {
                            (1300110, 3, 0, (0, 1000), -1): 10,
                            (1300109, 3, 0, (0, 1000), -1): 10,
                            (1300108, 3, 0, (0, 1000), -1): 10,
                            (1300107, 3, 0, (0, 1000), -1): 10,
                            (1300106, 3, 0, (0, 1000), -1): 10,
                            (1300105, 3, 0, (0, 1000), -1): 10,
                            (1301902, 1, 0, (0, 1000), -1): 10,
                            (1300104, 8, 0, (0, 1000), -1): 10,
                            (1300103, 3, 0, (0, 1000), -1): 10,
                            (1300102, 3, 0, (0, 1000), -1): 10 },
                        2: {
                            (1300111, 3, 4, (0, 1000), -1): 10,
                            (1301202, 1, 0, (0, 1000), -1): 10,
                            (1301201, 1, 0, (0, 1000), -1): 10,
                            (1300110, 3, 3, (0, 1000), -1): 10,
                            (1300109, 3, 2, (0, 1000), -1): 10,
                            (1300108, 3, 3, (0, 1000), -1): 10,
                            (1300107, 3, 2, (0, 1000), -1): 10,
                            (1300106, 3, 0, (0, 1000), -1): 10,
                            (1300105, 3, 4, (0, 1000), -1): 10,
                            (1301902, 6, 0, (0, 1000), -1): 10,
                            (1300104, 8, 0, (0, 1000), -1): 10,
                            (1300103, 3, 1, (0, 1000), -1): 10,
                            (1300102, 3, 1, (0, 1000), -1): 10 },
                        3: {
                            (1300110, 3, 0, (0, 1000), -1): 10,
                            (1300109, 3, 0, (0, 1000), -1): 10,
                            (1300108, 3, 0, (0, 1000), -1): 10,
                            (1300107, 3, 0, (0, 1000), -1): 10,
                            (1300106, 3, 0, (0, 1000), -1): 10,
                            (1300105, 3, 0, (0, 1000), -1): 10,
                            (1301902, 1, 0, (0, 1000), -1): 10,
                            (1300104, 8, 0, (0, 1000), -1): 10,
                            (1300103, 3, 0, (0, 1000), -1): 10,
                            (1300102, 3, 0, (0, 1000), -1): 10 } },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': {
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'AIlevelEnhance': 0 },
                3: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (1303101, 1303102, 1303103, 1303104, 1303105, 1303106, 1303107, 1303108),
                    'NormalFilter': {
                        1303101: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1303102: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1303103: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1303104: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1303105: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1303106: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1303107: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1303108: {
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
                            (1025, 1),
                            (1030, 1),
                            (1050, 1),
                            (1056, 1)],
                        (1, 0): [
                            (1050, 1)] },
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
                            1300102: [],
                            1300103: [],
                            1300104: [],
                            1301902: [],
                            1300105: [],
                            1300106: [],
                            1300107: [],
                            1300108: [],
                            1300109: [],
                            1300110: [] },
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
                        3: {
                            1300102: [],
                            1300103: [],
                            1300104: [],
                            1301902: [],
                            1300105: [],
                            1300106: [],
                            1300107: [],
                            1300108: [],
                            1300109: [],
                            1300110: [] } },
                    'HideLevel': {
                        1: {
                            1300102: 3,
                            1300103: 3,
                            1300104: 8,
                            1301902: 1,
                            1300105: 3,
                            1300106: 3,
                            1300107: 3,
                            1300108: 3,
                            1300109: 3,
                            1300110: 3 },
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
                            1301902: 1,
                            1300105: 3,
                            1300106: 3,
                            1300107: 3,
                            1300108: 3,
                            1300109: 3,
                            1300110: 3 } },
                    'HideLevelStore': {
                        1: {
                            (1300110, 3, 0, (0, 1000), -1): 10,
                            (1300109, 3, 0, (0, 1000), -1): 10,
                            (1300108, 3, 0, (0, 1000), -1): 10,
                            (1300107, 3, 0, (0, 1000), -1): 10,
                            (1300106, 3, 0, (0, 1000), -1): 10,
                            (1300105, 3, 0, (0, 1000), -1): 10,
                            (1301902, 1, 0, (0, 1000), -1): 10,
                            (1300104, 8, 0, (0, 1000), -1): 10,
                            (1300103, 3, 0, (0, 1000), -1): 10,
                            (1300102, 3, 0, (0, 1000), -1): 10 },
                        2: {
                            (1300111, 3, 4, (0, 1000), -1): 10,
                            (1301202, 1, 0, (0, 1000), -1): 10,
                            (1301201, 1, 0, (0, 1000), -1): 10,
                            (1300110, 3, 3, (0, 1000), -1): 10,
                            (1300109, 3, 2, (0, 1000), -1): 10,
                            (1300108, 3, 3, (0, 1000), -1): 10,
                            (1300107, 3, 2, (0, 1000), -1): 10,
                            (1300106, 3, 0, (0, 1000), -1): 10,
                            (1300105, 3, 4, (0, 1000), -1): 10,
                            (1301902, 6, 0, (0, 1000), -1): 10,
                            (1300104, 8, 0, (0, 1000), -1): 10,
                            (1300103, 3, 1, (0, 1000), -1): 10,
                            (1300102, 3, 1, (0, 1000), -1): 10 },
                        3: {
                            (1300110, 3, 0, (0, 1000), -1): 10,
                            (1300109, 3, 0, (0, 1000), -1): 10,
                            (1300108, 3, 0, (0, 1000), -1): 10,
                            (1300107, 3, 0, (0, 1000), -1): 10,
                            (1300106, 3, 0, (0, 1000), -1): 10,
                            (1300105, 3, 0, (0, 1000), -1): 10,
                            (1301902, 1, 0, (0, 1000), -1): 10,
                            (1300104, 8, 0, (0, 1000), -1): 10,
                            (1300103, 3, 0, (0, 1000), -1): 10,
                            (1300102, 3, 0, (0, 1000), -1): 10 } },
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
                        (3, 0): None,
                        (2, 0): [
                            (1003, 2),
                            (1051, 1),
                            (1015, 2),
                            (1050, 2)],
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
                            1401201: [],
                            1401204: [],
                            1401205: [] },
                        2: {
                            1401201: [],
                            1401204: [],
                            1401205: [] },
                        3: {
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
                        1: {
                            (1401205, 3, 0, (0, 1000), -1): 10,
                            (1401204, 3, 0, (0, 1000), -1): 10,
                            (1401201, 1, 0, (0, 1000), -1): 10 },
                        2: {
                            (1401205, 3, 0, (0, 1000), -1): 10,
                            (1401204, 3, 0, (0, 1000), -1): 10,
                            (1401201, 1, 0, (0, 1000), -1): 10 },
                        3: {
                            (1401205, 3, 0, (0, 1000), -1): 10,
                            (1401204, 3, 0, (0, 1000), -1): 10,
                            (1401201, 1, 0, (0, 1000), -1): 10 } },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': {
                        (3, 0): [],
                        (2, 0): [],
                        (1, 0): [] },
                    'AIlevelEnhance': 0 },
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
                        (3, 0): None,
                        (2, 0): [
                            (1054, 1),
                            (1056, 1),
                            (1087, 1),
                            (1053, 1)],
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
                            1401202: [],
                            1401203: [],
                            1401206: [] },
                        2: {
                            1401202: [],
                            1401203: [],
                            1401206: [] },
                        3: {
                            1401202: [],
                            1401203: [],
                            1401206: [] } },
                    'HideLevel': {
                        1: {
                            1401202: 1,
                            1401203: 3,
                            1401206: 1 },
                        2: {
                            1401202: 1,
                            1401203: 3,
                            1401206: 1 },
                        3: {
                            1401202: 1,
                            1401203: 3,
                            1401206: 1 } },
                    'HideLevelStore': {
                        1: {
                            (1401206, 1, 0, (0, 1000), -1): 10,
                            (1401203, 3, 0, (0, 1000), -1): 10,
                            (1401202, 1, 0, (0, 1000), -1): 10 },
                        2: {
                            (1401206, 1, 0, (0, 1000), -1): 10,
                            (1401203, 3, 0, (0, 1000), -1): 10,
                            (1401202, 1, 0, (0, 1000), -1): 10 },
                        3: {
                            (1401206, 1, 0, (0, 1000), -1): 10,
                            (1401203, 3, 0, (0, 1000), -1): 10,
                            (1401202, 1, 0, (0, 1000), -1): 10 } },
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
                            ('HPMax', -3500, 0),
                            ('ShieldMax', -3500, 0),
                            ('ArmorMax', -3500, 0),
                            ('Att', -4000, 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', -2500, 0),
                            ('ShieldMax', -2500, 0),
                            ('ArmorMax', -2500, 0),
                            ('Att', -3000, 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', -3500, 0),
                            ('ShieldMax', -3500, 0),
                            ('ArmorMax', -3500, 0),
                            ('Att', -4000, 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', -2500, 0),
                            ('ShieldMax', -2500, 0),
                            ('ArmorMax', -2500, 0),
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
                            ('HPMax', -5000, 0),
                            ('ShieldMax', -5000, 0),
                            ('ArmorMax', -5000, 0),
                            ('Att', -3000, 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', -5000, 0),
                            ('ShieldMax', -5000, 0),
                            ('ArmorMax', -5000, 0),
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
            'Att': 4000,
            'HPMax': 4000,
            'ArmorMax': 4000,
            'ShieldMax': 4000,
            'MoveSpeed': 2000 },
        2: {
            'Att': 4000,
            'HPMax': 4000,
            'ArmorMax': 4000,
            'ShieldMax': 4000,
            'MoveSpeed': 2000 },
        3: {
            'Att': 8000,
            'HPMax': 14000,
            'ArmorMax': 14000,
            'ShieldMax': 14000,
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
                    'ChooseRatio': (lambda *a: 20 + min(int(Func231(*a) // 3), 50)),
                    'LevelConfig': {
                        1: {
                            'LevelLimit': (lambda *a: 6 + min(int(Func231(*a) // 35), 4)),
                            'LevelLive': 1,
                            'RoomLimit': (lambda *a: 2 + min(int(Func231(*a) // 70), 2)),
                            'RoomLive': 1 },
                        2: {
                            'LevelLimit': (lambda *a: 8 + min(int(Func231(*a) // 35), 4)),
                            'LevelLive': 1,
                            'RoomLimit': (lambda *a: 3 + min(int(Func231(*a) // 70), 2)),
                            'RoomLive': 1 },
                        3: {
                            'LevelLimit': (lambda *a: 11 + min(int(Func231(*a) // 35), 4)),
                            'LevelLive': 1,
                            'RoomLimit': (lambda *a: 3 + min(int(Func231(*a) // 70), 2)),
                            'RoomLive': 1 },
                        4: {
                            'LevelLimit': (lambda *a: 13 + min(int(Func231(*a) // 35), 4)),
                            'LevelLive': (lambda *a: 1 + min(int(Func231(*a) // 100), 1)),
                            'RoomLimit': (lambda *a: 4 + min(int(Func231(*a) // 70), 2)),
                            'RoomLive': (lambda *a: 1 + min(int(Func231(*a) // 100), 1)) } },
                    'SuperLevel': 2 },
                2: {
                    'ChooseRatio': (lambda *a: 20 + min(int(Func231(*a) // 3), 50)),
                    'LevelConfig': {
                        1: {
                            'LevelLimit': (lambda *a: 8 + min(int(Func231(*a) // 35), 4)),
                            'LevelLive': 1,
                            'RoomLimit': (lambda *a: 3 + min(int(Func231(*a) // 70), 2)),
                            'RoomLive': 1 },
                        2: {
                            'LevelLimit': (lambda *a: 11 + min(int(Func231(*a) // 35), 4)),
                            'LevelLive': 1,
                            'RoomLimit': (lambda *a: 3 + min(int(Func231(*a) // 70), 2)),
                            'RoomLive': 1 },
                        3: {
                            'LevelLimit': (lambda *a: 13 + min(int(Func231(*a) // 35), 4)),
                            'LevelLive': (lambda *a: 1 + min(int(Func231(*a) // 100), 1)),
                            'RoomLimit': (lambda *a: 4 + min(int(Func231(*a) // 70), 2)),
                            'RoomLive': (lambda *a: 1 + min(int(Func231(*a) // 100), 1)) } },
                    'SuperLevel': 2 },
                3: {
                    'ChooseRatio': (lambda *a: 20 + min(int(Func231(*a) // 3), 50)),
                    'LevelConfig': {
                        1: {
                            'LevelLimit': (lambda *a: 8 + min(int(Func231(*a) // 35), 4)),
                            'LevelLive': 1,
                            'RoomLimit': (lambda *a: 3 + min(int(Func231(*a) // 70), 2)),
                            'RoomLive': 1 },
                        2: {
                            'LevelLimit': (lambda *a: 11 + min(int(Func231(*a) // 35), 4)),
                            'LevelLive': 1,
                            'RoomLimit': (lambda *a: 3 + min(int(Func231(*a) // 70), 2)),
                            'RoomLive': 1 },
                        3: {
                            'LevelLimit': (lambda *a: 13 + min(int(Func231(*a) // 35), 4)),
                            'LevelLive': (lambda *a: 1 + min(int(Func231(*a) // 100), 1)),
                            'RoomLimit': (lambda *a: 4 + min(int(Func231(*a) // 70), 2)),
                            'RoomLive': (lambda *a: 1 + min(int(Func231(*a) // 100), 1)) } },
                    'SuperLevel': 2 },
                4: {
                    'ChooseRatio': (lambda *a: 20 + min(int(Func231(*a) // 3), 50)),
                    'LevelConfig': {
                        1: {
                            'LevelLimit': (lambda *a: 8 + min(int(Func231(*a) // 35), 4)),
                            'LevelLive': 1,
                            'RoomLimit': (lambda *a: 3 + min(int(Func231(*a) // 70), 2)),
                            'RoomLive': 1 },
                        2: {
                            'LevelLimit': (lambda *a: 11 + min(int(Func231(*a) // 35), 4)),
                            'LevelLive': 1,
                            'RoomLimit': (lambda *a: 3 + min(int(Func231(*a) // 70), 2)),
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
    m_SID = 3008
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

