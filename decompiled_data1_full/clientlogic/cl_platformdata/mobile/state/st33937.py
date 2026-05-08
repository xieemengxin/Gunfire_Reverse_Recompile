# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33937.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33937.pyc
# Source Generated with Decompyle++
# File: st33937.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DPSUBMSG_DEFAULT, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func303, Func404, Func429

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DP, DPSUBMSG_DEFAULT, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromMinorPerform(oTarget, oEventCB) and cl_evcon.GetSkillCacheValue(oTarget, oEventCB, 'MaxPFBullet'):
        cl_evact.StateSetSelfCount(oTarget, oEventCB, cl_evcon.GetSkillCacheValue(oTarget, oEventCB, 'MaxPFBullet') // 1000)
        cl_evact.EventSetSkillCache(oTarget, oEventCB, 'st33623_Lucky', (lambda *a: Func429(*a, **{
'sArg': 'LuckyHitRatio' }) * Func404(*a)))
        if cl_evcon.CheckRandom(oTarget, oEventCB, 100, (lambda *a: min(int(Func429(*a, **{
'sArg': 'ExtraDamRatio' }) * Func404(*a)), 100))):
            cl_evact.EventSetSkillCache(oTarget, oEventCB, 'st33623_Copy', 1)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.GetSkillCacheValue(oTarget, oEventCB, 'st33623_Lucky'):
        cl_evact.EventCBChangeLuckyHit(oTarget, oEventCB, (lambda *a: Func303(*a, **{
'sAttr': 'st33623_Lucky' })))
        if cl_evcon.GetSkillCacheValue(oTarget, oEventCB, 'st33623_Copy'):
            cl_evact.EventCBCopyCurPerformDamage(oTarget, oEventCB, (lambda *a: Func303(*a, **{
'sAttr': 'st33623_Copy' })))


class CState(cl_state.CState):
    m_SID = 33937
    m_Name = '能源回收'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_SendExtraInfo = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2 }

