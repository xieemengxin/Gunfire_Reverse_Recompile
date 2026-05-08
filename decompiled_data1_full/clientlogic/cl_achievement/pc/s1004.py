# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/pc/s1004.pyc
# RelativePath: clientlogic/cl_achievement/pc/s1004.pyc
# Source Generated with Decompyle++
# File: s1004.pyc (Python 3.6)

from cl_commondefines import WARRIOR_BOSS
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    CustomCBAction(oListener, oEventCB, {
        'Target': 10 })


class CAchieveStat(CCustom):
    m_SID = 1004
    m_Name = '功亏一篑'
    m_TargetValue = 1
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }


def CustomCBAction(oListener, oEventCB, dArgs):
    oGame = oListener.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oListener.m_Scene)
    if not oScene:
        return None
    iTargetValue = dArgs['Target']
    lstMonster = oScene.GetObjectsByType('Monster')
    for iMonsterID in lstMonster:
        oTarget = oGame.GetObject(iMonsterID)
        if not oTarget or oTarget.m_FightType & WARRIOR_BOSS != WARRIOR_BOSS:
            continue
        iHPPercent = oTarget.HP() * 100 // oTarget.QueryAttr('HPMax')
        if iHPPercent <= iTargetValue:
            cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)
            break
    

