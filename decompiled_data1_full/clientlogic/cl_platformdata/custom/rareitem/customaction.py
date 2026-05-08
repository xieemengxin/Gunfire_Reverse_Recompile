# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/custom/rareitem/customaction.pyc
# RelativePath: clientlogic/cl_platformdata/custom/rareitem/customaction.pyc
# Source Generated with Decompyle++
# File: customaction.pyc (Python 3.6)

import cl_object
import cl_formula
from cl_only import PY_FLAG_DEAD
from cl_commondefines import DAM_TYPE_TRUE, DAM_USE_HP, WARRIOR_NORMAL, WARRIOR_ELITE, DAM_USE_ALL, WARRIOR_NORBOX

def CustomAction7005(oTarget, oLifeCycle, dInfo):
    oGame = oTarget.m_Game
    iScene = oTarget.m_Scene
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return None
    oReason = cl_object.reason.CStrReason('customaction7005', None, {
        'DamType': DAM_TYPE_TRUE | DAM_USE_HP })
    oEliteReason = oReason.ExtInfo({
        'DamType': DAM_TYPE_TRUE | DAM_USE_ALL })
    for iMonsterSID in oScene.GetObjectsByType('Monster'):
        oMonster = oGame.GetObject(iMonsterSID, PY_FLAG_DEAD)
        if not oMonster:
            continue
        if oMonster.m_FightType & WARRIOR_ELITE == WARRIOR_ELITE or oMonster.m_FightType & WARRIOR_NORBOX == WARRIOR_NORBOX:
            if 'EliteDam' not in dInfo:
                continue
            iDam = dInfo['EliteDam']
            iDam = cl_formula.GetResultByData(oMonster, iDam, { })
            oMonster.HPModifyDam(0, [
                [
                    iDam,
                    oEliteReason]])
            continue
        if oMonster.m_FightType & WARRIOR_NORMAL == WARRIOR_NORMAL:
            oMonster.HPModifyDam(0, [
                [
                    oMonster.HP(),
                    oReason]])
    

