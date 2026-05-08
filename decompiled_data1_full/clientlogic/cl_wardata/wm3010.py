# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/wm3010.pyc
# RelativePath: clientlogic/cl_wardata/wm3010.pyc
# Source Generated with Decompyle++
# File: wm3010.pyc (Python 3.6)

from __future__ import absolute_import
from cl_warmgr.mobject import CWarManager as CCustomWarMgr
from cl_commondefines import GAMETYPE_DESTROY, LEVEL_TYPE_BOSS, LEVEL_TYPE_FIGHT, LEVEL_TYPE_HALL, LEVEL_TYPE_HIDE
from cl_newformula import Func201, Func202, Func204
import cl_msgcenter
import cl_warmgr.waraction as waraction
import cl_warmgr.warcondition as warcondition
import cl_warmgr.initresourceelement
import cl_warmgr.levelctrl
import cl_warmgr.warreport
import cl_warmgr.pvedieelement
import cl_warmgr.roundelement
import cl_warmgr.explorelevelctrl
import cl_warmgr.newbieelement

class CInitResourceElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'INITBULLET': ((4502, 135), (4503, 36), (4504, 18), (4508, 3)) }


class CLevelCtrlElement(cl_warmgr.mobject.CElementData):
    m_LevelCtrlConf = {
        1: {
            'CtrlSize': 3,
            'HallInfo': 0,
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
                'craftsman': {
                    1018: 10 },
                'shop': {
                    1005: 10 } },
            'CtrlInfo': {
                1: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (9200101,),
                    'NormalFilter': {
                        9200101: {
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
                    'ChallengeStore': { },
                    'SingleChallengeStore': { },
                    'HideLevelRoomChallenge': { },
                    'HideLevelExcludeChallenge': { },
                    'HideLevel': { },
                    'HideLevelStore': { },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': { },
                    'AIlevelEnhance': 0 },
                2: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (1101176, 1101179),
                    'NormalFilter': {
                        1101176: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1101179: {
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
                    'ChallengeStore': { },
                    'SingleChallengeStore': { },
                    'HideLevelRoomChallenge': { },
                    'HideLevelExcludeChallenge': { },
                    'HideLevel': { },
                    'HideLevelStore': { },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': { },
                    'AIlevelEnhance': 0 },
                3: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (7103154, 7103157),
                    'NormalFilter': {
                        7103154: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7103157: {
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
                    'ChallengeStore': { },
                    'SingleChallengeStore': { },
                    'HideLevelRoomChallenge': { },
                    'HideLevelExcludeChallenge': { },
                    'HideLevel': { },
                    'HideLevelStore': { },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': { },
                    'AIlevelEnhance': 0 } },
            'LayerChoose': { },
            'BaseGrade': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        2: (2, 0),
                        3: (5, 0) },
                    LEVEL_TYPE_FIGHT: {
                        2: (1, 0),
                        3: (3, 0) },
                    LEVEL_TYPE_BOSS: (5, 0),
                    LEVEL_TYPE_HALL: (0, 0) } },
            'MonsterAttAdjust': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                        ('MoveSpeed', (lambda *a: (Func204(*a) - 1) * 600 + 0), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] } },
            'EliteAttAdjust': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * 18000 + 0), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 18000 + 0), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 18000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] } },
            'ItemChoose': 1001 } }
    m_LayerAndLevelMap = { }
    m_ChooseItem = {
        1001: {
            (1, 3): {
                'WeaponChoose': (1, 0, 1001),
                'GoldenCupChoose': (0, 0, 4101),
                'RelicChoose': (1, 0, 2401) },
            (1, 2): {
                'WeaponChoose': (1, 0, 1001),
                'GoldenCupChoose': (0, 0, 4101),
                'RelicChoose': (1, 0, 2401) },
            (1, 1): {
                'WeaponChoose': (0, 0, 1001),
                'GoldenCupChoose': (0, 0, 4101),
                'RelicChoose': (0, 0, 2401) } } }
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
                        'Att': (lambda *a: max(int(Func201(*a) * -2000 + Func202(*a) * -200 + 5000), 2000)),
                        'HPMax': (lambda *a: min(int(Func201(*a) * 6000 + Func202(*a) * 1000 - 6000), 16000)),
                        'ArmorMax': (lambda *a: min(int(Func201(*a) * 6000 + Func202(*a) * 1000 - 6000), 16000)),
                        'ShieldMax': (lambda *a: min(int(Func201(*a) * 6000 + Func202(*a) * 1000 - 6000), 16000)),
                        'MoveSpeed': 200 } } },
            2: {
                (0, 0): {
                    0: {
                        'Att': (lambda *a: max(int(Func201(*a) * -4000 + Func202(*a) * -400 + 10000), 4000)),
                        'HPMax': (lambda *a: min(int(Func201(*a) * 12000 + Func202(*a) * 2000 - 12000), 32000)),
                        'ArmorMax': (lambda *a: min(int(Func201(*a) * 12000 + Func202(*a) * 2000 - 12000), 32000)),
                        'ShieldMax': (lambda *a: min(int(Func201(*a) * 12000 + Func202(*a) * 2000 - 12000), 32000)),
                        'MoveSpeed': 400 } } },
            3: {
                (0, 0): {
                    0: {
                        'Att': (lambda *a: max(int(Func201(*a) * -6000 + Func202(*a) * -600 + 15000), 6000)),
                        'HPMax': (lambda *a: min(int(Func201(*a) * 18000 + Func202(*a) * 3000 - 18000), 48000)),
                        'ArmorMax': (lambda *a: min(int(Func201(*a) * 18000 + Func202(*a) * 3000 - 18000), 48000)),
                        'ShieldMax': (lambda *a: min(int(Func201(*a) * 18000 + Func202(*a) * 3000 - 18000), 48000)),
                        'MoveSpeed': 600 } } },
            4: {
                (0, 0): {
                    0: {
                        'Att': (lambda *a: max(int(Func201(*a) * -8000 + Func202(*a) * -800 + 20000), 8000)),
                        'HPMax': (lambda *a: min(int(Func201(*a) * 24000 + Func202(*a) * 4000 - 24000), 64000)),
                        'ArmorMax': (lambda *a: min(int(Func201(*a) * 24000 + Func202(*a) * 4000 - 24000), 64000)),
                        'ShieldMax': (lambda *a: min(int(Func201(*a) * 24000 + Func202(*a) * 4000 - 24000), 64000)),
                        'MoveSpeed': 800 } } },
            5: {
                (0, 0): {
                    0: {
                        'Att': (lambda *a: max(int(Func201(*a) * -10000 + Func202(*a) * -1000 + 25000), 10000)),
                        'HPMax': (lambda *a: min(int(Func201(*a) * 30000 + Func202(*a) * 5000 - 30000), 80000)),
                        'ArmorMax': (lambda *a: min(int(Func201(*a) * 30000 + Func202(*a) * 5000 - 30000), 80000)),
                        'ShieldMax': (lambda *a: min(int(Func201(*a) * 30000 + Func202(*a) * 5000 - 30000), 80000)),
                        'MoveSpeed': 1000 } } },
            6: {
                (0, 0): {
                    0: {
                        'Att': (lambda *a: max(int(Func201(*a) * -12000 + Func202(*a) * -1200 + 30000), 12000)),
                        'HPMax': (lambda *a: min(int(Func201(*a) * 36000 + Func202(*a) * 6000 - 36000), 96000)),
                        'ArmorMax': (lambda *a: min(int(Func201(*a) * 36000 + Func202(*a) * 6000 - 36000), 96000)),
                        'ShieldMax': (lambda *a: min(int(Func201(*a) * 36000 + Func202(*a) * 6000 - 36000), 96000)),
                        'MoveSpeed': 1200 } } },
            7: {
                (0, 0): {
                    0: {
                        'Att': (lambda *a: max(int(Func201(*a) * -14000 + Func202(*a) * -1400 + 35000), 14000)),
                        'HPMax': (lambda *a: min(int(Func201(*a) * 42000 + Func202(*a) * 7000 - 42000), 112000)),
                        'ArmorMax': (lambda *a: min(int(Func201(*a) * 42000 + Func202(*a) * 7000 - 42000), 112000)),
                        'ShieldMax': (lambda *a: min(int(Func201(*a) * 42000 + Func202(*a) * 7000 - 42000), 112000)),
                        'MoveSpeed': 1400 } } },
            8: {
                (0, 0): {
                    0: {
                        'Att': (lambda *a: max(int(Func201(*a) * -14000 + Func202(*a) * -1400 + 35000), 14000)),
                        'HPMax': (lambda *a: min(int(Func201(*a) * 42000 + Func202(*a) * 7000 - 42000), 112000)),
                        'ArmorMax': (lambda *a: min(int(Func201(*a) * 42000 + Func202(*a) * 7000 - 42000), 112000)),
                        'ShieldMax': (lambda *a: min(int(Func201(*a) * 42000 + Func202(*a) * 7000 - 42000), 112000)),
                        'MoveSpeed': 1400 } } } } }
    m_ModeMonsterAttrAdjust = {
        1: { },
        2: { },
        3: { } }
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
    m_ExtRule = { }


class CExploreLevelCtrl(cl_warmgr.mobject.CElementData):
    m_LevelCtrlConf = {
        1: {
            'CtrlSize': 3,
            'HallInfo': 0,
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
                'craftsman': {
                    1018: 10 },
                'shop': {
                    1005: 10 } },
            'CtrlInfo': {
                1: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (9200101,),
                    'NormalFilter': {
                        9200101: {
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
                    'ChallengeStore': { },
                    'SingleChallengeStore': { },
                    'HideLevelRoomChallenge': { },
                    'HideLevelExcludeChallenge': { },
                    'HideLevel': { },
                    'HideLevelStore': { },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': { },
                    'AIlevelEnhance': 0 },
                2: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (1101176, 1101179),
                    'NormalFilter': {
                        1101176: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        1101179: {
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
                    'ChallengeStore': { },
                    'SingleChallengeStore': { },
                    'HideLevelRoomChallenge': { },
                    'HideLevelExcludeChallenge': { },
                    'HideLevel': { },
                    'HideLevelStore': { },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': { },
                    'AIlevelEnhance': 0 },
                3: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (7103154, 7103157),
                    'NormalFilter': {
                        7103154: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None },
                        7103157: {
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
                    'ChallengeStore': { },
                    'SingleChallengeStore': { },
                    'HideLevelRoomChallenge': { },
                    'HideLevelExcludeChallenge': { },
                    'HideLevel': { },
                    'HideLevelStore': { },
                    'HideLevelConfMap': { },
                    'HideLevelAllocMap': { },
                    'ExcludeChallengeArea': { },
                    'AIlevelEnhance': 0 } },
            'LayerChoose': { },
            'BaseGrade': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        2: (2, 0),
                        3: (5, 0) },
                    LEVEL_TYPE_FIGHT: {
                        2: (1, 0),
                        3: (3, 0) },
                    LEVEL_TYPE_BOSS: (5, 0),
                    LEVEL_TYPE_HALL: (0, 0) } },
            'MonsterAttAdjust': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                        ('MoveSpeed', (lambda *a: (Func204(*a) - 1) * 600 + 0), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] } },
            'EliteAttAdjust': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        2: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                        3: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * 18000 + 0), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 18000 + 0), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 18000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)],
                    LEVEL_TYPE_HALL: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 10000 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] } },
            'ItemChoose': 1001 } }
    m_LayerAndLevelMap = { }
    m_ChooseItem = {
        1001: {
            (1, 3): {
                'WeaponChoose': (1, 0, 1001),
                'GoldenCupChoose': (0, 0, 4101),
                'RelicChoose': (1, 0, 2401) },
            (1, 2): {
                'WeaponChoose': (1, 0, 1001),
                'GoldenCupChoose': (0, 0, 4101),
                'RelicChoose': (1, 0, 2401) },
            (1, 1): {
                'WeaponChoose': (0, 0, 1001),
                'GoldenCupChoose': (0, 0, 4101),
                'RelicChoose': (0, 0, 2401) } } }
    m_SightLevelConf = { }


class CNewbieElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'INITBULLET': ((4508, 2),),
        'INITPERFORM': (4244, 4245) }


class CWarManager(CCustomWarMgr):
    m_SID = 3010
    m_StepInfo = { }
    m_InitStep = []
    m_ComponentCls = {
        'InitResourceElement': (cl_warmgr.initresourceelement.GetComponentClass, CInitResourceElement),
        'LevelCtrl': (cl_warmgr.levelctrl.GetComponentClass, CLevelCtrlElement),
        'Warreport': (cl_warmgr.warreport.GetComponentClass, CWarreport),
        'PVEDieElement': (cl_warmgr.pvedieelement.GetComponentClass, CPVEDieElement),
        'RoundElement': (cl_warmgr.roundelement.GetComponentClass, CRoundElement),
        'LevelCtrl': (cl_warmgr.explorelevelctrl.GetComponentClass, CExploreLevelCtrl),
        'NewbieElement': (cl_warmgr.newbieelement.GetComponentClass, CNewbieElement) }
    m_SeasonFuncConfing = { }
    m_AllSeasonElement = { }
    m_NewVerLayer = set()
    m_SeasonElement = { }

