# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/wm3003.pyc
# RelativePath: clientlogic/cl_wardata/wm3003.pyc
# Source Generated with Decompyle++
# File: wm3003.pyc (Python 3.6)

from __future__ import absolute_import
from cl_warmgr.mobject import CWarManager as CCustomWarMgr
from cl_commondefines import LEVEL_TYPE_BOSS, LEVEL_TYPE_FIGHT, LEVEL_TYPE_HALL, LEVEL_TYPE_HIDE
import cl_msgcenter
import cl_warmgr.waraction as waraction
import cl_warmgr.warcondition as warcondition
import cl_warmgr.levelctrl
import cl_warmgr.testelement
import cl_warmgr.warreport
import cl_warmgr.pvedieelement
import cl_warmgr.watchelement

class CLevelCtrlElement(cl_warmgr.mobject.CElementData):
    m_LevelCtrlConf = {
        1: {
            'CtrlSize': 0,
            'HallInfo': 0,
            'BossInfo': {
                'BossStore': {
                    1101006: 20 },
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
            'NpcInfo': { },
            'CtrlInfo': { },
            'LayerChoose': { },
            'BaseGrade': { },
            'MonsterAttAdjust': { },
            'EliteAttAdjust': { },
            'ItemChoose': 0 } }
    m_LayerAndLevelMap = { }
    m_ChooseItem = { }
    m_SightLevelConf = { }


class CTestElement(cl_warmgr.mobject.CElementData):
    m_Config = {
        'TESTTALENT': ((2029, 0, 3), (2030, 0, 3), (2031, 0, 1), (2032, 0, 1), (2033, 0, 3), (2036, 0, 3), (2105, 0, 3), (2108, 0, 3), (2111, 0, 3), (2116, 0, 3), (2120, 0, 1), (2121, 0, 1)) }


class CWarreport(cl_warmgr.mobject.CElementData):
    pass


class CPVEDieElement(cl_warmgr.mobject.CElementData):
    pass


class CWatchElement(cl_warmgr.mobject.CElementData):
    pass


class CWarManager(CCustomWarMgr):
    m_SID = 3003
    m_StepInfo = { }
    m_InitStep = []
    m_ComponentCls = {
        'LevelCtrl': (cl_warmgr.levelctrl.GetComponentClass, CLevelCtrlElement),
        'TestElement': (cl_warmgr.testelement.GetComponentClass, CTestElement),
        'Warreport': (cl_warmgr.warreport.GetComponentClass, CWarreport),
        'PVEDieElement': (cl_warmgr.pvedieelement.GetComponentClass, CPVEDieElement),
        'WatchElement': (cl_warmgr.watchelement.GetComponentClass, CWatchElement) }
    m_SeasonFuncConfing = { }
    m_AllSeasonElement = { }
    m_NewVerLayer = set()
    m_SeasonElement = { }

