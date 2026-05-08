# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/round/__init__.pyc
# RelativePath: clientlogic/cl_warmgr/round/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_commondefines import ROUND_EXTRULE_REPLACEMONSTER, ROUND_EXTRULE_APPEARCHALLENGE, ROUND_EXTRULE_REPLACECONFIG_CHALLENGE, ROUND_EXTRULE_HIDELEVEL_APPEARCHALLENGE, ROUND_EXTRULE_SMASHOBSTACLE_CREATEMONSTER_LOCKROOM, ROUND_EXTRULE_TRANSOBSTACLE_TO_MONSTER
from . import extrule
g_RoundExtRuleClass = {
    ROUND_EXTRULE_TRANSOBSTACLE_TO_MONSTER: extrule.CRondomTransObstacleToMonster,
    ROUND_EXTRULE_SMASHOBSTACLE_CREATEMONSTER_LOCKROOM: extrule.CSmashObstacleCreateMonsterLockRoom,
    ROUND_EXTRULE_HIDELEVEL_APPEARCHALLENGE: extrule.CHideLevelAppearChallenge,
    ROUND_EXTRULE_REPLACECONFIG_CHALLENGE: extrule.CReplaceConfigChallenge,
    ROUND_EXTRULE_APPEARCHALLENGE: extrule.CAppearChallenge,
    ROUND_EXTRULE_REPLACEMONSTER: extrule.CReplaceMonster }

def NewRoundExtRule(oRoundElement, oGame, iType, dParam):
    if iType not in g_RoundExtRuleClass:
        return None
    oRoundExtRule = g_RoundExtRuleClass[iType](oRoundElement, oGame)
    oRoundExtRule.Init(dParam)
    return oRoundExtRule

