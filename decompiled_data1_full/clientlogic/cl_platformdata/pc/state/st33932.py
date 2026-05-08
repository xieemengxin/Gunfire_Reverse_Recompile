# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33932.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33932.pyc
# Source Generated with Decompyle++
# File: st33932.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_math
import cl_war
from cl_only import TraceLog
from cl_platformdata.custom.state.customaction import CustomAction33932 as CustomAction
from cl_commondefines import AFTER_ADDCOUNT, BEFORE_ADDCOUNT
import cl_state
from cl_commondefines import OBJ_ENEMY, STATE_ADD_REFRESHORSYNC, STATE_CLS_ABNORMAL, STATE_EFF_NONE
from cl_newformula import Func404, Func429, Func536

def StateActAction(oTarget, oLifeCycle):
    oLifeCycle.m_Owner.SetMaxCount(oTarget, 5 + oLifeCycle.m_Owner.GetArgValue('MaxCount'))
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_EXECUTE_BEFORE, -1, 1, 0, 0)
    cl_action.StateChangeStateDelayInfo(oTarget, oLifeCycle, (lambda *a: Func429(*a, **{
'sArg': 'Interval' }) // 2), (lambda *a: Func429(*a, **{
'sArg': 'Interval' })), 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateCBSelfAttackerUseOnlyServerPerform(oTarget, oEventCB, 1992, {
        'Att': (lambda *a: Func404(*a) * (Func429(*a, **{
'sArg': 'BaseCountDam' }) + Func429(*a, **{
'sArg': 'BaseTalentDam' })) * (10000 + Func429(*a, **{
'sArg': 'OtherDamMul' }) + Func536(*a) * Func429(*a, **{
'sArg': 'DeBuffDamMul' })) // 10000) })


def CallBack1(oEventCB, oTarget):
    CustomAction(oTarget, oEventCB.GetCBLifeCycle(), {
        'Dis': 20,
        'CDTime': 50,
        'MinSpreadCount': 3,
        'ExtraPerform': 1992,
        'ExtraAttRatio': (lambda *a: Func429(*a, **{
'sArg': 'Spread' })),
        'AddTime': 500,
        'Att': (lambda *a: Func404(*a) * (Func429(*a, **{
'sArg': 'BaseCountDam' }) + Func429(*a, **{
'sArg': 'BaseTalentDam' })) * (10000 + Func429(*a, **{
'sArg': 'OtherDamMul' }) + Func536(*a) * Func429(*a, **{
'sArg': 'DeBuffDamMul' })) // 10000) })


def StateRefreshAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


class CState(cl_state.CState):
    m_SID = 33932
    m_Name = '#NT#毒雾毒气状态'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESHORSYNC
    m_TargetType = OBJ_ENEMY
    m_MinCount = 0
    m_MaxCount = 5
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_OnlyLocalShow = 1
    m_Action = (StateActAction, None)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 100,
        'firsttime': 50 }
    m_RefreshFunc = {
        'action': StateRefreshAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }
    
    def AddCount(self, oTarget, iCnt, iFrame = 0):
        oGame = self.m_Game
        if not oGame:
            return None
        oAttacker = oGame.GetObject(self.m_Attacker)
        if not oAttacker:
            return None
        if iCnt and iFrame != 125:
            TraceLog('err', '%s %s st33932 addcount err %s %s' % (self.m_Game.m_ID, oAttacker.m_PlayerID, iFrame, iCnt))
            iFrame = 125
        if iCnt > 0:
            iTarget = oTarget.m_ID
            dMsgInfo = {
                'AddCount': iCnt,
                'VID': iTarget }
            iOldCount = self.GetCount()
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_FOGPOISON, oAttacker, dMsgInfo, iSub = BEFORE_ADDCOUNT)
            super().AddCount(oTarget, dMsgInfo['AddCount'], iFrame)
            dMsgInfo.update({
                'OldCount': iOldCount,
                'NewCount': self.GetCount() })
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_FOGPOISON, oAttacker, dMsgInfo, iSub = AFTER_ADDCOUNT)
        else:
            super().AddCount(oTarget, iCnt, iFrame)

    
    def SetNextRefreshCountTimer(self, oTarget, iRefreshFrame):
        if self.m_NextRefreshCountFrame == iRefreshFrame:
            return None
        self.m_NextRefreshCountFrame = iRefreshFrame
        oGame = self.m_Game
        iNextFrame = iRefreshFrame - oGame.GetFrameNum()
        if iNextFrame < 0:
            oAttacker = oGame.GetObject(self.m_Attacker)
            if oAttacker:
                TraceLog('err', '%s %s st33932 timer err %s %s' % (oGame.m_ID, oAttacker.m_PlayerID, iNextFrame, iRefreshFrame))
        iLimitCountIdx = self.GetLimitCountIdx()
        oTarget.DelStateTime(iLimitCountIdx)
        oTarget.AddStateTime(iLimitCountIdx, iNextFrame, {
            'SID': self.m_SID })


