# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/wm3005.pyc
# RelativePath: clientlogic/cl_wardata/wm3005.pyc
# Source Generated with Decompyle++
# File: wm3005.pyc (Python 3.6)

from __future__ import absolute_import
from cl_warmgr.mobject import CWarManager as CCustomWarMgr
from cl_commondefines import GAMETYPE_DESTROY, HIDELV_TYPE_NORMAL, LAYER_CHOOSE_CHALLENGE, LAYER_CHOOSE_CRAFTSMAN, LAYER_CHOOSE_EVENTNPC, LAYER_CHOOSE_HIDE, LAYER_CHOOSE_SHOP, LEVEL_TYPE_BOSS, LEVEL_TYPE_FIGHT, LEVEL_TYPE_HALL, LEVEL_TYPE_HIDE
from cl_newformula import Func204, Func205
import cl_msgcenter
import cl_warmgr.waraction as waraction
import cl_warmgr.warcondition as warcondition
import cl_warmgr.testelement
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

class CTestElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'TESTBULLET': ((4502, 30), (4503, 10), (4504, 4), (4508, 8)) }


class CLevelCtrlElement(cl_warmgr.mobject.CElementData):
    m_LevelCtrlConf = {
        1: {
            'CtrlSize': 3,
            'HallInfo': 1100001,
            'BossInfo': {
                'BossStore': {
                    1101006: 10 },
                'BossExtra': {
                    1101006: (None, None) },
                'ChallengeStore': { },
                'SingleChallengeStore': { },
                'ExcludeChallengeArea': { },
                'UnSpawnRuleInfo': {
                    1101006: [] },
                'ChallengeModeLimit': { },
                'AIBosslevelEnhance': {
                    1101006: 0 } },
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
                        (3, 0): None,
                        (2, 0): None,
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
                            1101203: [] },
                        2: {
                            1101201: [],
                            1101202: [],
                            1101203: [] },
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
                            1101203: 1 },
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
                        (3, 0): None,
                        (2, 0): None,
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
                            1101601: [] },
                        2: {
                            1101201: [],
                            1101202: [],
                            1101203: [],
                            1101601: [] },
                        3: {
                            1101201: [],
                            1101202: [],
                            1101203: [],
                            1101601: [] } },
                    'HideLevel': {
                        1: {
                            1101201: 1,
                            1101202: 1,
                            1101203: 1,
                            1101601: 1 },
                        2: {
                            1101201: 1,
                            1101202: 1,
                            1101203: 1,
                            1101601: 1 },
                        3: {
                            1101201: 1,
                            1101202: 1,
                            1101203: 1,
                            1101601: 1 } },
                    'HideLevelStore': {
                        1: {
                            (1101601, 1, 0, (0, 1000), -1): 10,
                            (1101203, 1, 0, (0, 1000), -1): 10,
                            (1101202, 1, 0, (0, 1000), -1): 10,
                            (1101201, 1, 0, (0, 1000), -1): 10 },
                        2: {
                            (1101601, 1, 0, (0, 1000), -1): 10,
                            (1101203, 1, 0, (0, 1000), -1): 10,
                            (1101202, 1, 0, (0, 1000), -1): 10,
                            (1101201, 1, 0, (0, 1000), -1): 10 },
                        3: {
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
                    'NormalStore': (1103154, 1103155, 1103157, 1103158, 1103159, 1103160),
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
                            1101601: [],
                            1101111: [],
                            1101205: [],
                            1101206: [],
                            1101251: [],
                            1101252: [] },
                        2: {
                            1101201: [],
                            1101601: [],
                            1101111: [],
                            1101205: [],
                            1101206: [],
                            1101251: [],
                            1101252: [] },
                        3: {
                            1101201: [],
                            1101601: [],
                            1101111: [],
                            1101205: [],
                            1101206: [],
                            1101251: [],
                            1101252: [] } },
                    'HideLevel': {
                        1: {
                            1101201: 1,
                            1101601: 1,
                            1101111: 1,
                            1101205: 1,
                            1101206: 1,
                            1101251: 1,
                            1101252: 1 },
                        2: {
                            1101201: 1,
                            1101601: 1,
                            1101111: 1,
                            1101205: 1,
                            1101206: 1,
                            1101251: 1,
                            1101252: 1 },
                        3: {
                            1101201: 1,
                            1101601: 1,
                            1101111: 1,
                            1101205: 1,
                            1101206: 1,
                            1101251: 1,
                            1101252: 1 } },
                    'HideLevelStore': {
                        1: {
                            (1101252, 1, 0, (0, 1000), -1): 10,
                            (1101251, 1, 0, (0, 1000), -1): 10,
                            (1101206, 1, 0, (0, 1000), -1): 10,
                            (1101205, 1, 0, (0, 1000), -1): 10,
                            (1101111, 1, 0, (0, 1000), -1): 10,
                            (1101601, 1, 0, (0, 1000), -1): 10,
                            (1101201, 1, 0, (0, 1000), -1): 10 },
                        2: {
                            (1101252, 1, 0, (0, 1000), -1): 10,
                            (1101251, 1, 0, (0, 1000), -1): 10,
                            (1101206, 1, 0, (0, 1000), -1): 10,
                            (1101205, 1, 0, (0, 1000), -1): 10,
                            (1101111, 1, 0, (0, 1000), -1): 10,
                            (1101601, 1, 0, (0, 1000), -1): 10,
                            (1101201, 1, 0, (0, 1000), -1): 10 },
                        3: {
                            (1101252, 1, 0, (0, 1000), -1): 10,
                            (1101251, 1, 0, (0, 1000), -1): 10,
                            (1101206, 1, 0, (0, 1000), -1): 10,
                            (1101205, 1, 0, (0, 1000), -1): 10,
                            (1101111, 1, 0, (0, 1000), -1): 10,
                            (1101601, 1, 0, (0, 1000), -1): 10,
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
                    LAYER_CHOOSE_CRAFTSMAN: (1, 0, 0, 99, {
                        1: 0,
                        2: 15,
                        3: 30 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_SHOP: (1, 0, 1, 99, {
                        1: 0,
                        2: 5,
                        3: 30 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_EVENTNPC: (1, 0, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 30 }, { }),
                    LAYER_CHOOSE_CHALLENGE: (1, 0, 0, 99, {
                        1: 15,
                        2: 20,
                        3: 25 }, { }),
                    LAYER_CHOOSE_HIDE: (2, 0, 0, 99, {
                        1: 10,
                        2: 20,
                        3: 30 }, {
                        1: 1,
                        2: 1,
                        3: 1 }) },
                2: {
                    LAYER_CHOOSE_CRAFTSMAN: (1, 0, 0, 99, {
                        1: 0,
                        2: 15,
                        3: 30 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_SHOP: (1, 0, 1, 99, {
                        1: 0,
                        2: 5,
                        3: 30 }, {
                        1: 1,
                        2: 1,
                        3: 1 }),
                    LAYER_CHOOSE_EVENTNPC: (2, 0, 0, 99, {
                        1: 10,
                        2: 10,
                        3: 30 }, { }),
                    LAYER_CHOOSE_CHALLENGE: (1, 0, 0, 99, {
                        1: 15,
                        2: 20,
                        3: 25 }, { }),
                    LAYER_CHOOSE_HIDE: (2, 0, 0, 99, {
                        1: 10,
                        2: 20,
                        3: 30 }, {
                        1: 1,
                        2: 1,
                        3: 1 }) } },
            'BaseGrade': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: (2, 0),
                        2: (5, 0),
                        3: (7, 0) },
                    LEVEL_TYPE_FIGHT: {
                        1: (1, 0),
                        2: (3, 0),
                        3: (5, 0) },
                    LEVEL_TYPE_BOSS: (5, 0),
                    LEVEL_TYPE_HALL: (0, 0) } },
            'MonsterAttAdjust': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 12000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 12000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 12000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 12000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 12000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 12000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 12000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 12000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 12000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 12000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 12000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 12000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 12000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 12000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 12000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 12000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 12000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 12000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * 32000 + 0), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 32000 + 0), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 32000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                        ('MoveSpeed', (lambda *a: (Func204(*a) - 1) * 600 + 0), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 30000 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * 12000 + 0), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 12000 + 0), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 12000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] } },
            'EliteAttAdjust': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 18000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 18000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 18000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 18000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 18000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 18000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 22000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 22000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 22000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 18000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 18000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 18000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 18000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 18000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 18000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 18000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 18000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 18000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * 18000 + 0), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 18000 + 0), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 18000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * 18000 + 0), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 18000 + 0), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 18000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] } },
            'ItemChoose': 1001 } }
    m_LayerAndLevelMap = { }
    m_ChooseItem = {
        1001: {
            (1, 3): {
                'WeaponChoose': (1, 0, 1001),
                'GoldenCupChoose': (0, 0, 4101),
                'RelicChoose': (1, 1, 2401) },
            (1, 2): {
                'WeaponChoose': (1, 1, 1001),
                'GoldenCupChoose': (0, 0, 4101),
                'RelicChoose': (1, 0, 2401) },
            (1, 1): {
                'WeaponChoose': (1, 0, 1001),
                'GoldenCupChoose': (0, 0, 4101),
                'RelicChoose': (1, 0, 2401) } } }
    m_SightLevelConf = { }


class CWarreport(cl_warmgr.mobject.CElementData):
    pass


class CPVEDieElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'RelifeData': 1003,
        'InitDyingSecond': 16,
        'MinDyingSecond': 6,
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
                    'ChooseRatio': (lambda *a: min(int((Func204(*a) - 1) * Func204(*a) * 25), int(Func204(*a) * 25))),
                    'LevelConfig': {
                        1: {
                            'LevelLimit': (lambda *a: Func204(*a) * 3 - 3),
                            'LevelLive': (lambda *a: Func204(*a) / 2 + 0),
                            'RoomLimit': (lambda *a: Func204(*a) - 1),
                            'RoomLive': (lambda *a: Func204(*a) / 2 + 0) },
                        2: {
                            'LevelLimit': (lambda *a: Func204(*a) * 3 - 1),
                            'LevelLive': (lambda *a: Func204(*a) / 2 + 0),
                            'RoomLimit': (lambda *a: Func204(*a) + 0),
                            'RoomLive': (lambda *a: Func204(*a) / 2 + 0) },
                        3: {
                            'LevelLimit': (lambda *a: Func204(*a) * 3 + 1),
                            'LevelLive': (lambda *a: Func204(*a) / 2 + 1),
                            'RoomLimit': (lambda *a: Func204(*a) + 1),
                            'RoomLive': (lambda *a: Func204(*a) / 2 + 1) },
                        4: {
                            'LevelLimit': (lambda *a: Func204(*a) * 3 + 3),
                            'LevelLive': (lambda *a: Func204(*a) / 2 + 1),
                            'RoomLimit': (lambda *a: Func204(*a) + 1),
                            'RoomLive': (lambda *a: Func204(*a) / 2 + 1) } },
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
                    'SuperLevel': 0 } } } }
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
            143: 0,
            198: 0 },
        'm_IgnoreHalt': [
            1413] }


class CRecycleDropElement(cl_warmgr.mobject.CElementData):
    pass


class CWarManager(CCustomWarMgr):
    m_SID = 3005
    m_StepInfo = { }
    m_InitStep = []
    m_ComponentCls = {
        'TestElement': (cl_warmgr.testelement.GetComponentClass, CTestElement),
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
        'RecycleDropElement': (cl_warmgr.recycledropelement.GetComponentClass, CRecycleDropElement) }
    m_SeasonFuncConfing = { }
    m_AllSeasonElement = { }
    m_NewVerLayer = set()
    m_SeasonElement = { }

