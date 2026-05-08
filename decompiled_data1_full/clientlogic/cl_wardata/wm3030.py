# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/wm3030.pyc
# RelativePath: clientlogic/cl_wardata/wm3030.pyc
# Source Generated with Decompyle++
# File: wm3030.pyc (Python 3.6)

from __future__ import absolute_import
from cl_warmgr.mobject import CWarManager as CCustomWarMgr
from cl_commondefines import LAYER_CHOOSE_CHALLENGE, LAYER_CHOOSE_CRAFTSMAN, LAYER_CHOOSE_EVENTNPC, LAYER_CHOOSE_HIDE, LAYER_CHOOSE_SHOP, LEVEL_TYPE_BOSS, LEVEL_TYPE_FIGHT, LEVEL_TYPE_HALL, LEVEL_TYPE_HIDE, MODE_SNOWMOUNTAINS, NPC_INTERVAL_REFRESH, NPC_NOENTITY_REFRESH, NPC_TYPE_CRAFTSMAN, NPC_TYPE_EVENTNPC, NPC_TYPE_GOLDENCUP, NPC_TYPE_SHOP, NWARRIOR_DROP_BULLET, NWARRIOR_DROP_EQUIP, NWARRIOR_DROP_TRIGGER
from cl_newformula import Func201, Func202, Func204, Func205, Func211, Func221, Func230, Func238, Func544, Func572
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
import cl_warmgr.newsurvivorelement
import cl_warmgr.refleshobstacle
import cl_warmgr.rollrelicelement

class CInitResourceElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'INITBULLET': ((4502, 120), (4503, 40), (4504, 16), (4508, 8)) }


class CLevelCtrlElement(cl_warmgr.mobject.CElementData):
    m_LevelCtrlConf = {
        1: {
            'CtrlSize': 1,
            'HallInfo': 0,
            'BossInfo': {
                'BossStore': {
                    7101007: 10 },
                'BossExtra': {
                    7101007: (None, None) },
                'ChallengeStore': { },
                'SingleChallengeStore': { },
                'ExcludeChallengeArea': { },
                'UnSpawnRuleInfo': {
                    7101007: [] },
                'ChallengeModeLimit': { },
                'AIBosslevelEnhance': {
                    7101007: 0 } },
            'NpcInfo': {
                'shop': {
                    1005: 0 },
                'craftsman': {
                    1018: 0 },
                'gscashshop': {
                    1054: 0 } },
            'CtrlInfo': {
                1: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (7201302,),
                    'NormalFilter': {
                        7201302: {
                            'PlayerCnt': 0,
                            'RoundInfo': { },
                            'UnSpawnRuleInfo': [],
                            'ChooseAction': None } },
                    'MediumStore': (),
                    'HardStore': (),
                    'NormalWeight': { },
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
            'LayerChoose': {
                1: {
                    LAYER_CHOOSE_CRAFTSMAN: (0, 0, 0, 99, {
                        1: 10 }, {
                        1: 1 }),
                    LAYER_CHOOSE_SHOP: (0, 0, 0, 99, {
                        1: 10 }, {
                        1: 1 }),
                    LAYER_CHOOSE_EVENTNPC: (0, 0, 0, 99, {
                        1: 10 }, {
                        1: 1 }),
                    LAYER_CHOOSE_CHALLENGE: (0, 0, 0, 99, {
                        1: 10 }, { }),
                    LAYER_CHOOSE_HIDE: (0, 0, 0, 99, {
                        1: 10 }, {
                        1: 1 }) } },
            'BaseGrade': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: (0, 0) },
                    LEVEL_TYPE_FIGHT: {
                        1: (0, 0) },
                    LEVEL_TYPE_BOSS: (1, 0),
                    LEVEL_TYPE_HALL: (0, 0) } },
            'MonsterAttAdjust': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 5500 * 1 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 5500 * 1 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 5500 * 1 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 5500 * 1 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 5500 * 1 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 5500 * 1 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 1500 * 1 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * 30000 * 1 + 0), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 30000 * 1 + 0), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 30000 * 1 + 0), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 2000 * 1 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                        ('MoveSpeed', (lambda *a: (Func204(*a) - 1) * 500 + 0), 0)],
                    LEVEL_TYPE_HALL: [] } },
            'EliteAttAdjust': {
                0: {
                    LEVEL_TYPE_HIDE: {
                        1: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 15000 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_FIGHT: {
                        1: [
                            ('HPMax', (lambda *a: (Func204(*a) - 1) * 11000 * 1 + 0), 0),
                            ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 11000 * 1 + 0), 0),
                            ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 11000 * 1 + 0), 0),
                            ('Att', (lambda *a: (Func204(*a) - 1) * 1500 + 0), 0),
                            ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0)] },
                    LEVEL_TYPE_BOSS: [
                        ('HPMax', (lambda *a: (Func204(*a) - 1) * 20000 * 1 + 0), 0),
                        ('ShieldMax', (lambda *a: (Func204(*a) - 1) * 20000 * 1 + 0), 0),
                        ('ArmorMax', (lambda *a: (Func204(*a) - 1) * 20000 * 1 + 0), 0),
                        ('Att', (lambda *a: (Func204(*a) - 1) * 2000 * 1 + 0), 0),
                        ('Toughness', (lambda *a: (Func204(*a) - 1) * 2000 + 0), 0),
                        ('MoveSpeed', (lambda *a: (Func204(*a) - 1) * 500 + 0), 0)],
                    LEVEL_TYPE_HALL: [] } },
            'ItemChoose': 1001 } }
    m_LayerAndLevelMap = { }
    m_ChooseItem = {
        1001: {
            (1, 1): {
                'WeaponChoose': (0, 0, 1001),
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
                501: 4000 } } }
    m_ExtRule = { }


class CMonsterSuperElement(cl_warmgr.mobject.CElementData):
    m_SuperConfig = {
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
        'Default': {
            LEVEL_TYPE_HIDE: {
                (3, 4): {
                    6101: 0,
                    6102: 0,
                    6103: 0,
                    6107: 0 },
                (3, 3): {
                    6101: 0,
                    6102: 0,
                    6103: 0,
                    6107: 0 },
                (3, 2): {
                    6101: 0,
                    6102: 0,
                    6103: 0,
                    6107: 0 },
                (3, 1): {
                    6101: 0,
                    6102: 0,
                    6103: 0,
                    6107: 0 } },
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
            12013] }


class CRecycleDropElement(cl_warmgr.mobject.CElementData):
    pass


class CCheckCheatElement(cl_warmgr.mobject.CElementData):
    pass


class CHangUpKickElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'TOTALTIME': 120000,
        'CHECKTIME': 2000 }


class CNewSurvivorElement(cl_warmgr.mobject.CElementData):
    m_PhaseConfig = {
        1001: {
            1: {
                'MonsterSuper': {
                    1001: {
                        'TargetMonster': {
                            20021: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1002: {
                        'TargetMonster': {
                            20211: 1,
                            20411: 1,
                            20851: 1,
                            21031: 1,
                            22421: 1,
                            22431: 1,
                            22441: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1003: {
                        'TargetMonster': {
                            21241: 1,
                            21251: 1,
                            21421: 1,
                            21621: 1,
                            21631: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1004: {
                        'TargetMonster': {
                            21221: 1,
                            22011: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 } },
                'MonsterGrade': 1,
                'FightTime': 3000,
                'RestTime': 3000,
                'WarCash': (400, (lambda *a: Func238(*a) * 20)),
                'WeaponArgs': (1, 2),
                'WeaponDrop': (1, 0, 1001),
                'WarGSCash': 20 },
            2: {
                'MonsterSuper': {
                    1001: {
                        'TargetMonster': {
                            20021: 1 },
                        'SuperRatio': 5,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1002: {
                        'TargetMonster': {
                            20211: 1,
                            20411: 1,
                            20851: 1,
                            21031: 1,
                            22421: 1,
                            22431: 1,
                            22441: 1 },
                        'SuperRatio': 5,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1003: {
                        'TargetMonster': {
                            21241: 1,
                            21251: 1,
                            21421: 1,
                            21621: 1,
                            21631: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1004: {
                        'TargetMonster': {
                            21221: 1,
                            22011: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 } },
                'MonsterGrade': 2,
                'FightTime': 4500,
                'RestTime': 3000,
                'WarCash': (600, (lambda *a: Func238(*a) * 20)),
                'WeaponArgs': (2, 2),
                'WeaponDrop': (1, 0, 1001),
                'WarGSCash': 29 },
            3: {
                'MonsterSuper': {
                    1001: {
                        'TargetMonster': {
                            20021: 1 },
                        'SuperRatio': 10,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1002: {
                        'TargetMonster': {
                            20211: 1,
                            20411: 1,
                            20851: 1,
                            21031: 1,
                            22421: 1,
                            22431: 1,
                            22441: 1 },
                        'SuperRatio': 10,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1003: {
                        'TargetMonster': {
                            21241: 1,
                            21251: 1,
                            21421: 1,
                            21621: 1,
                            21631: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1004: {
                        'TargetMonster': {
                            21221: 1,
                            22011: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 } },
                'MonsterGrade': 4,
                'FightTime': 6000,
                'RestTime': 3000,
                'WarCash': (800, (lambda *a: Func238(*a) * 20)),
                'WeaponArgs': (2, 3),
                'WeaponDrop': (1, 0, 1001),
                'WarGSCash': 39 },
            4: {
                'MonsterSuper': {
                    1001: {
                        'TargetMonster': {
                            20021: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1002: {
                        'TargetMonster': {
                            20211: 1,
                            20411: 1,
                            20851: 1,
                            21031: 1,
                            22421: 1,
                            22431: 1,
                            22441: 1 },
                        'SuperRatio': 10,
                        'SuperLimit': ((lambda *a: 1 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1003: {
                        'TargetMonster': {
                            21241: 1,
                            21251: 1,
                            21421: 1,
                            21621: 1,
                            21631: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1004: {
                        'TargetMonster': {
                            21221: 1,
                            22011: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 } },
                'MonsterGrade': 6,
                'FightTime': 6000,
                'RestTime': 3000,
                'WarCash': (1000, (lambda *a: Func238(*a) * 20)),
                'WeaponArgs': (3, 3),
                'WeaponDrop': (1, 0, 1001),
                'WarGSCash': 49 },
            5: {
                'MonsterSuper': {
                    1001: {
                        'TargetMonster': {
                            20021: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1002: {
                        'TargetMonster': {
                            20211: 1,
                            20411: 1,
                            20851: 1,
                            21031: 1,
                            22421: 1,
                            22431: 1,
                            22441: 1 },
                        'SuperRatio': 15,
                        'SuperLimit': ((lambda *a: 1 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1003: {
                        'TargetMonster': {
                            21241: 1,
                            21251: 1,
                            21421: 1,
                            21621: 1,
                            21631: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1004: {
                        'TargetMonster': {
                            21221: 1,
                            22011: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 } },
                'MonsterGrade': 8,
                'FightTime': 0,
                'RestTime': 6000,
                'WarCash': (1500, 0),
                'WeaponArgs': (3, 4),
                'WeaponDrop': (2, 1, 1001),
                'WarGSCash': 60 },
            6: {
                'MonsterSuper': {
                    1001: {
                        'TargetMonster': {
                            20021: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1002: {
                        'TargetMonster': {
                            20211: 1,
                            20411: 1,
                            20851: 1,
                            21031: 1,
                            22421: 1,
                            22431: 1,
                            22441: 1 },
                        'SuperRatio': 20,
                        'SuperLimit': ((lambda *a: 1 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1003: {
                        'TargetMonster': {
                            21241: 1,
                            21251: 1,
                            21421: 1,
                            21621: 1,
                            21631: 1 },
                        'SuperRatio': 20,
                        'SuperLimit': ((lambda *a: 1 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1004: {
                        'TargetMonster': {
                            21221: 1,
                            22011: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 } },
                'MonsterGrade': 18,
                'FightTime': 6000,
                'RestTime': 3000,
                'WarCash': (800, (lambda *a: Func238(*a) * 20)),
                'WeaponArgs': (4, 4),
                'WeaponDrop': (2, 1, 1001),
                'WarGSCash': 73 },
            7: {
                'MonsterSuper': {
                    1001: {
                        'TargetMonster': {
                            20021: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1002: {
                        'TargetMonster': {
                            20211: 1,
                            20411: 1,
                            20851: 1,
                            21031: 1,
                            22421: 1,
                            22431: 1,
                            22441: 1 },
                        'SuperRatio': 25,
                        'SuperLimit': ((lambda *a: 1 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1003: {
                        'TargetMonster': {
                            21241: 1,
                            21251: 1,
                            21421: 1,
                            21621: 1,
                            21631: 1 },
                        'SuperRatio': 25,
                        'SuperLimit': ((lambda *a: 1 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1004: {
                        'TargetMonster': {
                            21221: 1,
                            22011: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 } },
                'MonsterGrade': 24,
                'FightTime': 7500,
                'RestTime': 3000,
                'WarCash': (1000, (lambda *a: Func238(*a) * 20)),
                'WeaponArgs': (5, 5),
                'WeaponDrop': (2, 1, 1001),
                'WarGSCash': 87 },
            8: {
                'MonsterSuper': {
                    1001: {
                        'TargetMonster': {
                            20021: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1002: {
                        'TargetMonster': {
                            20211: 1,
                            20411: 1,
                            20851: 1,
                            21031: 1,
                            22421: 1,
                            22431: 1,
                            22441: 1 },
                        'SuperRatio': 30,
                        'SuperLimit': ((lambda *a: 2 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1003: {
                        'TargetMonster': {
                            21241: 1,
                            21251: 1,
                            21421: 1,
                            21621: 1,
                            21631: 1 },
                        'SuperRatio': 30,
                        'SuperLimit': ((lambda *a: 2 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1004: {
                        'TargetMonster': {
                            21221: 1,
                            22011: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 } },
                'MonsterGrade': 30,
                'FightTime': 9000,
                'RestTime': 3000,
                'WarCash': (1200, (lambda *a: Func238(*a) * 20)),
                'WeaponArgs': (6, 5),
                'WeaponDrop': (2, 1, 1001),
                'WarGSCash': 104 },
            9: {
                'MonsterSuper': {
                    1001: {
                        'TargetMonster': {
                            20021: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1002: {
                        'TargetMonster': {
                            20211: 1,
                            20411: 1,
                            20851: 1,
                            21031: 1,
                            22421: 1,
                            22431: 1,
                            22441: 1 },
                        'SuperRatio': 35,
                        'SuperLimit': ((lambda *a: 2 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1003: {
                        'TargetMonster': {
                            21241: 1,
                            21251: 1,
                            21421: 1,
                            21621: 1,
                            21631: 1 },
                        'SuperRatio': 35,
                        'SuperLimit': ((lambda *a: 2 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1004: {
                        'TargetMonster': {
                            21221: 1,
                            22011: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 } },
                'MonsterGrade': 36,
                'FightTime': 0,
                'RestTime': 6000,
                'WarCash': (2000, 0),
                'WeaponArgs': (7, 5),
                'WeaponDrop': (2, 1, 1001),
                'WarGSCash': 125 },
            10: {
                'MonsterSuper': {
                    1001: {
                        'TargetMonster': {
                            20021: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1002: {
                        'TargetMonster': {
                            20211: 1,
                            20411: 1,
                            20851: 1,
                            21031: 1,
                            22421: 1,
                            22431: 1,
                            22441: 1 },
                        'SuperRatio': 40,
                        'SuperLimit': ((lambda *a: 3 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1003: {
                        'TargetMonster': {
                            21241: 1,
                            21251: 1,
                            21421: 1,
                            21621: 1,
                            21631: 1 },
                        'SuperRatio': 40,
                        'SuperLimit': ((lambda *a: 2 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1004: {
                        'TargetMonster': {
                            21221: 1,
                            22011: 1 },
                        'SuperRatio': 40,
                        'SuperLimit': ((lambda *a: 1 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 } },
                'MonsterGrade': 72,
                'FightTime': 9000,
                'RestTime': 3000,
                'WarCash': (1500, (lambda *a: Func238(*a) * 20)),
                'WeaponArgs': (8, 5),
                'WeaponDrop': (2, 1, 1001),
                'WarGSCash': 153 },
            11: {
                'MonsterSuper': {
                    1001: {
                        'TargetMonster': {
                            20021: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1002: {
                        'TargetMonster': {
                            20211: 1,
                            20411: 1,
                            20851: 1,
                            21031: 1,
                            22421: 1,
                            22431: 1,
                            22441: 1 },
                        'SuperRatio': 45,
                        'SuperLimit': ((lambda *a: 3 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1003: {
                        'TargetMonster': {
                            21241: 1,
                            21251: 1,
                            21421: 1,
                            21621: 1,
                            21631: 1 },
                        'SuperRatio': 45,
                        'SuperLimit': ((lambda *a: 2 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1004: {
                        'TargetMonster': {
                            21221: 1,
                            22011: 1 },
                        'SuperRatio': 45,
                        'SuperLimit': ((lambda *a: 1 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 } },
                'MonsterGrade': 86,
                'FightTime': 12000,
                'RestTime': 3000,
                'WarCash': (1750, (lambda *a: Func238(*a) * 20)),
                'WeaponArgs': (9, 5),
                'WeaponDrop': (2, 1, 1001),
                'WarGSCash': 191 },
            12: {
                'MonsterSuper': {
                    1001: {
                        'TargetMonster': {
                            20021: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1002: {
                        'TargetMonster': {
                            20211: 1,
                            20411: 1,
                            20851: 1,
                            21031: 1,
                            22421: 1,
                            22431: 1,
                            22441: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1003: {
                        'TargetMonster': {
                            21241: 1,
                            21251: 1,
                            21421: 1,
                            21621: 1,
                            21631: 1 },
                        'SuperRatio': 50,
                        'SuperLimit': ((lambda *a: 3 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1004: {
                        'TargetMonster': {
                            21221: 1,
                            22011: 1 },
                        'SuperRatio': 50,
                        'SuperLimit': ((lambda *a: 3 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 } },
                'MonsterGrade': 100,
                'FightTime': 15000,
                'RestTime': 0,
                'WarCash': (2000, (lambda *a: Func238(*a) * 20)),
                'WeaponArgs': (10, 5),
                'WeaponDrop': (2, 1, 1001),
                'WarGSCash': 246 } },
        1002: {
            1: {
                'MonsterSuper': {
                    1001: {
                        'TargetMonster': {
                            20021: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1002: {
                        'TargetMonster': {
                            20211: 1,
                            20411: 1,
                            20851: 1,
                            21031: 1,
                            22421: 1,
                            22431: 1,
                            22441: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1003: {
                        'TargetMonster': {
                            21241: 1,
                            21251: 1,
                            21421: 1,
                            21621: 1,
                            21631: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1004: {
                        'TargetMonster': {
                            21221: 1,
                            22011: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 } },
                'MonsterGrade': 1,
                'FightTime': 3000,
                'RestTime': (lambda *a: 5000 + Func204(*a) * 1000),
                'WarCash': (500, (lambda *a: Func238(*a) * 20)),
                'WeaponArgs': (1, 2),
                'WeaponDrop': (1, 0, 1001),
                'WarGSCash': 20 },
            2: {
                'MonsterSuper': {
                    1001: {
                        'TargetMonster': {
                            20021: 1 },
                        'SuperRatio': 5,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1002: {
                        'TargetMonster': {
                            20211: 1,
                            20411: 1,
                            20851: 1,
                            21031: 1,
                            22421: 1,
                            22431: 1,
                            22441: 1 },
                        'SuperRatio': 5,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1003: {
                        'TargetMonster': {
                            21241: 1,
                            21251: 1,
                            21421: 1,
                            21621: 1,
                            21631: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1004: {
                        'TargetMonster': {
                            21221: 1,
                            22011: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 } },
                'MonsterGrade': 2,
                'FightTime': 4000,
                'RestTime': (lambda *a: 5000 + Func204(*a) * 1000),
                'WarCash': (700, (lambda *a: Func238(*a) * 20)),
                'WeaponArgs': (2, 2),
                'WeaponDrop': (1, 0, 1001),
                'WarGSCash': 29 },
            3: {
                'MonsterSuper': {
                    1001: {
                        'TargetMonster': {
                            20021: 1 },
                        'SuperRatio': 10,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1002: {
                        'TargetMonster': {
                            20211: 1,
                            20411: 1,
                            20851: 1,
                            21031: 1,
                            22421: 1,
                            22431: 1,
                            22441: 1 },
                        'SuperRatio': 10,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1003: {
                        'TargetMonster': {
                            21241: 1,
                            21251: 1,
                            21421: 1,
                            21621: 1,
                            21631: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1004: {
                        'TargetMonster': {
                            21221: 1,
                            22011: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 } },
                'MonsterGrade': 5,
                'FightTime': 5000,
                'RestTime': (lambda *a: 5000 + Func204(*a) * 1000),
                'WarCash': (1000, (lambda *a: Func238(*a) * 20)),
                'WeaponArgs': (2, 3),
                'WeaponDrop': (1, 0, 1001),
                'WarGSCash': 39 },
            4: {
                'MonsterSuper': {
                    1001: {
                        'TargetMonster': {
                            20021: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1002: {
                        'TargetMonster': {
                            20211: 1,
                            20411: 1,
                            20851: 1,
                            21031: 1,
                            22421: 1,
                            22431: 1,
                            22441: 1 },
                        'SuperRatio': 10,
                        'SuperLimit': ((lambda *a: 1 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1003: {
                        'TargetMonster': {
                            21241: 1,
                            21251: 1,
                            21421: 1,
                            21621: 1,
                            21631: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1004: {
                        'TargetMonster': {
                            21221: 1,
                            22011: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 } },
                'MonsterGrade': 10,
                'FightTime': 6000,
                'RestTime': (lambda *a: 5000 + Func204(*a) * 1000),
                'WarCash': (1200, (lambda *a: Func238(*a) * 20)),
                'WeaponArgs': (3, 3),
                'WeaponDrop': (1, 0, 1001),
                'WarGSCash': 49 },
            5: {
                'MonsterSuper': {
                    1001: {
                        'TargetMonster': {
                            20021: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1002: {
                        'TargetMonster': {
                            20211: 1,
                            20411: 1,
                            20851: 1,
                            21031: 1,
                            22421: 1,
                            22431: 1,
                            22441: 1 },
                        'SuperRatio': 15,
                        'SuperLimit': ((lambda *a: 1 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1003: {
                        'TargetMonster': {
                            21241: 1,
                            21251: 1,
                            21421: 1,
                            21621: 1,
                            21631: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1004: {
                        'TargetMonster': {
                            21221: 1,
                            22011: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 } },
                'MonsterGrade': 18,
                'FightTime': 0,
                'RestTime': (lambda *a: 8000 + Func204(*a) * 1000),
                'WarCash': (1800, 0),
                'WeaponArgs': (3, 4),
                'WeaponDrop': (2, 1, 1001),
                'WarGSCash': 60 },
            6: {
                'MonsterSuper': {
                    1001: {
                        'TargetMonster': {
                            20021: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1002: {
                        'TargetMonster': {
                            20211: 1,
                            20411: 1,
                            20851: 1,
                            21031: 1,
                            22421: 1,
                            22431: 1,
                            22441: 1 },
                        'SuperRatio': 20,
                        'SuperLimit': ((lambda *a: 1 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1003: {
                        'TargetMonster': {
                            21241: 1,
                            21251: 1,
                            21421: 1,
                            21621: 1,
                            21631: 1 },
                        'SuperRatio': 20,
                        'SuperLimit': ((lambda *a: 1 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1004: {
                        'TargetMonster': {
                            21221: 1,
                            22011: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 } },
                'MonsterGrade': 50,
                'FightTime': 6000,
                'RestTime': (lambda *a: 5000 + Func204(*a) * 1000),
                'WarCash': (1100, (lambda *a: Func238(*a) * 20)),
                'WeaponArgs': (4, 4),
                'WeaponDrop': (2, 1, 1001),
                'WarGSCash': 73 },
            7: {
                'MonsterSuper': {
                    1001: {
                        'TargetMonster': {
                            20021: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1002: {
                        'TargetMonster': {
                            20211: 1,
                            20411: 1,
                            20851: 1,
                            21031: 1,
                            22421: 1,
                            22431: 1,
                            22441: 1 },
                        'SuperRatio': 25,
                        'SuperLimit': ((lambda *a: 1 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1003: {
                        'TargetMonster': {
                            21241: 1,
                            21251: 1,
                            21421: 1,
                            21621: 1,
                            21631: 1 },
                        'SuperRatio': 25,
                        'SuperLimit': ((lambda *a: 1 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1004: {
                        'TargetMonster': {
                            21221: 1,
                            22011: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 } },
                'MonsterGrade': 85,
                'FightTime': 7500,
                'RestTime': (lambda *a: 5000 + Func204(*a) * 1000),
                'WarCash': (1300, (lambda *a: Func238(*a) * 20)),
                'WeaponArgs': (5, 5),
                'WeaponDrop': (2, 1, 1001),
                'WarGSCash': 87 },
            8: {
                'MonsterSuper': {
                    1001: {
                        'TargetMonster': {
                            20021: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1002: {
                        'TargetMonster': {
                            20211: 1,
                            20411: 1,
                            20851: 1,
                            21031: 1,
                            22421: 1,
                            22431: 1,
                            22441: 1 },
                        'SuperRatio': 30,
                        'SuperLimit': ((lambda *a: 2 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1003: {
                        'TargetMonster': {
                            21241: 1,
                            21251: 1,
                            21421: 1,
                            21621: 1,
                            21631: 1 },
                        'SuperRatio': 30,
                        'SuperLimit': ((lambda *a: 2 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1004: {
                        'TargetMonster': {
                            21221: 1,
                            22011: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 } },
                'MonsterGrade': 145,
                'FightTime': 9000,
                'RestTime': (lambda *a: 5000 + Func204(*a) * 1000),
                'WarCash': (1500, (lambda *a: Func238(*a) * 20)),
                'WeaponArgs': (6, 5),
                'WeaponDrop': (2, 1, 1001),
                'WarGSCash': 104 },
            9: {
                'MonsterSuper': {
                    1001: {
                        'TargetMonster': {
                            20021: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1002: {
                        'TargetMonster': {
                            20211: 1,
                            20411: 1,
                            20851: 1,
                            21031: 1,
                            22421: 1,
                            22431: 1,
                            22441: 1 },
                        'SuperRatio': 35,
                        'SuperLimit': ((lambda *a: 2 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1003: {
                        'TargetMonster': {
                            21241: 1,
                            21251: 1,
                            21421: 1,
                            21621: 1,
                            21631: 1 },
                        'SuperRatio': 35,
                        'SuperLimit': ((lambda *a: 2 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1004: {
                        'TargetMonster': {
                            21221: 1,
                            22011: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 } },
                'MonsterGrade': 250,
                'FightTime': 0,
                'RestTime': (lambda *a: 8000 + Func204(*a) * 1000),
                'WarCash': (2400, 0),
                'WeaponArgs': (7, 5),
                'WeaponDrop': (2, 1, 1001),
                'WarGSCash': 125 },
            10: {
                'MonsterSuper': {
                    1001: {
                        'TargetMonster': {
                            20021: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1002: {
                        'TargetMonster': {
                            20211: 1,
                            20411: 1,
                            20851: 1,
                            21031: 1,
                            22421: 1,
                            22431: 1,
                            22441: 1 },
                        'SuperRatio': 40,
                        'SuperLimit': ((lambda *a: 3 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1003: {
                        'TargetMonster': {
                            21241: 1,
                            21251: 1,
                            21421: 1,
                            21621: 1,
                            21631: 1 },
                        'SuperRatio': 40,
                        'SuperLimit': ((lambda *a: 2 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1004: {
                        'TargetMonster': {
                            21221: 1,
                            22011: 1 },
                        'SuperRatio': 40,
                        'SuperLimit': ((lambda *a: 1 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 } },
                'MonsterGrade': 500,
                'FightTime': 9000,
                'RestTime': (lambda *a: 5000 + Func204(*a) * 1000),
                'WarCash': (2000, (lambda *a: Func238(*a) * 20)),
                'WeaponArgs': (8, 5),
                'WeaponDrop': (2, 1, 1001),
                'WarGSCash': 153 },
            11: {
                'MonsterSuper': {
                    1001: {
                        'TargetMonster': {
                            20021: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1002: {
                        'TargetMonster': {
                            20211: 1,
                            20411: 1,
                            20851: 1,
                            21031: 1,
                            22421: 1,
                            22431: 1,
                            22441: 1 },
                        'SuperRatio': 45,
                        'SuperLimit': ((lambda *a: 3 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1003: {
                        'TargetMonster': {
                            21241: 1,
                            21251: 1,
                            21421: 1,
                            21621: 1,
                            21631: 1 },
                        'SuperRatio': 45,
                        'SuperLimit': ((lambda *a: 2 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1004: {
                        'TargetMonster': {
                            21221: 1,
                            22011: 1 },
                        'SuperRatio': 45,
                        'SuperLimit': ((lambda *a: 1 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 } },
                'MonsterGrade': 700,
                'FightTime': 12000,
                'RestTime': (lambda *a: 5000 + Func204(*a) * 1000),
                'WarCash': (2250, (lambda *a: Func238(*a) * 20)),
                'WeaponArgs': (9, 5),
                'WeaponDrop': (2, 1, 1001),
                'WarGSCash': 191 },
            12: {
                'MonsterSuper': {
                    1001: {
                        'TargetMonster': {
                            20021: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1002: {
                        'TargetMonster': {
                            20211: 1,
                            20411: 1,
                            20851: 1,
                            21031: 1,
                            22421: 1,
                            22431: 1,
                            22441: 1 },
                        'SuperRatio': 0,
                        'SuperLimit': ((lambda *a: 0 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1003: {
                        'TargetMonster': {
                            21241: 1,
                            21251: 1,
                            21421: 1,
                            21621: 1,
                            21631: 1 },
                        'SuperRatio': 50,
                        'SuperLimit': ((lambda *a: 3 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 },
                    1004: {
                        'TargetMonster': {
                            21221: 1,
                            22011: 1 },
                        'SuperRatio': 50,
                        'SuperLimit': ((lambda *a: 3 + ceil(Func204(*a) * 0.5 - 0.5)), (lambda *a: 5 + ceil(Func204(*a) * 0.5 - 0.5))),
                        'SuperGrade': 3 } },
                'MonsterGrade': 1000,
                'FightTime': 15000,
                'RestTime': 0,
                'WarCash': (2500, (lambda *a: Func238(*a) * 20)),
                'WeaponArgs': (10, 5),
                'WeaponDrop': (2, 1, 1001),
                'WarGSCash': 246 } } }
    m_LevelMap = {
        7201301: 1001,
        7201302: 1002 }
    m_NpcConfigMap = {
        1001: 1001,
        1002: 1001 }
    m_NpcConfig = {
        1001: {
            NPC_NOENTITY_REFRESH: {
                'ChooseRule': {
                    NPC_TYPE_GOLDENCUP: {
                        'PutNumber': 1,
                        'PutWeight': {
                            1069: 10 } },
                    NPC_TYPE_CRAFTSMAN: {
                        'PutNumber': 1,
                        'PutWeight': {
                            1064: 10 } },
                    NPC_TYPE_SHOP: {
                        'PutNumber': 1,
                        'PutWeight': {
                            1063: 10 } } },
                'RefreshRule': {
                    1: {
                        'StartTime': 0,
                        'MinDistance': 0,
                        'MaxDistance': 0,
                        'Duration': 0,
                        'IntervalRefershTime': 0,
                        'PhaseIntervalStart': 1,
                        'RemoveOnFight': 1,
                        'RemoveNpcType': [],
                        'ClearMonster': 0,
                        'PutWeight': { } },
                    2: {
                        'StartTime': 0,
                        'MinDistance': 0,
                        'MaxDistance': 0,
                        'Duration': 0,
                        'IntervalRefershTime': 0,
                        'PhaseIntervalStart': 1,
                        'RemoveOnFight': 1,
                        'RemoveNpcType': [],
                        'ClearMonster': 0,
                        'PutWeight': { } },
                    3: {
                        'StartTime': 0,
                        'MinDistance': 0,
                        'MaxDistance': 0,
                        'Duration': 0,
                        'IntervalRefershTime': 0,
                        'PhaseIntervalStart': 1,
                        'RemoveOnFight': 1,
                        'RemoveNpcType': [],
                        'ClearMonster': 0,
                        'PutWeight': { } },
                    4: {
                        'StartTime': 0,
                        'MinDistance': 0,
                        'MaxDistance': 0,
                        'Duration': 0,
                        'IntervalRefershTime': 0,
                        'PhaseIntervalStart': 1,
                        'RemoveOnFight': 1,
                        'RemoveNpcType': [],
                        'ClearMonster': 0,
                        'PutWeight': { } },
                    5: {
                        'StartTime': 0,
                        'MinDistance': 0,
                        'MaxDistance': 0,
                        'Duration': 0,
                        'IntervalRefershTime': 0,
                        'PhaseIntervalStart': 1,
                        'RemoveOnFight': 1,
                        'RemoveNpcType': [],
                        'ClearMonster': 0,
                        'PutWeight': { } },
                    6: {
                        'StartTime': 0,
                        'MinDistance': 0,
                        'MaxDistance': 0,
                        'Duration': 0,
                        'IntervalRefershTime': 0,
                        'PhaseIntervalStart': 1,
                        'RemoveOnFight': 1,
                        'RemoveNpcType': [],
                        'ClearMonster': 0,
                        'PutWeight': { } },
                    7: {
                        'StartTime': 0,
                        'MinDistance': 0,
                        'MaxDistance': 0,
                        'Duration': 0,
                        'IntervalRefershTime': 0,
                        'PhaseIntervalStart': 1,
                        'RemoveOnFight': 1,
                        'RemoveNpcType': [],
                        'ClearMonster': 0,
                        'PutWeight': { } },
                    8: {
                        'StartTime': 0,
                        'MinDistance': 0,
                        'MaxDistance': 0,
                        'Duration': 0,
                        'IntervalRefershTime': 0,
                        'PhaseIntervalStart': 1,
                        'RemoveOnFight': 1,
                        'RemoveNpcType': [],
                        'ClearMonster': 0,
                        'PutWeight': { } },
                    9: {
                        'StartTime': 0,
                        'MinDistance': 0,
                        'MaxDistance': 0,
                        'Duration': 0,
                        'IntervalRefershTime': 0,
                        'PhaseIntervalStart': 1,
                        'RemoveOnFight': 1,
                        'RemoveNpcType': [],
                        'ClearMonster': 0,
                        'PutWeight': { } },
                    10: {
                        'StartTime': 0,
                        'MinDistance': 0,
                        'MaxDistance': 0,
                        'Duration': 0,
                        'IntervalRefershTime': 0,
                        'PhaseIntervalStart': 1,
                        'RemoveOnFight': 1,
                        'RemoveNpcType': [],
                        'ClearMonster': 0,
                        'PutWeight': { } },
                    11: {
                        'StartTime': 0,
                        'MinDistance': 0,
                        'MaxDistance': 0,
                        'Duration': 0,
                        'IntervalRefershTime': 0,
                        'PhaseIntervalStart': 1,
                        'RemoveOnFight': 1,
                        'RemoveNpcType': [],
                        'ClearMonster': 0,
                        'PutWeight': { } },
                    12: {
                        'StartTime': 0,
                        'MinDistance': 0,
                        'MaxDistance': 0,
                        'Duration': 0,
                        'IntervalRefershTime': 0,
                        'PhaseIntervalStart': 1,
                        'RemoveOnFight': 1,
                        'RemoveNpcType': [],
                        'ClearMonster': 0,
                        'PutWeight': { } } } },
            NPC_INTERVAL_REFRESH: {
                'ChooseRule': {
                    NPC_TYPE_EVENTNPC: {
                        'PutNumber': 1,
                        'PutWeight': { } } },
                'RefreshRule': {
                    1: {
                        'StartTime': 0,
                        'MinDistance': 10,
                        'MaxDistance': 30,
                        'Duration': 0,
                        'IntervalRefershTime': 0,
                        'PhaseIntervalStart': 1,
                        'RemoveOnFight': 0,
                        'RemoveNpcType': [],
                        'ClearMonster': 0,
                        'PutWeight': {
                            3205: 10,
                            3209: 5,
                            3212: 5,
                            3215: 10,
                            3216: 5,
                            3217: 10,
                            3218: 0,
                            3201: 5,
                            3202: 10,
                            3223: 5,
                            3224: 5 } },
                    3: {
                        'StartTime': 0,
                        'MinDistance': 10,
                        'MaxDistance': 30,
                        'Duration': 0,
                        'IntervalRefershTime': 0,
                        'PhaseIntervalStart': 0,
                        'RemoveOnFight': 0,
                        'RemoveNpcType': [],
                        'ClearMonster': 0,
                        'PutWeight': {
                            3205: 10,
                            3209: 5,
                            3212: 5,
                            3215: 10,
                            3216: 5,
                            3217: 10,
                            3218: 0,
                            3201: 5,
                            3202: 10,
                            3223: 5,
                            3224: 5 } },
                    5: {
                        'StartTime': 0,
                        'MinDistance': 10,
                        'MaxDistance': 40,
                        'Duration': 0,
                        'IntervalRefershTime': 0,
                        'PhaseIntervalStart': 0,
                        'RemoveOnFight': 0,
                        'RemoveNpcType': [],
                        'ClearMonster': 0,
                        'PutWeight': {
                            3205: 10,
                            3209: 5,
                            3212: 5,
                            3215: 10,
                            3216: 5,
                            3217: 10,
                            3218: 0,
                            3201: 5,
                            3202: 10,
                            3223: 5,
                            3224: 5 } },
                    7: {
                        'StartTime': 0,
                        'MinDistance': 10,
                        'MaxDistance': 40,
                        'Duration': 0,
                        'IntervalRefershTime': 0,
                        'PhaseIntervalStart': 0,
                        'RemoveOnFight': 0,
                        'RemoveNpcType': [],
                        'ClearMonster': 0,
                        'PutWeight': {
                            3205: 10,
                            3209: 5,
                            3212: 5,
                            3215: 10,
                            3216: 5,
                            3217: 10,
                            3218: 0,
                            3201: 5,
                            3202: 10,
                            3223: 5,
                            3224: 5 } },
                    9: {
                        'StartTime': 0,
                        'MinDistance': 10,
                        'MaxDistance': 40,
                        'Duration': 0,
                        'IntervalRefershTime': 0,
                        'PhaseIntervalStart': 0,
                        'RemoveOnFight': 0,
                        'RemoveNpcType': [],
                        'ClearMonster': 0,
                        'PutWeight': {
                            3205: 10,
                            3209: 5,
                            3212: 5,
                            3215: 10,
                            3216: 5,
                            3217: 10,
                            3218: 0,
                            3201: 5,
                            3202: 10,
                            3223: 5,
                            3224: 5 } },
                    11: {
                        'StartTime': 0,
                        'MinDistance': 10,
                        'MaxDistance': 40,
                        'Duration': 0,
                        'IntervalRefershTime': 0,
                        'PhaseIntervalStart': 0,
                        'RemoveOnFight': 0,
                        'RemoveNpcType': [],
                        'ClearMonster': 0,
                        'PutWeight': {
                            3205: 10,
                            3209: 5,
                            3212: 5,
                            3215: 10,
                            3216: 5,
                            3217: 10,
                            3218: 0,
                            3201: 5,
                            3202: 10,
                            3223: 5,
                            3224: 5 } } } } } }
    m_DropSurvivalTime = {
        NWARRIOR_DROP_BULLET: 6000,
        NWARRIOR_DROP_TRIGGER: 9000,
        NWARRIOR_DROP_EQUIP: 30000 }
    m_RareItemConfig = {
        701: {
            'PhaseGroup': [
                9,
                10],
            'RareItemWeight': {
                7005: 10,
                7006: 10,
                7007: 10,
                7004: 10,
                7003: 10,
                7009: 10 },
            'TargetMonster': {
                20211: 1,
                20851: 1,
                21221: 1,
                21241: 1,
                21251: 1,
                21421: 1,
                21621: 1,
                21631: 1,
                22011: 1,
                22421: 1,
                22431: 1,
                22441: 1 },
            'ExpectNum': 1,
            'DropRatio': 250 },
        702: {
            'PhaseGroup': [
                11],
            'RareItemWeight': {
                7005: 10,
                7006: 10,
                7007: 10,
                7004: 10,
                7003: 10,
                7009: 10 },
            'TargetMonster': {
                20211: 1,
                20851: 1,
                21221: 1,
                21241: 1,
                21251: 1,
                21421: 1,
                21621: 1,
                21631: 1,
                22011: 1,
                22421: 1,
                22431: 1,
                22441: 1 },
            'ExpectNum': (lambda *a: ceil(Func204(*a) * 0.25)),
            'DropRatio': 1000 },
        703: {
            'PhaseGroup': [
                22,
                23],
            'RareItemWeight': {
                7005: 10,
                7006: 10,
                7007: 20,
                7004: 10,
                7003: 10,
                7009: 10 },
            'TargetMonster': {
                20211: 1,
                20851: 1,
                21221: 1,
                21241: 1,
                21251: 1,
                21421: 1,
                21621: 1,
                21631: 1,
                22011: 1,
                22421: 1,
                22431: 1,
                22441: 1 },
            'ExpectNum': 1,
            'DropRatio': 500 },
        704: {
            'PhaseGroup': [
                24],
            'RareItemWeight': {
                7005: 10,
                7006: 10,
                7007: 20,
                7004: 10,
                7003: 10,
                7009: 10 },
            'TargetMonster': {
                20211: 1,
                20851: 1,
                21221: 1,
                21241: 1,
                21251: 1,
                21421: 1,
                21621: 1,
                21631: 1,
                22011: 1,
                22421: 1,
                22431: 1,
                22441: 1 },
            'ExpectNum': (lambda *a: ceil(Func204(*a) * 0.25)),
            'DropRatio': 1000 },
        705: {
            'PhaseGroup': [
                6,
                7],
            'RareItemWeight': {
                7005: 10,
                7006: 20,
                7007: 10,
                7004: 10,
                7003: 10,
                7009: 10 },
            'TargetMonster': {
                20211: 1,
                20851: 1,
                21221: 1,
                21241: 1,
                21251: 1,
                21421: 1,
                21621: 1,
                21631: 1,
                22011: 1,
                22421: 1,
                22431: 1,
                22441: 1 },
            'ExpectNum': 1,
            'DropRatio': 250 },
        706: {
            'PhaseGroup': [
                10,
                11],
            'RareItemWeight': {
                7005: 10,
                7006: 20,
                7007: 10,
                7004: 10,
                7003: 10,
                7009: 10 },
            'TargetMonster': {
                20211: 1,
                20851: 1,
                21221: 1,
                21241: 1,
                21251: 1,
                21421: 1,
                21621: 1,
                21631: 1,
                22011: 1,
                22421: 1,
                22431: 1,
                22441: 1 },
            'ExpectNum': 1,
            'DropRatio': 250 },
        707: {
            'PhaseGroup': [
                19,
                20],
            'RareItemWeight': {
                7005: 10,
                7006: 20,
                7007: 10,
                7004: 10,
                7003: 10,
                7009: 10 },
            'TargetMonster': {
                20211: 1,
                20851: 1,
                21221: 1,
                21241: 1,
                21251: 1,
                21421: 1,
                21621: 1,
                21631: 1,
                22011: 1,
                22421: 1,
                22431: 1,
                22441: 1 },
            'ExpectNum': 1,
            'DropRatio': 250 },
        708: {
            'PhaseGroup': [
                23,
                24],
            'RareItemWeight': {
                7005: 10,
                7006: 20,
                7007: 10,
                7004: 10,
                7003: 10,
                7009: 10 },
            'TargetMonster': {
                20211: 1,
                20851: 1,
                21221: 1,
                21241: 1,
                21251: 1,
                21421: 1,
                21621: 1,
                21631: 1,
                22011: 1,
                22421: 1,
                22431: 1,
                22441: 1 },
            'ExpectNum': 1,
            'DropRatio': 250 } }
    m_Config = {
        'REFRESHAREA': [
            1,
            4,
            5,
            7,
            8],
        'REWARD': {
            'TalentMG': 4004,
            'WeaponMG': 1010 },
        'm_RareTalentInfo': {
            'TypeNum': (lambda *a: 10 + Func230(*a) * 10),
            'RefreshCost': (lambda *a: 10 + Func211(*a) * 20),
            'RefreshMaxTimes': 99,
            'DropMiniGm': 4105,
            'DropProb': 10000,
            'DropTimes': 1 },
        'InscriptionConfig': {
            'AdditionalGemini': 1,
            'ExclusiveInscription': 1 },
        'WudiTime': 1500,
        'InitEquipInfo': [
            0,
            1],
        'RemainNotifyCnt': (lambda *a: Func572(*a) + 4),
        'NotifyPhase': [
            1,
            2,
            3,
            4,
            6,
            8,
            10,
            11] }


class CRefleshObstacle(cl_warmgr.mobject.CElementData):
    m_Config = {
        'm_Time': 200,
        'm_TargetTime': 1000,
        'm_TargetDistance': 10 }


class CRollRelicElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'RelicDrop': {
            1: 2421,
            2: 2422,
            4: 2423 },
        'RelicPerform': {
            1: 2424,
            2: 2425,
            4: 2426 } }


class CWarManager(CCustomWarMgr):
    m_SID = 3030
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
        'NewSurvivorElement': (cl_warmgr.newsurvivorelement.GetComponentClass, CNewSurvivorElement),
        'RefleshObstacle': (cl_warmgr.refleshobstacle.GetComponentClass, CRefleshObstacle),
        'RollRelicElement': (cl_warmgr.rollrelicelement.GetComponentClass, CRollRelicElement) }
    m_SeasonFuncConfing = { }
    m_AllSeasonElement = { }
    m_NewVerLayer = set()
    m_SeasonElement = { }

