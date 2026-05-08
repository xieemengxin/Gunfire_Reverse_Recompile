# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33446.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33446.pyc
# Source Generated with Decompyle++
# File: st33446.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_platformdata.custom.state.customaction import CustomActionUsePerformByInfo as CustomActionUsePerform
from cl_platformdata.custom.state.customaction import CustomActionCollectSkillInfo as CustomAction
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func429

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 2, 0, 0)


def CallBack0(oEventCB, oTarget):
    if not cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 8608, 0, 0):
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, 1, 'SkillCnt')
        if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'SkillCnt') >= cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func429(*a, **{
'sArg': 'Att' }))):
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'SkillCnt', 0)
            cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 1, None)
        CustomActionUsePerform(oTarget, oEventCB.GetCBLifeCycle(), {
            'Perform': 8608,
            'ChildrenSkill': (lambda *a: Func429(*a, **{
'sArg': 'Cache' })),
            'Att': 30000,
            'Num': 3,
            'DoubleLevel': 2 })


def CallBack2(oEventCB, oTarget):
    CustomAction(oTarget, oEventCB, { })


class CState(cl_state.CState):
    m_SID = 33446
    m_Name = '陨石秘法'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 6
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2 }

