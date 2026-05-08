# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/mobile/s1089.pyc
# RelativePath: clientlogic/cl_achievement/mobile/s1089.pyc
# Source Generated with Decompyle++
# File: s1089.pyc (Python 3.6)

from cl_only import Frame2Time
from cl_commondefines import PLAYMODE_ROGUELIKE, PLAY_TYPE_SINGLE, WARRIOR_ELITE
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    if cl_condition.CheckHero(oListener, oLifeCycle, 205) and cl_condition.CheckWarPlayMode(oListener, oLifeCycle, PLAYMODE_ROGUELIKE) and cl_condition.CheckWarPlayType(oListener, oLifeCycle, PLAY_TYPE_SINGLE):
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.EventCBCheckFromPointState(oListener, oEventCB, 32101) and cl_evcon.CheckVictimFightType(oListener, oEventCB, WARRIOR_ELITE):
        CustomCBAction(oListener, oEventCB, {
            'Time': 1000 })


def DoCallBackAction1(oEventCB, oListener):
    cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)
    cl_evact.AchieveRewardCheek(oListener, oEventCB, 1004)


class CAchieveStat(CCustom):
    m_SID = 1089
    m_Name = '源力锁链'
    m_TargetValue = 1
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }


def CustomCBAction(oListener, oEventCB, dInfo):
    oGame = oListener.m_Game
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oTarget = oGame.GetObject(dMsgInfo['VID'])
    if not oTarget:
        return None
    iCreate = dMsgInfo['CreateFrame']
    iNow = oGame.GetFrameNum()
    iBegin = oTarget.Query('ImmobilizeBegin', 0)
    iEnd = oTarget.Query('ImmobilizeEnd', 0)
    if iBegin and iCreate <= iEnd:
        oTarget.Set('ImmobilizeEnd', max(iEnd, iNow))
    else:
        oTarget.Set('ImmobilizeBegin', iCreate)
        oTarget.Set('ImmobilizeEnd', iNow)
    iContinueImmobilize = oTarget.Query('ImmobilizeEnd') - oTarget.Query('ImmobilizeBegin')
    if Frame2Time(iContinueImmobilize) >= dInfo['Time']:
        cl_action.CommonDirectEventCBFunc(oListener, oEventCB.GetCBLifeCycle(), 1)

