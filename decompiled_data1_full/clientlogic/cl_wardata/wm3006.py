# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/wm3006.pyc
# RelativePath: clientlogic/cl_wardata/wm3006.pyc
# Source Generated with Decompyle++
# File: wm3006.pyc (Python 3.6)

from __future__ import absolute_import
from cl_warmgr.mobject import CWarManager as CCustomWarMgr
from cl_commondefines import GAMETYPE_DESTROY, LEVEL_TYPE_BOSS, LEVEL_TYPE_FIGHT, LEVEL_TYPE_HALL, LEVEL_TYPE_HIDE
import cl_msgcenter
import cl_warmgr.waraction as waraction
import cl_warmgr.warcondition as warcondition
import cl_warmgr.explorelevelctrl
import cl_warmgr.testelement
import cl_warmgr.warreport
import cl_warmgr.pvedieelement
import cl_warmgr.newbieelement
import cl_warmgr.watchelement

class CExploreLevelCtrl(cl_warmgr.mobject.CElementData):
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
                    'AIlevelEnhance': 0 } },
            'LayerChoose': { },
            'BaseGrade': { },
            'MonsterAttAdjust': { },
            'EliteAttAdjust': { },
            'ItemChoose': 1001 } }
    m_LayerAndLevelMap = { }
    m_ChooseItem = {
        1001: {
            (1, 1): {
                'WeaponChoose': (0, 0, 0),
                'GoldenCupChoose': (0, 0, 0),
                'RelicChoose': (0, 0, 0) } } }
    m_SightLevelConf = { }


class CTestElement(cl_warmgr.mobject.CElementData):
    pass


class CWarreport(cl_warmgr.mobject.CElementData):
    pass


class CPVEDieElement(cl_warmgr.mobject.CElementData):
    pass


class CNewbieElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'INITBULLET': ((4508, 2),),
        'INITPERFORM': (4245,) }


class CWatchElement(cl_warmgr.mobject.CElementData):
    pass


class CWarManager(CCustomWarMgr):
    m_SID = 3006
    m_StepInfo = { }
    m_InitStep = []
    m_ComponentCls = {
        'LevelCtrl': (cl_warmgr.explorelevelctrl.GetComponentClass, CExploreLevelCtrl),
        'TestElement': (cl_warmgr.testelement.GetComponentClass, CTestElement),
        'Warreport': (cl_warmgr.warreport.GetComponentClass, CWarreport),
        'PVEDieElement': (cl_warmgr.pvedieelement.GetComponentClass, CPVEDieElement),
        'NewbieElement': (cl_warmgr.newbieelement.GetComponentClass, CNewbieElement),
        'WatchElement': (cl_warmgr.watchelement.GetComponentClass, CWatchElement) }
    m_SeasonFuncConfing = { }
    m_AllSeasonElement = { }
    m_SeasonElement = { }

