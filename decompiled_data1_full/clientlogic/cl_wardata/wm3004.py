# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/wm3004.pyc
# RelativePath: clientlogic/cl_wardata/wm3004.pyc
# Source Generated with Decompyle++
# File: wm3004.pyc (Python 3.6)

from __future__ import absolute_import
from cl_warmgr.mobject import CWarManager as CCustomWarMgr
from cl_commondefines import GAMETYPE_DESTROY, LAYER_CHOOSE_HIDE, LEVEL_TYPE_BOSS, LEVEL_TYPE_FIGHT, LEVEL_TYPE_HALL, LEVEL_TYPE_HIDE
import cl_msgcenter
import cl_warmgr.waraction as waraction
import cl_warmgr.warcondition as warcondition
import cl_warmgr.testelement
import cl_warmgr.testlevelctrl
import cl_warmgr.pvedieelement
import cl_warmgr.warreport
import cl_warmgr.teaminfoelement
import cl_warmgr.watchelement
import cl_signal

class CTestElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'TESTBULLET': ((4502, 999), (4503, 999), (4504, 999), (4508, 999)),
        'TESTPASSIVE': ((6308, 1), (4100, 1)) }


class CTestLevelCtrl(cl_warmgr.mobject.CElementData):
    m_LevelCtrlConf = {
        1: {
            'CtrlSize': 1,
            'HallInfo': 0,
            'BossInfo': {
                'BossStore': { },
                'BossExtra': { },
                'ChallengeStore': { },
                'SingleChallengeStore': { },
                'ExcludeChallengeArea': { },
                'UnSpawnRuleInfo': { },
                'ChallengeModeLimit': { },
                'AIBosslevelEnhance': { } },
            'NpcInfo': { },
            'CtrlInfo': {
                1: {
                    'Ratio': (100, 0, 0),
                    'NormalStore': (9000002,),
                    'NormalFilter': {
                        9000002: {
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
            'LayerChoose': {
                1: {
                    LAYER_CHOOSE_HIDE: (3, 0, 0, 99, {
                        1: 10 }, { }) },
                2: {
                    LAYER_CHOOSE_HIDE: (3, 0, 0, 99, {
                        1: 10 }, { }) } },
            'BaseGrade': { },
            'MonsterAttAdjust': { },
            'EliteAttAdjust': { },
            'ItemChoose': 1001 } }
    m_LayerAndLevelMap = { }
    m_ChooseItem = {
        1001: {
            (1, 1): {
                'WeaponChoose': (2, 0, 1001),
                'GoldenCupChoose': (1, 0, 4101),
                'RelicChoose': (0, 0, 0) } } }
    m_SightLevelConf = { }


class CPVEDieElement(cl_warmgr.mobject.CElementData):
    pass


class CWarreport(cl_warmgr.mobject.CElementData):
    pass


class CTeamInfoElement(cl_warmgr.mobject.CElementData):
    pass


class CWatchElement(cl_warmgr.mobject.CElementData):
    pass


class CSignalElement(cl_warmgr.mobject.CElementData):
    pass


class CWarManager(CCustomWarMgr):
    m_SID = 3004
    m_StepInfo = { }
    m_InitStep = []
    m_ComponentCls = {
        'TestElement': (cl_warmgr.testelement.GetComponentClass, CTestElement),
        'LevelCtrl': (cl_warmgr.testlevelctrl.GetComponentClass, CTestLevelCtrl),
        'PVEDieElement': (cl_warmgr.pvedieelement.GetComponentClass, CPVEDieElement),
        'Warreport': (cl_warmgr.warreport.GetComponentClass, CWarreport),
        'TeamInfo': (cl_warmgr.teaminfoelement.GetComponentClass, CTeamInfoElement),
        'WatchElement': (cl_warmgr.watchelement.GetComponentClass, CWatchElement),
        'SignalElement': (cl_signal.GetComponentClass, CSignalElement) }
    m_SeasonFuncConfing = { }
    m_AllSeasonElement = { }
    m_NewVerLayer = set()
    m_SeasonElement = { }

