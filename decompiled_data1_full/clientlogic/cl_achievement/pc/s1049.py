# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/pc/s1049.pyc
# RelativePath: clientlogic/cl_achievement/pc/s1049.pyc
# Source Generated with Decompyle++
# File: s1049.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.AchieveListenWarMgrMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, -1, 0)


def DoCallBackAction0(oEventCB, oListener):
    CustomCBAction(oListener, oEventCB, { })


class CAchieveStat(CCustom):
    m_SID = 1049
    m_Name = '队伍大腿'
    m_TargetValue = 1
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }


def CustomCBAction(oListener, oEventCB, dArgs):
    if oListener.IsDead():
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dRelifed = dMsgInfo.get('Relifed', { })
    if oListener.m_ID in dRelifed:
        return None
    oGame = oListener.m_Game
    lstHero = oGame.m_WarMgr.GetRoomHero()
    iRoomCnt = len(lstHero)
    iDead = len(dRelifed)
    for iHero in lstHero:
        oHero = oGame.GetObject(iHero)
        if oHero and oHero.IsDead():
            iDead += 1
    
    if iDead and iDead >= iRoomCnt - 1:
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)

