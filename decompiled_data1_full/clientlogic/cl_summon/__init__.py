# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_summon/__init__.pyc
# RelativePath: clientlogic/cl_summon/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_commondefines import WARRIOR_PERFORM, WARRIOR_SUMMON_BUILD, WARRIOR_CIRCLE, WARRIOR_BODYPART, WARRIOR_INKWALL, WARRIOR_BEACON, WARRIOR_MONSTERBEACON, WARRIOR_MOVEEFFECT, WARRIOR_NOPHYSMOVEEFFECT, WARRIOR_SUMMON_BARRIER, WARRIOR_SUMMON_SEED
from cl_commondefines import WARRIOR_SUMMON_AIRFOLLOWEFFECT
from . import mobject
from . import circlesummon
from . import performsummon
from . import bodypartsummon
from . import inkwallsummon
from . import beaconsummon
from . import buildsummon
from . import monsterbeaconsummon
from . import windsummon
from . import windtrapsummon
from . import barriersummon
from . import seedsummon
from . import airfolloweffectsummon
SUMMONTYPEINFO = {
    WARRIOR_SUMMON_AIRFOLLOWEFFECT: airfolloweffectsummon.CAirFollowEffectSummon,
    WARRIOR_SUMMON_SEED: seedsummon.CSeedSummon,
    WARRIOR_SUMMON_BARRIER: barriersummon.CBarrierSummon,
    WARRIOR_NOPHYSMOVEEFFECT: windtrapsummon.CWindTrapSummon,
    WARRIOR_MOVEEFFECT: windsummon.CWindSummon,
    WARRIOR_SUMMON_BUILD: buildsummon.CBuildSummon,
    WARRIOR_MONSTERBEACON: monsterbeaconsummon.CMonsterBeaconSummon,
    WARRIOR_BEACON: beaconsummon.CBeaconSummon,
    WARRIOR_INKWALL: inkwallsummon.CInkWallSummon,
    WARRIOR_BODYPART: bodypartsummon.CBodyPartSummon,
    WARRIOR_CIRCLE: circlesummon.CCirecleSummon,
    WARRIOR_PERFORM: performsummon.CPerformSummon }

def NewSummon(oGame, clsData, dAddData):
    iSummon = oGame.NewNPCID()
    iType = clsData.m_FightType
    if iType in SUMMONTYPEINFO:
        oSummon = SUMMONTYPEINFO[iType](oGame, iSummon)
    else:
        oSummon = mobject.CBaseSummon(oGame, iSummon)
    oSummon.InitSummon(clsData, dAddData)
    return oSummon

