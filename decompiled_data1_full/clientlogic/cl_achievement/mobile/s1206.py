# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/mobile/s1206.pyc
# RelativePath: clientlogic/cl_achievement/mobile/s1206.pyc
# Source Generated with Decompyle++
# File: s1206.pyc (Python 3.6)

from cl_commondefines import ATTACKERSUBMSG_NORMAL
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    if cl_condition.CheckHero(oListener, oLifeCycle, 214):
        cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckFromPointPerform(oListener, oEventCB, 1315, 0, 1) or cl_evcon.CheckFromPointPerform(oListener, oEventCB, 1709, 0, 1):
        CustomCBAction(oListener, oEventCB, {
            'Target': 10 })


class CAchieveStat(CCustom):
    m_SID = 1206
    m_Name = '摄魂夺魄'
    m_TargetValue = 1
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }


def CustomCBAction(oListener, oEventCB, dArgs):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oGame = oListener.m_Game
    iActNum = 0
    oSkill = None
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
    elif 'AID' in dMsgInfo and 'RS' in dMsgInfo:
        oReason = dMsgInfo['RS']
        iActNum = oReason.Query('FromActNum', 0)
        oSkill = oGame.m_SkillMgr.GetSkill(oListener.m_ID, iActNum)
    if oSkill and 'TriggerPerfromActNum' in oSkill.m_Custom:
        iActNum = oSkill.m_Custom['TriggerPerfromActNum']
        oSkill = oGame.m_SkillMgr.GetSkill(oListener.m_ID, iActNum)
    if not oSkill:
        return None
    if 'KillCnt' not in oSkill.m_Collect:
        oSkill.m_Collect['KillCnt'] = 0
    oSkill.m_Collect['KillCnt'] += 1
    iTargetValue = dArgs['Target']
    if oSkill.m_Collect['KillCnt'] == iTargetValue:
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)
        cl_evact.AchieveRewardCheek(oListener, oEventCB, 1011)

